# Models of cosmological perturbations

Scope: the classes of backgrounds and of initial conditions that the perturbation formalism is applied to: matter contents of the FLRW background, the adiabatic and isocurvature modes, anisotropic backgrounds in outline.

Snapshot: 2026-11-20

Snapshot of model statuses: 2026-11-20. This domain is formalism; its "models" are the backgrounds and initial conditions the formalism is applied to. Inflationary models are in `thcosmo-inflation`, dark-energy and modified-gravity models in `thcosmo-dark-energy` and `thcosmo-modified-gravity`.

## Backgrounds
<!-- key: backgrounds -->

### Constant equation of state: radiation, matter, de Sitter, kination
<!-- key: constant-equation-of-state-radiation-matter-de -->
- **Defining equations:** $w\;\equiv\;\frac{\bar{p}}{\bar{e}}\;,$ taken approximately constant (Laine & Procacci 2026, arXiv:2607.06983) [src: Sect. 1.4, Eq. 1.74], in the Friedmann equations of `formalism.md`.
- **Parameters:** w; the conventional values are 0 for matter (dust), 1/3 for radiation, "strictly speaking only correct for non-interacting blackbody radiation", 1 for kination, and −1 for de Sitter when the kinetic energy of the field is negligible against $\bar e$ and there is no radiation (arXiv:2607.06983) [src: Sect. 1.4, "Simplified equations of state"].
- **Predictions:** w < −1/3 gives accelerated and w > −1/3 decelerated expansion (arXiv:2607.06983) [src: Sect. 1.4, "Simplified equations of state", last paragraph]; the comoving Hubble radius scales as $(aH)^{-1}=H_{0}^{-1}a^{\frac{1}{2}(1+3w)}\,.$ (Baumann 2009, arXiv:0907.5424) [src: Sect. 4.2, Eq. 37].
- **Consistency:** none disputed.
- **Observational status:** not a model to be tested by itself; measured expansion histories are in cosmoskill.
- **Status date:** 2026-11-20

### Spatially curved FLRW
<!-- key: spatially-curved-flrw -->
- **Defining equations:** the curvature κ of Eq. 1.2 and the Friedmann equation with κ (arXiv:2607.06983) [src: Sect. 1.2, Eq. 1.2; Sect. 1.3, Eq. 1.39]; during a cosmological-constant era, $\frac{\dot{a}^{2}}{a^{2}}+\frac{\kappa}{a^{2}}\;\overset{{\mbox{\tiny\rm{(\ref{eq_end0-1})}}}}{=}\;\frac{8\pi G\bar{e}_{i}}{3}\;\equiv\;H_{i}^{2}\;\approx\;{\rm constant}\;.$ (arXiv:2607.06983) [src: Sect. 1.4, Eq. 1.75].
- **Parameters:** κ, or $\Omega_K$ in the convention of each paper (see the conventions block of `formalism.md`).
- **Predictions:** the authors' goal in that subsection is "to show that even if κ ≠ 0, the actual Hubble rate soon approaches the value $H_{i}$, so that effectively κ plays no role" (arXiv:2607.06983) [src: Sect. 1.4, text after Eq. 1.75]; the transverse distance takes the sinh or sin form of Hogg's Eq. 16 (arXiv:astro-ph/9905116) [src: Sect. 5, Eq. 16]. <!-- num: not a value -->
- **Consistency:** none disputed at the level of the formalism.
- **Observational status:** Laine & Procacci quote, from their Ref. 6, $\Omega_{K}<10^{-3}$ at the current time (arXiv:2607.06983) [src: Sect. 1.4, "De Sitter space-time as an explanation for spatial flatness", inline]; current measured values and their dataset dependence are in cosmoskill `cosmo-cmb` and `cosmo-galaxy-clustering`.
- **Status date:** 2026-11-20

### Bianchi I and other homogeneous anisotropic backgrounds (outline)
<!-- key: bianchi-i-and-other-homogeneous-anisotropic -->
- **Defining equations:** homogeneous but anisotropic Bianchi spacetimes; Scholtens et al. 2026 work "in a frame such that metric components depend solely on (cosmic) time" (arXiv:2604.19706) [src: abstract].
- **Parameters:** the anisotropic metric functions of cosmic time and the matter content; Saito & Naruko 2026 take a scalar field coupled to a U(1) gauge field and use shear and electric-flux integration constants (arXiv:2607.11814) [src: abstract].
- **Predictions:** in Bianchi I, "scalar, vector and tensor modes do not decouple", giving a scalar–tensor "see-saw" mechanism, and the statistics of density perturbations and gravitational waves depend "on the wave-vector instead of its norm" (Pereira, Pitrou & Uzan 2007, arXiv:0707.0736) [src: abstract]; three physical degrees of freedom generalise the Mukhanov–Sasaki variables for a scalar field [src: abstract]. Scholtens et al. derive Newtonian-gauge perturbation equations for general Bianchi models, for scalar and pure tensor perturbations, and, for the scalar ones, "the equivalent of the Mukhanov-Sasaki equation for Bianchi models" (arXiv:2604.19706) [src: abstract]. For linear superhorizon perturbations of Bianchi I with a scalar coupled to a U(1) gauge field, the conserved comoving curvature perturbation is the δN contribution plus an intrinsic-curvature contribution (arXiv:2607.11814) [src: abstract].
- **Consistency:** none found.
- **Observational status:** Pereira et al. say these effects "may be related to some anomalies of the cosmic microwave background anisotropies on large angular scales" (arXiv:0707.0736) [src: abstract]; the anomalies are in cosmoskill `cosmo-tensions-anomalies`. Inhomogeneous exact solutions belong to `thcosmo-relativistic-cosmology`.
- **Status date:** 2026-11-20

## Initial conditions: the regular modes
<!-- key: initial-conditions-the-regular-modes -->

The mode basis is that of Bucher, Moodley & Turok (arXiv:astro-ph/9904231, abstract): one growing adiabatic mode and four regular isocurvature modes (CDM, baryon, neutrino density, neutrino velocity). Measured amplitudes belong to cosmoskill `cosmo-inflation-primordial` and `cosmo-cmb`; the statuses below are given with the dataset and the paper. <!-- num: not a value -->

### Adiabatic mode
<!-- key: adiabatic-mode -->
- **Defining equations:** a vanishing non-adiabatic pressure, $\delta P_{\rm nad}\equiv\delta P-\frac{P^{\prime}}{\rho^{\prime}}\delta\rho\,.$ (arXiv:0809.4944) [src: Sect. 9.1, Eq. 9.5] equal to zero, and vanishing relative entropy perturbations $S_{IJ}$ (Eq. 9.4 there); Baumann's form is in the hub atlas (arXiv:0907.5424, Eq. 137).
- **Parameters:** the amplitude and tilt of ζ or ℛ (see `thcosmo-inflation`).
- **Predictions:** ζ constant on super-Hubble scales "so long as Ψ remains finite" (arXiv:0809.4944) [src: Sect. 8.2.2, text after Eq. 8.36]; for an inflaton thermalizing with a plasma, isocurvature vanishes when $\mathcal{R}_{\varphi}$ freezes out, under the assumptions stated in `formalism.md` (arXiv:2607.06983) [src: Sect. 8.3].
- **Consistency:** none disputed at the level of the formalism; the vanishing of isocurvature is "justified rather succinctly in the literature" according to Laine & Procacci (arXiv:2607.06983) [src: Sect. 8.3, first paragraph]; reply: none found.
- **Observational status:** adiabatic ΛCDM is the reference against which Planck 2018 X compares its isocurvature extensions; the one-parameter CDI extensions of adiabatic ΛCDM have Bayes factors that "all … fall below −5" and none improves χ² (Planck 2018 X, arXiv:1807.06211) [src: Sect. 9.4].
- **Status date:** 2026-11-20

### CDM density isocurvature, uncorrelated ("axion I")
<!-- key: cdm-density-isocurvature-uncorrelated-axion-i -->
- **Defining equations:** a CDM–radiation relative entropy perturbation $S_{IJ}$ (arXiv:0809.4944, Eq. 9.4), uncorrelated with ℛ; Planck 2018 X sets $\mathcal{P}_{\cal R\cal I}=0$ and $n_{\cal I\cal I}=1$ (arXiv:1807.06211) [src: Sect. 9.4.1]. <!-- num: not a value -->
- **Parameters:** the primordial isocurvature fraction $\beta_{\rm iso}$ at $k_{\rm mid}$ (arXiv:1807.06211) [src: Sect. 9.4.1].
- **Predictions:** the uncorrelated case with $n_{\cal I\cal I}=1$ "is a good approximation for many multi-field inflationary models where the slow-roll parameter (in the isocurvature field perturbation direction) $\eta_{ss}$ is negligible and the background trajectory in field space is straight between Hubble radius exit and the end of inflation"; to first order in the slow-roll parameters, $n_{\mathcal{II}}=1-2\epsilon+2\eta_{ss}$ (arXiv:1807.06211) [src: Sect. 9.4.1, inline].
- **Consistency:** none disputed here.
- **Observational status:** $\beta_{\rm iso}(k_{\rm mid})<0.038$ at 95 % CL, Planck TT,TE,EE+lowE+lensing (arXiv:1807.06211) [src: Sect. 9.4.1, Eq. 90]; if all the dark matter is in axions, $H_{\mathrm{inf}}<0.86\times 10^{7}\thinspace\mathrm{GeV}\left(\frac{f_{a}}{10^{11}\thinspace\mathrm{GeV}}\right)^{0.408}$ at 95 % CL [src: Sect. 9.4.1, Eq. 91]. For ultralight axions, Liu, Hu & Grin 2026 (arXiv:2608.07803) give, from the Planck CDM-isocurvature bound, $r\ f_{\rm dm} < 0.08\,(m_a/10^{-27}\,{\rm eV})^{-1/2}$ in the dark-matter regime [src: abstract].
- **Status date:** 2026-11-20

### CDM density isocurvature, fully correlated or anticorrelated ("curvaton I/II")
<!-- key: cdm-density-isocurvature-fully-correlated-or -->
- **Defining equations:** $n_{\cal I\cal I}=n_{\cal R\cal R}$ and $\cos\Delta=\pm 1$ (arXiv:1807.06211) [src: Sect. 9.4.2, inline]; the curvaton is the physically motivated example quoted there [src: Sect. 9.4.2].
- **Parameters:** $\beta_{\rm iso}$, independent of k in this case; the parameter $r_D$ of the curvaton models quoted there [src: Sect. 9.4.2].
- **Predictions:** after curvaton decay, as printed, $\beta_{\mathrm{iso}}\simeq 9(1-\tilde{r})^{2}/[r_{D}^{2}+9(1-\tilde{r})^{2}]$ (arXiv:1807.06211) [src: Sect. 9.4.2, inline, text after Eq. 93], for the cases of Gordon & Lewis quoted there; the local non-Gaussianity quoted from Sasaki et al. 2006 is $f_{\mathrm{NL}}^{\mathrm{local}}=\left(1+\Delta_{s}^{2}\right)\frac{5}{4r_{D}}-\frac{5}{3}-\frac{5r_{D}}{6},$ [src: Sect. 9.4.2, Eq. 94].
- **Consistency:** "Many models giving anticorrelation produce too large an isocurvature fraction to be consistent with the above limit, but case 9 of Gordon & Lewis (2003) survives" (arXiv:1807.06211) [src: Sect. 9.4.2].
- **Observational status:** $\beta_{\mathrm{iso}}<0.00095$ (fully correlated) and $\beta_{\mathrm{iso}}<0.00107$ (fully anticorrelated), 95 % CL, Planck TT,TE,EE+lowE+lensing (arXiv:1807.06211) [src: Sect. 9.4.2, Eqs. 92–93].
- **Status date:** 2026-11-20

### Neutrino density and neutrino velocity isocurvature
<!-- key: neutrino-density-and-neutrino-velocity -->
- **Defining equations:** the neutrino-to-photon ratio varies at zero net density perturbation (density mode); a relative bulk velocity of neutrinos and photon–baryon plasma at zero net momentum (velocity mode) (arXiv:astro-ph/9904231) [src: abstract].
- **Parameters:** the amplitudes in the 5×5 correlation matrix of Bucher et al. [src: abstract]. <!-- num: not a value -->
- **Predictions:** identified as modes "which do not seem to have been discussed before" in 1999 (arXiv:astro-ph/9904231) [src: abstract].
- **Consistency:** none found.
- **Observational status:** with the CMB-SPA combination (Planck 2018, ACT DR6, SPT-3G), DESI DR2 BAO and DES Y5 supernovae, the neutrino density isocurvature amplitude is "consistent with zero" in ΛCDM, and the 95 % upper limit on $\sum m_\nu$ moves from < 0.052 eV (adiabatic) to < 0.057 eV with it (Hou et al. 2026, arXiv:2606.17994) [src: abstract].
- **Status date:** 2026-11-20

