# Approximations, traps and referee checks for neutrinos and light relics

Scope: the approximations the domain relies on, their validated range and quoted error, how they fail, convention traps and numerical issues; the referee checklist at the end.

Snapshot: 2026-11-03

## Instantaneous decoupling
<!-- key: instantaneous-decoupling -->

- Assumes that neutrinos are fully decoupled when $e^\pm$ annihilate, so that $T_{\gamma}/T_{\nu}=(11/4)^{1/3}\simeq 1.40102$; it is "very simple" and "reasonably accurate" (Lesgourgues & Pastor 2006, arXiv:astro-ph/0603494) [src: Sect. 3.1, inline, text after Eq. 8]. With non-instantaneous decoupling and oscillations the factor is 1.3978 [src: Sect. 3.1, text after Fig. 3].
- Its error on $N_{\rm eff}$: the leading-digit contributions to $N_{\rm eff}^{\rm SM}-3$ are listed in `results.md` (arXiv:2012.02726, Table 5). The non-instantaneous term is defined relative to instantaneous decoupling at $T_d=1.3453$ MeV [src: Table 5 caption].
- Where the neutrino masses matter, the spectra of the mass eigenstates, not the flavour eigenstates, should be used, and the momentum-dependent distortions can be integrated over only when neutrinos are relativistic or the observable does not depend on mass (arXiv:astro-ph/0603494) [src: Sect. 3.1, text after Fig. 3]; the relation between the masses and $\Omega_\nu h^2$ "must be evaluated numerically using the distorted distributions" for high precision [src: Sect. 3.3, footnote 1].

## $N_{\rm eff}$ as a fitting parameter in BBN
<!-- key: n-rm-eff-as-a-fitting-parameter-in-bbn -->

- Extrapolating dark-radiation scenarios to $\Delta N_{\rm eff}<0$ in BBN is "unphysical": a negative $\Delta N_{\rm eff}$ from entropy injection into photons after neutrino decoupling dilutes the neutrinos and suppresses neutrino-driven neutron–proton conversion, so one must either restrict the range of $N_{\rm eff}$ or adjust the neutrino-induced rates; the resulting BBN constraints "deviate significantly" from the conventional ones (Ganguly, Jung & Yun 2025, arXiv:2507.23354) [src: abstract].

## Interacting neutrinos: contact limit, collision kernel, fluid approximation
<!-- key: interacting-neutrinos-contact-limit-collision -->

- **Contact limit.** Integrating out the mediator is valid when its mass exceeds the energy of the scattering; for the CMB, $m_{\varphi}\gtrsim 1$ keV (arXiv:1902.00534) [src: Sect. II]. Pérez-Castro et al. compute the collision term for free neutrino and mediator masses, which "eliminates the need to approximate at high redshifts when the temperature increases above the mediator mass" (arXiv:2602.12477) [src: abstract], who find "a smooth transition from the light to the heavy mediator approximation as the Universe cools down for non-resonant cases" [src: abstract].
- **Universal coupling.** $g_{ij}\equiv g_{\nu}\delta_{ij}$ is "likely unrealistic" (arXiv:1902.00534) [src: Eq. 2; Sect. II]; with flavour-specific couplings and mixing, CMB bounds on the coupling weaken by $\sqrt{2}$ or $\sqrt{6}$ (arXiv:2609.13821) [src: abstract].
- **Bimodal posteriors.** Constraints on $G_{\rm eff}$ "suffer from bimodality"; a phase-shift detection could give a more robust limit, but BAO alone will not reach the precision needed (**forecast**, Whitford et al. 2025, arXiv:2511.00800) [src: abstract]. Profile likelihoods with DESI data show multimodality and lead to separate moderately and strongly interacting regimes (arXiv:2610.26654) [src: abstract].
- **Decay rate.** The anisotropy-loss rate $(1/\tau_0)(m_{\nu H}/E_{\nu H})^3$ used before 2020 is wrong by the power of the boost factor; limits derived with it are superseded (arXiv:2011.01502) [src: abstract] (arXiv:2203.09075) [src: abstract].

## Massive neutrinos in Boltzmann codes: momentum grid, truncation, fluid approximations
<!-- key: massive-neutrinos-in-boltzmann-codes-momentum -->

- **Momentum dependence.** The hierarchy of Eqs. 56–57 of Ma & Bertschinger depends on q, which makes massive neutrinos "computationally expensive"; they used 128 q-points and $l_{\rm max}=50$, adequate "at better than the 0.1% level", with an estimated relative accuracy better than $10^{-3}$ (arXiv:astro-ph/9506072) [src: Sect. 8].
- **Truncation.** The hierarchy is closed at $l_{\rm max}$ by Eq. 58 (`formalism.md`), together with Eqs. 51 and 65 for the other species (arXiv:astro-ph/9506072) [src: Sect. 8]. <!-- num: not a value -->
- **Viscous fluid approximation inside the Hubble radius** (CLASS): for any distribution function, the optimal momentum sampling "compatible with a given level of accuracy", and a switch to an approximate viscous fluid description inside the Hubble radius; one massive neutrino makes CLASS "just 1.5 times slower, instead of about 5 times in other codes (for fixed accuracy requirements)" (Lesgourgues & Tram 2011, arXiv:1104.2935) [src: abstract].
- **Its accuracy, revisited in 2025–2026.** The Dispersive Fluid Approximation, which captures the scale-dependent sound speed, "Within the standard ncdm module", "significantly outperforms the default CLASS fluid approximation" in the cross and neutrino power spectra and reduces errors in the CDM power spectrum "by up to an order of magnitude"; the Generalized Boltzmann Hierarchy integrates out the momentum dependence and, "Combined with the DFA and tested on massive neutrinos", reproduces the matter power spectrum "to better than permille accuracy" (Nasiri, Saravanan & Nascimento 2026, arXiv:2610.40275) [src: abstract]. A quasi-stationary analytic approximation inside an integral-equation version of CLASS keeps "sub-0.1% accuracy in the matter power spectrum today up to comoving wavenumber k = 100 Mpc⁻¹" (Lee, Ali-Haïmoud & Kamionkowski 2025, arXiv:2510.20821) [src: abstract].
- **Constant $f_\nu$.** The analytic growth law $\delta_{\rm cdm}\propto a^{p_{+}}\simeq a^{1-\frac{3}{5}f_{\nu}}~,$ (arXiv:astro-ph/0603494) [src: Eq. 134] assumes a time-independent $f_\nu$ after the transition, which is "not strictly valid" for non-degenerate masses [src: Sect. 4.5.6, text after Eq. 136]; the linear $-8f_\nu$ rule holds "for $0<f_{\nu}<0.07$" at fixed $(\omega_{\rm m},\Omega_\Lambda)$ [src: Sect. 4.5.7].
- **Non-linear scales.** Massive neutrinos in perturbation theory beyond linear order and in the EFTofLSS are in `thcosmo-lss-perturbation-theory` (two-home rule of the suite).

## Convention traps
<!-- key: convention-traps -->

- **Baseline of $\Delta N_{\rm eff}$.** The Planck 2018 limits compiled by Dvorkin et al. fix Standard-Model neutrinos at N_eff,fs = 3.046 (arXiv:2203.07943) [src: Sect. 3; Table 1], and Baumann, Green & Wallisch 2016 take the Standard-Model value as 3.046 (arXiv:1604.08614) [src: Sect. 1]; the same 2022 review gives N_eff^SM = 3.044(1) (arXiv:2203.07943) [src: Sect. 1], and arXiv:2012.02726 gives $3.0440 \pm 0.0002$ [src: abstract]. A $\Delta N_{\rm eff}$ must name its baseline.
- **Metric potentials.** φ and ψ swap roles between Lesgourgues & Pastor (arXiv:astro-ph/0603494, Eq. 25) and Ma & Bertschinger (arXiv:astro-ph/9506072, Eq. 5); Baumann et al. use Φ and Ψ with $\Phi_{\pm}$ (arXiv:1508.06342, Eqs. 1.4–1.5). See the table in `formalism.md`. <!-- num: not a value -->
- **The 93 eV coefficient.** $\Omega_{\nu}=\frac{\rho_{\nu}}{\rho_{\rm c}}=\frac{\sum_{i}m_{i}}{93.14\,h^{2}~{\rm eV}}~,$ (arXiv:astro-ph/0603494) [src: Eq. 12] assumes the instantaneous-decoupling distribution; the same paper uses 93.2 eV in Sect. 4.5.6 [src: text before Eq. 143], and "for high precision" the distorted distributions must be used [src: Sect. 3.3, footnote 1].
- **Flavour or mass states.** Distortions computed for flavour eigenstates must be converted to mass eigenstates when masses matter (arXiv:astro-ph/0603494) [src: Sect. 3.1, text after Fig. 3].
- **Fixed parameters in a "neutrino-mass effect".** The $-8f_\nu$ suppression, "a reasonable first-order approximation for $0<f_{\nu}<0.07$", is computed at fixed $(\omega_{\rm m},\Omega_\Lambda)$ (arXiv:astro-ph/0603494) [src: Sect. 4.5.7]; Fig. 15 of the same paper shows that fixing instead $\omega_{\rm b}$ and $\omega_{\rm cdm}$ shifts h or $\Omega_\Lambda$ [src: Fig. 15 caption].
- **The phase shift is not unique in a fit.** Its absence "can be compensated by shifting the value of other cosmological parameters" (arXiv:1902.00534) [src: abstract]; Bashinsky & Seljak's uniqueness statement is for adiabatic initial conditions and "standard physics" (arXiv:astro-ph/0310198) [src: abstract].

## What a referee checks in a theory paper of the domain
<!-- key: what-a-referee-checks-in-a-theory-paper-of-the -->

1. The Standard-Model $N_{\rm eff}$ used, its source, and whether $\Delta N_{\rm eff}$ is measured from it; the benchmark is 3.0440 (arXiv:2012.02726) [src: abstract].
2. Instantaneous or non-instantaneous decoupling, and whether spectral distortions matter for the observable (arXiv:astro-ph/0603494, Sect. 3.1).
3. For a light relic: spin, decoupling temperature, the $g_\star$ table used, and the assumed reheating temperature (arXiv:2203.07943, Eq. 2; arXiv:1604.08614, Sect. 1).
4. For massive neutrinos: mass ordering or degenerate approximation, which parameters are held fixed, and the accuracy of the fluid approximation at the scales used (arXiv:1104.2935; arXiv:2610.40275).
5. Gauge and potential names stated, and the hierarchy truncated consistently (arXiv:astro-ph/9506072, Eq. 58).
6. For interactions: contact limit justified by the mediator mass, universal or flavour-specific coupling, multimodal posteriors handled (arXiv:1902.00534, Sect. II; arXiv:2609.13821; arXiv:2610.26654).
7. For decays: the anisotropy-loss rate with the $(m/E)^5$ scaling and the daughter mass (arXiv:2011.01502; arXiv:2203.09075).
8. For negative $\Delta N_{\rm eff}$ in BBN: neutrino-driven rates adjusted consistently (arXiv:2507.23354).
9. For sterile neutrinos: fully or partially thermalised, and effective versus physical mass (arXiv:2606.21518).
