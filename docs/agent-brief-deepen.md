# Brief for a deepening run

You deepen one domain skill of the thcosmoskill package where a gate, the
gap audit or the blind test (Q0) found it thin. The skill, the subtopics
or questions that failed, and the date of the run are in your prompt. The
rules of `docs/agent-brief.md` hold in full.

## What to do

1. Read the failed questions and the sections of the reference files that
   should have answered them (`subtopics.tsv` names the files).
2. Decide where the missing content belongs: a reference file (a
   definition, an equation, a model card, a result, an approximation, an
   open question) or a dossier (a derivation or a choice of method: then
   stop and report, since dossiers have their own brief).
3. Research and write it in place, with the same rules as a build: subtopic
   sources by rule (foundation, review or lectures, latest result,
   critique), equations transcribed with their numbers, model cards
   complete with their status date.
4. Set the subtopic's status in `subtopics.tsv` (`covered` or `thin`).

Do not rewrite sections that are not part of the gap. Do not remove a
verified statement to make room.

## Budget

At most 45 research calls. Keep `references/_progress.md`; delete it at the
end.

## Before you finish

The checks of `docs/agent-brief.md`, section 4, plus
`python3 tools/check_shape.py --skill <skill>` and
`python3 tools/check_transcription.py --skill <skill>`. Do not commit.

Final message, under 200 words: what was added where, the questions it now
answers, what is left for a dossier, the checkers' last lines.
