"""Plan v2, T2: every equation names its paper and equation number; the baseline is zero."""

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import check_equations  # noqa: E402

F2 = r"$F_{2}=\frac{5}{7}+\frac{2}{7}\mu^{2}$"


class EquationsTest(unittest.TestCase):
    def test_no_skill_above_the_baseline(self):
        result = subprocess.run([sys.executable, str(ROOT / "tools" / "check_equations.py"), "--check"],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_every_equation_has_its_source(self):
        skills = sorted(path for path in (ROOT / "plugin" / "skills").iterdir() if (path / "references").is_dir())
        failing = [f"{r['file']}:{r['line']}: {r['status']}" for skill in skills
                   for r in check_equations.scan(skill) if r["status"] not in check_equations.PASSING]
        self.assertEqual(failing, [], "\n".join(failing[:20]))

    def test_the_baseline_is_zero(self):
        self.assertTrue(all(count == 0 for count in check_equations.read_baseline().values()))

    def test_what_is_an_equation(self):
        self.assertEqual(check_equations.equations(F2 + " and $F_2$"), [r"F_{2}=\frac{5}{7}+\frac{2}{7}\mu^{2}"])
        for relation in (r"\equiv", r"\propto", r"\simeq", r"\approx", r"\sim", r"\ll", r"\to", r"\leq"):
            with self.subTest(relation=relation):
                self.assertTrue(check_equations.equations(f"$a {relation} b$"))
        self.assertEqual(check_equations.equations(r"$\sigma_8$ and $\mathbf{k}$"), [])
        self.assertEqual(check_equations.equations(r"scales $k<0.2\,h/{\rm Mpc}$"), [])
        self.assertEqual(check_equations.equations(r"`$a=b$` in code"), [])
        self.assertTrue(check_equations.equations(r"$$\delta = \int F_2\,\delta_1\delta_1$$"))

    def test_classification(self):
        cls = check_equations.classify
        self.assertEqual(cls(F2 + " (arXiv:astro-ph/0112551) [src: Eq. 45]", ""), "ok")
        self.assertEqual(cls(F2 + " (arXiv:astro-ph/0112551) [src: Eq. (45)]", ""), "ok")
        self.assertEqual(cls(F2 + " (arXiv:1234.56789) [src: Sect. 3.2, unnumbered display after Eq. 12]", ""), "ok")
        self.assertEqual(cls(F2 + " (arXiv:astro-ph/0112551) [src: Sect. 2.4]", ""), "no-eq")
        self.assertEqual(cls(F2 + " (arXiv:astro-ph/0112551)", ""), "no-place")
        self.assertEqual(cls(F2 + " [src: Eq. 45]", ""), "no-paper")
        self.assertEqual(cls(F2, ""), "none")
        self.assertEqual(cls(r"$x = y$ <!-- eq: notation -->", ""), "notation")
        self.assertEqual(cls(r"$N=10$ steps by default [doc: https://example.org/code, 2026-10-30]", ""), "doc")
        self.assertEqual(cls("| $F_2$ | Eq. 45 |", "From arXiv:astro-ph/0112551:"), "ok")

    def test_table_pipe(self):
        self.assertEqual(check_equations.classify(r"| $|k| = 1$ | x |", ""), "table-pipe")
        self.assertEqual(check_equations.classify(r"| $\lvert k\rvert = 1$ | arXiv:1234.56789, Eq. 2 |", ""), "ok")


if __name__ == "__main__":
    unittest.main()
