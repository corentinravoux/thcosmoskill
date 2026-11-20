# Changelog

Each release names the commit it was cut from. The plans that set each step
are in `docs/plans/`; the record of every gate is
`docs/history/tests/gate-log.md`.

## 0.3.0 — 2026-11-20

Waves W1 and W2: six domain skills added, dossiers for every built domain,
and a strict reading of hedges at every gate. Plan:
`docs/plans/2026-10-30-plan-v2.md`, stage 5; every gate in
`docs/history/tests/gate-log.md`; manifest `releases/0.3.0.tsv` (841
sections added, 23 changed, none moved or retired, against `d69c4d3`).

- **New domains**: `thcosmo-dark-energy`, `thcosmo-dark-matter-models`,
  `thcosmo-neutrinos-light-relics` (W1);
  `thcosmo-cosmological-gravitational-waves`,
  `thcosmo-baryogenesis-phase-transitions`, `thcosmo-pbh-defects` (W2).
  Each passed G1 (tools) and G2 (re-read in the papers).
- **Dossiers**: 37 in all, three to six per domain, each answering the
  gap-audit questions that caused it and gated at G3. **Deepening runs**
  for the thin subtopics of modified gravity, the three W2 domains and the
  light sterile neutrinos.
- **Strict reading (owner decisions D35, D36, in
  `docs/plans/2026-10-30-decisions.md`)**: a dropped hedge, condition,
  premise, range or scope, a wrong place or a wrong attribution counts as
  an error in a draw. A draw that still fails on wording after one full
  qualifier sweep is closed once every error is fixed at source, with the
  residual logged; equation and number errors keep the zero-in-59 rule. The
  dark-energy and dark-matter dossiers were re-gated under this reading.
  The agent briefs carry a mandatory qualifier pass.
- **Hub**: router marks ten domains built; `stale-claims.md` holds 90
  rows, among them the printed slips confirmed at source in W1–W2.
- **Tools**: `check_transcription.py` reads section-prefixed equation
  labels (`II.19`) and attributes an equation to the paper cited before
  it when its flag closes that citation; `latex_norm.py` normalises
  `\mspace` and `\rightarrow`; `verify_sources.py` keeps balanced
  parentheses in DOIs; `sample_statements.py --changed-since` draws a
  deepening's new lines only.
- 1019 sources checked against arXiv; 159 tests pass.

## 0.2.0 — 2026-11-03

First milestone: the hub and four domain skills. Plan:
`docs/plans/2026-10-30-plan-v2.md`, stages 3 and 4; every gate in
`docs/history/tests/gate-log.md`. Owner decision of 2026-11-02: the pilot
review (P2) skipped, the pilot accepted on its gates; pace as fast as
limits allow.

- **`thcosmo-lss-perturbation-theory`** (pilot): SPT, LPT, EFTofLSS, IR
  resummation, bias, redshift space, consistency relations, PNG, velocity
  statistics, intrinsic alignments, large deviations, field-level forward
  models; six dossiers in `deep/`. Gates G1, G2 (59/59), G3 (59/59).
- **`thcosmo-inflation`**: slow roll and flow parameters, single-field
  models, attractors, ultra-slow and constant roll, multi-field, reheating
  and preheating, initial conditions, stochastic and eternal inflation,
  n_s and r after ACT DR6. Gates G1, G2 (59/59).
- **`thcosmo-primordial-correlators`**: in-in, EFT of inflation, shapes,
  consistency relations, collider, bootstrap, features, loops,
  decoherence, QFT in de Sitter. Gates G1, G2 (59/59).
- **`thcosmo-modified-gravity`**: Horndeski to DHOST, f(R), massive
  gravity and bigravity, vector–tensor, teleparallel and f(Q), non-local
  gravity, screening, consistency and positivity, EFT of dark energy, the
  tensor sector, screening in simulations. Gates G1, G2 (59/59).
- **Hub `theoretical-cosmology`**: conventions atlas (G2 59/59); router
  marks the four domains built; `methods-index.md` names the home section
  of each method; `stale-claims.md` holds 26 corrected statements and 17
  printed slips confirmed at source.
- **Brief**: numbers in the form printed, qualitative claims quoted, hedges
  and qualifiers kept (from the G2 and G3 findings).
- 301 sources checked against arXiv; tests pass.
- **For layer users:** `releases/0.2.0.tsv` lists 345 added and 14
  changed sections.

## 0.1.0 — 2026-10-30

Base release: the machinery of cosmoskill 1.0.3, adapted to theoretical
cosmology. No domain skill yet. Plan: `docs/plans/2026-10-30-plan.md`.

- **Hub `theoretical-cosmology`**: router table of the twenty planned
  domains, levels, review rules; skeleton references (`conventions`,
  `review-rubric`, `review-checklists`) and `suite-conventions` with the
  theory file contract (`formalism`, `models`, `results`, `approximations`,
  `open-questions`) and the equation-provenance rules.
- **Scripts** from cosmoskill, renamed: `fetch_paper.py`, `verify_sources.py`
  (source roles `textbook`, `lectures`, `model`, `constraint` added),
  `layers.py`, `sync_layers.py`, `promote.py`; layers in `~/.thcosmoskill/`
  and `.thcosmoskill/`, cache in `~/.cache/thcosmo-skill-verify/`.
- **`thcosmoskill-refine`** with an example layer attached to the hub.
- **Tools and tests** from cosmoskill; the level block states the equation
  rule; layer tests run against the fixture base; 112 tests.
- **Docs**: design, domain scopes and boundary with cosmoskill, research
  brief for theory, 66 verified anchor papers, plan.
