# Gap audit — thcosmo-cosmological-gravitational-waves

Plan v2, section 3, step 4. Written by the coordinator on 2026-11-10 from
`references/subtopics.tsv` and the reference files (section sizes measured
in characters). Two subtopics are marked thin (radiation bound, preheating):
they go to a deepening run (`docs/agent-brief-deepen.md`), not to a dossier.

Generality check at G1 (`tools/word_share.py`): Caprini as first author
holds 47.1 % of 323 citations (152). Most come from the review of Caprini &
Figueroa (arXiv:1801.04268), which is the only source of the formalism
sections on the tensor equation, the stochastic background, preheating and
most of the irreducible inflationary background and of the defects
(5/5, 8/8, 5/5, 11/14 and 7/14 arXiv citations of those sections). The
three dossiers below and the deepening run draw from primary papers and
later reviews; the share is measured again at G3.

| # | Question | L2 verdict | Dossier |
|---|---|---|---|
| 1 | How are the gravitational-wave spectra of a first-order phase transition derived: sound-shell model against lattice fits, the suppression for short-lived sound waves, the turbulence part, and what changed between the LISA templates of arXiv:1910.13125 and arXiv:2403.03723? | partly: formalism ≈7.3k, approximations ≈2.5k and the two model cards give the templates and their inputs; the sound-shell model and the source-lifetime factor are stated, not derived; turbulence is an open calculation (≈0.4k) | `phase-transition-spectra` |
| 2 | How is the spectrum of a cosmic-string network computed: loop number density (one-scale, VOS, simulations), emission per loop (cusps, kinks, harmonics), Nambu–Goto against field-theory loops, and how do the fits to the PTA signal depend on these choices? | partly: formalism ≈4.4k (7 of 14 citations from arXiv:1801.04268), model card ≈2.1k, open question ≈0.7k; the loop distributions are named, not given; the scaling-network emission of Sect. 9.1 under "Not verified" | `cosmic-string-spectra` |
| 3 | How is the scalar-induced kernel derived, for which equations of state and at which order; how do non-Gaussian curvature and the gauge choice change the spectrum; what is the infrared tail? | partly: formalism ≈3.6k from Domènech (arXiv:2109.01398), approximations ≈1.6k, open question ≈0.6k; the kernel is quoted, its derivation and the non-Gaussian terms are not | `scalar-induced-kernels` |
| 4 | How is the irreducible inflationary background evolved to today: transfer function, changes of g_*, neutrino damping, a non-standard expansion before BBN? | yes: formalism ≈6.8k and approximations ≈1.5k (Watanabe & Komatsu, Boyle & Steinhardt, Weinberg); 11 of 14 citations from arXiv:1801.04268, to be rebalanced in the deepening run | none |
| 5 | How does gauge-field production in axion inflation source chiral waves, and does homogeneous backreaction describe it? | yes at L2: formalism ≈2.8k, model card ≈2.5k, approximations ≈1.3k, open question ≈1.0k | none |
| 6 | What bound does extra radiation (ΔN_eff) put on the integrated background, for which sources, and with which data? | no: thin (results ≈1.7k, 3 of 4 citations from arXiv:1801.04268) | deepening run |
| 7 | How are the waves of preheating computed (lattice, resonance parameters, peak frequency and amplitude), and how do oscillons or gauge preheating change them? | no: thin (formalism ≈2.2k and model card ≈1.3k, all from arXiv:1801.04268, Sect. 7) | deepening run |
| 8 | How do gravitational waves propagate in modified gravity: friction, speed, mass, GW luminosity distance and its Ξ parameterisation? | yes: formalism ≈2.9k, results ≈1.2k; speed of tensors has its dossier in `thcosmo-modified-gravity` | none |
| 9 | How are the anisotropies and the polarisation of the stochastic background computed, and how does the CMB tensor transfer enter? | no: under "Not verified"; the CMB tensor transfer and B modes belong to `thcosmo-cmb-physics` (W3) | none in this round |
| 10 | Can the PTA signal be cosmological, and which source classes survive? | partly: open question ≈0.8k and the string, phase-transition and scalar-induced cards give their status; dossiers 1–3 cover the source side | none |

Dossiers chosen: three, questions 1–3; one deepening run for questions 6
and 7, which also replaces citations of arXiv:1801.04268 by the primary
papers it cites in the sections of question 4 and the defect section where
those papers can be read.
