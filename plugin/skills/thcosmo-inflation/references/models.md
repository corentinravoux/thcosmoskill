# Models of inflation

Scope: the inflationary model landscape, one card per model or class, chosen by literature weight; formalism in `formalism.md`, model-independent results in `results.md`.

Snapshot: 2026-11-02

The models are chosen by their weight in the Encyclopaedia Inflationaris (Martin, Ringeval & Vennin, arXiv:1303.3787), the Bayesian comparison of Planck 2018 X (arXiv:1807.06211, Table 5) and the 2025–2026 literature on the ACT DR6 spectral index. Its library ASPIC "presently supports 118 different models" (arXiv:1303.3787, v5) [src: abstract]; this file is not a zoo. Bayes factors $\ln B$ of Planck 2018 X are relative to the $R^{2}$ model, with "strongly disfavoured" meaning $\ln B<-5$ and an error of 0.3 on $\ln B$ (arXiv:1807.06211) [src: Table 5 caption]; they assume Planck 2018 with BK15, $w_{\rm int}$ fixed and the pivot $k=0.002$ Mpc⁻¹ [src: Sect. 4.2].

## Single-field models
<!-- key: single-field-models -->

### Starobinsky ($R+R^{2}$) inflation
<!-- key: starobinsky-r-r-2-inflation -->
- **Defining equations:** Einstein-frame potential $V\left(\phi\right)=M^{4}\left(1-e^{-\sqrt{\frac{2}{3}}\frac{\phi}{M_{\mathrm{g}}}}\right)^{2},$ (arXiv:1303.3787) [src: Eq. 72]; Planck 2018 X writes it $\Lambda^{4}\left(1-e^{-\sqrt{2/3}\phi/M_{\mathrm{Pl}}}\right)^{2}$ for $R+R^{2}/(6M^{2})$ (arXiv:1807.06211) [src: Table 5].
- **Parameters:** none besides the scale M, fixed by the CMB normalisation; zero-parameter model in the Encyclopaedia (arXiv:1303.3787, Sect. 4). For $\Delta N_{*}=55$ the normalisation gives $M\simeq 3.3\times 10^{-3}M_{\mathrm{g}}$ and a mass scale $\mu\simeq 10^{-5}M_{\mathrm{g}}\simeq 10^{13}\mathrm{GeV}$ (arXiv:1303.3787) [src: Sect. 4.1.3, text after Eq. 106].
- **Predictions:** with $x\equiv\phi/M_{\mathrm{g}}$, $\epsilon_{1}=\frac{4}{3}\left(1-e^{\sqrt{2/3}x}\right)^{-2},\qquad\epsilon_{2}=\frac{2}{3}\left[\sinh\left(\frac{x}{\sqrt{6}}\right)\right]^{-2},$ (arXiv:1303.3787) [src: Eq. 99]; inflation ends at $x_{\mathrm{end}}=\sqrt{\frac{3}{2}}\ln\left(1+\frac{2}{\sqrt{3}}\right)\simeq 0.94\,.$ (arXiv:1303.3787) [src: Eq. 100], but slow roll fails earlier, at $x_{\epsilon_{2}=1}=\sqrt{6}\,\arsinh\left(\sqrt{\frac{2}{3}}\right)\simeq 1.83\,.$ (arXiv:1303.3787) [src: Eq. 101]. Trajectory $N_{\mathrm{end}}-N=\frac{1}{2}\sqrt{\frac{3}{2}}\left(x_{\mathrm{end}}-x\right)+\frac{3}{4}\left(e^{\sqrt{\frac{2}{3}}x}-e^{\sqrt{\frac{2}{3}}x_{\mathrm{end}}}\right).$ (arXiv:1303.3787) [src: Eq. 103]. Lowest-order predictions $n_{\mathrm{s}}-1\simeq-\frac{2}{N}\thinspace,\quad r\simeq\frac{12}{N^{2}},$ (Planck 2018 X, arXiv:1807.06211) [src: Eq. 48], originally computed by Mukhanov & Chibisov and Starobinsky [src: Sect. 4.2].
- **Consistency:** the Hubble scale lies close to the unitarity bound on the scale of new physics, as for Higgs inflation (Burgess et al. 2009, arXiv:0902.4465) [src: abstract]. Couplings of the inflaton to matter, needed for reheating, shift $n_s$ and r through radiative corrections, while its self-interactions are of higher order in H and unimportant (Ellis et al. 2025, arXiv:2510.15137) [src: abstract]; reply: none found. String and supergravity embeddings: `thcosmo-fundamental-theory`.
- **Observational status:** reference model of Planck 2018 X, in good agreement with Planck 2018, with 49 < N_* < 59 at 95% CL compatible with the $R^{2}$ prediction N_* = 54 (arXiv:1807.06211) [src: Sect. 4.2]. After ACT DR6: on the 2σ boundary of P-ACT-LB for 50–60 e-folds (arXiv:2503.14454) [src: Sect. IV.4]; disfavoured at more than 2σ by CMB-SPA with DESI DR2 (arXiv:2512.05108) [src: abstract]; Ellis et al. find n_s = 0.958–0.963 for reheating temperatures between $100 - 10^{10}$ GeV, within the 95% CL region of Planck-ACT-SPT but below the 95% region of Planck-ACT-DESI, with near-instantaneous reheating improving the agreement (arXiv:2510.18656) [src: abstract]. See `open-questions.md` for the debate on the $n_s$ shift.
- **Status date:** 2026-11-02

### Higgs inflation (non-minimal coupling)
<!-- key: higgs-inflation-non-minimal-coupling -->
- **Defining equations:** Jordan-frame action of the Encyclopaedia's non-minimal class, $S\left(\bar{g}^{\mu\nu},\bar{\phi},\psi\right)=\frac{M_{\mathrm{g}}^{2}}{2}\int\mathrm{d}^{4}{\boldsymbol{x}}\sqrt{-\bar{g}}\left[F(\bar{\phi})\bar{R}-Z(\bar{\phi})\bar{g}^{\mu\nu}\partial_{\mu}\bar{\phi}\partial_{\nu}\bar{\phi}-2U(\bar{\phi})\right]+\int\mathrm{d}^{4}{\boldsymbol{x}}\,\mathcal{L}_{\mathrm{mat}}\left(\psi,\bar{g}_{\mu\nu}\right).$ (arXiv:1303.3787) [src: Eq. 123]; Planck 2018 X tests $\lambda^{4}\phi^{4}+\xi\phi^{2}R/2$ (arXiv:1807.06211) [src: Table 5].
- **Parameters:** the non-minimal coupling ξ; Planck 2018 X scans $-4<\log_{10}\xi<4$ (arXiv:1807.06211) [src: Table 5].
- **Predictions:** the Standard-Model Higgs with a non-minimal coupling to gravity can be the inflaton without a new particle (Bezrukov & Shaposhnikov 2008, arXiv:0710.3755) [src: abstract]; a reheating temperature T_reh ∼ 10^13 GeV is predicted, against $10^{9}$ GeV for $R^{2}$ (arXiv:1807.06211) [src: Sect. 4.2].
- **Consistency:** the Hubble scale is close to the unitarity bound on the cutoff of the effective theory (Burgess, Lee & Trott 2009, arXiv:0902.4465) [src: abstract]; reply: the cutoff depends on the background field and stays above the dynamical scales throughout inflation and reheating, but connecting inflationary and collider parameters requires assumptions on the UV completion (Bezrukov et al. 2010, arXiv:1008.5157) [src: abstract].
- **Observational status:** Δχ² = 0.4 and ln B = −2.4 relative to $R^{2}$ (Planck 2018 + BK15, arXiv:1807.06211) [src: Table 5]; disfavoured at more than 2σ, with Starobinsky, by CMB-SPA + DESI DR2 (arXiv:2512.05108) [src: abstract].
- **Status date:** 2026-11-02

### Large-field monomial potentials
<!-- key: large-field-monomial-potentials -->
- **Defining equations:** $V(\phi)=M^{4}\left(\frac{\phi}{M_{\scriptscriptstyle{\mathrm{Pl}}}}\right)^{p}.$ (arXiv:1303.3787) [src: Eq. 193].
- **Parameters:** the power p.
- **Predictions:** $\epsilon_{1}=\frac{p^{2}}{2x^{2}}\,,\qquad\epsilon_{2}=\frac{2p}{x^{2}}\,,\qquad\epsilon_{3}=\epsilon_{2}\,.$ with $x\equiv\phi/M_{\rm Pl}$ (arXiv:1303.3787) [src: Eq. 194]; the model lies on the line $\epsilon_{1}=(p/4)\epsilon_{2}$ (arXiv:1303.3787) [src: Sect. 5.2.2, inline, text after Eq. 194]; inflation ends at $x_{\mathrm{end}}=\frac{p}{\sqrt{2}}\,.$ (arXiv:1303.3787) [src: Eq. 197]; at the pivot $x_{*}^{2}=2p\left(\Delta N_{*}+\frac{p}{4}\right),$ (arXiv:1303.3787) [src: Eq. 200]. For $p=2$, Baumann gives $n_{\rm s}=1+2\eta_{\rm v}^{\star}-6\epsilon_{\rm v}^{\star}=1-\frac{2}{N_{\rm cmb}}\approx 0.96$ (boxed) (arXiv:0907.5424) [src: Eq. 242] and $r=16\epsilon_{\rm v}^{\star}=\frac{8}{N_{\rm cmb}}\approx 0.1$ [src: Eq. 243].
- **Consistency:** the field excursion is super-Planckian; the model stays under control only if $x_{\mathrm{ini}}=\dfrac{\phi_{\mathrm{ini}}}{M_{\scriptscriptstyle{\mathrm{Pl}}}}\lesssim\left(\frac{M_{\scriptscriptstyle{\mathrm{Pl}}}}{M}\right)^{4/p}.$ (arXiv:1303.3787) [src: Eq. 199]; flatness over a super-Planckian range must be controlled dynamically (arXiv:0907.5424) [src: Sect. 28.3]. Embeddings (monodromy): `thcosmo-fundamental-theory`.
- **Observational status:** p ≥ 2 strongly disfavoured relative to $R^{2}$, with ln B = −11.5 for φ² and −56.0 for φ⁴; p = 1 and p = 2/3 more compatible, with ln B = −3.9 and −4.6 (Planck 2018 + BK15, arXiv:1807.06211) [src: Table 5; Sect. 4.2]. BK18 strongly excludes monomial models with convex potentials; P-ACT allows slightly higher powers than Planck alone (arXiv:2503.14454) [src: Sect. IV.4].
- **Status date:** 2026-11-02

### Natural inflation
<!-- key: natural-inflation -->
- **Defining equations:** $V(\phi)=M^{4}\left[1+\cos\left(\frac{\phi}{f}\right)\right].$ (arXiv:1303.3787) [src: Eq. 251].
- **Parameters:** the decay constant f; Planck 2018 X scans $0.3<\log_{10}(f/M_{\mathrm{Pl}})<2.5$ (arXiv:1807.06211) [src: Table 5].
- **Predictions:** with $x\equiv\phi/f$, $\epsilon_{1}=\frac{M_{\scriptscriptstyle{\mathrm{Pl}}}^{2}}{2f^{2}}\frac{\sin^{2}x}{\left(1+\cos x\right)^{2}}\,,\qquad\epsilon_{2}=\frac{2M_{\scriptscriptstyle{\mathrm{Pl}}}^{2}}{f^{2}}\frac{1}{1+\cos x}\,,\qquad\epsilon_{3}=2\epsilon_{1}\,.$ (arXiv:1303.3787) [src: Eq. 252]; since $\epsilon_{2}>\frac{M_{\scriptscriptstyle{\mathrm{Pl}}}^{2}}{f^{2}}\,.$ [src: Eq. 253], slow roll requires $f/M_{\scriptscriptstyle{\mathrm{Pl}}}\gg 1$ (arXiv:1303.3787) [src: Sect. 5.6.2, inline, text after Eq. 253].
- **Consistency:** a super-Planckian decay constant is required by Eq. 253 above; its status in quantum gravity belongs to `thcosmo-fundamental-theory`.
- **Observational status:** strongly disfavoured by Planck 2018 + BK15, ln B = −6.6 (arXiv:1807.06211) [src: Sect. 4.2; Table 5].
- **Status date:** 2026-11-02

### Hilltop (small-field) inflation
<!-- key: hilltop-small-field-inflation -->
- **Defining equations:** Planck 2018 X tests $\Lambda^{4}\left(1-\phi^{2}/\mu_{2}^{2}+\ldots\right)$ and $\Lambda^{4}\left(1-\phi^{4}/\mu_{4}^{4}+\ldots\right)$ (arXiv:1807.06211) [src: Table 5].
- **Parameters:** the scale $\mu_{2}$ or $\mu_{4}$.
- **Predictions:** inflation near a maximum of the potential; if the potential steepens monotonically, observable hilltop inflation gives a tiny tensor fraction, r below 0.002 (Boubekeur & Lyth 2005, arXiv:hep-ph/0502047) [src: abstract].
- **Consistency:** Boubekeur & Lyth argue that hilltop inflation is generic, both as observable inflation and as an initial condition, and that tree-level hybrid inflation is the only commonly considered observable model that is not hilltop (arXiv:hep-ph/0502047) [src: abstract]; reply: none found.
- **Observational status:** quartic fits better than quadratic, ln B = −1.4 against −2.0 (arXiv:1807.06211) [src: Table 5]; Planck 2018 X then prints a 95% CL lower limit $\log_{10}(\mu_{2}/M_{\mathrm{Pl}})>1.0$ "in the quartic case", with the subscript of the quadratic scale as printed [src: Sect. 4.2].
- **Status date:** 2026-11-02

### Other single-field classes in the Planck 2018 comparison
<!-- key: other-single-field-classes-in-the-planck-2018 -->
- **Defining equations:** D-brane potentials $\Lambda^{4}\left(1-\mu^{2}_{{\rm D}\thinspace 2}/\phi^{p}+\ldots\right)$, exponential tails $\Lambda^{4}\left[1-\exp{\left(-q\phi/M_{\mathrm{Pl}}\right)}+\ldots\right]$ and the logarithmic SUSY-breaking potential $\Lambda^{4}\left[1+\alpha_{h}\log\left(\phi/M_{\mathrm{Pl}}\right)+\ldots\right]$ (arXiv:1807.06211) [src: Table 5].
- **Parameters:** one scale or slope each, with the ranges of Table 5.
- **Predictions:** not read in a primary paper.
- **Consistency:** none read.
- **Observational status:** D-brane models fit well over a large part of their parameter space (ln B = 0.6 for p = 2); exponential tails ln B = −1.0; the SB SUSY hybrid model strongly disfavoured, ln B = −6.8 (Planck 2018 + BK15, arXiv:1807.06211) [src: Sect. 4.2; Table 5].
- **Status date:** 2026-11-02

## Attractor and plateau classes
<!-- key: attractor-and-plateau-classes -->

### α-attractors (E-models and T-models)
<!-- key: alpha-attractors-e-models-and-t-models -->
- **Defining equations:** the kinetic pole of Galante et al., $\mathcal{L}_{\rm E}=\sqrt{-g}\left[{1\over 2}R-\frac{\alpha}{(1-\phi^{2}/6)^{2}}{(\partial\phi)^{2}\over 2}-\alpha f^{2}(\phi/\sqrt{6})\right]\,.$ (arXiv:1412.3797) [src: Eq. 1.3]. In canonical variables Planck 2018 X writes the E-model as $\Lambda^{4}\left\{1-\exp{\left[-\sqrt{2}\phi\left(\sqrt{3\alpha_{1}^{\rm E}}M_{\mathrm{Pl}}\right)^{-1}\right]}\right\}^{2n}$ and the T-model as $\Lambda^{4}\tanh^{2m}\left[\phi\left(\sqrt{6\alpha_{1}^{\rm T}}M_{\mathrm{Pl}}\right)^{-1}\right]$ (arXiv:1807.06211) [src: Table 5].
- **Parameters:** α, inversely proportional to the curvature of the Kähler manifold (arXiv:1311.0472) [src: abstract], and the power n or m.
- **Predictions:** at small α, n_s = 1 − 2/N and r = 12α/N² (Kallosh, Linde & Roest 2013, arXiv:1311.0472) [src: abstract]; corrections in Eq. 5.7 of that paper (see `formalism.md`). Generalised α-attractors behaving as V(φ) ∝ φ^k near the minimum with $k \geq 6$ predict n_s ≃ 0.965–0.968 for typical numbers of e-folds; T-models predict $n_s$ of 0.956–0.961 (Ellis et al. 2025, arXiv:2510.18656) [src: abstract]. Monomial T-models cannot exceed n_s = 0.9682, even with a stiff reheating stage, under perturbative reheating (Iacconi et al. 2025, arXiv:2511.14673) [src: abstract].
- **Consistency:** the supergravity motivation of the discrete values α = i/3, i from 1 to 7, comes from maximal supersymmetry (arXiv:1807.06211) [src: Sect. 4.2]; their embedding belongs to `thcosmo-fundamental-theory`. No theoretical objection specific to the class was read.
- **Observational status:** Planck 2018 + BK15 give log₁₀ α₁^E < 1.3 and, for the T-model, log₁₀ α₁^T < 1.0 at 95% CL, with the discrete values α = i/3 compatible (arXiv:1807.06211) [src: Sect. 4.2]. Ellis et al. find α ≲ 25 for E-models and α ≲ 11 for T-models from Planck, BICEP/Keck, ACT DR6 and SPT-3G (arXiv:2510.18656) [src: abstract]. Exponential α-attractors are disfavoured at more than 2σ by CMB-SPA with DESI DR2, polynomial ones favoured (arXiv:2512.05108) [src: abstract].
- **Status date:** 2026-11-02

### ξ-attractors (non-minimal coupling)
<!-- key: xi-attractors-non-minimal-coupling -->
- **Defining equations:** non-minimal coupling to gravity with the kinetic pole of the Einstein frame; the special class is equivalent to α-attractors with α = 1 + 1/(6ξ) (Galante et al. 2015, arXiv:1412.3797) [src: abstract].
- **Parameters:** ξ.
- **Predictions:** universal attractor predictions at large ξ, including Higgs inflation; no theoretical lower bound on r in the special class (arXiv:1412.3797) [src: abstract].
- **Consistency:** as for Higgs inflation (card above).
- **Observational status:** as the non-minimal-coupling row of Planck 2018 X, ln B = −2.4 (arXiv:1807.06211) [src: Table 5]; after ACT DR6 see the Higgs card.
- **Status date:** 2026-11-02

### Polynomial and interpolating attractors
<!-- key: polynomial-and-interpolating-attractors -->
- **Defining equations:** not transcribed; Kallosh & Linde introduce a family of α-attractor models that interpolates between exponential and polynomial attractors through a parameter μ (arXiv:2607.07684) [src: abstract].
- **Parameters:** α and the interpolation parameter μ.
- **Predictions:** by varying μ one scans a wide range of $n_s$, matching any combination of CMB and DESI data (arXiv:2607.07684) [src: abstract].
- **Consistency:** `[der]` the freedom to match any $n_s$ reduces the predictivity that made the exponential class a benchmark; no paper making this objection was read.
- **Observational status:** polynomial α-attractors are favoured over exponential ones by CMB-SPA with DESI DR2 (arXiv:2512.05108) [src: abstract].
- **Status date:** 2026-11-02

## Multi-field models
<!-- key: multi-field-models -->

### Hybrid inflation
<!-- key: hybrid-inflation -->
- **Defining equations:** inflaton φ plus a waterfall field σ whose rapid roll, triggered by φ, ends inflation (Linde 1994, arXiv:astro-ph/9307002) [src: abstract]; the potential was not transcribed in this run.
- **Parameters:** couplings and masses of the two fields (not read).
- **Predictions:** tree-level hybrid inflation is the one commonly considered model of observable inflation that is not of hilltop type (arXiv:hep-ph/0502047) [src: abstract].
- **Consistency:** large-η solutions do not solve the η problem of hybrid inflation in supergravity (Kinney 2005, arXiv:gr-qc/0503017) [src: abstract]; reply: none found.
- **Observational status:** the hybrid model driven by logarithmic quantum corrections in spontaneously broken supersymmetry is strongly disfavoured, ln B = −6.8 (Planck 2018 + BK15, arXiv:1807.06211) [src: Sect. 4.2].
- **Status date:** 2026-11-02

### Curvaton
<!-- key: curvaton -->
- **Defining equations:** a light field during inflation, subdominant, which later decays; its isocurvature perturbation converts to curvature when its density becomes a significant fraction of the total (Lyth & Wands 2002, arXiv:hep-ph/0110002) [src: abstract].
- **Parameters:** curvaton fraction at decay and decay products (not transcribed).
- **Predictions:** residual isocurvature fully correlated with curvature (arXiv:hep-ph/0110002) [src: abstract]; after decay, Planck 2018 X writes the isocurvature fraction of the two curvaton cases as $\beta_{\mathrm{iso}}\simeq 9(1-\tilde{r})^{2}/[r_{D}^{2}+9(1-\tilde{r})^{2}]$, with $\tilde{r}=r_{D}$ for the fully correlated CDI case (arXiv:1807.06211) [src: Sect. 9.4.2, inline].
- **Consistency:** none read in this run.
- **Observational status:** with the maximal allowed isocurvature fraction the local non-Gaussianity of the curvaton model is well within the Planck limits, and the residual isocurvature constrains the curvaton decay fraction much more tightly than non-Gaussianity does (arXiv:1807.06211) [src: Sect. 9.4.2].
- **Status date:** 2026-11-02

### Curved field spaces and turning trajectories
<!-- key: curved-field-spaces-and-turning-trajectories -->
- **Defining equations:** the covariant action and turn rate of `formalism.md` (arXiv:1010.3693, Eqs. 2.1, 2.18).
- **Parameters:** field-space curvature, heavy masses, turn rate $\eta_\bot$.
- **Predictions:** damped oscillations on the power spectrum and a reduced sound speed of the adiabatic mode for fast turns (arXiv:1010.3693) [src: abstract].
- **Consistency:** geometrical destabilisation can end inflation prematurely and exclude models that would otherwise fit the data (arXiv:1510.01281) [src: abstract].
- **Observational status:** not tested as a class in the sources read; Planck 2018 X finds no evidence for parameterised features (arXiv:1807.06211) [src: abstract].
- **Status date:** 2026-11-02

## Not verified
<!-- key: not-verified -->

- The Einstein-frame potential of Higgs inflation and its next-to-leading-order predictions (arXiv:1303.3787, Sects. 4.2.3–4.2.4) were not transcribed.
- D-brane, exponential-tail and logarithmic SUSY potentials: primary papers not read; only their rows in Planck 2018 X Table 5.
- Curvaton parameters and their $f_{\rm NL}$ prediction were not read in a primary paper.
- Quintessential and hybrid α-attractors (Kallosh, Linde and collaborators, 2026) were seen as search listings only and are not used.
- k-inflation and DBI models (sound speed below one) are left to `thcosmo-primordial-correlators`; warm inflation was not researched.
