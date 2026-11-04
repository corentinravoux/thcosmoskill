#!/usr/bin/env python3
"""Build the re-read sheet of gate G2 for one skill, and compute its error bound.

Plan v2, section 3, step 3 (decision D20). The sheet lists what a second
session re-reads in the cited paper, at the place named:

  1. every statement of `SKILL.md` that holds a number or an equation, and
     every statement of the conventions block of `formalism.md` (the first
     section whose heading contains "Conventions");
  2. every equation that `check_transcription.py` did not class `exact`, and
     every number statement that `check_places.py` did not class
     `found-at-place`;
  3. a random draw of 59 items (or all, if fewer) from those the two tools
     passed, not already in parts 1 and 2.

Pass: no error left in parts 1 and 2, and zero errors in the draw, which
bounds the error rate of tool-passed items below 5 % at 95 % confidence
(one-sided Clopper–Pearson). An error in the draw: fix it, fix the same
pattern across the skill, and draw again with a new seed; log every draw.

    python3 tools/sample_statements.py --skill thcosmo-lss-perturbation-theory --seed 1 [--offline]
    python3 tools/sample_statements.py --bound 0 59          # upper bound for 0 errors in 59
    python3 tools/sample_statements.py --skill thcosmo-x --seed 2 --changed-since HEAD   # deepening run

`--changed-since REV` restricts parts 2 and 3 to the lines added or changed
since that git revision (a deepening run re-reads its new lines only).

Standard library.
"""

from __future__ import annotations

import argparse
import random
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from layout import SKILLS  # noqa: E402
import check_equations  # noqa: E402
import check_numbers  # noqa: E402
import check_places  # noqa: E402
import check_transcription  # noqa: E402

DRAW = 59


def upper_bound(errors: int, n: int, confidence: float = 0.95) -> float:
    """One-sided Clopper–Pearson upper bound on an error rate, by bisection on the binomial CDF."""
    if n == 0:
        return 1.0
    if errors >= n:
        return 1.0
    alpha = 1 - confidence

    def cdf(p: float) -> float:
        term, total = (1 - p) ** n, 0.0
        for k in range(errors + 1):
            if k:
                term *= (n - k + 1) / k * p / (1 - p)
            total += term
        return total

    low, high = 0.0, 1.0
    for _ in range(100):
        middle = (low + high) / 2
        if cdf(middle) > alpha:
            low = middle
        else:
            high = middle
    return high


def conventions_lines(formalism: Path) -> set[int]:
    """Line numbers of the conventions block: the first section whose heading contains 'Conventions'."""
    if not formalism.is_file():
        return set()
    lines, inside, level, found = formalism.read_text(encoding="utf-8").split("\n"), False, 0, set()
    for number, line in enumerate(lines, 1):
        heading = re.match(r"^(#+)\s+(.*)", line)
        if heading:
            if inside and len(heading.group(1)) <= level:
                break
            if not inside and "conventions" in heading.group(2).lower():
                inside, level = True, len(heading.group(1))
            continue
        if inside:
            found.add(number)
    return found


def changed_lines(diff: str) -> dict[str, set[int]]:
    """Lines added or changed, per file, from the text of `git diff -U0`."""
    lines: dict[str, set[int]] = {}
    current = None
    for row in diff.splitlines():
        if row.startswith("+++ "):
            current = row[6:] if row.startswith("+++ b/") else None
        elif row.startswith("@@") and current:
            start, _, count = re.match(r"@@ -\S+ \+(\d+)(,(\d+))? @@", row).groups()
            span = 1 if count is None else int(count)
            lines.setdefault(current, set()).update(range(int(start), int(start) + span))
    return lines


def git_changed_lines(rev: str, skill: Path) -> dict[str, set[int]]:
    diff = subprocess.run(["git", "diff", "-U0", rev, "--", str(skill)], cwd=ROOT,
                          capture_output=True, text=True, check=True).stdout
    return changed_lines(diff)


def sheet(skill: Path, seed: int, offline: bool, only: str = "",
          changed: dict[str, set[int]] | None = None) -> tuple[list[dict], list[dict], list[dict]]:
    skill_md = str((skill / "SKILL.md").relative_to(ROOT) if (skill / "SKILL.md").is_relative_to(ROOT) else skill / "SKILL.md")
    formalism = skill / "references" / "formalism.md"
    formalism_name = str(formalism.relative_to(ROOT) if formalism.is_relative_to(ROOT) else formalism)
    conventions = conventions_lines(formalism)

    def item(record, kind, status):
        return {"file": record["file"], "line": record["line"], "kind": kind, "status": status,
                "text": " ".join(record["text"].split())[:220]}

    numbers = check_numbers.scan(skill)
    eqs = check_equations.scan(skill)
    part1, keys = [], set()
    for record in numbers + eqs:
        key = (record["file"], record["line"])
        in_conventions = record["file"] == formalism_name and record["line"] in conventions
        if (record["file"] == skill_md or in_conventions) and key not in keys:
            keys.add(key)
            part1.append(item(record, "SKILL.md" if record["file"] == skill_md else "conventions", record["status"]))

    part2, passed = [], []
    for record in check_transcription.check(skill, offline):
        key = (record["file"], record["line"])
        entry = {"file": record["file"], "line": record["line"], "kind": "equation", "status": record["class"],
                 "text": f"${record['transcribed'][:200]}$ (arXiv:{record['id']}, Eq. {record['eq']})"}
        if key in keys:
            continue
        (passed if record["class"] == "exact" else part2).append(entry)
    for record in check_places.check(skill, offline, {}):
        key = (record["file"], record["line"])
        entry = {"file": record["file"], "line": record["line"], "kind": "number", "status": record["class"],
                 "text": " ".join(record["text"].split())[:220]}
        if key in keys:
            continue
        (passed if record["class"] == "found-at-place" else part2).append(entry)
    for record in numbers:
        if record["status"] in ("doc",) and (record["file"], record["line"]) not in keys:
            part2.append(item(record, "doc", "doc"))
    if only:
        # Gate G3 re-reads the new files only (for example `--only /deep/`); part 1 stays whole.
        part2 = [e for e in part2 if only in e["file"]]
        passed = [e for e in passed if only in e["file"]]
    if changed is not None:
        # A deepening run re-reads the lines it added or changed; part 1 stays whole.
        part2 = [e for e in part2 if e["line"] in changed.get(e["file"], ())]
        passed = [e for e in passed if e["line"] in changed.get(e["file"], ())]
    rng = random.Random(seed)
    draw = rng.sample(passed, min(DRAW, len(passed)))
    return part1, part2, draw


def render(skill: str, seed: int, parts) -> str:
    titles = ["1. SKILL.md and conventions block (all)", "2. Items the tools could not pass (all)",
              f"3. Random draw from tool-passed items (seed {seed})"]
    out = [f"# G2 re-read sheet — {skill}", "",
           "Re-read each item in the cited paper at the place named (L4). Verdict: `ok`, `wrong` (say what), "
           "`unclear`. Pass: no `wrong` left in parts 1–2 after fixes; zero `wrong` in part 3.", ""]
    for title, items in zip(titles, parts):
        out += [f"## {title}", "", "| # | file:line | kind | tool status | statement | verdict | note |",
                "|---|---|---|---|---|---|---|"]
        for number, entry in enumerate(items, 1):
            text = entry["text"].replace("|", "\\vert ")
            out.append(f"| {number} | {entry['file']}:{entry['line']} | {entry['kind']} | {entry['status']} | {text} | | |")
        out.append("")
    n = len(parts[2])
    out.append(f"Upper bound on the error rate of tool-passed items with 0 errors in {n}: "
               f"{100 * upper_bound(0, n):.1f} % (95 %, one-sided).")
    return "\n".join(out) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--skill")
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--bound", nargs=2, type=int, metavar=("ERRORS", "N"))
    parser.add_argument("--only", default="", help="parts 2 and 3 restricted to files whose path contains this (G3: /deep/)")
    parser.add_argument("--changed-since", metavar="REV",
                        help="parts 2 and 3 restricted to lines added or changed since this git revision")
    args = parser.parse_args()
    if args.bound:
        print(f"{100 * upper_bound(*args.bound):.2f} %")
        return 0
    if not args.skill:
        parser.error("--skill or --bound is required")
    skill = ROOT / SKILLS / args.skill
    changed = git_changed_lines(args.changed_since, skill) if args.changed_since else None
    parts = sheet(skill, args.seed, args.offline, args.only, changed)
    sys.stdout.write(render(args.skill, args.seed, parts))
    return 0


if __name__ == "__main__":
    sys.exit(main())
