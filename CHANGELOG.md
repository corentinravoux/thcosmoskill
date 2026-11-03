# Changelog

Each release names the commit it was cut from. The plans that set each step
are in `docs/plans/`; the record of every gate is
`docs/history/tests/gate-log.md`.

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
