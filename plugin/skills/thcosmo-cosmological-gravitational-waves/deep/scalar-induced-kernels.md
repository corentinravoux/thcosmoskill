# Scalar-induced kernels — thcosmo-cosmological-gravitational-waves dossier

Scope: how the second-order kernel of scalar-induced waves is derived step by step in radiation and matter domination, how other equations of state are reached, how local non-Gaussianity of the curvature adds terms, what the gauge debate settled and for which epochs, and what fixes the infrared tail, including beyond second order.
Snapshot: 2026-11-10.
From: Caprini & Figueroa arXiv:1801.04268, Sect. 6.4; Roshan & White arXiv:2401.04388, Sect. V; Domènech arXiv:2109.01398 — `references/subtopics.tsv`, row `scalar-induced-waves`.
Audit questions: (3) How is the scalar-induced kernel derived, for which equations of state and at which order; how do non-Gaussian curvature and the gauge choice change the spectrum; what is the infrared tail?

Already in the reference files, and not repeated here: the general constant-w transfer function, its radiation and kination forms and the redshifting to today (Eqs. 10.2–10.7 and 5.2 of the Domènech review), the infrared slopes of its Eqs. 2.22–2.23, and the third-order matter-era result (`formalism.md#scalar-induced-gravitational-waves`); the gauge statements of the review and the instantaneous-reheating caveat (`approximations.md#scalar-induced-waves-gaussianity-gauge-and`); the model card (`models.md#scalar-induced-waves-from-an-enhanced-small`); the gauge debate as an open question (`open-questions.md#the-gauge-question-for-scalar-induced-waves`). The formation of primordial black holes from the same peak belongs to `thcosmo-pbh-defects` (planned); second-order gauge transformations as such to `thcosmo-cosmological-perturbations` (planned).

## Conventions
<!-- key: conventions -->

- Kohri & Terada (arXiv:1804.08577, Kohri & Terada 2018) work in conformal time η with $x\equiv k\eta$, the Newtonian-gauge potential Φ, the curvature spectrum $\mathcal{P}_\zeta$ <!-- eq: notation -->, and a Fourier measure with $(2\pi)^{3/2}$ in the source integral [src: Eq. 8]. The fraction of the critical density is defined with an oscillation average and summed over both polarisations, $\displaystyle\Omega_{\text{GW}}(\eta,k)=\frac{\rho_{\text{GW}}(\eta,k)}{\rho_{\text{tot}}(\eta)}=\frac{1}{24}\left(\frac{k}{a(\eta)H(\eta)}\right)^{2}\overline{\mathcal{P}_{h}(\eta,k)},$ (arXiv:1804.08577) [src: Eq. 6].
- Adshead, Lozanov & Weiner (arXiv:2105.01659, Adshead et al. 2021) write the curvature as $\mathcal R$ with a power spectrum defined without a $(2\pi)^3$ in front of the delta function, and use τ for conformal time (arXiv:2105.01659) [src: Eq. 31]. <!-- num: not a value -->
- The Domènech review uses the reduced Planck mass and $\mathcal{P}_{\cal R}$ (`formalism.md#scalar-induced-gravitational-waves`). No conversion between these normalisations is made here.

## The derivation
<!-- key: the-derivation -->

### Step 1 — the second-order tensor equation and its source
<!-- key: step-1-the-second-order-tensor-equation-and-its -->

In the second-order tensor equation, "squares of first-order quantities also appear", and the first-order stress is traded for derivatives of Φ through the first-order Einstein equations [src: Sect. 2.2]. The result is $h^{\prime\prime}_{\bf k}(\eta)+2\mathcal{H}h^{\prime}_{\bf k}(\eta)+k^{2}h_{\bf k}(\eta)=4S_{\bf k}(\eta),$ [src: Eq. 7] with $S_{\bf k}=\int\frac{\text{d}^{3}q}{(2\pi)^{3/2}}e_{ij}({\bf k})q_{i}q_{j}\left(2\Phi_{\bf q}\Phi_{{\bf k}-{\bf q}}+\frac{4}{3(1+w)}\left(\mathcal{H}^{-1}\Phi^{\prime}_{\bf q}+\Phi_{\bf q}\right)\left(\mathcal{H}^{-1}\Phi^{\prime}_{{\bf k}-{\bf q}}+\Phi_{{\bf k}-{\bf q}}\right)\right).$ [src: Eq. 8], using $-2\dot{H}=\rho+P=(1+w)\rho=3(1+w)H^{2}$ [src: Sect. 2.2, inline, text after Eq. 8]. It is solved with a Green's function, $a(\eta)h_{\bf k}(\eta)=4\int^{\eta}\text{d}\bar{\eta}G_{\bf k}(\eta,\bar{\eta})a(\bar{\eta})S_{\bf k}(\bar{\eta}),$ [src: Eq. 9], where $G_{\bf k}^{\prime\prime}(\eta,\bar{\eta})+\left(k^{2}-\frac{a^{\prime\prime}(\eta)}{a(\eta)}\right)G_{\bf k}(\eta,\bar{\eta})=\delta(\eta-\bar{\eta}).$ (arXiv:1804.08577) [src: Eq. 10]. The source equation and Green's function are those of the Newtonian (shear-free) gauge; Step 6 is about what changes in other gauges. The radiation-era version of this source was first computed by Ananda, Clarkson & Wands (arXiv:gr-qc/0612013) [src: abstract] and extended to all observable wavelengths by Baumann et al. (arXiv:hep-th/0703290) [src: abstract].

### Step 2 — the potential and the kernel
<!-- key: step-2-the-potential-and-the-kernel -->

"In the absence of entropy perturbations and using $c_{\text{s}}^{2}=w$", the potential obeys $\Phi^{\prime\prime}_{\bf k}(\eta)+\frac{6(1+w)}{(1+3w)\eta}\Phi^{\prime}_{\bf k}(\eta)+wk^{2}\Phi_{\bf k}(\eta)=0.$ [src: Eq. 12], with the primordial value normalised as $\langle\phi_{\bf k}\phi_{\bf k^{\prime}}\rangle=\delta({\bf k}+{\bf k}^{\prime})\frac{2\pi^{2}}{k^{3}}\left(\frac{3+3w}{5+3w}\right)^{2}\mathcal{P}_{\zeta}(k),$ [src: Eq. 13], "where $w$ should be evaluated at time well before the horizon entry" [src: Sect. 2.2, text after Eq. 13]. Neglecting the non-Gaussianity of the curvature, the two-point function of the source gives $\mathcal{P}_{h}(\eta,k)=4\int_{0}^{\infty}\text{d}v\int_{\left|1-v\right|}^{1+v}\text{d}u\left(\frac{4v^{2}-(1+v^{2}-u^{2})^{2}}{4vu}\right)^{2}I^{2}(v,u,x)\mathcal{P}_{\zeta}(kv)\mathcal{P}_{\zeta}(ku),$ [src: Eq. 14] with the kernel $I(v,u,x)=\int_{0}^{x}\text{d}\bar{x}\frac{a(\bar{\eta})}{a(\eta)}kG_{k}(\eta,\bar{\eta})f(v,u,\bar{x}),$ [src: Eq. 15], and f the source function of their Eq. 16 [src: Eq. 16]. They note that the integrand contains "the square of a single function $I(v,u,x)$" after symmetrisation, "seemingly unnoticed in the original paper [22], which makes their analytic expression so complicated" (arXiv:1804.08577) [src: Sect. 2.2, text after Eq. 16]. <!-- num: not a value -->

### Step 3 — radiation domination
<!-- key: step-3-radiation-domination -->

The Green's function is $kG_{\bf k}(\eta,\bar{\eta})=-x\bar{x}(j_{0}(x)y_{0}(\bar{x})-y_{0}(x)j_{0}(\bar{x}))=\sin(x-\bar{x}),$ [src: Eq. 18], and the potential that tends to 1 at early times is $\Phi(x)=\frac{9}{x^{2}}\left(\frac{\sin(x/\sqrt{3})}{x/\sqrt{3}}-\cos(x/\sqrt{3})\right).$ [src: Eq. 19], decaying "like $x^{-2}$" [src: Sect. 3.1, text after Eq. 19]. The scale-factor ratio is $\bar x/x$; the paper's footnote gives the correction from changes of $g_*$ and $g_{*,s}$ and states "We neglect these factors for analytic calculations" [src: Sect. 3.1, footnote 2]. The integral needs "multiple usages of the trigonometric addition theorem and integration by parts" and gives the full $I_{\rm RD}(v,u,x)$ of their Eq. 22 in terms of Si and Ci [src: Sect. 3.1, Eqs. 22–23]; "For small $x$, the leading term is independent of $u$ and $v$, $I_{\text{RD}}(v,u,x)\simeq x^{2}/2$" [src: Sect. 3.1, inline, text after Eq. 24]. In the late-time limit the kernel "redshifts like $x^{-1}\propto a^{-1}$", and its oscillation average is $\overline{I_{\text{RD}}^{2}(v,u,x\to\infty)}=\frac{1}{2}\left(\frac{3(u^{2}+v^{2}-3)}{4u^{3}v^{3}x}\right)^{2}\left(\left(-4uv+(u^{2}+v^{2}-3)\log\left|\frac{3-(u+v)^{2}}{3-(u-v)^{2}}\right|\right)^{2}\right.\left.\hskip 20.00003pt\hskip 20.00003pt\hskip 20.00003pt\hskip 20.00003pt\hskip 20.00003pt+\pi^{2}(u^{2}+v^{2}-3)^{2}\Theta(v+u-\sqrt{3})\right).$ (arXiv:1804.08577) [src: Eq. 26], copied with the spacing commands of the rendering. The theta function comes from "the sign change of the limit of Si" [src: Sect. 3.1, text after Eq. 25]. The radiation-era transfer function of the Domènech review, which "recovers the result of Kohri and Terada [63] after taking into account all numerical factors", is in `formalism.md#scalar-induced-gravitational-waves`.

For a monochromatic spectrum the result has a logarithmic singularity at $k=(2/\sqrt{3})k_{*}$, "due to resonant amplification: the frequency of the source term oscillation is twice that of the gravitational potential" (arXiv:1804.08577) [src: Sect. 3.1, inline, Example 1, text after Eq. 29].

### Step 4 — matter domination and other equations of state
<!-- key: step-4-matter-domination-and-other-equations-of -->

In matter domination the Green's function is $kG_{\bf k}(\eta,\bar{\eta})=-x\bar{x}(j_{1}(x)y_{1}(\bar{x})-y_{1}(x)j_{1}(\bar{x}))=\frac{1}{x\bar{x}}\left((1+x\bar{x})\sin(x-\bar{x})-(x-\bar{x})\cos(x-\bar{x})\right).$ [src: Eq. 34] and the potential solution "regular at $x\to 0$" is constant, $\Phi(x)=1.$ [src: Eq. 35; Sect. 3.2, text before Eq. 35], with the footnote that "This heuristic derivation is actually not a proper treatment because small perturbations to the pure MD equation affect properties of its solution significantly" [src: Sect. 3.2, footnote 3]. The source is $f_{\text{MD}}(v,u,x)=\frac{6}{5}.$ [src: Eq. 36], and $I_{\text{MD}}(v,u,x)=\frac{6(x^{3}+3x\cos x-3\sin x)}{5x^{3}}.$ [src: Eq. 37], which "asymptotes to 6/5 in the large x limit" [src: Sect. 3.2, text after Eq. 37]. Because the late-time kernel does not oscillate, the oscillation average is corrected by hand: "we neglect the kinetic term and instead multiply the gradient term by 2. To compensate for the factor 2 for the oscillation average of the nonoscillating term, we have to multiply the correction factor by 1/2", giving $\overline{I^{2}(v,u,x\to\infty)}=\frac{18}{25}.$ (arXiv:1804.08577) [src: Eq. 38 and text before]. Step 6 explains why this tensor is not a freely propagating wave.

For a general constant w, Domènech derives "new analytic integral formulas for the induced gravitational waves on subhorizon scales in a general cosmological background with a constant equation of state", where previously "semi-analytical solutions are only known for matter and radiation domination eras" (arXiv:1912.05583, Domènech 2019) [src: abstract]; the resulting transfer functions and their condition $c_s\neq 0$ are in `formalism.md#scalar-induced-gravitational-waves`. Sudden and gradual transitions between eras are treated in Sect. 3.3 of arXiv:1804.08577, not read here.

### Step 5 — local non-Gaussianity of the curvature
<!-- key: step-5-local-non-gaussianity-of-the-curvature -->

Eq. 14 assumes a Gaussian curvature. With local non-Gaussianity, $\mathcal{R}(\mathbf{x})=\mathcal{R}_{g}(\mathbf{x})+F_{\mathrm{NL}}\left(\mathcal{R}_{g}(\mathbf{x})^{2}-\langle\mathcal{R}_{g}(\mathbf{x})^{2}\rangle\right),$ (arXiv:2105.01659) [src: Eq. 30], the power spectrum itself acquires a one-loop term, $\mathcal{P}_{\mathcal{R}}(k)=\mathcal{P}_{g}(k)+2F_{\mathrm{NL}}^{2}\int\frac{\mathrm{d}^{3}q}{(2\pi)^{3}}\mathcal{P}_{g}(q)\mathcal{P}_{g}({\left|\mathbf{k}-\mathbf{q}\right|}).$ (arXiv:2105.01659) [src: Eq. 32], and the induced spectrum, being a four-point function of $\mathcal R$, picks up the trispectrum. Adshead et al. classify the contributions into three disconnected ones (Gaussian, a "hybrid" term of order $F_{\rm NL}^2$ and a "reducible" term of order $F_{\rm NL}^4$) and four connected ones ("C" and "Z" of order $F_{\rm NL}^2$, "planar" and "nonplanar" of order $F_{\rm NL}^4$) [src: Eqs. 33–39], and state that the "C" term "does not appear in Ref. [74], while" the "Z" term "does not appear in Ref. [88]" (arXiv:2105.01659) [src: Sect. 2.2, text after Eq. 39]; they "numerically compute all contributions" for several enhanced spectra [src: abstract]. <!-- num: not a value -->

Earlier calculations with a narrow peak and local non-Gaussianity find that the non-Gaussian contribution "increases as $k^3$, peaks at $k/k_*=4/\sqrt{3}$, and has a sharp cutoff at $k=4k_*$", and "can exceed the Gaussian part if $\mathcal{P}_\mathcal{R}(k)f_\text{NL}^2\gtrsim1$" (arXiv:1810.11000, Cai, Pi & Sasaki 2019) [src: abstract, inline]. Unal finds that "even if scalar curvature fluctuations have a subdominant non-Gaussian component, these non-Gaussian perturbations can source a dominant portion of the induced GWs", which "peaks at a higher frequency" (arXiv:1811.09151, Unal 2019) [src: abstract]. Beyond a perturbative $F_{\rm NL}$ expansion, lattice simulations of ultra-slow-roll inflation find that for moderate non-Gaussianity "the semi-analytical prediction captures the correct order of magnitude of the GW signal but receives important corrections", and that for large non-Gaussianity "it can fail dramatically in both amplitude and spectral shape" (arXiv:2604.03628, Caravano et al. 2026) [src: abstract]. A lattice method recasting the Fourier integrals as "about 50 convolutions" computes "fully non-perturbative, non-Gaussian SIGW spectra in seconds with an error within 10%", in a first implementation for $w = 1/3$ (arXiv:2605.27231, Piccoli 2026) [src: abstract, inline].

### Step 6 — gauge choice
<!-- key: step-6-gauge-choice -->

The chain of results, in order:

1. **Gauge dependence exists.** "being second order in perturbation, such an induced tensor perturbation is generically gauge dependent", the spectrum depending "on the hypersurface (temporal gauge) condition taken for the linear scalar perturbation"; previous studies were "based on zero-shear gauge without proper justification" (arXiv:1704.03500, Hwang et al. 2017) [src: abstract].
2. **Which gauges differ, for constant w.** In the Newtonian, comoving and uniform-curvature gauges, "Huge differences are found between the Newtonian and comoving gauge results for any $w \,(\ge 0)$", "always caused by the perturbation of the shift vector"; the Newtonian and uniform-curvature gauges "give the same energy density for $w>0$", while for $w=0$ the uniform-curvature result "deviates significantly from that of the Newtonian gauge" (arXiv:1910.01880, Tomikawa & Kobayashi 2020) [src: abstract, inline].
3. **The late-time wave is gauge independent in radiation domination.** Inomata & Terada find that "the late-time (e.g. observable) GWs calculated in the TT gauge and in the Newtonian gauge coincide with each other, in contrast to Ref. [41]", "late time" meaning "time much after the horizon entry of the relevant scalar source modes as well as the tensor mode"; the agreement holds "because the tensor perturbations are finally dominated by the freely propagating tensor perturbations (GWs)" (arXiv:1912.00785, Inomata & Terada 2020) [src: Sect. 3]. The comoving-gauge difference comes from terms oscillating as $\cos\left((u\pm v)k\eta/\sqrt{3}\right)$, "which are not the oscillations of gravitational waves", so "the gauge dependence appears only in the tensor perturbations coupling with scalar perturbation, not in the gravitational wave" [src: Sect. 3, inline]; they "expect" that diffusion damping removes it [src: Sect. 3].
4. **Matter domination is different.** In a matter era "the scalar perturbations continue to couple with the tensor perturbations on subhorizon scales even in the Newtonian gauge", the kernel in the TT gauge "is different from that in the Newtonian gauge even at late time", and "this kind of tensor perturbation is not a gravitational wave", being "time-independent in the Newtonian gauge" (arXiv:1912.00785) [src: Sect. 3]. This is the constant kernel of Step 4.
5. **A set of admissible gauges.** Domènech & Sasaki show that "the induced GW spectrum is invariant under a set of reasonable gauge transformations, i.e. physically well behaved on small scales, once the source term has become inactive", including "the commonly used flat, constant Hubble and synchronous gauges but excludes the comoving slicing gauge", and that in dust domination a particular solution "can be gauged away by a small change of gauge" (arXiv:2012.14016, Domènech & Sasaki 2021) [src: abstract].
6. **Production, propagation, measurement.** De Luca et al. divide the question "in three parts: the production of gravitational waves, their propagation in the real universe, and their measurement" (arXiv:1911.09689, De Luca et al. 2020) [src: abstract]; their conclusions were not read.

### Step 7 — the infrared tail
<!-- key: step-7-the-infrared-tail -->

The infrared slopes $3-2|b|$ and 3 are those of the Domènech review (arXiv:2109.01398) [src: Eqs. 2.22–2.23] (`formalism.md#scalar-induced-gravitational-waves`). Their origin and conditions:

- **Causality, for a general bilinear source.** $\Omega_{\text{GW}}\propto k^{3}$ "is universally valid when the source term is bounded in both frequency and time, is effective in a radiation-dominated stage, and for $k$ smaller than all the physical scales associated with the source, like the peak frequency, peak width, and time duration" (arXiv:1909.13728, Cai, Pi & Sasaki 2019) [src: abstract, inline]. In their words, induced waves "with a broad peak" scale as $f^{3}$, "while a δ-function peak gives $f^{2}$" (arXiv:1909.13728) [src: introduction, inline].
- **Beyond second order and with non-Gaussianity.** Yuan traces the scaling to "the stress of sound waves with nearly equal frequencies", which "produces a slow beat" that sources the long-wavelength tensor "before its horizon entry", and shows that higher-order interactions "lead to the same slow beat"; "Since non-Gaussianities would not change the speed of the freely propagating waves, they do not modify the infrared scaling" (arXiv:2609.17928, Yuan 2026) [src: abstract].
- **Scale-dependent non-Gaussianity.** "For localized sources with finite weighted moments, smooth running preserves the leading $k^3$ infrared behavior up to logarithmic corrections" (arXiv:2608.24883, Marriott-Best et al. 2026) [src: abstract, inline].

### Step 8 — higher orders
<!-- key: step-8-higher-orders -->

The second-order kernel is not the end of the expansion. In a matter era the third-order kernels grow secularly (`formalism.md#scalar-induced-gravitational-waves`). For the PTA interpretation, Zhao et al. include third-order waves, "which allow for a substantial enhancement in the spectral amplitude of SIGWs", and conclude that the favoured region "can to some extent alleviate the PBH overproduction problem" (arXiv:2603.05191, Zhao et al. 2026) [src: abstract]. The non-perturbative lattice results of Step 5 concern the inflationary scalar statistics, not the order of the tensor source: Caravano et al. evolve "the Newtonian potential linearly while retaining the full non-Gaussian structure of the initial conditions" (arXiv:2604.03628) [src: abstract].

## Variants and what they cost
<!-- key: variants-and-what-they-cost -->

- **Analytic kernel (Kohri & Terada) against numerical time integration.** The analytic radiation and matter kernels neglect the change of $g_*$ in the scale factor (Step 3) and assume a single era; sudden or gradual transitions need their Sect. 3.3 or the reheating treatment of `approximations.md#scalar-induced-waves-gaussianity-gauge-and`.
- **General w (Domènech).** Analytic for constant w, "not valid for $c_{s}=0$", peaks entering during that epoch (arXiv:2109.01398) [src: Sect. 10.1, inline, text after Eq. 10.5] (`formalism.md#scalar-induced-gravitational-waves`); the dust case needs Step 4 and the gauge caveats of Step 6.
- **Perturbative non-Gaussianity against lattice.** The $F_{\rm NL}$ expansion of arXiv:2105.01659 is complete to fourth order in $F_{\rm NL}$ for local type [src: Sect. 2.2]; lattice approaches are needed when non-Gaussianity is large (arXiv:2604.03628) [src: abstract].
- **Newtonian gauge against others.** Newtonian, flat, constant-Hubble, synchronous and TT gauges agree on the late-time wave in radiation domination (Step 6); the comoving gauge does not (arXiv:1910.01880; arXiv:2012.14016) [src: abstracts].

## Numbers
<!-- key: numbers -->

| Quantity | Value as printed | Assumptions | Source | Place read |
|---|---|---|---|---|
| Late-time MD kernel squared | 18/25 | Φ = 1, corrected oscillation average | arXiv:1804.08577 | [src: Eq. 38] |
| RD source function at early times | "equal to 4/3 at x=0" | radiation domination | arXiv:1804.08577 | [src: Sect. 3.1, text after Eq. 20] |
| Resonance of a monochromatic peak | k = (2/√3) k_* | radiation domination | arXiv:1804.08577 | [src: Sect. 3.1, Example 1] |
| Non-Gaussian peak and cutoff | k/k_* = 4/√3; k = 4k_* | narrow peak, local NG | arXiv:1810.11000 | [src: abstract] |
| NG term exceeds Gaussian | P_R f_NL² ≳ 1 | narrow peak, local NG | arXiv:1810.11000 | [src: abstract] |
| Lattice SIGW accuracy | within 10 % | w = 1/3, FLAN-SIGW | arXiv:2605.27231 | [src: abstract] |

## What goes wrong
<!-- key: what-goes-wrong -->

- **A Dirac-delta spectrum read as physical.** A δ-function peak gives an $f^2$ infrared tail instead of $f^3$ (arXiv:1909.13728) [src: introduction, inline] and a logarithmic resonance (Step 3); the review attributes the slope change to "the unphysical divergence" (`approximations.md#scalar-induced-waves-gaussianity-gauge-and`). Check: use a finite width before quoting a tail.
- **The matter-era kernel taken as a wave.** The constant kernel of Step 4 is a tensor that couples to growing scalars and "is not a gravitational wave" (arXiv:1912.00785) [src: Sect. 3]; its late-time average needs the hand-made oscillation-average factor of Step 4.
- **Comoving gauge.** Excluded from the admissible set (arXiv:2012.14016) [src: abstract]; huge differences from Newtonian gauge for any $w\ge 0$ (arXiv:1910.01880) [src: abstract, inline]. Check: the gauge of the source term, and that the source is inactive when the energy is evaluated.
- **Missing non-Gaussian diagrams.** Earlier papers each omitted one connected term (arXiv:2105.01659) [src: Sect. 2.2, text after Eq. 39]. Check: all seven contributions to fourth order in $F_{\rm NL}$ for local type.
- **Perturbative non-Gaussianity for large non-Gaussianity.** Can "fail dramatically" (arXiv:2604.03628) [src: abstract].
- **Primordial normalisation.** Eq. 13 of arXiv:1804.08577 fixes Φ with w "evaluated at time well before the horizon entry", but at the same equation of state as at horizon entry [src: Sect. 2.2, text after Eq. 13]; a peak entering across a change of w does not satisfy this.
- **A printed form to check in arXiv:1804.08577 (v2).** The source function Eq. 16 is printed with the products $\bar{x}\partial_{\bar{\eta}}\Phi(v\bar{x})$ and $\bar{x}^{2}\partial_{\bar{\eta}}\Phi(v\bar{x})\partial_{\bar{\eta}}\Phi(u\bar{x})$, a dimensionless $\bar x$ times a derivative with respect to conformal time [src: Eq. 16]; whether a derivative with respect to $\bar x$ is meant was not checked against an erratum. Use the explicit RD form, Eq. 20, which "is equal to 4/3 at x=0" [src: Sect. 3.1, text after Eq. 20].

## Reading list
<!-- key: reading-list -->

- Ananda, Clarkson & Wands 2007, arXiv:gr-qc/0612013 (foundation) — the radiation-era induced background.
- Baumann, Ichiki, Steinhardt & Takahashi 2007, arXiv:hep-th/0703290 (foundation) — the spectrum over all observable wavelengths.
- Kohri & Terada 2018, arXiv:1804.08577 (derivation) — Sects. 2–3: Green's function, kernel, analytic RD and MD results.
- Domènech 2019, arXiv:1912.05583 (extension) — analytic kernels for constant w.
- Cai, Pi & Sasaki 2019, arXiv:1810.11000 (extension) — local non-Gaussianity, narrow peak.
- Adshead, Lozanov & Weiner 2021, arXiv:2105.01659 (critique) — Sect. 2.2: the complete set of non-Gaussian contributions.
- Tomikawa & Kobayashi 2020, arXiv:1910.01880 (critique) — gauge comparison for constant w.
- Inomata & Terada 2020, arXiv:1912.00785 (derivation) — Sect. 3: why the late-time wave is gauge independent in radiation domination, and why matter domination differs.
- Domènech & Sasaki 2021, arXiv:2012.14016 (review of the gauge issue) — the admissible gauges.
- Cai, Pi & Sasaki 2019, arXiv:1909.13728 (foundation) — conditions for the $k^3$ tail.
- Yuan 2026, arXiv:2609.17928 (latest) — infrared universality beyond second order.
- Caravano, Franciolini & Renaux-Petel 2026, arXiv:2604.03628 (critique) — lattice SIGW from ultra-slow-roll inflation.

## Not verified
<!-- key: not-verified -->

- The full radiation kernel Eq. 22 of Kohri & Terada and its $(t,s)$ form, Eq. 27, were read but not transcribed; transitions between eras (its Sect. 3.3) were not read.
- The general-w kernels were taken from the reference files (Domènech review); the derivation in arXiv:1912.05583 was read at the abstract only.
- Which papers are Refs. [74] and [88] of arXiv:2105.01659 (the INSPIRE record lists few references) and Ref. [41] of arXiv:1912.00785 was not established.
- The second-order gauge transformation of $h_{ij}$ itself, and the conclusions of arXiv:1911.09689, were not read; they belong to `thcosmo-cosmological-perturbations` (planned).
- The one-loop (in the tensor sense) and third-order radiation-era corrections were read at abstract level only (arXiv:2603.05191); the matter-era third-order result is in `formalism.md`.
- The equations of arXiv:1909.13728 are printed incompletely in the HTML rendering read; only its abstract and introduction are used.
