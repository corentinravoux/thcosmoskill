# Gate log

One entry per gated run: date, run, gate (G1 tools, G2 sample re-read, G3
dossiers), what was checked, result, fixes. Plan:
`docs/plans/2026-10-30-plan-v2.md`, "How one domain is built".

## 2026-10-30 — base 0.1.0

- Anchor bibliography `docs/anchor-sources.tsv`: 66 papers, built from
  identifiers looked up this session; `verify_sources.py` online, 0
  problems. Before the lookup, three of fifty-one identifiers recalled from
  memory pointed to other papers (1105.5280, 1001.4707, 1201.5375); each was
  replaced by the paper the arXiv record gives or corrected in the row.
- Test suite: 112 passed, 1 skipped (icon not yet drawn).

## 2026-10-30 — plan v2, stage 1 (docs aligned with the decisions)

- Hub router: 19 domains; `gr-background` folded, `relics` → `pbh-defects`,
  `theory-codes` conditional. Hub skeletons `methods-index.md`,
  `stale-claims.md` added.
- `scopes-domains.md`, `suite-conventions.md`, `agent-brief.md`, README,
  design spec updated. Brief and conventions example (F₂ kernel,
  arXiv:astro-ph/0112551 Eq. 45) re-read in the paper with `fetch_paper.py
  --grep "(45)"`.
- `docs/anchor-sources.tsv`: `version` column from the arXiv API; six
  seeds added (2302.09032, 2303.15565, 1511.08641, 2410.17109, 2607.22914,
  2301.04146); `verify_sources.py` online on the 72 rows: 0 problems.
- Tests: 112 passed, 1 skipped; `check_numbers.py --list` empty.

## 2026-10-30 — plan v2, stage 2 (tooling)

Tools added, each with tests; suite at the end of the stage: all tests pass.

- T8 `verify_sources.py`: `version` column; legacy six-column tables read as
  version `-`; warning when arXiv has a newer version.
- T1 `tools/latex_norm.py` and `check_numbers.py`: equations read first;
  the four strings of the review (F₂ kernel, n_s − 1 = −2/N, BBKS transfer
  function, `\hskip`) and 21 more in `tests/fixtures/theory-statements.tsv`
  (a TSV rather than the planned Markdown file, for exact expected values).
- T2 `check_equations.py`, zero baseline. T2b `check_transcription.py`:
  the hub's F₂ example is `exact` against the real rendering of
  arXiv:astro-ph/0112551, Eq. 45.
- T4b `check_places.py`; T4 `sample_statements.py` (bound for 0 errors in
  59: 4.95 %); T6 `check_shape.py`; T9 model-status dates in
  `refresh_status.py`; T11 `word_share.py`.
- T5 briefs rewritten (dossier, numbers, refresh, deepen); rebalance brief
  removed.
- T10 `tools/run_questions.py` (named for its wider use: trigger test, E2
  baseline, Q0 run, blind sheet and scoring). Smoke test on three
  questions with the plugin on: all three loaded the hub
  (`thcosmoskill:theoretical-cosmology`), which routed to the planned domain
  and said it is not built; 0 of 3 used the expected domain skill, as
  expected with no domain built. Cost per question 267k–390k tokens, mostly
  cache reads (the session reports 0.38–0.45 USD, an estimate at API list prices; the runs used the owner's subscription login, `apiKeySource: none`, so nothing is billed in dollars: the runs count against the plan's usage limits). One answer began
  with a message of the claude-mem hook of the owner's setup: the
  environment's hooks appear in headless answers, in both baseline and
  skills-on runs alike.
- E1 template written, then removed the same day when the owner withdrew
  the evaluation stage from the plan (D24–D28).

## 2026-10-31 — stage 3, P0 hep-th probe (gated)

Run: three subtopics of `thcosmo-primordial-correlators` staged in
`docs/history/tests/p0-probe/`, 36 of 40 research calls, 10 sources
(`verify_sources` online: 0 problems). Nineteen breakages logged in
`docs/history/tests/p0-probe.md` (B1–B19). Coordinator's response:

- Tools fixed: `latex_norm` strips `~`, `\boxed`, `\framebox`, aligned
  environments and alignment marks; parameter assignments (`$s=0$`) and
  measured values with errors are not equations (B5, B9, B18).
  `check_transcription` parses the rendering's equation tables directly
  (rows and cells joined, unnumbered rows attached to the next numbered
  one), attributes each equation to the nearest paper and flag, compares
  consecutive spans joined, and searches inline mathematics for
  `inline` / `text after Eq. n` places (B6, B10, B13, B14, B15).
  `check_equations` accepts inline places; `check_places` reads
  `text after Eq. n`, `footnote n` and dotted table numbers (B7);
  `check_numbers` scopes `[der]` to its sentence (B18); `verify_sources`
  no longer crashes on a malformed version (B16). `fetch_paper` prints the
  latest version with `--abstract`, the rendering's version and its count
  of numbered displays in the other headers ("none tagged" for
  harvmac-era renderings), takes `--section "Sect. 4"` for the paper's
  own numbering, and prints footnote marks once as `[fn n]` (B1, B2, B3,
  B11). Tests: `tests/test_probe_fixes.py`.
- Not reproduced: B8 (`--context` counts a display as one block; the
  display after a context window is not dropped, only outside it). Now
  documented in the brief.
- Not changed: B11 mangled HTML titles (cosmetic), B17 (references through
  INSPIRE named in the brief instead of a new network helper), B19
  (probe-only).
- Rules added to `suite-conventions.md` and the brief: places for inline
  equations, letters, table footnotes; multi-row displays copied whole;
  untagged renderings through a readable secondary source; textbooks and
  pre-arXiv papers alike; slips copied as printed and described in words,
  recorded in `stale-claims.md`; one citation and flag after each paper's
  equations.
- Effect on the probe's own files: 22 → 25 exact, 12 → 6 unreadable,
  0 mismatch (the 6 are inline equations placed by section only, left to
  the G2 re-read). The staged text is kept as the start of the
  correlators build (stage 4).

## 2026-10-31 — stage 3, P4 conventions atlas (G1 passed; G2 running)

Run: 89 of 90 research calls; `conventions.md` 323 lines, 15 conventions,
27 sources (`verify_sources` online: 0 problems).

- G1: `check_numbers` and `check_equations` empty; `check_transcription`
  118 equations, 82 exact, 7 contained, 0 mismatch, 29 unreadable;
  `check_places` 4 statements, 3 found at place, 1 found elsewhere; tests
  pass. Reports in `docs/history/tests/transcription/` and `places/`.
- Generality: Baumann 2009 (arXiv:0907.5424) holds 16.4 % of citations,
  above the 15 % flag. Kept: the TASI lectures are the convention
  reference for several entries of the early-universe and perturbation
  tables, and every such entry also cites at least one other work; the
  owner's papers: 0 %.
- Two printed slips reported by the run were confirmed by the coordinator
  at source and recorded in `stale-claims.md`: arXiv:2212.08488 Eq. 28 (F₂
  and G₂ dipole terms without the factor one half of arXiv:astro-ph/0112551
  Eq. 45); arXiv:0907.5424 Sect. 9.2.3 ("equal") against Eq. 141 (−ζ).
- Not verified (from the run): sign and definition of Ω_K; the bias review
  arXiv:1611.09787 (no HTML rendering); Galileon bias operators; f_NL sign
  conversion between ζ conventions; n_s and r beyond leading order;
  isocurvature normalisation; α_i definitions and α_B conversion.
- G2 sheet: `docs/history/tests/g2/theoretical-cosmology-atlas-2026-10-31.md`
  (100 items, seed 31), re-read by a second session.

## 2026-10-31 — stage 3, P4 atlas, G2 re-read (second session)

Sheet: `docs/history/tests/g2/theoretical-cosmology-atlas-2026-10-31.md`,
100 items. Part 1: 1 ok. Part 2: 39 ok, 1 wrong (a CAMB `[doc]` fact
cited from `results.py` where the unit is stated in `initialpower.py`).
Part 3 (draw of 59): every equation and equation number exact; one place
label wrong (Baumann Eq. 1 placed in Sect. 1, it is in Sect. 3.1), so under
the strict rule the draw has **1 error** and does not pass. Further
place-label slips outside the draw: Sect. 9.2.1 display is numbered (119);
Malik & Wands' Planck-mass entry is in the List of Symbols, not App. A.1;
Komatsu's ζ = 5Φ/3 is before Eq. 24.

Coordinator: all six corrected after re-reading each at source; per-
equation flags where one row held equations from two places. Pattern
(free-text section labels) fixed mechanically: `check_transcription`
now classes `wrong-section` when the section or appendix named does not
contain the numbered display, and appendix labels (`Eq. A.1`) are read by
all checkers. After the fixes: 118 equations, 85 exact, 7 contained,
0 mismatch, 0 wrong-section, 26 unreadable. **A fresh draw (new seed) is
due** before the atlas passes G2; it is run with the pilot's G2.

## 2026-10-31 — stage 3, P1 pilot `thcosmo-lss-perturbation-theory` (G1 passed; G2 running)

Run: about 85 of 90 research calls; SKILL.md 134 lines, formalism 156,
models 125 (11 model cards), approximations 114, open questions 72,
results 54; 49 sources, 12 subtopics (two thin: velocity statistics and
momentum power spectrum; perturbative forward models). Four reference
files are under the brief's 150 lines: dense paragraphs, to be judged at
the owner's review (P2).

- G1: `verify_sources` online 0 problems; `check_numbers` 0 without paper
  and place (12 marked); `check_equations` empty; `check_transcription`
  125 equations, 119 exact, 0 mismatch, 0 wrong-section, 6 unreadable;
  `check_places` 41 statements, 30 found at place, 2 elsewhere, 9
  unreadable; `check_shape` 0 problems; tests pass.
- Generality: Bernardeau 14.5 %, Ivanov 13.9 %, Cabass 9.9 % of
  citations; owner's papers 0 %.
- Two printed slips reported by the run, confirmed by the coordinator at
  source and recorded in `stale-claims.md`: arXiv:2212.08488 Eq. 32
  (P₁₃ written with δ⁽²⁾ next to an F₃ integral) and Eq. 39 (UV limit
  labelled q ≪ k).
- Not read (from the run): arXiv:1611.09787 (no HTML rendering), Kaiser
  1987, RPT and RegPT papers.
- G2 sheet: `docs/history/tests/g2/thcosmo-lss-perturbation-theory-2026-10-31.md`
  (90 items, seed 1031). Owner review sheet (P2):
  `docs/history/tests/p2/thcosmo-lss-perturbation-theory-review.md`.
- Atlas fresh draw: `docs/history/tests/g2/theoretical-cosmology-atlas-2026-10-31-redraw.md`
  (seed 77), part 3 to be re-read.

## 2026-10-31 — stage 3, P6 overlap with cosmoskill

`docs/overlap-cosmoskill.md`: the pilot shares with cosmoskill's
`cosmo-theory-foundations` its sections 8 (redshift space), 9 (PT and EFT
ingredients), 10 (bias expansions) and the EFT dossier; the home of the
formalism is thcosmoskill (D9). cosmoskill 1.0.4 (commit on its `main`,
tag left to the owner): one routing paragraph in its hub, one pointer
sentence in each shared section and the dossier; existing text kept so it
still answers alone; `releases/1.0.4.tsv` lists the 5 changed sections;
its tests pass. `cosmo-galaxy-clustering`'s full-shape dossier stays
cosmoskill's (analysis practice).

G2 re-reads of the pilot and of the atlas's fresh draw were cut by the
usage limit on 2026-10-31 and resumed on 2026-11-02.

## 2026-11-02 — stage 3, P4 atlas, G2 fresh draw: **passed**

Sheet: `docs/history/tests/g2/theoretical-cosmology-atlas-2026-10-31-redraw.md`
(seed 77). Part 3: 59 of 59 ok, 0 wrong: the atlas passes G2 (error rate of
tool-passed items below 5 % at 95 %). The corrected lines 73, 88 and 181
fell in the draw and are ok. Parts 1–2, corrected rows re-read: 2 ok, 1
wrong (line 43: the units statement of Malik & Wands is in App. A.1,
"Notation"; the label named only the List of Symbols and Sect. 11).
Coordinator re-read App. A.1 and corrected the label. Pattern unchanged:
equations exact; a row drawing on several places can miss one in its
label.

## 2026-11-02 — stage 3, P1 pilot, G2: **passed**

Sheet: `docs/history/tests/g2/thcosmo-lss-perturbation-theory-2026-10-31.md`
(90 items, seed 1031). Part 1: 18 ok. Part 2: 12 ok, 1 wrong. Part 3: 59
ok, 0 wrong: the pilot passes G2. No wrong section, appendix or equation
label anywhere.

- Wrong item: `open-questions.md:29` turned the printed ratios of
  arXiv:2005.04805 (about 1.003 for the monopole, 1.007 for the quadrupole,
  abstract) into percentages, a number of the agent's own making.
  Coordinator re-read the abstract and restated the ratios; a typo on line
  49 fixed. Pattern: the brief now states that numbers are quoted in the
  form the paper prints them (rule 2).
- Checker fix found on the way: an `inline` place with a section but no
  "text after Eq. n" was compared with the wrong pool of inline equations
  (two false mismatches in the atlas); it now goes to the person's re-read.
  Label fragments quoted in `stale-claims.md` marked `eq: notation`.
- After the fixes: atlas 118 equations, 85 exact, 0 mismatch; pilot 125
  equations, 119 exact, 0 mismatch; tests pass.
- The hub router marks the pilot as built (under the owner's review, no
  dossiers yet). Next: P2 owner review; P7 gap audit and dossiers.

## 2026-11-02 — stage 3, P7 pilot dossiers (G1 passed; G3 re-read running)

Six dossiers from the gap audit, two runs of three (about 55 and 75
research calls): `one-loop-eft-power-spectrum` (141 lines),
`ir-resummation` (132), `redshift-space-eft` (135),
`bias-renormalisation-and-bases` (147), `png-scale-dependent-bias` (108),
`velocity-momentum-statistics` (114). Subtopic velocity-momentum moved from
thin to covered; field-level forward models stays thin (deepening run
later).

- G1 on the whole skill: 83 sources, 0 problems; `check_numbers` and
  `check_equations` empty; `check_transcription` 356 equations, 299
  exact, 21 contained, 0 mismatch, 0 wrong-section, 36 unreadable;
  `check_shape` 0 problems; tests pass. Generality: Ivanov 14.9 %,
  Bernardeau 9.0 %; owner 0 %.
- One `[der]` paragraph in `png-scale-dependent-bias` (b_φ left free by
  renormalisation, reasoned from Assassi et al. 2015, arXiv:1510.03723, Eq. 2.53) is marked as
  the agent's reasoning, carries no number; kept, flagged for the owner.
- Eight further printed slips reported by the runs: seven confirmed by the
  coordinator at source (arXiv:2212.08488 Eqs. 25, 27, 32, 110;
  arXiv:1708.08130 Eqs. 2.26, 2.28; arXiv:1605.02149 Eq. 7.3) and recorded
  in `stale-claims.md`; one (Chan et al. arXiv:1201.3614 Eq. 116) recorded
  as reported by arXiv:1812.03208 and not checked in the source, whose
  rendering shows no Eq. 116.
- `sample_statements.py --only /deep/`: the G3 sheet covers the new files;
  `docs/history/tests/g2/thcosmo-lss-perturbation-theory-dossiers-2026-11-02.md`
  (part 2: 89 items, part 3: 59 items, seed 1102).

## 2026-11-02 — stage 3, P7 pilot dossiers, G3: **passed**

Sheet: `docs/history/tests/g2/thcosmo-lss-perturbation-theory-dossiers-2026-11-02.md`,
two reviewers. Part 3 (draw of 59, seed 1102): 59 ok, 0 wrong: G3 passes.
Part 2 (89 items the tools could not pass): 87 ok, 2 wrong reported.

Coordinator, after re-reading each at source:
- `ir-resummation.md:28`: "of order one in ΛCDM" is not in arXiv:1404.5954;
  replaced by the paper's own wording, "in our Universe controls the
  largest non-linearity in the range of scales of interest for the BAO"
  [src: Sect. 1]. Brief rule 2 now asks that qualitative claims of size be
  quoted.
- `ir-resummation.md:91`: reported wrong place (Sect. 7.1 for k_osc =
  h/(110 Mpc)); rejected: Sect. 7.1 prints the value in exactly this form
  (it is also defined in Sect. 1).
- Next to drawn items, reported by the part-3 reviewer:
  `one-loop-eft-power-spectrum.md:37` label corrected to "text after
  Eq. 31" (the statement is in the paper, after Eq. 31, not Eq. 30);
  `ir-resummation.md:49` label corrected to Sect. 3.2, where arXiv:1605.02149
  says both that observables do not depend on k_S when computed exactly
  and that residual dependence estimates the theoretical uncertainty.
- After the fixes: 356 equations, 299 exact, 0 mismatch, 0 wrong-section;
  tests pass. The hub router marks the pilot as built with six dossiers,
  under the owner's review.

## 2026-11-02 — stage 4, build `thcosmo-inflation` (G1 passed; G2 running)

Run: 76 of 90 research calls; SKILL.md 127 lines, formalism 150, models
133 (12 model cards), approximations 88, open questions 58, results 79;
48 sources; 9 subtopics (slow roll and flow parameters, single-field
models, attractors, ultra-slow and constant roll, multi-field, reheating and
preheating, initial conditions, stochastic and eternal inflation, n_s and r
after ACT DR6).

- G1: `verify_sources` online 0 problems; `check_numbers` and
  `check_equations` empty; `check_transcription` 142 equations, 125 exact,
  14 contained, 0 mismatch, 0 wrong-section, 3 unreadable (inline in
  arXiv:1807.06211 and arXiv:2203.07629); `check_places` 41 statements, 20
  found at place, 0 elsewhere, 0 not found, 21 unreadable; `check_shape` 0
  problems; tests pass.
- Generality: Martin 17.6 % (flag), Planck Collaboration 14.5 %, Baumann
  9.2 %; owner's papers 0 %. Martin's share is one source,
  Encyclopaedia Inflationaris (arXiv:1303.3787), the catalogue of
  single-field models with their slow-roll predictions that the model cards
  quote one by one; kept, justified.
- Printed slip reported by the run, confirmed by the coordinator at source
  and recorded in `stale-claims.md`: arXiv:1807.06211 Sect. 4.2, quartic
  hilltop limit printed with $\mu_{2}$.
- G2 sheet: `docs/history/tests/g2/thcosmo-inflation-2026-11-02.md`
  (107 items: 19 + 29 + 59, seed 1103).

## 2026-11-02 — stage 4, build `thcosmo-primordial-correlators` (G1 passed; G2 running)

Run: 59 of 90 research calls, started from the P0 probe text (kept, an
f_NL escape and one Maldacena place fixed); SKILL.md 131 lines, formalism
189, models 84 (7 model cards), approximations 108, open questions 70,
results 120; 79 sources; 10 subtopics (the seed list).

- G1: `verify_sources` online 0 problems; `check_numbers` and
  `check_equations` empty; `check_transcription` 110 equations, 93 exact,
  10 contained, 0 mismatch, 0 wrong-section, 7 unreadable (Penedones inline
  and table equations); `check_places` 9 statements, 4 found at place, 5
  unreadable; `check_shape` 0 problems; tests pass (155).
- Generality: Chen 14.1 %, Cheung 7.7 %, Achúcarro 5.9 %; none above
  15 %; owner's papers 0 %.
- Printed slips reported by the run, confirmed by the coordinator at
  source and recorded in `stale-claims.md`: arXiv:1002.1416 Eqs. 2.1 and 4.1
  ($M_{\rm P}$ not squared; the run named Eq. 4.1 only); arXiv:2203.08128
  Sect. 4.1 (sharp feature described with the slow-roll inequality).
- Not read (from the run): Maldacena 2002 at source (rendering without
  equation numbers); Starobinsky–Yokoyama (abstract only).
- G2 sheet: `docs/history/tests/g2/thcosmo-primordial-correlators-2026-11-02.md`
  (102 items: 23 + 20 + 59, seed 1104).
- Both runs: 14 `eq: notation` escapes in total.

## 2026-11-02 — stage 4, `thcosmo-primordial-correlators` G2: **passed**

Sheet: `docs/history/tests/g2/thcosmo-primordial-correlators-2026-11-02.md`
(102 items, seed 1104). Part 1: 23 ok. Part 2: 20 ok. Part 3: 59 ok, 0
wrong: the skill passes G2. No equation, number or place wrong.

Coordinator, after re-reading each reviewer note at source:
- `formalism.md:74`: the tie between $\dot{\pi}(\partial_{i}\pi)^{2}$ and
  the sound speed is stated after Eq. 41 of arXiv:0709.0293, the free
  $M_{3}$ coefficient after Eq. 44; the line now names both places.
- Wording brought back to the paper: `SKILL.md:34` ("bulk particle
  production in a weakly coupled background", arXiv:2203.08128, not "weak
  mixing"); `approximations.md:77` ($m^{2}=\Delta(d-\Delta)$ holds for
  $s=0$ only); `formalism.md:169` (the paper's hedge "is expected to
  describe" for ${\cal V}_{1,0}$); `models.md:74` ("by up to").
- Pattern: hedges and qualifiers of the source dropped in paraphrase,
  already covered by brief rule 2.
- Hub router: built; README row updated.

## 2026-11-02 — stage 4, `thcosmo-inflation` G2: **passed**

Sheet: `docs/history/tests/g2/thcosmo-inflation-2026-11-02.md` (107 items,
seed 1103). Part 1: 19 ok. Part 2: 27 ok, 1 wrong, 1 unclear. Part 3: 59
ok, 0 wrong: the skill passes G2.

Coordinator, after re-reading each at source:
- Wrong, `models.md:7`: "the Encyclopaedia covers more than seventy
  potentials" had no source and is not printed; replaced by the abstract of
  arXiv:1303.3787 (v5): ASPIC "presently supports 118 different models".
  Pattern: an untagged summary sentence in a file preamble; the brief's
  rule 1 already forbids it.
- Unclear, `formalism.md:58`: $V=M^{4}v$ is written in Sect. 3.1, text
  before Eq. 33, not in Eq. 35; the label now names both places.
- After the fixes: 143 equations, 125 exact, 15 contained, 0 mismatch;
  `check_numbers` and `check_equations` empty.
- Hub router: built; README row updated.

## 2026-11-02 — stage 4, build `thcosmo-modified-gravity` (G1 passed; G2 running)

Run: about 70 of 90 research calls; SKILL.md 125 lines, formalism 171,
models 140 (13 model cards), approximations 60, open questions 64, results
79; 85 sources; 11 subtopics, so no split (D6); vector–tensor,
teleparallel and f(Q), non-local gravity marked thin.

- G1: `verify_sources` online 0 problems; `check_numbers` and
  `check_equations` empty; `check_transcription` 92 equations, 65 exact,
  12 contained, 0 mismatch, 0 wrong-section, 15 unreadable (inline or
  unnumbered places, all in part 2 of the G2 sheet); `check_places` 26
  statements, 11 found at place, 15 unreadable; `check_shape` 0 problems;
  tests pass (155).
- Generality: Kobayashi 16.9 % (flag), Euclid Collaboration 13.8 %, de Rham
  7.7 %; owner's papers 0 %. Kobayashi's share is four papers, 53 of the 70
  citations to the Horndeski review arXiv:1901.07183, the reference the
  scalar–tensor sections transcribe their Lagrangians from; the other three
  are distinct results (G-inflation, Vainshtein breaking, unscreened
  multipoles); kept, justified. The Euclid share is its theory review,
  quoted [sec] for bounds whose primary sources were not read (listed
  under "Not verified").
- Printed slips reported by the run, confirmed by the coordinator at
  source and recorded in `stale-claims.md`: arXiv:1404.3713 Eq. 13 (scalar
  gradient term not squared); arXiv:1407.0059 Fig. 9 caption (Λ for Λ⁻¹).
- G2 sheet: `docs/history/tests/g2/thcosmo-modified-gravity-2026-11-02.md`
  (107 items: 12 + 36 + 59, seed 1105).

## 2026-11-03 — stage 4, `thcosmo-modified-gravity` G2: **passed**

Sheet: `docs/history/tests/g2/thcosmo-modified-gravity-2026-11-02.md`
(107 items, seed 1105). Part 1: 12 ok. Part 2: 30 ok, 5 wrong, 1 unclear.
Part 3: 59 ok, 0 wrong: the skill passes G2. Every equation matched as
printed.

Coordinator, after re-reading each at source (all wrongs are dropped
hedges or qualifiers):
- `formalism.md:139`: arXiv:1404.3713 Sect. 3.3 says $c_{\rm s}$ is "not in
  general equivalent" to $C^{2}$, which "usually depends on scale"; quoted.
- `approximations.md:29`: arXiv:2604.15434 adds "for the range of tested
  values"; arXiv:2607.24940 lists the normal and self-accelerating DGP
  models; both restored.
- `models.md:32`: arXiv:0705.1158 conditions on the halo "and local
  environment", "substantially deeper", "during the acceleration epoch";
  quoted.
- `models.md:34`: arXiv:2009.08743 bounds hold in the Compton-wavelength
  range 0.3–8 Mpc; restored.
- `models.md:81`: arXiv:2609.10760 counts 199 "symmetry-inequivalent"
  amplitudes; restored.
- Unclear, `open-questions.md:53`: the link between DGP and the galileon
  is in arXiv:0811.2197 (abstract), not in arXiv:1707.02263; both now
  cited at their place.
- After the fixes: 92 equations, 65 exact, 0 mismatch; `check_numbers` and
  `check_equations` empty; tests pass.
- Pattern: qualifiers dropped in paraphrase, the same as in the
  correlators gate; brief rule 2 covers it. The next build prompts add an
  explicit line: keep the paper's hedges.
- Hub: router built; README row; six entries in `stale-claims.md`.

## 2026-11-03 — stage 5 W1, build `thcosmo-dark-energy` (G1 passed; G2 running)

Run: about 78 of 90 research calls; SKILL.md 127 lines, formalism 127,
models 176 (16 model cards), approximations 69, open questions 66, results
60; 61 sources; 9 subtopics (Λ problem, quintessence, k-essence and
Chaplygin, phantom and crossing, interacting dark energy, early dark energy
as formalism, phenomenological classes, perturbations and PPF, post-DESI
model building).

- G1: `verify_sources` online 0 problems; `check_numbers` and
  `check_equations` empty; `check_transcription` 125 equations, 97 exact,
  26 contained, 0 mismatch, 0 wrong-section, 2 unreadable; `check_places`
  27 statements, 14 at place, 2 elsewhere, 11 unreadable; `check_shape` 0
  problems.
- Generality: Copeland 17.4 % (flag), Li 13.1 %, Ren 6.1 %, Poulin 6.1 %;
  owner's papers 0 %. Copeland's share is one source, the review "Dynamics
  of dark energy" (arXiv:hep-th/0603057), 55 citations, from which the
  scalar-field formalism is transcribed; kept, justified.
- Printed slips reported by the run, confirmed by the coordinator at source
  and recorded in `stale-claims.md`: arXiv:hep-th/0603057 Eq. 179 (+V) and
  Sect. IV.2 ("10^{121} orders of magnitude"); arXiv:2302.09032 Eq. 24
  ($c_{a}^{2}$ inverted).
- G2 sheet: `docs/history/tests/g2/thcosmo-dark-energy-2026-11-03.md`
  (106 items: 14 + 33 + 59, seed 1106).

## 2026-11-03 — stage 5 W1, build `thcosmo-dark-matter-models` (G1 passed; G2 waiting for a slot)

Run: 76 of 90 research calls; SKILL.md 125 lines, formalism 122, models
135 (12 model cards), approximations 95, open questions 74, results 80; 66
sources; 12 subtopics, 10 covered, 2 thin (dark sectors, gravitational
production). All five reference files are under the brief's 150 lines;
judged dense, not padded.

- G1: `verify_sources` online 0 problems; `check_numbers` and
  `check_equations` empty; `check_transcription` 136 equations, 55 exact,
  28 contained, 0 mismatch, 0 wrong-section, 53 unreadable (abstract values
  and inline equations: all in part 2 of the G2 sheet, re-read by hand);
  `check_places` 52 statements, 30 at place, 22 unreadable; `check_shape` 0
  problems.
- Generality: Safdi 15.6 % (flag), Bernal 5.7 %, Viel 5.1 %; owner's papers
  0 %. Safdi's share is one source, the TASI lectures arXiv:2303.02169
  (53 citations), the formalism reference for axions and freeze-out; kept,
  justified.
- Printed slips reported by the run, confirmed by the coordinator at source
  and recorded in `stale-claims.md`: arXiv:2507.00705 (sign of the
  $m_{22}$ exponent against arXiv:astro-ph/0003365; sign of the quantum
  term in $\gamma^{2}$; unit "M⊙ kpc³"); arXiv:1801.08609 Eqs. 16–17
  (Maxwellian normalised by $\bar{v}^{3/2}$).
- Not read: the pre-arXiv foundations (Lee–Weinberg, Gondolo–Gelmini,
  Griest–Seckel, misalignment papers).
- G2 sheet: `docs/history/tests/g2/thcosmo-dark-matter-models-2026-11-03.md`
  (170 items: 20 + 91 + 59, seed 1107).

## 2026-11-03 — stage 5 W1, `thcosmo-dark-energy` G2: **failed the draw**, fixed, fresh draw running

Sheet: `docs/history/tests/g2/thcosmo-dark-energy-2026-11-03.md` (106
items, seed 1106). Part 1: 11 ok, 2 wrong, 1 unclear. Part 2: 31 ok, 2
wrong. Part 3: 57 ok, 1 wrong, 1 unclear: the draw fails (D20).

Coordinator, after re-reading each at source:
- `SKILL.md:55`, `approximations.md:64` (wrong): "120 orders of magnitude"
  attributed to arXiv:1205.3365, whose abstract prints 122; 120 is printed
  by arXiv:2606.20778 (abstract). Both now quoted with their own paper.
  `check_places` had classed both "found-elsewhere": an elsewhere number is
  now read by the coordinator at G1, not left to G2.
- `SKILL.md:37` (wrong): the "toy potential" of arXiv:2302.09032 is now
  quoted with both routes of Sect. III.1 (instanton corrections with
  fine-tuning, or an axion–dilaton interaction).
- `approximations.md:28` (wrong): "typically" restored (arXiv:0712.3450).
- `models.md:146` (wrong, in the draw): "many analyses assume" ν̃ = ν/2
  replaced by the paper's words: the most recent constraints it cites use
  "the simplified assumption" (arXiv:2504.01669, Sect. 4.2.1.e).
- `SKILL.md:33` (unclear): Vikman's hedges ("generally", dominance,
  quadratic Lagrangians) now quoted; the unqualified no-go is attributed to
  arXiv:2606.01360 only.
- `open-questions.md:52` (unclear): the few×10⁻² mag level is the
  sensitivity the review names, not its requirement; restated.
- Same pattern searched in the whole skill (unquoted "usually", "most",
  "commonly", "many"): three more fixed at source (`approximations.md:19`,
  arXiv:1603.08299 Sect. 4.2; `approximations.md:33`; `models.md:114`,
  arXiv:2302.09032 Sect. III.1 "it is now conventional to trade").
- After the fixes: 126 equations, 97 exact, 0 mismatch; `check_numbers`
  and `check_equations` empty; `check_places` 0 found-elsewhere.
- Fresh draw: `docs/history/tests/g2/thcosmo-dark-energy-2026-11-03-redraw.md`
  (seed 1108); part 1 and part 3 to be re-read.
