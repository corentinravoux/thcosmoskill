# Results on inflation

Scope: results that hold independently of one model: theorems and no-go results, bounds on the primordial parameters as they bear on models, reheating constraints, initial conditions, stochastic tails; then the history of the key results.

Snapshot: 2026-11-02

## Observational bounds on the primordial parameters
<!-- key: observational-bounds-on-the-primordial -->

Measured values belong to cosmoskill `cosmo-inflation-primordial`; they are quoted here only for the status of the model classes. Every bound below is quoted with its dataset combination and pivot.

| Quantity | Value as printed | Data | Paper and place |
|---|---|---|---|
| $n_{\rm s}$ | $n_\mathrm{s}=0.9649\pm 0.0042$ at 68% CL | Planck 2018 temperature, polarisation and lensing | Planck 2018 X, arXiv:1807.06211 [src: abstract] |
| $r$ | $r_{0.002}<0.10$ at 95% CL; $r_{0.002}<0.056$ with BK15 | Planck 2018; Planck 2018 + BK15 | arXiv:1807.06211 [src: abstract] |
| $r$ | $r_{0.05}<0.036$ at 95% confidence, with σ(r) = 0.009 from simulations | BICEP/Keck through 2018, with WMAP and Planck maps | BICEP/Keck XIII, arXiv:2110.00483 [src: abstract] |
| $n_{\rm s}$ | $n_s=0.974\pm0.003$ | P-ACT with CMB lensing (ACT and Planck) and DESI DR1 BAO | ACT DR6, Louis et al. 2025, arXiv:2503.14452 [src: abstract] |
| $r$ | $r<0.038$ (95%, P-ACT-LB-BK18) | P-ACT, lensing, BAO, BK18 | ACT DR6, Calabrese et al. 2025, arXiv:2503.14454 [src: Sect. IV.4] |
| running | $d n_s/d\ln k = 0.0062 \pm 0.0052$ | ACT DR6 with Planck, lensing and DESI Y1 | arXiv:2503.14454 [src: abstract] |

- Planck 2018 X concludes, for single-field models with Einstein gravity, that concave potentials, $V''(\phi)<0$, are increasingly favoured, and that two reconstructions of the potential find no evidence for dynamics beyond slow roll (arXiv:1807.06211) [src: abstract].
- ACT DR6: the BK18 limit on r, with $n_s$ from Planck, strongly excludes monomial models with convex potentials; P-ACT accommodates power laws with slightly higher indices than Planck alone, and the Starobinsky $R^{2}$ model with 50–60 e-folds lies on the 2σ boundary of P-ACT-LB (arXiv:2503.14454) [src: Sect. IV.4, Fig. 10 caption and text]. ACT adds in a footnote that the number of e-folds depends on the highly uncertain reheating history [src: Sect. IV.4, footnote 13].
- McDonough & Ferreira (2025) find that every CMB dataset (Planck PR3 and PR4, ACT, SPT-3G and their combination CMB-SPA) gives a higher $n_s$ when DESI DR2 BAO is added, the largest shift being ACT's, with a commensurate shift in the optical depth τ; CMB-SPA with DESI disfavours at more than 2σ the models preferred by Planck alone (Higgs, Starobinsky, exponential α-attractors) in favour of others such as polynomial α-attractors (arXiv:2512.05108) [src: abstract]. They trace the correlation of $n_s$ with the BAO parameters $r_{d}h$ and $\Omega_{m}$ in all CMB experiments to their sensitivity to large angular scales [src: Sect. I].
- Qiu & Huang's 2026 review states that with ACT DR6, and particularly with a SH0ES prior on $H_0$, the Starobinsky model is disfavoured at more than 95% confidence (arXiv:2606.24474) [src: abstract].

## Reheating constraints
<!-- key: reheating-constraints -->

- The reheating stage enters the predictions of every single-field model through $\Delta N_{*}$ (Eq. 48 of arXiv:1303.3787, in `formalism.md`); Planck 2018 X marginalises over it, and finds for $R^{2}$ the 95% CL range 49 < N_* < 59, compatible with N_* = 54 for T_reh ∼ 10^9 GeV (arXiv:1807.06211) [src: Sect. 4.2].
- Starobinsky model and inflaton couplings: the Planck measurement of $n_s$ constrains the Einstein-frame Yukawa coupling to light fermions, y < 4.5 × 10⁻⁴, corresponding to T_RH < 2 × 10¹¹ GeV; the ACT DR6 $n_s$ corresponds to 3.8 × 10⁻⁴ < y < 5.6 × 10⁻⁴ and 1.7 × 10¹¹ GeV < T_RH < 2.8 × 10¹¹ GeV (Ellis et al. 2025, arXiv:2510.15137) [src: abstract].
- E-model predictions move toward ACT values with higher reheating temperatures (arXiv:2510.18656) [src: abstract]; a stiff reheating stage, w̄ > 1/3, raises $n_s$ in T-models but saturates as w̄ → 1 (arXiv:2511.14673) [src: abstract].
- Lattice equation of state: with a trilinear coupling to a daughter field, tachyonic resonance raises $\bar w$ from 0 to a maximum below 1/3, after which the inflaton homogeneous mode dominates again and $\bar w$ returns toward 0 until perturbative reheating; accounting for this return can lower the predicted preheating gravitational-wave amplitude by many orders of magnitude relative to previous estimates (Antusch, Marschall & Torrenti 2025, arXiv:2507.13465) [src: abstract].
- Kinetic preheating in α-attractor models with derivative couplings forms black holes of masses of order tens of grams in fully general-relativistic lattice simulations, without large primordial curvature perturbations; their evaporation can reheat the Universe before BBN (Adshead, Currens & Giblin 2025, arXiv:2511.02059) [src: abstract]. Their formation and abundance theory: `thcosmo-pbh-defects`.

## Initial conditions
<!-- key: initial-conditions -->

- Duration: solving the horizon and flatness problems requires $N_{\rm tot}\equiv\ln\frac{a_{\rm end}}{a_{\rm start}}\gtrsim 60\,.$ (Baumann, arXiv:0907.5424) [src: Eq. 84], the precise value depending on the energy scale and on reheating [src: Sect. 6.2, text after Eq. 84].
- No-hair theorems (Snowmass report, arXiv:2203.07629, Sect. 3.3): except Bianchi IX, all homogeneous anisotropic cosmologies with a positive cosmological constant asymptote to de Sitter; for inhomogeneous ones, with the weak energy condition, global recollapse requires a positive three-dimensional Ricci scalar everywhere, which is topologically impossible for most 3-manifolds, and there is always an open neighbourhood expanding at least as fast as de Sitter; with mean curvature flow the result extends to a scalar field whose potential is bounded above and below by positive cosmological constants with a ratio between unity and 3/2 [src: Sect. 3.3].
- Numerical relativity, plateau and large-field: an expanding, highly inhomogeneous, gradient-dominated universe inflates if the initial field variations lie within a sufficiently flat region of the potential and the universe is flat or open on average, even when overdense regions collapse to black holes (East et al. 2016, arXiv:1511.05143) [src: abstract].
- Small against large field: small-field inflation can fail with subdominant gradient energies, whereas large-field inflation withstands dominant ones; large-field inflation is robust if the inflaton starts on the inflationary part of the potential, and with varying extrinsic curvature the spacetime stays inflationary if it is open (Clough et al. 2017, arXiv:1608.04408) [src: abstract].
- Snowmass summary: the new simulations show inflation more robust than previously thought, beginning even when gradient energy exceeds potential energy by orders of magnitude, for plateau models and for chaotic models below the Planck scale (arXiv:2203.07629) [src: Sect. 3.3].
- Anti-ultralocality, 2026: growth of gradient terms relative to velocity terms before inflation either prevents enough e-folds or triggers a quantum runaway for a plateau potential from generic initial conditions; the fine-tuning needed grows as the energy scale is lowered, which the authors read as disfavouring the usual ways of reducing r (Shterenberg et al. 2026, arXiv:2608.24997) [src: abstract]. It disagrees in conclusion with East et al. for plateau models; see `open-questions.md`.

## Stochastic inflation and the tails
<!-- key: stochastic-inflation-and-the-tails -->

- Exponential tails are generic: in the stochastic-δN formalism the tails of the curvature distribution decay exponentially, not as a Gaussian, from quantum diffusion alone, and cannot be described by the standard non-Gaussian expansions built near the maximum; the resulting PBH abundance can differ from standard results by several orders of magnitude, and potentials with an inflection point overproduce PBHs unless slow roll is violated (Ezquiaga, García-Bellido & Vennin 2020, arXiv:1912.05399) [src: abstract].
- In the regime of large diffusion, a strong suppression of the power spectrum is generically obtained (arXiv:1506.04732) [src: abstract].
- Friction and time reversal: in a semi-infinite flat potential with constant drift, time-reversed stochastic inflation gives exponentially decaying tails, against Lévy-like power laws without friction; forward and reverse approaches differ quantitatively, and in the classical-like limit of very large drift the tails become Gaussian only in the time-reversed picture. With negative drift (a toy model of eternal inflation) the forward approach becomes pathological while the reverse one keeps a finite distribution (Blachier & Ringeval 2025, arXiv:2511.21388) [src: abstract].
- Separate-universe breakdown: the approximation behind stochastic inflation fails during transitions between attractor and non-attractor phases; including gradient interactions through higher-dimensional Langevin equations recovers the perturbative gradient corrections and reveals a "pullback" effect that damps the tails of the first-passage-time distributions (Briaud, Kawaguchi & Vennin 2025, arXiv:2509.05124) [src: abstract].
- Foundations in QFT: stochastic inflation follows from QFT and the renormalisation group with corrections computable order by order, but the quantum dynamics is expected to matter for the tail; Green & Gupta reduce an exact-RG master equation for the long-wavelength density matrix to stochastic inflation and absorb divergences and secular growth by dynamical renormalisation (arXiv:2512.13842) [src: abstract].
- Heavy tails from multi-field kinetic couplings: an interaction $\dot{\phi}^{2}\text{exp}(\chi/M_{*})$ on a hyperbolic field space gives a non-perturbative pdf with a heavy tail $\propto\,\text{exp}\left\{-(\text{log}(\delta\phi^{2}))^{2}M_{*}^{2}/H^{2}\right\}$ (Snowmass Theory Frontier report, arXiv:2203.07629) [src: Sect. 3.5.3, inline].
- How the tail translates into PBH formation and abundance is in `thcosmo-pbh-defects` (two-home rule of the suite).

## History of the key results
<!-- key: history-of-the-key-results -->

| Date | Result | Paper | Status |
|---|---|---|---|
| 2009 | $\frac{1}{2}m^{2}\phi^{2}$ predicts n_s ≈ 0.96 and r ≈ 0.1, "something to look out for in the near future" | Baumann, arXiv:0907.5424 [src: Eqs. 242–243, text after] | superseded: $\phi^{2}$ strongly disfavoured, ln B = −11.5 (arXiv:1807.06211) [src: Table 5] |
| 2013 | α-attractors: n_s = 1 − 2/N, r = 12α/N² at small α | Kallosh, Linde & Roest, arXiv:1311.0472 [src: abstract] | current as a prediction; exponential class under pressure since 2025 (arXiv:2512.05108) [src: abstract] |
| 2013 | Plateau preference said to deepen the initial-conditions problem | Ijjas, Steinhardt & Loeb, arXiv:1304.2785 [src: abstract] | disputed by arXiv:1312.7619 [src: abstract]; revived for plateau models in 2026 (arXiv:2608.24997) [src: abstract] |
| 2015 | Non-perturbative stochastic-δN correlators; classicality criterion | Vennin & Starobinsky, arXiv:1506.04732 [src: abstract] | current; extended to gradient interactions (arXiv:2509.05124) and time reversal (arXiv:2511.21388) |
| 2016 | Inflation begins from highly inhomogeneous initial data in numerical relativity | East et al., arXiv:1511.05143 [src: abstract] | current for large-field and flat-region starts; contested for plateau models (arXiv:2608.24997) [src: abstract] |
| 2018 | $n_\mathrm{s}=0.9649\pm 0.0042$; $r_{0.002}<0.056$ with BK15; concave potentials favoured; $R^{2}$ as reference model | Planck 2018 X, arXiv:1807.06211 [src: abstract; Sect. 4.2] | $n_s$ superseded in combinations with DESI (below); r bound superseded by BK18 |
| 2019 | Exponential, not Gaussian, tails of the curvature distribution from quantum diffusion | Ezquiaga, García-Bellido & Vennin, arXiv:1912.05399 [src: abstract] | current |
| 2021 | $r_{0.05}<0.036$ at 95% confidence | BICEP/Keck XIII, arXiv:2110.00483 [src: abstract] | current tensor bound of the sources read |
| 2025 | $n_s=0.974\pm0.003$ (P-ACT + lensing + DESI DR1); Starobinsky on the 2σ boundary | ACT DR6, arXiv:2503.14452 [src: abstract]; arXiv:2503.14454 [src: Sect. IV.4] | debated (`open-questions.md`) |
| 2025 | CMB-SPA + DESI DR2 disfavour Higgs, Starobinsky and exponential α-attractors at more than 2σ; shift tied to the CMB–BAO tension and τ | McDonough & Ferreira, arXiv:2512.05108 [src: abstract] | current within ΛCDM |
| 2026 | With negative curvature or evolving dark energy, $n_s$ moves back toward plateau predictions | Chudaykin et al., arXiv:2607.28445 [src: abstract] | current; model-dependent |

## Not verified
<!-- key: not-verified -->

- The SPT-3G D1 value of $n_s$ alone was not read (only its abstract, arXiv:2506.20707).
- Planck PR4 inflation constraints were not read; the Planck 2018 X values above are from the 2018 release.
- The CMB-SPA + DESI DR2 value of $n_s$ of arXiv:2512.05108 was not read (abstract only, which gives no number).
- The volume measure and eternal-inflation predictivity debates beyond arXiv:0802.1067 and arXiv:1304.2785 / arXiv:1312.7619 were not researched.
