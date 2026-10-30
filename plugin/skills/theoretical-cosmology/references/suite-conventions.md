# Suite conventions — how the thcosmo-* skills are built and kept current

Scope: the rules every `thcosmo-<domain>` skill follows, how to check one, and
how to refresh one. The design documents are in the `docs/` directory of the
package repository.

Snapshot: 2026-10-30

## File contract
<!-- key: file-contract -->

```
thcosmo-<domain>/
├── SKILL.md                         triggers, file map, core facts, checklists
├── references/
│   ├── formalism.md                 definitions, governing equations, conventions, each with the paper and equation that fix it
│   ├── models.md                    model landscape: action or defining equations, parameters, predictions, consistency, status
│   ├── results.md                   dated key results: theorems, no-go results, computed predictions, bounds on models
│   ├── approximations.md            approximations and their range of validity, theoretical errors, numerical issues, traps
│   ├── open-questions.md            debates with both sides, what next data or calculations will decide
│   ├── sources.tsv                  key, id, first_author, year, title, role
│   └── subtopics.tsv                key, title, from, files, status
└── deep/                            six dossiers: derivations and method choices
```

These five reference files are standard. A skill may add topical files; its
file map lists them. Load `SKILL.md` first: it says which reference answers
which question. Load one reference at a time.

## Citations and provenance
<!-- key: citations-and-provenance -->

- Prose cites `arXiv:<id>` or `doi:<doi>`. Every cited identifier has one row
  in `sources.tsv`, and every row is cited.
- Only numbers and equations read in a paper are given. Every number and
  every equation names its paper (`arXiv:` or `doi:`) and the place it was
  read, in a flag:

  | flag | meaning | use in a manuscript |
  |---|---|---|
  | `[src: <place>]` | read in the cited paper itself at that place (equation, section, table, figure, appendix, footnote or abstract) when the file was written | re-read the paper, then quote |
  | `[sec: <place>]` | taken from a named secondary source at that place | go to the primary paper first |
  | `[doc: <source>, <date>]` | a code fact (version, release date, default setting) read on that date at a URL, a repository path or an installed package; not a paper; stale two years after the read date | re-read the page; quote with its date |
  | `[der]` | reasoning in words drawn from cited results; carries no number and no equation | do not quote as a result |

  A statement whose numbers are not values (notation, names, pointers)
  carries `<!-- num: not a value -->`.

- **Equations are transcribed, not derived.** An equation is written as the
  cited paper writes it, in that paper's conventions, which are named next
  to it when they differ from the skill's stated conventions. Converting an
  equation to other conventions, or completing a derivation, is not done in
  the files; it is done in an answer, labelled as derived.
- A number or an equation without its paper and place, one computed by an
  agent, or a claim with no citation, is a defect in the file: fix the file,
  do not quote it. `tools/check_numbers.py` lists numbers without source.
- A model's status ("viable", "excluded", "disfavoured") names the dataset,
  the confidence level and the paper; a theoretical objection (ghost,
  instability, swampland, fine-tuning) names the paper that makes it, and the
  reply where one exists.
- Forecasts are labelled as forecasts and never share a table with
  measurements without a column that says which is which.
- Each `results.md` and `models.md` starts with a snapshot date.

## Checking a skill
<!-- key: checking-a-skill -->

From the repository root, which is three levels above the hub skill's
directory (the skills are in `plugin/skills/`):

```bash
python3 plugin/skills/theoretical-cosmology/scripts/verify_sources.py plugin/skills/thcosmo-<domain>
python3 plugin/skills/theoretical-cosmology/scripts/verify_sources.py --offline plugin/skills/*/
```

The checker asks arXiv for every cited paper (existence, title, first
author) and reports citations without a bibliography row and rows without a
citation. `--offline` runs the local checks only. Exit status 0 means clean.
Papers found once are cached under the user's cache directory.

It does not check that an equation or a number is the one the paper gives.
That is done by reading the paper, when it is needed:

```bash
python3 plugin/skills/theoretical-cosmology/scripts/fetch_paper.py 0907.5424 --abstract
python3 plugin/skills/theoretical-cosmology/scripts/fetch_paper.py 0907.5424 --outline
python3 plugin/skills/theoretical-cosmology/scripts/fetch_paper.py 0907.5424 --grep "slow-roll" --context 1
```

## Refreshing a domain
<!-- key: refreshing-a-domain -->

A skill is as current as its snapshot date. The update cycle below is run
every few months, one domain at a time, for the reference files and for the
dossiers under `deep/`, each of which carries its own snapshot date.

1. **Read the snapshot date** at the top of the domain's `results.md`.
   `python3 tools/refresh_status.py --due <days>` lists, per skill, the
   files older than that many days and the `[doc]` facts that go stale.
2. **Find what appeared since.** For each section of `results.md` and
   `models.md`, a date-sorted arXiv search from the snapshot date on
   (`astro-ph.CO`, `hep-th`, `hep-ph`, `gr-qc`), and what cites the papers
   behind the headline results.
3. **Read each new result at source**: the abstract, and the section or
   equation that holds it. Nothing is written from memory.
4. **Edit the files.**
   - `results.md`: add the row; move the result it replaces to the history
     section, marked as superseded, instead of deleting it.
   - `models.md`: a model whose status changed, a new model that the
     literature takes up.
   - `open-questions.md`: a debate that moved, a claim that became stale.
   - `SKILL.md`: the "What an expert holds in mind" bullets when a headline
     moved, and "Errors that recur" when a common statement became wrong.
   - `sources.tsv`: one row per new paper cited.
5. **Bump the snapshot date** in every file touched.
6. **Keys.** A new section needs a key; an existing key is never renamed.
   A section that is removed is recorded in `references/retired-keys.tsv`,
   because a researcher's notes may be attached to it.
7. **Run the upkeep tools**, from the repository root:

   ```bash
   python3 tools/assign_keys.py                 # keys for new sections
   python3 tools/sync_blocks.py                 # level block and sizes of each SKILL.md
   python3 plugin/skills/theoretical-cosmology/scripts/verify_sources.py plugin/skills/thcosmo-<domain>
   python3 tools/check_keys.py --against <last release tag or commit>
   python3 -m unittest discover -s tests
   ```

8. **After the domains, the synthesis**: `thcosmo-tensions-model-building`
   is updated last, from the other skills.
9. **Record what moved** in the commit message.

A researcher with local layers then runs
`python3 plugin/skills/theoretical-cosmology/scripts/layers.py check`, which lists
notes attached to a section the update retired.

## Adding a domain
<!-- key: adding-a-domain -->

Copy the shape of an existing `thcosmo-*` skill, follow `docs/agent-brief.md`
of the package repository, set the skill's row in the router table of the
hub `SKILL.md` to built, and run the upkeep tools of the update cycle.

## What the suite does not hold
<!-- key: what-the-suite-does-not-hold -->

Discussion, tables for reading, transcribed equations and links to sources.
It is not a database of verified equations: an equation needed for a
manuscript is read again in the linked paper. Measured values and survey
facts belong to the observational suite.
