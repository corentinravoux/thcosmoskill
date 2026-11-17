# Gap audit — thcosmo-baryogenesis-phase-transitions

Plan v2, section 3, step 4. Written by the coordinator on 2026-11-17 from
`references/subtopics.tsv` and the reference files (section sizes measured
in characters). One subtopic is marked thin (Affleck–Dine and other
mechanisms): it goes to a deepening run (`docs/agent-brief-deepen.md`),
not to a dossier. The deepening also rebalances the word share (Bodeker
26.6 %, Athron 19.3 % at G1: the reviews arXiv:2009.07294 and
arXiv:2305.02357 carry most of the formalism).

| # | Question | L2 verdict | Dossier |
|---|---|---|---|
| 1 | How is the bubble-wall velocity computed: the Boltzmann equations with a wall force, the friction from local thermal equilibrium against out-of-equilibrium terms, the leading-log and full collision terms, the runaway criterion and the $\gamma^1$ against $\gamma^2$ friction at ultra-relativistic speeds; which method to use when? | partly: formalism ≈5.7k and approximations ≈3.1k give the regimes, the LTE friction and the debate (open ≈1.7k); the kinetic equations and the Bödeker–Moore pressure beyond leading order are under "Not verified" | `bubble-wall-velocity` |
| 2 | How is the CP-violating source of electroweak baryogenesis derived (vev-insertion against semiclassical force, the gradient expansion, why the leading-order vev-insertion source vanishes), and how are the transport equations solved for the asymmetry; how far do EDM bounds constrain it? | partly: formalism ≈3.8k, approximations ≈1.7k, model card ≈2.8k; the vanishing of the vev-insertion source is stated, not derived; transport equations not written out | `ewbg-sources-and-transport` |
| 3 | How is the baryon asymmetry of thermal leptogenesis computed: the Boltzmann equations for $N_1$ and $B-L$, the efficiency factor and its washout regimes, flavour effects, and what the density-matrix and Kadanoff–Baym treatments change? | partly: formalism ≈4.7k gives the result and the efficiency; $\varepsilon_1$ in terms of Yukawas and the Kadanoff–Baym form are under "Not verified"; flavour and resonant cards ≈1.2k each | `leptogenesis-kinetic-equations` |
| 4 | How is the nucleation rate computed from the bounce action, and how do percolation, completion and the milestone temperatures relate; when does $\beta/H$ fail? | yes: formalism ≈6.4k and approximations ≈3.2k (Athron et al.'s review, with the definitions and their premises) | none |
| 5 | How reliable is the perturbative effective potential (daisy resummation, the 3d EFT, gauge dependence), and when must lattice results be used? | yes at L2: formalism ≈4.0k, approximations ≈3.2k, open question ≈0.6k | none |
| 6 | What is the Standard-Model electroweak transition (crossover, endpoint, sphaleron freeze-out temperature and rate)? | yes: formalism ≈3.1k, results ≈2.3k and ≈3.2k (lattice values with their places) | none |
| 7 | How do Affleck–Dine and other non-thermal mechanisms produce the asymmetry, and what fixes its size? | no: thin (formalism ≈2.5k, card ≈2.6k, other cards ≈1.1–1.8k) | deepening run |
| 8 | How are primordial magnetic fields produced at transitions and during inflation, and how do they evolve (helicity, inverse cascade, decay laws)? | yes at L2: formalism ≈4.8k and ≈2.4k, four model cards, approximations ≈1.7k | none in this round |
| 9 | What does a first-order transition need in a model (which extensions, which strength $v/T_c$), and how does the 2025 lattice criterion change it? | yes: results ≈3.3k, model cards; the $v/T_c\gtrsim 1.33$ criterion with its conditions | none |
| 10 | How is the energy budget of a bubble (efficiency κ, sound-shell profiles) obtained? | lives in `thcosmo-cosmological-gravitational-waves` (`deep/phase-transition-spectra.md`); the original derivation not read here | none |

Dossiers chosen: three, questions 1–3; one deepening run for question 7,
which also rebalances the word share.
