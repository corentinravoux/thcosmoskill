"""Fixes from the hep-th probe P0 (docs/history/tests/p0-probe.md, 2026-10-31)."""

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "plugin" / "skills" / "theoretical-cosmology" / "scripts"))
import check_equations  # noqa: E402
import check_numbers  # noqa: E402
import check_places  # noqa: E402
import fetch_paper  # noqa: E402
import latex_norm  # noqa: E402
import verify_sources  # noqa: E402


class ProbeFixesTest(unittest.TestCase):
    def test_b3_section_by_the_papers_own_number(self):
        blocks = [("heading", 1, "Title"), ("heading", 2, "1 Introduction"), ("heading", 3, "1.1 Road map"),
                  ("heading", 2, "2 Setup"), ("text", 0, "body of two"), ("heading", 2, "4 A no-go theorem"),
                  ("text", 0, "body of four")]
        self.assertEqual(fetch_paper.section(blocks, "Sect. 4")[0][2], "4 A no-go theorem")
        self.assertEqual(fetch_paper.section(blocks, "4.")[0][2], "4 A no-go theorem")
        self.assertEqual(fetch_paper.section(blocks, "2")[0][2], "1.1 Road map")  # outline entry

    def test_b11_footnote_marks_once(self):
        html = ('<p>Text<sup class="ltx_note_mark">3</sup><span class="ltx_note_outer"><span class="ltx_note_content">'
                '<sup class="ltx_note_mark">3</sup><span class="ltx_tag ltx_tag_note">3</span>A note.</span></span></p>')
        text = fetch_paper.parse(html)[0][2]
        self.assertEqual(text.count("[fn 3]"), 1)
        self.assertNotIn(" 3 A note", text)

    def test_b5_b9_normalisation(self):
        self.assertEqual(latex_norm.normalise(r"a~=~b~,"), latex_norm.normalise("a=b"))
        self.assertEqual(latex_norm.normalise(r"\boxed{\begin{aligned} x&=y\end{aligned}}"), "x=y")

    def test_b13_inline_place_passes_the_equation_check(self):
        statement = r"$m^{2}=\Delta(d-\Delta)$ (arXiv:2301.04146) [src: Sect. 2.1, inline, text after Eq. 2.5]"
        self.assertEqual(check_equations.classify(statement, ""), "ok")

    def test_b16_malformed_version_does_not_crash(self):
        self.assertFalse(verify_sources.newer("v?", "v2"))

    def test_b18_notation_values_and_der_scope(self):
        self.assertEqual(check_equations.equations("for $s=0$ and $d=1$, and $t=s-1$"), [])
        self.assertEqual(check_equations.equations(r"$f_{\rm NL}=-0.9\pm 5.1$"), [])
        self.assertFalse(check_numbers.derived("A value 0.47 (arXiv:1807.06209) [src: Sect. 3]. So it is slow [der]."))

    def test_b7_places_without_sections(self):
        self.assertEqual(check_places.places("[src: text after Eq. 3] [src: Table 1.3, footnote 6]"),
                         [("after-equation", "3"), ("table", "1.3"), ("footnote", "6")])


if __name__ == "__main__":
    unittest.main()
