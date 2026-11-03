# Models of dark energy

Scope: the dark-energy model landscape within general relativity, one card per model or class, chosen by literature weight; formalism in `formalism.md`, model-independent results in `results.md`.

Snapshot: 2026-11-03

## Quintessence
<!-- key: quintessence -->

### Exponential quintessence
<!-- key: exponential-quintessence -->
- **Defining equations:** $V(\phi)=V_{0}e^{-\kappa\lambda\phi}\,.$ (arXiv:hep-th/0603057) [src: Eq. 191].
- **Parameters:** the slope λ.
- **Predictions:** late-time attractor field-dominated with $w_{\rm eff}=w_{\phi}=-1+\lambda^{2}/3$, accelerating for $\lambda^{2}<2$ (arXiv:hep-th/0603057) [src: Sect. VI.2.1, inline, text after Eq. 196]; for λ² > 3γ a scaling attractor that does not accelerate [src: Table I; Sect. VI.2.1]. Two fields with double-exponential potentials emulate one field with a shallower potential, so that fields that "individually cannot drive cosmic acceleration" can collectively do so (Alestas et al., arXiv:2510.21627) [src: abstract].
- **Consistency:** single-field exponential quintessence is the main string-theory route reviewed by Andriot (arXiv:2603.25797) [src: abstract]; the proposed swampland criterion |∇V| ≥ c·V "forbids dS vacua" (arXiv:1806.08362) [src: abstract]; reply: none found in this run (see `thcosmo-fundamental-theory`).
- **Observational status:** two-field model with Planck 2018 shift parameters, DESI DR2 BAO and DES Y5 SN Ia: Δln B ∼ 4 against flat ΛCDM, "moderate evidence against the latter", with both slopes close to 1 (arXiv:2510.21627) [src: abstract].
- **Status date:** 2026-11-03

### Inverse power-law (tracker) quintessence
<!-- key: inverse-power-law-tracker-quintessence -->
- **Defining equations:** $V(\phi)=\frac{M^{4+\alpha}}{\phi^{\alpha}}\,,$ the potential of the original quintessence models (arXiv:hep-th/0603057) [src: Eq. 112].
- **Parameters:** M and α.
- **Predictions:** tracker solutions insensitive to initial conditions (arXiv:astro-ph/9812313) [src: abstract]; freezing behaviour, "initially w>-1 and w'<0", as the field slows (arXiv:astro-ph/0505494) [src: text after Fig. 1; Fig. 2 caption].
- **Consistency:** trackers depend sensitively on the shape of the potential over the whole field range (arXiv:0712.3450) [src: Sect. V]; reply: none found.
- **Observational status:** not assessed in a paper read this run. Freezing fields evolve towards "w→-1, w'→0" as they are critically damped (arXiv:astro-ph/0505494) [src: text after Fig. 1], while thawing fields start at w ≈ −1 and move away from it (see `open-questions.md` for the thawing debate).
- **Status date:** 2026-11-03

### Thawing quintessence (monomial, PNGB / axion)
<!-- key: thawing-quintessence-monomial-pngb-axion -->
- **Defining equations:** thawing potentials analysed by Caldwell & Linder: V = M^{4−n}φ^n, exponential, and the PNGB V = M⁴cos²(φ/2f) (arXiv:astro-ph/0505494) [src: text after Fig. 1].
- **Parameters:** the scale and shape of V; the initial field value; for the PNGB the decay constant f.
- **Predictions:** w starts at −1 and grows, w' > 0 (arXiv:astro-ph/0505494) [src: text after Fig. 1]; for a field kept below the Planck scale ($E<M_{P}$) and Ω_de ≈ 0.7, thawing models must satisfy 1 + w ≳ 0.004, which "may be the limit of quintessence" (arXiv:astro-ph/0505494) [src: abstract; inline, text after Fig. 2]; for nearly flat potentials a universal w(a) (arXiv:0712.3450) [src: abstract].
- **Consistency:** Caldwell & Linder leave out the PNGB with f ≪ M_P "since the field rapidly evolves to w→0 unless the initial conditions are finely tuned" (arXiv:astro-ph/0505494) [src: text after Fig. 1]. Shiu, Tonioni & Tran derive an analytic bound on the axion mass and decay constant which, combined with proposed quantum-gravity constraints, pushes the masses "much larger than the Hubble scale, in tension with basic models of axion quintessence" (arXiv:2604.09141) [src: abstract]; reply: none found.
- **Observational status:** disputed. Payeur et al. find a preference over Λ only "if we use priors which are heavily informed by the data itself", and "if we extend the priors to physically better motivated ranges, the evidence for thawing quintessence disappears" (DESI BAO, Planck 2018, Pantheon+ or DES SN) (arXiv:2411.13637, v4) [src: abstract]. Shlivko finds thawing "consistently preferred" with DESI DR2, Planck+ACT and any major SN compilation, not sensitive to the prior but "contingent on the inclusion of supernovae" (arXiv:2512.20832) [src: abstract]. With non-zero curvature, thawing quintessence fits the data as well as $w_0w_a$ in a flat background (Dinda & Maartens, arXiv:2504.15190) [src: abstract].
- **Status date:** 2026-11-03

### Kinetically mixed axion–dilaton quintessence (KMIX)
<!-- key: kinetically-mixed-axion-dilaton-quintessence -->
- **Defining equations:** an axion-like field coupled exponentially to a dilaton-like field, string-motivated (Toomey et al., arXiv:2511.23463) [src: abstract]; the Lagrangian was not read this run.
- **Parameters:** not read.
- **Predictions:** KMIX "can appear phantom in a standard Chevallier-Polarski-Linder (CPL) based analysis", and "may account for the DESI preference without invoking true phantom behavior" (arXiv:2511.23463) [src: abstract].
- **Consistency:** none found.
- **Observational status:** Planck + DESI DR2 BAO: support at 2.5σ against 3.1σ for the CPL fit; with SN above 3σ for Union3 and DES Y5, 2.1σ with Pantheon+, 1.7σ adding DESI full-shape power spectrum and bispectrum (arXiv:2511.23463) [src: abstract].
- **Status date:** 2026-11-03

## Non-canonical and phantom models
<!-- key: non-canonical-and-phantom-models -->

### k-essence (attractor k-essence)
<!-- key: k-essence-attractor-k-essence -->
- **Defining equations:** $S=\int{\rm d}^{4}x\sqrt{-g}\,p(\phi,X)\,,$ with $p(\phi,X)=f(\phi)\hat{p}(X)\,.$ (arXiv:hep-th/0603057) [src: Eqs. 115–116].
- **Parameters:** the functions f and $\hat{p}$.
- **Predictions:** an attractor tracks radiation and makes k-essence behave as a cosmological constant at the onset of matter domination, overtaking matter "at about the present epoch" (Armendariz-Picon et al., arXiv:astro-ph/0006373) [src: abstract]; sound speed $c_{s}^{2}\equiv\frac{p_{,X}}{\rho_{,X}}$, which may differ from one (arXiv:hep-th/0603057) [src: Eq. 147].
- **Consistency:** stability needs $\xi_1>0$, $\xi_2\geq 0$ (arXiv:hep-th/0603057) [src: Eq. 145]; for $p=-X+X^2$, at X ≥ 1/2 "the system is completely stable at the quantum level", but the small dark-energy density gives $|X|\gg X^2$, "in which case one can not ensure the stability of quantum fluctuations" [src: Sect. V.5, text after Eq. 147]. Reply: none found in this run.
- **Observational status:** no dedicated 2025–2026 constraint read in this run.
- **Status date:** 2026-11-03

### Chaplygin gas (unified dark matter–dark energy fluid)
<!-- key: chaplygin-gas-unified-dark-matter-dark-energy -->
- **Defining equations:** $p=-\frac{A}{\rho}\,,$ (arXiv:hep-th/0603057) [src: Eq. 151]; $\rho=\sqrt{A+\frac{B}{a^{6}}}\,,$ [src: Eq. 152].
- **Parameters:** A > 0 and the integration constant B.
- **Predictions:** dust at early times, cosmological constant at late times (arXiv:hep-th/0603057) [src: Eqs. 153–154]; "an increasing value for the effective cosmological constant" (arXiv:gr-qc/0103004) [src: abstract].
- **Consistency:** none found in this run.
- **Observational status:** not assessed with a paper read this run.
- **Status date:** 2026-11-03

### Phantom scalar field
<!-- key: phantom-scalar-field -->
- **Defining equations:** Lagrangian $p=-X-V(\phi)$ (arXiv:hep-th/0603057) [src: Sect. V.5, text after Eq. 147]; ε = −1 in Eqs. 179–189 [src: Eq. 179].
- **Parameters:** the potential V.
- **Predictions:** w < −1 (arXiv:astro-ph/9908168) [src: abstract]; a Big Rip in finite time for a phantom density that grows without bound (arXiv:astro-ph/0302506) [src: abstract].
- **Consistency:** quantum-mechanically unstable ghost (arXiv:hep-th/0603057) [src: Sect. V.5]; bounds on the cutoff of a ghost effective theory, "assuming only that ghosts interact at least gravitationally", Λ < 3 MeV (arXiv:hep-ph/0311312) [src: abstract]; reply: a negative kinetic term "does not necessarily lead to inconsistencies" with suitable higher-order kinetic terms (ghost condensate) (arXiv:hep-th/0603057) [src: Sect. V.5, text after Eq. 147].
- **Observational status:** in GR a phantom equation of state is "unphysical" and the DESI crossing is "an artifact of a parametrization", per Dinda & Maartens (arXiv:2504.15190) [src: abstract]; see `open-questions.md`.
- **Status date:** 2026-11-03

### Two-field Quintom
<!-- key: two-field-quintom -->
- **Defining equations:** $S=\int d^{4}x\sqrt{-g}\left[-\frac{1}{2}\nabla_{\mu}\phi\nabla^{\mu}\phi+\frac{1}{2}\nabla_{\mu}\sigma\nabla^{\mu}\sigma-V(\phi,\sigma)\right].$ (Ren et al., arXiv:2606.01360) [src: Eq. 11].
- **Parameters:** the potential $V(\phi,\sigma)$ and initial conditions.
- **Predictions:** crossing of w = −1 in either direction (arXiv:2606.01360) [src: text before Eq. 1]. Goh & Taylor realise a phantom-to-quintessence crossing "naturally" with hill-top or cliff-face potentials bounded from above, a tanh potential reproducing the crossing "although such models can suffer from fine-tuning effects" (arXiv:2509.12335) [src: abstract]. With an exponential quintessence and an inverse power-law phantom, the late-time attractor is phantom-dominated and the crossing is "gradual and asymptotic" (Thanankullaphong et al., arXiv:2601.02284) [src: abstract].
- **Consistency:** the σ field is a ghost (opposite kinetic sign in Eq. 11), with the quantum instability of the phantom card; reply: none found in this run.
- **Observational status:** moderate preference for dynamical dark energy with Pantheon+, compressed CMB priors, DESI DR2 BAO and DES Y5 (arXiv:2601.02284) [src: abstract].
- **Status date:** 2026-11-03

## Interacting dark energy
<!-- key: interacting-dark-energy -->

### Coupled dark fluids and the interacting vacuum
<!-- key: coupled-dark-fluids-and-the-interacting-vacuum -->
- **Defining equations:** ${\rho}_{\rm de}^{\prime}+3\mathcal{H}(1+w)\rho_{\rm de}=aQ,$ and ${\rho}_{\rm c}^{\prime}+3\mathcal{H}\rho_{\rm c}=-aQ,$ (arXiv:2606.21826) [src: Eqs. 3–4], with $Q=\beta H_{0}\rho_{\rm c},\qquad Q=\beta H_{0}\rho_{\rm de}.$ [src: Eq. 6] or the H-proportional forms of Eq. 5; the interacting vacuum has w = −1.
- **Parameters:** the coupling β (sign convention of the paper), w, and the kernel.
- **Predictions:** an apparent phantom crossing in $w_{\rm de}^{\rm eff}$ (arXiv:2606.21826) [src: Eq. 9; Sect. III.1]. For the constant-w model with Q = βH₀ρ_de, the effective equation of state resembles $w_0w_a$CDM and crosses the phantom divide (Li et al., arXiv:2610.30784) [src: abstract].
- **Consistency:** large-scale early-time instability for constant w and Q ∝ ρ_c (arXiv:0804.0232) [src: abstract; Sect. III, Eq. 38]; reply: for Q ∝ ρ_c "the divergence does not exist when ω_d < −1", and for Q ∝ ρ_de the system is "stable for any constant ω_d < −1" but "could become unstable in the observationally allowed range ω_d > −1 when the interaction parameter is ξ₂ ∼ 1" (arXiv:1603.08299, Sect. 4.2), and the ePPF treatment (arXiv:2606.21826, Sect. III.1). Sign-switching fits that send energy from dark energy to dark matter at low redshift come with "negative dark energy densities in the past, which may be unphysical" (Figueruelo et al., arXiv:2601.03122) [src: abstract].
- **Observational status:** Q = βH₀ρ_de with SPT + DESI DR2 + DES Y5: β = −0.4170 ± 0.1220, a 3.4σ deviation from zero, weakening to 2.1σ with Pantheon+ (Li et al., arXiv:2510.11363) [src: abstract]. Constant w with the same kernel and CMB + DESI + DES-Dovekie: $\beta=-2.52^{+0.80}_{-0.54}$ and $w=-1.510^{+0.170}_{-0.120}$, 3.2σ and 3.0σ from β = 0 and w = −1 (arXiv:2610.30784) [src: abstract]. Non-parametric β(z) for the interacting vacuum changes sign, ∼2σ from ΛCDM at high redshift, low-redshift results depending on the SN sample, $\ln\mathcal{B} = 5.98 \pm 0.69$ for CMB + DESI DR2 + DES Y5 (Li & Zhang, arXiv:2506.18477) [src: abstract]. Interacting extensions of CPL and JBP keep an early phantom phase but reduce the significance of excluding w = −1 (arXiv:2606.21826) [src: Sect. III.1].
- **Status date:** 2026-11-03

### Coupled quintessence
<!-- key: coupled-quintessence -->
- **Defining equations:** exponential potential and linear coupling to matter (Amendola, arXiv:astro-ph/9908023) [src: abstract]; the Lagrangian was not transcribed in this run.
- **Parameters:** the slope of the potential and the coupling β.
- **Predictions:** a φMDE during matter domination; large-angle tilt of the CMB spectrum, shifted and rescaled acoustic peaks, lower $\sigma_8$ (arXiv:astro-ph/9908023) [src: abstract]. An apparent phantom crossing appears when a coupled dark sector is analysed assuming separate conservation (arXiv:2606.21826, Sect. III.1). A technically natural axion–WIMP realisation transfers energy from dark energy to dark matter at late times and yields an apparent crossing "without ghosts or violation of the null-energy condition", with percent-level suppression of growth (Delaunay et al., arXiv:2607.28721) [src: abstract].
- **Consistency:** a direct axion–WIMP coupling "would ordinarily radiatively destabilize the ultralight axion potential", avoided by a $\mathbb{Z}_N$ symmetry (arXiv:2607.28721) [src: abstract]; reply: none found.
- **Observational status:** 1999 data gave $\vert\beta\vert\leq 0.1$ (arXiv:astro-ph/9908023) [src: abstract]; post-DESI constraints in the β–α plane are shown in arXiv:2606.21826, Fig. 4, without a number transcribed here.
- **Status date:** 2026-11-03

## Early dark energy
<!-- key: early-dark-energy -->

Status as an H0 solution: `thcosmo-tensions-model-building` (planned). The cards give the theory and the consistency issues.

### Axion-like early dark energy
<!-- key: axion-like-early-dark-energy -->
- **Defining equations:** $V(\theta)=m^{2}f^{2}[1-\cos(\theta)]^{n},$ (arXiv:2302.09032) [src: Eq. 6].
- **Parameters:** m, f, n and $\theta_i$; "it is now conventional to trade" m and f for $z_c$ and $f_{\rm EDE}(z_c)$ (arXiv:2302.09032) [src: Sect. III.1].
- **Predictions:** a component that does not dilute before $a_c$ and dilutes as $a^{-3(1+w_f)}$ after (arXiv:2302.09032) [src: Eq. 21; Sect. IV.1].
- **Consistency:** the potential is "a toy potential" that "may be generated by higher-order instanton corrections that require fine-tuning to cancel the leading contributions, or through the interaction of an axion and a dilaton and is therefore non-generic" (arXiv:2302.09032) [src: Sect. III.1]; generating it from an instanton expansion with the leading terms vanished "is generically hard to achieve" [src: Sect. VII.2]; near-Planckian field excursions "may run into problems with the weak-gravity conjecture", and, "for models not protected by approximate shift-symmetries like the axion-like model", radiative corrections bring $\phi^2$ terms that spoil the dilution unless, for one example, $m_b/m_a\lesssim 10^{-4}$ [src: Sect. VII.2, footnote 26]; a "why then" coincidence problem [src: Sect. VII.1]. Reply: a string-theory embedding has model-building challenges "not particularly different" from those of inflation, dark energy or fuzzy dark matter (as summarised in arXiv:2302.09032) [sec: Sect. III.1].
- **Observational status:** SPT + ACT + Planck: $f_{\rm EDE}<0.070$ at 95% CL; adding DESI: $f_{\rm EDE}\,=\, 0.055^{+0.024}_{-0.047}$ at 68% CL, a "weak preference", the shift being "a manifestation of the discrepancy currently present between DESI and CMB experiments" in ΛCDM (SPT-3G D1, arXiv:2507.23355) [src: abstract]. Details: `thcosmo-tensions-model-building`.
- **Status date:** 2026-11-03

### New early dark energy (cold and hot NEDE)
<!-- key: new-early-dark-energy-cold-and-hot-nede -->
- **Defining equations:** $V(\psi,\phi)=\frac{\lambda}{4}\psi^{4}+\frac{1}{2}\beta M^{2}\psi^{2}-\frac{1}{3}\alpha M\psi^{3}+\frac{1}{2}m^{2}\phi^{2}+\frac{1}{2}\gamma\phi^{2}\psi^{2}.$ (arXiv:2302.09032) [src: Eq. 10].
- **Parameters:** couplings λ, β, α, γ, masses M and m; phenomenologically $f_{\rm NEDE}(z_*)$ (arXiv:2302.09032) [src: Sect. III.4].
- **Predictions:** a first-order phase transition with a short percolation phase; the trigger sets the initial conditions of the decaying NEDE fluid (arXiv:2302.09032) [src: Sect. III.4]. Hot NEDE with dark SU(N) → SU(N−1) breaking, a dark-matter multiplet interacting with dark radiation, and "dark radiation matter decoupling" (Garny et al., arXiv:2508.03795) [src: abstract].
- **Consistency:** none found in this run.
- **Observational status:** the hot NEDE–DRMD authors report agreement with SH0ES at 1.4σ against 5.7σ in ΛCDM with Planck 2018, Pantheon+ and DESI DR2 BAO (arXiv:2508.03795) [src: abstract]; not independently assessed here.
- **Status date:** 2026-11-03

## Phenomenological classes
<!-- key: phenomenological-classes -->

Chosen by their weight in the CosmoVerse white paper (arXiv:2504.01669, v3, Sects. 4.2.1.c–f and 4.2.2); a long zoo is left to it.

### Holographic dark energy
<!-- key: holographic-dark-energy -->
- **Defining equations:** the infrared cut-off of the holographic energy is the size of the future event horizon (Li, arXiv:hep-th/0403127) [src: abstract]; the rendering carries no equation numbers and the density formula was not transcribed.
- **Parameters:** the holographic constant c of the paper.
- **Predictions:** with $\Omega_\Lambda=0.73$ as input, w = −0.90 today (arXiv:hep-th/0403127) [src: abstract]; with the Hubble or particle horizon as cut-off the model does not accelerate, which is why the event horizon is chosen (arXiv:hep-th/0403127) [src: text before the causality discussion].
- **Consistency:** the event horizon depends on the future evolution of a(t), so the model "appears" to violate causality; Li argues the horizon is defined globally (arXiv:hep-th/0403127) [src: causality paragraph]. Reply in the literature: none read in this run.
- **Observational status:** not assessed with a paper read in this run; see arXiv:2504.01669, Sect. 4.2.1.c.
- **Status date:** 2026-11-03

### Running vacuum models
<!-- key: running-vacuum-models -->
- **Defining equations:** $\rho_{\rm vac}(H)=\frac{3}{8\pi G}(c_{0}+\nu H^{2}+\tilde{\nu}\dot{H})+\mathcal{O}(H^{4})\,.$ (CosmoVerse, arXiv:2504.01669) [src: Eq. 4.11].
- **Parameters:** ν and $\tilde\nu$, "expected to be ≲ O(10⁻⁴–10⁻²)" from the masses and non-minimal couplings of the fields, "ultimately determined from observations"; the most recent constraints it cites use "the simplified assumption" $\tilde{\nu}=\nu/2$ (arXiv:2504.01669) [src: Sect. 4.2.1.e, inline, text after Eq. 4.11].
- **Predictions:** a time-varying vacuum energy implies non-conservation of matter or a time-varying G; the $O(H^4)$ terms can drive inflation (arXiv:2504.01669) [src: Sect. 4.2.1.e].
- **Consistency:** motivated by renormalisation-group arguments in curved spacetime and by adiabatic regularisation in QFT in curved spacetime (arXiv:2504.01669) [src: Sect. 4.2.1.e]; Martin's renormalised flat-space vacuum energy (arXiv:1205.3365, Eq. 515) is the comparison point. Reply: none found in this run.
- **Observational status:** the white-paper section states that RVMs "accommodate the wealth of cosmological data" and that coupling to dark matter or a running G can loosen the growth and H0 tensions (arXiv:2504.01669) [src: Sect. 4.2.1.e] — a claim of the RVM authors, not checked here.
- **Status date:** 2026-11-03

### Phenomenologically emergent dark energy (PEDE)
<!-- key: phenomenologically-emergent-dark-energy-pede -->
- **Defining equations:** not transcribed in this run; dark energy "has no effective presence in the past and emerges at the later times", with zero extra degrees of freedom (Li & Shafieloo, arXiv:1906.08275) [src: abstract].
- **Parameters:** none beyond ΛCDM.
- **Predictions:** w increases from $-\frac{2}{3 {\rm{ln}}\, 10} -1$ in the past to −1 in the future (arXiv:1906.08275) [src: abstract].
- **Consistency:** none found.
- **Observational status:** with a hard 2σ lower prior on $H_0$ from local measurements, Δχ²_bf ∼ −41.08 against ΛCDM (arXiv:1906.08275) [src: abstract]; the result is obtained "by setting a hard-cut 2σ lower bound prior for the H_0" [src: abstract].
- **Status date:** 2026-11-03

### Sign-switching cosmological constant ($\Lambda_{\rm s}$CDM) and negative dark-energy densities
<!-- key: sign-switching-cosmological-constant-lambda-rm -->
- **Defining equations:** a cosmological constant that switches sign at a redshift $z_\dagger$, from anti-de Sitter to de Sitter (Akarsu et al., arXiv:2108.09239) [src: abstract].
- **Parameters:** $z_\dagger$.
- **Predictions:** z† ≳ 1.1 for monotonic expansion when consistent with the CMB; H0 ≈ 74.5 km s⁻¹ Mpc⁻¹ for z† = 1.5 (arXiv:2108.09239) [src: abstract].
- **Consistency:** with a negative density, w = −1 stops being a global separator and the null-energy-condition boundary ρ_DE + p_DE = 0 is the meaningful criterion (Gökçen, Akarsu & Di Valentino, arXiv:2602.21169) [src: abstract]. Scalar-field realisations of sign-switching histories select the phantom branch; some prescribed histories have no ordinary classical one-field realisation, so "field-map existence, invertibility, and endpoint regularity must be assessed before interpreting a phenomenological history as scalar dynamics" (Adil et al., arXiv:2609.09261) [src: abstract].
- **Observational status:** Planck CMB + BAO: $z_\dagger=2.44\pm0.29$ (68% C.L.) (arXiv:2108.09239) [src: abstract]. CPL extensions with a negative-density phase are "statistically disfavored relative to the baseline CPL", but admitting such a phase "generally reduces the significance of deviations from a cosmological constant" (arXiv:2602.21169) [src: abstract].
- **Status date:** 2026-11-03

## Not verified
<!-- key: not-verified -->

- Tachyon, dilatonic ghost-condensate and assisted quintessence models (arXiv:hep-th/0603057, Sects. V.3, V.5, VIII.3): listed in the review, not carded.
- Emergent dark energy variants, vacuum metamorphosis and the other late-time models of arXiv:2504.01669, Sects. 4.2.1.f–h: not read.
- The 2025–2026 observational status of k-essence, Chaplygin gas, holographic dark energy and tracker quintessence: no dedicated paper read.
- Bound Dark Energy (arXiv:2601.08943) is cited in `results.md` from its abstract only; no card.
