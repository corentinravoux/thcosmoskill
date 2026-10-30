# thcosmoskill — design

Date: 2026-10-30. Status: base built (version 0.1.0); amended the same day
by the owner's decisions after an independent review
(`docs/plans/2026-10-30-decisions.md`), which section 6 summarises. Plan:
`docs/plans/2026-10-30-plan-v2.md`.

## 1. Aim

A theoretical-cosmology skill package for Claude, useful to any researcher
in the field, built on the machinery of cosmoskill (observational
cosmology, version 1.0.3 at the time of writing): levels L1 to L4, personal
and project layers, every statement traced to the paper and the place it
was read, nothing written from model memory.

The reader is a researcher who derives, builds models, computes predictions
or referees theory papers, and who asks an assistant for the equation, the
convention, the model's status or the validity of an approximation. What
such a reader needs differs from what cosmoskill's reader needs, and the
design follows the difference.

## 2. What carries over from cosmoskill unchanged

- The plugin layout (`plugin/` with manifest, skills, licence; tools, tests,
  docs outside) and its tests against Anthropic's directory limits.
- The four levels, the generated "Levels and layers" block, section keys,
  retired keys, release manifests.
- The layer system (`layers.py`, `sync_layers.py`, `promote.py`) and its
  specification (`docs/layers.md`, `docs/layers-v1.md`).
- The provenance flags `[src]`, `[sec]`, `[doc]`, `[der]`, the
  not-a-value marker, `check_numbers.py` and its zero baseline.
- The bibliography checker against arXiv and the paper reader.
- The research discipline: subtopics from reviews, checkpoint after each
  subtopic, at most 90 research calls per domain build, no cap on sources,
  a second session gates each run, at most two research agents at once.

Lessons cosmoskill learned late are built in from the start: the numbers
rule (introduced there on 2026-10-23, after the content, and costing a
campaign over every file), the `[doc]` flag for code facts, strict YAML
front matter, the `plugin/` layout, and Claude-app script paths.

## 3. What changes, and why

### 3.1 Names

| Item | cosmoskill | thcosmoskill |
|---|---|---|
| hub | `observational-cosmology` | `theoretical-cosmology` |
| domains | `cosmo-*` | `thcosmo-*` |
| refine skill | `cosmoskill-refine` | `thcosmoskill-refine` |
| layer folder, variables | `.cosmoskill`, `COSMOSKILL_HOME`, `COSMOSKILL_BASE` | `.thcosmoskill`, `THCOSMOSKILL_HOME`, `THCOSMOSKILL_BASE` |
| cache | `~/.cache/cosmo-skill-verify` | `~/.cache/thcosmo-skill-verify` |
| block markers, answer line | `cosmoskill:block`, `[cosmoskill L…]` | `thcosmoskill:block`, `[thcosmoskill L…]` |

The two plugins install side by side without collision. The caches are
separate so that a change of format in one package cannot break the other
(decision D6 may merge them).

### 3.2 File contract

| cosmoskill | thcosmoskill | Why |
|---|---|---|
| `physics-and-methods.md` | `formalism.md` | a theorist's first need is the equation and its convention |
| `surveys-and-data.md` | `models.md` | the model landscape plays the role the survey landscape plays for observers |
| `results.md` | `results.md` | theorems, no-go results, computed predictions, bounds on models |
| `systematics.md` | `approximations.md` | the theory analogue of a systematic is an approximation used outside its range |
| `open-questions.md` | `open-questions.md` | unchanged |

`formalism.md` opens with a conventions block. The block in each SKILL.md
says L2 holds "the formalism and its conventions, the model landscape,
other results and their history, the validity of each approximation".

### 3.3 Equations are provenance-bearing statements

In cosmoskill the unit of trust is the number. Here it is also the
equation: a factor of two, a sign or a convention is where theory text goes
wrong, and where model memory is least reliable. Rules (suite conventions,
agent brief):

1. Every equation names its paper and equation number, in the same
   statement.
2. Equations are transcribed in the conventions of their source, which are
   named when they differ from the skill's stated conventions.
3. No conversion between conventions, no simplification, no combination of
   equations from two papers, no completion of a derivation, in the files.
   An answer may derive, labelled as derived.
4. Dossiers (L3) give derivations as the cited papers give them: a chain of
   steps, each pointing to the source's equations.

`check_numbers.py` already catches numbers inside equations; a new check
(plan, T2) requires a source and an equation number for every equation.

### 3.4 Model status is a claim with evidence

Theory files are full of verdicts: "excluded", "disfavoured", "natural",
"fine-tuned", "in the swampland". Each names its evidence: dataset,
confidence level, paper and date for an observational verdict; the paper
making a theoretical objection, and the reply where one exists. A
`constraint` role in `sources.tsv` marks data papers cited for a bound.

### 3.5 Source roles

Added to cosmoskill's roles: `textbook`, `lectures`, `model`, `constraint`.
Textbooks are cited by DOI; since the scripts cannot read them, an equation
taken from a textbook needs a second, readable source or goes under "Not
verified". A DOI check against Crossref is planned (T3), which adds one host
to the disclosure.

### 3.6 Mathematics in the files

LaTeX between single dollars for equations, Unicode allowed in prose. The
paper reader prints the LaTeX annotations of arXiv's HTML rendering, so an
equation in a skill file can be found in its source with `--grep` on a
symbol. `check_numbers.py` must not count structural digits (exponents,
indices, small integer coefficients written as single digits are already
exempt); calibration on the pilot is step T1.

### 3.7 Relation to cosmoskill

The two suites are independent packages. Each hub routes to the other when
installed: thcosmoskill's hub sends measured values to cosmoskill; a line in
cosmoskill's hub (decision D7, a change in that repository) would send
formalism and model questions here. Boundaries are in
`docs/scopes-domains.md`.

## 4. Non-goals

- Not a textbook or a course; the reader is a researcher.
- No symbolic-algebra engine in the plugin; scripts stay standard-library
  Python.
- No observational compilations; those belong to cosmoskill or to data
  packages.
- No content tailored to the owner's research in the base: the owner's
  depth goes in a personal layer, as in cosmoskill.

## 5. Open decisions for the owner

None open: see section 6.

## 6. Amendments of 2026-10-30 (decisions D1–D34)

- **Architecture (D1)**: topical domains plus three hub artefacts, the
  conventions atlas, the methods index and the stale-claims register;
  models in `models.md` as fixed-schema cards with a status date.
- **Domains (D2–D8)**: 19; `gr-background` folded into
  `cosmological-perturbations`; `relics` renamed `pbh-defects`, with
  magnetogenesis moved to `baryogenesis-phase-transitions`; `theory-codes`
  conditional; new homes for early dark energy, intrinsic alignments,
  large deviations, velocity statistics, baryonic effects, decoherence and
  QFT in de Sitter; five two-home rules.
- **Overlap with cosmoskill (D9, D29)**: formalism has its home here;
  cosmoskill's `cosmo-theory-foundations` keeps survey conventions and
  points here; router lines in both hubs during the pilot.
- **Provenance (D10–D18)**: an equation with its own equation number is
  sourced as a whole; verbatim up to a list of meaning-preserving
  normalisations; place format for unnumbered equations; arXiv version
  recorded; PDF reading by maintainers; textbooks through readable
  sources; errata in a register; conversions only as stated by a paper; no
  symbolic checks before 1.0. A transcription checker compares every
  equation with its source.
- **Gates and evaluation (D19–D28)**: a G2 draw of 59 tool-passed items
  with zero errors (error rate below 5 % at 95 %); dossiers zero to six
  from a gap audit; a blind test of 30 owner questions at milestone 0.2,
  graded by the owner alone, decides whether to continue.
