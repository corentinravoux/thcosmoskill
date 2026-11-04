---
name: theoretical-cosmology
description: Use when reviewing, deriving, planning or fact-checking theoretical-cosmology content that spans several areas or whose area is not yet clear — inflation, primordial correlators, dark energy, modified gravity, dark-matter models, perturbation theory, early-universe physics — and for sign, unit and normalisation conventions, to find which thcosmo-* skill covers a topic, or to update the thcosmo-* skills from the recent literature.
---

# Theoretical cosmology working knowledge

## State of the suite
<!-- key: state-of-the-suite -->

Version 0.2.0 <!-- num: not a value -->: the hub and four domain skills are built,
`thcosmo-lss-perturbation-theory` (with six dossiers), `thcosmo-inflation`,
`thcosmo-primordial-correlators` and `thcosmo-modified-gravity`; the others are planned, in the order of `docs/plans/2026-10-30-plan-v2.md` of the package
repository. Until a domain is built, say that the suite holds no material on
it, answer from general knowledge only if the asker accepts that, label such
an answer as unsourced, and never present it as coming from the suite.

## Which skill holds what
<!-- key: which-skill-holds-what -->

This skill is the hub of a suite. Each domain below is, once built, its own
skill with dated results, provenance flags and a bibliography checked against
arXiv. For a question inside one domain, load that skill and follow its file
map; its content supersedes this hub.

| Topic | Skill | Status |
|---|---|---|
| SPT, LPT, EFTofLSS, IR resummation, bias expansion, redshift-space theory, consistency relations, primordial non-Gaussianity in LSS, velocity statistics and the momentum power spectrum, intrinsic alignments and shape bias, large-deviation and one-point statistics | `thcosmo-lss-perturbation-theory` | built (pilot, with six dossiers) |
| Inflationary dynamics and model landscape, slow roll, attractors, multi-field, reheating, initial conditions, eternal and stochastic inflation | `thcosmo-inflation` | built (first milestone) |
| Quantum fluctuations, in-in formalism, EFT of inflation, non-Gaussianity shapes, consistency relations, cosmological collider, bootstrap, features, loop corrections, decoherence, QFT in de Sitter and infrared effects | `thcosmo-primordial-correlators` | built (first milestone) |
| Scalar–tensor (Horndeski, beyond Horndeski, DHOST), f(R), vector–tensor, massive gravity, teleparallel and other theories, screening, consistency (ghosts, instabilities, positivity), EFT of dark energy, parameterised frameworks, speed of tensors | `thcosmo-modified-gravity` | built (first milestone) |
| Cosmological-constant problem, quintessence, k-essence, phantom crossing, interacting dark energy, early dark energy, dark-energy model building after DESI | `thcosmo-dark-energy` | built (W1) |
| Dark-matter production (freeze-out, freeze-in, misalignment, gravitational), candidates (WIMP, axion and ultralight, sterile neutrino, self-interacting, dark sectors), linear and non-linear signatures | `thcosmo-dark-matter-models` | built (W1) |
| Neutrino decoupling and N_eff in the Standard Model, massive-neutrino perturbations, dark radiation, interacting neutrinos | `thcosmo-neutrinos-light-relics` | built (W1) |
| Primordial tensors, stochastic backgrounds from inflation, phase transitions, defects and scalar-induced sources, gravitational-wave propagation in cosmology | `thcosmo-cosmological-gravitational-waves` | planned |
| Baryogenesis and leptogenesis, electroweak and QCD transitions, first-order phase transitions and bubble dynamics, primordial magnetogenesis | `thcosmo-baryogenesis-phase-transitions` | planned |
| Primordial black-hole formation and abundance, cosmic strings and other topological defects | `thcosmo-pbh-defects` | planned |
| FLRW backgrounds, Friedmann equations, distances and horizons, curvature; relativistic linear and second-order perturbations, gauges and gauge-invariant variables, ζ and R, separate universe and δN, Einstein–Boltzmann hierarchy, adiabatic and isocurvature initial conditions | `thcosmo-cosmological-perturbations` | planned |
| Equilibrium thermodynamics, Boltzmann equation in an expanding universe, freeze-out, BBN theory, recombination physics and codes, dark ages | `thcosmo-thermal-history` | planned |
| Acoustic physics, Thomson scattering, polarisation, damping, reionisation imprint, ISW, SZ and CMB-lensing theory, spectral distortions | `thcosmo-cmb-physics` | planned |
| Spherical and ellipsoidal collapse, excursion sets, mass-function theory, halo model, Vlasov–Poisson and N-body theory, wave dark-matter dynamics, baryonic effects on the matter power spectrum | `thcosmo-nonlinear-structure` | planned |
| Relativistic effects in observables, light propagation and the lensing formalism, backreaction and averaging, inhomogeneous exact solutions, numerical relativity and relativistic N-body | `thcosmo-relativistic-cosmology` | planned |
| String cosmology, moduli, de Sitter constructions, swampland conjectures, trans-Planckian questions, quantum cosmology, holography, alternatives to inflation (bounces, ekpyrosis, emergent) | `thcosmo-fundamental-theory` | planned |
| IGM thermal state, Lyα forest theory, 21 cm brightness temperature, reionisation modelling | `thcosmo-cosmic-dawn-igm` | planned |
| Theory codes: Boltzmann solvers and their forks, perturbation-theory codes, inflation solvers, phase-transition and BBN codes, relativistic and modified-gravity N-body (built only if the evaluation asks for it) | `thcosmo-theory-codes` | conditional |
| Theory responses to tensions and anomalies (H0, S8, DESI dark energy, neutrino mass, lensing amplitude): which models survive which data, by whom, and on what grounds | `thcosmo-tensions-model-building` | planned (last) |

Topics shared by several skills have one home; the others point to it. The
boundaries, and five rules for topics that fit two skills, are in
`docs/scopes-domains.md` of the package repository: a non-linear extension
lives with the non-linear method; a mechanism lives with its physics and
its signature with the observable; an interaction between two dark
components lives with the component whose equation of state changes; a
code question lives in `thcosmo-theory-codes` if it exists; a measured
value lives in the observational suite.
Observational results (measured values, survey facts, data systematics)
belong to the observational suite, cosmoskill (`cosmo-*` skills), when it is
installed; a theory skill quotes an observational bound only where a model's
status depends on it, with its source.

How the suite is built, checked and updated: `references/suite-conventions.md`.
Design documents and plans are in the `docs/` directory of the package
repository.

## Hub files
<!-- key: hub-files -->

- `references/conventions.md`: the conventions atlas: what to pin down in a
  theory text and, once built, who uses which choice and the sourced
  relations between choices.
- `references/methods-index.md`: where each method (in-in, EFT power
  counting, Boltzmann hierarchy, lattice, numerical relativity) is treated.
- `references/stale-claims.md`: statements still in circulation that a
  paper has corrected, and known errata in sources.
- `references/review-rubric.md`: how to review theory prose.
- `references/review-checklists.md`: checklists per family of domains.
- `references/suite-conventions.md`: file contract, provenance rules,
  checking and refreshing a domain.

In the lines below, `${CLAUDE_SKILL_DIR}` is the folder of this file; if it
reaches you unexpanded, write that folder's path in its place.

- `python3 "${CLAUDE_SKILL_DIR}"/scripts/verify_sources.py <skill directory>`: checks
  every cited arXiv identifier of a skill against arXiv.
- `python3 "${CLAUDE_SKILL_DIR}"/scripts/fetch_paper.py <arXiv id>`: reads a cited
  paper: `--abstract`, `--outline`, `--section <title>`, `--grep <text>`.
- `python3 "${CLAUDE_SKILL_DIR}"/scripts/layers.py <skill>`: prints a researcher's
  personal and project notes, papers and dossiers for a skill. To record
  something for the researcher, when asked: `layers.py note <skill>
  <file>#<key> <text>`, `layers.py source <skill> <arXiv id> --role <role>`,
  `layers.py dossier <skill> <name>`; add `--project` for one project only.

## Choosing the level
<!-- key: choosing-the-level -->

Every skill of the suite answers at four depths. Start at the lowest that
can answer, and go deeper only when it cannot.

| Level | Read | It holds |
|---|---|---|
| L1 | the domain's `SKILL.md`, nothing else | the headline equations and results, where the domain stands, the checks a referee makes, the errors that recur |
| L2 | one reference file, chosen from the file map | the formalism and its conventions, the model landscape, other results and their history, the validity of each approximation, open questions |
| L3 | a dossier of `deep/` | a derivation step by step, as the cited papers give it, and how to choose between methods or models |
| L4 | the cited paper, at the place the equation or number is given | the source itself |

- **The lowest level that answers.** An equation that is in the `SKILL.md`
  is an L1 answer. An L1 answer does not open a reference file "to be safe".
- **Levels stack.** L4 starts from the L2 entry, whose citation and flag say
  where to look: `[src: <place>]` was read in the paper at that place,
  `[sec: <place>]` came from a named secondary source, `[doc: <page>,
  <date>]` is a code fact read on an official page on that date, `[der]`
  marks reasoning in words and carries no number and no equation.
- **L4 is mandatory** before endorsing an equation or a number for a
  manuscript, a proposal or a referee report. Read the paper with
  `python3 "${CLAUDE_SKILL_DIR}"/scripts/fetch_paper.py <arXiv id>`. If the script
  cannot run, or reports that arXiv cannot be reached, do not run it again:
  read `https://arxiv.org/abs/<id>` or `https://arxiv.org/html/<id>` with a
  web tool if you have one. If the paper cannot be read, say that L4 was
  required and not done; never give its content from memory. A skill file is
  never the verification.
- **Deriving for the asker.** Carrying out a derivation or applying a
  formula to the asker's case is allowed; label every step that is not in a
  cited source as derived, and state the conventions used.
- **Which skill, when two fit.** A model's status against the data:
  `thcosmo-tensions-model-building` for the cross-probe picture, the model's
  own domain otherwise. A code question: `thcosmo-theory-codes`. A measured
  value: the observational suite.
- **State the level.** End the answer with the line each skill gives:
  `[thcosmoskill L<level> · <layer> · <skill>/<file>#<key>]`.

## How to use this in review
<!-- key: how-to-use-this-in-review -->

1. **Pin the conventions first.** Metric signature, curvature sign, units
   (reduced or full Planck mass), Fourier and power-spectrum normalisation,
   time variable, gauge. Silent convention drift between sections is the
   most common real error in a theory manuscript
   (`references/conventions.md`).
2. **Trace each equation to a source.** An equation stated without a source
   or a derivation is a finding; an equation transcribed from a paper with
   other conventions is checked term by term.
3. **Never invent results.** Coefficients, predictions, bounds and paper
   numbers come from a fetched source or the author. If unverified, say so.
4. **Separate the claim from the evidence.** "Ruled out", "favoured",
   "natural", "fine-tuned" need the dataset, the confidence level and the
   paper behind them, or they are opinion.

<!-- thcosmoskill:block:start — generated by tools/sync_blocks.py, do not edit by hand -->
## Levels and layers
<!-- key: levels-and-layers -->

Answer at the lowest level that answers the question, then stop.

| Level | Read | Holds |
|---|---|---|
| L1 | this file only | the headline equations and values, the state of the domain, the checks a referee makes, the errors that recur |
| L2 | one file of `references/` | what this file does not hold: the formalism and its conventions, the model landscape, other results and their history, the validity of each approximation, open questions |
| L3 | one dossier of `deep/` | none in this skill yet: say so and answer at L2 |
| L4 | the cited paper itself | what L1 to L3 quote; required before an equation or a number goes into a manuscript, a proposal or a referee report, and when two statements of the skills disagree |

Sizes, in thousands of tokens: L1 5k; conventions 12k; methods-index 2k; review-checklists 1k; review-rubric 1k; stale-claims 6k; suite-conventions 4k.

- L2: when the file map names several files, search them for the term
  before reading, and read only the passage.
- L4 starts from the L2 entry: its citation and flag say where to look. Read
  the paper with
  `python3 "${CLAUDE_SKILL_DIR}"/../*theoretical-cosmology/scripts/fetch_paper.py <arXiv id>`
  (`--abstract`, `--outline`, `--section`, `--grep`). `${CLAUDE_SKILL_DIR}` is
  the folder of this file; if it reaches you unexpanded, write that folder's
  path in its place. If the script cannot run, or reports that arXiv cannot
  be reached, do not run it again: read `https://arxiv.org/abs/<id>` or
  `https://arxiv.org/html/<id>` with a web tool if you have one. If the paper
  cannot be read, say that L4 was required and not done; never give its
  content from memory.
- Quote a number or an equation only with its paper and the place it was
  read (an equation with its equation number), or, for a code fact, its
  `[doc]` page and read date, as the skill gives them; the skill holds no
  number and no equation of its own making. State the conventions the
  equation assumes (metric signature, units, Fourier and normalisation
  conventions) when the skill gives them. A formula may be applied, or a
  derivation carried out, for the asker; label the result as derived.

Local layers: if a directory `.thcosmoskill/` exists in the working directory,
in one of its parents, or in the home directory, or if `THCOSMOSKILL_HOME` is
set, run
`python3 "${CLAUDE_SKILL_DIR}"/../*theoretical-cosmology/scripts/layers.py theoretical-cosmology`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. An
override replaces its base section for this researcher: use it, and quote
the base value beside it, both labelled. A suppressed section is left out
and named as suppressed; use it only when the question asks for that
section's own content, and then say that the layer hides it. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[thcosmoskill L<level> · <base, personal, project, or several joined by +> · theoretical-cosmology/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- thcosmoskill:block:end -->
