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

## 2026-11-04 — stage 5 W1, `thcosmo-primordial-correlators` dossiers batch B, G3: **passed**

Sheet: `docs/history/tests/g2/thcosmo-primordial-correlators-dossiers-B-2026-11-04.md`
(seed 1116). New-dossier rows: part 2, 25 ok; part 3, 23 ok; 0 wrong, 0
unclear (rows of batch A, already passed, skipped). Audit questions 4–5:
answered. The draw was over all of `deep/`, so 23 of its 59 items fell in
the new dossiers; with the 25 part-2 rows, 48 of their tool-passed and
non-passed items were re-read without error.

Coordinator, minor notes fixed at source:
- `cosmological-collider.md:133`: arXiv:2010.04727 does not "remove" the
  Boltzmann factor in general; Eqs. 79–80 carry none for $M_{\rm eff}<\lambda$
  and it returns above λ (Sect. 4.3); restated.
- `cosmological-collider.md:146`: the assignment of $n=0,0,2,3$ is printed
  after Eq. 21 of arXiv:2608.23243; resolved.
- `loop-corrections.md:72` `[der]`: "over all momenta" replaced by the
  paper's set-up (UV dropped by iε, IR cut at $k_{\rm min}\gg p$).
- `thcosmo-primordial-correlators`: five dossiers, gap audit closed.

## 2026-11-04 — stage 5 W1, `thcosmo-modified-gravity` dossiers batch A, G3: **passed**

Sheet: `docs/history/tests/g2/thcosmo-modified-gravity-dossiers-2026-11-04.md`
(seed 1117). Part 2: 55 ok, 2 wrong. Part 3: 59 ok, 0 wrong: G3 passes.
Audit questions 1–3: answered.

- `deep/eft-dark-energy-alpha-basis.md:90` (wrong): Eq. 55 of
  arXiv:1405.3590 has four rows; the first,
  $M_{*}^{2}/m_{0}^{2}=1+\tilde{M}=1+\Omega+\gamma_{3}$, is now in the
  transcription.
- `deep/screening-mechanisms.md:96, :123` (wrong): the 1.4 and 1.8 orders
  of magnitude of arXiv:2611.02213 hold for the profile truncated at the
  physical pion mass (3.0 and 2.4 in the chiral limit), the chameleon one
  "at the dark-energy scale"; both conditions quoted.
- After the fixes: 286 equations, 0 mismatch; checks empty.

## 2026-11-04 — stage 5 W1, `thcosmo-modified-gravity` dossier 4 (G1 passed; G3 waiting)

Run: `deep/speed-of-tensors-constraints.md` (215 lines), audit question 4:
the GW170817 conditions, graviton decay, a survival table with each
paper's assumptions, the cutoff objection and its replies; 6 sources added
(108); five of them read at the abstract only.

- G1: checks empty; `check_transcription` 310 equations, 0 mismatch, 28
  unreadable; `check_places` 0 elsewhere; tests pass. Generality: Bellini
  11.8 %, Creminelli 10.1 %, Kobayashi 8.4 %.
- Slip confirmed at source and recorded: arXiv:1710.05877 says the
  Cherenkov bounds apply to GWs "faster, and not slower, than light",
  against arXiv:1710.06394 and arXiv:1710.05901.
- File map and `subtopics.tsv` updated.
- G3 sheet: `docs/history/tests/g2/thcosmo-modified-gravity-dossier-tensors-2026-11-04.md`
  (seed 1118).

## 2026-11-04 — stage 5 W1, `thcosmo-modified-gravity` dossier 4, G3: **passed**

Sheet: `docs/history/tests/g2/thcosmo-modified-gravity-dossier-tensors-2026-11-04.md`
(seed 1118). Part 2: 11 ok. Part 3: 32 ok (all tool-passed items of the
dossier), 0 wrong. Audit question 4: answered. Two minor notes fixed at
source: `:128` the condition of arXiv:1806.09417, "if those were at all
representative of the types of operators we would expect from the UV
completion", quoted; `:136` the LISA forecast of arXiv:2203.00566 quoted
whole ("bounds on departures from General Relativity in unexplored
low-frequency regimes"). `thcosmo-modified-gravity`: four dossiers; the
13 dossiers of the three gap audits are written and gated.

## 2026-11-04 — stage 5 W1, `thcosmo-modified-gravity` deepening run (G1 passed; G2 running)

Run (`docs/agent-brief-deepen.md`, gap-audit questions 7–9): the three thin
subtopics now covered. Vector–tensor: generalised Proca action, background
and tensor sector (arXiv:1603.05806, Eqs. 1–7, 12–14, 33–34), Einstein–aether
(arXiv:0801.1547, Eqs. 1–2, 9–10) and a new model card. Teleparallel and
non-metricity: f(T) action, field and Friedmann equations
(arXiv:2106.13793, Eqs. 5.48–5.54, 6.4–6.7b), f(Q) (arXiv:2309.15958,
Eqs. 5.40–5.42, 6.4–6.10). Non-local: RR action and general quadratic
action (arXiv:1712.07066, Eqs. 1.1, 2.51), the Lunar Laser Ranging verdict
(arXiv:1812.11181), DW-2019; a new open question "Are the non-local models
still viable?". 18 sources added (126). The run stopped before its final
checks (session of the second account ended); the coordinator of the main
account took it over.

- G1 (coordinator): `verify_sources` 0 problems; `check_transcription` 363
  equations, 273 exact, 56 contained, 0 mismatch, 34 unreadable;
  `check_places` 0 elsewhere; `check_shape` 0 problems; tests pass.
- Fixed at G1: three `[der]` flags moved to the end of their own sentence
  (they were read as covering numbers of the sentence before); three
  statements whose relations are read in an abstract marked
  `<!-- eq: notation -->`; a table row with `|` inside `$…$` rewritten in
  plain text, as row 52 of `results.md`.
- Slip recorded by the run, to be confirmed at G2: Sect. 6.1 of
  arXiv:2309.15958 normalises f differently from Eq. 5.40 (no κ on the
  matter side of Eq. 6.4, 1/κ inside f in Eqs. 6.8–6.9).
- Generality: Bellini 10.3 %, Creminelli 8.9 %, Kobayashi 7.3 %; no flag.
- Tool: `sample_statements.py --changed-since REV` restricts parts 2 and 3
  to the lines a deepening run added or changed.
- G2 sheet: `docs/history/tests/g2/thcosmo-modified-gravity-deepening-2026-11-04.md`
  (seed 1119; 12 + 16 + 43, the 43 being every tool-passed new item).

## 2026-11-04 — stage 5 W1, `thcosmo-modified-gravity` deepening run, G2: **passed**

Sheet: `docs/history/tests/g2/thcosmo-modified-gravity-deepening-2026-11-04.md`
(seed 1119). Part 1: 12 skip (lines unchanged since G2 of 2026-11-03).
Part 2: 16 ok. Part 3: 43 ok (every tool-passed new item), 0 wrong. The
f(Q) normalisation slip is confirmed at source: Eq. 6.4 of arXiv:2309.15958
has no κ on the matter side, Eq. 5.41 has $\kappa\,\mathcal{T}_{\mu\nu}$,
Eqs. 6.8–6.9 put 1/κ before f, and Eq. 6.9 in Eq. 6.4 gives Eq. 6.10.
Minor notes fixed at source:
- `formalism.md:104`: the `[der]` names Eqs. 6.4–6.10, not Sect. 6.1, since
  Eq. 6.3 keeps the prefactor of Eq. 5.40.
- `formalism.md:186`: f(Q) equations transcribed are 6.4 and 6.8–6.10, not
  6.4–6.10.
- `models.md:100`: the qualifier of arXiv:2404.07782, that the change of
  wave speed "vanishes in the limit in which gravitational waves propagate
  with luminal speed", quoted.

`thcosmo-modified-gravity`: the three thin subtopics covered; gap audit
closed. Gap audits written for `thcosmo-dark-energy`,
`thcosmo-dark-matter-models` and `thcosmo-neutrinos-light-relics`
(`docs/history/tests/gap-audit/`): three dossiers each, deepening runs for
dark sectors, gravitational production and light sterile neutrinos.

## 2026-11-05 — stage 5 W2, build `thcosmo-cosmological-gravitational-waves` (G1 passed; G2 waiting)

Run (second account, started 2026-11-05): stopped on the account's weekly
usage limit after writing every file but before its final checks, at 58 or
more of 90 research calls; the owner committed the state as `8730d26`; the
coordinator of the main account took it over. SKILL.md 127 lines,
formalism 159, models 103 (8 model cards), results 86, approximations 89,
open questions 67; 39 sources; 9 subtopics (radiation bound and preheating
thin).

- G1 (coordinator): `verify_sources` online 0 problems; `check_numbers`
  and `check_equations` empty; `check_transcription` 219 equations, 197
  exact, 22 contained, 0 mismatch, 0 unreadable; `check_places` 31
  statements, 22 at place, 0 elsewhere, 0 not found, 9 unreadable (each
  cites several papers or an inline place); `check_shape` 0 problems; no
  `eq: notation` escape; tests pass.
- Generality: Caprini 47.1 % (flag), Domènech 7.1 %, Figueroa 3.4 %;
  owner's papers 0 %. The share is the review of Caprini & Figueroa
  (arXiv:1801.04268) used as the spine of every subtopic, plus the LISA
  phase-transition papers. Not justified at this level: the deepening run
  of the two thin subtopics also rebalances, citing the original papers
  (sound waves, string loops, axion–gauge production, scalar-induced
  kernels) where readable.
- Printed slips reported by the run, confirmed by the coordinator at source
  and recorded in `stale-claims.md`: arXiv:1801.04268 text after Eq. 230
  (exponent printed as a product) and text before Eq. 380 ($\dot l$ without
  μ); arXiv:2401.04388 Eq. 116 (limits ∞ to ∞); arXiv:1807.09241 Eq. 61
  ($(1+\cos\iota)^{2}$). The two linear terms of Eq. 224 of
  arXiv:1801.04268 are described in `approximations.md` but not recorded:
  the original fit was not read. A Fig. 9 slip noted in the run's progress
  file is not used in the skill and not recorded.
- G2 sheet: `docs/history/tests/g2/thcosmo-cosmological-gravitational-waves-2026-11-05.md`
  (seed 1120; 19 + 29 + 59).

## 2026-11-05 — stage 5 W1, `thcosmo-dark-energy` dossiers (G1 passed; G3 waiting)

Run (2026-11-04, from the gap audit): `deep/thawing-quintessence-w0wa.md`
(135 lines, audit question 1), `deep/dark-energy-perturbations-ppf.md`
(106, question 2), `deep/interacting-de-instabilities.md` (124, question 3).
The run stopped before its final checks (its progress file still marked
dossier 3 in progress, though the file was complete); committed by the
owner in `8730d26`; gated by the coordinator of the main account.

- Fixed at G1: three `[der]` flags moved to the end of their own sentence;
  twelve relations read in running text, an abstract or a caption given
  the `inline` place after a re-read at source (all as printed); a table
  value rewritten in plain text; three pointer statements marked
  `num: not a value`; four rows of `interacting-de-instabilities.md`
  (arXiv:0804.0232 Eqs. 43, 75, 76, 86) re-transcribed as printed instead
  of simplified (`2/(1+w_x)` for `{2\over 1+w_{x}}`), one flag per
  equation; four sources added (arXiv:0901.1611, 1109.6234, 1404.5220,
  1904.04149).
- After the fixes: `verify_sources` 76 sources, 0 problems;
  `check_transcription` 302 equations, 206 exact, 59 contained, 0
  mismatch, 37 unreadable; `check_places` 0 elsewhere, 0 not found;
  `check_shape` 0 problems; tests pass.
- Generality: Li 10.9 %, Copeland 10.8 %, Valiviita 6.9 %; no flag.
- G3 sheet: `docs/history/tests/g2/thcosmo-dark-energy-dossiers-2026-11-05.md`
  (seed 1121, `--only /deep/`; 14 + 74 + 59; part 1 was re-read at G2 of
  2026-11-03).

## 2026-11-05 — stage 5 W1, `thcosmo-dark-matter-models` dossiers (G1 passed; G3 waiting)

Runs: `deep/relic-abundance-beyond-freeze-out.md` (134 lines, audit
question 1) and `deep/axion-relic-abundance.md` (136, question 2) written
2026-11-04 by a run that stopped before its checks (committed by the owner
in `8730d26`); `deep/noncold-dm-mass-mappings.md` (149, question 3: seven
mass maps, the two half-mode conventions $T^2=1/2$ and $T=1/2$) written
2026-11-05 by a resumed run (29 of 30 calls), which was also allowed to fix
the G1 failures of the first two. Six sources added (88).

- Fixed at G1 (coordinator): the runs had put 27 `eq: notation` escapes on
  statements holding values and relations read in a paper (for example
  $\lambda_{\rm hm}\approx 13.93\lambda^{\rm eff}_{\rm fs}$, $\xi=15(2)$),
  which hid them from `check_transcription`. All removed but one (the
  definitions of the two half-mode conventions); the statements that then
  failed were given their `inline` place after a grep of the paper at the
  named section, or re-transcribed: seven mismatches exposed and fixed
  (equations simplified or cut in the middle, now copied whole as printed:
  arXiv:1112.0330 Eqs. 8–9, arXiv:2003.01100 Eq. 162; a notation symbol and
  two values outside `$…$`; a quote given its own place, Sect. VII of
  arXiv:2401.17253).
- After the fixes: `verify_sources` 88 sources, 0 problems;
  `check_numbers` and `check_equations` empty; `check_transcription` 294
  equations, 155 exact, 42 contained, 0 mismatch, 97 unreadable;
  `check_places` 66 at place, 2 elsewhere (multi-equation rows), 0 not
  found; `check_shape` 0 problems.
- Generality: Safdi 10.3 %, Vogel 5.1 %, Murgia 4.3 %; no flag.
- Printed slip reported by the run, confirmed by the coordinator and
  recorded in `stale-claims.md`: arXiv:2011.13458 Eq. 2.28 (moments not one
  at n = 0, against the definition of Eq. 2.14).
- Lesson for the briefs: `eq: notation` is for definitions only; a value
  or a relation read in text takes `inline` with its place.
- G3 sheet: `docs/history/tests/g2/thcosmo-dark-matter-models-dossiers-2026-11-05.md`
  (seed 1122, `--only /deep/`; 20 + 73 + 59; part 1 was re-read at G2 of
  2026-11-03).

## 2026-11-05 — stage 5 W2, `thcosmo-cosmological-gravitational-waves` G2: **passed**

Sheet: `docs/history/tests/g2/thcosmo-cosmological-gravitational-waves-2026-11-05.md`
(seed 1120). Part 1: 18 ok, 1 wrong. Part 2: 29 ok. Part 3: 59 ok, 0
wrong. Fixed at source:
- `formalism.md:14` (part 1): an added sentence, "The factor 2 in this
  normalisation propagates into every amplitude below; other papers
  normalise to 1", not in arXiv:1801.04268 and overstated (the block holds
  formulas of other papers in their own conventions); replaced by the
  paper's own text after Eq. 85 (the 2 counts two polarisations; their
  Ref. [54] "differs by a factor 2").
- `models.md:14` (reviewer's side finding, not sampled): quotes placed
  "text after Eq. 204" are in the introduction of Sect. 5; relabelled.

`thcosmo-cosmological-gravitational-waves` set to built (W2) in the hub
router and the README. Open: the Caprini share (47.1 %), the two thin
subtopics, and the gap audit and dossiers.

## 2026-11-05 — stage 5 W1, `thcosmo-neutrinos-light-relics` dossiers (G1 passed; G3 waiting)

Run (2026-11-05, gap-audit questions 1–3): `deep/neff-standard-model-calculation.md`
(139 lines; the kinetic equations and collision integrals of
arXiv:2012.02726, Eqs. 2–4, 14, 19–21, closing the "Not verified" item;
3.0440 against 3.043 explained from arXiv:2012.02726 and Drewes et al.),
`deep/neutrino-mass-below-the-floor.md` (152; CLASS grid, truncation and
fluid closure as `[doc]` facts read 2026-11-05; five definitions of an
effective or negative mass; no measured value quoted),
`deep/interacting-neutrino-perturbations.md` (149; the α_ℓ of
arXiv:2606.03395 from its body; the (m/E)³ cancellation behind the (m/E)⁵
decay rate). Nine sources added (58).

- G1 (coordinator): `verify_sources` 0 problems; `check_numbers` and
  `check_equations` empty, with no `eq: notation` escape in `deep/`;
  `check_transcription` 227 equations, 169 exact, 42 contained, 0
  mismatch, 16 unreadable; `check_places` 48 at place, 1 elsewhere
  (`interacting-neutrino-perturbations.md:110`, to re-read), 0 not found;
  `check_shape` 0 problems; tests pass.
- Generality: Bennett 14.8 %, Lesgourgues 13.7 %, Barenboim 7.1 %; no
  flag (Bennett just under).
- Slips reported by the run, not recorded in the hub: Table 1 of
  arXiv:2402.18481 prints −0.006 where Table 5 of arXiv:2012.02726 prints
  −0.005 (confirmed; the first table is "adapted", so possibly rounding;
  quoted both in the dossier); the text after Eq. 3 of arXiv:2012.02726
  calling a prefactor the inverse Hubble rate rests on a `[der]` reading,
  to be judged at G3; the "light scalar" of the abstract of
  arXiv:2606.03395 against the massive mediator of its body is wording,
  described in the dossier.
- G3 sheet: `docs/history/tests/g2/thcosmo-neutrinos-light-relics-dossiers-2026-11-05.md`
  (seed 1123, `--only /deep/`; part 1 was re-read at G2 of 2026-11-03).

## 2026-11-05 — stage 5 W1, `thcosmo-dark-energy` dossiers, G3: first draw fails

Sheet: `docs/history/tests/g2/thcosmo-dark-energy-dossiers-2026-11-05.md`
(seed 1121). Part 1: skipped (G2 of 2026-11-03). Part 2: 72 ok, 2 wrong.
Part 3: 58 ok, 1 wrong: G3 not passed. No equation wrong; both errors are
wording. Audit questions 1–3 answered. Fixed at source:
- `thawing-quintessence-w0wa.md:17`: de Putter & Linder do not define
  $w_a$; they quote it, "defined by [24]" (Linder 2003).
- `thawing-quintessence-w0wa.md:30` (part 2 and part 3): "linear in
  $s^2=\gamma$" said Eq. 22 of arXiv:0712.3450 is linear in γ; replaced by
  the paper's sentence, it "can be transformed into a linear differential
  equation with the change of variables $s^{2}=\gamma$" (Sect. III).
- Side findings: `interacting-de-instabilities.md:43` hedge "It appears
  that" restored; `:68` the code of arXiv:1109.6234 suppresses
  perturbations when $\vert 1+w\vert<0.01$ (Sect. IV), App. A calls it
  imposing; both places now given.
- Pattern search (a paraphrase that changes a mathematical property or
  drops a hedge): no other "linear in" or "define" paraphrase in `deep/`.
- Fresh draw: `docs/history/tests/g2/thcosmo-dark-energy-dossiers-2026-11-05-redraw.md`
  (seed 1124): part 3 and the fixed rows to be re-read.

## 2026-11-05 — stage 5 W1, `thcosmo-dark-matter-models` dossiers, G3: first draw fails

Sheet: `docs/history/tests/g2/thcosmo-dark-matter-models-dossiers-2026-11-05.md`
(seed 1122). Part 1: skipped (G2 of 2026-11-03). Part 2: 70 ok, 3 wrong.
Part 3: 58 ok, 1 wrong: G3 not passed (bound 7.8 %). Audit questions 1–3
answered. Fixed at source, each read by the coordinator in the paper:
- `relic-abundance-beyond-freeze-out.md:15` (part 3): the Hubble rate of
  arXiv:2610.03718 is in footnote 4 of Sect. 3, not the running text.
- `:13`: the ordering $m_{1}\leq\cdots\leq m_{N-1}\leq m_{N}$ restored as
  printed in arXiv:hep-ph/9704361.
- `:76`: the "below 0.2%" of arXiv:2610.03718 Sect. 4.2 compares the
  numerical and semi-analytical freeze-out temperatures for either c, not
  c = √2 with c = 1.5; the paper's sentence quoted.
- `axion-relic-abundance.md:82`: Saikawa et al. call understanding the
  origin of the discrepancy, not the discrepancy, "a crucial step"; quoted.
- Side findings: `axion:76` the factor-5 boost is the estimate of Ref. [51]
  of arXiv:2609.20801, Benabou et al. (arXiv:2412.08699, source added), not
  Saikawa et al.; `axion:30` and `:132` the rendering of arXiv:1606.07494
  holds the main text (Fig. 3 caption read), so the DIGA sentence is placed
  in the main text and the "Not verified" item rewritten; `axion:15` place
  is Sect. 2, not 2.1; `relic:67` γ(T) is defined in Eq. 6, now "Eqs. 5–6".
- Not applied: the reviewer read the two `[sec: …]` flags of `relic:25` as
  typos; they are the rule-6 flag for a pre-arXiv paper (Griest & Seckel)
  read through a citing paper, and stay.
- Pattern search: no other claim about a rendering in the skill's `deep/`
  or `references/`.
- Fresh draw: `docs/history/tests/g2/thcosmo-dark-matter-models-dossiers-2026-11-05-redraw.md`
  (seed 1125): part 3 and the fixed rows to be re-read.

## 2026-11-05 — stage 5 W1, `thcosmo-dark-energy` dossiers, G3 fresh draw: **passed**

Sheet: `docs/history/tests/g2/thcosmo-dark-energy-dossiers-2026-11-05-redraw.md`
(seed 1124). Part 3: 59 ok, 0 wrong. The four fixed lines re-read: ok.
Reviewer's note, not a fix: App. A of arXiv:1109.6234 says it imposes
$\vert 1+w\vert<0.01$ where Sect. IV suppresses perturbations in that
range; both are quoted as printed in `interacting-de-instabilities.md:68`.
Audit questions 1–3 answered (first draw). The three dossiers added to the
file map of `SKILL.md` and to the `files` column of `subtopics.tsv`
(quintessence, perturbations, interacting-de). `thcosmo-dark-energy` gap
audit closed.

## 2026-11-10 — stage 5 W1, `thcosmo-dark-matter-models` dossiers, G3 fresh draw: fails

Sheet: `docs/history/tests/g2/thcosmo-dark-matter-models-dossiers-2026-11-05-redraw.md`
(seed 1125). Part 2: the 10 rows on the fixed lines re-read, 10 ok. The
nine fixed lines of the first draw confirmed in their papers. Part 3: 58 ok,
1 wrong: G3 not passed. Fixed at source, each read by the coordinator in
the paper:
- `relic-abundance-beyond-freeze-out.md:92` (part 3): the Numbers row
  dropped the hedge "can"; arXiv:2103.01944 Sect. 4.1 reads "even for widths
  as large as that of the SM Z-boson the refined prediction of the DM
  abundance can deviate at a level well exceeding the typically quoted
  observational uncertainty of ∼1 %". Row rewritten with the quote.
- Side findings applied: `:76` the 0.2 % sentence of arXiv:2610.03718
  Sect. 4.2 regains "over the range of $\alpha$ considered in this work";
  `:67` γ(T) is the "momentum exchange rate" of Eqs. 5–6, in Sect. II of
  arXiv:1706.07433, not Sect. II.2.
- Not applied: the reviewer's remark that the unnumbered ⟨σv⟩ display of
  arXiv:1706.07433 is probably Eqs. 13–14 in print (a broken label in the
  rendering); the place stays as read. The place "paragraph after Fig. 3
  caption" of `axion:30` stays: it is the place in the rendering read.
- Pattern search (a quoted value in a Numbers table that drops a modal or a
  range): the other five quoted values of the skill's `deep/` tables keep
  their hedges; `:91` re-read in Sect. 4.2, ok.
- G1 after the fixes: check_numbers and check_equations empty; transcription
  154 exact, 42 contained, 0 mismatch, 98 unreadable; places 66
  found-at-place, 2 found-elsewhere, 35 unreadable; check_shape 0 problems;
  156 tests passed.
- Fresh draw: `docs/history/tests/g2/thcosmo-dark-matter-models-dossiers-2026-11-10-redraw2.md`
  (seed 1126): part 3 and the three fixed lines to be re-read.

## 2026-11-10 — stage 5 W2, `thcosmo-cosmological-gravitational-waves` gap audit

`docs/history/tests/gap-audit/thcosmo-cosmological-gravitational-waves.md`:
ten questions; three dossiers (phase-transition spectra, cosmic-string
spectra, scalar-induced kernels); one deepening run (radiation bound,
preheating) that also rebalances the Caprini share (47.1 % at G1) toward
the primary papers.

## 2026-11-10 — stage 5 W1, `thcosmo-neutrinos-light-relics` dossiers, G3: first draw fails

Sheet: `docs/history/tests/g2/thcosmo-neutrinos-light-relics-dossiers-2026-11-05.md`
(seed 1123). Part 1: skipped (G2 of 2026-11-03). Part 2: 51 ok, 0 wrong.
Part 3: 57 ok, 2 wrong: G3 not passed. Audit questions 1–3: yes, yes, yes.
Fixed at source, each read by the coordinator in the paper:
- `neff-standard-model-calculation.md:76` (part 3): hedge dropped;
  arXiv:2402.18481 Sect. 5 reads "our results strongly suggest that the SM
  benchmark value … is correct within the quoted uncertainties".
- `neutrino-mass-below-the-floor.md:117` and `:77` (part 3): condition
  dropped; the "within 0.1%" of arXiv:2407.10965 is the Fig. 1 caption's one
  case, ±0.15 eV in linear theory, dark-matter P(k) at z = 0.
- Side findings applied: `neff:86` restores "may be" (arXiv:2012.02726
  Sect. 5.3.1); `neff:78–80` the stellar-plasma origin of the NLO rate
  correction is now Drewes et al.'s reading (arXiv:2402.18481 Sect. 1),
  set against Cielo et al.'s "up to plasma temperatures T∼20 MeV"
  (arXiv:2306.05460 Sect. II), and the `[der]` line no longer carries it;
  the table row `:105` follows; `neff:55` the unsourced clause on the
  flavour asymmetry of $G^L$ removed; `neff:13` and `:62` placed in
  footnotes 4 and 5; `interacting:27` $f_i$ copied whole from Eq. 4 of
  arXiv:2606.03395; `interacting:92` the isotropisation count rewritten
  as App. C.2 of arXiv:2203.09075 gives it ($M\sim 1/\theta^{2}$ swaps of
  one coverage time, "$\sim M\times T_{2}$"); `interacting:87` and `:124`
  regain "in the ultra-relativistic limit".
- Pattern search (an unhedged conclusion): no other in the skill's `deep/`.
- G1 after the fixes: check_numbers and check_equations empty;
  transcription 171 exact, 40 contained, 0 mismatch, 19 unreadable; places
  48 found-at-place, 1 found-elsewhere, 41 unreadable; check_shape 0
  problems; 156 tests passed. Word share: Bennett 14.8 %, Lesgourgues
  13.7 %, under 15 %.
- Fresh draw: `docs/history/tests/g2/thcosmo-neutrinos-light-relics-dossiers-2026-11-10-redraw.md`
  (seed 1127): part 3 and the fixed lines to be re-read.

## 2026-11-10 — stage 5 W1, `thcosmo-dark-matter-models` dossiers, G3 second fresh draw: **passed**

Sheet: `docs/history/tests/g2/thcosmo-dark-matter-models-dossiers-2026-11-10-redraw2.md`
(seed 1126). Part 2: the 3 rows on the fixed lines re-read, 3 ok. The three
fixed lines (`relic:67`, `:76`, `:92`) confirmed in their papers. Part 3:
59 ok, 0 wrong, 0 unclear. Audit questions 1–3 answered (first draw).
Side findings, each read by the coordinator in the paper and applied:
- `relic:60`: the 1/4 and 3/4 weights are printed in Eq. 22 of
  arXiv:2610.03718, not in the text after it; the branching-ratio gloss
  removed and the paper's sentence quoted ("treated on the same footing, as
  orthodarkonium and paradarkonium decay at the same order in the
  coupling").
- `relic:76`: "for either choice" replaced by the paper's "We compared the
  choice c=√2 with c=1.5 and find that …".
- `axion:25`: the 800 MeV estimate of arXiv:2003.01100 Sect. 3.3 also
  assumes $g_{*}(T>T_{C})$ = 61.75; added.
G1 after the edits: check_numbers and check_equations empty; transcription
154 exact, 43 contained, 0 mismatch; check_shape 0 problems; 156 tests
passed. Word share: Safdi 10.3 %, under 15 %. The three dossiers added to
the file map of `SKILL.md` and to the `files` column of `subtopics.tsv`
(thermal-freeze-out, axion-misalignment, linear-signatures,
sterile-neutrinos-wdm). `thcosmo-dark-matter-models` gap audit closed.

## 2026-11-10 — stage 5 W1, `thcosmo-neutrinos-light-relics` dossiers, G3 fresh draw: fails (coordinator's count)

Sheet: `docs/history/tests/g2/thcosmo-neutrinos-light-relics-dossiers-2026-11-10-redraw.md`
(seed 1127). Part 2: the 11 rows on the fixed lines re-read, 11 ok; every
fixed line of the first draw confirmed. Part 3: reviewer 59 ok, with row 20
flagged as a possible dropped hedge. The coordinator read it in the paper
and counts it **wrong**: `interacting:62` gives the s-channel resonance
range of arXiv:2602.12477 Sect. 4.2 without "as we preliminarily scanned";
the paper presents the range as provisional. Part 3: 58 ok, 1 wrong: G3 not
passed. Fixed at source:
- `interacting:62`: "as we preliminarily scanned" restored.
- Side findings applied: `neff:78` the `[der]` line says "at least thirty
  times smaller (their most optimistic estimate)", for "even our most
  'optimistic' estimate is a factor of 30 smaller" (arXiv:2402.18481
  Sect. 5); `interacting:116` the revised lifetime bound of Eq. 61 of
  arXiv:2011.01502 assumes a massless daughter, "strictly valid only for"
  $m_{\nu H}$ below $\sqrt{\Delta m_{\rm atm}^{2}}$ (Fig. 9 caption,
  footnote 8); added to the assumptions column.
- Not applied: `neff:39` quotes the ≲4×10⁻⁶ estimate from arXiv:2012.02726
  Sect. 3.1.1, the paper read; naming its own source (arXiv:1911.04504) is
  left to a refresh.
- Pattern search (an approximate value quoted without the paper's
  qualifier on the evidence): the other five "about / approximately /
  roughly" quotes of `deep/` keep their wording.
- G1 after the fixes: check_numbers and check_equations empty;
  transcription 171 exact, 40 contained, 0 mismatch, 18 unreadable; places
  48 found-at-place, 1 found-elsewhere, 42 unreadable; check_shape 0
  problems; 156 tests passed.
- Fresh draw: `docs/history/tests/g2/thcosmo-neutrinos-light-relics-dossiers-2026-11-10-redraw2.md`
  (seed 1128).

## 2026-11-10 — stage 5 W1, `thcosmo-neutrinos-light-relics` dossiers, G3 second fresh draw: fails

Sheet: `docs/history/tests/g2/thcosmo-neutrinos-light-relics-dossiers-2026-11-10-redraw2.md`
(seed 1128). The three fixed lines confirmed. Part 3: 57 ok, 2 wrong: G3
not passed. Fixed at source, each read by the coordinator in the paper:
- `neff:114` (part 3): conditions dropped; arXiv:1911.04504 gives 0.010121
  as the log-independent ${\cal O}(e^2)$ term "for $T_{d}=1.3453$ MeV"
  (Eq. 33), against the "oft-quoted" 0.010594 "in the limit
  $T_{d}/m_{e}\to\infty$" (Sect. 4.1.1).
- `neff:119` (part 3): one comparison stated as general ("miss the infrared
  part"); arXiv:2511.04747 Sect. 6 reports, in its Fig. 3 comparison with
  FortEPiaNO, "differences of up to 0.1% in the infrared domain", "phase-space
  suppressed in the integrated number and energy densities"; quoted.
- Side findings applied: `neff:72` restores "should be at most $10^{-5}$ …
  and is therefore negligible" (arXiv:2306.05460 Sect. III); `neff:78`
  "first-principles correction" → "diagram-(d) correction".
- Three draws in a row failed on the same pattern (a hedge, condition or
  scope dropped while numbers and equations are right). A random draw does
  not find every instance, so the pattern search is a full sweep: one agent
  re-reads every attributed claim of the three dossiers at its place
  (qualifier sweep), with the reviewer's three unchecked side findings
  (`interacting:77`, `:116`, `mass:13`). A fresh draw follows the sweep.

## 2026-11-10 — stage 5 W1, `thcosmo-neutrinos-light-relics` dossiers: qualifier sweep

One agent re-read every attributed claim of the three dossiers at its place
(interacting 112, neff 114, mass 92 statements, 12 `[der]` lines; about 45
research calls) and changed 33 statements: restored hedges, conditions and
scopes, footnote places, attributions of one paper's critique of another.
One real error beyond wording: `mass:129` placed Eq. 2.7 of arXiv:2405.00836
at general z; it is "the suppression of the matter power spectrum at z=1".
The three unchecked side findings of seed 1128 confirmed and fixed
(`interacting:77` the monopole response is estimated through χ(a), Eq. 52,
since the modified CLASS "does not include first-order collision terms";
`interacting:116` "τ₀ ≳"; `mass:13` "in the case of a thermal relic").
Coordinator spot-checks in the papers: `mass:129`, `neff:115`,
`interacting:77`: ok. G1 after the sweep: check_numbers and check_equations
empty; transcription 172 exact, 40 contained, 0 mismatch; check_shape 0
problems. Fresh draw: `docs/history/tests/g2/thcosmo-neutrinos-light-relics-dossiers-2026-11-10-redraw3.md`
(seed 1129): part 3 and the 16 part-2 rows on changed lines to be re-read.

## 2026-11-10 — stage 5 W2, `thcosmo-cosmological-gravitational-waves` dossiers, G1: passed

Three dossiers from the gap audit: `deep/phase-transition-spectra.md`
(140 lines), `deep/cosmic-string-spectra.md` (141), `deep/scalar-induced-kernels.md`
(133); 41 sources added. G1: verify_sources 81 sources, 0 problems (one
warning: arXiv:2610.14806 read in v1, v2 now out; its places are re-read at
G2); check_numbers and check_equations empty; transcription 346 equations,
285 exact, 38 contained, 0 mismatch, 23 unreadable; places 58 statements,
38 found-at-place, 1 found-elsewhere, 19 unreadable; check_shape 0
problems; 4 `eq: notation` escapes; 156 tests passed.
Generality: Caprini 28.8 % of the skill's citations (was 47.1 %),
Hindmarsh 6.2 %, Domènech 5.5 %; the deepening run continues the
rebalance. Within single dossiers the groups that carry the subtopic stay
above 15 % (Hindmarsh, sound-shell model and lattice fits, 21 %; Auclair,
LISA string study, 25 %; Blanco-Pillado, loop simulations, 16 %; Kohri,
second-order kernels, 19 %): each is the foundation of its method, set
against the rival treatments in the same dossier; justified.
Printed slips recorded in the hub's `stale-claims.md` (errata table):
arXiv:1909.10040 Eqs. 16, 20, 57–62; arXiv:2003.07360 Fig. 1 caption;
arXiv:1909.00819 Sect. 3.1 and Eq. 35; arXiv:1709.02693 Sect. I;
arXiv:1704.05871 erratum (factor 3). Not recorded: arXiv:1804.08577 Eq. 16,
flagged by the agent "to check", not a confirmed slip.
G3 sheet: `docs/history/tests/g2/thcosmo-cosmological-gravitational-waves-dossiers-2026-11-10.md`
(seed 1130); part 1 skipped (G2 of 2026-11-05).

## 2026-11-10 — stage 5 W1, `thcosmo-neutrinos-light-relics` dossiers, G3 draw after the sweep: fails

Sheet: `docs/history/tests/g2/thcosmo-neutrinos-light-relics-dossiers-2026-11-10-redraw3.md`
(seed 1129). Part 2: the 16 rows on changed lines re-read, 15 ok, 1 wrong.
Part 3: 58 ok, 1 wrong: G3 not passed. Fixed at source, each read by the
coordinator in the paper:
- `neff:115` (part 3): "dropping the neutrino–neutrino collisions" was
  broader than the approximation; arXiv:2012.02726 Sect. 5.3.1 sets only
  the diagonal entries to zero, which "generally underestimates"
  $N_{\rm eff}^{\rm SM}$ "by about" $4\times 10^{-4}$. The coordinator's
  spot-check of this line after the sweep had checked only the swept clause
  and passed it; that check was incomplete.
- `interacting:64` (part 2): the ξ values of arXiv:2602.12477 hold in "the
  region where resonances do not appear" for $T_\nu\gtrsim 0.5$ eV, and the
  Majorana value omits the indistinguishability factor 1/2 (footnote 14);
  added.
- Side findings applied: `interacting:82` doubled quote; `interacting:87`
  "for a fixed decay opening angle" (arXiv:2203.09075 Sect. 4.1); `mass:129`
  "on scales smaller than the neutrino free-streaming length"
  (arXiv:2508.20999 Sect. 2.1); `mass:130` "the two figures" → "the figures".
- G1 after the fixes: check_numbers and check_equations empty;
  transcription 172 exact, 40 contained, 0 mismatch; check_shape 0
  problems; 156 tests passed.
- No fresh draw yet. Four draws in a row failed with one or two errors each
  (2, 1, 2, 1+1). Redrawing until one draw has zero errors would no longer
  bound the error rate below 5 %: each failed draw is evidence of a residual
  rate near 2–3 % on the strict reading of hedges. How to close the gate is
  put to the owner.

## 2026-11-12 — stage 5 W2, `thcosmo-cosmological-gravitational-waves` dossiers, G3: **passed**

Sheet: `docs/history/tests/g2/thcosmo-cosmological-gravitational-waves-dossiers-2026-11-10.md`
(seed 1130), read under the strict standard (a dropped hedge, condition or
scope counts as wrong). Part 1: skipped (G2 of 2026-11-05). Part 2: 48 ok,
2 wrong, fixed at source and read by the coordinator in the paper. Part 3:
59 ok, 0 wrong. Audit questions 1–3: yes, yes, yes (Q3: general constant w
and higher orders cited, not derived). The five printed slips recorded on
2026-11-10 confirmed; the matter-era $C_0$ of Eq. 35 of arXiv:1909.00819
carries the same sign swap.
- `cosmic-string-spectra.md:45` (part 2): the Polchinski–Rocha power law
  holds "for $x>x_{\rm c}$", with "$x_{\rm c}\ll\mathrm{\Gamma}G\mu$"
  (arXiv:1909.00819 Sect. 3.3); added.
- `phase-transition-spectra.md:137` (part 2): Ref. [111] of
  arXiv:2403.03723 is arXiv:2409.03651, printed in its reference list, and
  the 0.6 factor is "as found in Ref. [42] (see discussion in Ref. [111])"
  (Sect. 2.2.1); the "Not verified" item rewritten; arXiv:2409.03651 added
  to `sources.tsv` (v2, abstract only).
- arXiv:2610.14806, read in v1, now in v2: the v1 finding (normalised GWs
  "roughly an order of magnitude smaller" than Minkowski simulations) is
  gone; v2 reads "of order $\mathcal{O}(10^{-2})$, in alignment with
  Minkowski-spacetime results", with spectra that "differ markedly". The
  coordinator read the v2 abstract and rewrote the six places that carried
  the v1 claims (`approximations.md:38`, `models.md:51`, `results.md:38`
  and `:80`, `open-questions.md:41` and `:60`, `deep/phase-transition-spectra.md:87`),
  set the row to v2, and recorded the withdrawal in the hub's
  `stale-claims.md`.
- Side findings applied after reading at source: `phase-transition-spectra.md:15`
  (footnote 3 of arXiv:1909.10040 is about the simulations' velocity);
  `cosmic-string-spectra.md:59` ("Without backreaction" is not in the
  abstract of arXiv:2610.39983; its own framing quoted); `scalar-induced-kernels.md:40`
  (the solution "regular at $x\to 0$").
- Side findings not yet checked by the coordinator, left for the deepening
  run: `phase-transition-spectra.md:41` ("are obscured"), `:109` (Sect.
  VI.1 or V.1 of arXiv:2308.12943), `cosmic-string-spectra.md:57`
  (attribution of the equal-kinks assumption), `:64` (ellipsis drops "of
  this radiation"), arXiv:2508.04263 Eq. 4 (a square missing, a possible
  slip).
G1 after the fixes: verify_sources 82 sources, 0 problems; check_numbers
and check_equations empty; transcription 349 equations, 284 exact, 42
contained, 0 mismatch; check_shape 0 problems; 156 tests passed. Word
share: Caprini 28.6 % (flag, rebalanced in the deepening run). The three
dossiers added to the file map of `SKILL.md` and the `files` column of
`subtopics.tsv`. GW gap-audit dossiers closed; the deepening run (radiation
bound, preheating, rebalance) is next.

## 2026-11-12 — owner decision: second sweep for the neutrinos dossiers, sweeps of earlier dossiers

Asked how to close G3 after four failed draws, the owner chose a second full
sweep, then a fresh draw reported as it falls (no redraw-until-pass), and
the same qualifier sweep, now, for the `thcosmo-dark-energy` and
`thcosmo-dark-matter-models` dossiers, which passed G3 under a looser
reading of hedges.

## 2026-11-12 — `thcosmo-neutrinos-light-relics` dossiers: second qualifier sweep

A fresh agent read every attributed statement whole against its paper
(about 318 statements and the `[der]` lines; about 92 research calls) and
changed 37: conditions and scopes restored (e.g. "for $l_{\max}\to\infty$",
"at late times, z≪z_ν", "with oscillations, having included the neutrino
chemical potentials"), modals ("typically requires", "is expected to be",
"apparent preference"), attributions (the massless result to its Ref. 5),
and two narrowings: `mass:77` the 0.1 % check of arXiv:2407.10965 Fig. 1 is
for −0.15 eV, not ±0.15 eV (the coordinator's fix of 2026-11-10 had written
±); `interacting:100` the subtraction of the resonant contribution is
stated for Fig. 5 only. Coordinator spot-checks, whole statement:
`mass:77`, `interacting:100` (Fig. 6 caption of arXiv:2602.12477, Dirac-like
neutrinos): ok. G1: check_numbers and check_equations empty; transcription
232 equations, 171 exact, 43 contained, 0 mismatch; check_shape 0
problems; 156 tests passed. Draw: `docs/history/tests/g2/thcosmo-neutrinos-light-relics-dossiers-2026-11-12-redraw4.md`
(seed 1131); part 3 and the 20 part-2 rows on changed lines to be re-read.

## 2026-11-12 — `thcosmo-dark-energy` dossiers: qualifier sweep

One agent re-read every attributed statement of the three dossiers (about
255; about 68 research calls) and changed 59 places, all wording within the
paper's scope except one factual error: `interacting-de-instabilities.md:87`
called both w = −0.9 and w = −1.1 unstable, where Fig. 4 of
arXiv:0901.1611 shows w = −0.9 free of the early-time instability. One
general claim narrowed to its single case: `thawing:104` "differ by
$\mathcal{O}(100\%)$" is the k²M_pl² = 100 hilltop of Fig. 4 of
arXiv:2405.03933. One place corrected: `ppf:15` Sect. II.1, not III.1.
`[doc:]` statements on CAMB and CLASS not re-checked. G1:
check_numbers and check_equations empty; transcription 305 equations, 208
exact, 60 contained, 0 mismatch; check_shape 0 problems. The G3 pass of
2026-11-05 stands as history; the dossiers are re-gated: draw
`docs/history/tests/g2/thcosmo-dark-energy-dossiers-2026-11-12-sweep.md`
(seed 1132), part 3 and the 43 part-2 rows on changed lines to be re-read.

## 2026-11-12 — stage 5 W1, `thcosmo-neutrinos-light-relics` dossiers, G3 draw after the second sweep: **passed**

Sheet: `docs/history/tests/g2/thcosmo-neutrinos-light-relics-dossiers-2026-11-12-redraw4.md`
(seed 1131), the first draw after the owner's decision, reported as it
fell. Part 2: the 20 rows on changed lines re-read, 18 ok, 2 wrong (one
line). Part 3: 59 ok, 0 wrong, 0 unclear. Audit questions 1–3 answered
(first draw). Fixed at source, read by the coordinator in the paper:
- `mass:66` (part 2): the second sweep put "[src: Sect. 2.1, text before
  Eq. 2.2]" after the 7.5 enhancement, which is printed after Eq. 2.2 of
  arXiv:2407.07878; "[src: Sect. 2.1, text after Eq. 2.2]" placed after
  "≈ 7.5".
- Side finding applied: `interacting:13` N is "a normalisation factor"
  (arXiv:2606.03395 Sect. 2.3); place added.
- Not applied: `mass:118` gives the 7.5 at "z ≪ z_ν" as the paper does; the
  `[der]` line `mass:130` already warns that the figures refer to different
  redshifts.
G1: check_numbers and check_equations empty; transcription 232 equations,
171 exact, 43 contained, 0 mismatch; check_shape 0 problems; 156 tests
passed. Word share: Bennett 14.7 %, Lesgourgues 13.6 %. The three dossiers
added to the file map of `SKILL.md` and the `files` column of
`subtopics.tsv`. `thcosmo-neutrinos-light-relics` gap audit closed; the
light-sterile deepening run (question 8) stays queued. W1 dossiers closed
(the `thcosmo-dark-energy` re-gate and the `thcosmo-dark-matter-models`
sweep are the owner's later strictness pass, not W1 gates).

## 2026-11-12 — `thcosmo-dark-matter-models` dossiers: qualifier sweep

One agent re-read every attributed statement of the three dossiers (about
310; about 100 research calls) and made 53 edits: hedges and conditions
restored (e.g. "can be affected", "can deviate … by up to approximately
15%", "strongly suggests", "assuming a standard cosmology and canonical
properties for the axion", "in the high-lepton asymmetry regime"), places
corrected (`axion:72` Sect. I, not VII), four derived sentences tagged
`[der]`, one unsourced sentence removed (`noncold:13`). Two factual errors:
- `axion:114`: "neither includes strings" was wrong for arXiv:0903.4377,
  whose Sect. VI includes in $\Omega_a$ "the contribution from axionic
  strings decay, Eq. (45)"; read by the coordinator: ok.
- `axion:73`: the q ≈ 1 statement attributed to Buschmann et al. a
  logarithmic enhancement; arXiv:2108.05368 ("Dark matter density") finds
  δ ∝ log(m_r/H) if the spectrum "is exactly scale invariant at large k".
  The sweep's added inference that $\log_{*}$ "drops out" of their
  $n_a^{\rm string}$ is not in the paper; removed by the coordinator.
The agent stashed and restored the working tree once while comparing
checker baselines (`git stash list` empty afterwards; no file lost). G1:
check_numbers and check_equations empty; transcription 299 equations, 154
exact, 43 contained, 0 mismatch; check_shape 0 problems; 156 tests passed.
The G3 pass of 2026-11-10 stands as history; re-gate draw
`docs/history/tests/g2/thcosmo-dark-matter-models-dossiers-2026-11-12-sweep.md`
(seed 1133): part 3 and the 25 part-2 rows on changed lines to be re-read.

## 2026-11-12 — `thcosmo-dark-energy` dossiers, G3 re-gate after the sweep: fails

Sheet: `docs/history/tests/g2/thcosmo-dark-energy-dossiers-2026-11-12-sweep.md`
(seed 1132). Part 2: the 43 rows on changed lines re-read, 41 ok, 2 wrong.
Part 3: 55 ok, 4 wrong (one shared with part 2). The factual fix of
`interacting:87` confirmed (Sect. 3.4 of arXiv:0901.1611: Fig. 4 right panel
unstable, left panel free of instabilities), its place incomplete. Fixed at
source, each read by the coordinator in the paper:
- `ppf:34`: Jeans stable "so long as $p_{e}^{\prime}/\rho_{e}^{\prime}$
  remains finite" (arXiv:0808.3125 Sect. II, after Eq. 4).
- `thawing:92`: the slope "can vary by" ∼10 % (arXiv:2405.03933 Sect. 3).
- `thawing:70`: the pivot "(assuming such a limit exists in the models
  being fitted)" (same place).
- `interacting:87`: place "Sect. 3.4, text after Eq. 43" added.
- Not yet verified by the coordinator, passed to the second sweep:
  `thawing:69` (the premise "with w near −1 … Ω_φ given by equation (25)"
  of Crittenden's scheme in arXiv:0712.3450), and the side findings
  `ppf:58`, `ppf:82`, `thawing:47`, `interacting:14`.
- Tool note: sheet rows 56–57 credit two equations to arXiv:2410.10981
  where the dossier cites arXiv:0708.0024 (a parsing slip of
  `sample_statements.py`, not a dossier error); to fix in the tool.

## 2026-11-12 — `thcosmo-dark-matter-models` dossiers, G3 re-gate after the sweep: fails

Sheet: `docs/history/tests/g2/thcosmo-dark-matter-models-dossiers-2026-11-12-sweep.md`
(seed 1133). Part 2: the 25 rows on changed lines re-read, 25 ok. Part 3:
58 ok, 1 wrong. Both factual fixes (`axion:73`, `:114`) confirmed. Fixed at
source, read by the coordinator in the paper:
- `axion:96` (part 3): the 28 μeV row of arXiv:2003.01100 Eq. 170 also
  assumes $\langle\theta_{i}^{2}\rangle=(2.15)^{2}$ and
  $g_{*}(T\gtrsim T_{C})$ = 61.75, and "a standard cosmology and canonical
  properties for the axion" (text after Eq. 170); added.
- Side findings applied: `axion:60` the unsourced "about fifty e-folds"
  removed; `axion:62` the hedge of arXiv:2007.04990 Sect. 4 ("cannot
  exclude a partial destructive interference", "highly unlikely … beyond
  an ${\cal O}(1)$ factor") added.
- Passed to the second sweep: `axion:30` ("Within this pre-inflation
  scenario", the scalings stated after Eq. S36), `noncold:125` (the
  correction factor is reported from Refs. [36, 74] of arXiv:2011.13458).

Both domains take the neutrinos path decided by the owner: a second full
sweep, then one draw reported as it falls.

## 2026-11-12 — `thcosmo-dark-energy` dossiers: second qualifier sweep

A fresh agent read every attributed statement whole (about 260; `[doc:]`
quotes checked in CAMB `dark_energy.py`, `DarkEnergyPPF.f90` and CLASS
`explanatory.ini` on GitHub master: all match) and made 30 fixes, none
factual: premises restored (`thawing:69` "With w near -1, they took the
evolution for Ω_φ to be given by equation (25)…", `thawing:42` "in the limit
where the Hubble parameter … is well-approximated by ΛCDM", `ppf:34`,
`ppf:41`), scopes (`interacting:57` "no matter how weak the coupling is"
belongs to the Γρ_c model; the αℋρ_c model is among "The other models
discussed in Sec. III" that "also suffer from this instability",
arXiv:0804.0232 Sect. IV), places (`interacting:70`, `:100` Eq. 44;
`interacting:14` Sect. II, Eq. 6), an unread attribution removed
(`ppf:16`), six own readings tagged `[der]`, and the code of
arXiv:2511.22478 named from its App. C (`ppf:58`, `:83`). Coordinator
spot-check, whole statement: `interacting:57` in arXiv:0804.0232 Sect. IV:
ok. G1: check_numbers and check_equations empty; transcription 306
equations, 211 exact, 60 contained, 0 mismatch; check_shape 0 problems;
157 tests passed. Draw: `docs/history/tests/g2/thcosmo-dark-energy-dossiers-2026-11-12-sweep2.md`
(seed 1134), reported as it falls.

## 2026-11-12 — tool: `check_transcription.py` attribution

The DE re-gate found two equations credited to the paper cited later in the
line (arXiv:2410.10981) where the line's convention gives them to the paper
cited before (arXiv:0708.0024). The tool now reads an equation in the paper
cited before it when its flag closes that citation and the later paper does
not hold it. Effect over all domains: DE and DM 2 unreadable → exact each;
no other count changed. Test added (`test_flag_closes_the_citation_of_the_paper_before`).
The owner asked on 2026-11-12 for one agent at a time.

## 2026-11-12 — `thcosmo-dark-energy` dossiers, G3 draw after the second sweep: fails

Sheet: `docs/history/tests/g2/thcosmo-dark-energy-dossiers-2026-11-12-sweep2.md`
(seed 1134), reported as it fell. Part 2: the 18 rows on changed lines,
17 ok, 1 wrong. Part 3: 58 ok, 1 wrong (one-sided 95 % bound 7.8 %). Fixed
at source, read by the coordinator in the paper:
- `ppf:69` (part 3): the Fig. 2 caption of arXiv:0808.3125 has "a two-field
  crossing model that approximates" $w_0=-1.15$, $w_a=0.5$, "flat"; both
  restored.
- `thawing:47` (part 2): the Caldwell–Linder bounds "are valid for
  (1+w)≪1, and so w≲−0.8 is a practical limit of applicability"
  (arXiv:astro-ph/0505494, text after Fig. 1); added.
- Side findings applied: `interacting:48` the `[der]` "turns Hubble friction
  into anti-friction" replaced by the paper's "a positive d acts as an
  antidamping source" (arXiv:0901.1611 Sect. 2.4); `interacting:31` Eqs.
  47–50 of arXiv:0804.0232 also assume $\pi_{c}=0=\pi_{x}$ and $w_{c}=0$.
- Not yet checked by the coordinator: `ppf:41` (the paper enforces ζ
  conservation through the $U_e$–$V_T$ relation, not the Einstein equation
  itself).
G1 after the fixes: check_numbers and check_equations empty; transcription
308 equations, 211 exact, 62 contained, 0 mismatch; check_shape 0
problems; 157 tests passed. Closure put to the owner (the neutrinos path,
second sweep then one draw, did not close this domain).

## 2026-11-12 — `thcosmo-dark-matter-models` dossiers: second qualifier sweep

A fresh agent read every attributed statement whole (about 510 tagged
places; about 85 research calls) and made 30 fixes. Two factual errors:
`noncold:43` the WDM–NCDM correspondence was traced to "Viel et al. (their
Ref. [69])", but Ref. [69] of arXiv:2011.13458 is Colombi, Dodelson &
Widrow (read by the coordinator in its reference list: ok); `axion:35` and
row 93 gave θ_i ≈ 2.15 as Di Luzio et al.'s own, where arXiv:2003.01100
Sect. 3.3 credits it to its Ref. [47]. The two pre-flagged items settled
(`axion:30`, `noncold:125`); Assumptions cells completed (`axion:96`, `:99`,
`:102`, `noncold:112`, `:114`); hedges and premises restored; credits to
the original fits; scopes narrowed; seven own readings tagged `[der]`. G1:
check_numbers and check_equations empty; transcription 300 equations, 157
exact, 43 contained, 0 mismatch; check_shape 0 problems; 157 tests passed.
Draw: `docs/history/tests/g2/thcosmo-dark-matter-models-dossiers-2026-11-12-sweep2.md`
(seed 1135), reported as it falls.

## 2026-11-12 — `thcosmo-dark-matter-models` dossiers, G3 draw after the second sweep: fails

Sheet: `docs/history/tests/g2/thcosmo-dark-matter-models-dossiers-2026-11-12-sweep2.md`
(seed 1135), reported as it fell. Part 2: the 26 rows on changed lines,
24 ok, 2 wrong. Part 3: 55 ok, 4 wrong (the first re-gate, seed 1133, had
1). All six read by the coordinator in the paper and fixed at source:
- `axion:13` (P3): the power law of arXiv:2003.01100 Eq. 150 is assumed
  "For definiteness" to hold "well above $T_{C}$" (Sect. 3.2).
- `noncold:103` (P3): 18.5 keV is a "non-resonant sterile neutrino mass"
  from a "2-σ bound" on thermal WDM (arXiv:1601.07553 Sect. 4.1).
- `axion:63` (P3): the lower $f_a$ bound "conservatively allowed" the
  remaining string energy to go into axions (arXiv:2108.05368).
- `relic:110` (P3): "nearly 10%" is for "the 1-1000 GeV dark matter
  abundance, compared to the conventional estimate of the EOS"
  (arXiv:2005.03544 abstract).
- `noncold:29` (P2): the 14 → 26 % correction is "For spin-1/2 thermal WDM"
  (arXiv:2210.10753 Sect. IV).
- `noncold:84` (P2): "well described by (2.27)" is in the text after Eq.
  2.29; the other case is footnote 7, not 6 (arXiv:2011.13458).
- Side findings not yet checked by the coordinator: `noncold:76` and `:54`
  untagged own claims and a place (Sect. II.1, not II.3); `noncold:125`,
  `:49` "partially"; `noncold:98` θ, η fitted at 2 keV only; `axion:63`
  the range words are from the abstract.
G1 after the fixes: check_numbers and check_equations empty; transcription
300 equations, 157 exact, 43 contained, 0 mismatch; check_shape 0
problems; 157 tests passed. Two sweeps have not brought the strict-standard
error rate of these dossiers to the level a 0/59 draw needs (1/59, then
4/59); closure put to the owner with the DE dossiers.

## 2026-11-13 — owner decision: `thcosmo-dark-energy` and `thcosmo-dark-matter-models` dossiers closed with the residual logged

Asked how to close the strict-standard re-gates after two sweeps each, the
owner chose to accept and log the residual. Every error found by the six
draws and four sweeps is fixed at source. Last draws, strict reading:
`thcosmo-dark-energy` 1 wrong in 59 (seed 1134; point estimate 1.7 %,
one-sided 95 % upper bound 7.8 %); `thcosmo-dark-matter-models` 4 wrong in
59 (seed 1135; 6.8 %, upper bound 14.8 %). These rates are of dropped
hedges, conditions, premises, scopes and places; no equation and no number
was found wrong in either draw. Their G3 passes of 2026-11-05 and
2026-11-10 (looser reading) stand; the strict-standard residual is the
figure to quote for these dossiers. A refresh pass can return to them.

## 2026-11-13 — stage 5 W2, `thcosmo-cosmological-gravitational-waves` deepening, G1: passed

One run (radiation bound, preheating; rebalance; five side findings of the
dossier G3). Added: formalism "The background as extra radiation"
(arXiv:2508.15134, arXiv:2004.11396), BBN and CMB bounds in results
(arXiv:0708.2279, astro-ph/0603144, 2004.11396, 2507.06930, 2508.15134),
the preheating no-go theorem, peak estimates and lattice projection
(arXiv:0707.0875, 1907.04402, 2512.15627, 1110.0337), the
parametric-resonance card expanded (arXiv:1707.04533), new cards for gauge
preheating and oscillons, approximations and open questions to match
(arXiv:1607.01314 against 1803.08047; 1905.05724). Both subtopics now
`covered`; 26 sources added (108). The five side findings settled
(`phase-transition-spectra.md:41`, `:109`, `cosmic-string-spectra.md:57`,
`:64`, arXiv:2508.04263 Eq. 4). G1: verify_sources 108, 0 problems;
check_numbers and check_equations empty; transcription 449 equations, 338
exact, 62 contained, 0 mismatch, 49 unreadable; places 66, 41
found-at-place, 1 found-elsewhere, 24 unreadable; check_shape 0 problems;
no `eq: notation` escape in references; 157 tests passed. Word share:
Caprini 23.0 % (was 47.1 % at build, 28.6 % after the dossiers), Hindmarsh
4.9 %, Domènech 4.3 %. The remaining Caprini share is the review
arXiv:1801.04268 as source of the basic formalism (tensor equation,
stochastic background, transfer of the inflationary background), now with
primary citations beside it where they were read, and the LISA reports
(arXiv:1910.13125, 2403.03723) as the templates the field uses; justified,
no further rebalance before the refresh pass. Slips recorded in the hub's
`stale-claims.md`: arXiv:0707.0875 Eq. 82, arXiv:2508.04263 Eq. 4; not
recorded: a missing unit in arXiv:1909.12843 (not a physics slip). G2
sheet over the changed lines: `docs/history/tests/g2/thcosmo-cosmological-gravitational-waves-deepening-2026-11-13.md`
(seed 1136).

## 2026-11-13 — stage 5 W2, `thcosmo-cosmological-gravitational-waves` deepening, G2: fails

Sheet: `docs/history/tests/g2/thcosmo-cosmological-gravitational-waves-deepening-2026-11-13.md`
(seed 1136), changed lines only, strict standard. Part 1: the 3 changed
rows ok. Part 2: 46 ok, 10 wrong. Part 3: 44 ok, 15 wrong. The wrong rows
come from eight defective lines (a defect marks every item of its line); no
equation and no number misprinted: places (`formalism.md:37` Maggiore
defines $S_h$ by Eq. 8, `:50`, `:98` "next sentence", `results.md:15`),
attributions (`formalism.md:138` bare tags after an inserted clause read as
the wrong paper; `results.md:13` the sBBN bound is quoted by Boyle &
Buonanno from their Refs. [71–76]), premises and hedges (`formalism.md:138`
"It can be argued", `models.md:43` "in a simple scalar field model" and
"agree with the predictions expected from numerical simulations",
`results.md:16` "Assuming adiabatic initial conditions" and "using the
upper limit"). Read by the coordinator: `models.md:43` (arXiv:1905.05724
abstract) and `results.md:16` (arXiv:2004.11396 Sect. 3.2): wrong as
reported. Both printed slips of the hub confirmed; the locator of the
arXiv:0707.0875 slip ("the next sentence") is off, also in
`stale-claims.md`. The deepening's new lines carry the dropped-qualifier
pattern of the DE and DM dossiers; as there, a qualifier sweep of the
changed lines (with the eight items and the side findings) precedes a
fresh draw.

## 2026-11-13 — `thcosmo-cosmological-gravitational-waves` deepening: qualifier sweep

One agent read every added or changed line whole (about 176, and the
2026-11-13 row of the hub's `stale-claims.md`; about 65 research calls).
The eight items of the G2 sheet were all as reported and are fixed (places,
attributions, premises, hedges; `formalism.md:138` Eqs. 381 and 383 now
carry arXiv:1801.04268; the arXiv:0707.0875 slip locator now names the
sentence). Side findings fixed (`formalism.md:95` the no-go theorem quoted
whole with "at first order in the gravitational coupling"; `:90–91` the
priority claim replaced, Eqs. 296 and 299 sourced to the review's Ref.
[401] = arXiv:1707.04533; `:63`; `open-questions.md:36`;
`approximations.md:85`; SKILL.md 67–68; dossier snapshots set to
2026-11-13). Further errors found: `results.md:104` "saturates N_eff
bounds" not in the paper, now "generically contribute significantly"
(arXiv:1909.12843 abstract, read by the coordinator: verbatim);
`approximations.md:76` a quote made verbatim; `:86`; `models.md:60`, `:62`
"Under certain conditions"; `models.md:49` place; `results.md:47`
"preliminary estimates"; `formalism.md:100` credit; three bare
`[src: References]` tags moved. G1: verify_sources 108, 0 problems;
check_numbers and check_equations empty; transcription 450 equations, 341
exact, 62 contained, 0 mismatch; check_shape 0 problems; 157 tests passed.
Fresh draw over the changed lines: `docs/history/tests/g2/thcosmo-cosmological-gravitational-waves-deepening-2026-11-13-redraw.md`
(seed 1137), reported as it falls.

## 2026-11-13 — `thcosmo-cosmological-gravitational-waves` deepening, G2 fresh draw after the sweep: fails

Sheet: `docs/history/tests/g2/thcosmo-cosmological-gravitational-waves-deepening-2026-11-13-redraw.md`
(seed 1137), reported as it fell. Part 1: 3 changed rows ok. Part 2: 52 ok,
2 wrong. Part 3: 54 ok, 5 wrong, from two lines (one-sided 95 % bound on
the line-level rate not computed; per item 8.5 %, upper bound 17 %). No
equation or number wrong. Three lines, each read by the coordinator in the
paper and fixed at source:
- `formalism.md:37`: Maggiore's Eq. 8 holds "For a stochastic background,
  assumed to be isotropic, unpolarized and stationary" (arXiv:gr-qc/9909001
  Sect. 2.2); added.
- `formalism.md:68`: the transfer function of arXiv:astro-ph/0512014
  incorporates "dark energy with time-varying equation-of-state w(z)";
  the abstract's three items quoted.
- `open-questions.md:35`: the bounds of arXiv:2507.06930 are 95 % CL
  "assuming a uniform prior", and "can become tighter by a factor of" ∼4
  with a log-uniform prior, "suggesting the results to be prior-sensitive"
  (abstract); added.
- Side findings not yet checked: `formalism.md:63` (Eq. 203 "at the lowest
  order in the slow-roll parameters"), `:91` (the δ tail belongs to Ĩ),
  `:49` (Eq. 33 from its Ref. [102]), `cosmic-string-spectra.md:57`
  ("for large tensions" for Gμ ≳ 10⁻⁷), `results.md:26` and
  `open-questions.md:70` (forecast fiducials).
G1 after the fixes: check_numbers and check_equations empty; transcription
450 equations, 341 exact, 62 contained, 0 mismatch; check_shape 0
problems; 157 tests passed. Closure put to the owner.

## 2026-11-13 — owner decision D36; `thcosmo-cosmological-gravitational-waves` deepening closed

The owner made the DE/DM closure a standing rule (D36, recorded in
`docs/plans/2026-10-30-decisions.md` with D35, the strict reading of
2026-11-12): a fresh draw after one full qualifier sweep that still fails
on wording only is closed once every error is fixed at source, with the
residual logged; an equation or number error keeps D20. Applied to the GW
deepening: last draw (seed 1137) 5 wrong in 59 from two lines, all
wording, all fixed at source; residual per item 8.5 % (one-sided 95 %
upper bound 17 %), per defective line lower (the draw has several items on
a line). The deepening is closed; both subtopics `covered`. Six side
findings stay listed in the previous entry for the refresh pass.
`thcosmo-cosmological-gravitational-waves` is complete for W2: built, three
dossiers, one deepening.

## 2026-11-13 — stage 5 W2, `thcosmo-baryogenesis-phase-transitions` build, G1: passed

First build under the mandatory qualifier pass (the agent reports about
250 attributed statements checked, about 100 changed). 49 sources; files
SKILL.md 126 lines, formalism 150, models 147, results 79, approximations
88, open-questions 75. Thin: Affleck–Dine and other mechanisms. Pre-arXiv
foundations (Sakharov, Coleman, Linde, Kuzmin–Rubakov–Shaposhnikov,
Affleck–Dine, Fukugita–Yanagida) cited through reviews (rule 6). G1:
verify_sources 49, 0 problems; check_numbers and check_equations empty;
transcription 274 equations, 151 exact, 50 contained, 0 mismatch, 73
unreadable; places 9, 4 found-at-place, 5 unreadable; check_shape 0
problems; 5 `eq: notation` escapes (SKILL 2, formalism 2, models 1); 158
tests passed. Word share: Bodeker 26.5 % and Athron 19.4 % flagged (the
review of Bodeker & Buchmüller and the bubble-dynamics review of Athron et
al. carry the formalism); rebalance to be done in the deepening run.
Tool fix: `verify_sources.py` cut DOIs at the first parenthesis
(Elsevier DOIs such as 10.1016/0550-3213(83)90072-X), so the agent had
percent-encoded four of them; the pattern now keeps balanced parentheses
(test added) and the four DOIs are restored. Findings the build reports
against textbook expectations, for G2 to confirm: the 2025 lattice washout
criterion $v/T_c\gtrsim 1.33$; non-zero friction in local thermal
equilibrium; the vanishing of the leading-order vev-insertion CP source.
G2 sheet: `docs/history/tests/g2/thcosmo-baryogenesis-phase-transitions-2026-11-13.md`
(seed 1138).

## 2026-11-13 — `thcosmo-baryogenesis-phase-transitions` build, G2: fails on wording

Sheet: `docs/history/tests/g2/thcosmo-baryogenesis-phase-transitions-2026-11-13.md`
(seed 1138), strict standard. Part 1: 21 ok, 3 wrong. Part 2: 113 ok, 2
wrong. Part 3: 58 ok, 1 wrong (from one line). No equation and no number
wrong: the first build under the qualifier pass has the lowest part-3 rate
of the suite's strict-standard draws. The three findings against textbook
expectations confirmed (arXiv:2506.04939 abstract, $v/T_c\gtrsim 1.33$;
arXiv:2305.02357 Eq. 5.63 friction in LTE, and its "leading-log
approximation underestimates the friction" read from its Refs. [517, 518];
arXiv:2508.09989 Sect. 3.4.1, the vev-insertion source vanishing "at
leading order in the gradient expansion"). Fixed at source, each read by
the coordinator in the paper:
- `SKILL.md:34`: the review's own $R_{\rm sep}$ is Eq. 5.49 (exponential
  rate, expansion neglected, "Strictly speaking" at $P_f=1/e$); Eq. 5.50 is
  its Ref. [10]'s modification (arXiv:2305.02357 Sect. 5.4).
- `SKILL.md:38`: "For a hierarchical spectrum of right-handed neutrinos"
  (arXiv:hep-ph/0202239 abstract); "Assuming $\widetilde{m}_{1}=\mathcal{O}(m_{i})$"
  for Eq. 111 (arXiv:2009.07294).
- `SKILL.md:41`: decaying MHD with "vanishing velocity field at the initial
  time"; the helical law "determined by simulations" (arXiv:2010.10525
  Sect. IV.1).
- `approximations.md:28`: "not ultra-relativistic" is text before Eq. 5.62.
- `results.md:24`: the abstract reads "by applying previous lattice
  results"; quoted.
- `models.md:35` (part 3): Eq. 113 of arXiv:2009.07294 holds for
  "$M_{1}/M_{3}\sim 10^{-5}\cdots 10^{-4}$" and "$\kappa_{f}\sim 10^{-2}\cdots 10^{-1}$";
  the sentence called "not read" quoted whole.
- Side findings applied: `approximations.md:19` place (text after Eq.
  5.49); `formalism.md:14`, `:104` the variable is "$z=M/T$" (Sect.
  IV.3.1). Not yet checked: "paragraph after Fig. 5" (four places, the
  third paragraph per the reviewer); the tool attached the wrong paper to
  sheet rows 10, 26, 67 (skill lines correct).
G1 after the fixes: check_numbers and check_equations empty; transcription
279 equations, 152 exact, 51 contained, 0 mismatch, 76 unreadable;
check_shape 0 problems; 158 tests passed. No sweep has run on this skill,
so D20 applies: fresh draw `docs/history/tests/g2/thcosmo-baryogenesis-phase-transitions-2026-11-13-redraw.md`
(seed 1139), part 3 and the rows on changed lines to be re-read.

## 2026-11-13 — `thcosmo-baryogenesis-phase-transitions` build, G2 fresh draw: fails on wording

Sheet: `docs/history/tests/g2/thcosmo-baryogenesis-phase-transitions-2026-11-13-redraw.md`
(seed 1139), reported as it fell. Parts 1–2: the 9 rows on fixed lines,
8 ok, 1 wrong. Part 3: 54 ok, 5 wrong (four lines), no equation or number
error. Two fixes of the first draw were incomplete: `SKILL.md:38` still
lacked the premises of the Davidson–Ibarra bound, and the coordinator's
place fix of `approximations.md:19` moved the error (the "caution" quotes
are in the paragraph after Eq. 5.50). Fixed at source, read by the
coordinator in the paper:
- `SKILL.md:38`: $m_{\nu_3}=\sqrt{\Delta m^2_{\rm atm}}$, thermal ν_R,
  $T_{\rm reh}>M_{\nu_R}>10^8$ GeV, and the $10^9$ GeV from "Reasonable
  estimates … as made by Buchmuller and Plumacher" (arXiv:hep-ph/0202239
  abstract); the bare tag of Eq. 111's premise now names arXiv:2009.07294.
- `approximations.md:19`: both places given.
- `approximations.md:68`: lepton chemical potentials family-independent
  "For simplicity" (arXiv:2009.07294 Sect. II.3).
- `models.md:121`: Eq. 35 adopted "at least for a short time" as "a simple
  power law in conformal time" (arXiv:1303.7121 Sect. 3.1.1).
- Passed to the sweep, not yet checked: `models.md:114` (assumptions of the
  random-walk estimate $E_M\sim k^3$); side findings `formalism.md:35`,
  `:122`, "paragraph after Fig. 5" in four places.
G1 after the fixes: check_numbers and check_equations empty; transcription
280 equations, 152 exact, 51 contained, 0 mismatch; check_shape 0 problems;
158 tests passed. D36 path: one full qualifier sweep, then a fresh draw.
