# Approximations, traps and checks in modified gravity

Scope: the approximations the domain relies on (quasi-static, linear, screening approximations, EFT validity), convention traps, numerical issues, and the list a referee checks.

Snapshot: 2026-11-02

## Quasi-static approximation
<!-- key: quasi-static-approximation -->

- **What it assumes.** Time derivatives of the potentials and of the scalar are neglected against spatial gradients inside the sound horizon, $\dot{\varepsilon}\sim H\varepsilon\ll\partial\varepsilon/a$ (arXiv:1901.07183) [src: Sect. 3.4.2, inline, text after Eq. 90]; Kobayashi's $G_{\rm eff}$ and η (Eqs. 100–101) also drop mass terms and so do not apply to f(R) and chameleon models [src: Sect. 3.4.2, text after Eq. 101].
- **Where it is validated.** The modified-gravity N-body code comparison tested the quasi-static limit for the symmetron, the model of the comparison with the largest non-static effects expected, and concludes that it "is a very good approximation for all of the observables considered here" (arXiv:1506.06384, Winther et al. 2015) [src: abstract].
- **How it fails.** On scales comparable to the sound horizon of the scalar and on very large scales; Kobayashi points to his Refs. [151–153] for the limits and to [150, 154, 155] for the complete equations (arXiv:1901.07183) [src: Sect. 3.4.2, text after Eq. 101]. `[der]` Those references were not read in this run.

- **Sound horizon, not Hubble horizon.** The quasi-static approximation breaks down, at best, outside the sound horizon of dark energy rather than the cosmological horizon; as an order-of-magnitude estimate it may be used for today's weak-lensing and peculiar-velocity data only if the sound speed exceeds "order 1%" of the speed of light, for Euclid-like surveys above "around 10%", never for the ISW effect, and for CMB lensing only above 10% (arXiv:1503.06831, Sawicki & Bellini 2015) [src: abstract].

## Validity of the effective theory
<!-- key: validity-of-the-effective-theory -->

- Gravitational-wave constraints on dark-energy theories assume that the low-energy theory holds at the LIGO scale (about 100 Hz, $10^{-13}$ eV as Kobayashi writes it) (arXiv:1901.07183) [src: Sect. 4.2, text after Eq. 131]. De Rham & Melville show that the LIGO band lies close to the cutoff of many dark-energy models, where the speed of gravitational waves can return to one (arXiv:1806.09417) [src: abstract]. A referee asks the author to state the cutoff of the theory.

- **Ghosts, gradient and tachyonic instabilities, superluminality.** Joyce et al. collect the diagnostics of an EFT in an appendix: ghosts, gradient instabilities, tachyonic instabilities, and analyticity, locality and superluminality (arXiv:1407.0059) [src: outline, App. D.1–D.4]. In the α basis, a fit that samples $\alpha_{i}$ freely must reject parameter regions with D ≤ 0 or $c_{\rm s}^{2}\le0$ (arXiv:1404.3713) [src: Sect. 3.3]; the resulting prior shapes the $w_0w_a$ posterior (arXiv:2606.31977) [src: abstract].
- **Positivity priors** reduce the allowed parameter space of Horndeski fits strongly (arXiv:1904.05874) [src: abstract]; they assume a unitary, causal, local UV completion, which is the premise a referee checks.
- **Strong coupling of new branches.** A reduced linear spectrum on a cosmological background signals infinite strong coupling (arXiv:2311.04201) [src: abstract]; massive gravity's partially massless point and f(Q) branches are examples (arXiv:1401.4173, Sect. 8.3.6; arXiv:2311.04201) [src: same places].

## Screening in simulations
<!-- key: screening-in-simulations -->

- **Code agreement.** For f(R), DGP and the symmetron, started from the same initial conditions, the fractional deviation of the matter power spectrum from ΛCDM agrees between codes "to better than 1% up to k ∼ 5−10 h/Mpc", with good agreement for the velocity-divergence spectrum, halo abundances and profiles (arXiv:1506.06384) [src: abstract].
- **Solvers.** ECOSMOG adds a multigrid-relaxation solver for the extra degrees of freedom to the adaptive-mesh code RAMSES, tested on f(R) (arXiv:1110.1379, Li et al. 2011) [src: abstract]. EFT-RAMSES embeds the EFT of DE in the α basis and reduces the normal and self-accelerating DGP models, the cubic scalar and vector Galileons, the generalised cubic covariant Galileon and generic EFT parameterisations to one "master" Vainshtein equation (arXiv:2607.24940, Ota Woodcock et al. 2026) [src: abstract]. PySCo-EFT (particle mesh) and ECOSMOG-EFT (adaptive mesh) treat luminal Horndeski with Vainshtein screening; they agree with linear theory "sub-0.5 percent" on large scales, and numerical effects on the power-spectrum boost (mass resolution, finite volume, refinement threshold, starting redshift) stay "below 2% at the largest wavenumbers (k=10 h/Mpc) for the range of tested values" (arXiv:2604.15434, Ganjoo et al. 2026) [src: abstract].
- **Semi-analytic alternatives.** The halo-model reaction applied to luminal Horndeski with Vainshtein screening in spherical collapse is presented as focused on "qualitative trends and parameter dependencies" (arXiv:2601.02074, de Boe et al. 2026) [src: abstract]. In the generalised cubic covariant Galileon the reaction "captures the qualitative behaviour of the simulations, while residual differences appear on deeply nonlinear scales"; in that model the enhancement of the power spectrum over QCDM reaches "approximately $7\%$ at $z=0$" in the transition to the non-linear regime and decreases at smaller scales because of Vainshtein screening (arXiv:2608.06499, Atayde et al. 2026) [src: abstract]. A one-loop EFTofLSS implementation (PyBird) for Vainshtein-screened luminal Horndeski and nDGP is validated against N-body for the $\alpha_i\propto\Omega_{\rm DE}$ parameterisation <!-- eq: notation -->, and retaining the exact time dependence instead of the Einstein–de Sitter approximation costs little (arXiv:2607.26945) [src: abstract].
- **Fitting formulae.** The Euclid review lists, for f(R), a fitting formula (Winther et al. 2019), the FORGE, mgemu and e-MANTIS emulators and ReACT (arXiv:2512.09748) [src: outline, Sect. 6.2.1]; their accuracy was not read in this run. N-body codes themselves belong to `thcosmo-theory-codes` when it exists.

## Convention traps
<!-- key: convention-traps -->

- **Which potential sits in $g_{00}$.** Planck 2015 XIV puts Ψ in $g_{00}$ and Φ in $g_{ij}$ (arXiv:1502.01590) [src: Eq. 1]; Kobayashi puts Φ in $g_{00}$ and Ψ in $g_{ij}$ (arXiv:1901.07183) [src: Eq. 87]. The slip "η" is therefore Φ/Ψ in one and Ψ/Φ in the other (arXiv:1502.01590, Eq. 6; arXiv:1901.07183, Eq. 101), and MGCAMB calls it γ (arXiv:1502.01590) [src: Sect. 3.2.2, footnote 2].
- **The α functions are not the EFT coefficients.** Bellini & Sawicki's $\alpha_{i}$ are dimensionless combinations (arXiv:1404.3713, Eqs. 51–55); the EFT of DE of Gubitosi et al. uses mass-dimension coefficients such as $M_{2}^{4}$, $\bar{M}_{1}^{3}$ (arXiv:1210.0201; Planck 2015 XIV form in the hub atlas); Bellini & Sawicki give the translation table [src: Sect. 3.5].
- **X.** Kobayashi's $X$ carries $-1/2$ (arXiv:1901.07183, Sect. 4.1); other works do not (hub atlas). A sound speed or a stability condition written with $G_{iX}$ is quoted with the X it assumes.
- **Bellini & Sawicki's Eq. 13** prints the scalar gradient term without a square (arXiv:1404.3713) [src: Eq. 13]; copy it as printed and do not read it as a different operator.

## Referee checklist
<!-- key: referee-checklist -->

1. Signature, potential in $g_{00}$, definition of X and sign of the $G_{3}$ term stated (see `formalism.md`, conventions).
2. For a fit in the α basis or with μ–Σ: the time parameterisation ($\alpha_i\propto\Omega_{\rm DE}$, $\propto a$, $\propto a^3$), the stability prior (D > 0, $c_s^2>0$) and its effect on the posterior stated (arXiv:1404.3713; arXiv:2606.31977). <!-- num: not a value --> <!-- eq: notation -->
3. $\alpha_{\rm T}=0$ or $c_{\rm GW}=1$ imposed, or the cutoff argument made explicit (arXiv:1901.07183, Sect. 4.2; arXiv:1806.09417).
4. For DHOST or GLPV: graviton decay ($\alpha_{\rm H}$) addressed (arXiv:1809.03484).
5. Quasi-static approximation justified against the dark-energy sound speed and not used for ISW (arXiv:1503.06831).
6. Screening: which mechanism, whether the non-linear prescription is unscreened or super-screened (arXiv:2512.09748, Sect. 4.1.1), and whether non-spherical sources matter (arXiv:2607.09098).
7. Ghost, gradient, tachyonic and strong-coupling checks on the background used, including new branches (arXiv:1407.0059, App. D; arXiv:2311.04201).
8. Positivity bounds, if invoked, with the UV assumption stated (arXiv:1904.05874; arXiv:2103.06855).
9. For f(R): $\lvert f_{R0}\rvert$ compared with astrophysical bounds, not only cosmological ones (arXiv:2512.09748, Sect. 5.1; arXiv:2009.08743).
10. Simulation-based predictions: code validated against the code comparison or a second code (arXiv:1506.06384; arXiv:2604.15434).

## Not verified
<!-- key: not-verified -->

- The accuracy of the f(R) fitting formula and the FORGE, mgemu and e-MANTIS emulators (arXiv:2512.09748, Sect. 6.2.1) was not read.
- Kobayashi's references on the limits of the quasi-static approximation (his Refs. 151–153) were not read; Sawicki & Bellini (arXiv:1503.06831) stand in for them.
- The accuracy of ReACT for screened models was not read beyond the Euclid review's statement that the α-parameterisation case was not validated against simulations (arXiv:2512.09748, Sect. 4.1.2).
