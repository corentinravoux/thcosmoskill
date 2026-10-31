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
    wrong-section  the equation matches, but the flag names a section or
                 appendix that does not contain it
    unreadable   no HTML rendering, no equation of that number, an equation
                 printed without LaTeX, a PDF place, an unnumbered display

Each equation is attributed to the paper cited nearest after it in the
statement (else the nearest before), and to the flag that follows it, so a
statement may cite several papers (P0 probe, B14). A display of several rows
or cells is compared with its rows and cells joined in reading order, and the
consecutive math spans of a statement are also compared joined (B6, B15). An
inline place, `[src: Sect. 3, inline, text after Eq. 12]` or `[src: text
after Eq. 12]`, is searched among the inline equations that follow display
12, up to the next numbered display (B10, B13).

`mismatch` and `wrong-section` must be zero at gate G1; `contained` and `unreadable` are re-read
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
from html.parser import HTMLParser
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
LABEL = r"\(?([A-Z]?\.?\d+(?:\.\d+)*[a-z]?)\)?"
EQ_REF = re.compile(rf"\bEq(?:s|uations?)?\.?\s*{LABEL}(?:\s*(?:[–\-]|to|and|,)\s*{LABEL})?")
ROW_NUMBER = re.compile(r"\|\s*\(([A-Z]?\.?\d+(?:\.\d+)*[a-z]?)\)\s*$")
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


class Rendering(HTMLParser):
    """Numbered displays of a LaTeXML rendering, and the inline equations that follow each.

    `displays[label]` is the LaTeX of a numbered display, its rows and cells
    joined in reading order (unnumbered rows before a numbered one belong to
    it); `inline[label]` lists the inline equations after display `label` up to
    the next numbered display; `tagged` counts numbered displays.
    """

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.displays: dict[str, str] = {}
        self.inline: dict[str, list[str]] = {"": []}
        self.table = 0
        self.rows: list[tuple[str, str]] = []
        self.row: list[str] = []
        self.tag = ""
        self.in_tag = False
        self.last = ""
        self.heading: list[str] | None = None
        self.section = ""
        self.sections: dict[str, str] = {}

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        classes = attributes.get("class") or ""
        if tag == "table" and ("ltx_eqn_table" in classes or "ltx_equation" in classes):
            self.table += 1
            if self.table == 1:
                self.rows = []
        elif tag == "tr" and self.table:
            self.row, self.tag = [], ""
        elif tag == "math":
            source = attributes.get("alttext") or ""
            if self.table:
                self.row.append(source)
            elif source:
                self.inline.setdefault(self.last, []).append(source)
        elif tag == "span" and self.table and "ltx_tag_equation" in classes:
            self.in_tag = True
        elif tag in ("h2", "h3", "h4", "h5", "h6"):
            self.heading = []

    def handle_data(self, data):
        if self.in_tag:
            self.tag += data
        elif self.heading is not None:
            self.heading.append(data)

    def handle_endtag(self, tag):
        if tag in ("h2", "h3", "h4", "h5", "h6") and self.heading is not None:
            self.section = " ".join("".join(self.heading).split())
            self.heading = None
        elif tag == "span" and self.in_tag:
            self.in_tag = False
        elif tag == "tr" and self.table:
            self.rows.append(("".join(self.row), self.tag.strip().strip("()")))
        elif tag == "table" and self.table:
            self.table -= 1
            if self.table == 0:
                pending = []
                for latex, label in self.rows:
                    pending.append(latex)
                    if label:
                        self.displays[label] = "".join(pending).strip()
                        self.sections[label] = self.section
                        self.inline.setdefault(label, [])
                        self.last = label
                        pending = []

    @property
    def tagged(self) -> int:
        return len(self.displays)


def load(ident: str, offline: bool, cache: dict):
    """The parsed rendering of a paper, or None when it cannot be read."""
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
    rendering = Rendering()
    rendering.feed(document)
    cache[ident] = rendering
    return rendering


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


FLAG = re.compile(r"\[(?:src|sec):[^\]]*\]")
SECTION = re.compile(r"\b(?:Sects?\.?|Sections?|App\.?|Appendix)\s*([A-Z](?:\.\d+)*|\d+(?:\.\d+)*)(?![\w.]*\d)")


def section_agrees(flag: str, heading: str) -> bool:
    """True when the section or appendix a flag names contains the display (heading number prefix)."""
    named = SECTION.search(flag)
    number = re.match(r"([A-Z](?:\.\d+)*|\d+(?:\.\d+)*)\b", heading or "")
    if not named or not number:
        return True
    want, have = named.group(1).split("."), number.group(1).split(".")
    return have[:len(want)] == want
AFTER = re.compile(rf"(?:text\s+)?after\s+Eq\.?\s*{LABEL}", re.I)


def attribute(text: str, start: int, end: int) -> tuple[str, str]:
    """The paper and the flag of a math span at text[start:end]: nearest after, else nearest before."""
    ids = [(m.start(), m.group(1)) for m in ARXIV.finditer(text)]
    flags = [(m.start(), m.group(0)) for m in FLAG.finditer(text)]
    after_ids = [i for pos, i in ids if pos >= end]
    before_ids = [i for pos, i in ids if pos < start]
    after_flags = [f for pos, f in flags if pos >= end]
    before_flags = [f for pos, f in flags if pos < start]
    ident = after_ids[0] if after_ids else (before_ids[-1] if before_ids else "")
    flag = after_flags[0] if after_flags else (before_flags[-1] if before_flags else "")
    return ident, flag


def check(skill: Path, offline: bool) -> list[dict]:
    papers: dict = {}
    records = []
    for path in check_numbers.skill_files(skill):
        for line, _, statement, caption in check_numbers.statements(path.read_text(encoding="utf-8")):
            if check_equations.NOTATION in statement:
                continue
            text = re.sub(r"`[^`]*`", lambda m: " " * len(m.group(0)), statement)
            spans = [(m.start(), m.end(), next(g for g in m.groups() if g is not None))
                     for m in latex_norm.MATH.finditer(text)]
            spans = [s for s in spans if s[2] in check_equations.equations(statement)]
            if not spans:
                continue
            where = str(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path)
            caption_ids = [m.group(1) for m in ARXIV.finditer(caption)]
            groups: dict[tuple[str, str], list[dict]] = {}
            for start, end, span in spans:
                ident, flag = attribute(text, start, end)
                ident = ident or (caption_ids[0] if len(caption_ids) == 1 else "")
                flag = flag or caption
                record = {"file": where, "line": line, "id": ident, "eq": "", "transcribed": span, "source": ""}
                after = AFTER.search(flag)
                wanted = labels(latex_norm.without_math(flag))
                record["eq"] = after.group(1) if after else ",".join(wanted)
                if not ident or "PDF" in flag or "unnumbered display" in flag or not (after or wanted):
                    record["class"] = "unreadable"
                else:
                    rendering = load(ident, offline, papers)
                    if rendering is None:
                        record["class"] = "unreadable"
                    elif after or re.search(r"\binline\b", flag):
                        pool = rendering.inline.get(after.group(1) if after else "", [])
                        record["class"], record["source"] = compare(span, pool) if pool else ("unreadable", "")
                    else:
                        record["class"], record["source"] = compare(span, [rendering.displays.get(l, "") for l in wanted])
                        heading = rendering.sections.get(wanted[0], "")
                        if record["class"] != "unreadable" and not section_agrees(flag, heading):
                            # The equation number is right but the section named is not (G2 of the atlas).
                            record["class"], record["source"] = "wrong-section", f"display is in: {heading}"
                        groups.setdefault((ident, record["eq"]), []).append(record)
                records.append(record)
            # Rows of one display copied as consecutive spans: compare them joined.
            for (ident, eq), members in groups.items():
                if len(members) > 1 and any(m["class"] != "exact" for m in members):
                    joined = "".join(m["transcribed"] for m in members)
                    rendering = papers.get(ident)
                    sources = [rendering.displays.get(l, "") for l in eq.split(",")] if rendering else []
                    verdict, source = compare(joined, sources)
                    if verdict in ("exact", "contained"):
                        for m in members:
                            m["class"], m["source"] = verdict, source
    return records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--skill", required=True, help="one skill, e.g. thcosmo-lss-perturbation-theory")
    parser.add_argument("--offline", action="store_true", help="read only papers already cached")
    parser.add_argument("--write", action="store_true", help=f"save the report under {REPORTS.relative_to(ROOT)}")
    args = parser.parse_args()
    records = check(ROOT / SKILLS / args.skill, args.offline)
    counts = {name: sum(r["class"] == name for r in records)
              for name in ("exact", "contained", "mismatch", "wrong-section", "unreadable")}
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
    return 1 if counts["mismatch"] or counts["wrong-section"] else 0


if __name__ == "__main__":
    sys.exit(main())
