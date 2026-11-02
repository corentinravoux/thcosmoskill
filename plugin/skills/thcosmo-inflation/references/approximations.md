# Approximations in inflationary theory

Scope: the approximations inflationary calculations rely on, their range of validity and their failure, with convention traps and numerical issues.

Snapshot: 2026-11-02

## Physical approximations
<!-- key: physical-approximations -->

### Slow-roll expansion: order and range
<!-- key: slow-roll-expansion-order-and-range -->
- **Assumes:** all Hubble-flow parameters much smaller than one (Martin et al., arXiv:1303.3787) [src: Sect. 3.1, text after Eq. 6].
- **Orders in use:** first order gives $n_{\scriptscriptstyle{\mathrm{S}}}=1-2\epsilon_{1}-\epsilon_{2},\quad n_{\scriptscriptstyle{\mathrm{T}}}=-2\epsilon_{1}.$ (arXiv:1303.3787) [src: Eq. 31]; the Encyclopaedia and Planck 2018 X fit with the second-order spectra (Eqs. 21–28 of arXiv:1303.3787) and marginalise over the second-order parameters (arXiv:1303.3787) [src: Sect. 3.1, text after Eq. 34]; Planck 2018 X uses the Hubble-flow spectra "to second order" (arXiv:1807.06211) [src: Sect. 4.2]. Third order is known (arXiv:1303.3787, Sect. 3.1, text after Eq. 28) and arbitrary order since 2026 (Giarè, arXiv:2610.28608) [src: abstract].
- **How it fails:** near the end of inflation, before $\epsilon_{1}=1$. In Starobinsky inflation $\epsilon_{2}$ exceeds one at x ≃ 1.83, before the end at x ≃ 0.94 (arXiv:1303.3787) [src: Eqs. 100–101]; in natural inflation $\epsilon_{2}$ and $\epsilon_{3}$ already exceed one when $\epsilon_{1}=1$, so the last few e-folds may not be described by slow roll [src: Sect. 5.6.2, text after Eq. 252]. Exact integration of the background and of the mode equations is possible numerically (FieldInf) [src: Sect. 3.1, text after Eq. 20].
- **Referee expects:** arXiv:1303.3787 for the expansions; the order used stated with the data's precision in mind.

### Horizon crossing and the attractor
<!-- key: horizon-crossing-and-the-attractor -->
- **Assumes:** the curvature perturbation freezes at horizon crossing, which requires the background to have relaxed to the slow-roll attractor.
- **How it fails:** in ultra-slow roll (η = 3) the curvature perturbation evolves rapidly on super-horizon scales and the horizon-crossing formalism is invalid (Kinney 2005, arXiv:gr-qc/0503017) [src: abstract]; in constant roll the would-be decaying mode can grow on non-attractor solutions (arXiv:1411.5021) [src: abstract].
- **Referee expects:** arXiv:gr-qc/0503017; numerical mode integration through any non-attractor phase.

### The number of e-folds at the pivot
<!-- key: the-number-of-e-folds-at-the-pivot -->
- **Assumes:** a reheating history, through $\ln R_{\mathrm{rad}}$ or $w_{\rm int}$ (arXiv:1303.3787, Eq. 48; arXiv:1807.06211, Eq. 47).
- **Range:** the window $N_{\rm cmb}\approx 40-60$ of Baumann (arXiv:0907.5424) [src: Eq. 85] or "50<N_{*}<60" used by Planck 2018 X for its $(n_s,r)$ figure (arXiv:1807.06211) [src: Sect. 4.2]; ACT notes that the number of e-folds depends on the highly uncertain reheating history (arXiv:2503.14454) [src: Sect. IV.4, footnote 13].
- **How it fails:** the verdict on a plateau model can depend on the reheating assumption: Ellis et al. find the Starobinsky model predicting n_s = 0.958–0.963 for reheating temperatures between $100 - 10^{10}$ GeV, and near-instantaneous reheating improving the agreement with the data (arXiv:2510.18656) [src: abstract].
- **Referee expects:** the reheating assumption stated with every $(n_s,r)$ prediction; arXiv:1303.3787 Sect. 3.2.

### Lyth bound
<!-- key: lyth-bound -->
- **Assumes:** slow roll during the observable e-folds; the bound is $\frac{\Delta\phi}{M_{\rm pl}}\simeq{\cal O}(1)\left(\frac{r}{0.01}\right)^{1/2}\,,$ (arXiv:0907.5424) [src: Eq. 356], an order-of-magnitude statement with an $\mathcal{O}(1)$ coefficient.
- **How it fails:** not read in a paper of this run (see "Not verified").

### Effective field theory and frames
<!-- key: effective-field-theory-and-frames -->
- **Higgs and $R^{2}$ inflation:** the Hubble scale is close to the unitarity bound on the cutoff (arXiv:0902.4465) [src: abstract]; the background-dependent cutoff stays above the dynamical scales (arXiv:1008.5157) [src: abstract].
- **Einstein and Jordan frames:** for Starobinsky inflation, matter is not universally coupled to the Einstein-frame metric, so the reheating parametrisation must be reconsidered in that frame (arXiv:1303.3787) [src: Sect. 4.1.3, last paragraph].
- **Radiative corrections:** inflaton couplings to matter can shift $n_s$ and r of Starobinsky inflation (arXiv:2510.15137) [src: abstract]; tree-level predictions assume they are negligible.

### Separate universe and stochastic inflation
<!-- key: separate-universe-and-stochastic-inflation -->
- **Assumes:** long-wavelength fluctuations evolve as homogeneous perturbations of the background (separate universe), with the noise term of the Langevin equation (arXiv:1506.04732) [src: Eq. 1].
- **Validity:** stochastic effects are small only for sub-Planckian, not too flat potentials (arXiv:1506.04732) [src: abstract]; perturbative corrections in the classical regime are Eq. 53 of that paper.
- **How it fails:** during transitions between attractor and non-attractor phases; gradient interactions are then needed (arXiv:2509.05124) [src: abstract]. The quantum dynamics is expected to matter for the far tail (arXiv:2512.13842) [src: abstract]. Forward and time-reversed formulations differ quantitatively in the tails (arXiv:2511.21388) [src: abstract].
- **Referee expects:** arXiv:1506.04732 and arXiv:1912.05399 for tails; a statement of the boundary conditions and of the time variable (e-folds; arXiv:1506.04732, Sect. 2).

### Analytic Hubble-flow parametrisations of transient phases
<!-- key: analytic-hubble-flow-parametrisations-of -->
- **How it fails:** smooth parametrisations of a transient ultra-slow-roll phase can hide sharp features in the reconstructed potential (Barnert et al. 2026, arXiv:2606.28005) [src: abstract].

## Convention traps
<!-- key: convention-traps -->

- **Direction of N.** Baumann counts N forward in his Eq. 70 and backward from the end in his Eq. 82 (arXiv:0907.5424) [src: Sect. 6.2]; Martin et al. count forward from $N_{\rm ini}$ (arXiv:1303.3787, Eq. 6). The sign in front of $d\varepsilon/dN$ follows; see the hub atlas for Kinney's backward convention.
- **Three meanings of η.** Baumann's second slow-roll parameter η = −φ̈/(Hφ̇) (arXiv:0907.5424, Eq. 73) is not the second Hubble-flow parameter $\epsilon_2$; Martin et al. use η for conformal time (arXiv:1303.3787, Eq. 15); Kinney's ultra-slow-roll η = 3 is the Hubble slow-roll parameter (arXiv:gr-qc/0503017) [src: abstract]. <!-- num: not a value -->
- **Three meanings of α.** The α of α-attractors (Kähler curvature, arXiv:1311.0472), the rate-of-roll constant of constant-roll inflation (arXiv:1411.5021, Eq. 7) and the running $\alpha_{\rm S}$ (arXiv:1303.3787, Eq. 30).
- **Pivot scale.** Planck 2018 X compares models at $k=0.002$ Mpc⁻¹ and quotes $r_{0.002}$ (arXiv:1807.06211) [src: Sect. 4.2; abstract]; BICEP/Keck and ACT quote r at 0.05 Mpc⁻¹ (arXiv:2110.00483; arXiv:2503.14454) [src: abstract; Sect. IV.4]. A bound is quoted with its pivot.
- **Two parametrisations of the same reheating.** $\ln R_{\rm rad}$ with $\overline{w}_{\rm reh}$ (arXiv:1303.3787, Eqs. 44–46) and $w_{\rm int}$, $\rho_{\rm th}$, $g_{\rm th}$ (arXiv:1807.06211, Eq. 47).
- **Hilltop scale in Planck 2018 X.** The 95% CL limit stated "in the quartic case" is printed with the subscript of the quadratic scale, $\mu_{2}$ (arXiv:1807.06211) [src: Sect. 4.2]; quote it with that caveat.
- **Planck mass.** The Starobinsky section of the Encyclopaedia uses $M_{\rm g}$, with $M_{\mathrm{g}}\simeq M_{\scriptscriptstyle{\mathrm{Pl}}}$ after inflation (arXiv:1303.3787) [src: Sect. 4.1.3, text after Eq. 99]; reduced and full Planck masses are compared in the hub atlas.

## Numerical issues
<!-- key: numerical-issues -->

- Exact background and mode integration: FieldInf (arXiv:1303.3787) [src: Sect. 3.1, text after Eq. 20]; slow-roll predictions of the Encyclopaedia models: the ASPIC library (arXiv:1303.3787, Sect. 2.2), also used by Planck 2018 X for its model comparison (arXiv:1807.06211) [src: Sect. 4.2, footnote 11].
- Preheating needs lattice simulations; Antusch et al. track the equation of state for about ten e-folds on 2+1-dimensional lattices and join them to a Boltzmann treatment (arXiv:2507.13465) [src: abstract]; fully general-relativistic lattices are needed when gravitational collapse occurs (arXiv:2511.02059) [src: abstract].
- Stochastic tails: Langevin realisations reproduce the analytic first-passage results (arXiv:1506.04732) [src: Sect. 3.3.2, Fig. 3 caption]; tails require dedicated methods (spectral, eigenvalue) beyond direct sampling `[der]`.
- Initial conditions require 3+1 numerical relativity (arXiv:1511.05143; arXiv:1608.04408) [src: abstracts].

## Referee checklist for an inflation paper
<!-- key: referee-checklist-for-an-inflation-paper -->

1. Planck-mass convention, direction of N and the meaning of η and α stated.
2. Slow-roll order of the predictions stated; numerical integration where slow roll fails (end of inflation, non-attractor phases).
3. $N_{*}$ derived from a stated reheating history, not the fixed 50–60 window of Planck 2018 X figures (arXiv:1807.06211) [src: Sect. 4.2], when the conclusion depends on $n_s$ at the present precision.
4. Bounds quoted with dataset combination and pivot; the dependence of the high-$n_s$ result on DESI BAO, τ and the cosmological model acknowledged (arXiv:2512.05108; arXiv:2607.28445).
5. For non-minimal coupling and $R^{2}$: the EFT cutoff and the frame of reheating discussed (arXiv:0902.4465; arXiv:1008.5157).
6. For multi-field models: field-space curvature and geometrical destabilisation checked (arXiv:1510.01281); isocurvature constraints applied (arXiv:1807.06211, Sect. 9).
7. For enhanced small-scale power: horizon-crossing formulas not used through ultra-slow roll; tails from stochastic δN, not from a perturbative non-Gaussian expansion (arXiv:1912.05399).
8. Forecasts labelled as forecasts.

## Not verified
<!-- key: not-verified -->

- Violations of the Lyth bound in non-monotonic or multi-field trajectories were not read in a paper of this run.
- The trans-Planckian problem of the mode functions and its censorship conjecture belong to `thcosmo-fundamental-theory` and were not read here.
- The size of the error of first- against second-order slow-roll predictions at the present precision was not found quoted in a paper read.
