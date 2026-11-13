"""Plan v2, T2b: transcribed equations are compared with the equation their source prints."""

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import check_transcription  # noqa: E402
import latex_norm  # noqa: E402

PAPERS = ROOT / "tests" / "fixtures" / "papers"
B = "(Bernardeau et al. 2002, arXiv:astro-ph/0112551)"
STATEMENTS = {
    # verbatim up to spacing, font-command style and braces: exact
    "exact": r"$F_2(\mathbf{q}_1,\mathbf{q}_2) = \frac{5}{7}+\frac{1}{2}\frac{\mathbf{q}_1\cdot\mathbf{q}_2}{q_1 q_2}"
             r"\left(\frac{q_1}{q_2}+\frac{q_2}{q_1}\right)+\frac{2}{7}\frac{(\mathbf{q}_1\cdot\mathbf{q}_2)^2}{q_1^2q_2^2}$ "
             + B + " [src: Eq. 45]",
    # the right-hand side only of a two-equality display: contained
    "contained": r"$\eta_{\rm v}(\phi)=2\left(\frac{M_{\rm pl}}{\phi}\right)^{2}$ (Baumann 2009, arXiv:0907.5424) [src: Eq. 87]",
    # 3/7 where the source has 5/7: mismatch
    "mismatch": r"$F_{2}({\bf q}_{1},{\bf q}_{2})=\frac{3}{7}+\frac{1}{2}\frac{{\bf q}_{1}\cdot{\bf q}_{2}}{q_{1}q_{2}}"
                r"(\frac{q_{1}}{q_{2}}+\frac{q_{2}}{q_{1}})+\frac{2}{7}\frac{({\bf q}_{1}\cdot{\bf q}_{2})^{2}}{q_{1}^{2}q_{2}^{2}}$ "
                + B + " [src: Eq. 45]",
    # an equation the rendering prints without LaTeX: unreadable
    "unreadable": r"$a = b + c$ " + B + " [src: Eq. 85]",
}


class TranscriptionTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        cache = Path(self.tmp.name) / "papers"
        shutil.copytree(PAPERS, cache)
        self.old = check_transcription.fetch_paper.CACHE
        check_transcription.fetch_paper.CACHE = cache

    def tearDown(self):
        check_transcription.fetch_paper.CACHE = self.old
        self.tmp.cleanup()

    def skill(self, statements):
        path = Path(self.tmp.name) / "thcosmo-x"
        (path / "references").mkdir(parents=True, exist_ok=True)
        (path / "references" / "formalism.md").write_text("# F\n\n" + "\n\n".join(statements) + "\n", encoding="utf-8")
        return path

    def test_four_classes(self):
        for expected, statement in STATEMENTS.items():
            with self.subTest(expected=expected):
                records = check_transcription.check(self.skill([statement]), offline=True)
                self.assertEqual([r["class"] for r in records], [expected])

    def test_range_of_equations(self):
        statement = (r"$G_{2}({\bf q}_{1},{\bf q}_{2})=\frac{3}{7}+\frac{1}{2}\frac{{\bf q}_{1}\cdot{\bf q}_{2}}{q_{1}q_{2}}"
                     r"(\frac{q_{1}}{q_{2}}+\frac{q_{2}}{q_{1}})+\frac{4}{7}\frac{({\bf q}_{1}\cdot{\bf q}_{2})^{2}}"
                     r"{q_{1}^{2}q_{2}^{2}}$ " + B + " [src: Eqs. 45–46]")
        self.assertEqual(check_transcription.labels("[src: Eqs. 45–46]"), ["45", "46"])
        self.assertEqual([r["class"] for r in check_transcription.check(self.skill([statement]), offline=True)], ["exact"])

    def test_paper_not_cached_offline_is_unreadable(self):
        statement = r"$x = y + z$ (arXiv:1234.56789) [src: Eq. 2]"
        self.assertEqual([r["class"] for r in check_transcription.check(self.skill([statement]), offline=True)],
                         ["unreadable"])

    def test_unnumbered_and_pdf_places_go_to_a_person(self):
        for place in ("[src: Sect. 3.2, unnumbered display after Eq. 45]", "[src: Eq. 45 (PDF v2)]",
                      "[src: Sect. 2, inline]"):
            with self.subTest(place=place):
                statement = r"$x = y + z$ " + B + " " + place
                self.assertEqual([r["class"] for r in check_transcription.check(self.skill([statement]), offline=True)],
                                 ["unreadable"])

    def test_rows_and_wrappers(self):
        self.assertEqual(latex_norm.normalise(r"\framebox{$\displaystyle a=b$}\,."), latex_norm.normalise("a=b"))
        self.assertEqual(latex_norm.normalise(r"\boxed{\begin{aligned} a&=b\\ &+c\end{aligned}}~."),
                         latex_norm.normalise("a=b+c"))

    def test_attribution_to_the_nearest_paper(self):
        statement = (STATEMENTS["exact"] + "; it is reproduced in later reviews (arXiv:0907.5424, Sect. 2).")
        records = check_transcription.check(self.skill([statement]), offline=True)
        self.assertEqual([(r["id"], r["class"]) for r in records], [("astro-ph/0112551", "exact")])

    def test_flag_closes_the_citation_of_the_paper_before(self):
        # `$a$ (arXiv:X) [src] … $b$ [src] … (arXiv:Y) [src]`: `$b$` is read in X when Y does not hold it.
        span = STATEMENTS["exact"].replace(" " + B + " [src: Eq. 45]", "")
        statement = (STATEMENTS["unreadable"] + "; the kernel is " + span + " [src: Eq. 45]; "
                     "compare (arXiv:0907.5424) [src: Eq. 87].")
        records = check_transcription.check(self.skill([statement]), offline=True)
        kernel = [r for r in records if r["transcribed"].startswith("F_2")]
        self.assertEqual([(r["id"], r["class"]) for r in kernel], [("astro-ph/0112551", "exact")])

    def test_section_must_contain_the_equation(self):
        right = STATEMENTS["exact"].replace("[src: Eq. 45]", "[src: Sect. 2, Eq. 45]")
        wrong = STATEMENTS["exact"].replace("[src: Eq. 45]", "[src: Sect. 5, Eq. 45]")
        self.assertEqual([r["class"] for r in check_transcription.check(self.skill([right]), offline=True)], ["exact"])
        self.assertEqual([r["class"] for r in check_transcription.check(self.skill([wrong]), offline=True)],
                         ["wrong-section"])

    def test_normalise(self):
        self.assertEqual(latex_norm.normalise(r"{\bf q}_{1}\hskip 18.49988pt\,"), latex_norm.normalise(r"\mathbf{q}_1"))
        self.assertEqual(latex_norm.normalise(r"\displaystyle\dfrac{a}{b}."), latex_norm.normalise(r"\frac{a}{b}"))
        self.assertNotEqual(latex_norm.normalise(r"\frac{5}{7}"), latex_norm.normalise(r"\frac{3}{7}"))
        self.assertEqual(latex_norm.normalise(r"G_{\mspace{-2mu}\mathrm{N}}=c=1"), latex_norm.normalise(r"G_{\mathrm{N}}=c=1"))
        self.assertEqual(latex_norm.normalise(r"q\rightarrow\infty"), latex_norm.normalise(r"q\to\infty"))
        self.assertNotEqual(latex_norm.normalise(r"\rightarrowtail"), latex_norm.normalise(r"\totail"))

    def test_section_prefixed_labels(self):
        # Reviews number equations by section in Roman numerals: (II.19), (III.7), (II.25b).
        self.assertEqual(check_transcription.labels("[src: Eq. II.19; Eqs. III.6, II.25b]"), ["II.19", "III.6", "II.25b"])
        self.assertEqual(check_transcription.labels("[src: Eq. A.3]"), ["A.3"])


if __name__ == "__main__":
    unittest.main()
