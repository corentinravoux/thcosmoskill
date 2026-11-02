# Stage 4 — prompts for the research runs

Plan: `docs/plans/2026-10-30-plan-v2.md`, stage 4. Same recipe and
after-run commands as `stage3-prompts.md`. Two agents at a time; the third
domain starts when the first build is gated.

## Build run (one per domain)

```
Build the skill thcosmo-<domain> of the thcosmoskill package in
~/Software/thcosmoskill. Date of the run: <date>.
Follow docs/agent-brief.md exactly (read it in full first, and
plugin/skills/theoretical-cosmology/references/suite-conventions.md#citations-and-provenance).
Scope and boundaries: the row of thcosmo-<domain> in docs/scopes-domains.md
and the two-home rules. Anchor papers (already verified): the rows of
docs/anchor-sources.tsv whose domains column names <domain>. Seed
subtopics, to be replaced by the list you draw from reviews: <plan §7>.
Conventions: point to plugin/skills/theoretical-cosmology/references/conventions.md.
The built pilot plugin/skills/thcosmo-lss-perturbation-theory/ shows the
expected shape; read it as a model, do not edit it.
Find papers with the arXiv MCP server (load its tools with ToolSearch) and
read equations with plugin/skills/theoretical-cosmology/scripts/fetch_paper.py.
Budget: 90 research calls. Write as you go (brief section 1b) and keep
references/_progress.md; if it already exists you are resuming. Write only
inside plugin/skills/thcosmo-<domain>/. Do not commit. Run the checks of
docs/agent-brief.md section 4 on your skill before finishing.
Final message under 200 words: subtopics covered, number of sources, the
checkers' last lines, what is under "Not verified".
```

For `thcosmo-primordial-correlators`, add: start from the P0 probe text in
`docs/history/tests/p0-probe/thcosmo-primordial-correlators/`, re-check it
against the current brief, keep what passes, build the rest.

Runs: `inflation` and `primordial-correlators` started 2026-11-02;
`modified-gravity` follows the first gated build.
