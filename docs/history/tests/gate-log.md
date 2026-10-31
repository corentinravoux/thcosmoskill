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
