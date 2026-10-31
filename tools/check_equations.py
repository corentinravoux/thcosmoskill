#!/usr/bin/env python3
"""List the equations of the skills that do not name their paper and equation.

Rule (plan v2, step T2; decisions D10–D12): every equation in a skill file is
transcribed from a paper and names it (`arXiv:` or `doi:`) and the equation
number read (`[src: Eq. 45]`). An unnumbered display is placed as
`[src: Sect. 3.2, unnumbered display after Eq. 12]`. A math span that only
defines a symbol or names an object carries `<!-- eq: notation -->`.

An equation is a math span (`$...$`, `$$...$$`, `\\[...\\]`) that states a
relation: =, \\equiv, \\propto, \\simeq, \\approx, \\sim, <, >, \\ll, \\gg,
\\leq, \\geq, \\to. An inequality whose one side is a bare number
(`$k<0.2$`) is a value, left to `check_numbers.py`. A statement is a table
row, a list item or a paragraph, as in `check_numbers.py`; a display block
belongs to the paragraph it sits in. Each statement holding at least one
equation is classed

    ok          an identifier, and an equation place (`Eq. n`, `Eqs. n–m`),
                the words "unnumbered display", or an inline place
                (`[src: Sect. 3, inline, text after Eq. 12]`)
    doc         a valid `[doc: …]` flag: a code fact, such as a default setting
    notation    carries `<!-- eq: notation -->` (counted, passes)
    no-eq       an identifier and a place, but not an equation place
    no-place    an identifier and no place
    no-paper    a place and no identifier
    none        neither
    table-pipe  a table row whose cell holds an odd number of `$`: a `|` inside
                `$…$` broke the row (write \\lvert…\\rvert, \\vert)

    python3 tools/check_equations.py                       # one line per skill
    python3 tools/check_equations.py --skill thcosmo-inflation --list
    python3 tools/check_equations.py --check               # exit 1 above the baseline
    python3 tools/check_equations.py --write-baseline

Standard library only.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from layout import SKILLS  # noqa: E402
import check_numbers  # noqa: E402
import latex_norm  # noqa: E402

BASELINE = Path(__file__).resolve().parent / "equations-baseline.tsv"
NOTATION = "<!-- eq: notation -->"
EQ_PLACE = re.compile(r"\bEqs?\.?\s*\(?\d|\bEquations?\s*\(?\d|unnumbered display|\binline\b", re.I)
INEQUALITY = re.compile(r"<|>|\\leq?(?![A-Za-z])|\\geq?(?![A-Za-z])|\\ll(?![A-Za-z])|\\gg(?![A-Za-z])")
BARE_NUMBER = re.compile(r"^[−\-]?\s*\d+(?:\.\d+)?\s*(?:[A-Za-z/\s]*)$")
PASSING = {"ok", "doc", "notation"}


def value_inequality(latex: str) -> bool:
    """An inequality with a bare number on one side, such as `k<0.2\\,h/Mpc`: a value, not an equation."""
    if latex_norm.RELATION.findall(latex) and all(INEQUALITY.fullmatch(r) for r in latex_norm.RELATION.findall(latex)):
        sides = INEQUALITY.split(latex_norm.SPACING.sub(" ", latex))
        return any(BARE_NUMBER.match(re.sub(r"[{}]", " ", latex_norm.structure_free(side)).strip()) for side in sides)
    return False


def equations(statement: str) -> list[str]:
    text = re.sub(r"`[^`]*`", " ", statement)
    return [span for span in latex_norm.spans(text) if latex_norm.is_equation(span) and not value_inequality(span)]


def table_pipe(statement: str) -> bool:
    if not statement.startswith("|"):
        return False
    cells = re.sub(r"`[^`]*`", " ", statement).strip().strip("|").split("|")
    return any(len(re.findall(r"(?<!\\)\$", cell)) % 2 for cell in cells)


def classify(statement: str, caption: str) -> str:
    if table_pipe(statement):
        return "table-pipe"
    if NOTATION in statement:
        return "notation"
    context = re.sub(r"`[^`]*`", " ", statement + " " + caption)
    if check_numbers.doc_dates(context):
        return "doc"
    has_ident = bool(check_numbers.IDENT.search(context))
    has_eq = bool(EQ_PLACE.search(context))
    has_place = has_eq or bool(check_numbers.PLACE.search(context))
    if has_ident and has_eq:
        return "ok"
    if has_ident and has_place:
        return "no-eq"
    if has_ident:
        return "no-place"
    if has_place:
        return "no-paper"
    return "none"


def scan(skill: Path) -> list[dict]:
    found = []
    for path in check_numbers.skill_files(skill):
        for line, last, statement, caption in check_numbers.statements(path.read_text(encoding="utf-8")):
            spans = equations(statement)
            if not spans and not table_pipe(statement):
                continue
            found.append({"file": str(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path),
                          "line": line, "status": classify(statement, caption), "equations": spans,
                          "text": statement})
    return found


def read_baseline() -> dict[str, int]:
    if not BASELINE.is_file():
        return {}
    rows = [line.split("\t") for line in BASELINE.read_text(encoding="utf-8").splitlines()[1:] if line.strip()]
    return {row[0]: int(row[1]) for row in rows}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--skill", help="one skill, e.g. thcosmo-inflation")
    parser.add_argument("--list", action="store_true", help="list the statements that do not pass")
    parser.add_argument("--status", help="with --list, list this status instead (e.g. notation)")
    parser.add_argument("--check", action="store_true", help="exit 1 if a skill is above the baseline")
    parser.add_argument("--write-baseline", action="store_true")
    args = parser.parse_args()
    skills = [ROOT / SKILLS / args.skill] if args.skill else sorted(
        path for path in (ROOT / SKILLS).iterdir() if (path / "references").is_dir())
    baseline, above, rows = read_baseline(), [], []
    for skill in skills:
        records = scan(skill)
        failing = [r for r in records if r["status"] not in PASSING]
        notation = sum(r["status"] == "notation" for r in records)
        rows.append((skill.name, len(failing)))
        if args.list:
            wanted = [r for r in records if r["status"] == args.status] if args.status else failing
            for record in wanted:
                print(f"{record['file']}:{record['line']}: {record['status']}: {record['text'][:160]}")
        else:
            print(f"{skill.name:40} {len(records):4} statements with equations, {len(failing):4} without paper and "
                  f"equation, {notation:3} notation")
        if len(failing) > baseline.get(skill.name, 0):
            above.append(skill.name)
    if args.write_baseline:
        BASELINE.write_text("skill\twithout_paper_and_equation\n" + "".join(f"{n}\t{c}\n" for n, c in rows),
                            encoding="utf-8")
        print(f"wrote {BASELINE.relative_to(ROOT)}")
    if args.check and above:
        print("above the baseline: " + ", ".join(above))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
