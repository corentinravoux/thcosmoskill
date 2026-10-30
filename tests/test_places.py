"""Plan v2, T4b: each number is looked for at the place its flag names."""

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import check_places  # noqa: E402

PAPERS = ROOT / "tests" / "fixtures" / "papers"
P = "(Fixture 2099, arXiv:9999.00020)"
CASES = {
    "found-at-place": [f"The index is 0.9649 {P} [src: Sect. 4.2].",
                       f"An amplitude of 0.471 {P} [src: abstract].",
                       f"A table value of 12.34 {P} [src: Table 3]."],
    "found-elsewhere": [f"The index is 0.9649 {P} [src: Sect. 5]."],
    "not-found": [f"The index is 0.9650 {P} [src: Sect. 4.2]."],
    "unreadable": ["The index is 0.9649 (arXiv:9999.00020, arXiv:9999.00021) [src: Sect. 4.2].",
                   "A value of 3.14 (arXiv:1234.56789) [src: Sect. 2]."],
}


class PlacesTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        cache = Path(self.tmp.name) / "papers"
        shutil.copytree(PAPERS, cache)
        self.old = check_places.fetch_paper.CACHE
        check_places.fetch_paper.CACHE = cache

    def tearDown(self):
        check_places.fetch_paper.CACHE = self.old
        self.tmp.cleanup()

    def run_on(self, statement):
        skill = Path(self.tmp.name) / "thcosmo-x"
        (skill / "references").mkdir(parents=True, exist_ok=True)
        (skill / "references" / "results.md").write_text(f"# R\n\n{statement}\n", encoding="utf-8")
        return [item["class"] for item in check_places.check(skill, offline=True, store={})]

    def test_classes(self):
        for expected, statements in CASES.items():
            for statement in statements:
                with self.subTest(statement=statement):
                    self.assertEqual(self.run_on(statement), [expected])

    def test_equation_numbers_are_left_to_the_transcription_check(self):
        self.assertEqual(self.run_on(r"$x=0.9649$ " + P + " [src: Eq. 4]."), [])

    def test_places(self):
        self.assertEqual(check_places.places("[src: Sect. 4.2, Table 3] [sec: abstract]"),
                         [("section", "4.2"), ("table", "3"), ("abstract", "")])


if __name__ == "__main__":
    unittest.main()
