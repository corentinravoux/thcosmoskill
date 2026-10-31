#!/usr/bin/env python3
"""Check that each number of a skill appears at the place its flag names.

Plan v2, step T4b. For every statement that `check_numbers.py` classes `ok`
(an identifier and a place) and that cites exactly one arXiv paper, the
numbers written in prose (equations are left to `check_transcription.py`)
are searched in the paper's HTML rendering, read through the cache of
`fetch_paper.py`, or in its abstract:

    found-at-place   every number occurs in the place named: the abstract, a
                     section or appendix (its subsections included), or the
                     blocks that follow the caption of a table or figure, or
                     the rows around an equation
    found-elsewhere  every number occurs in the paper, not all at that place
    not-found        a number does not occur in what could be read
    unreadable       no rendering and the place is not the abstract, several
                     papers cited, a `doi:` source, or a place not recognised

Items `found-at-place` enter the random draw of gate G2; every other item
is re-read by a person (plan v2, section 3).

    python3 tools/check_places.py --skill thcosmo-lss-perturbation-theory [--offline] [--write]

`--write` saves the report to `docs/history/tests/places/<skill>.tsv`.
Standard library; network only for papers and abstracts not cached.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from layout import SKILLS  # noqa: E402
import check_numbers  # noqa: E402
import latex_norm  # noqa: E402
import locate_numbers  # noqa: E402

fetch_paper = locate_numbers.fetch_paper
REPORTS = ROOT / "docs" / "history" / "tests" / "places"
FLAG = re.compile(r"\[(?:src|sec):\s*([^\]]+)\]")
ARXIV = re.compile(r"arXiv:\s?(\d{4}\.\d{4,5}|[a-z][a-z\-]+(?:\.[A-Z]{2})?/\d{7})", re.I)
SECTION = re.compile(r"\b(?:Sects?\.?|Sections?)\s*([A-Z]?\d+(?:\.\d+)*)|\b(?:App\.?|Appendix)\s*([A-Z](?:\.\d+)*)", re.I)
CAPTIONED = re.compile(r"\b(Tables?|Tab\.|Figs?\.?|Figures?)\s*(\d+(?:\.\d+)*)", re.I)
EQUATION = re.compile(r"(?<!after )\bEqs?\.?\s*\(?([A-Z]?\.?\d+(?:\.\d+)*)\)?")
AFTER_EQUATION = re.compile(r"after\s+Eq\.?\s*\(?([A-Z]?\.?\d+(?:\.\d+)*)\)?", re.I)
FOOTNOTE = re.compile(r"\bfootnote\s*(\d+)", re.I)
WINDOW = 60


def places(statement: str) -> list[tuple[str, str]]:
    """The places named in the statement's flags: ('abstract', ''), ('section', '4.2'), ('table', '3'), ..."""
    found = []
    for flag in FLAG.findall(statement):
        if re.search(r"\babstract\b", flag, re.I):
            found.append(("abstract", ""))
        for match in SECTION.finditer(flag):
            found.append(("section", match.group(1) or match.group(2)))
        for match in CAPTIONED.finditer(flag):
            found.append(("table" if match.group(1).lower().startswith("tab") else "figure", match.group(2)))
        for match in EQUATION.finditer(flag):
            found.append(("equation", match.group(1)))
        # Papers without sections (letters): the text after an equation, a footnote (P0 probe, B7).
        for match in AFTER_EQUATION.finditer(flag):
            found.append(("after-equation", match.group(1)))
        for match in FOOTNOTE.finditer(flag):
            found.append(("footnote", match.group(1)))
    return found


def texts_at(place: tuple[str, str], blocks, abstract: str | None) -> list[str]:
    kind, label = place
    if kind == "abstract":
        head = [text for section, text in blocks if section == "abstract"] if blocks else []
        return head + ([abstract] if abstract else [])
    if not blocks:
        return []
    if kind == "section":
        wanted = (f"Sect. {label}", f"App. {label}")
        return [text for section, text in blocks
                if any(section == w or section.startswith(w + ".") for w in wanted)]
    if kind in ("table", "figure"):
        word = "Table" if kind == "table" else "(?:Figure|Fig\\.)"
        caption = re.compile(rf"^(?:{word})\s*{re.escape(label)}\b", re.I)
        out = []
        for index, (_, text) in enumerate(blocks):
            if caption.match(text):
                out += [t for _, t in blocks[max(0, index - WINDOW):index + WINDOW]]
        return out
    if kind == "equation":
        row = re.compile(rf"\|\s*\({re.escape(label)}\)\s*$")
        out = []
        for index, (_, text) in enumerate(blocks):
            if text.startswith("|") and row.search(text):
                out += [t for _, t in blocks[max(0, index - 3):index + 4]]
        return out
    if kind == "after-equation":
        row = re.compile(rf"\|\s*\({re.escape(label)}\)\s*$")
        numbered = re.compile(r"\|\s*\([A-Z]?\d+(?:\.\d+)*[a-z]?\)\s*$")
        for index, (_, text) in enumerate(blocks):
            if text.startswith("|") and row.search(text):
                out = []
                for _, following in blocks[index + 1:]:
                    if following.startswith("|") and numbered.search(following):
                        break
                    out.append(following)
                return out
        return []
    if kind == "footnote":
        return [text for _, text in blocks]
    return []


def prose_numbers(statement: str) -> list[str]:
    text = latex_norm.without_math(re.sub(r"`[^`]*`", " ", statement))
    return [n.lstrip("−-–").replace(",", "") for n in check_numbers.numbers_in(text)]


def check(skill: Path, offline: bool, store: dict) -> list[dict]:
    papers: dict = {}
    out = []
    for record in check_numbers.scan(skill):
        if record["status"] != "ok":
            continue
        numbers = prose_numbers(record["text"])
        if not numbers:
            continue
        item = {"file": record["file"], "line": record["line"], "numbers": " ".join(numbers),
                "place": "; ".join(f"{k} {v}".strip() for k, v in places(record["text"])), "text": record["text"]}
        idents = list(dict.fromkeys(m.group(1) for m in ARXIV.finditer(record["text"])))
        named = places(record["text"])
        if len(idents) != 1 or not named:
            out.append({**item, "id": ",".join(idents), "class": "unreadable"})
            continue
        ident = idents[0]
        if ident not in papers:
            cached = (fetch_paper.CACHE / (ident.replace("/", "_") + ".html")).is_file()
            papers[ident] = locate_numbers.blocks_with_sections(ident) if (cached or not offline) else None
            if papers[ident] is None and not offline:
                locate_numbers.abstract_of(ident, store)
        blocks, abstract = papers[ident], store.get(ident)
        at_place = [text for place in named for text in texts_at(place, blocks, abstract)]
        everywhere = [text for _, text in blocks] if blocks else ([abstract] if abstract else [])
        if not everywhere:
            cls = "unreadable"
        elif at_place and all(any(locate_numbers.contains(t, n) for t in at_place) for n in numbers):
            cls = "found-at-place"
        elif all(any(locate_numbers.contains(t, n) for t in everywhere) for n in numbers):
            cls = "found-elsewhere"
        elif not blocks and any(kind != "abstract" for kind, _ in named):
            cls = "unreadable"
        else:
            cls = "not-found"
        out.append({**item, "id": ident, "class": cls})
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--skill", required=True)
    parser.add_argument("--offline", action="store_true", help="read only papers and abstracts already cached")
    parser.add_argument("--write", action="store_true", help=f"save the report under {REPORTS.relative_to(ROOT)}")
    args = parser.parse_args()
    store_path = locate_numbers.ABSTRACTS
    store = json.loads(store_path.read_text(encoding="utf-8")) if store_path.is_file() else {}
    items = check(ROOT / SKILLS / args.skill, args.offline, store)
    if not args.offline:
        store_path.parent.mkdir(parents=True, exist_ok=True)
        store_path.write_text(json.dumps(store), encoding="utf-8")
    classes = ("found-at-place", "found-elsewhere", "not-found", "unreadable")
    for item in items:
        if item["class"] != "found-at-place":
            print(f"{item['class']:15} {item['file']}:{item['line']} arXiv:{item['id']} [{item['place']}] "
                  f"{item['numbers']}")
    print(f"{args.skill}: {len(items)} statements; "
          + ", ".join(f"{sum(i['class'] == c for i in items)} {c}" for c in classes))
    if args.write:
        REPORTS.mkdir(parents=True, exist_ok=True)
        path = REPORTS / f"{args.skill}.tsv"
        columns = ["file", "line", "id", "place", "numbers", "class", "text"]
        path.write_text("\t".join(columns) + "\n" + "".join(
            "\t".join(str(i[c]).replace("\t", " ")[:300] for c in columns) + "\n" for i in items), encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
