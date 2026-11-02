# Models of primordial correlators

Scope: classes of inflationary models as sources of primordial correlators, one card per class, with the correlator each predicts; the inflationary dynamics, $n_s$ and $r$ of each model live in `thcosmo-inflation`.

Snapshot: 2026-11-02

The classes are those around which the reviews of this skill organise the bispectrum (Chen 2010, arXiv:1002.1416, Sects. 6–8; Achúcarro et al. 2022, arXiv:2203.08128, Sect. 3.1). Measured $f_{\rm NL}$ values belong to cosmoskill `cosmo-inflation-primordial`; they are quoted here only for a model's status.

## Single-field models
<!-- key: single-field-models -->

### Canonical single-field slow-roll inflation
<!-- key: canonical-single-field-slow-roll-inflation -->
- **Defining equations:** $S_{2}=\int dtd^{3}x~\left[a^{3}\epsilon\dot{\zeta}^{2}-a\epsilon(\partial\zeta)^{2}\right]~$ for the comoving curvature perturbation, in units of the reduced Planck mass (Chen 2010, arXiv:1002.1416) [src: Eq. 4.8]; the covariant action of that paper is printed with a slip (formalism.md, "Not verified").
- **Parameters:** the Hubble rate $H$ and the Hubble-flow parameters $\epsilon$ and $\eta$ of Chen 2010, arXiv:1002.1416 [src: Eq. 4.2], all evaluated at horizon exit [src: Sect. 4, text after Eq. 4.18].
- **Predictions:**
  - $P_{\zeta}=\frac{H^{2}}{8\pi^{2}\epsilon}~$ (arXiv:1002.1416) [src: Eq. 4.18]; full bispectrum shape in formalism.md (arXiv:1002.1416) [src: Eqs. 4.22–4.23]. <!-- num: not a value -->
  - Squeezed limit fixed by the tilt (Creminelli & Zaldarriaga 2004, arXiv:astro-ph/0407059) [src: Eq. 1].
- **Consistency:** the squeezed-limit bispectrum predicted by the model produces no primordial signal in the squeezed CMB bispectrum or in scale-dependent halo bias, only projection effects (Pajer et al. 2013, arXiv:1305.0824) [src: abstract]; reply: none found.
- **Observational status:** consistent with Gaussian initial conditions; Planck 2018 temperature and E-mode bispectra give $f_{\rm NL}^{\rm local}=-0.9\pm 5.1$ at 68% CL, statistical (arXiv:1905.05697) [src: abstract].
- **Status date:** 2026-11-02

### Small sound speed (EFT of inflation, DBI and P(X) models)
<!-- key: small-sound-speed-eft-of-inflation-dbi-and-p-x -->
- **Defining equations:** the Goldstone action $S_{\rm\pi}=\int\!d^{4}x\>\sqrt{-g}\left[-\frac{M^{2}_{\rm Pl}\dot{H}}{c^{2}_{s}}\left(\dot{\pi}^{2}-c^{2}_{s}\frac{(\partial_{i}\pi)^{2}}{a^{2}}\right)+M_{\rm Pl}^{2}\dot{H}\left(1-\frac{1}{c^{2}_{s}}\right)\left(\dot{\pi}^{3}-\dot{\pi}\frac{(\partial_{i}\pi)^{2}}{a^{2}}\right)-\frac{4}{3}M_{3}^{4}\dot{\pi}^{3}...\right]$ (Cheung et al. 2007, arXiv:0709.0293) [src: Eq. 39].
- **Parameters:** $c_{s}$ (equivalently $M_{2}^{4}$, through Eq. 38) and $M_{3}^{4}$ at leading order in slow roll and derivatives; four more slow-variation parameters at first order in slow roll (arXiv:0709.0293) [src: Sect. 4.2, text after Eq. 48]. <!-- num: not a value -->
- **Predictions:** equilateral-type bispectrum with $f_{\rm NL}^{\rm equil.}=\frac{85}{324}\cdot\frac{1}{c_{s}^{2}}\;$ from $\dot{\pi}(\nabla\pi)^{2}$ at leading order in $c_{s}^{-1}$ (arXiv:0709.0293) [src: Eq. 45]; in DBI inflation $M_{3}^{4}\sim M_{\rm Pl}^{2}|\dot{H}|c_{s}^{-4}$, so the $\dot{\pi}^{3}$ contribution is of the same order (arXiv:0709.0293) [src: Sect. 4.2, inline, text after Eq. 44].
- **Consistency:** the Goldstone self-interactions become strongly coupled at $\Lambda^{4}\simeq 16\pi^{2}M_{2}^{4}\frac{c_{s}^{7}}{(1-c_{s}^{2})^{2}}\simeq 16\pi^{2}M_{\rm Pl}^{2}|\dot{H}|\frac{c_{s}^{5}}{1-c_{s}^{2}}\;$ (arXiv:0709.0293) [src: Eq. 50]; superluminal $c_{s}$ would imply no Lorentz-invariant UV completion (arXiv:0709.0293) [src: Sect. 4.2, text after Eq. 38]; reply: none needed for $c_{s}\leq 1$, the case the paper treats. <!-- num: not a value -->
- **Observational status:** constrained, not detected. Planck 2018 gives $c_{\mathrm{s}}^{\rm DBI}\geq\ 0.086$ at 95% from T+E bispectra (arXiv:1905.05697) [src: Eq. 59]. With the Open EFToI and the Modal pipeline on Planck data, $c_s \geq 0.38$ at 95% CL, marginalised over a dissipation scale bounded by $γ\leq 384\,H$ (Agüí Salcedo et al. 2026, arXiv:2603.13473) [src: abstract].
- **Status date:** 2026-11-02

### Excited (non-Bunch–Davies) initial states
<!-- key: excited-non-bunch-davies-initial-states -->
- **Defining equations:** an excited initial state built over the Bunch–Davies state, treated with effective field theory in an expanding universe (Holman & Tolley 2008, arXiv:0710.1302) [src: abstract]; the Bunch–Davies mode function it departs from is $u_{k}=u({\bf k},\tau)=\frac{iH}{\sqrt{4\epsilon k^{3}}}(1+ik\tau)e^{-ik\tau}~$ (Chen 2010, arXiv:1002.1416) [src: Eq. 4.14].
- **Parameters:** the occupation of the excited modes and the time at which the state is set (arXiv:0710.1302) [src: abstract]. <!-- num: not a value -->
- **Predictions:** bispectrum enhancement, parametrically larger than the standard one, most pronounced for flattened triangles with two collinear momenta, even for Hadamard states (arXiv:0710.1302) [src: abstract]; resonant features can also arise from certain non-Bunch–Davies vacua (Achúcarro et al. 2022, arXiv:2203.08128) [src: Sect. 4.1].
- **Consistency:** the folded-enhanced region is cutoff-regulated with a power-law width (Yang & Philcox 2026, arXiv:2607.15337) [src: abstract]; the Bunch–Davies initial condition is the one that is Hermitian analytic and underlies the cosmological cutting rules (arXiv:2203.08121) [src: Sect. 3.1], so the bootstrap rules derived from it do not apply as such [der]; reply: none found.
- **Observational status:** no dedicated detection; the orthogonal template peaks in folded configurations and serves as a proxy (arXiv:2203.08128) [src: Sect. 3.1, text after Fig. 4]; galaxy-bispectrum sensitivity to folded shapes is a **forecast** (arXiv:2607.15337) [src: abstract].
- **Status date:** 2026-11-02

## Multi-field models
<!-- key: multi-field-models -->

### Curvaton and other local-type multi-field models
<!-- key: curvaton-and-other-local-type-multi-field-models -->
- **Defining equations:** an extra light field, not the inflaton, determines or contributes to the curvature perturbation, isocurvature perturbations being transferred to curvature on superhorizon scales; in the curvaton model the curvaton decay fraction is $r_{\rm D}=[3\rho_{\rm curv}/(3\rho_{\rm curv}+4\rho_{\rm rad})]_{\rm D}$ at decay, in the sudden-decay approximation (Planck 2018 IX, arXiv:1905.05697) [src: Sect. 2.2, inline, text after Eq. 3].
- **Parameters:** $r_{\rm D}$ for the minimal adiabatic curvaton with a quadratic potential (arXiv:1905.05697) [src: Sect. 2.2]. <!-- num: not a value -->
- **Predictions:** a local-type bispectrum, peaked in squeezed configurations (arXiv:1905.05697) [src: Sect. 2.2]; in the minimal adiabatic curvaton scenario $f_{\rm NL}^{\rm local}=(5/4r_{\mathrm{D}})-5r_{\mathrm{D}}/6-5/3$ (arXiv:1905.05697) [src: Sect. 2.2, inline, text after Eq. 3], so that significant non-Gaussianity requires low $r_{\rm D}$ [src: Sect. 2.2]. The non-Gaussianity of these models arises from evolution outside the horizon, the second class of Babich et al. (arXiv:astro-ph/0405356) [src: abstract].
- **Consistency:** Ullah 2026 states that a violation of the scalar soft theorem would rule out all attractor single-field models and point to multi-field dynamics or a non-attractor phase (arXiv:2604.09765) [src: abstract]; the local shape is the multi-field signal of that statement [der]; reply: none found. The δN computation of these predictions belongs to `thcosmo-cosmological-perturbations`.
- **Observational status:** constrained, not detected: $f_{\rm NL}^{\rm local}=-0.9\pm 5.1$ at 68% CL, statistical, from Planck 2018 temperature and E-mode bispectra (arXiv:1905.05697) [src: abstract]; the updated curvaton limits of that paper's Sect. 8 were not read.
- **Status date:** 2026-11-02

### Quasi-single-field inflation and massive-particle exchange (cosmological collider)
<!-- key: quasi-single-field-inflation-and-massive -->
- **Defining equations:** massive fields of mass of order H coupled to the inflaton, for example through a turning trajectory (Chen & Wang 2009, arXiv:0911.3380) [src: abstract]; mass parameter $\mu=\sqrt{m^{2}/H^{2}-9/4}$ (Achúcarro et al. 2022, arXiv:2203.08128) [src: Sect. 3.1, inline, text after Eq. 3.7]; exchange bispectrum of Eq. 3.8 of that review (formalism.md, "Cosmological collider").
- **Parameters:** mass, spin, couplings $\lambda_{s}$ (arXiv:2203.08128) [src: Sect. 3.1, text after Eq. 3.8]; in the eight-parameter multi-field likelihood of Philcox 2026, masses in the complementary and principal series, mixings and sound speeds (arXiv:2607.18369) [src: abstract]. <!-- num: not a value -->
- **Predictions:**
  - shapes between local and equilateral, and trispectra with $t_{\rm NL}$ possibly much larger than $f_{\rm NL}^{2}$ (arXiv:0911.3380) [src: abstract];
  - squeezed limit $S\sim q^{\frac{1}{2}+\mathrm{i}\mu}P_{s}(\cos\theta)$ and amplitude $f_{\mathrm{NL}}^{\mathrm{ex}}\sim\varepsilon\mu^{n}\mathrm{e}^{-\pi\mu}$ at weak coupling (arXiv:2203.08128) [src: Sect. 3.1, inline, text after Eq. 3.8];
  - at strong mixing, only half the usual Boltzmann suppression (arXiv:2608.23243) [src: abstract]. <!-- num: not a value -->
- **Consistency:** the amplitudes are bounded by perturbativity and unitarity, and the weak-mixing assumption of most studies is incompatible with current data except at the smallest masses (Philcox 2026, arXiv:2607.18369) [src: abstract]; reply: strong-mixing calculations (arXiv:2608.23243) [src: abstract]. Large-N_f embeddings make an almost-local squeezed limit generic, so an enhanced squeezed limit with few fields is fine-tuned (arXiv:2609.37570) [src: abstract]. <!-- num: not a value -->
- **Observational status:** not detected. Planck Modal searches with orthogonalised collider templates find a maximum of $2.35σ$ for massive spin-0 exchange after the look-elsewhere effect (Suman et al. 2025, arXiv:2512.22085) [src: abstract], quoted as $2.4σ$ in the companion letter, with spin-1 and spin-2 peaking near 2σ (arXiv:2511.17500) [src: abstract]; a joint Bayesian analysis of single, double and triple exchange finds Planck constraints much tighter than the theoretical bounds and no evidence for new physics, with a maximal $χ^2$ improvement of $5.3$ (Philcox 2026, arXiv:2607.18369) [src: abstract].
- **Status date:** 2026-11-02

## Feature models
<!-- key: feature-models -->

### Sharp features (steps, sudden turns, sudden changes of sound speed)
<!-- key: sharp-features-steps-sudden-turns-sudden -->
- **Defining equations:** a transient departure of a background quantity from slow roll; template $\delta\Delta_{\mathcal{R}}^{2}(k)=f(k)\hskip 1.0pt\cos(2k/k_{0}+\phi)$ (Achúcarro et al. 2022, arXiv:2203.08128) [src: Sect. 4.1, inline, text after Eq. 4.1].
- **Parameters:** envelope f(k), feature scale $k_{0}$, phase φ (arXiv:2203.08128) [src: Sect. 4.1]; for step potentials, the step height and width (arXiv:astro-ph/0611645) [src: abstract]. <!-- num: not a value -->
- **Predictions:** an oscillation in the power spectrum and a bispectrum with non-trivial shape and scale dependence, far larger than in slow roll and correlated with the 2-point feature (Chen, Easther & Lim 2006, arXiv:astro-ph/0611645) [src: abstract].
- **Consistency:** the renormalised one-loop power spectrum of a localised feature vanishes at large and small scales, so feature models used to fit CMB residuals are consistent with perturbativity bounds (Braglia, Céspedes & Pinol 2026, arXiv:2603.12216) [src: abstract]; reply: none found.
- **Observational status:** no detection. In Planck PR3 and PR4, several frequencies improve the fit by up to Δχ² ≃ −10 to −15, not supported by Bayesian model comparison, with global significance at most $2.6σ$ after the look-elsewhere effect (Raffaelli et al. 2026, arXiv:2605.30236) [src: abstract]. DESI DR1 power spectrum and bispectrum bound linear oscillations to $A_{\rm lin}<0.033$ at 95% CL marginalising over ΛCDM (Chen et al. 2026, arXiv:2610.10530) [src: abstract].
- **Status date:** 2026-11-02

### Resonant features (axion monodromy)
<!-- key: resonant-features-axion-monodromy -->
- **Defining equations:** monomial potentials over super-Planckian ranges with superimposed sinusoidal modulations from instantons (Flauger et al. 2009, arXiv:0907.2916) [src: abstract]; template $\delta\Delta_{\mathcal{R}}^{2}(k)\propto\cos(\Omega\log(2k)+\phi)$ (arXiv:2203.08128) [src: Sect. 4.1, inline, text after Eq. 4.1].
- **Parameters:** amplitude and frequency of the modulation, phase (arXiv:0907.2916) [src: abstract]. <!-- num: not a value -->
- **Predictions:** detectable modulations of the scalar power spectrum are commonplace in well-controlled string examples, while the resonant bispectrum is detectable in some classes and not in others (arXiv:0907.2916) [src: abstract]; the resonant bispectrum has essentially no overlap with the standard shapes (Flauger & Pajer 2010, arXiv:1002.0833) [src: abstract].
- **Consistency:** a superposition of $\mathcal{O}(10)$ resonant contributions can mimic an equilateral shape, but without oscillations in the 2-point function an equilateral signal above the Planck sensitivity would rule out a resonant origin (Gwyn, Rummel & Westphal 2012, arXiv:1211.0070) [src: abstract]; reply: none found. <!-- num: not a value -->
- **Observational status:** no detection. DESI DR1 bounds logarithmic oscillations to $A_{\rm log}<0.035$ at 95% CL marginalising over ΛCDM; with Planck 2018 cosmology fixed, a ≃ 3σ global preference for ω_log ≃ 15 appears and disappears once cosmology is varied, attributed by the authors to the DESI–Planck distance-scale tension (Chen et al. 2026, arXiv:2610.10530) [src: abstract].
- **Status date:** 2026-11-02
