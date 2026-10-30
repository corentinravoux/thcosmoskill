"""Plan v2, T11: citation shares by first author, and the owner's share."""

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import word_share  # noqa: E402


class WordShareTest(unittest.TestCase):
    def test_shares(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / "thcosmo-x"
            (skill / "references").mkdir(parents=True)
            (skill / "references" / "sources.tsv").write_text(
                "key\tid\tversion\tfirst_author\tyear\ttitle\trole\n"
                "A2099\t9999.00031\tv1\tAlpha\t2099\tOne\tmethod\n"
                "B2099\t9999.00032\tv1\tBeta\t2099\tTwo\tmethod\n", encoding="utf-8")
            (skill / "references" / "results.md").write_text(
                "arXiv:9999.00031 arXiv:9999.00031 arXiv:9999.00031 arXiv:9999.00032\n", encoding="utf-8")
            cache = {"9999.00032": {"authors": ["B. Beta", "C. Ravoux"]}}
            result = word_share.shares(skill, "Ravoux", cache)
        self.assertEqual(result["total"], 4)
        self.assertEqual(result["groups"]["Alpha"], 3)
        self.assertEqual(result["owned"], 1)


if __name__ == "__main__":
    unittest.main()
