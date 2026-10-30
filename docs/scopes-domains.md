# Scopes of the thcosmo-* domains

Fixed on 2026-10-30 by the owner's decisions D2–D9
(`docs/plans/2026-10-30-decisions.md`); revised after the pilot if it shows
a boundary does not hold. This file fixes the scope of each domain and its
boundary with the others, so that an equation or a result has one home.
Where a boundary says "stays in", the other skill gives the essentials in
two or three sentences and names the home.

## Boundary with the observational suite (cosmoskill)

The theory suite holds **formalism, models, theoretical results,
approximations and debates**. The observational suite holds **measured
values, survey facts, data systematics and pipelines**. A theory skill
quotes an observational bound only where a model's status depends on it, in
`models.md` (status column) or `results.md` (bounds on model parameters),
with dataset, confidence level and paper, and names the cosmoskill skill
that holds the measurement.

**Formalism has one home, here (decision D9).** cosmoskill's
`cosmo-theory-foundations` keeps the conventions each survey analysis adopts
and the accuracy of fitting formulae in data use, and points here for the
derivations and the conventions themselves. Equations shared by the two
suites are listed, with their home, in `docs/overlap-cosmoskill.md` (step
P6 of the plan). Six cosmoskill skills overlap in topic:

| cosmoskill skill | Stays there | Comes here |
|---|---|---|
| `cosmo-theory-foundations` | conventions adopted by each survey analysis; accuracy of fitting formulae against data use | the derivations and the conventions themselves (`thcosmo-cosmological-perturbations`, `thcosmo-lss-perturbation-theory`) |
| `cosmo-inflation-primordial` | measured n_s, r, f_NL, curvature, birefringence | inflation models and their predictions, correlator theory |
| `cosmo-dark-energy-modified-gravity` | w0wa evidence, μ–Σ and E_G measurements | the theories, their consistency and their status |
| `cosmo-neutrinos-dark-matter` | Σmν and N_eff bounds, dark-matter limits from data | the Standard-Model N_eff calculation, production mechanisms, perturbation theory with massive neutrinos |
| `cosmo-early-universe-exotica` | PTA and LVK background measurements, limits on PBHs, defects, spectral distortions | formation and sourcing theory |
| `cosmo-bbn` | measured abundances, nuclear rate measurements | the BBN network and its theory |

## Domains

| Skill | Holds | Stays elsewhere |
|---|---|---|
| `thcosmo-lss-perturbation-theory` | Standard and Lagrangian perturbation theory, renormalised and resummed schemes, EFTofLSS and its counterterms, IR resummation, bias expansion and bases, redshift-space distortions from Kaiser to EFT, consistency relations of LSS, primordial non-Gaussianity in LSS, velocity statistics and the momentum power spectrum, intrinsic alignments and shape bias, large-deviation and one-point statistics, perturbative forward models for field-level inference, massive neutrinos and other species in the non-linear perturbative regime. | Halo model and collapse: `thcosmo-nonlinear-structure`. Relativistic and wide-angle corrections beyond the standard RSD treatment: `thcosmo-relativistic-cosmology`. Fits to data: cosmoskill `cosmo-galaxy-clustering`, `cosmo-peculiar-velocities`. |
| `thcosmo-inflation` | Inflationary dynamics, slow roll and its parameter definitions, attractors, the model landscape (single-field, multi-field, plateau, hilltop, natural, Higgs and others by literature weight), reheating and preheating, initial-conditions problem, stochastic and eternal inflation including the tails of the curvature distribution, predictions for n_s and r. | Correlators beyond the power spectrum: `thcosmo-primordial-correlators`. String embeddings: `thcosmo-fundamental-theory`. PBH formation from the tails: `thcosmo-pbh-defects`. Tensor backgrounds beyond r: `thcosmo-cosmological-gravitational-waves`. |
| `thcosmo-primordial-correlators` | Quantisation of fluctuations, in-in formalism, EFT of inflation, non-Gaussianity shapes and templates, consistency relations and soft limits, cosmological collider, cosmological bootstrap, features, loop corrections and their debates, decoherence and the quantum-to-classical transition, QFT in de Sitter and infrared effects. | Late-time consistency relations and scale-dependent bias: `thcosmo-lss-perturbation-theory`. |
| `thcosmo-modified-gravity` | Scalar–tensor theories (Horndeski, beyond Horndeski, DHOST), f(R), vector–tensor, massive gravity and bigravity, teleparallel and non-metricity theories, non-local gravity, screening mechanisms, consistency conditions (ghosts, instabilities, strong coupling, positivity), the EFT of dark energy and parameterised frameworks (α_i, μ–Σ, PPF), the speed of tensors and its consequences, screening as treated in simulations. Split into two skills only if the build exceeds twelve subtopics (D6). | N-body codes: `thcosmo-theory-codes`. Measured μ–Σ: cosmoskill. |
| `thcosmo-dark-energy` | The cosmological-constant problem and vacuum energy, quintessence (thawing, freezing, tracking), k-essence, phantom fields and the crossing of w = −1, interacting dark energy (and its instabilities), early dark energy (formalism and models), holographic and other phenomenological classes by literature weight, model building after the DESI results. | Theories that modify gravity and the EFT of dark energy: `thcosmo-modified-gravity`. Early dark energy as a response to the H0 tension, status: `thcosmo-tensions-model-building`. Measured w0wa: cosmoskill. |
| `thcosmo-dark-matter-models` | Production mechanisms (thermal freeze-out, freeze-in, misalignment, non-thermal, gravitational), candidates (WIMPs, axions and ultralight fields, sterile neutrinos, self-interacting and dissipative dark matter, dark sectors), their linear signatures (transfer functions, cut-offs, acoustic oscillations), PBHs as dark matter (status). | Laboratory and indirect searches: out of scope. Wave dark-matter dynamics: `thcosmo-nonlinear-structure`. Dark-matter–dark-energy interactions: `thcosmo-dark-energy`. |
| `thcosmo-neutrinos-light-relics` | Neutrino decoupling and the Standard-Model N_eff calculation, massive-neutrino linear perturbations and free streaming, phase shift, dark radiation and light relics, interacting and decaying neutrinos. | Measured Σmν and N_eff: cosmoskill `cosmo-neutrinos-dark-matter`. Neutrinos in non-linear perturbation theory: `thcosmo-lss-perturbation-theory`. |
| `thcosmo-cosmological-gravitational-waves` | Primordial tensor modes, stochastic backgrounds from inflation, phase transitions, defects and scalar-induced sources, their spectral templates, gravitational-wave propagation on cosmological backgrounds and in modified gravity. | Gauge questions of second-order perturbations: `thcosmo-cosmological-perturbations`. Measured backgrounds: cosmoskill `cosmo-early-universe-exotica`. Standard sirens: cosmoskill `cosmo-multimessenger`. The speed of tensors as a constraint on theories: `thcosmo-modified-gravity`. |
| `thcosmo-baryogenesis-phase-transitions` | Sakharov conditions, electroweak baryogenesis, leptogenesis, Affleck–Dine and other mechanisms, electroweak and QCD transitions, first-order transitions: nucleation, bubble walls, dynamics; primordial magnetogenesis (at transitions and during inflation) and magnetic-field evolution. | Gravitational-wave spectra from transitions: `thcosmo-cosmological-gravitational-waves`. PBHs from transitions: `thcosmo-pbh-defects`. |
| `thcosmo-pbh-defects` | Primordial black-hole formation (thresholds, statistics, clustering), abundance theory, evaporation; cosmic strings and other topological defects, network evolution. | Their gravitational-wave signals: `thcosmo-cosmological-gravitational-waves`. PBHs as dark matter, status: `thcosmo-dark-matter-models`. The inflationary tail itself: `thcosmo-inflation`. |
| `thcosmo-cosmological-perturbations` | The FLRW background (metric, Friedmann and Raychaudhuri equations, fluids, distances and horizons as derived quantities, curvature, anisotropic backgrounds in outline), scalar–vector–tensor decomposition, gauge transformations and gauge-invariant variables, conserved curvature perturbations, separate-universe and δN, Einstein–Boltzmann hierarchy, adiabatic and isocurvature initial conditions, second-order perturbations and their gauge issues, line-of-sight integration as an algorithm. | CMB-specific physics: `thcosmo-cmb-physics`. Non-linear perturbation theory: `thcosmo-lss-perturbation-theory`. Inhomogeneous exact solutions: `thcosmo-relativistic-cosmology`. The Λ problem: `thcosmo-dark-energy`. |
| `thcosmo-thermal-history` | Equilibrium thermodynamics in an expanding universe, entropy and effective degrees of freedom, the Boltzmann equation and freeze-out as a method, BBN network theory and its inputs, recombination physics (hydrogen and helium, two-photon and Lyα escape) and recombination codes, the dark ages. | Neutrino decoupling and N_eff: `thcosmo-neutrinos-light-relics`. Dark-matter freeze-out as a production mechanism: `thcosmo-dark-matter-models`. Spectral distortions: `thcosmo-cmb-physics`. |
| `thcosmo-cmb-physics` | Acoustic oscillations, Thomson scattering, tight coupling and diffusion damping, polarisation and E/B, reionisation imprint, ISW, SZ effects and CMB lensing as theory, spectral distortions and thermalisation. | Measured spectra and likelihoods: cosmoskill `cosmo-cmb`. Primordial non-Gaussianity: `thcosmo-primordial-correlators`. |
| `thcosmo-nonlinear-structure` | Spherical and ellipsoidal collapse, excursion sets and mass-function theory, halo bias and profiles as theory, the halo model, Vlasov–Poisson and the theory of N-body discreteness and convergence, wave dark-matter dynamics (Schrödinger–Poisson), baryonic effects on the matter power spectrum (models and their parameterisation). | Simulation suites and emulators: cosmoskill `cosmo-simulations-mocks`. HOD fits: cosmoskill `cosmo-galaxy-halo-connection`. Screening in N-body: `thcosmo-modified-gravity`. |
| `thcosmo-relativistic-cosmology` | Relativistic effects in observables (number counts, light-cone effects, wide-angle terms), light propagation and the lensing formalism (Born and beyond, magnification), backreaction and averaging, inhomogeneous exact solutions (LTB, Szekeres), numerical relativity in cosmology, relativistic N-body. | CMB lensing: `thcosmo-cmb-physics`. Measured relativistic effects: cosmoskill. |
| `thcosmo-fundamental-theory` | String cosmology, moduli stabilisation, de Sitter constructions and their critiques, swampland conjectures and trans-Planckian censorship, quantum cosmology (Wheeler–DeWitt, loop quantum cosmology), holographic approaches, alternatives to inflation (bouncing, ekpyrotic, string-gas, emergent). | Inflation models without a UV embedding: `thcosmo-inflation`. QFT in de Sitter as a calculational framework: `thcosmo-primordial-correlators`. |
| `thcosmo-cosmic-dawn-igm` | IGM thermal and ionisation state, Lyα forest theory (fluctuating Gunn–Peterson and beyond), 21 cm brightness temperature and spin temperature, reionisation modelling (excursion-set and semi-numerical). | Measurements: cosmoskill `cosmo-lyman-alpha`, `cosmo-reionization-21cm`. |
| `thcosmo-theory-codes` | Built only if the evaluation asks for it (D5). Boltzmann codes and their forks, perturbation-theory codes, inflation and correlator solvers, phase-transition and BBN codes, relativistic and modified-gravity N-body codes; algorithms, accuracy settings, code agreement, maintenance. | Observational analysis codes: cosmoskill `cosmo-software-ecosystem`. While it does not exist, a code question goes to the domain of the physics. |
| `thcosmo-tensions-model-building` | Synthesis, updated last: for each tension or anomaly, the classes of theory responses, which data each survives, the theoretical cost of each, and the status of the debate. | Each model's own formalism and status: its domain. The size of each tension: cosmoskill `cosmo-tensions-anomalies`. |

## Topics that fit two skills (decision D7)

1. **A non-linear or late-time extension** lives with the non-linear method
   and points to the linear home. Massive neutrinos in the EFTofLSS:
   `thcosmo-lss-perturbation-theory`, pointer from
   `thcosmo-neutrinos-light-relics`.
2. **A mechanism lives with its physics; its observable signature with the
   observable.** The tail of the curvature distribution from stochastic
   inflation: `thcosmo-inflation`; PBH formation and abundance from it:
   `thcosmo-pbh-defects`. The scalar-induced background:
   `thcosmo-cosmological-gravitational-waves`; its gauge question:
   `thcosmo-cosmological-perturbations`.
3. **An interaction between two dark components** lives with the component
   whose equation of state is modified: interacting dark energy,
   `thcosmo-dark-energy`.
4. **A code question** lives in `thcosmo-theory-codes` if it exists,
   otherwise with the physics.
5. **A measured value** lives in cosmoskill; a theory skill quotes it only
   for a model's status.

Out of scope: laboratory and indirect dark-matter searches, collider
physics, and quantum gravity without a cosmological application.
