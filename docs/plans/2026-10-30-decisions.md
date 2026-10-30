# Decisions needed before the final plan

**Answered by the owner on 2026-10-30: every ★ option; D26 = owner only.
Amended the same day: D24–D28 withdrawn (no evaluation set, baseline or
blind test; usefulness is judged later from user feedback and
benchmarks); D5 and D22 follow user feedback instead of the blind test.** The plan built from these
answers is `2026-10-30-plan-v2.md`. Each decision lists its options, the
recommendation (★) and the reason. A later change is recorded here with
its date.

## A. Scope and architecture

| # | Decision | Options | Why the recommendation |
|---|---|---|---|
| D1 | Architecture | ★ hybrid: topical domains + hub artefacts (conventions atlas, methods index, stale-claims register) + fixed-schema model cards · plain topical domains | method questions and convention translation have no home in plain topical; dated cards make status checkable |
| D2 | `gr-background` | ★ fold into `cosmological-perturbations` · keep, build last and thin · keep as planned | no anchor review, textbook-bound, most duplicated by cosmoskill |
| D3 | `relics` | ★ rename `pbh-defects`, magnetogenesis to `baryogenesis-phase-transitions` · keep as one grab-bag domain · split three ways | the three topics share no formalism; magnetogenesis is sourced at transitions and inflation |
| D4 | `cosmic-dawn-igm` | ★ keep, build last · drop (cosmoskill covers the data side) · merge into `thermal-history` | IGM theory has users but one 2006 anchor; low priority |
| D5 | `theory-codes` | ★ build only if Q0 asks · build in the last wave regardless · fold code facts into each domain | mostly `[doc]` facts that go stale in two years |
| D6 | `modified-gravity` | ★ split only if the build exceeds twelve subtopics · split now (theories / EFT and parameterisations) | split costs a run; decide on evidence |
| D7 | Two-home rules | ★ adopt the five rules of the draft · write rules per case at build time | seven questions of twenty had two homes |
| D8 | Velocity statistics, IA, large deviations in `lss-perturbation-theory` | ★ add as subtopics, with a word-share check against tilt · add velocity statistics as its own domain · leave out | velocity statistics is the owner's field: include it, but weighted as the literature weights it |
| D9 | Overlap with cosmoskill's `cosmo-theory-foundations` | ★ thcosmoskill holds formalism; cosmoskill keeps "conventions each survey adopts" and points here · allow duplication, kept in step by a check · retire `cosmo-theory-foundations` into thcosmoskill | one home per equation; no change in content of cosmoskill beyond pointers |

## B. Provenance rules

| # | Decision | Options | Why |
|---|---|---|---|
| D10 | Coefficients inside equations | ★ an equation with its own `[src: Eq. n]` is sourced as a whole; a coefficient outside a sourced equation needs a source · count every coefficient separately | the first is the verbatim rule; the second floods the checker |
| D11 | Verbatim transcription | ★ verbatim up to a published list of meaning-preserving normalisations · strict character match · free rewriting | needed for `check_transcription.py`; strict fails on LaTeXML artefacts |
| D12 | Unnumbered equations | ★ `[src: Sect. 3.2, unnumbered display after Eq. 12]`, always in the human re-read · not allowed (cite another source) | some classics number nothing |
| D13 | Paper versions | ★ `version` column in `sources.tsv`; places refer to it; warning when arXiv has newer · cite latest version always | equation numbers move between versions |
| D14 | Papers without HTML | ★ maintainers may read the PDF (`pdftotext`, poppler as a maintainer tool), place `Eq. n (PDF vN)` · "Not verified" only | many hep-th and older papers lack HTML |
| D15 | Textbooks | ★ readable secondary source citing the textbook, else "Not verified"; Crossref check deferred to the first `doi:` row · allow textbook citations unread · build Crossref check now | the scripts cannot read textbooks |
| D16 | Errata in sources | ★ cite the corrected version; record the slip in `stale-claims.md` · copy verbatim with a note | verbatim copying would preserve known errors |
| D17 | Conversions between conventions | ★ only relations a paper states, flagged `[src]`; the atlas collects them · allow agent conversions flagged `[der]` · none at all | convention translation is the top theorist need, but agent algebra is the top error source |
| D18 | Symbolic checks (SymPy) | ★ not before 1.0 · prototype in stage 1 | checks algebra, not sources; T2b covers transcription |

## C. Process and gates

| # | Decision | Options | Why |
|---|---|---|---|
| D19 | Pilot | ★ conventions atlas, then hep-th probe (two or three `primordial-correlators` subtopics), then `lss-perturbation-theory` · pilot `inflation` instead · pilot only | owner can grade LSS; the probe covers hep-th mechanics |
| D20 | G2 pass threshold | ★ every SKILL.md and conventions item correct, and 95 % upper bound on error rate < 5 % over mechanically checked equations · zero errors in a 10 + 10 sample (old) · bound < 10 % | the old rule passes a 10 % error rate 35 % of the time |
| D21 | Dossiers | ★ zero to six per domain, from a gap audit · six per domain | cosmoskill already moved to "more only where a test shows a gap" |
| D22 | Order | ★ 0.2 = pilot + inflation + correlators + modified gravity; then value × staleness adjusted by Q0 · foundations first (old plan) | high-value, fast-moving domains first; foundations are the most textbook-bound |
| D23 | Model status staleness | ★ flag status dates older than six months · twelve months · no flag | DESI-era and swampland debates move monthly |
| D31 | Concurrency and pace | ★ two agents at a time, one window per week · two agents, as fast as limits allow · one agent | existing rule; owner time also goes to HDR and grants |

## D. Evaluation

| # | Decision | Options | Why |
|---|---|---|---|
| D24 | Q0 questions | ★ owner writes about 30 from real work before any build (≈ 3 h) · Claude drafts, owner edits · skip Q0 | questions written by Claude are not evidence |
| D25 | Baseline | ★ skills-off answers in fresh sessions now, stored unseen, re-run at Q0 time if the model has changed · baseline only at Q0 time | an early baseline cannot be contaminated by the build; a re-run keeps the comparison on one model version |
| D26 | Graders | ★ owner grades all, plus one second theorist on half if one can be found (name?) · owner only, stated as single-grader evidence | single-grader evidence is weak |
| D27 | Metrics | ★ correctness, convention errors, staleness detection, harm, routing and trigger accuracy, tokens · correctness only | harm and tokens decide whether the suite is worth installing |
| D28 | Go/no-go after Q0 | ★ go if skills-on wins on correctness or convention errors in at least 60 % of graded pairs and harm is not higher · owner judgement without a threshold | a threshold set before the data |

## E. Release and integration

| # | Decision | Options | Why |
|---|---|---|---|
| D29 | Router line in cosmoskill's hub | ★ during the pilot, as cosmoskill 1.0.4 · at 1.0 · never | avoids two answers early |
| D30 | Visibility and releases | ★ repository private (or unannounced) until 0.2 and Q0; 0.2 is a release; owner tags on GitHub · public now | nothing to show before 0.2 |
| D32 | Caches | ★ separate verify caches; maintainers may read cosmoskill's paper-HTML cache read-only · fully separate · shared | the paper cache is what made cosmoskill's dossiers cheap |
| D33 | Git flow | ★ as cosmoskill: commit to `main`, push, no tags from Claude · branches per stage | same owner, same tooling |
| D34 | Icon | ★ last, theory image in cosmoskill's ring style · now | not needed before release |
