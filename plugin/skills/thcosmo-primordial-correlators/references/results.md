# Results on primordial correlators

Scope: theorems, no-go results, computed predictions and bounds that hold independently of one model, then the history of the key results.

Snapshot: 2026-11-02

## Theorems and consistency conditions
<!-- key: theorems-and-consistency-conditions -->

### Single-field consistency relation (squeezed limit)
<!-- key: single-field-consistency-relation-squeezed-limit -->

- **Statement.** Creminelli & Zaldarriaga 2004 (arXiv:astro-ph/0407059) show that, if the inflaton is the only dynamical field, the three-point function with one momentum much smaller than the other two is fixed by the power spectrum and its tilt, independently of the inflaton Lagrangian [src: abstract].
- **Equation.** The relation reads $\lim_{k_{1}\rightarrow 0}\langle\zeta_{\vec{\kappa}_{1}}\zeta_{\vec{\kappa}_{2}}\zeta_{\vec{\kappa}_{3}}\rangle=-(2\pi)^{3}\delta^{3}(\sum_{i}\vec{k}_{i})(n_{s}-1)P_{k_{1}}P_{k_{3}}\;$ (arXiv:astro-ph/0407059) [src: Eq. 1], with $P_{k}$ defined by Eq. 3 of the same paper (see formalism.md). The paper prints $\vec{\kappa}_{i}$ on the left and $\vec{k}_{i}$ on the right; it is copied as printed.
- **Local template in the same limit.** For the local $f_{\rm NL}$ of Eq. 5 of that paper, the squeezed limit is $\lim_{k_{1}\rightarrow 0}\langle\zeta_{\vec{\kappa}_{1}}\zeta_{\vec{\kappa}_{2}}\zeta_{\vec{\kappa}_{3}}\rangle=(2\pi)^{3}\delta^{3}(\sum_{i}\vec{k}_{i})\;4f_{\rm NL}P_{k_{1}}P_{k_{3}}\;$ (arXiv:astro-ph/0407059) [src: Eq. 6].
- **Original slow-roll statement.** Maldacena 2002 (arXiv:astro-ph/0210603) states that in a particular limit the three-point functions are determined completely by the tilt of the spectrum [src: abstract].
- **Multi-soft generalisation (2026).** Ullah 2026 (arXiv:2604.09765) derives tree-level multi-soft theorems at leading order in the soft expansion for scalar and tensor correlators with the background-wave method [src: abstract]. Its single-soft scalar theorem in terms of stripped correlators is $\lim_{\vec{k}_{1}\rightarrow 0}\langle\zeta(\vec{k}_{1}\dots\zeta(\vec{k_{N}})\rangle^{\prime}=\langle\zeta(\vec{k_{1}})\zeta(-\vec{k}_{1})\rangle^{\prime}\delta_{\zeta}\langle\zeta(\vec{k}_{2})\dots\zeta(\vec{k}_{N})\rangle^{\prime}$ (arXiv:2604.09765) [src: Eq. 14], with $\delta_{\zeta}$ the operator defined in Sect. 2 of that paper (not transcribed here); the unbalanced parenthesis is the paper's.
- **Conformal consistency relation.** Creminelli, Noreña & Simonović 2012 (arXiv:1203.4595) extend the relation to the subleading term of the squeezed limit, going as $1/q^2$, fixed by the variation of the n-point function under a special conformal transformation; for the 3-point function it implies no $1/q^2$ term, and in any single-field model the correlators of $\zeta$ carry an SO(4,1) symmetry with dilations and special conformal transformations non-linearly realised [src: abstract]. <!-- num: not a value -->
- **Infinite tower of Ward identities.** Hinterbichler, Hui & Khoury 2013 (arXiv:1304.5527) derive, for any single-field model with constant growing modes, an infinite number of consistency relations from non-linearly realised global symmetries labelled by an integer n: they constrain the $q^n$ behaviour of the soft limit completely for n = 0, 1 and partially for n ≥ 2; n = 0 recovers Maldacena's relations for a soft scalar and a soft tensor, n = 1 the conformal ones [src: abstract]. <!-- num: not a value -->
- **Violation in non-attractor single-field inflation.** Namjoo, Firouzjahi & Sasaki 2012 (arXiv:1210.3692) give a single-field toy model in which curvature perturbations are not conserved on superhorizon scales and decaying modes are not negligible in the non-attractor phase, so that a large local non-Gaussianity in the squeezed limit violates the standard consistency condition [src: abstract]. The assumption violated is the constant growing mode of Hinterbichler et al. (arXiv:1304.5527) [der].
- **Squeezed limit in the $\Phi$ normalisation.** The hub's atlas (`conventions.md`, section "Sign and normalisation of f_NL, and the shape template") transcribes Komatsu's 2010 form of the single-field squeezed limit in terms of $1-n_{s}$; it is not repeated here. <!-- num: not a value -->
- **What a violation would mean.** Ullah 2026 (arXiv:2604.09765) states that a violation of the scalar soft theorem would rule out all attractor single-field models and point to multi-field dynamics or a non-attractor phase [src: abstract].

### Observability of the squeezed limit
<!-- key: observability-of-the-squeezed-limit -->

- Pajer, Schmidt & Zaldarriaga 2013 (arXiv:1305.0824) show, using conformal Fermi coordinates, that Maldacena's squeezed scalar bispectrum and the tensor–scalar–scalar bispectrum of slow-roll single-field inflation lead to no deviation from a Gaussian universe except projection effects: the primordial contributions to the squeezed CMB bispectrum and to scale-dependent halo bias vanish [src: abstract].

## Shapes, trispectrum and bounds on model parameters
<!-- key: shapes-trispectrum-and-bounds-on-model -->

- **Suyama–Yamaguchi inequality.** When non-Gaussianity comes from superhorizon evolution, $\tau_{NL}\geq\frac{36}{25}f_{NL}^{2}.$ (Suyama & Yamaguchi 2008, arXiv:0709.2545) [src: Sect. II, Eq. 19]; it allows $f_{NL}$ to vanish while $\tau_{NL}$ stays finite, the leading non-Gaussianity then being the trispectrum [src: Sect. V]. <!-- num: not a value -->
- **Equilateral amplitude and sound speed.** $f_{\rm NL}^{\rm equil.}=\frac{85}{324}\cdot\frac{1}{c_{s}^{2}}\;$ at leading order in $1/c_{s}$ from the operator $\dot{\pi}(\nabla\pi)^{2}$ (Cheung et al. 2007, arXiv:0709.0293) [src: Eq. 45].
- **Bounds on the sound speed.** $c_{\mathrm{s}}^{\rm DBI}\geq\ 0.086$ at 95% from Planck 2018 T+E bispectra (arXiv:1905.05697) [src: Eq. 59]; $c_s \geq 0.38$ at 95% CL in the Open EFT of inflation with dissipation (arXiv:2603.13473) [src: abstract]. These bounds assume the model named; the measured $f_{\rm NL}$ values are held by cosmoskill `cosmo-inflation-primordial`.
- **Shape classes.** Shapes from horizon crossing (equilateral) and from superhorizon evolution (squeezed) are fairly orthogonal, so converting constraints between models through equilateral normalisations misleads (arXiv:astro-ph/0405356) [src: abstract]; single-field shapes are described by two templates, equilateral and orthogonal (arXiv:0905.3746) [src: abstract].
- **Excited initial states.** Even Hadamard excited states built over Bunch–Davies enhance the bispectrum for flattened (folded) triangles, parametrically above the standard result (Holman & Tolley 2008, arXiv:0710.1302) [src: abstract].

## Cosmological collider
<!-- key: cosmological-collider -->

- **Symmetry fixes the signal.** The squeezed limit carries the mass as a power law or oscillation, the spin as an angular dependence, and a relative phase from quantum interference (Arkani-Hamed & Maldacena 2015, arXiv:1503.08043) [src: abstract].
- **Boltzmann suppression at strong mixing.** Half the usual Boltzmann suppression at strong mixing (arXiv:2608.23243) [src: abstract]; exponential enhancement relative to Boltzmann suppression with high-frequency mass oscillations (arXiv:2511.00152) [src: abstract]. <!-- num: not a value -->
- **Data.** Maximum $2.35σ$ for spin-0 exchange in Planck after the look-elsewhere effect (arXiv:2512.22085) [src: abstract]; maximal $χ^2$ improvement of $5.3$ over the full multi-field landscape (arXiv:2607.18369) [src: abstract].

## Cosmological bootstrap
<!-- key: cosmological-bootstrap -->

- **Amplitude limit.** The total-energy singularity of a wavefunction coefficient has the flat-space amplitude as coefficient, $\lim_{E\to 0}\psi_{n}=\frac{iA_{n}}{E^{\alpha}}\,$ (arXiv:2203.08121) [src: Sect. 2.1.3, Eq. 2.9].
- **Cosmological optical theorem.** Unitarity implies an infinite set of relations among wavefunction coefficients for fields of any mass and general local interactions in de Sitter; any contact correlator with an odd number of conformally coupled scalars and any number of massless scalars vanishes (Goodhew, Jazayeri & Pajer 2020, arXiv:2009.02898) [src: abstract].
- **Bispectrum positivity.** For scalar-operator exchange from a hidden sector with mildly broken de Sitter isometries, the bispectrum is negative near the equilateral configuration and bounded above and below (arXiv:2506.19198) [src: abstract].
- **In-in and Euclidean equivalence.** Analytic continuation from the Euclidean sphere reproduces Schwinger–Keldysh results for tree and loop diagrams (arXiv:2610.28516) [src: abstract].

## Loop corrections
<!-- key: loop-corrections -->

- **No secular growth beyond logarithms.** Perturbative loop corrections grow at most as powers of the logarithm of the scale factor (Weinberg 2006, arXiv:hep-th/0605244) [src: abstract].
- **Running with $H$, not $k$.** The one-loop logarithm is $\log(H/\mu)$ in three regularisations (Senatore & Zaldarriaga 2009, arXiv:0912.2734) [src: abstract]. <!-- num: not a value --> <!-- eq: notation -->
- **Conservation at one loop.** The super-horizon $\zeta$ correlator is time independent at one loop in single-clock inflation (arXiv:1203.6651) [src: abstract].
- **Large scales and enhanced small scales.** Kristiano & Yokoyama 2022 (arXiv:2211.03395) compute the one-loop correction to the large-scale spectrum in a model with a sharp transition of the second slow-roll parameter and find that models producing appreciable primordial black holes induce non-perturbative coupling on CMB scales [src: abstract]. The version read (v3) is titled "Constraining Primordial Black Hole Formation from Single-Field Inflation" and speaks of constraining, not excluding, the small-scale spectrum [src: abstract].
- **Replies.** Including boundary (total-derivative) terms gives cancellations of the non-volume-suppressed contributions (Fumagalli 2023, arXiv:2305.19263) [src: abstract], and including the quartic Hamiltonian and the consistency relations of a transient non-slow-roll phase, the one-loop correction to long modes is a total derivative in comoving momenta, so long modes are unaffected (Fumagalli 2024, arXiv:2408.08296) [src: abstract]. With the separate-universe framework, the one-loop back-reaction comes from non-linear super-horizon evolution or one-loop-corrected initial conditions, and with separation of scales and adiabaticity it is not observable (Iacconi 2026, arXiv:2605.04815) [src: abstract]. Ward identities give the same conclusion for scalars and tensors (arXiv:2605.13325; arXiv:2509.00420) [src: abstracts].
- **Features.** The renormalised one-loop power spectrum generated by a localised feature vanishes at both large and small scales (Braglia, Céspedes & Pinol 2026, arXiv:2603.12216) [src: abstract].

## Decoherence
<!-- key: decoherence -->

- **Scalar decoherence is not slow-roll suppressed.** The leading decoherence of primordial scalar fluctuations in single-clock inflation, including all contributing interactions at leading order in $(H/M_p)^2$ and $ε_1$, is not slow-roll suppressed, unlike all earlier calculations, because it comes from interactions involving tensor and scalar environments simultaneously (Burgess et al. 2026, arXiv:2607.22914) [src: abstract]. The same derivation shows why the effects that undermine perturbation theory for decoherence do not undermine the prediction for the amplitude of primordial fluctuations [src: abstract]. <!-- num: not a value -->
- **Bound on classicalising decoherence.** Requiring the Newtonian potential to stay linear bounds the momentum variance any decoherence model can generate; the bound is violated by decohered thermal states with more than $14$ e-folds of inflation, and amplitude-basis decoherence is restricted to fewer than roughly $64$ e-folds (Haque & Underwood 2026, arXiv:2606.07663) [src: abstract].
- **Purity is not enough.** Interactions modelled by a quadratic Lindblad term de-squeeze the state, which suppresses quantum correlations beyond the purity loss (arXiv:2512.17622) [src: abstract].

## QFT in de Sitter
<!-- key: qft-in-de-sitter -->

### Infrared effects and stochastic inflation
<!-- key: infrared-effects-and-stochastic-inflation -->

- **Equilibrium of a light scalar.** A light self-interacting scalar in de Sitter reaches a de Sitter-invariant equilibrium for either sign of the mass term (Starobinsky & Yokoyama 1994, arXiv:astro-ph/9407016) [src: abstract]; the leading-order equilibrium distribution is $P_{\rm eq}(\phi)=Ce^{-8\pi^{2}V(\phi)/3H^{4}}\,$ (arXiv:2106.09728) [src: Sect. 2.1, Eq. 2.4].
- **Stochastic inflation from QFT.** SdSET derives stochastic inflation as renormalisation-group resummation of marginal superhorizon interactions of light fields (arXiv:2007.03693) [src: abstract]; the NNLO equation and equilibrium distribution (arXiv:2106.09728) [src: abstract] and the two-loop correction to the diffusion term (arXiv:2604.14283) [src: abstract] are computed. Conservation of adiabatic $\zeta$ and tensors to all orders follows from the irrelevance of superhorizon interactions when gravity is dynamical (arXiv:2007.03693) [src: abstract].

### Hilbert-space decomposition (Penedones et al. 2023)
<!-- key: hilbert-space-decomposition-penedones-et-al-2023 -->

- **Method and scope.** arXiv:2301.04146 decomposes the Hilbert space of QFT in $\text{dS}_{d+1}$ into unitary irreducible representations of $\text{SO}(1,d+1)$, using Harish-Chandra characters and numerical diagonalisation of the truncated quadratic Casimir; results are complete for $d=1$ and $d=2$ [src: abstract]. <!-- num: not a value --> <!-- eq: notation -->
- **Complementary series in two-particle states, $d\geq 3$.** For each pair $(n,s)$ of non-negative integers with $\Delta_{1}+\Delta_{2}-d-s-2n>\frac{d}{2}$, the tensor product $\mathcal{C}_{\Delta_{1},0}\otimes\mathcal{C}_{\Delta_{2},0}$ of $\text{SO}(1,d+1)$ contains a complementary series (arXiv:2301.04146) [src: Table 1.3, footnote 6, inline]. The table lists it as $\mathcal{C}_{\Delta_{1}+\Delta_{2}-d-s-2n,s}$ [src: Table 1.3]. <!-- num: not a value -->
- **Photon inside two massless scalars.** The tensor product ${\cal V}_{1,0}\otimes{\cal V}_{1,0}$ contains the type II exceptional series ${\cal U}_{1,0}$: the two-particle Hilbert space of two different massless scalars has an invariant subspace that is a photon, shown in $\text{dS}_{4}$ and stated to hold in higher dimensions (arXiv:2301.04146) [src: Sect. 4.4]. The coefficients of the photon state solve the recurrence with the general solution $c_{n}=\frac{A}{(n+1)(n+2)}$ (arXiv:2301.04146) [src: Eq. 4.26], and the state is normalisable, ${}_{a,b}\langle\chi|\chi\rangle_{a,b}=2|A|^{2}\sum_{n\geq 1}\frac{1}{n(n+2)}<\infty$ (arXiv:2301.04146) [src: Eq. 4.27]. The paper calls this an example of a novel result [src: Sect. 1].
- **Earlier results it builds on.** For $\text{SO}(1,3)$, Naimark found that $\mathcal{C}_{\Delta_{1}}\otimes\mathcal{C}_{\Delta_{2}}$ can contain one complementary series $\mathcal{C}_{\Delta_{1}+\Delta_{2}-2}$ when $\Delta_{1}+\Delta_{2}>3$, as reported by arXiv:2301.04146 [sec: Sect. 1, Brief literature review]; Naimark's papers predate arXiv and were not read. <!-- num: not a value -->
- **Källén–Lehmann representation.** Hogervorst et al. 2021 (arXiv:2107.13871) recover the Källén–Lehmann spectral decomposition of the scalar bulk two-point function from the Hilbert-space decomposition, relate poles of the spectral densities to boundary CFT data, and derive an inversion formula for the spectral density by continuation from the sphere [src: abstract].
- **Recent use (2026).** Belrhali, Poisson, Renaux-Petel & Werth 2026 (arXiv:2601.15228) build a momentum space for QFT in $\text{dS}_{d+1}$ in Poincaré slicing in which the dS frequency is the unitary-representation label of $\text{SO}(1,d+1)$, reformulate in-in perturbation theory in it, and accommodate principal and complementary series in the Källén–Lehmann decomposition of composite operators [src: abstract]. <!-- num: not a value -->

## History of the key results
<!-- key: history-of-the-key-results -->

| Year | Result | Paper | Status |
|---|---|---|---|
| 1995 | Squeezed vacuum perturbations equivalent to classical stochastic ones once the decaying mode is neglected | Polarski & Starobinsky, arXiv:gr-qc/9504030 [src: abstract] | Standard; refined by open-system calculations (2018–2026) |
| 2002 | Slow-roll bispectrum computed; squeezed limit fixed by the tilt | Maldacena, arXiv:astro-ph/0210603 [src: abstract] | Standard; equations read here through the review arXiv:1002.1416 [src: Eqs. 4.22–4.23] |
| 2004 | Squeezed-limit relation for any single-field Lagrangian | Creminelli & Zaldarriaga, arXiv:astro-ph/0407059 [src: abstract] | Standard |
| 2005 | In-in formalism extended to loops | Weinberg, arXiv:hep-th/0506236 [src: abstract] | Standard |
| 2007 | EFT of inflation; $f_{\rm NL}^{\rm equil}$ tied to $c_{s}$ | Cheung et al., arXiv:0709.0293 [src: abstract; Eq. 45] | Standard |
| 2009 | Orthogonal template | Senatore et al., arXiv:0905.3746 [src: abstract] | Standard basis of CMB searches |
| 2009 | One-loop running is $\log(H/\mu)$, not $\log(k/\mu)$ | Senatore & Zaldarriaga, arXiv:0912.2734 [src: abstract] | Supersedes the $\log(k/\mu)$ running of earlier calculations <!-- eq: notation --> |
| 2012 | Conformal consistency relations; non-attractor violation | arXiv:1203.4595; arXiv:1210.3692 [src: abstracts] | Standard |
| 2013 | Relation is a coordinate (projection) effect; no primordial squeezed signal in observables | Pajer, Schmidt & Zaldarriaga, arXiv:1305.0824 [src: abstract] | Refines how the 2002/2004 results are read, does not supersede them |
| 2015 | Cosmological collider | Arkani-Hamed & Maldacena, arXiv:1503.08043 [src: abstract] | Standard |
| 2018 | Bootstrap from symmetries and singularities | Arkani-Hamed et al., arXiv:1811.00024 [src: abstract] | Extended to boost-breaking (2020–2022) |
| 2020 | Cosmological optical theorem; SdSET | arXiv:2009.02898; arXiv:2007.03693 [src: abstracts] | Current |
| 2021 | Källén–Lehmann decomposition of dS two-point functions from the Hilbert space | Hogervorst et al., arXiv:2107.13871 [src: abstract] | Basis of the non-perturbative dS bootstrap |
| 2022 | One-loop large-scale effect of enhanced small scales | Kristiano & Yokoyama, arXiv:2211.03395 [src: abstract] | Disputed; replies find no observable effect (arXiv:2408.08296, arXiv:2605.04815) |
| 2023 | UIR content of free multi-particle and CFT Hilbert spaces in dS | Penedones et al., arXiv:2301.04146 [src: abstract] | Complete for $d=1,2$; open for $d\geq 3$ [src: Sect. 1] <!-- eq: notation --> |
| 2025 | Planck collider searches with orthogonalised templates: $2.35σ$ maximum | Suman et al., arXiv:2512.22085 [src: abstract] | Current; no detection |
| 2026 | Scalar decoherence not slow-roll suppressed | Burgess et al., arXiv:2607.22914 [src: abstract] | Supersedes slow-roll-suppressed estimates; no reply found |
| 2026 | Two-loop correction to the stochastic diffusion term | Beneke et al., arXiv:2604.14283 [src: abstract] | Current |
| 2026 | Multi-soft theorems for scalars and tensors, tree level, leading soft order | Ullah, arXiv:2604.09765 [src: abstract] | Recent, single-author; no reply found |

## Not verified
<!-- key: not-verified -->

- The general-$d$ results of arXiv:2301.04146 for spinning complementary series are described by the paper as very incomplete [src: Table 1.3 caption]; none is given here.
- Naimark's $\text{SO}(1,3)$ result is quoted only through arXiv:2301.04146; no primary paper or DOI was read. <!-- num: not a value -->
- The squeezed-limit $f_{\rm NL}$ value implied by comparing Eqs. 1 and 6 of arXiv:astro-ph/0407059: the sentence that states it was not located with the tool (a grep for the fraction returned nothing), and no agent-made value is given.
- No date-sorted search from 2025-06-01 returned a correction to the tree-level slow-roll bispectrum itself (searches of this run: in-in methods, consistency relations and soft theorems, EFT of inflation).
