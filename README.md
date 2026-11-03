# thcosmoskill

**Theoretical-cosmology skills for Claude: they work in Claude Code and in
the Claude app (web, Desktop, Cowork), from this one repository.**

Ask Claude about a model, a derivation, a convention or a theoretical
result, and the skills give it the governing equations with the paper and
equation number that fix each one, the model landscape and the status of
each model, the range of validity of each approximation, and the statements
still in circulation that are out of date. When it matters, Claude reads the
paper again rather than trusting the skill.

**Status: release 0.2.0.** The hub and four domain skills are built:
LSS perturbation theory (with six dossiers), inflation, primordial
correlators and modified gravity; 301 sources checked against arXiv. The
other domains are planned: see [`docs/plans/2026-10-30-plan-v2.md`](docs/plans/2026-10-30-plan-v2.md)
(decisions: [`docs/plans/2026-10-30-decisions.md`](docs/plans/2026-10-30-decisions.md)).
Until a domain exists, the hub says that the suite holds no material on it.

The package is the theory companion of
[cosmoskill](https://github.com/corentinravoux/cosmoskill), the
observational-cosmology suite, and is built on the same machinery. The two
install side by side; their skill names do not collide.

## Install

### In the Claude app

Paid plan (Pro, Max, Team, Enterprise).

1. **Customize → Plugins → Add → Add marketplace → Add from a repository**.
2. Enter `corentinravoux/thcosmoskill`, then install **thcosmoskill**.
3. Turn on code execution, which skills need: **Settings → Capabilities →
   Create and edit files**.
4. To let Claude read the cited papers (level 4, below), turn on **web search**
   in the chat.

### In Claude Code

```
/plugin marketplace add corentinravoux/thcosmoskill
/plugin install thcosmoskill@thcosmoskill
```

Update with `claude plugin update thcosmoskill@thcosmoskill`.

<details>
<summary>Without the plugin system: link the skills</summary>

```bash
git clone https://github.com/corentinravoux/thcosmoskill
for d in thcosmoskill/plugin/skills/*/; do
    ln -s "$(realpath "$d")" ~/.claude/skills/"$(basename "$d")"
done
```

Update with `git pull`.
</details>

### In other agents

The skills follow the open [Agent Skills](https://agentskills.io) format:

```
npx skills add corentinravoux/thcosmoskill --skill '*'
```

Install all of them: every domain skill calls the hub's scripts in
`theoretical-cosmology`.

### What it runs and contacts

The skills are text; the scripts run only when Claude calls them, use the
Python standard library only, and send arXiv identifiers to arXiv, nothing
else. The hosts and cache paths are listed in
[`plugin/README.md`](plugin/README.md#what-it-runs-and-contacts).

## How it answers

Claude answers at the shallowest level that answers the question, and says
which one it used:

| Level | Claude reads | Enough for |
|---|---|---|
| L1 | the skill's `SKILL.md` | where a domain stands, the headline equations and results, what to watch for |
| L2 | one reference file | the formalism and its conventions, a model, a result and its history, the validity of an approximation |
| L3 | a dossier in `deep/` | a derivation step by step as the sources give it, how to choose a method or a model |
| L4 | the cited paper | an equation or a number about to go into a manuscript, a proposal or a referee report |

Each answer ends with a line such as
`[thcosmoskill L2 · base · thcosmo-inflation/models#plateau-models]`.

## What is grounded

- **Every equation and every number carries its source**: `[src: Eq. 2.14]`
  when read in the cited paper, `[sec: …]` when read in a named secondary
  source, `[doc: page, date]` for a code fact. Equations are transcribed in
  the conventions of their source, which are named; the files hold no
  derivation of the model's own making.
- **Every citation is checked** against arXiv (`verify_sources.py`).
- **A model's status names its evidence**: dataset, confidence level and
  paper for "excluded"; the paper making the objection, and the reply, for
  a theoretical problem.
- **Each file lists what could not be verified**, under "Not verified".

## Domains

In build order (plan v2): the pilot, the three domains of milestone 0.2
(built), then the rest (planned).

| Skill | Covers |
|---|---|
| `theoretical-cosmology` | hub: routes to the others; conventions atlas; methods index; stale-claims register (built; methods index and stale claims in first versions) |
| `thcosmo-lss-perturbation-theory` | SPT, LPT, EFTofLSS, bias, redshift space, velocity statistics, intrinsic alignments, large deviations (pilot: built, six dossiers) |
| `thcosmo-inflation` | inflationary dynamics and models, reheating, stochastic and eternal inflation (0.2: built) |
| `thcosmo-primordial-correlators` | in-in, EFT of inflation, non-Gaussianity, collider, bootstrap, decoherence, QFT in de Sitter (0.2: built) |
| `thcosmo-modified-gravity` | Horndeski and beyond, f(R), massive gravity, screening, EFT of dark energy (0.2: built) |
| `thcosmo-dark-energy` | Λ problem, quintessence, phantom crossing, interacting and early dark energy |
| `thcosmo-dark-matter-models` | production mechanisms, candidates, signatures |
| `thcosmo-neutrinos-light-relics` | N_eff, massive neutrinos, dark radiation |
| `thcosmo-cosmological-gravitational-waves` | primordial tensors, stochastic backgrounds, propagation |
| `thcosmo-baryogenesis-phase-transitions` | baryogenesis, leptogenesis, phase transitions, magnetogenesis |
| `thcosmo-pbh-defects` | primordial black holes, cosmic strings and other defects |
| `thcosmo-cosmological-perturbations` | FLRW background, relativistic perturbations, gauges, ζ, δN, Einstein–Boltzmann hierarchy |
| `thcosmo-thermal-history` | thermodynamics, freeze-out, BBN theory, recombination |
| `thcosmo-cmb-physics` | acoustic physics, polarisation, secondary anisotropies, spectral distortions |
| `thcosmo-nonlinear-structure` | collapse, mass function, halo model, Vlasov–Poisson, baryonic effects |
| `thcosmo-relativistic-cosmology` | relativistic observables, lensing formalism, backreaction, numerical relativity |
| `thcosmo-fundamental-theory` | string cosmology, de Sitter, swampland, quantum cosmology, alternatives to inflation |
| `thcosmo-cosmic-dawn-igm` | IGM, Lyα forest theory, 21 cm, reionisation modelling |
| `thcosmo-theory-codes` | Boltzmann codes and forks, PT codes, solvers (built only if the evaluation asks for it) |
| `thcosmo-tensions-model-building` | theory responses to H0, S8, DESI dark energy and other anomalies (last) |

Each domain skill will have the same shape: a `SKILL.md`, five reference
files (`formalism`, `models` with one card per model, `results`,
`approximations`, `open-questions`), a bibliography `sources.tsv` with the
arXiv version read, a subtopic list `subtopics.tsv`, and up to six dossiers
in `deep/`.

## Your own layer (Claude Code)

Add your own notes, papers, dossiers, or a different version of one section,
without editing the package. They live in `~/.thcosmoskill/` (personal) or
`.thcosmoskill/` in a project, and the skills say when an answer uses them.
In a conversation, just ask ("note, for my work, that …", "add this paper to
my layer"); the `thcosmoskill-refine` skill runs the commands. Format:
`docs/layers.md`; specification: `docs/layers-v1.md`.

## Maintaining

Build and refresh domains never from memory: the procedure is in
`plugin/skills/theoretical-cosmology/references/suite-conventions.md` and the
research brief in `docs/agent-brief.md`. After editing:

```bash
python3 tools/assign_keys.py && python3 tools/sync_blocks.py
python3 plugin/skills/theoretical-cosmology/scripts/verify_sources.py plugin/skills/thcosmo-<domain>
python3 tools/check_numbers.py --skill thcosmo-<domain> --list   # must print nothing
python3 -m pytest -q
```

Contributions follow `CONTRIBUTING.md`. Scripts need Python 3.9+ and the
standard library only.

## Repository layout

The plugin is in `plugin/` (manifest, skills, licence); the rest of the
repository (docs, tests, tools, release manifests) is for maintainers.

## Licence

MIT, for the text and for the scripts. See `LICENSE`.
