# Contributing to thcosmoskill

thcosmoskill is a reference for an assistant helping researchers in
theoretical cosmology. What makes it useful is that every equation and every
statement can be traced to its source. A contribution is welcome when it
keeps that true. This file lists the rules a change must pass; the tests
check most of them.

## Before you start

- To add to the package for your own work only, use a layer instead
  (`docs/layers.md`): notes, overrides and your own dossiers live in
  `~/.thcosmoskill/` and never need a pull request. An entry that would
  serve others can be promoted later
  (`plugin/skills/theoretical-cosmology/scripts/promote.py`).
- For a change to the package, open an issue first when it adds a domain,
  a dossier or a new kind of file.

## The rules

1. **Nothing from memory.** Every statement you add was read at its source
   while you wrote it.
2. **Every equation and every number names its source and the place read.**
   - From a paper: the `arXiv:` or `doi:` identifier, and the place in a
     flag, `[src: Eq. 2.14]`, `[src: Sect. 4.2]`, `[src: Table 3]`,
     `[src: abstract]`. `[sec: <place>]` when it was taken from another
     paper, named with its identifier.
   - A code fact (version, release date, default setting):
     `[doc: <URL, repository path or installed package and version>,
     <YYYY-MM-DD read>]`. It goes stale two years after its read date.
   - An equation is transcribed in the conventions of its source, which are
     named when they differ from the skill's. No conversion between
     conventions and no derivation of your own in the files; reasoning in
     words is flagged `[der]` and carries no number and no equation.
   - A statement whose numbers are not values (notation, names, pointers)
     carries `<!-- num: not a value -->`.
3. **A model's status names its evidence**: dataset, confidence level and
   paper for an observational verdict; the paper making a theoretical
   objection, and the reply where one exists.
4. **Every identifier you cite has one row in the skill's
   `references/sources.tsv`, and every row is cited.**
5. **Superseded results are kept** in the history section of `results.md`,
   marked as superseded, not deleted.
6. **Forecasts are labelled as forecasts.**
7. **Section keys.** Never write, rename or remove a `<!-- key: ... -->`
   line by hand; `tools/assign_keys.py` adds keys for new sections. A
   section you remove goes to `references/retired-keys.tsv`.
8. **Generality.** The package follows the field's own weights: a subject
   is not built around one group, school, code or model, including yours.
9. **Plain technical English**, complete sentences.

The file layout and flags are in
`plugin/skills/theoretical-cosmology/references/suite-conventions.md`; the
brief that the package's own research runs follow is `docs/agent-brief.md`,
with `docs/agent-brief-numbers.md` for numbers and equations.

## Checks to run

From the repository root, before opening a pull request:

```bash
python3 tools/assign_keys.py
python3 tools/sync_blocks.py
python3 plugin/skills/theoretical-cosmology/scripts/verify_sources.py plugin/skills/<skill>
python3 tools/check_keys.py --against <last release tag>
python3 tools/check_numbers.py --skill <skill> --list
python3 tools/check_equations.py --skill <skill> --list
python3 tools/check_transcription.py --skill <skill>
python3 tools/check_places.py --skill <skill>
python3 tools/check_shape.py --skill <skill>
python3 -m unittest discover -s tests
```

`check_numbers.py --list` and `check_equations.py --list` must print
nothing; `check_transcription.py` must report no mismatch. The gate run by
the maintainers adds a re-read of a sample in the papers
(`tools/sample_statements.py`) and a generality check
(`tools/word_share.py`).

## Licence

Contributions are accepted under the MIT licence of the package (`LICENSE`).
