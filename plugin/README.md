# thcosmoskill

Theoretical-cosmology skills for Claude Code and the Claude app: one hub
skill (`theoretical-cosmology`), domain skills (`thcosmo-*`), and a skill to
refine them with your own layer (`thcosmoskill-refine`).

Ask Claude about a model, a derivation, a convention or a theoretical
result, and the skills give it the governing equations with the paper and
equation number that fix each one, the model landscape, the range of
validity of each approximation, and which statements in circulation are out
of date. Base release 0.1.0: the domain skills are planned, not yet built.

## How it answers

| Level | Claude reads | Enough for |
|---|---|---|
| L1 | the skill's `SKILL.md` | where a domain stands, the headline equations and results |
| L2 | one reference file | the formalism, a model, a result, an approximation |
| L3 | a dossier in `deep/` | a derivation as the sources give it, a choice of method |
| L4 | the cited paper | an equation or a number about to go into a manuscript |

## Install

In the Claude app (paid plan): **Customize → Plugins → Add → Add marketplace →
Add from a repository**, enter `corentinravoux/thcosmoskill`, install
**thcosmoskill**, and turn on **Settings → Capabilities → Create and edit
files**. Turn on web search in a chat to let Claude read the cited papers.

In Claude Code:

```
/plugin marketplace add corentinravoux/thcosmoskill
/plugin install thcosmoskill@thcosmoskill
```

## What each host can do

| | Claude Code | Claude app |
|---|---|---|
| Skills, reference files, dossiers (levels 1–3) | yes | yes |
| Read the cited paper (level 4) | yes, with `fetch_paper.py` | with web search on; or `fetch_paper.py` if `arxiv.org`, `export.arxiv.org` and `ar5iv.labs.arxiv.org` are allowed domains |
| Personal and project layers, `thcosmoskill-refine` | yes | no: the app starts each chat with an empty disk |

## What it runs and contacts

The skills are text. The scripts in the hub skill's `theoretical-cosmology/scripts/`
(Python standard library only, readable source, nothing downloaded at install)
run only when Claude calls them:

- `fetch_paper.py` downloads a cited paper's abstract or text from
  `export.arxiv.org`, `arxiv.org` and `ar5iv.labs.arxiv.org`, and caches it
  in `~/.cache/thcosmo-skill-verify/papers/`.
- `verify_sources.py` asks `export.arxiv.org` for the title and first author
  of arXiv identifiers, cached in `~/.cache/thcosmo-skill-verify/arxiv.json`;
  `--offline` contacts nothing.
- `layers.py`, `sync_layers.py` and `promote.py` read and write layer files in
  `~/.thcosmoskill/` (or `$THCOSMOSKILL_HOME`) and `.thcosmoskill/`; adding a
  paper to a layer asks `export.arxiv.org` for its title and author.

Only arXiv identifiers are sent. No personal data, credentials or usage data
leave the machine.

## More

Domains, plan, layers and maintenance: the repository,
https://github.com/corentinravoux/thcosmoskill. Licence: MIT (`LICENSE`).
