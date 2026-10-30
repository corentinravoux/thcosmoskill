#!/usr/bin/env python3
"""Check a thcosmo-* skill's bibliography against arXiv.

For one or more skill directories, verify that

  1. every row of references/sources.tsv with an arXiv ID names a paper that
     exists, with a matching title and first author;
  2. every ``arXiv:<id>`` or ``doi:<doi>`` cited in the skill's Markdown files
     has a row in sources.tsv, and every row is cited at least once;
  3. the arXiv version a row records (`version` column, `v2`) is the latest:
     when arXiv holds a newer one, a warning is printed (not a problem), since
     the places given may have moved.

The `version` column (plan v2, decision D13) is optional in a table written
before it existed: such a table is read with the version `-`, unknown.

A skill without a `references/` directory is a workflow skill with no
bibliography (`thcosmoskill-refine`) and is skipped. Standard library only.
Exit status 0 when nothing is wrong, 1 otherwise.

    python3 verify_sources.py <skill-dir> [<skill-dir> ...] [--offline]
"""

from __future__ import annotations

import argparse
import csv
import difflib
import errno
import json
import os
import re
import socket
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

API = "https://export.arxiv.org/api/query"
ATOM = {"a": "http://www.w3.org/2005/Atom"}
BATCH = 40
PAUSE = 3.1  # arXiv asks for one request every three seconds
COLUMNS = ["key", "id", "version", "first_author", "year", "title", "role"]
LEGACY_COLUMNS = ["key", "id", "first_author", "year", "title", "role"]
VERSION = re.compile(r"^(?:v\d+|-)$")
# Theory adds textbook, lectures, model (a paper that defines a model) and constraint (a data paper used
# for its bound on a model's parameters) to the observational suite's roles.
ROLES = {
    "foundation", "review", "textbook", "lectures", "method", "model", "results", "constraint",
    "data", "systematics", "forecast", "code", "critique",
}
TITLE_THRESHOLD = 0.85
ATTEMPTS = 8
CACHE = Path(os.environ.get("XDG_CACHE_HOME", Path.home() / ".cache")) / "thcosmo-skill-verify" / "arxiv.json"

NEW_ID = r"\d{4}\.\d{4,5}"
OLD_ID = r"[a-z][a-z\-]+(?:\.[A-Z]{2})?/\d{7}"
ARXIV_CITE = re.compile(rf"arXiv:\s?({NEW_ID}|{OLD_ID})", re.IGNORECASE)
DOI_CITE = re.compile(r"doi:\s?(10\.\d{4,9}/[^\s,;)\]>|`]+)", re.IGNORECASE)
ARXIV_ID = re.compile(rf"^(?:{NEW_ID}|{OLD_ID})$")


def fold(text: str) -> str:
    """Lower-case, strip accents, LaTeX markup and punctuation."""
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"\\[a-zA-Z]+", " ", text)
    text = re.sub(r"[^a-zA-Z0-9]+", " ", text)
    return " ".join(text.lower().split())


def read_sources(path: Path) -> tuple[list[dict], list[str]]:
    problems: list[str] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t", quoting=csv.QUOTE_NONE)
        legacy = reader.fieldnames == LEGACY_COLUMNS
        if reader.fieldnames != COLUMNS and not legacy:
            problems.append(
                f"{path}: header is {reader.fieldnames}, expected {COLUMNS}"
            )
            return [], problems
        rows = []
        for number, row in enumerate(reader, start=2):
            if None in row or any(value is None for value in row.values()):
                problems.append(f"{path}:{number}: wrong number of columns")
                continue
            row = {name: value.strip() for name, value in row.items()}
            if legacy:
                row["version"] = "-"
            row["_line"] = number
            rows.append(row)
    seen_keys: dict[str, int] = {}
    seen_ids: dict[str, int] = {}
    for row in rows:
        where = f"{path}:{row['_line']}"
        if not all(row[name] for name in COLUMNS):
            problems.append(f"{where}: empty field")
        if row["role"] not in ROLES:
            problems.append(f"{where}: role '{row['role']}' not in {sorted(ROLES)}")
        if not VERSION.match(row["version"]):
            problems.append(f"{where}: version '{row['version']}' is neither v<n> nor -")
        if not re.fullmatch(r"\d{4}", row["year"]):
            problems.append(f"{where}: year '{row['year']}' is not four digits")
        ident = row["id"]
        if not (ARXIV_ID.match(ident) or ident.lower().startswith("doi:10.")):
            problems.append(f"{where}: id '{ident}' is neither an arXiv ID nor doi:<doi>")
        for label, value, seen in (("key", row["key"], seen_keys), ("id", ident.lower(), seen_ids)):
            if value in seen:
                problems.append(f"{where}: duplicate {label} '{value}' (line {seen[value]})")
            seen[value] = row["_line"]
    return rows, problems


def cited_ids(skill: Path) -> tuple[dict[str, set[str]], dict[str, set[str]]]:
    """Return ({arxiv_id: files}, {doi: files}) cited in the skill's Markdown
    files and in its subtopic list, whose `from` column names reviews."""
    arxiv: dict[str, set[str]] = {}
    doi: dict[str, set[str]] = {}
    for md in sorted(skill.rglob("*.md")) + sorted(skill.glob("references/subtopics.tsv")):
        text = md.read_text(encoding="utf-8")
        name = str(md.relative_to(skill))
        for match in ARXIV_CITE.finditer(text):
            arxiv.setdefault(match.group(1).lower(), set()).add(name)
        for match in DOI_CITE.finditer(text):
            doi.setdefault(match.group(1).rstrip(".").lower(), set()).add(name)
    return arxiv, doi


def load_cache() -> dict[str, dict]:
    try:
        return json.loads(CACHE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def save_cache(cache: dict[str, dict]) -> None:
    try:
        CACHE.parent.mkdir(parents=True, exist_ok=True)
        temporary = CACHE.with_suffix(f".{os.getpid()}.tmp")
        temporary.write_text(json.dumps(cache, ensure_ascii=False, indent=0), encoding="utf-8")
        temporary.replace(CACHE)
    except OSError as error:
        print(f"  cache not written: {error}", file=sys.stderr)


def unreachable(error: BaseException) -> bool:
    """True when this machine has no route to arXiv, as opposed to a slow or busy arXiv.

    A failed name lookup, a refused connection, an unreachable network, or the
    403 an egress proxy answers for a blocked host. A sandbox that allows only
    some domains (the Claude app's) fails this way; retrying cannot help.
    """
    if isinstance(error, urllib.error.HTTPError):
        return error.code == 403
    if not isinstance(error, urllib.error.URLError):
        return False
    reason = error.reason
    if isinstance(reason, (socket.gaierror, ConnectionRefusedError)):
        return True
    if not isinstance(reason, OSError):
        return False
    # over HTTPS a proxy's refusal arrives as "Tunnel connection failed: 403 Forbidden"
    return reason.errno in (errno.ENETUNREACH, errno.EHOSTUNREACH) or str(reason).startswith(
        "Tunnel connection failed: 4")


def query(chunk: list[str]) -> bytes:
    """One arXiv API request, with backoff on rate limiting and network errors."""
    url = f"{API}?{urllib.parse.urlencode({'id_list': ','.join(chunk), 'max_results': len(chunk)})}"
    for attempt in range(ATTEMPTS):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "thcosmo-skill-verify/1.0"})
            with urllib.request.urlopen(request, timeout=60) as response:
                return response.read()
        except (urllib.error.URLError, TimeoutError) as error:
            if unreachable(error):
                print(f"arXiv cannot be reached from this machine ({error}); do not retry. "
                      "Use --offline for the local checks only.", file=sys.stderr)
                raise SystemExit(3)
            wait = min(15 * 2 ** attempt, 240)
            retry_after = getattr(error, "headers", None) and error.headers.get("Retry-After")
            if retry_after and retry_after.isdigit():
                wait = max(wait, int(retry_after))
            print(f"  arXiv API: {error}; retry in {wait} s", file=sys.stderr)
            time.sleep(wait)
    raise SystemExit(
        "arXiv API unreachable or rate-limited; rerun later (found papers are cached), "
        "or use --offline for the local checks only"
    )


def fetch(ids: list[str], need_version: bool = False) -> dict[str, dict]:
    """Return {id: {'title', 'authors', 'version'}} for the papers arXiv knows.

    Papers found once are cached on disk: a record on arXiv does not change
    its title or first author in a way that matters here, and the cache keeps
    repeated runs from hitting the rate limit. Missing papers are not cached.
    With `need_version`, a cached record is asked again when it holds no
    version or was read more than a day ago, since new versions appear.
    """
    cache = load_cache()
    today = time.strftime("%Y-%m-%d")

    def fresh(ident: str) -> bool:
        record = cache.get(ident)
        if record is None:
            return False
        return not need_version or ("version" in record and record.get("read") == today)

    found = {ident: cache[ident] for ident in ids if fresh(ident)}
    missing = [ident for ident in ids if not fresh(ident)]
    for start in range(0, len(missing), BATCH):
        chunk = missing[start:start + BATCH]
        root = ET.fromstring(query(chunk))
        for entry in root.findall("a:entry", ATOM):
            ident = entry.findtext("a:id", default="", namespaces=ATOM)
            title = entry.findtext("a:title", default="", namespaces=ATOM)
            if "/abs/" not in ident or not title or title.strip() == "Error":
                continue
            versioned = ident.split("/abs/")[1]
            bare = re.sub(r"v\d+$", "", versioned).lower()
            version = re.search(r"(v\d+)$", versioned)
            authors = [a.findtext("a:name", default="", namespaces=ATOM) for a in entry.findall("a:author", ATOM)]
            found[bare] = cache[bare] = {"title": " ".join(title.split()), "authors": authors,
                                         "version": version.group(1) if version else "-", "read": today}
        save_cache(cache)
        if start + BATCH < len(missing):
            time.sleep(PAUSE)
    return found


def check_skill(skill: Path, offline: bool, warnings: list[str] | None = None) -> list[str]:
    sources = skill / "references" / "sources.tsv"
    if not sources.is_file():
        return [f"{sources}: missing"]
    rows, problems = read_sources(sources)
    cited_arxiv, cited_doi = cited_ids(skill)

    row_arxiv = {row["id"].lower(): row for row in rows if ARXIV_ID.match(row["id"])}
    row_doi = {row["id"][4:].lower(): row for row in rows if row["id"].lower().startswith("doi:")}

    for ident, files in sorted(cited_arxiv.items()):
        if ident not in row_arxiv:
            problems.append(f"{skill.name}: arXiv:{ident} cited in {sorted(files)} has no row in sources.tsv")
    for ident, files in sorted(cited_doi.items()):
        if ident not in row_doi:
            problems.append(f"{skill.name}: doi:{ident} cited in {sorted(files)} has no row in sources.tsv")
    for ident, row in sorted(row_arxiv.items()):
        if ident not in cited_arxiv:
            problems.append(f"{sources}:{row['_line']}: arXiv:{ident} ({row['key']}) is never cited")
    for ident, row in sorted(row_doi.items()):
        if ident not in cited_doi:
            problems.append(f"{sources}:{row['_line']}: doi:{ident} ({row['key']}) is never cited")

    if offline or not row_arxiv:
        return problems
    return problems + compare_with_arxiv(row_arxiv, sources, warnings)


def newer(recorded: str, latest: str) -> bool:
    """True when arXiv's latest version is after the one recorded."""
    if not (recorded.startswith("v") and latest.startswith("v")):
        return False
    return int(latest[1:]) > int(recorded[1:])


def compare_with_arxiv(row_arxiv: dict[str, dict], sources: Path, warnings: list[str] | None = None) -> list[str]:
    """Compare rows, given as {arXiv id: row}, with what arXiv lists.

    Warnings (a newer version on arXiv, a version not recorded) go to
    `warnings` when a list is given; they are not problems.
    """
    problems: list[str] = []
    want_versions = warnings is not None and any(row.get("version", "-") != "-" for row in row_arxiv.values())
    found = fetch(sorted(row_arxiv), need_version=want_versions)
    for ident, row in sorted(row_arxiv.items()):
        where = f"{sources}:{row['_line']}"
        record = found.get(ident)
        if record is None:
            problems.append(f"{where}: arXiv:{ident} ({row['key']}) not found on arXiv")
            continue
        ratio = difflib.SequenceMatcher(None, fold(row["title"]), fold(record["title"])).ratio()
        if ratio < TITLE_THRESHOLD:
            problems.append(
                f"{where}: arXiv:{ident} title mismatch ({ratio:.2f})\n"
                f"      file : {row['title']}\n      arXiv: {record['title']}"
            )
        wanted = fold(row["first_author"])
        first = fold(record["authors"][0]) if record["authors"] else ""
        if wanted and not (wanted in first or first in wanted or set(wanted.split()) & set(first.split())):
            problems.append(
                f"{where}: arXiv:{ident} first author '{row['first_author']}' "
                f"but arXiv lists '{record['authors'][0] if record['authors'] else '?'}'"
            )
        if warnings is not None:
            recorded, latest = row.get("version", "-"), record.get("version", "-")
            if recorded == "-":
                warnings.append(f"{where}: arXiv:{ident} ({row['key']}) records no version")
            elif newer(recorded, latest):
                warnings.append(f"{where}: arXiv:{ident} ({row['key']}) read in {recorded}, arXiv now has {latest}: "
                                f"check that the places given still hold")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("skills", nargs="+", type=Path, help="skill directories to check")
    parser.add_argument("--offline", action="store_true", help="skip the arXiv API; local consistency only")
    args = parser.parse_args()

    total = 0
    for skill in args.skills:
        if (skill / "SKILL.md").is_file() and not (skill / "references").is_dir():
            print(f"{skill.name}: workflow skill, no bibliography; skipped")
            continue
        warnings: list[str] = []
        problems = check_skill(skill.resolve(), args.offline, warnings)
        rows = skill / "references" / "sources.tsv"
        count = sum(1 for _ in rows.open(encoding="utf-8")) - 1 if rows.is_file() else 0
        for problem in problems:
            print(problem)
        for warning in warnings:
            print(f"warning: {warning}")
        mode = "offline" if args.offline else "arXiv-checked"
        print(f"{skill.name}: {count} sources, {len(problems)} problem(s) [{mode}]")
        total += len(problems)
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
