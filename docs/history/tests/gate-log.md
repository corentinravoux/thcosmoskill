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
