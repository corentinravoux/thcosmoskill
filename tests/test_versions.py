"""Plan v2, T8: the `version` column of sources.tsv (decision D13)."""

import io
import json
import os
import sys
import tempfile
import time
import unittest
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "plugin" / "skills" / "theoretical-cosmology" / "scripts"))
import verify_sources  # noqa: E402

HEADER = "key\tid\tversion\tfirst_author\tyear\ttitle\trole\n"
LEGACY = "key\tid\tfirst_author\tyear\ttitle\trole\n"


def skill(tmp, table, cite="arXiv:9999.00011"):
    path = Path(tmp) / "thcosmo-x"
    (path / "references").mkdir(parents=True)
    (path / "references" / "sources.tsv").write_text(table, encoding="utf-8")
    (path / "references" / "results.md").write_text(f"# R\n\nSee {cite}.\n", encoding="utf-8")
    return path


class VersionColumnTest(unittest.TestCase):
    def test_new_header_is_read(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = skill(tmp, HEADER + "A2099\t9999.00011\tv2\tFixture\t2099\tA paper\tmethod\n")
            rows, problems = verify_sources.read_sources(path / "references" / "sources.tsv")
        self.assertEqual(problems, [])
        self.assertEqual(rows[0]["version"], "v2")

    def test_legacy_header_reads_as_unknown_version(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = skill(tmp, LEGACY + "A2099\t9999.00011\tFixture\t2099\tA paper\tmethod\n")
            rows, problems = verify_sources.read_sources(path / "references" / "sources.tsv")
        self.assertEqual(problems, [])
        self.assertEqual(rows[0]["version"], "-")

    def test_malformed_version_is_a_problem(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = skill(tmp, HEADER + "A2099\t9999.00011\t2\tFixture\t2099\tA paper\tmethod\n")
            _, problems = verify_sources.read_sources(path / "references" / "sources.tsv")
        self.assertTrue(any("version '2'" in problem for problem in problems))

    def test_newer(self):
        self.assertTrue(verify_sources.newer("v1", "v3"))
        self.assertFalse(verify_sources.newer("v3", "v3"))
        self.assertFalse(verify_sources.newer("-", "v3"))

    def test_a_newer_version_on_arxiv_is_a_warning_not_a_problem(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = skill(tmp, HEADER + "A2099\t9999.00011\tv1\tFixture\t2099\tA paper\tmethod\n")
            cache = Path(tmp) / "cache" / "thcosmo-skill-verify"
            cache.mkdir(parents=True)
            (cache / "arxiv.json").write_text(json.dumps({"9999.00011": {
                "title": "A paper", "authors": ["Ada Fixture"], "version": "v3",
                "read": time.strftime("%Y-%m-%d")}}), encoding="utf-8")
            old = verify_sources.CACHE
            verify_sources.CACHE = cache / "arxiv.json"
            try:
                warnings = []
                problems = verify_sources.check_skill(path, offline=False, warnings=warnings)
            finally:
                verify_sources.CACHE = old
        self.assertEqual(problems, [])
        self.assertEqual(len(warnings), 1)
        self.assertIn("read in v1, arXiv now has v3", warnings[0])


if __name__ == "__main__":
    unittest.main()
