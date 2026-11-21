# Approximations in cosmological perturbation theory

Scope: the approximations the relativistic perturbation formalism relies on, their range of validity, gauge artefacts and convention traps, numerical issues of Einstein–Boltzmann codes, and the referee checklist.

Snapshot: 2026-11-20

## Super-Hubble limit and gradient expansion
<!-- key: super-hubble-limit-and-gradient-expansion -->

- **Assumes:** $k/{\cal H}\ll 1$ in linear theory (arXiv:0809.4944, Sect. 8.2.2), or a universe "smooth over a sufficiently large comoving scale", with conditions stated to first order in a small parameter ε, in the non-linear treatment of Lyth, Malik & Sasaki (arXiv:astro-ph/0411220) [src: abstract; Sect. III.1]. <!-- num: not a value -->
- **Validated:** conservation of ζ needs, in addition, a vanishing non-adiabatic pressure, "so long as Ψ remains finite" (arXiv:0809.4944) [src: Sect. 8.2.2, text after Eq. 8.37], or P a unique function of ρ (arXiv:astro-ph/0411220) [src: abstract]; with the anisotropic stress taken "negligible at that order" [src: Sect. III.1], if, to first order in ε, P is a unique function of ρ, Lyth, Malik & Sasaki find on uniform-density slices $-\dot{\psi}=\dot{\zeta}=O(\epsilon^{2})\,.$ (arXiv:astro-ph/0411220) [src: Sect. III.1, Eq. 24].
- **Fails:** when $\delta P_{\rm nad}\neq 0$ on super-Hubble scales, which "will lead to a change in the curvature perturbation ζ", the mechanism of the curvaton scenario (arXiv:0809.4944) [src: Sect. 8.2.2]; at the transition into ultra-slow roll, where gradient terms break the separate-universe approximation, and for the momentum Π at the transition back (arXiv:2506.23571) [src: abstract].
- **Cite:** Wands et al. (arXiv:astro-ph/0003278), Lyth, Malik & Sasaki (arXiv:astro-ph/0411220), Weinberg (arXiv:astro-ph/0302326).

## Separate universe and δN
<!-- key: separate-universe-and-n -->

- **Assumes:** anisotropy and spatial gradients neglected on large scales, so that each patch evolves as a homogeneous FRW universe (arXiv:0809.4944) [src: Sect. 11, text after Eq. 11.2]; for the leading-order δN of field fluctuations, the slow-roll approximation or, "more generally", a negligible decaying mode of the field perturbations on super-Hubble scales [src: Sect. 11, text before Eq. 11.3].
- **Validated:** for multi-field non-linear sigma models with non-minimal coupling, the approach "adequately reproduces the dynamics of the large scale perturbations" for wavelengths above a list of lower bounds derived from the background (arXiv:2609.34788) [src: abstract].
- **Fails:** at the slow-roll to ultra-slow-roll transition, and for the momentum Π also at the transition back (arXiv:2506.23571) [src: abstract]; in the computation of Ahmadi & Ahmadi, standard δN misses "some essential physical features" of the equilateral $f_{\rm NL}$ that their gradient-corrected method captures (arXiv:2602.00902) [src: abstract]; in Bianchi I with a scalar coupled to a U(1) field, an intrinsic-curvature contribution adds to the δN contribution in the conserved comoving curvature perturbation (arXiv:2607.11814) [src: abstract].
- **Cite:** Sasaki & Stewart (arXiv:astro-ph/9507001), Wands et al. (arXiv:astro-ph/0003278), Lyth, Malik & Sasaki (arXiv:astro-ph/0411220); stochastic δN is in `thcosmo-inflation`.

## Truncation of the Boltzmann hierarchy
<!-- key: truncation-of-the-boltzmann-hierarchy -->

- **Assumes:** multipoles above $l_{\rm max}$ set to zero or extrapolated.
- **Validated:** Ma & Bertschinger's extrapolation, Eq. 51, from the spherical-Bessel behaviour that is exact for l > 0 if $\partial_{\tau}(\phi+\psi)=0$ in conformal Newtonian gauge, assuming "that this relation holds approximately for time-varying potentials" (arXiv:astro-ph/9506072) [src: Sect. 5.3, inline, text after Eq. 50]; they find that it "greatly improves on the simple truncation", but that time variations of the potentials in the radiation era "make even equation (51) a poor approximation if $l_{\max}$ is chosen too small" [src: Sect. 5.3, text after Eq. 51]. <!-- num: not a value -->
- **Fails:** plain truncation is "simple but inaccurate": errors propagate to l = 0 in a time $\tau\approx l_{\rm max}/k$ and reflect back, amplifying errors in the "square well" $0\leq l\leq l_{\rm max}$ (arXiv:astro-ph/9506072) [src: Sect. 5.3, inline, text after Eq. 50]; truncating massless-neutrino moments beyond l ≥ 2 in the pure CDM model gives "a 10% error in the anisotropy power spectrum", as quoted from Hu et al. (1995) [src: Sect. 1]. <!-- num: not a value -->
- **Cite:** Ma & Bertschinger (arXiv:astro-ph/9506072).

## Tight coupling, ultra-relativistic fluid and radiation streaming
<!-- key: tight-coupling-ultra-relativistic-fluid-and -->

- **Assumes:** the three approximations of CLASS for basic ΛCDM: baryon–photon tight coupling (first order, second order or a compromise), an ultra-relativistic fluid approximation for massless neutrinos (a "Sub-Hubble fluid approximation", Sect. 3.2 title), and radiation streaming after decoupling, "taking reionisation into account" (arXiv:1104.2933) [src: abstract].
- **Validated:** with cl_3permille.pre, 0.3 % precision on the $C_l$ up to l = 3000, exact equations being used only around Hubble crossing and in the super-Hubble, non-tightly-coupled region (arXiv:1104.2933) [src: Sect. 5; Fig. 10 caption]; with the precision file cl_permille.pre and $l_{\rm max}=(k\tau)_{\rm ufa}=18$, the fluid approximation is both faster and more accurate than plain truncation, and the no-fluid results "are very unstable and depend a lot on the choice" of $l_{\rm max}$ (the truncation multipole) and $(k\tau)_{\rm ufa}$; "with the present choice" they have "a twice larger error in the CMB spectra than in any UFA scheme" [src: Sect. 3.6; Table 3 caption, inline]. <!-- num: not a value -->
- **Not covered:** more general cosmological models, in which "other approximation schemes can be introduced", more exotic cases being discussed "case-by-case"; massive neutrinos and non-cold relics are treated in a companion paper (arXiv:1104.2933) [src: Sect. 5].
- **Cite:** Blas, Lesgourgues & Tram (arXiv:1104.2933).

## Fluid approximations for non-cold relics
<!-- key: fluid-approximations-for-non-cold-relics -->

- **Assumes:** solvers evolve non-cold relics on a momentum grid and often switch "to a fluid approximation on small scales for efficiency" (Nasiri et al. 2026, arXiv:2610.40275) [src: abstract].
- **Validated:** within the standard ncdm module of CLASS, the dispersive fluid approximation "significantly outperforms the default CLASS fluid approximation in the cross and neutrino power spectra" and reduces CDM power-spectrum errors "by up to an order of magnitude", adding 1–4 % to the runtime; combined with the generalized Boltzmann hierarchy for massive neutrinos and tested on massive neutrinos, it reproduces the matter power spectrum "to better than permille accuracy" (arXiv:2610.40275) [src: abstract].
- **Limits:** within the standard ncdm module, the default fluid approximation of CLASS is outperformed by the dispersive one in the spectra named above (arXiv:2610.40275) [src: abstract]. The massive-neutrino hierarchy itself is in `thcosmo-neutrinos-light-relics`.

## Newtonian limit and the gauge of simulations
<!-- key: newtonian-limit-and-the-gauge-of-simulations -->

- **Assumes:** Newtonian N-body dynamics with initial displacements from an Einstein–Boltzmann spectrum and the Zel'dovich approximation.
- **Validated:** "in most gauges the initial displacements generated in this way receive a first-order relativistic correction"; in the N-body gauge it vanishes, and a Newtonian simulation then "includes all first-order relativistic contributions (in the absence of radiation)" (Fidler et al., arXiv:1505.04756) [src: abstract]. The longitudinal gauge "has also proven useful for calculations on small scales, since it gives evolution equations closest to the Newtonian ones" (arXiv:0809.4944) [src: Sect. 7.1.1, text after Eq. 7.8; the authors cite their Ref. 54].
- **Not covered:** radiation, excluded by the condition of Fidler et al. quoted above; the longitudinal gauge can be "difficult to define … in the super-horizon limit", with numerical instabilities on large scales (arXiv:0809.4944) [src: Sect. 7.1.1].
- **Cite:** Chisari & Zaldarriaga (arXiv:1101.3555), Fidler et al. (arXiv:1505.04756); the Newtonian-motion-gauge method is in `thcosmo-lss-perturbation-theory`.

## Convention traps
<!-- key: convention-traps -->

- **Sign of ζ.** Malik & Wands write $-\zeta_1$ for the uniform-density curvature with ψ entering $C_{ij}$ with a minus sign (arXiv:0809.4944, Eqs. 2.12, 7.61); Lyth, Malik & Sasaki write −ζ for ψ that enters the metric as $e^{2\psi}$ (arXiv:astro-ph/0411220, Eqs. 3, 5, 37).
- No paper read states the relation between the two ζ: quote each with its own metric.
- **Sign of Φ against ζ.** Malik & Wands give $\Phi=-(3/5)\zeta$ for the Newtonian potential "on large scales in the matter era" (arXiv:0809.4944) [src: Sect. 11, footnote 5, inline]; the atlas lists Planck 2018 IX and Komatsu with a plus sign. An $f_{\rm NL}$ is quoted with its variable and sign.
- **Bardeen's notation.** Malik & Wands' Ψ is minus Bardeen's $\Phi_H$ (arXiv:0809.4944, Sect. 7.1.1, footnote 2).
- **τ.** Conformal time in Laine & Procacci (arXiv:2607.06983, Eq. 1.3) and Ma & Bertschinger (arXiv:astro-ph/9506072), cosmic (proper) time in Malik & Wands' synchronous-gauge paragraph (arXiv:0809.4944, Sect. 7.3); Malik & Wands use η for conformal time (Eq. 2.7).
- **Names of the potentials.** ψ in $g_{00}$ for Ma & Bertschinger, ϕ for Malik & Wands, and the swaps listed in the atlas; Laine & Procacci call φ and ψ the Bardeen potentials (arXiv:2607.06983) [src: Sect. 8.3, second paragraph]. <!-- num: not a value -->
- **Poisson gauge.** A synonym of the Newtonian gauge in Laine & Procacci's subsection title (arXiv:2607.06983, Sect. 4.2), its extension to vectors and tensors in Malik & Wands (arXiv:0809.4944, Sect. 7.1.1).
- **$\Omega_K$.** Defined with $\lvert\kappa\rvert$ by Laine & Procacci (arXiv:2607.06983, Sect. 1.4) and by a sum rule by Hogg (arXiv:astro-ph/9905116, Eq. 7); Hogg's Eq. 16 attaches the sinh form to positive $\Omega_k$.
- **Second-order factors.** Malik & Wands expand $g_{00}=-a^{2}\left(1+2{\phi_{{1}}}+{\phi_{{2}}}\right)\,,$ (arXiv:0809.4944) [src: Sect. 2.2.2, Eq. 2.15, first row] and note "further choices for the way the spatial metric is split into the different perturbation variables at second (and higher) order" [src: Sect. 2.2.2, text after Eq. 2.14].
- `[der]` A second-order variable is compared between papers only after its expansion convention is read.
- **Distances.** The angular-diameter distance between two redshifts is not the difference of the two distances, and Hogg's Eq. 19 does not hold for negative $\Omega_k$ (arXiv:astro-ph/9905116) [src: Sect. 6]. <!-- num: not a value -->

## Gauge artefacts
<!-- key: gauge-artefacts -->

- Super-horizon density contrasts are "strongly gauge-dependent": they grow as $a^2$ in synchronous gauge in the radiation era and stay constant in conformal Newtonian gauge (arXiv:astro-ph/9506072) [src: Sect. 8, "Before horizon crossing", item 1]. <!-- num: not a value -->
- Synchronous gauge leaves residual gauge modes unless fixed, for example by a vanishing initial CDM velocity (arXiv:0809.4944) [src: Sect. 7.3, Eq. 7.43 and text before].
- The flat-gauge shear grows as $\eta$ in radiation or matter eras while Ψ is constant (arXiv:0809.4944) [src: Sect. 7.2.1].
- `[der]` Growth of a gauge-dependent variable is not physical growth.
- Weinberg's discussion of synchronous and Newtonian gauges suggesting "inequivalent assumptions" at large wavelength (arXiv:astro-ph/0302326) [src: abstract].
- Second-order induced tensors are gauge dependent through mode mixing (arXiv:2509.26159) [src: abstract]; see `thcosmo-cosmological-gravitational-waves`.
- Initial conditions taken from general relativity in a modified-gravity code give "significant deviations" in CMB spectra against theory-consistent ones, for the early modified-gravity models of Pan et al., Horndeski theory in the EFT approach "assuming constant EFT functions at early times" (arXiv:2506.17411) [src: abstract].

## What a referee checks in a theory paper of the domain
<!-- key: what-a-referee-checks-in-a-theory-paper-of-the -->

- Signature, the definition of each potential through a written line element, the meaning of τ or η, and the sign of ζ and ℛ stated against a written metric.
- Gauge stated for every perturbation variable; gauge-invariant combinations named with their gauge (longitudinal, flat, comoving, uniform density).
- Synchronous-gauge residual freedom fixed and said how.
- Conservation of ζ claimed only with its conditions: super-Hubble scales, $\delta P_{\rm nad}$ negligible or P(ρ), shear term negligible.
- Separate universe or δN used only where gradients are negligible; transitions (ultra-slow roll), anisotropy and non-minimal couplings checked against the papers above.
- Initial conditions: adiabatic or which isocurvature mode, regular or not; consistent initial conditions in theories beyond general relativity.
- Boltzmann code: hierarchy truncation and approximation switches, precision settings, and agreement with a second code quoted with its range.
- Second order: generator and expansion convention stated; gauge of second-order tensors and of observables stated.
- Distances: $\Omega_k$ convention and the sign of curvature in the sinh or sin form.

