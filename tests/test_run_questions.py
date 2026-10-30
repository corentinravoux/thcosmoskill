"""Plan v2, T10: the question harness reads the template and digests a headless transcript."""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import run_questions  # noqa: E402

FIXTURES = ROOT / "tests" / "fixtures" / "q0"


class RunQuestionsTest(unittest.TestCase):
    def test_read_questions(self):
        questions = run_questions.read_questions(FIXTURES / "questions.md")
        self.assertEqual([q["id"] for q in questions], ["Q01", "Q02"])
        self.assertEqual(questions[0]["question"], "What does the fixture ask, on two lines?")
        self.assertEqual(questions[0]["domain"], "thcosmo-inflation")
        self.assertEqual(questions[1]["bad"], "y.")

    def test_parse_stream(self):
        digest = run_questions.parse_stream((FIXTURES / "stream.jsonl").read_text(encoding="utf-8").splitlines())
        self.assertEqual(digest["model"], "claude-opus-5-5")
        self.assertEqual(digest["skills"], ["thcosmoskill:theoretical-cosmology"])
        self.assertEqual(digest["reads"], ["thcosmo-inflation/references/models.md"])
        self.assertEqual(digest["answer"], "Answer.")
        self.assertEqual(sum(digest["usage"].values()), 100)
        self.assertEqual(digest["listed"], ["thcosmoskill:theoretical-cosmology"])



class BlindGradingTest(unittest.TestCase):
    def test_sheet_and_score(self):
        import json
        import tempfile
        from types import SimpleNamespace
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            base = {"skills": [], "reads": [], "usage": {"input_tokens": 1, "output_tokens": 1}}
            (tmp / "off.jsonl").write_text("\n".join(json.dumps({**base, "id": i, "mode": "off", "answer": f"off {i}"})
                                                     for i in ("Q01", "Q02")) + "\n", encoding="utf-8")
            (tmp / "on.jsonl").write_text("\n".join(json.dumps({**base, "id": i, "mode": "on", "answer": f"on {i}"})
                                                    for i in ("Q01", "Q02")) + "\n", encoding="utf-8")
            args = SimpleNamespace(questions=FIXTURES / "questions.md", off=tmp / "off.jsonl", on=tmp / "on.jsonl",
                                   sheet=tmp / "sheet.md", key=tmp / "key.json", seed=1)
            run_questions.sheet(args)
            text = (tmp / "sheet.md").read_text(encoding="utf-8")
            self.assertIn("### Answer A", text)
            key = json.loads((tmp / "key.json").read_text(encoding="utf-8"))
            # The grader prefers the skills-on answer in both pairs, with no harm.
            for ident, labels in key.items():
                on_label = "A" if labels["A"] == "on" else "B"
                block = text.split(f"## {ident}", 1)[1].split("\n## ", 1)[0]
                graded = (block.replace("(A, B or tie): ", f"(A, B or tie): {on_label}")
                          .replace("(number): ", "(number): 0")
                          .replace("n.a.): ", "n.a.): n.a.")
                          .replace("other: ...): ", "other: ...): none"))
                text = text.replace(block, graded)
            (tmp / "sheet.md").write_text(text, encoding="utf-8")
            grades = run_questions.read_grades(tmp / "sheet.md")
            self.assertEqual(len(grades), 2)
            self.assertTrue(all(g["better"] in ("A", "B") for g in grades.values()))
            import io
            from contextlib import redirect_stdout
            out = io.StringIO()
            with redirect_stdout(out):
                run_questions.score(SimpleNamespace(sheet=tmp / "sheet.md", key=tmp / "key.json",
                                                    off=tmp / "off.jsonl", on=tmp / "on.jsonl"))
            self.assertIn("decision (D28): GO", out.getvalue())


if __name__ == "__main__":
    unittest.main()
