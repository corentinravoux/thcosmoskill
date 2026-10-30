#!/usr/bin/env python3
"""Generality check of a skill: how much of it leans on one group or on the owner.

Plan v2, section 3, "Generality check" (decision D8). Counts every citation
(`arXiv:<id>` or `doi:<doi>`) in the skill's Markdown files, groups them by
the first author (or collaboration) of the cited row in `sources.tsv`, and
reports:

- the share of citations of each first author or collaboration; above 15 %
  is flagged;
- the share of citations of papers the owner co-authored, read from the
  author lists in the arXiv cache of `verify_sources.py`; above 5 % is
  flagged.

A flag is not a failure: it is reviewed at the gate and either justified in
the gate log or rebalanced. Codes and models named in prose are not counted
here; the reviewer reads for them.

    python3 tools/word_share.py --skill thcosmo-lss-perturbation-theory [--owner Ravoux]

Standard library only.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from layout import SKILLS  # noqa: E402

sys.path.insert(0, str(ROOT / SKILLS / "theoretical-cosmology" / "scripts"))
import verify_sources  # noqa: E402

GROUP_LIMIT = 0.15
OWNER_LIMIT = 0.05


def citations(skill: Path) -> Counter:
    counts: Counter = Counter()
    for path in sorted(skill.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for match in verify_sources.ARXIV_CITE.finditer(text):
            counts[match.group(1).lower()] += 1
        for match in verify_sources.DOI_CITE.finditer(text):
            counts["doi:" + match.group(1).rstrip(".").lower()] += 1
    return counts


def shares(skill: Path, owner: str, cache: dict) -> dict:
    rows, _ = verify_sources.read_sources(skill / "references" / "sources.tsv")
    by_id = {row["id"].lower(): row for row in rows}
    counts = citations(skill)
    total = sum(counts.values())
    groups: Counter = Counter()
    owned = 0
    for ident, n in counts.items():
        row = by_id.get(ident)
        groups[row["first_author"] if row else "(no row)"] += n
        authors = cache.get(ident, {}).get("authors", [])
        if owner and any(owner.lower() in author.lower() for author in authors):
            owned += n
    return {"total": total, "groups": groups, "owned": owned}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--skill", required=True)
    parser.add_argument("--owner", default="Ravoux", help="surname of the package owner")
    parser.add_argument("--top", type=int, default=8)
    args = parser.parse_args()
    cache = json.loads(verify_sources.CACHE.read_text(encoding="utf-8")) if verify_sources.CACHE.is_file() else {}
    result = shares(ROOT / SKILLS / args.skill, args.owner, cache)
    total = result["total"] or 1
    print(f"{args.skill}: {result['total']} citations")
    for name, n in result["groups"].most_common(args.top):
        flag = "  FLAG > 15 %" if n / total > GROUP_LIMIT else ""
        print(f"  {100 * n / total:5.1f} %  {n:4}  {name}{flag}")
    owned = result["owned"] / total
    print(f"  owner ({args.owner}) co-authored: {100 * owned:.1f} %" + ("  FLAG > 5 %" if owned > OWNER_LIMIT else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
