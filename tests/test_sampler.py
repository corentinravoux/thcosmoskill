"""Plan v2, T4: the G2 sheet and its error bound."""

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import check_places  # noqa: E402
import check_transcription  # noqa: E402
import sample_statements  # noqa: E402

PAPERS = ROOT / "tests" / "fixtures" / "papers"
P = "(Fixture 2099, arXiv:9999.00020)"
F2 = (r"$F_{2}({\bf q}_{1},{\bf q}_{2})=\frac{5}{7}+\frac{1}{2}\frac{{\bf q}_{1}\cdot{\bf q}_{2}}{q_{1}q_{2}}"
      r"(\frac{q_{1}}{q_{2}}+\frac{q_{2}}{q_{1}})+\frac{2}{7}\frac{({\bf q}_{1}\cdot{\bf q}_{2})^{2}}{q_{1}^{2}q_{2}^{2}}$"
      " (arXiv:astro-ph/0112551) [src: Eq. 45]")


class SamplerTest(unittest.TestCase):
    def test_upper_bound(self):
        self.assertAlmostEqual(sample_statements.upper_bound(0, 59), 0.0495, places=3)
        self.assertLess(sample_statements.upper_bound(0, 59), 0.05)
        self.assertGreater(sample_statements.upper_bound(0, 58), 0.05)
        self.assertAlmostEqual(sample_statements.upper_bound(1, 93), 0.0501, places=2)
        self.assertAlmostEqual(sample_statements.upper_bound(0, 10), 0.2589, places=3)

    def test_sheet_parts(self):
        with tempfile.TemporaryDirectory() as tmp:
            cache = Path(tmp) / "papers"
            shutil.copytree(PAPERS, cache)
            old = check_places.fetch_paper.CACHE
            check_places.fetch_paper.CACHE = check_transcription.fetch_paper.CACHE = cache
            try:
                skill = Path(tmp) / "thcosmo-x"
                (skill / "references").mkdir(parents=True)
                (skill / "SKILL.md").write_text(f"# X\n\nHeadline 0.9649 {P} [src: Sect. 4.2].\n", encoding="utf-8")
                (skill / "references" / "formalism.md").write_text(
                    "# F\n\n## Conventions\n\nSignature from " + P + " [src: Sect. 4.2] with 0.471.\n\n"
                    "## Kernels\n\n" + F2 + "\n\nIndex 0.9650 " + P + " [src: Sect. 4.2].\n\n"
                    "Amplitude 0.471 " + P + " [src: abstract].\n", encoding="utf-8")
                part1, part2, draw = sample_statements.sheet(skill, seed=3, offline=True)
            finally:
                check_places.fetch_paper.CACHE = old
        self.assertEqual(sorted(e["kind"] for e in part1), ["SKILL.md", "conventions"])
        self.assertEqual([e["status"] for e in part2], ["not-found"])
        self.assertEqual(sorted(e["kind"] for e in draw), ["equation", "number"])
        text = sample_statements.render("thcosmo-x", 3, (part1, part2, draw))
        self.assertIn("## 3. Random draw", text)


if __name__ == "__main__":
    unittest.main()
