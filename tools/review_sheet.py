#!/usr/bin/env python3
"""Build the owner's review sheet of a pilot domain (plan v2, stage 3, step P2).

Twenty items drawn at random, spread across the skill: 8 equations (from any
file), 4 entries of the conventions block of `formalism.md`, 4 statements of
`models.md` or `results.md`, 4 statements of `approximations.md`. The owner
marks each correct / wrong / unclear with a comment, then adds up to five
general remarks.

    python3 tools/review_sheet.py --skill thcosmo-lss-perturbation-theory --seed 1 > review.md

Standard library only.
"""

from __future__ import annotations

import argparse
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from layout import SKILLS  # noqa: E402
import check_equations  # noqa: E402
import check_numbers  # noqa: E402
import sample_statements  # noqa: E402

QUOTA = {"equation": 8, "conventions": 4, "model or result": 4, "approximation": 4}


def pools(skill: Path) -> dict[str, list[dict]]:
    refs = skill / "references"
    conventions = sample_statements.conventions_lines(refs / "formalism.md")
    found = {kind: [] for kind in QUOTA}
    for path in sorted(refs.glob("*.md")):
        for line, _, statement, _ in check_numbers.statements(path.read_text(encoding="utf-8")):
            if len(statement) < 40:
                continue
            item = {"file": f"{skill.name}/references/{path.name}", "line": line, "text": " ".join(statement.split())}
            if check_equations.equations(statement):
                found["equation"].append(item)
            elif path.name == "formalism.md" and line in conventions:
                found["conventions"].append(item)
            elif path.name in ("models.md", "results.md"):
                found["model or result"].append(item)
            elif path.name == "approximations.md":
                found["approximation"].append(item)
    return found


def render(skill: Path, seed: int) -> str:
    rng = random.Random(seed)
    out = [f"# Pilot review — {skill.name}", "",
           "For each item: verdict `correct`, `wrong` or `unclear`, and a comment. Then up to five general remarks "
           "at the end. About two hours.", ""]
    number = 0
    for kind, quota in QUOTA.items():
        pool = pools(skill)[kind]
        chosen = rng.sample(pool, min(quota, len(pool)))
        out += [f"## {kind.capitalize()} ({len(chosen)} of {len(pool)})", ""]
        for item in chosen:
            number += 1
            out += [f"### {number}. {item['file']}:{item['line']}", "", item["text"], "",
                    "- Verdict: ", "- Comment: ", ""]
    out += ["## General remarks", "", "1. ", "2. ", "3. ", "4. ", "5. ", ""]
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--skill", required=True)
    parser.add_argument("--seed", type=int, default=1)
    args = parser.parse_args()
    sys.stdout.write(render(ROOT / SKILLS / args.skill, args.seed))
    return 0


if __name__ == "__main__":
    sys.exit(main())
