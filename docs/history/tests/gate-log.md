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

## 2026-11-03 — stage 5 W1, `thcosmo-dark-matter-models` G2: **failed the draw**, fixed, fresh draw waiting

Sheet: `docs/history/tests/g2/thcosmo-dark-matter-models-2026-11-03.md`
(170 items, seed 1107). Part 1: 19 ok, 1 unclear. Part 2: 89 ok, 1 wrong,
1 unclear. Part 3: 58 ok, 1 wrong: the draw fails (D20).

Coordinator, after re-reading each at source:
- `formalism.md:115` (wrong, in the draw): $|\alpha_{k}|^{2}-|\beta_{k}|^{2}=1$
  of arXiv:2312.09042 stated for all particles; the paper writes it for the
  scalar field of its Sect. III (Sect. III.2, text after Eq. 17); the scope
  is now named and the relation called the bosonic one.
- `approximations.md:14` (wrong): the Boltzmann-equation claim was labelled
  "abstract" of arXiv:1204.3622, which does not print it; replaced by the
  abstract's own words.
- `formalism.md:10` (unclear): units are now attributed paper by paper
  (Arbey and Mahmoudi; Marsh "(mostly)", Notes; Safdi and Bernal et al.
  print none).
- `models.md:60` (unclear): "the first" WMAP + Lyman-α limit is not printed
  by arXiv:astro-ph/0501562; now "an early".
- Same pattern searched in the whole skill (scope or qualifier dropped,
  unquoted generalisations): one more fixed (`open-questions.md:14`, "in
  the post-inflationary scenario" restored, arXiv:2007.04990 abstract).
- After the fixes: 136 equations, 0 mismatch; `check_numbers` and
  `check_equations` empty.
- Fresh draw: `docs/history/tests/g2/thcosmo-dark-matter-models-2026-11-03-redraw.md`
  (seed 1109); part 1, part 3 and the fixed part-2 rows to be re-read.
- Pattern across W1 so far: the errors left after G1 are scope and
  qualifiers, not equations; every equation re-read in W1 matched.

## 2026-11-03 — stage 5 W1, build `thcosmo-neutrinos-light-relics` (G1 passed; G2 waiting)

Run: 62 of 90 research calls; SKILL.md 126 lines, formalism 123, models 79
(7 model cards), approximations 58, open questions 38, results 84; 49
sources; 9 subtopics (light sterile neutrinos thin).

- G1: `verify_sources` online 0 problems; `check_numbers` and
  `check_equations` empty; `check_transcription` 97 equations, 72 exact, 25
  contained, 0 mismatch, 0 unreadable; `check_places` 56 statements, 27 at
  place, 2 not found, 27 unreadable; `check_shape` 0 problems. The two
  "not found" (`models.md:60`, `results.md:57`) read by the coordinator in
  the abstract of arXiv:2107.09664: printed as quoted (the list
  "$m_X\leq 11.2, 1.06, 1.56$ eV" defeats the tool).
- Generality: Lesgourgues 19.1 % (flag), Dvorkin 12.1 %, Bennett 8.6 %;
  owner's papers 0 %. Lesgourgues's share is two sources, 47 citations to
  the review "Massive neutrinos and cosmology" (arXiv:astro-ph/0603494),
  the formalism reference of the domain, and the CLASS neutrino paper; kept,
  justified.
- Printed slips reported by the run, confirmed by the coordinator at source
  and recorded in `stale-claims.md`: arXiv:astro-ph/0603494 Eq. 144
  (negative ratio) and Eq. 12 against Sect. 4.5.6 (93.14 against 93.2 eV);
  arXiv:2404.19322 Sect. III ("=≈"; sign of $\lvert\Delta m^{2}_{31}\rvert$).
- G2 sheet: `docs/history/tests/g2/thcosmo-neutrinos-light-relics-2026-11-03.md`
  (127 items: 18 + 50 + 59, seed 1110).
- The two fresh-draw reviews (dark energy, dark matter) were cut by the
  usage limit; resumed one agent at a time (owner, 2026-11-03).

## 2026-11-03 — stage 5 W1, `thcosmo-dark-energy` G2 fresh draw: **failed** (1/59); qualifier audit

Sheet: `docs/history/tests/g2/thcosmo-dark-energy-2026-11-03-redraw.md`
(seed 1108). Part 1: 11 ok, 2 wrong, 1 unclear. Part 2 (fixed rows): 3 ok.
Part 3: 58 ok, 1 wrong.

- `results.md:20` (wrong, in the draw) and `models.md:32`: the Caldwell–Linder
  bounds (arXiv:astro-ph/0505494) lost their condition, a field below the
  Planck scale ($E<M_{P}$, text after Fig. 2), and their hedge, "this may be
  the limit of quintessence" (abstract); both restored.
- `SKILL.md:33`, `SKILL.md:55` (wrong): two of the coordinator's own fixes
  of the first round paraphrased; now quoted verbatim (Vikman's "a certain
  class …, in particular"; Martin's "far from being 122 orders of
  magnitude larger"; Kaya & Lahey's "does not account for regularization
  and renormalization").
- `formalism.md:15` (unclear): the Friedmann equation of
  arXiv:hep-th/0603057 uses 8πG in Eqs. 102 and 160 and κ² in Eq. 180;
  restated by equation, not by section.
- Lesson: a coordinator fix is quoted, never paraphrased.
- Two failed draws on one pattern: a targeted qualifier audit of the 47
  unquoted strong claims (`thcosmo-dark-energy-qualifier-audit-lines.txt`)
  runs before a third draw.
- Qualifier audit done (one agent, 40 calls): about 70 statements checked,
  41 rewritten to the papers' quoted words, one moved to "Not verified"
  (`results.md:18`); one factual error found (`models.md:25`: freezing
  fields go to "w→-1, w'→0", arXiv:astro-ph/0505494, not away from −1).
  No equation changed; `check_numbers`, `check_equations` empty; 128
  equations, 0 mismatch; tests pass. Third draw:
  `docs/history/tests/g2/thcosmo-dark-energy-2026-11-03-redraw2.md` (seed 1111).

## 2026-11-03 — stage 5 W1, `thcosmo-dark-matter-models` G2 fresh draw: **passed**

Sheet: `docs/history/tests/g2/thcosmo-dark-matter-models-2026-11-03-redraw.md`
(seed 1109). Part 1: 18 ok, 2 unclear. Part 2 (fixed rows): 2 ok, the
others skipped. Part 3: 57 ok, 2 unclear, 0 wrong: the skill passes G2.
Every equation re-read matched; the first-round fixes hold.

Coordinator, unclear items quoted at source:
- `SKILL.md:34`: 17.46(84) μeV "in this minimal model" (arXiv:2609.20801).
- `SKILL.md:37`: "conventional production through active-sterile mixing
  is tightly constrained by X-ray searches and structure-formation
  observations" (arXiv:2609.04650), not "non-resonant".
- `models.md:120`: "the first cosmological constraints on interactions
  between dark matter and protons" (arXiv:1801.08609).
- `approximations.md:58`: the fit of arXiv:astro-ph/0501562 is used for a
  "pure ΛWDM" universe (Sect. IV.1).
- Hub router: built; README row updated.

## 2026-11-03 — stage 5 W1, `thcosmo-dark-energy` G2 third draw: **failed** (2/59); full re-read

Sheet: `docs/history/tests/g2/thcosmo-dark-energy-2026-11-03-redraw2.md`
(seed 1111). Part 1: 13 ok, 1 wrong. Part 3: 57 ok, 2 wrong.

- `SKILL.md:55` (wrong): Martin's "(for a free theory)" restored, quoted.
- `formalism.md:90` (wrong, draw): Eq. 16 of arXiv:1603.08299 holds "if, to
  simplify, we hold $\omega_{d}$ constant" (Sect. 2.1.1); restored.
- `formalism.md:117` (wrong, draw): "the first meaningful constraint"
  (arXiv:2511.22478, abstract), not "first constraint".
- Three draws failed on one cause: paraphrase drift in qualitative text;
  every equation matched in all three. Sampling finds it one item at a time,
  so every non-equation statement of the skill is now re-read at source by
  one agent before a fourth draw. Brief rule 2 extended to conditions,
  scope and "first" claims.
- Full re-read done (one agent): about 190 non-equation statements checked;
  73 rewritten to the papers' quoted words (SKILL.md 4, formalism 19,
  models 24, results 14, approximations 7, open questions 5); 3 moved to
  "Not verified"; 5 place labels corrected (three σ(w') statements are in
  the abstract of arXiv:astro-ph/0505494, not after Fig. 1). Checks empty,
  128 equations, 0 mismatch; tests pass. Fourth draw:
  `docs/history/tests/g2/thcosmo-dark-energy-2026-11-03-redraw3.md` (seed 1112).

## 2026-11-03 — stage 5 W1, `thcosmo-dark-energy` G2 fourth draw: **passed**

Sheet: `docs/history/tests/g2/thcosmo-dark-energy-2026-11-03-redraw3.md`
(seed 1112). Part 1: 14 ok. Part 3: 59 ok, 0 wrong: the skill passes G2,
after three failed draws and a full qualitative re-read. Lead for a later
refresh (reviewer, not yet checked by the coordinator): the freezing upper
bound listed under "Not verified" in `formalism.md` may be printed in
arXiv:astro-ph/0505494, text after Fig. 1. Hub router: built; README row.

## 2026-11-03 — stage 5 W1, `thcosmo-neutrinos-light-relics` G2: **passed**

Sheet: `docs/history/tests/g2/thcosmo-neutrinos-light-relics-2026-11-03.md`
(127 items, seed 1110). Part 1: 16 ok, 2 unclear. Part 2: 41 ok, 1 wrong,
8 unclear. Part 3: 56 ok, 3 unclear, 0 wrong: the skill passes G2.

- One agent re-read the 14 flagged items at source (all reviewer notes
  confirmed) and fixed them with the papers' quoted words: one place label
  (`formalism.md:73`, text after Eq. 52 of arXiv:astro-ph/9506072), two
  more place labels, dropped hedges and conditions, one generalisation
  ("papers before 2020") removed; two more instances of the pattern fixed.
- arXiv:2107.09664: its abstract and body assign the vector and
  Dirac-fermion limits the other way round; both quoted, recorded in
  `stale-claims.md`.
- After the fixes: 97 equations, 75 exact, 0 mismatch; checks empty;
  tests pass. Hub router: built; README row.
- W1 domains: all three built (dark energy after four draws, dark matter
  after two, neutrinos after one). Next: the dossiers of the 0.2 domains.

## 2026-11-04 — stage 5 W1, `thcosmo-inflation` dossiers batch A (G1 passed; G3 waiting)

Run: three dossiers from the gap audit (questions 1–3):
`deep/slow-roll-predictions.md` (150 lines), `deep/reheating-and-efolds.md`
(135), `deep/multi-field-perturbations.md` (131); 20 sources added (68).
The second-order constants of `formalism.md` "Not verified" are resolved
at source (arXiv:1303.3787, text after Eq. 25).

- G1: `verify_sources` 68 sources, 0 problems; `check_numbers`,
  `check_equations` empty; `check_transcription` 309 equations, 235 exact,
  57 contained, 0 mismatch, 17 unreadable; `check_places` 3 found
  elsewhere, read by the coordinator at source: all printed at the places
  named (arXiv:astro-ph/0305263 Eq. 11 and Sect. II.1 "around 62";
  arXiv:2510.18656 Eqs. 29–30; arXiv:astro-ph/0202094 equation numbers in
  text); `check_shape` 0 problems.
- Generality: Martin 17.9 % (flag), the Encyclopaedia again; kept, as at
  the build.
- Slips reported by the run: three confirmed and recorded in
  `stale-claims.md` (arXiv:1807.06211 Eq. 4; arXiv:1502.02114 Eq. 45;
  arXiv:2511.14673 Sect. 2.2.1 against Sect. 1); one not confirmed by the
  coordinator (arXiv:1004.5525 Eq. 26 against Eq. 19: the rendering of
  Eq. 26 shows no ρ_nuc), left out.
- SKILL.md file map and `subtopics.tsv` list the three dossiers.
- G3 sheet: `docs/history/tests/g2/thcosmo-inflation-dossiers-2026-11-04.md`
  (seed 1113, `--only /deep/`).
- The correlators dossier run was cut by the usage limit at its start;
  resumed after this gate, one agent at a time.

## 2026-11-04 — stage 5 W1, `thcosmo-inflation` dossiers batch A, G3: **passed**

Sheet: `docs/history/tests/g2/thcosmo-inflation-dossiers-2026-11-04.md`
(seed 1113). Part 2: 67 ok, 1 wrong. Part 3: 59 ok, 0 wrong: G3 passes.
Audit questions 1–3: answered (reviewer: yes, yes, yes).

- `deep/slow-roll-predictions.md:87` (wrong): the N3LO expressions of
  arXiv:2205.12608 (Eqs. 138, 161) use the pivot of Eq. 66,
  $k_{\diamond}\eta_{\diamond}c_{\rm s}(\eta_{\diamond})=-1$, which reduces
  to Eq. 41 only for a unit sound speed; restated, Eq. 66 copied exactly.
- Lines 118 and 147: the "no paper gives the transformation" statements
  now quote the instance that arXiv:1303.3787 prints (text after Eq. 28:
  "would set f=3 and g=6"), and keep the gap that remains.
- After the fixes: 313 equations, 0 mismatch; tests pass.

## 2026-11-04 — stage 5 W1, `thcosmo-primordial-correlators` dossiers batch A (G1 passed; G3 waiting)

Run: three dossiers from the gap audit (questions 1–3):
`deep/in-in-bispectrum.md` (130 lines; Maldacena 2002 through
arXiv:hep-th/0605045 Sect. 5.1, [sec]), `deep/eft-of-inflation.md` (122;
the unitary-gauge action, arXiv:0709.0293 Eq. 10, listed as missing in the
reference files, now transcribed), `deep/soft-limits-and-consistency.md`
(140); 20 sources added (99).

- G1: `verify_sources` 0 problems; `check_numbers`, `check_equations`
  empty; `check_transcription` 237 equations, 185 exact, 42 contained, 0
  mismatch, 10 unreadable; `check_places` 0 elsewhere, 0 not found;
  `check_shape` 0 problems.
- Generality: Chen 19.9 % (flag; 14.1 % at the build), Cheung 10.6 %.
  The rise is two sources: the review arXiv:1002.1416 (88 citations) and
  arXiv:hep-th/0605045 (37), the readable route to Maldacena's bispectrum
  required by the brief (special cases, pre-rendering papers); kept,
  justified, to be rebalanced in the deepening runs if a second readable
  route exists.
- Slips reported by the run: two confirmed and recorded in
  `stale-claims.md` (arXiv:1905.05697 Eq. 61, equilateral row 0.0780
  against 0.780; arXiv:2005.02366, $c_{s}\approx-0.031$). Two not kept:
  the sign of arXiv:0709.0293 Eq. 45 against later papers is a sign
  convention of $f_{\rm NL}$, not a slip; the "+-" in its Eq. 10 is not in
  the rendering read by the coordinator.
- SKILL.md file map and `subtopics.tsv` list the three dossiers.
- G3 sheet: `docs/history/tests/g2/thcosmo-primordial-correlators-dossiers-2026-11-04.md`
  (seed 1114, `--only /deep/`; 23 + 37 + 59).

## 2026-11-04 — stage 5 W1, `thcosmo-inflation` dossier 4 (G1 passed; G3 waiting)

Run: `deep/stochastic-delta-n-tails.md` (148 lines), audit question 4;
5 sources added (73). Conditions stated as printed (leading-order slow
roll, white Gaussian noise, Itô form, uniform-N gauge; absorbing and
reflective boundaries; bounded domain for discrete poles).

- G1: `verify_sources` 0 problems; checks empty; `check_transcription` 403
  equations, 0 mismatch, 24 unreadable; no new found-elsewhere.
- Slips: two confirmed and recorded (arXiv:2510.04707 Eqs. 12, 15 against
  Eq. 7; arXiv:1707.00537 Eq. 15); one not seen in the rendering (the
  exponent before Eq. 54 of arXiv:1707.00537), left out.
- File map and `subtopics.tsv` updated.
- G3 sheet: `docs/history/tests/g2/thcosmo-inflation-dossier-stochastic-2026-11-04.md`
  (seed 1115).
- Push of 2026-11-04 09:38 rejected by GitHub ("Internal Server Error");
  the default SSH identity order also fails (NERSC keys offered first);
  pushes use the GitHub key explicitly.

## 2026-11-04 — stage 5 W1, `thcosmo-primordial-correlators` dossiers batch A, G3: **passed**

Sheet: `docs/history/tests/g2/thcosmo-primordial-correlators-dossiers-2026-11-04.md`
(seed 1114). Part 2: 35 ok, 2 wrong. Part 3: 59 ok, 0 wrong: G3 passes.
Audit questions 1–3: answered (yes, yes, yes; Maldacena through
arXiv:hep-th/0605045, recorded).

- `deep/eft-of-inflation.md:60, :82` (wrong): the T+E bound
  $c_{\rm s}\geq 0.021$ is Eq. 63 of arXiv:1905.05697, the T-only one
  Eq. 62; the two equations are now cited separately.
- `deep/in-in-bispectrum.md:127` (wrong): $\epsilon_X$ is defined at
  Eq. 5.6 (Sect. 5.1) of arXiv:hep-th/0605045 and relation 3.5 is in
  Sect. 3.1, both read by the coordinator; the "Not verified" line now says
  so and keeps what was not read.
- `deep/soft-limits-and-consistency.md:75`: quoted "becomes", as printed.
- After the fixes: 238 equations, 0 mismatch; tests pass.

## 2026-11-04 — stage 5 W1, `thcosmo-inflation` dossier 4, G3: **passed**

Sheet: `docs/history/tests/g2/thcosmo-inflation-dossier-stochastic-2026-11-04.md`
(seed 1115). Part 2: 34 ok. Part 3: 59 ok, 0 wrong: G3 passes. Audit
question 4: answered. Minor notes (reading list completeness; two
definitions printed one equation from their tag) left for the next refresh.
The reviewer also confirms the third slip of the run (exponent before
Eq. 54 of arXiv:1707.00537), which the coordinator could not see in the
rendering; not recorded until seen. `thcosmo-inflation`: four dossiers,
gap audit closed.

## 2026-11-04 — stage 5 W1, `thcosmo-primordial-correlators` dossiers batch B (G1 passed; G3 waiting)

Run (cut by the usage limit, resumed from `_progress.md`):
`deep/cosmological-collider.md` (149 lines, audit question 4; quasi-single
field followed through Assassi–Baumann–Green) and `deep/loop-corrections.md`
(130, question 5; each side of the PBH loop debate in its own words and
version); 18 sources added (117).

- G1: `verify_sources` 0 problems; checks empty; `check_transcription` 327
  equations, 255 exact, 0 mismatch, 18 unreadable; `check_places` 0
  elsewhere; `check_shape` 0 problems.
- Generality: Chen 15.7 % (flag, down from 19.9 %), Cheung 8.2 %; the run
  added two Chen citations only; kept, justified as before.
- Reported slips are spelling typos and one reused symbol (κ in
  arXiv:2607.12010): not physics slips, not recorded in the hub.
- G3 sheet: `docs/history/tests/g2/thcosmo-primordial-correlators-dossiers-B-2026-11-04.md`
  (seed 1116, all of `deep/`; 48 items in the two new dossiers).

## 2026-11-04 — stage 5 W1, `thcosmo-modified-gravity` dossiers batch A (G1 passed; G3 waiting)

Run: `deep/eft-dark-energy-alpha-basis.md` (147 lines, audit question 1;
Bellini–Sawicki Eqs. 53–55 transcribed whole, closing the "Not verified"
item; the α_B convention relations quoted from arXiv:1709.09135 App. A and
arXiv:1411.3712 footnote 8; hi_class against Bellini–Sawicki marked
`[der]`), `deep/quasi-static-mu-sigma.md` (120, question 2),
`deep/screening-mechanisms.md` (147, question 3); 17 sources added (102).

- G1: `verify_sources` 0 problems; checks empty; `check_transcription` 286
  equations, 210 exact, 50 contained, 0 mismatch, 26 unreadable;
  `check_places` 0 elsewhere; `check_shape` 0 problems; tests pass after
  `sync_blocks` (the run could not write the block).
- Generality: Bellini 14.8 %, Kobayashi 10.2 % (16.9 % at the build),
  Euclid 8.4 %; no flag.
- Slips: two confirmed and recorded (arXiv:1504.04623 Eq. 119;
  arXiv:1606.05339 Eq. 63). Not recorded: two `[der]` readings of the run
  (arXiv:1407.0059 Eq. 6.44, arXiv:1709.09071 Sect. 3.1.1), a ϵ/ε symbol
  change (arXiv:1503.06831), and arXiv:1606.05339 Eq. 58, whose rendering
  shows another row.
- File map and `subtopics.tsv` updated by the coordinator.
- G3 sheet: `docs/history/tests/g2/thcosmo-modified-gravity-dossiers-2026-11-04.md`
  (seed 1117; 12 + 57 + 59).
