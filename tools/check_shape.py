#!/usr/bin/env python3
"""Check the shape of a thcosmo-* domain skill (plan v2, step T6).

A domain skill has:

- `SKILL.md`, and in `references/` the five standard files `formalism.md`,
  `models.md`, `results.md`, `approximations.md`, `open-questions.md`, each
  with a `Snapshot: YYYY-MM-DD` line in its first twenty lines;
- `references/sources.tsv` with the header of `verify_sources.COLUMNS`
  (version column included);
- `references/subtopics.tsv` with the header `key, title, from, files,
  status`, statuses `covered`, `thin` or `missing`;
- a first `##` section of `formalism.md` whose heading contains
  "Conventions";
- in `models.md`, every model card (a `###` section) with the six fields of
  `suite-conventions.md#model-cards`, in order, and a valid status date;
- at most six dossiers in `deep/`.

    python3 tools/check_shape.py                    # every thcosmo-* skill
    python3 tools/check_shape.py --skill thcosmo-inflation

Exit status 1 when a problem is found. Standard library only.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from layout import SKILLS  # noqa: E402

sys.path.insert(0, str(ROOT / SKILLS / "theoretical-cosmology" / "scripts"))
import verify_sources  # noqa: E402

REFERENCES = ["formalism.md", "models.md", "results.md", "approximations.md", "open-questions.md"]
SUBTOPIC_COLUMNS = ["key", "title", "from", "files", "status"]
STATUSES = {"covered", "thin", "missing"}
CARD_FIELDS = ["Defining equations", "Parameters", "Predictions", "Consistency", "Observational status", "Status date"]
SNAPSHOT = re.compile(r"\bSnapshot:\s*\**\s*20\d\d-[01]\d-[0-3]\d", re.I)
MAX_DOSSIERS = 6


def card_problems(text: str, name: str = "models.md") -> list[str]:
    """Problems of the model cards of a models.md text."""
    problems = []
    sections = re.split(r"(?m)^### ", text)[1:]
    for section in sections:
        title = section.split("\n", 1)[0].strip()
        fields = re.findall(r"(?m)^- \*\*([^*:]+):\*\*", section)
        wanted = [f for f in fields if f in CARD_FIELDS]
        if wanted != CARD_FIELDS:
            missing = [f for f in CARD_FIELDS if f not in fields]
            problems.append(f"{name}: card '{title}': fields {wanted}, expected {CARD_FIELDS}"
                            + (f" (missing {missing})" if missing else " (order)"))
            continue
        status = re.search(r"(?m)^- \*\*Status date:\*\*\s*(\S+)", section).group(1)
        try:
            date.fromisoformat(status)
        except ValueError:
            problems.append(f"{name}: card '{title}': status date '{status}' is not YYYY-MM-DD")
    return problems


def status_dates(text: str) -> list[tuple[str, date]]:
    """(card title, status date) of each valid card of a models.md text."""
    out = []
    for section in re.split(r"(?m)^### ", text)[1:]:
        match = re.search(r"(?m)^- \*\*Status date:\*\*\s*(\d{4}-\d\d-\d\d)", section)
        if match:
            try:
                out.append((section.split("\n", 1)[0].strip(), date.fromisoformat(match.group(1))))
            except ValueError:
                pass
    return out


def header(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").split("\n", 1)[0].split("\t")


def problems_of(skill: Path) -> list[str]:
    problems = []
    refs = skill / "references"
    if not (skill / "SKILL.md").is_file():
        problems.append("SKILL.md missing")
    for name in REFERENCES:
        path = refs / name
        if not path.is_file():
            problems.append(f"references/{name} missing")
            continue
        head = "\n".join(path.read_text(encoding="utf-8").split("\n")[:20])
        if not SNAPSHOT.search(head):
            problems.append(f"references/{name}: no Snapshot date in its first twenty lines")
    sources = refs / "sources.tsv"
    if not sources.is_file():
        problems.append("references/sources.tsv missing")
    elif header(sources) != verify_sources.COLUMNS:
        problems.append(f"references/sources.tsv: header {header(sources)}, expected {verify_sources.COLUMNS}")
    subtopics = refs / "subtopics.tsv"
    if not subtopics.is_file():
        problems.append("references/subtopics.tsv missing")
    else:
        lines = subtopics.read_text(encoding="utf-8").splitlines()
        if lines[0].split("\t") != SUBTOPIC_COLUMNS:
            problems.append(f"references/subtopics.tsv: header {lines[0].split(chr(9))}, expected {SUBTOPIC_COLUMNS}")
        for number, line in enumerate(lines[1:], 2):
            fields = line.split("\t")
            if len(fields) != len(SUBTOPIC_COLUMNS) or fields[-1].strip() not in STATUSES:
                problems.append(f"references/subtopics.tsv:{number}: five fields, status in {sorted(STATUSES)}")
    formalism = refs / "formalism.md"
    if formalism.is_file():
        first = re.search(r"(?m)^## (.+)$", formalism.read_text(encoding="utf-8"))
        if not first or "conventions" not in first.group(1).lower():
            problems.append("references/formalism.md: the first ## section must be the conventions block")
    models = refs / "models.md"
    if models.is_file():
        problems += card_problems(models.read_text(encoding="utf-8"), "references/models.md")
    deep = skill / "deep"
    dossiers = [p for p in deep.glob("*.md") if not p.name.startswith("_")] if deep.is_dir() else []
    if len(dossiers) > MAX_DOSSIERS:
        problems.append(f"deep/: {len(dossiers)} dossiers, at most {MAX_DOSSIERS}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--skill")
    args = parser.parse_args()
    skills = [ROOT / SKILLS / args.skill] if args.skill else sorted((ROOT / SKILLS).glob("thcosmo-*"))
    total = 0
    for skill in skills:
        problems = problems_of(skill)
        for problem in problems:
            print(f"{skill.name}: {problem}")
        print(f"{skill.name}: {len(problems)} problem(s)")
        total += len(problems)
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
