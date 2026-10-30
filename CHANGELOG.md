# Changelog

Each release names the commit it was cut from. The plans that set each step
are in `docs/plans/`; the record of every gate is
`docs/history/tests/gate-log.md`.

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
