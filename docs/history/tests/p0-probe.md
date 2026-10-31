# P0 probe — provenance rules on high-energy-theory papers

Run: 2026-10-31. Domain staged: `thcosmo-primordial-correlators`, three
subtopics only (in-in scalar bispectrum in single-field slow roll; squeezed-limit
consistency relation; one QFT-in-de-Sitter result from arXiv:2301.04146).
Staging directory: `docs/history/tests/p0-probe/thcosmo-primordial-correlators/`.
Budget: 40 research calls.

## Breakage log (written as found)

### B1. `fetch_paper.py --abstract` does not print the arXiv version (tool)

The brief (`agent-brief.md` §3, `sources.tsv`) says "check which [version]
with `--abstract`", but the header line is `### <id> | <author> | <title>`:
no version. The `version` column of `sources.tsv` cannot be filled from the
tool the brief names. **Proposal:** print `vN` (latest version from the arXiv
API `<id>` element) and the date of that version in the `--abstract` header,
and print the version the HTML rendering was built from in the `read from`
line of `--grep`/`--section`.

### B2. Foundation paper rendered with no equation numbers and no sections: Maldacena 2003, arXiv:astro-ph/0210603 (rendering)

The arXiv HTML rendering exists (LaTeXML oxide 0.7.6) but the paper is
harvmac plain TeX: `<title>Untitled Document</title>`, `--outline` prints
nothing, and no display carries an equation tag (no `ltx_tag_equation`,
no `ltx_eqn_eqno` cell). The body text still refers to "(4.1)", "(4.6)", so the
PDF numbers exist but are lost. Displays are printed as plain-TeX alttext
(`\eqalign{...\cr...}`, `{a\over b}`), which `latex_norm.py` may or may not
normalise. Consequence: the single most-cited equation of the domain (the
slow-roll bispectrum) cannot carry `[src: Eq. n]` that the checker can verify,
and cannot even carry `[src: Sect. x, unnumbered display after Eq. n]`
because the rendering has neither sections nor numbers. Every Maldacena
equation is "unreadable" at best. Many classic hep-th papers (1995–2005,
harvmac, `\eqn`, `\eqalign`) will behave the same.
**Proposal:** (a) new place form `[src: Eq. 4.6 (PDF vN)]` accepted
when `fetch_paper.py` reports "rendering without equation tags" (a new
diagnostic, not only "no HTML"); (b) `fetch_paper.py --grep` should report
"N displays, 0 tagged" so the agent knows at once; (c) rule: for a
foundation paper with untagged rendering, transcribe from a readable
secondary source that reproduces the equation with a number, flagged
`[sec: ...]`, and log the primary as PDF-only for the maintainer.

### B3. `--section 4` selects the 4th outline entry, not Section 4 (tool)

On arXiv:1002.1416, `--section "4"` printed "3 In-in formalism" (outline
index 4) and `--section "2"` printed "1.1 Road map". The help text says
"its number in the outline", which is literally true but collides with the
paper's own section numbers, which are what a `[src: Sect. 4]` place names.
One research call wasted. **Proposal:** accept `--section "Sect. 4"` /
`--section 4.` as the paper's section number, and print the outline index
and the paper's number side by side in `--outline`; or rename the option's
numeric form to `--entry N`.

### B4. Typographical slip in the source itself: Chen 2010, arXiv:1002.1416 Eq. (4.1) (rule)

The rendering prints the Einstein–Hilbert term as `\frac{M_{\rm P}}{2}R`
(no square on the reduced Planck mass), while the text below sets
`M_{\rm P}=1`. Transcribing "as printed" carries the slip into the skill; the
rules say errata go to "Errors that recur" / hub `stale-claims.md`, but they
assume a later version or an erratum exists. Here there is none (v3 is the
latest), and correcting it would be an agent-made equation. I transcribed it
as printed and added a note in words without a corrected equation.
**Proposal:** a flag `[src: Eq. n, as printed; slip noted]` and a rule:
an apparent slip with no published correction is transcribed verbatim, the
slip described in words (no corrected equation) under "Not verified", and
listed for the maintainer.

### B5. `~` (LaTeX tie) not absorbed by `latex_norm.normalise` (tool)

Chen 2010 ends almost every display with `~,` or `~.`; `normalise` strips the
final punctuation but not the `~` before it, and does not strip `~` inside
(`\langle\Omega|[\ldots]~Q^{I}(t)~[\ldots]`). A copy without the ties is
reported as a mismatch or only "contained". I copied the ties verbatim.
**Proposal:** add `~` to `SPACING` in `tools/latex_norm.py` (it is a
non-breaking space, meaning-preserving), and list it in suite-conventions.

### B6. Multi-column displays (`eqnarray`/`align`) are printed as table cells (tool/rule)

Chen Eqs. (3.23), (4.19), (4.22), (4.23) are printed as
`| lhs | = | rhs |` cells over several rows, one number for the whole block.
The rule "one equation per statement, copied as printed" has no stated way to
join the cells (`lhs=rhs`), and continuation rows (`+ ... ~,`) belong to the
same number. I joined cells without adding anything and copied the full
block in one `$...$`; the checker's "contained" case will be what decides.
**Proposal:** say in suite-conventions that the cells of one numbered display
are concatenated in reading order (cells and rows), and make
`check_transcription.py` compare against that concatenation.

### B7. Letters without sections: Creminelli & Zaldarriaga 2004, arXiv:astro-ph/0407059 (rule)

PRL-format paper: the outline is "Abstract / pacs / References"; the whole
body sits under a heading "pacs". The fallback place form
`[src: Sect. x, unnumbered display after Eq. n]` and text places such as
`[src: Sect. x]` have no section to name. Numbered equations (1)–(8) are fine.
For text claims I wrote `[src: text after Eq. n]`.
**Proposal:** allow `[src: text after Eq. n]` and `[src: footnote n]` as
places for papers without sections, and have `check_places.py` accept them.

### B8. `--grep ... --context 1` drops the displays of the context paragraphs (tool)

On arXiv:astro-ph/0407059, `--grep "(2)" --context 1` printed the paragraph
"The power spectrum is defined by" immediately followed by "while n_s-1 is
the usual tilt", silently omitting the numbered display (3) that sits between
them (it is in the cached HTML). An agent reading the tool output would not
know Eq. 3 exists and could misnumber the next equation. **Proposal:** context
paragraphs must keep their display rows (with their numbers), as the matched
paragraph does.

### B9. Source notation slips inside numbered equations (rule)

- arXiv:astro-ph/0407059 Eq. (1): the correlator carries subscripts
  `\vec{\kappa}_{i}` while the delta function and the power spectra use
  `\vec{k}_{i}` and `k_{1}`; the text says `k_{1}`.
- arXiv:2604.09765 Eq. (14): `\zeta(\vec{k}_{1}\dots\zeta(\vec{k_{N}})` has an
  unbalanced parenthesis; the equation is wrapped in
  `\boxed{\begin{aligned}...\end{aligned}}`.
Both are transcribed as printed (verbatim copies of the slip), which is what
the rule demands but makes the skill propagate them. Same proposal as B4.
Separately, `latex_norm` does not strip `\boxed{...}` or
`\begin{aligned}...\end{aligned}`; I copied Eq. (14) without the wrapper to
test whether "contained" absorbs it. **Proposal:** strip `\boxed`,
`aligned`/`split` environments and `&`, `\\` alignment marks in `normalise`.

### B10. Headline hep-th results live in tables, table footnotes and inline math, not in numbered equations (rule)

Penedones et al. 2023, arXiv:2301.04146: the paper's main results are
Tables 1.1–1.4 (tensor-product decompositions) and the conditions for a
complementary series are footnotes *inside table cells* (footnotes 3, 4, 6).
Defining relations (quadratic Casimir $\Delta(d-\Delta)-s(d+s-2)$, mass
$m^{2}=\Delta(d-\Delta)$, the ranges of each series) are inline math in the
prose of Sect. 2.1, not displays. The place forms of the rules
(`[src: Eq. n]`, `[src: Sect. x, unnumbered display after Eq. n]`) do not
fit; `check_transcription.py` only checks `Eq.` places, so none of these
transcriptions is machine-checked. I used `[src: Table 1.3, footnote 6]` and
`[src: Sect. 2.1, inline, before Eq. 2.6]`.
**Proposal:** (a) add place forms `[src: Sect. x, inline before/after Eq. n]`
and `[src: Table t, footnote n]`; (b) extend `check_transcription.py` to
search inline math of the named section / table for a normalised match
(report `exact-inline`), since hep-th papers state far more in inline math
than in displays.

### B11. Rendering artefacts in footnote markers and titles (tool)

- Footnote markers are printed duplicated and glued to the text: "…−1} 33 3
  A complementary series…", "44 4", "66 6", "99 9 When d=2" in
  arXiv:2301.04146. A digit-sensitive checker (`check_numbers.py`) or an agent
  may read "33" as a value.
- The paper title in the `fetch_paper.py` header of `--outline/--section` is
  the HTML `<title>`, mangled by a macro: "in de Sitter spacetime" for
  arXiv:2301.04146, "Untitled Document" (empty) for arXiv:astro-ph/0210603.
- Section titles carry raw LaTeX (`2 A brief review of UIRs of
  {\text{SO}}(1,d+1)`), so `--section` by title needs the LaTeX spelling.
- The arXiv abstract itself contains author macros (`\SO$(1,d+1)$`).
**Proposal:** render footnote marks as `[fn n]`; take the header title from
the arXiv API (as `--abstract` does); match `--section` titles after
stripping LaTeX.

### B12. Foundation results that predate arXiv (rule)

The tensor-product results Penedones et al. build on are Pukánszky (SO(1,2)),
Naimark (SO(1,3)), Hirai and Martin (refs [22]–[31] of arXiv:2301.04146),
1950s–1970s journal papers with no arXiv identifier and no HTML. The rules
send textbook-only content to `[sec: ...]` but say nothing of pre-arXiv
journal papers, which are the normal foundations in mathematical physics.
I cite Naimark's result only through arXiv:2301.04146 with `[sec: Sect. 1,
Brief literature review]` and no `doi:` row (no DOI was fetched).
**Proposal:** treat pre-arXiv primary papers like textbooks: `[sec: ...]`
through a readable source, with a `doi:` row allowed only when the DOI was
returned by a tool (INSPIRE reference list), role `foundation`.

### B13. A text place that names an equation is read as an equation place (tool)

`check_transcription.py` takes every `Eq. n` in a statement as the place of
every equation in it. A statement such as "$M_{\rm P}=(8\pi G)^{-1/2}$ …
[src: Sect. 4, text after Eq. 4.1]" was compared with Eq. 4.1 and reported
as a mismatch (first run: 25 mismatches, about half of this kind, the rest
B6 and B14). Conversely, `check_equations.py` classes such a statement `ok`
merely because "Eq." appears, so a wrong place passes the equation check.
And an inline equation with an honest place without "Eq."
(`[src: Sect. 2.1, inline list]`) is `no-eq`. **No place form exists that
is honest for an inline equation and passes both checkers.** I rewrote
inline definitions in words where possible (Planck mass, conformal time,
$\delta\phi=0$, $H_{I,3}=-L_{3}$) and kept the irreducible ones (dS
representation ranges, masses) as `no-eq` / `unreadable`.
**Proposal:** a recognised place `[src: Sect. x, inline, text after Eq. n]`
that `check_equations` accepts and `check_transcription` searches in the
paragraph after display n (inline math), never against display n itself.

### B14. One statement citing two papers is "unreadable"; model-card fields force this (tool/rule)

`check_transcription.py` marks every equation of a statement "unreadable"
when the statement cites more than one identifier. A sentence noting that
the review reproduces Maldacena's result was enough to disable the check of
Eq. 4.22. I split such sentences. But the model-card format
(`suite-conventions.md#model-cards`) makes **Predictions** one list item that
normally cites several papers, so every predicted equation in a card is
unchecked (`models.md:10`: two unreadable).
**Proposal:** attribute each equation to the identifier nearest it (same
parenthesis or preceding clause), or allow card fields to be sub-lists, one
paper per sub-item.

### B15. Workaround for multi-row displays leaves continuation rows unchecked (tool)

Confirms B6: the checker's source string joins cells with spaces and rows
with ` | `, so a full copy of a multi-row display can never be `exact` or
`contained` (Chen Eqs. 4.9, 4.23 were mismatches on the first run; my
first-run 3.23 also wrongly joined row 1's left side with row 2's right
side, a defect of mine, fixed). Copying each row as its own `$...$` in the
same statement gives `contained` for the first row, but rows 2–3 hold no
relation sign and are not checked at all.
**Proposal:** strip row separators in the source string and compare the
concatenation of consecutive math spans of a statement with it.

### B16. Version column: learnt only from `verify_sources.py` warnings; crash on a placeholder (tool)

Following B1, I wrote `v?` for versions I could not read; `verify_sources.py`
crashed (`ValueError: invalid literal for int() ... '?'`, in `newer()`), and
with `v1` it warned "arXiv now has v2" for three papers, which is how the
column was finally filled. The MCP `search_papers`/`get_abstract` give the
latest version (`versioned_id`, `pdf_url`), not the one the HTML rendering was
built from. **Proposal:** B1, plus `verify_sources.py` should report a
malformed version instead of raising.

### B17. `citation_graph` returns no references for the anchor (tool)

Semantic Scholar lists 0 references for arXiv:2301.04146 (36 citations
returned). "The papers it builds on" had to be read from the paper's own
bibliography with `fetch_paper.py --section References`, where the
reference numbers are printed as `(14)` and the arXiv identifiers inline.
**Proposal:** fall back to the INSPIRE reference list (already named in the
brief) inside a small helper, `fetch_paper.py --refs`.

### B18. Checker side effects on ordinary hep-th notation (tool)

- Parameter values in prose (`$s=0$`, `$d=1$`, `$t=s-1$`) are classed as
  equations; hep-th text is full of them. I added `<!-- eq: notation -->`
  where the statement holds nothing else; in mixed statements they show up
  as `unreadable`.
- A measured value with an equals sign (`$f_{\rm NL}^{\rm local}=-0.9\pm 5.1$`,
  from an abstract) is classed as an equation needing `Eq. n`. Rephrased.
- Any `[der]` in a statement makes all its digits "derived" for
  `check_numbers.py`, even those carrying `[src]`. I removed my `[der]`
  sentences or moved them to their own statements.
**Proposal:** ignore `$<symbol>=<integer or symbol>$` spans in
`is_equation`; allow `[src: abstract]` values written with `=`; scope
`[der]` to the clause it follows.

### B19. Probe-only: `check_shape.py` expects the full file set (expected)

The probe brief asks for no SKILL.md, approximations.md, open-questions.md,
so `check_shape.py` reports 3 problems. Not a rule defect.

## Research calls

36 of 40 (arXiv MCP: 6 searches, 1 abstract, 1 citation graph; fetch_paper:
28 invocations). One call wasted by B3; two to three spent on B2/B8
diagnosis (plus local inspection of the HTML cache, not counted).

## Defects I caused and fixed

- 3.23 transcribed by joining row 1's left side with row 2's right side
  (an equation the paper does not print in one piece): replaced by row 1.
- Statements mixing an `Eq. n` equation with inline equations from the text,
  or two papers: split, inline definitions put in words.
- `[der]` sentences next to sourced numbers: removed.
- Maldacena's version first written from memory as `v5`; confirmed by
  `get_abstract` (`pdf_url` …v5) before the file was checked. Year corrected
  to the arXiv year 2002 in prose.

## Checker output (final run, from the repository root)

```
$ python3 tools/check_equations.py --skill ../../docs/history/tests/p0-probe/thcosmo-primordial-correlators --list
…/references/formalism.md:66: no-eq: **The four families for $d\geq 3$** (arXiv:2301.04146) [src: Sect. 2.1, inline list of the four series]: principal series ${\cal P}_{\Delta,s}$ wi
…/references/formalism.md:67: no-eq: **Field content.** ${\cal F}_{\Delta,s}$ (principal or complementary) describes a spin-$s$ massive field of mass $m^{2}=\Delta(d-\Delta)$ when $s=
…/references/results.md:25: no-eq: **Complementary series in two-particle states, $d\geq 3$.** For each pair $(n,s)$ of non-negative integers with $\Delta_{1}+\Delta_{2}-d-s-2n>\frac{
(exit 0)

$ python3 tools/check_transcription.py --skill ../../docs/history/tests/p0-probe/thcosmo-primordial-correlators
contained  …/references/formalism.md:25 arXiv:1002.1416 Eq. 3.23
           file  : \langle Q\rangle=\langle\Omega|F^{-1}(t,t_{0})Q^{I}(t)F(t,t_{0})|\Omega\rangle~
           source: \displaystyle\langle Q\rangle= \displaystyle\langle\Omega|F^{-1}(t,t_{0})Q^{I}(t)F(t,t_{0})|\Omega\rangle~, \displaystyle= \displaystyle\langle\Omega|\left[\bar{T}\exp\left(i\int_{t_{0}}^{t}H_{I}(t)dt
contained  …/references/formalism.md:35 arXiv:1002.1416 Eq. 4.9
           file  : S_{3}=\int dtd^{3}x\bigg[a^{3}\epsilon^{2}\zeta\dot{\zeta}^{2}+a\epsilon^{2}\zeta(\partial\zeta)^{2}-2a\epsilon\dot{\zeta}(\partial\zeta)(\partial\chi)
           source: \displaystyle S_{3}= \displaystyle\int dtd^{3}x\bigg[a^{3}\epsilon^{2}\zeta\dot{\zeta}^{2}+a\epsilon^{2}\zeta(\partial\zeta)^{2}-2a\epsilon\dot{\zeta}(\partial\zeta)(\partial\chi) | \displaystyle+\fra
contained  …/references/formalism.md:49 arXiv:1002.1416 Eq. 4.23
           file  : S=\frac{\epsilon}{8}\left[-\left(\frac{k_{1}^{2}}{k_{2}k_{3}}+{\rm 2~perm.}\right)+\left(\frac{k_{1}}{k_{2}}+{\rm 5~perm.}\right)+\frac{8}{K}\left(\frac{k_{1}k_{2}}{k_{3}}+{\rm 2~perm.}\right)\right]
           source: \displaystyle S \displaystyle=\frac{\epsilon}{8}\left[-\left(\frac{k_{1}^{2}}{k_{2}k_{3}}+{\rm 2~perm.}\right)+\left(\frac{k_{1}}{k_{2}}+{\rm 5~perm.}\right)+\frac{8}{K}\left(\frac{k_{1}k_{2}}{k_{3}}+
unreadable …/references/formalism.md:66 arXiv:2301.04146 Eq. 
           file  : s=0
           source: 
unreadable …/references/formalism.md:66 arXiv:2301.04146 Eq. 
           file  : \Delta=d+p-1
           source: 
unreadable …/references/formalism.md:66 arXiv:2301.04146 Eq. 
           file  : s=0
           source: 
unreadable …/references/formalism.md:66 arXiv:2301.04146 Eq. 
           file  : \Delta=d+t-1
           source: 
unreadable …/references/formalism.md:66 arXiv:2301.04146 Eq. 
           file  : t=0,1,2\cdots,s-1
           source: 
unreadable …/references/formalism.md:67 arXiv:2301.04146 Eq. 
           file  : m^{2}=\Delta(d-\Delta)
           source: 
unreadable …/references/formalism.md:67 arXiv:2301.04146 Eq. 
           file  : s=0
           source: 
unreadable …/references/formalism.md:67 arXiv:2301.04146 Eq. 
           file  : t=s-1
           source: 
unreadable …/references/formalism.md:67 arXiv:2301.04146 Eq. 
           file  : \phi(x)\to\phi(x)+c
           source: 
unreadable …/references/models.md:10 arXiv:1002.1416,astro-ph/0407059 Eq. 4.18,4.23,4.22,1
           file  : P_{\zeta}=\frac{H^{2}}{8\pi^{2}\epsilon}~
           source: 
unreadable …/references/models.md:10 arXiv:1002.1416,astro-ph/0407059 Eq. 4.18,4.23,4.22,1
           file  : f_{NL}\sim{\cal O}(0.01)
           source: 
contained  …/references/results.md:13 arXiv:2604.09765 Eq. 14
           file  : \lim_{\vec{k}_{1}\rightarrow 0}\langle\zeta(\vec{k}_{1}\dots\zeta(\vec{k_{N}})\rangle^{\prime}=\langle\zeta(\vec{k_{1}})\zeta(-\vec{k}_{1})\rangle^{\prime}\delta_{\zeta}\langle\zeta(\vec{k}_{2})\dots\
           source: \boxed{\begin{aligned} \lim_{\vec{k}_{1}\rightarrow 0}\langle\zeta(\vec{k}_{1}\dots\zeta(\vec{k_{N}})\rangle^{\prime}=\langle\zeta(\vec{k_{1}})\zeta(-\vec{k}_{1})\rangle^{\prime}\delta_{\zeta}\langle\
unreadable …/references/results.md:25 arXiv:2301.04146 Eq. 
           file  : \Delta_{1}+\Delta_{2}-d-s-2n>\frac{d}{2}
           source: 
../../docs/history/tests/p0-probe/thcosmo-primordial-correlators: 38 equations; 22 exact, 4 contained, 0 mismatch, 12 unreadable

$ python3 tools/check_numbers.py --skill ../../docs/history/tests/p0-probe/thcosmo-primordial-correlators --list
(no output)

$ python3 tools/check_shape.py --skill ../../docs/history/tests/p0-probe/thcosmo-primordial-correlators
thcosmo-primordial-correlators: SKILL.md missing
thcosmo-primordial-correlators: references/approximations.md missing
thcosmo-primordial-correlators: references/open-questions.md missing
thcosmo-primordial-correlators: 3 problem(s)

$ python3 plugin/skills/theoretical-cosmology/scripts/verify_sources.py docs/history/tests/p0-probe/thcosmo-primordial-correlators
thcosmo-primordial-correlators: 10 sources, 0 problem(s) [arXiv-checked]
```

Remaining `no-eq` (3) and `unreadable` (12) are all of kinds B10, B13, B14
and B18 (rules/tools); `contained` (4) are B6/B15 and B9 (`\boxed`).

## Summary by kind

| Kind | Cases | Proposal |
|---|---|---|
| Rendering without equation numbers or sections | B2 (Maldacena 2002, harvmac) | PDF place form; tool diagnostic "0 tagged displays"; `[sec]` via review |
| Letters without sections | B7 (Creminelli & Zaldarriaga 2004) | `[src: text after Eq. n]`, `[src: footnote n]` |
| Results in tables, table footnotes, inline math | B10, B13 (Penedones et al. 2023) | inline and table-footnote place forms; inline search in checker |
| Multi-row displays | B6, B15 | define cell/row concatenation; compare span sequences |
| Source slips (no erratum) | B4, B9 | `as printed; slip noted` flag, words only |
| Pre-arXiv foundations | B12 | treat like textbooks, `[sec]` via readable source |
| Version not readable | B1, B16 | print version in `fetch_paper`; no crash |
| Tool output gaps | B3, B8, B11, B17 | section numbers, keep displays in context, clean footnote marks, refs fallback |
| Normaliser gaps | B5, B9 | strip `~`, `\boxed`, `aligned` |
| Checker classing | B13, B14, B18 | inline places, per-equation paper attribution, ignore `s=0` |

No conventions mixed within one paper were found in the three papers read
closely (Chen 2010 is internally consistent; it differs from Maldacena 2002
in the definition of $\eta$, and from Creminelli & Zaldarriaga 2004 in the
normalisation of the power spectrum, both recorded in formalism.md without a
conversion). No erratum was found. No equation was too long to transcribe
(Chen Eq. 4.9 is the longest, three rows).
