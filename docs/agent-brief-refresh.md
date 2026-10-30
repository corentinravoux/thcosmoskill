# Brief for a refresh run

You bring one domain skill of the thcosmoskill package up to date. The
skill and the date of the run are in your prompt. The procedure is
`plugin/skills/theoretical-cosmology/references/suite-conventions.md`,
"Refreshing a domain"; the rules of `docs/agent-brief.md` hold, sections 1
to 2b.

## Inputs

```bash
python3 tools/refresh_status.py --skill <skill> --due 90
python3 plugin/skills/theoretical-cosmology/scripts/verify_sources.py plugin/skills/<skill>
```

The first lists the files past their snapshot, the `[doc]` facts going
stale, and the **model cards whose status date is older than six months**.
The second warns when arXiv now holds a newer version of a cited paper.

## What to do

1. For each section of `results.md` and each model card of `models.md`: a
   date-sorted arXiv search from the snapshot date (or the card's status
   date) on, in `astro-ph.CO`, `hep-th`, `hep-ph`, `gr-qc` as the domain
   requires, and the papers citing the ones behind the headline results.
2. Read each new result at source. A model's status changes only with a
   paper read: write the new verdict, dataset, confidence level and paper,
   and set the **status date** to the date of the run. A status checked and
   unchanged also gets the new status date, with "checked, unchanged" in
   your progress file.
3. A newer version of a cited paper: re-read the places the skill gives;
   update the `version` column; correct a place or an equation that moved;
   record a corrected error in the hub's `references/stale-claims.md`.
4. Superseded results move to the history section of `results.md`, marked
   as superseded, never deleted.
5. Update `open-questions.md` and the `SKILL.md` bullets when a headline
   moved, and "Errors that recur" when a common statement became wrong.
6. Bump the snapshot date of every file touched.

## Budget

At most 60 research calls. Keep `references/_progress.md`; delete it at the
end.

## Before you finish

The checks of `docs/agent-brief.md`, section 4, plus
`python3 tools/check_shape.py --skill <skill>` and
`python3 tools/check_transcription.py --skill <skill>`. Do not commit.

Final message, under 200 words: results added and superseded, model
statuses changed, versions updated, the checkers' last lines.
