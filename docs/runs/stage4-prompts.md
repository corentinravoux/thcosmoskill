# Stage 4 — prompts for the research runs

Ready to send, in this order, once stage 3 (the owner's questions and the
skills-off baseline) is done. Plan: `docs/plans/2026-10-30-plan-v2.md`,
stage 4. Fill `<date>` with the date of the run. At most two agents at a
time; the coordinator gates each run (recipe steps 2 and 3) before the next
depends on it.

## P4 — conventions atlas (first)

```
Build the conventions atlas of the thcosmoskill package in
~/Software/thcosmoskill: rewrite
plugin/skills/theoretical-cosmology/references/conventions.md. Date of the
run: <date>.

Follow docs/agent-brief.md, sections 1 to 2b and the citation format of
section 3. Keep the four sections and their keys (spacetime-and-gravity,
perturbations, early-universe, structure-formation-and-dark-sector); never
write, rename or remove a key line by hand.

For each convention listed in the file, write a table: the choices in use,
and which reference works adopt each, with the source and the place read
(equation or section). Reference works: lecture notes and reviews readable
on arXiv, first the anchors in docs/anchor-sources.tsv (for example
arXiv:0907.5424, arXiv:0809.4944, arXiv:astro-ph/0112551, arXiv:2212.08488,
arXiv:0709.0293, arXiv:1210.0201, arXiv:1901.07183, arXiv:1104.2932), then
others you find; the conventions of the main codes as [doc] facts.
Textbooks only through a readable source that cites them ([sec: ...]).
Add the relations between conventions that a paper states (for example
between potential and Hubble slow-roll parameters), each flagged [src];
no relation of your own making.

Cite with arXiv:<id>; add every cited paper to
plugin/skills/theoretical-cosmology/references/sources.tsv with the version
read. Budget: 90 research calls; keep a _progress.md beside the file and
delete it at the end. Write only conventions.md and the hub's sources.tsv.
Do not commit. Run the checks of docs/agent-brief.md, section 4, on
plugin/skills/theoretical-cosmology.
Final message under 200 words: conventions covered, sources, the checkers'
last lines, what is under "Not verified".
```

## P0 — hep-th probe (beside P4)

```
Run a probe for the thcosmoskill package in ~/Software/thcosmoskill. Date
of the run: <date>. Purpose: find where the provenance rules break on
high-energy-theory papers, before the pilot fixes the brief.

Write the start of plugin/skills/thcosmo-primordial-correlators/ as a build
would (docs/agent-brief.md), on three subtopics only: the in-in
calculation of the scalar bispectrum in single-field inflation; the
single-field consistency relation (squeezed limit); one result of QFT in de
Sitter space (choose from the anchor arXiv:2301.04146 and the papers it
builds on). Anchors: rows of docs/anchor-sources.tsv for
primordial-correlators. Write formalism.md, models.md (model cards),
results.md and sources.tsv for these subtopics only; no SKILL.md.

Budget: 40 research calls. Log every place where a rule could not be
followed in docs/history/tests/p0-probe.md: unnumbered equations, papers
without HTML, version changes, conventions mixed within one paper, errata,
equations too long or too nested to transcribe, anything else. For each,
propose the rule or tool change it needs. Do not commit.
Final message under 200 words: the breakages by kind, the proposed changes,
the checkers' last lines (check_equations, check_transcription).
```

## P1 — pilot build (after P4 and P0 are gated and the brief is revised)

```
Build the skill thcosmo-lss-perturbation-theory of the thcosmoskill package
in ~/Software/thcosmoskill. Date of the run: <date>.
Follow docs/agent-brief.md exactly. Scope and boundaries: the row of
thcosmo-lss-perturbation-theory in docs/scopes-domains.md and the two-home
rules. Anchor papers (already verified): the rows of docs/anchor-sources.tsv
whose domains column names lss-perturbation-theory. Seed subtopics, to be
replaced by the list you draw from reviews: SPT kernels and loops; LPT and
Zel'dovich; EFTofLSS counterterms; IR resummation; bias expansion and bases;
redshift space from Kaiser to EFT; consistency relations; PNG and
scale-dependent bias; velocity statistics and momentum power spectrum;
intrinsic alignments and shape bias; large-deviation and one-point
statistics; perturbative forward models.
Conventions: point to plugin/skills/theoretical-cosmology/references/conventions.md.
Budget: 90 research calls. Write only inside
plugin/skills/thcosmo-lss-perturbation-theory/. Do not commit.
```

## After each run (coordinator)

```bash
python3 tools/assign_keys.py && python3 tools/sync_blocks.py
python3 plugin/skills/theoretical-cosmology/scripts/verify_sources.py plugin/skills/<skill>
python3 tools/check_numbers.py --skill <skill> --list
python3 tools/check_equations.py --skill <skill> --list
python3 tools/check_transcription.py --skill <skill> --write
python3 tools/check_places.py --skill <skill> --write
python3 tools/check_shape.py --skill <skill>          # domains only
python3 tools/word_share.py --skill <skill>
python3 tools/sample_statements.py --skill <skill> --seed <n> > docs/history/tests/g2/<skill>-<date>.md
python3 -m pytest -q
```
