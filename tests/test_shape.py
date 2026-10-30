"""Plan v2, T6: the shape of a domain skill and its model cards."""

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import check_shape  # noqa: E402

FIXTURE = ROOT / "tests" / "fixtures" / "domain" / "thcosmo-shape"


class ShapeTest(unittest.TestCase):
    def copy(self, tmp):
        skill = Path(tmp) / "thcosmo-shape"
        shutil.copytree(FIXTURE, skill)
        (skill / "SKILL.fixture.md").rename(skill / "SKILL.md")
        return skill

    def test_every_built_domain_has_the_shape(self):
        for skill in sorted((ROOT / "plugin" / "skills").glob("thcosmo-*")):
            with self.subTest(skill=skill.name):
                self.assertEqual(check_shape.problems_of(skill), [])

    def test_fixture_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(check_shape.problems_of(self.copy(tmp)), [])

    def test_each_defect_is_found(self):
        cases = {
            "approximations.md missing": lambda s: (s / "references" / "approximations.md").unlink(),
            "no Snapshot": lambda s: (s / "references" / "results.md").write_text("# R\n", encoding="utf-8"),
            "conventions block": lambda s: (s / "references" / "formalism.md").write_text(
                "# F\nSnapshot: 2026-10-30\n\n## Kernels\n", encoding="utf-8"),
            "sources.tsv: header": lambda s: (s / "references" / "sources.tsv").write_text(
                "key\tid\tfirst_author\tyear\ttitle\trole\n", encoding="utf-8"),
            "subtopics.tsv:2": lambda s: (s / "references" / "subtopics.tsv").write_text(
                "key\ttitle\tfrom\tfiles\tstatus\nx\tX\ty\tz\tdone\n", encoding="utf-8"),
            "dossiers": lambda s: [(s / "deep" / f"d{i}.md").write_text("# D\n", encoding="utf-8") for i in range(7)],
        }
        for needle, damage in cases.items():
            with self.subTest(defect=needle), tempfile.TemporaryDirectory() as tmp:
                skill = self.copy(tmp)
                damage(skill)
                self.assertTrue(any(needle in p for p in check_shape.problems_of(skill)), needle)

    def test_model_cards(self):
        good = (FIXTURE / "references" / "models.md").read_text(encoding="utf-8")
        self.assertEqual(check_shape.card_problems(good), [])
        self.assertTrue(check_shape.card_problems(good.replace("- **Predictions:** fixture.\n", "")))
        swapped = good.replace("- **Parameters:** fixture.\n- **Predictions:** fixture.\n",
                               "- **Predictions:** fixture.\n- **Parameters:** fixture.\n")
        self.assertIn("(order)", check_shape.card_problems(swapped)[0])
        self.assertTrue(check_shape.card_problems(good.replace("2026-04-01", "April 2026")))
        self.assertEqual([t for t, _ in check_shape.status_dates(good)], ["Fixture model"])


if __name__ == "__main__":
    unittest.main()
