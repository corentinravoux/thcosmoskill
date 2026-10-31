# Suite conventions — how the thcosmo-* skills are built and kept current

Scope: the rules every `thcosmo-<domain>` skill follows, how to check one, and
how to refresh one. The design documents are in the `docs/` directory of the
package repository.

Snapshot: 2026-10-30 (rules of plan v2)

## File contract
<!-- key: file-contract -->

```
thcosmo-<domain>/
├── SKILL.md                         triggers, file map, core facts, checklists
├── references/
│   ├── formalism.md                 definitions, governing equations, conventions, each with the paper and equation that fix it
│   ├── models.md                    one model card per model: defining equations, parameters, predictions, consistency, status, status date
│   ├── results.md                   dated key results: theorems, no-go results, Standard-Model computed values, bounds on models
│   ├── approximations.md            approximations and their range of validity, theoretical errors, numerical issues, traps
│   ├── open-questions.md            debates with both sides, what next data or calculations will decide
│   ├── sources.tsv                  key, id, version, first_author, year, title, role
│   └── subtopics.tsv                key, title, from, files, status
└── deep/                            zero to six dossiers, where a gap audit shows L2 cannot answer
```

These five reference files are standard. A skill may add topical files; its
file map lists them. A prediction of one model goes in `models.md`; a result
that holds independently of the model (a theorem, a no-go result, a
Standard-Model computed value) goes in `results.md`.

### Model cards
<!-- key: model-cards -->

Each model in `models.md` is a card with these fields, in this order:

```markdown
### <Model name>
- **Defining equations:** $...$ [src: Eq. n] (arXiv:...)
- **Parameters:** ...
- **Predictions:** ... [src: ...]
- **Consistency:** <claim> (arXiv:..., place); reply: <claim> (arXiv:..., place) or "none found"
- **Observational status:** <verdict>, <dataset>, <confidence level> (arXiv:..., place)
- **Status date:** YYYY-MM-DD
```

A status date older than six months is listed by `tools/refresh_status.py`. Load `SKILL.md` first: it says which reference answers
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
  cited paper writes it, in that paper's conventions, named next to it when
  they differ from the skill's. Transcription is exact up to the
  meaning-preserving normalisations listed in `tools/latex_norm.py`
  (spacing commands such as `\hskip`, `\displaystyle`, brace style,
  `{\bf x}` for `\mathbf{x}`). An equation that carries its own
  `[src: Eq. n]` is sourced as a whole, coefficients included.
- **Example**: the second-order density kernel in an Einstein–de Sitter
  universe, $F_{2}({\bf q}_{1},{\bf q}_{2})=\frac{5}{7}+\frac{1}{2}\frac{{\bf q}_{1}\cdot{\bf q}_{2}}{q_{1}q_{2}}(\frac{q_{1}}{q_{2}}+\frac{q_{2}}{q_{1}})+\frac{2}{7}\frac{({\bf q}_{1}\cdot{\bf q}_{2})^{2}}{q_{1}^{2}q_{2}^{2}}$
  (Bernardeau et al. 2002, arXiv:astro-ph/0112551) [src: Eq. 45].
- **Places other than a numbered display** (hep-th probe, 2026-10-31):
  - an unnumbered display: `[src: Sect. 3.2, unnumbered display after
    Eq. 12]`;
  - an equation in the text: `[src: Sect. 3.2, inline, text after Eq. 12]`
    (the checker searches the inline mathematics after that display);
  - a paper without sections (a letter): `[src: text after Eq. 3]`,
    `[src: footnote 2]`;
  - a table or a footnote inside a table: `[src: Table 1.3]`,
    `[src: Table 1.3, footnote 6]`.
  A person re-reads at the gate every equation the checker cannot match.
- **A display of several rows or cells** is copied whole, rows and cells
  joined in reading order, in one `$…$`, or as consecutive `$…$` spans in
  one statement; never one row's left side with another row's right side.
- **A parameter set to a value** (`$s=0$`, `$d=1$`) is notation, not an
  equation; **a measured value with its error** (`$x=0.9\pm0.1$`) is a
  number, sourced like any number.
- **One statement, several papers**: each equation is attributed to the
  paper cited nearest after it; put each paper's citation and flag right
  after the equations taken from it (in a model card, one sub-item per
  paper if needed).
- **Versions**: `sources.tsv` records the arXiv version read (`v2`); places
  refer to that version. `verify_sources.py` warns when arXiv holds a newer
  one.
- **Papers without an HTML rendering, or with a rendering that carries no
  equation numbers** (`fetch_paper.py` says "none tagged", as for many
  plain-TeX papers of 1995–2005): copy the equation from a readable source
  that reproduces it with a number, flagged `[sec: <place>]`, and log the
  primary paper; a maintainer may read the PDF and write
  `[src: Eq. 12 (PDF v2)]`.
- **Textbooks and papers older than arXiv**: content found only there
  needs a readable source that cites it, flagged `[sec: <place>]`;
  otherwise it goes under "Not verified". A `doi:` row is written only when
  a tool returned the DOI (for example the INSPIRE reference list).
- **Errata and slips**: when a later version or an erratum corrects a
  source, cite the corrected version and record the slip in the hub's
  `references/stale-claims.md`. An apparent slip with no published
  correction (a missing square, a mismatched index) is copied as printed,
  described in words in the same statement ("as printed; the text below
  Eq. 4.1 sets …"), never corrected in an equation, and recorded in
  `stale-claims.md` with "none published".
- **Versions**: `fetch_paper.py --abstract` prints the latest arXiv
  version; the header of `--grep`, `--section` and `--outline` prints the
  version the rendering was built from. Record the version read.
- **`[der]`** covers its own sentence only.
- **Conversions between conventions**: only relations a paper states,
  flagged `[src]` and collected in the hub's conventions atlas; no
  conversion by an agent in the files.
- **Tables**: no `|` inside `$…$` in a table row; write `\lvert…\rvert`
  and `\vert`.
- A number or an equation without its paper and place, one computed by an
  agent, or a claim with no citation, is a defect in the file: fix the file,
  do not quote it. `tools/check_numbers.py` lists numbers without source.
- A model's status ("viable", "excluded", "disfavoured") names the dataset,
  the confidence level and the paper, and carries a status date; a
  theoretical objection (ghost, instability, swampland, fine-tuning) names
  the paper that makes it, and the reply where one exists.
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
python3 tools/check_numbers.py --skill thcosmo-<domain> --list
python3 tools/check_equations.py --skill thcosmo-<domain> --list
python3 tools/check_transcription.py --skill thcosmo-<domain>
```

The checker asks arXiv for every cited paper (existence, title, first
author) and reports citations without a bibliography row and rows without a
citation. `--offline` runs the local checks only. Exit status 0 means clean.
Papers found once are cached under the user's cache directory.

`check_transcription.py` compares each transcribed equation with the
equation of that number in the source. Whether a number is the one the
paper gives, and whether an equation means what the file says, is checked
by reading the paper:

```bash
python3 plugin/skills/theoretical-cosmology/scripts/fetch_paper.py astro-ph/0112551 --abstract
python3 plugin/skills/theoretical-cosmology/scripts/fetch_paper.py astro-ph/0112551 --outline
python3 plugin/skills/theoretical-cosmology/scripts/fetch_paper.py astro-ph/0112551 --grep "(45)" --context 1
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
   - `models.md`: a model whose status changed (new status date), a new
     model that the literature takes up.
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
