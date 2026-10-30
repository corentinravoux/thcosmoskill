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
  cache reads (0.38–0.45 USD as reported by the session). One answer began
  with a message of the claude-mem hook of the owner's setup: the
  environment's hooks appear in headless answers, in both baseline and
  skills-on runs alike.
- E1 template written to
  `~/Software/claude_config/reports/research/2026-10-30_thcosmoskill-q0/questions.md`
  (private, outside the package).
