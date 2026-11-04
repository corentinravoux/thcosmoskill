# Gap audit — thcosmo-neutrinos-light-relics

Plan v2, section 3, step 4. Written by the coordinator on 2026-11-04 from
`references/subtopics.tsv` and the reference files (section sizes measured
in characters). One subtopic is marked thin (light sterile neutrinos): it
goes to a deepening run (`docs/agent-brief-deepen.md`), not to a dossier.

| # | Question | L2 verdict | Dossier |
|---|---|---|---|
| 1 | How is the Standard-Model N_eff computed: the quantum kinetic equations for the density matrix, the collision integrals, finite-temperature QED to O(e³), the weak-rate corrections; and why do 3.0440 and 3.043 differ? | partly: formalism ≈3.6k and results ≈2.9k give the values and the breakdown (Table 5 of arXiv:2012.02726); the kinetic equations are under "Not verified"; the NLO dispute is stated, not explained | `neff-standard-model-calculation` |
| 2 | How are massive-neutrino perturbations solved in Boltzmann codes (momentum grid, hierarchy truncation, fluid approximation), and how are effective or negative neutrino masses defined when the data pull Σm_ν below the oscillation floor? | partly: approximations ≈2.5k cover the code treatment; open question "neutrino-mass tension as seen from theory" ≈2.1k states the proposals without their definitions or equations | `neutrino-mass-below-the-floor` |
| 3 | How are neutrino self-interactions and invisible decays put in the Boltzmann hierarchy (collision term, relaxation-time coefficients α_ℓ, the contact limit), and why was the earlier decay damping rate wrong? | partly: approximations ≈1.6k, model cards ≈3.3k + 1.8k; the α_ℓ of arXiv:2606.03395 not read beyond the abstract; the decay-rate correction (arXiv:2011.01502) from the abstract | `interacting-neutrino-perturbations` |
| 4 | How does free streaming produce the phase shift of acoustic oscillations, and what can produce one without free-streaming radiation? | yes: formalism ≈4.1k (Bashinsky & Seljak; arXiv:1508.06342); the value of a_ν under "Not verified" | none |
| 5 | Why is ΔN_eff ≥ 0.027 the minimal thermal target, and what lowers it? | yes: results ≈1.8k (arXiv:1604.08614, arXiv:2203.07943) | none |
| 6 | How is the small-scale suppression of P(k) by massive neutrinos derived, and at fixed what? | yes: Eqs. 143–144 of arXiv:astro-ph/0603494 with the fixed parameters | none |
| 7 | How do light but massive relics enter the background and perturbations, and how are their bounds reinterpreted between spins? | yes at L2: formalism ≈1.9k, results ≈0.8k | none |
| 8 | How are light sterile neutrinos thermalised (oscillation production, the role of lepton asymmetry and secret interactions), and how much ΔN_eff do they give? | no: thin | deepening run |
| 9 | How is N_eff used as a fitting parameter in BBN, and what does it hide? | yes: approximations ≈0.6k; BBN proper belongs to `thcosmo-thermal-history` | none |
| 10 | How do neutrino asymmetries change N_eff and BBN? | partly: the bounds quoted date from 2006 (formalism "Not verified") | none in this round |

Dossiers chosen: three, questions 1–3; one deepening run for question 8.
