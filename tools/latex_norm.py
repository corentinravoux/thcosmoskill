"""LaTeX in skill files: find equations, strip structure, normalise for comparison.

Shared by `check_numbers.py` (which digits of an equation are values),
`check_equations.py` (which statements hold an equation) and
`check_transcription.py` (is an equation the one its source prints).
Plan v2, decisions D10 and D11.

The normalisations below do not change what an equation says; they absorb the
differences between how a paper's LaTeX is printed by arXiv's HTML rendering
(LaTeXML) and how it is copied into a skill file:

- spacing commands and their dimensions (`\\,`, `\\;`, `\\!`, `\\quad`,
  `\\hskip 18.49988pt`, `\\kern`, `\\mskip`, `\\hspace{...}`);
- style commands (`\\displaystyle`, `\\textstyle`), sizing (`\\left`, `\\right`,
  `\\big`, `\\Big`, `\\bigl`, ...);
- font-command style: `{\\bf x}` = `\\mathbf{x}`, `{\\rm x}` = `\\mathrm{x}`,
  `\\boldsymbol` = `\\mathbf`, `\\dfrac` and `\\tfrac` = `\\frac`;
- braces around one token (`F_{2}` = `F_2`), whitespace, and punctuation at the
  end of a display.

Standard library only.
"""

from __future__ import annotations

import re

# Display math first, then inline: `$$...$$`, `\[...\]`, `$...$` (not an escaped dollar).
MATH = re.compile(r"\$\$(.+?)\$\$|\\\[(.+?)\\\]|(?<![\\$])\$(?!\$)([^$]+?)(?<!\\)\$", re.S)
SPACING = re.compile(r"\\(?:hskip|kern|mskip|mkern|vskip)\s*-?[\d.]+\s*(?:pt|em|ex|mu|mm|cm|in)?"
                     r"|\\h?space\*?\{[^}]*\}|\\(?:quad|qquad|,|;|:|!|\s)|(?<!\\)~")
# Wrappers and alignment that do not change what an equation says (P0 probe, B9).
ENVIRONMENT = re.compile(r"\\(?:begin|end)\{(?:aligned|split|gathered|align\*?|equation\*?|eqnarray\*?)\}(?:\[[a-z]\])?")
ALIGNMENT = re.compile(r"(?<!\\)&|\\\\(?:\[[^\]]*\])?")
STYLE = re.compile(r"\\(?:displaystyle|textstyle|scriptstyle|left|right|middle|[bB]igg?[lrm]?|nonumber|notag)(?![A-Za-z])")
RELATION = re.compile(r"=|\\equiv|\\propto|\\simeq|\\approx|\\sim(?![A-Za-z])|\\leq?(?![A-Za-z])|\\geq?(?![A-Za-z])"
                      r"|\\ll(?![A-Za-z])|\\gg(?![A-Za-z])|\\to(?![A-Za-z])|<|>")
DIGITS = re.compile(r"\d+(?:\.\d+)?")


def spans(text: str) -> list[str]:
    """The LaTeX of every math span in a text, in order."""
    return [next(group for group in match.groups() if group is not None) for match in MATH.finditer(text)]


def without_math(text: str, placeholder: str = " ") -> str:
    """The text with every math span replaced by a placeholder."""
    return MATH.sub(placeholder, text)


def _group_end(latex: str, start: int) -> int:
    """Index just after the brace group that opens at `start` (latex[start] == '{')."""
    depth = 0
    for index in range(start, len(latex)):
        if latex[index] == "{":
            depth += 1
        elif latex[index] == "}":
            depth -= 1
            if depth == 0:
                return index + 1
    return len(latex)


def _strip_scripts(latex: str) -> str:
    """Remove subscripts, and superscripts of one token (`^2`, `^{2}`, `^{\\prime}`); keep other superscripts."""
    out, index = [], 0
    while index < len(latex):
        char = latex[index]
        if char in "_^" and index + 1 < len(latex):
            nxt = index + 1
            while nxt < len(latex) and latex[nxt] == " ":
                nxt += 1
            if nxt < len(latex) and latex[nxt] == "{":
                end = _group_end(latex, nxt)
                inner = latex[nxt + 1:end - 1].strip()
                one_token = re.fullmatch(r"[A-Za-z0-9]|\\[A-Za-z]+", inner) is not None
                if char == "_" or one_token:
                    index = end
                    continue
            elif nxt < len(latex):
                command = re.match(r"\\[A-Za-z]+", latex[nxt:])
                index = nxt + (len(command.group(0)) if command else 1)
                continue
        out.append(char)
        index += 1
    return "".join(out)


def structure_free(latex: str) -> str:
    """An equation without the parts that are notation rather than value: spacing, style, scripts, commands."""
    text = SPACING.sub(" ", latex)
    text = STYLE.sub(" ", text)
    text = _strip_scripts(text)
    text = re.sub(r"\\[A-Za-z]+", " ", text)
    return text


def math_numbers(latex: str) -> list[str]:
    """The digits of an equation that are values: every number left once notation is removed.

    Single digits count here (a coefficient 5/7 is a value), unlike in prose.
    """
    return DIGITS.findall(structure_free(latex))


# A parameter set to a value or a symbol (`s=0`, `d=1`, `t=s-1`): notation, not an equation (P0 probe, B18).
ASSIGNMENT = re.compile(r"^\s*\\?[A-Za-z]+(?:_\{?[^{}=]{1,8}\}?)?\s*=\s*-?\s*(?:\d+(?:\.\d+)?|[A-Za-z](?:\s*[-+]\s*\d+)?)\s*[,.]?\s*$")
# A measured value with its error (`f_{\rm NL}=-0.9\pm 5.1`): a number, checked as one.
VALUE = re.compile(r"=\s*-?\s*\d+(?:\.\d+)?\s*(?:\\pm|\^\{?[+-])")


def is_equation(latex: str) -> bool:
    """A math span that states a relation (=, ≡, ∝, ≃, ≈, ∼, <, >, ≪, ≫, ≤, ≥, →).

    A parameter set to a value (`s=0`) and a measured value with its error
    (`x=0.9\\pm0.1`) are not equations: the first is notation, the second a
    number that `check_numbers.py` checks.
    """
    text = SPACING.sub(" ", latex)
    if ASSIGNMENT.match(text) or VALUE.search(text):
        return False
    return RELATION.search(text) is not None


def _unwrap(latex: str, command: str) -> str:
    """Remove a wrapper command and its brace pair: \\boxed{x} -> x."""
    while True:
        start = latex.find(command + "{")
        if start < 0:
            return latex
        brace = start + len(command)
        end = _group_end(latex, brace)
        latex = latex[:start] + latex[brace + 1:end - 1] + latex[end:]


def normalise(latex: str) -> str:
    """A canonical form for comparing a transcribed equation with its source."""
    text = latex
    for wrapper in (r"\boxed", r"\framebox", r"\fbox"):
        text = _unwrap(text, wrapper)
    text = text.replace("$", "")
    text = ENVIRONMENT.sub("", text)
    text = ALIGNMENT.sub("", text)
    text = SPACING.sub("", text)
    text = STYLE.sub("", text)
    text = re.sub(r"\{\\(bf|rm|it|cal|sf|tt)\s+([^{}]*)\}",
                  lambda m: {"bf": r"\mathbf", "rm": r"\mathrm", "it": r"\mathit", "cal": r"\mathcal",
                             "sf": r"\mathsf", "tt": r"\mathtt"}[m.group(1)] + "{" + m.group(2).strip() + "}", text)
    text = re.sub(r"\\boldsymbol(?![A-Za-z])", r"\\mathbf", text)
    text = re.sub(r"\\[dt]frac(?![A-Za-z])", r"\\frac", text)
    text = re.sub(r"\s+", "", text)
    # one token in braces after _ or ^: F_{2} -> F_2, k^{3} -> k^3
    text = re.sub(r"([_^])\{([A-Za-z0-9]|\\[A-Za-z]+)\}", r"\1\2", text)
    # a command's single-token argument: \mathbf{q} stays, but {q} alone loses its braces
    text = re.sub(r"(?<![\\A-Za-z}])\{([A-Za-z0-9])\}", r"\1", text)
    return text.rstrip(".,;")
