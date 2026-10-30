"""Release 1.0, step R2: the refresh script reads snapshot dates and [doc] read dates."""

import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import refresh_status  # noqa: E402


class RefreshStatusTest(unittest.TestCase):
    def test_snapshot_date(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "results.md"
            path.write_text("# X — results\n\nScope: ...\nSnapshot: 2026-10-16\n", encoding="utf-8")
            self.assertEqual(refresh_status.snapshot(path), date(2026, 10, 16))
            path.write_text("# X\n\nScope: ... Snapshot: **2026-10-14**\n", encoding="utf-8")
            self.assertEqual(refresh_status.snapshot(path), date(2026, 10, 14))
            path.write_text("# X\n\nno date here\n", encoding="utf-8")
            self.assertIsNone(refresh_status.snapshot(path))

    def test_every_domain_has_snapshot_dates(self):
        skills = [p for p in (ROOT / "plugin" / "skills").iterdir() if (p / "references").is_dir()]
        missing = [p.name for p in skills if not refresh_status.files_with_snapshot(p)]
        self.assertEqual(missing, [])

    def test_due_lists_stale_docs(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / "thcosmo-example"
            (skill / "references").mkdir(parents=True)
            (skill / "references" / "results.md").write_text(
                "# X\n\nSnapshot: 2026-10-30\n\n- The code default step is 0.25 [doc: https://example.org/code, 2026-10-30].\n",
                encoding="utf-8")
            self.check_due(skill)

    def check_due(self, skill):
        line, details = refresh_status.status(skill, date(2028, 10, 1), 60)
        self.assertIn("stale within 60 days", line)
        self.assertTrue(any(d.startswith("  [doc] read") for d in details))
        line, details = refresh_status.status(skill, date(2026, 10, 26), 60)
        self.assertFalse(any(d.startswith("  [doc] read") for d in details))

    def test_runs(self):
        result = subprocess.run([sys.executable, str(ROOT / "tools" / "refresh_status.py"), "--due", "90"],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("theoretical-cosmology", result.stdout)



class ModelStatusTest(unittest.TestCase):
    """Plan v2, T9 (decision D23): model statuses older than six months are listed."""

    def test_old_status_is_listed(self):
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / "thcosmo-example"
            (skill / "references").mkdir(parents=True)
            (skill / "references" / "models.md").write_text(
                "# M\n\nSnapshot: 2026-10-30\n\n### Old model\n\n- **Status date:** 2026-01-10\n\n"
                "### New model\n\n- **Status date:** 2026-10-01\n", encoding="utf-8")
            line, details = refresh_status.status(skill, date(2026, 10, 30), 90)
        self.assertIn("1 of 2 model statuses older than six months", line)
        self.assertTrue(any("Old model" in d for d in details))
        self.assertFalse(any("New model" in d for d in details))


if __name__ == "__main__":
    unittest.main()
