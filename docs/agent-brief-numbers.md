# Brief for a fix run (numbers, equations, places)

You repair one skill of the thcosmoskill package after a gate found
defects. The skill and the report to work from are in your prompt: the
output of `check_numbers.py --list`, `check_equations.py --list`,
`check_transcription.py`, `check_places.py`, or a G2 sheet with `wrong`
verdicts. The rules of `docs/agent-brief.md` hold, sections 1 to 2b.

## What to do, per item

| Report says | Do |
|---|---|
| `none`, `no-paper` (a number or an equation without source) | find the paper that states it and the place, read it there, and add the identifier and flag; if no paper states it, remove it |
| `no-place` | read the cited paper and add the place: `[src: Eq. 45]`, `[src: Sect. 5.2]`, `[src: Table 3]`, `[src: abstract]` |
| `no-eq` (an equation with a section place) | find the equation number in that section and give it; if the display is unnumbered, write `[src: Sect. 3.2, unnumbered display after Eq. 12]` |
| `table-pipe` | write `\lvert…\rvert` or `\vert` instead of `|` inside `$…$` |
| transcription `mismatch` | read the equation in the paper (`fetch_paper.py <id> --grep "(n)"`) and copy it as printed; if the file named the wrong number, correct the number; if the source has an erratum or a later corrected version, cite the corrected one and record the slip in the hub's `references/stale-claims.md` |
| transcription `contained` | check that the part transcribed is what the file says it is (one side, one line); say so in the text if it is not obvious |
| places `found-elsewhere` | correct the place to where the number is |
| places `not-found` | re-read: correct the number, or the paper, or remove the statement |
| G2 `wrong` | correct it, then look for the same error pattern across the whole skill and correct every instance; list them in your final message |
| `derived` (a `[der]` flag with a number or an equation) | replace the number or equation by one a paper states, or remove it |
| a statement whose numbers are names (`$\ell=2$` as a label) | mark it `<!-- num: not a value -->`, or `<!-- eq: notation -->` for a math span that only defines a symbol |

Never compute, convert or rescale a number or an equation yourself. Write
small counts the package makes of itself in words ("six dossiers").

## Budget

At most 60 research calls. Keep `references/_progress.md` with the items
done; delete it at the end.

## Before you finish

```bash
python3 tools/check_numbers.py --skill <skill> --list          # nothing
python3 tools/check_equations.py --skill <skill> --list        # nothing
python3 tools/check_transcription.py --skill <skill>           # no mismatch
python3 tools/check_places.py --skill <skill>
python3 plugin/skills/theoretical-cosmology/scripts/verify_sources.py plugin/skills/<skill>
python3 -m unittest discover -s tests
```

Do not commit. Final message, under 200 words: items fixed by kind, items
removed, error patterns found across the skill, the checkers' last lines.
