#!/usr/bin/env python3
"""Compare each transcribed equation of a skill with the equation its source prints.

Plan v2, step T2b (decision D11). A statement holding an equation, an arXiv
identifier and an equation place (`[src: Eq. 45]`, `Eqs. 45–46`) is checked
against the paper's HTML rendering, read through the cache of
`fetch_paper.py`. The LaTeX that arXiv's rendering prints for equation (n)
and the transcribed `$...$` are both normalised by `latex_norm.normalise`
(spacing, style, font-command style, braces around one token), then compared:

    exact        the two are equal
    contained    one is part of the other (one side, one line of a display,
                 or the transcription adds nothing beyond the source's text)
    mismatch     neither: a transcription error, or the wrong equation number
    unreadable   no HTML rendering, no equation of that number, an equation
                 printed without LaTeX, a PDF place, or several papers cited

`mismatch` must be zero at gate G1; `contained` and `unreadable` are re-read
by a person at gate G2 (plan v2, section 3).

    python3 tools/check_transcription.py --skill thcosmo-lss-perturbation-theory
    python3 tools/check_transcription.py --skill thcosmo-lss-perturbation-theory --offline --write

`--offline` reads only papers already in the cache. `--write` saves the
report to `docs/history/tests/transcription/<skill>.tsv`. Exit status 1 when
there is a mismatch. Standard library; network only for papers not cached.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from layout import SKILLS  # noqa: E402
import check_equations  # noqa: E402
import check_numbers  # noqa: E402
import latex_norm  # noqa: E402

sys.path.insert(0, str(ROOT / SKILLS / "theoretical-cosmology" / "scripts"))
import fetch_paper  # noqa: E402

REPORTS = ROOT / "docs" / "history" / "tests" / "transcription"
LABEL = r"\(?([A-Z]?\d+(?:\.\d+)*[a-z]?)\)?"
EQ_REF = re.compile(rf"\bEq(?:s|uations?)?\.?\s*{LABEL}(?:\s*(?:[–\-]|to|and|,)\s*{LABEL})?")
ROW_NUMBER = re.compile(r"\|\s*\(([A-Z]?\d+(?:\.\d+)*[a-z]?)\)\s*$")
ARXIV = re.compile(r"arXiv:\s?(\d{4}\.\d{4,5}|[a-z][a-z\-]+(?:\.[A-Z]{2})?/\d{7})", re.I)
MIN_CONTAINED = 6


def labels(statement: str) -> list[str]:
    """Equation labels named in a statement; a range of plain integers is expanded."""
    found = []
    for match in EQ_REF.finditer(statement):
        first, last = match.group(1), match.group(2)
        found.append(first)
        if last:
            if first.isdigit() and last.isdigit() and 0 < int(last) - int(first) <= 20:
                found += [str(n) for n in range(int(first) + 1, int(last) + 1)]
            else:
                found.append(last)
    return list(dict.fromkeys(found))


def paper_equations(blocks) -> dict[str, str]:
    """{label: LaTeX} of the numbered equations of a parsed rendering; rows of one display are joined."""
    equations, pending = {}, []
    for kind, _, text in blocks:
        if kind != "text" or not text.startswith("|"):
            pending = []
            continue
        number = ROW_NUMBER.search(text)
        body = ROW_NUMBER.sub("", text) if number else text
        cells = [cell.strip() for cell in body.strip().strip("|").split(" | ") if cell.strip()]
        pending.append(" ".join(cells))
        if number:
            equations[number.group(1)] = " ".join(part for part in pending if part).strip()
            pending = []
    return equations


def load(ident: str, offline: bool, cache: dict) -> dict[str, str] | None:
    if ident in cache:
        return cache[ident]
    stored = fetch_paper.CACHE / (ident.replace("/", "_") + ".html")
    if offline and not stored.is_file():
        cache[ident] = None
        return None
    try:
        document, _ = fetch_paper.download(ident, False)
    except SystemExit:
        cache[ident] = None
        return None
    cache[ident] = paper_equations(fetch_paper.parse(document))
    return cache[ident]


def compare(transcribed: str, sources: list[str]) -> tuple[str, str]:
    """Class of a transcribed equation against the source equations it cites, and the closest source."""
    norm = latex_norm.normalise(transcribed)
    readable = [source for source in sources if source]
    if not readable:
        return "unreadable", ""
    best = readable[0]
    for source in readable:
        if latex_norm.normalise(source) == norm:
            return "exact", source
    for source in readable:
        other = latex_norm.normalise(source)
        if min(len(norm), len(other)) >= MIN_CONTAINED and (norm in other or other in norm):
            return "contained", source
    return "mismatch", best


def check(skill: Path, offline: bool) -> list[dict]:
    papers: dict = {}
    records = []
    for path in check_numbers.skill_files(skill):
        for line, _, statement, caption in check_numbers.statements(path.read_text(encoding="utf-8")):
            spans = check_equations.equations(statement)
            if not spans or check_equations.NOTATION in statement:
                continue
            context = re.sub(r"`[^`]*`", " ", statement + " " + caption)
            idents = list(dict.fromkeys(match.group(1) for match in ARXIV.finditer(context)))
            wanted = labels(latex_norm.without_math(context))
            where = str(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path)
            for span in spans:
                record = {"file": where, "line": line, "id": ",".join(idents), "eq": ",".join(wanted),
                          "transcribed": span, "source": ""}
                if len(idents) != 1 or not wanted or "PDF" in context or "unnumbered display" in context:
                    record["class"] = "unreadable"
                else:
                    equations = load(idents[0], offline, papers)
                    if equations is None:
                        record["class"] = "unreadable"
                    else:
                        record["class"], record["source"] = compare(span, [equations.get(label, "") for label in wanted])
                records.append(record)
    return records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--skill", required=True, help="one skill, e.g. thcosmo-lss-perturbation-theory")
    parser.add_argument("--offline", action="store_true", help="read only papers already cached")
    parser.add_argument("--write", action="store_true", help=f"save the report under {REPORTS.relative_to(ROOT)}")
    args = parser.parse_args()
    records = check(ROOT / SKILLS / args.skill, args.offline)
    counts = {name: sum(r["class"] == name for r in records) for name in ("exact", "contained", "mismatch", "unreadable")}
    for record in records:
        if record["class"] != "exact":
            print(f"{record['class']:10} {record['file']}:{record['line']} arXiv:{record['id']} Eq. {record['eq']}\n"
                  f"           file  : {record['transcribed'][:200]}\n"
                  f"           source: {record['source'][:200]}")
    print(f"{args.skill}: {len(records)} equations; " + ", ".join(f"{n} {k}" for k, n in counts.items()))
    if args.write:
        REPORTS.mkdir(parents=True, exist_ok=True)
        out = REPORTS / f"{args.skill}.tsv"
        columns = ["file", "line", "id", "eq", "class", "transcribed", "source"]
        out.write_text("\t".join(columns) + "\n" + "".join(
            "\t".join(str(r[c]).replace("\t", " ") for c in columns) + "\n" for r in records), encoding="utf-8")
        print(f"wrote {out.relative_to(ROOT)}")
    return 1 if counts["mismatch"] else 0


if __name__ == "__main__":
    sys.exit(main())
