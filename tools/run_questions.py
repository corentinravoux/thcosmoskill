#!/usr/bin/env python3
"""Run evaluation questions in fresh headless Claude Code sessions, with or without thcosmoskill.

Plan v2: step T10 (which skills a question triggers), stage 3 step E2 (the
baseline, skills off) and stage 5 step 4 (Q0, skills on). Each question runs
in its own `claude -p` session, in an empty working directory, with session
persistence off and stdin closed. With `--mode on` the plugin is loaded from
this repository (`--plugin-dir plugin`); with `--mode off` it is not, and the
run is marked `contaminated` if the session lists a thcosmoskill skill
anyway (an install elsewhere).

Recorded per question, appended to the output JSON-lines file: identifier,
mode, date, Claude Code version, model, the answer, the skills invoked (Skill
tool) and skill files read, token usage, cost and duration. Answers are not
printed: a baseline stays unseen until it is graded (plan v2, E2).

The questions file follows the template of plan v2, stage 3:

    ## Q07
    - Domain: thcosmo-primordial-correlators
    - Category: convention check
    - Question: <text>
    - A good answer contains: <text>
    - A bad answer would: <text>

    python3 tools/run_questions.py run --questions Q.md --mode off --out baseline.jsonl
    python3 tools/run_questions.py run --questions Q.md --mode on --out q0.jsonl --only Q01 Q02 Q03
    python3 tools/run_questions.py triggers --questions Q.md --results q0.jsonl
    python3 tools/run_questions.py sheet --questions Q.md --off baseline.jsonl --on q0.jsonl \
        --sheet grading.md --key key.json --seed 7
    python3 tools/run_questions.py score --sheet grading.md --key key.json --off baseline.jsonl --on q0.jsonl

`sheet` pairs each question's two answers, labels them A and B at random
and writes the grading sheet, with the key in a separate file the grader
does not open. `score` reads the graded sheet, unblinds it with the key and
computes the metrics and the go / no-go of plan v2, decision D28: go when
the skills-on answer is better on correctness, or has fewer convention
errors, in at least 60 % of the graded pairs, and causes no more harm than
the baseline.

Standard library; runs the `claude` command, which needs to be installed and
signed in.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugin"
FIELDS = {"domain": "Domain", "category": "Category", "question": "Question",
          "good": "A good answer contains", "bad": "A bad answer would"}
DEFAULT_TOOLS = "Skill Read Grep Glob WebFetch Bash(python3:*)"


def read_questions(path: Path) -> list[dict]:
    questions = []
    for block in re.split(r"(?m)^## ", path.read_text(encoding="utf-8"))[1:]:
        ident = block.split("\n", 1)[0].strip()
        entry = {"id": ident}
        for key, label in FIELDS.items():
            match = re.search(rf"(?ms)^- {re.escape(label)}:\s*(.*?)(?=^- [A-Z][^:\n]*:|\Z)", block)
            entry[key] = " ".join(match.group(1).split()) if match else ""
        if entry["question"]:
            questions.append(entry)
    return questions


def parse_stream(lines) -> dict:
    """Digest a stream-json transcript: model, plugins, skills used, files read, answer, usage."""
    out = {"model": "", "version": "", "plugins": [], "listed": [], "skills": [], "reads": [], "answer": "",
           "usage": {}, "cost_usd": None, "duration_ms": None, "turns": None, "error": False}
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            event = json.loads(line)
        except ValueError:
            continue
        kind = event.get("type")
        if kind == "system" and event.get("subtype") == "init":
            out["model"] = event.get("model", "")
            out["version"] = event.get("claude_code_version", "")
            out["plugins"] = [p.get("name", "") if isinstance(p, dict) else str(p) for p in event.get("plugins", [])]
            out["listed"] = [s for s in event.get("skills", []) if "thcosmo" in str(s)]
        elif kind == "assistant":
            for content in event.get("message", {}).get("content", []):
                if content.get("type") != "tool_use":
                    continue
                if content.get("name") == "Skill":
                    out["skills"].append(content.get("input", {}).get("skill", ""))
                elif content.get("name") == "Read":
                    path = content.get("input", {}).get("file_path", "")
                    if "/skills/" in path:
                        out["reads"].append(path.split("/skills/", 1)[1])
        elif kind == "result":
            out["answer"] = event.get("result", "") or ""
            usage = event.get("usage", {}) or {}
            out["usage"] = {k: usage.get(k, 0) for k in ("input_tokens", "cache_creation_input_tokens",
                                                       "cache_read_input_tokens", "output_tokens")}
            out["cost_usd"] = event.get("total_cost_usd")
            out["duration_ms"] = event.get("duration_ms")
            out["turns"] = event.get("num_turns")
            out["error"] = bool(event.get("is_error"))
    return out


def run_one(question: dict, mode: str, tools: str, timeout: int) -> dict:
    command = ["claude", "-p", question["question"], "--output-format", "stream-json", "--verbose",
               "--no-session-persistence", "--allowed-tools", tools]
    if mode == "on":
        command += ["--plugin-dir", str(PLUGIN)]
    with tempfile.TemporaryDirectory() as work:
        try:
            result = subprocess.run(command, cwd=work, stdin=subprocess.DEVNULL, capture_output=True, text=True,
                                    timeout=timeout)
            digest = parse_stream(result.stdout.splitlines())
            digest["exit"] = result.returncode
        except subprocess.TimeoutExpired:
            digest = parse_stream([])
            digest["exit"], digest["error"] = "timeout", True
    digest["contaminated"] = mode == "off" and bool(digest["listed"])
    return {"id": question["id"], "mode": mode, "date": time.strftime("%Y-%m-%d %H:%M"), **digest}


def run(args) -> int:
    questions = read_questions(args.questions)
    if args.only:
        questions = [q for q in questions if q["id"] in set(args.only)]
    done = set()
    if args.out.is_file():
        done = {(json.loads(line)["id"], json.loads(line)["mode"]) for line in args.out.read_text(encoding="utf-8").splitlines() if line.strip()}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    for question in questions:
        if (question["id"], args.mode) in done and not args.again:
            print(f"{question['id']}: already in {args.out}; skipped (use --again)")
            continue
        record = run_one(question, args.mode, args.allowed_tools, args.timeout)
        with args.out.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
        tokens = sum(record["usage"].values()) if record["usage"] else 0
        flag = " CONTAMINATED" if record["contaminated"] else ""
        print(f"{question['id']} [{args.mode}] model {record['model']}: skills {record['skills'] or '-'}; "
              f"{tokens} tokens; exit {record['exit']}{flag}")
    return 0


def triggers(args) -> int:
    questions = {q["id"]: q for q in read_questions(args.questions)}
    rows = [json.loads(line) for line in args.results.read_text(encoding="utf-8").splitlines() if line.strip()]
    hit = 0
    for row in rows:
        expected = questions.get(row["id"], {}).get("domain", "")
        used = [s.split(":", 1)[-1] for s in row["skills"]] + [r.split("/", 1)[0].split(":", 1)[-1] for r in row["reads"]]
        ok = bool(expected) and expected in used
        hit += ok
        print(f"{row['id']:6} [{row['mode']}] expected {expected or '-':40} used {sorted(set(used)) or '-'}"
              + ("" if ok else "  MISS"))
    print(f"{hit} of {len(rows)} runs used the expected skill")
    return 0


GRADE_FIELDS = {
    "better": "Better on correctness (A, B or tie)",
    "conv_a": "Convention errors in A (number)",
    "conv_b": "Convention errors in B (number)",
    "stale": "Stale claim caught by (A, B, both, neither, n.a.)",
    "harm_a": "Harm in A (none, false no-material, wrong refusal, citation flood, other: ...)",
    "harm_b": "Harm in B (none, false no-material, wrong refusal, citation flood, other: ...)",
}


def records(path: Path) -> dict[str, dict]:
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    return {row["id"]: row for row in rows}


def sheet(args) -> int:
    import random
    questions = read_questions(args.questions)
    off, on = records(args.off), records(args.on)
    rng = random.Random(args.seed)
    key, out = {}, ["# Q0 grading sheet", "",
                    "Grade each pair without opening the key file. Fill every field after the colon.", ""]
    for question in questions:
        if question["id"] not in off or question["id"] not in on:
            continue
        pair = [("on", on[question["id"]]["answer"]), ("off", off[question["id"]]["answer"])]
        rng.shuffle(pair)
        key[question["id"]] = {"A": pair[0][0], "B": pair[1][0]}
        out += [f"## {question['id']}", "", f"**Category:** {question['category']}", "",
                f"**Question:** {question['question']}", "",
                f"**A good answer contains:** {question['good']}", "",
                f"**A bad answer would:** {question['bad']}", "",
                "### Answer A", "", pair[0][1].strip() or "(empty)", "",
                "### Answer B", "", pair[1][1].strip() or "(empty)", "",
                "### Grades", ""] + [f"- {label}: " for label in GRADE_FIELDS.values()] + [""]
    args.sheet.write_text("\n".join(out) + "\n", encoding="utf-8")
    args.key.write_text(json.dumps(key, indent=1) + "\n", encoding="utf-8")
    print(f"{len(key)} pairs written to {args.sheet}; key in {args.key} (do not open before grading)")
    return 0


def read_grades(path: Path) -> dict[str, dict]:
    grades = {}
    for block in re.split(r"(?m)^## ", path.read_text(encoding="utf-8"))[1:]:
        ident = block.split("\n", 1)[0].strip()
        part = block.split("### Grades", 1)[-1]
        entry = {}
        for field, label in GRADE_FIELDS.items():
            match = re.search(rf"(?m)^- {re.escape(label)}:[ \t]*(.*)$", part)
            entry[field] = match.group(1).strip() if match else ""
        grades[ident] = entry
    return grades


def harmful(value: str) -> bool:
    return bool(value) and value.lower() != "none"


def number(value: str) -> int:
    match = re.match(r"\d+", value.strip())
    return int(match.group(0)) if match else 0


def score(args) -> int:
    grades, key = read_grades(args.sheet), json.loads(args.key.read_text(encoding="utf-8"))
    off, on = records(args.off), records(args.on)
    graded = wins = harm_on = harm_off = conv_on = conv_off = 0
    stale = {"on": 0, "off": 0, "asked": 0}
    for ident, grade in grades.items():
        if ident not in key or not grade["better"]:
            continue
        label_on = "A" if key[ident]["A"] == "on" else "B"
        label_off = "B" if label_on == "A" else "A"
        c_on = number(grade["conv_a" if label_on == "A" else "conv_b"])
        c_off = number(grade["conv_a" if label_off == "A" else "conv_b"])
        better = grade["better"].strip().upper()[:1]
        graded += 1
        wins += better == label_on or c_on < c_off
        conv_on, conv_off = conv_on + c_on, conv_off + c_off
        harm_on += harmful(grade["harm_a" if label_on == "A" else "harm_b"])
        harm_off += harmful(grade["harm_a" if label_off == "A" else "harm_b"])
        caught = grade["stale"].strip().lower()
        if caught and caught not in ("n.a.", "na", "n/a"):
            stale["asked"] += 1
            stale["on"] += caught == "both" or caught.upper() == label_on
            stale["off"] += caught == "both" or caught.upper() == label_off

    def median_tokens(rows):
        values = sorted(sum(r["usage"].values()) for r in rows.values() if r.get("usage"))
        return values[len(values) // 2] if values else 0

    share = wins / graded if graded else 0.0
    go = graded > 0 and share >= 0.6 and harm_on <= harm_off
    print(f"graded pairs: {graded}")
    print(f"skills on better on correctness or with fewer convention errors: {wins} ({100 * share:.0f} %)")
    print(f"convention errors: on {conv_on}, off {conv_off}")
    print(f"stale claims caught (of {stale['asked']} asked): on {stale['on']}, off {stale['off']}")
    print(f"answers with harm: on {harm_on}, off {harm_off}")
    print(f"median tokens per answer: on {median_tokens(on)}, off {median_tokens(off)}")
    print(f"decision (D28): {'GO' if go else 'NO-GO'}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    one = sub.add_parser("run", help="run questions in headless sessions")
    one.add_argument("--questions", type=Path, required=True)
    one.add_argument("--mode", choices=["on", "off"], required=True)
    one.add_argument("--out", type=Path, required=True)
    one.add_argument("--only", nargs="*")
    one.add_argument("--again", action="store_true", help="run again questions already in the output")
    one.add_argument("--allowed-tools", default=DEFAULT_TOOLS)
    one.add_argument("--timeout", type=int, default=900)
    two = sub.add_parser("triggers", help="which skills each run used, against the expected domain")
    two.add_argument("--questions", type=Path, required=True)
    two.add_argument("--results", type=Path, required=True)
    three = sub.add_parser("sheet", help="blind grading sheet and its key")
    three.add_argument("--questions", type=Path, required=True)
    three.add_argument("--off", type=Path, required=True)
    three.add_argument("--on", type=Path, required=True)
    three.add_argument("--sheet", type=Path, required=True)
    three.add_argument("--key", type=Path, required=True)
    three.add_argument("--seed", type=int, default=7)
    four = sub.add_parser("score", help="unblind a graded sheet and compute the metrics and the decision")
    four.add_argument("--sheet", type=Path, required=True)
    four.add_argument("--key", type=Path, required=True)
    four.add_argument("--off", type=Path, required=True)
    four.add_argument("--on", type=Path, required=True)
    args = parser.parse_args()
    return {"run": run, "triggers": triggers, "sheet": sheet, "score": score}[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
