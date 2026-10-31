"""Plan v2, P2: the owner's review sheet of the pilot."""

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import review_sheet  # noqa: E402

LONG = "a statement long enough to be reviewed, with some words in it"


class ReviewSheetTest(unittest.TestCase):
    def test_sheet(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / "thcosmo-x"
            refs = skill / "references"
            refs.mkdir(parents=True)
            (refs / "formalism.md").write_text(
                f"# F\n\n## Conventions\n\nConvention one, {LONG}.\n\n## Kernels\n\n"
                f"$F_2=\\frac{{5}}{{7}}$ (arXiv:astro-ph/0112551) [src: Eq. 45], {LONG}.\n", encoding="utf-8")
            (refs / "models.md").write_text(f"# M\n\nModel statement, {LONG}.\n", encoding="utf-8")
            (refs / "approximations.md").write_text(f"# A\n\nApproximation statement, {LONG}.\n", encoding="utf-8")
            pools = review_sheet.pools(skill)
            text = review_sheet.render(skill, 1)
        self.assertEqual({k: len(v) for k, v in pools.items()},
                         {"equation": 1, "conventions": 1, "model or result": 1, "approximation": 1})
        self.assertIn("## General remarks", text)
        self.assertEqual(text.count("- Verdict: "), 4)


if __name__ == "__main__":
    unittest.main()
