# Models of modified gravity

Scope: the modified-gravity model landscape, one card per model or class, chosen by literature weight; formalism in `formalism.md`, model-independent results in `results.md`.

Snapshot: 2026-11-02

## Scalar–tensor models
<!-- key: scalar-tensor-models -->

### Horndeski theory (generalised Galileons)
<!-- key: horndeski-theory-generalised-galileons -->
- **Defining equations:** the Lagrangian of `formalism.md`, Horndeski section (arXiv:1901.07183, Eq. 8); after GW170817 the subclass with luminal tensors is ${\cal L}=G_{2}(\phi,X)-G_{3}(\phi,X)\Box\phi+G_{4}(\phi)R.$ (arXiv:1901.07183) [src: Eq. 125], which excludes the scalar coupled to the Gauss–Bonnet term [src: Sect. 4.2, text after Eq. 125].
- **Parameters:** four free functions $G_{2},\ldots,G_{5}$ of φ and X (arXiv:1901.07183) [src: Sect. 2.1, text after Eq. 8]; on linear cosmological scales they enter only through the α functions of the EFT of dark energy (`formalism.md`, EFT section).
- **Predictions:** a time-dependent effective Newton constant and gravitational slip in the quasi-static limit (arXiv:1901.07183) [src: Eqs. 100–101]; even with $c_{\rm GW}=1$ a time-dependent f (or $G_{4}$) adds the friction term $\dot{f}/f$ to the equation of $h_{ij}$ and modifies the amplitude of gravitational waves [src: Sect. 4.2, last paragraph].
- **Consistency:** GW170817 restricts the theory to Eq. 125 (arXiv:1901.07183) [src: Sect. 4.2]; reply: the LIGO band lies close to the strong-coupling scale or cutoff of many dark-energy models, where operators at the cutoff can bring the speed back to one, so the constraint need not apply to the low-energy theory (de Rham & Melville 2018, arXiv:1806.09417) [src: abstract]. Kobayashi also notes that the constraint assumes the theory to be valid at the LIGO scale and leaves gravity in the early universe unconstrained (arXiv:1901.07183) [src: Sect. 4.2, text after Eq. 131]. Shift-symmetric Horndeski with luminal tensors and no direct coupling to dark matter crosses $w_{\rm DE}=-1$ only with pathologies according to Tsujikawa (arXiv:2508.17231) [src: abstract]; reply: Calderon & Linder show analytically and numerically that it can cross while ghost-free and stable (arXiv:2610.36063) [src: abstract]. See `open-questions.md`.
- **Observational status:** within Horndeski gravity, a non-parametric reconstruction from DESI 2024 BAO implies that gravity should be non-minimally coupled, with a crossing of the phantom divide at $z\lesssim1$ (Ye et al. 2024, arXiv:2407.15832) [src: abstract]; a reconstruction of $\Lambda(t)$ and $\Omega(t)$ from CMB, DESI BAO, SN Ia, CMB-ISW lensing and DES Y3 3x2pt finds a 2.8σ hint for a non-minimal coupling (Ye et al. 2026, arXiv:2605.12415) [src: abstract]. Constraints on the α functions are in `results.md`.
- **Status date:** 2026-11-02

### Beyond Horndeski (GLPV) and DHOST
<!-- key: beyond-horndeski-glpv-and-dhost -->
- **Defining equations:** quadratic DHOST and GLPV Lagrangians of `formalism.md` (arXiv:1901.07183, Eqs. 114–120). After GW170817 and the absence of graviton decay the quadratic DHOST theories reduce to $A_{4}=\frac{3f_{X}^{2}}{2f},\quad A_{1}=A_{2}=A_{3}=A_{5}=0.$ (arXiv:1901.07183) [src: Eq. 131], a subclass that is neither Horndeski nor GLPV if $f_{X}\neq 0$ [src: Sect. 4.2, text after Eq. 131].
- **Parameters:** f, $A_{1}$, $A_{3}$ in class Ia, plus $G_{2}$ and $G_{3}$ (arXiv:1901.07183) [src: Sect. 4.1, text after Eq. 118].
- **Predictions:** the scalar changes the sound speed of minimally coupled matter (arXiv:1404.6495) [src: abstract]; Vainshtein screening is partially broken inside matter (arXiv:1901.07183, Sect. 5.3; see `formalism.md`, screening).
- **Consistency:** all cubic DHOST theories give $c_{\rm GW}\neq1$ and are ruled out (arXiv:1901.07183) [src: Sect. 4.2, text after Eq. 125]; graviton decay into dark-energy fluctuations forces $\alpha_{\rm H}=0$ and, with luminal tensors, rules out all quartic and quintic GLPV theories (Creminelli et al. 2018, arXiv:1809.03484) [src: abstract]; reply: the cutoff argument of arXiv:1806.09417 [src: abstract] applies to both constraints.
- **Observational status:** constrained mainly through $\alpha_{\rm H}$ and the gravitational-wave constraints above; no cosmological detection found in this run.
- **Status date:** 2026-11-02

### f(R) gravity, Hu–Sawicki model
<!-- key: f-r-gravity-hu-sawicki-model -->
- **Defining equations:** $f(R)=-m^{2}{c_{1}(R/m^{2})^{n}\over c_{2}(R/m^{2})^{n}+1}\,,$ (arXiv:0705.1158) [src: Eq. 3]; the n = 1 small-field form of the Euclid review is in `formalism.md` (arXiv:2512.09748, Eq. 49).
- **Parameters:** n and $|f_{R0}|$, the background being matched to ΛCDM (arXiv:0705.1158) [src: Fig. 1 caption]; $f_{R0}<0$ (arXiv:2512.09748) [src: Sect. 5.1].
- **Predictions:** scale-dependent μ with the transition at $m_{f_{R}}$ and $\Sigma(a)=\frac{1}{1+f_{R}(a)}\,.$ (arXiv:2512.09748) [src: Eq. 52]. The scalar is locked to the GR value across "more than 25 orders of magnitude in density", out through the solar corona; if the galactic halo and local environment do not have "substantially deeper potentials than expected in LCDM", |f_R| > 10⁻⁶ makes the galactic interior evolve to low curvature "during the acceleration epoch" (arXiv:0705.1158) [src: abstract].
- **Consistency:** chameleon no-go: the Compton wavelength is at most Mpc at present cosmic density and the conformal factor is essentially constant over the last Hubble time, so that chameleon-like theories cannot self-accelerate and rely "on a form of dark energy rather than a genuine modified gravity effect" (Wang, Hui & Khoury 2012, arXiv:1208.4612) [src: abstract]; reply: none found.
- **Observational status:** cosmological bound |f_R0| < 6.3 × 10⁻⁴ at 95% CL from Planck 2015, BAO, JLA, WiggleZ and CFHTLenS; astrophysical tests reach $10^{-7}$; galaxy morphology gives |f_R0| < 1.4 × 10⁻⁸ (all as quoted by the Euclid review, arXiv:2512.09748) [sec: Sect. 5.1, inline]; the morphology paper finds no evidence for a screened fifth force of any strength in the Compton wavelength range 0.3–8 Mpc and rules out astrophysically relevant Hu–Sawicki gravity (Desmond & Ferreira 2020, arXiv:2009.08743) [src: abstract, title].
- **Status date:** 2026-11-02

### Jordan–Brans–Dicke
<!-- key: jordan-brans-dicke -->
- **Defining equations:** $S_{\rm BD}$ of `formalism.md` (arXiv:2512.09748, Eq. 37), with a cosmological constant mimicking a constant potential [src: Sect. 4.1.3].
- **Parameters:** $\omega_{\rm BD}$, the "sole, dimensionless, parameter" (arXiv:2512.09748) [src: Sect. 4.1.3].
- **Predictions:** background equations of arXiv:2512.09748 [src: Eqs. 38–39]; JBD "can, in principle, capture the large-scale behaviour of more general scalar-tensor theories" [src: Sect. 4.1.3].
- **Consistency:** no objection read in this run; local-test bounds on $\omega_{\rm BD}$ are listed under "Not verified".
- **Observational status:** Euclid forecasts in arXiv:2512.09748, Sect. 4.2.3 (not read in this run).
- **Status date:** 2026-11-02

### Covariant Galileons (cubic, quartic, quintic)
<!-- key: covariant-galileons-cubic-quartic-quintic -->
- **Defining equations:** the galileon is the 4D effective scalar π of DGP, universally coupled to matter, with an internal "galilean" invariance under which its gradient shifts by a constant; Nicolis et al. argue that it is the only generalisation allowing a robust Vainshtein effect (arXiv:0811.2197, Nicolis et al. 2008) [src: abstract]. Its covariant completion is a subclass of Horndeski (`formalism.md`).
- **Parameters:** the coefficients of the cubic, quartic and quintic terms (arXiv:1707.02263) [src: abstract].
- **Predictions:** self-accelerating solutions; the sign of the ISW cross-correlation $C_\ell^{\rm T g}$ is negative for the cubic Galileon because the lensing potential deepens (arXiv:1707.02263) [src: abstract]. In N-body runs of the generalised cubic covariant Galileon, Vainshtein screening reduces the enhancement at small scales (arXiv:2608.06499) [src: abstract].
- **Consistency:** the quartic and quintic Galileons change $c_g$ at low redshift; GW170817 "eliminate[s] any late-universe application" of the covariant Galileon (arXiv:1710.05901) [src: abstract].
- **Observational status:** cubic Galileon in "$7.8σ$ tension" with CMB, BAO and ISW (WISE × CMB temperature) data, "which effectively rules it out"; ISW also rules out a significant region of the quartic and quintic parameter space (Renk et al. 2017, arXiv:1707.02263) [src: abstract]. The generalised cubic covariant Galileon, with power-law kinetic and cubic terms, admits tracker solutions and remains under study (arXiv:2608.06499) [src: abstract].
- **Status date:** 2026-11-02

### k-mouflage
<!-- key: k-mouflage -->
- **Defining equations:** $S=\int\mathrm{d}^{4}x\sqrt{-\tilde{g}}\left[\frac{c^{4}\tilde{R}}{16\pi\tilde{G}_{\rm N}}+c^{2}\tilde{M}^{4}K(X)\right]+S_{\rm m}(\psi,g_{\mu\nu})\,,$ with Jordan metric $g_{\mu\nu}=A^{2}(\varphi)\tilde{g}_{\mu\nu}$ (arXiv:2512.09748) [src: Eq. 41]; local Newton constant $G_{\rm eff}=\tilde{G}_{\rm N}A^{2}\left(1+\frac{2\beta^{2}}{K^{\prime}}\right)\,,$ [src: Eq. 42].
- **Parameters:** the functions K(X) and A(φ); cosmologically $\epsilon_{1}(a)=\frac{2\bar{\beta}^{2}}{\bar{K}^{\prime}}\,,\quad\epsilon_{2}(a)=\frac{\mathrm{d}\ln\bar{A}}{\mathrm{d}\ln a}\,,$ (arXiv:2512.09748) [src: Eq. 43].
- **Predictions:** $\mu(a)=\bar{A}^{2}(a)\left[1+\epsilon_{1}(a)\right]\,,\quad\Sigma(a)=\bar{A}^{2}(a)\,.$ (arXiv:2512.09748) [src: Eq. 44]; screening where $K^{\prime}\gg1$, in regions whose gravitational acceleration exceeds roughly $H_{0}c$, so that the Solar System and the Galaxy are screened and clusters are not [src: Sect. 4.1.4]. Introduced by Babichev et al. (arXiv:0905.2943) [src: abstract].
- **Consistency:** none read in this run.
- **Observational status:** $-0.04\leq\epsilon_{2,0}\leq 0$ at 95% CL from CMB, SN Ia, BAO and local $H_0$, other parameters unconstrained (Benevento et al. 2019, as quoted in arXiv:2512.09748) [sec: Sect. 4.1.4].
- **Status date:** 2026-11-02

## Massive and vector models
<!-- key: massive-and-vector-models -->

### Ghost-free (dRGT) massive gravity
<!-- key: ghost-free-drgt-massive-gravity -->
- **Defining equations:** $\mathcal{L}_{\rm mGR}$ of `formalism.md` (arXiv:1401.4173, Eq. 5.37).
- **Parameters:** the graviton mass m and $\alpha_{3}$, $\alpha_{4}$ (arXiv:1401.4173) [src: Eq. 5.37], and the reference metric.
- **Predictions:** Vainshtein screening built in (arXiv:2607.15507) [src: abstract]; no flat FLRW solution with a Minkowski reference metric (arXiv:1401.4173) [src: Sect. 12.2.1]; approximately FRW domains of size the inverse graviton mass, with an upper bound on the graviton mass "roughly" an order of magnitude below the present Hubble rate (arXiv:1108.5231) [src: abstract].
- **Consistency:** superluminal shock waves, hence acausality, arising from the constraint that removes the Boulware–Deser ghost (Deser & Waldron 2012, arXiv:1212.5835) [src: abstract]; reply: from an EFT perspective, unitarity, analyticity and causality "strongly single out" the ghost-free theory as the infrared realisation of massive gravity (arXiv:2607.15507) [src: abstract]; positivity bounds on 2→2 scattering of $\Lambda_5$ theories impose the tunings that produce the $\Lambda_3$ (ghost-free) structure, and the $\Lambda_3$ "island of positivity" "appears relatively stable" against further bounds (de Rham et al. 2018, arXiv:1804.10624) [src: abstract].
- **Observational status:** no cosmological detection; viability rests on screening and on the cosmological branch chosen (arXiv:2607.15507) [src: abstract].
- **Status date:** 2026-11-02

### Ghost-free bigravity (Hassan–Rosen)
<!-- key: ghost-free-bigravity-hassan-rosen -->
- **Defining equations:** dRGT with a dynamical reference metric (arXiv:1109.3515) [src: abstract]; the mass term is $\mathcal{L}_{m}(g,f)=\sum_{n=0}^{4}\alpha_{n}\mathcal{L}_{n}[\mathcal{K}(g,f)]$ (arXiv:1401.4173) [src: Sect. 8.2.1, inline].
- **Parameters:** the two Planck masses, m and the $\alpha_{n}$ (arXiv:1401.4173) [src: Sect. 8.2.1].
- **Predictions:** one massless and one massive graviton; candidates for dynamical dark energy and spin-2 dark matter (arXiv:2609.10760, Herber et al. 2026) [src: abstract].
- **Consistency:** Higuchi ghost absent on the healthy branch, gradient instability avoided with weakly constrained parameters (arXiv:1404.0008) [src: abstract]; the complete tree-level 2→2 amplitudes, 199 "symmetry-inequivalent" helicity amplitudes, show non-linear ghost-free parameter dependence first with three massive external states (arXiv:2609.10760) [src: abstract].
- **Observational status:** described as admitting "observationally viable cosmologies" and passing local tests (arXiv:2609.10760) [src: abstract]; no dataset-level verdict read in this run.
- **Status date:** 2026-11-02

### Generalised Proca and vector Galileons
<!-- key: generalised-proca-and-vector-galileons -->
- **Defining equations:** the Horndeski-Proca action of arXiv:1402.7026 [src: abstract]; the full action with $\mathcal{L}_{F}$ and $\mathcal{L}_{2}$–$\mathcal{L}_{5}$, its background and tensor equations (arXiv:1603.05806, Eqs. 1–7, 12–14, 33–34) are transcribed in `formalism.md#vector-tensor-theories`.
- **Parameters:** free functions of $A^{2}$ at each order (arXiv:1402.7026) [src: Sect. 2]; De Felice et al. treat the Lagrangian up to quintic order (arXiv:1603.05806) [src: abstract].
- **Predictions:** a stable de Sitter attractor for the late-time acceleration in the examples studied (arXiv:1603.05806) [src: abstract].
- **Consistency:** shift-symmetric generalised Proca with luminal tensors and no coupling to dark matter crosses the phantom divide only with pathologies (arXiv:2508.17231) [src: abstract]; reply: none found for the Proca case. GW170817 bounds also apply to vector–tensor theories (Baker et al. 2017, arXiv:1710.06394) [src: abstract]; the varying $c_g$ conclusion extends to Einstein–aether, Hořava gravity and generalised Proca (arXiv:1710.05901) [src: abstract]. Replacing the Proca mass term by a general potential "inevitably introduces ghost instabilities of the same kind as those recently identified for vector-tensor theories of modified gravity", and evolving such a field on a Kerr background shows that non-perturbative dynamics does not drive the system away from them (Clough et al. 2022, arXiv:2204.10868) [src: abstract]; reply: none found in this run. `[der]` That paper treats a minimally coupled self-interacting Proca field around a black hole, not the cosmological branch of generalised Proca.
- **Observational status:** a scalar–vector–tensor model whose vector drives $w<-1$ early and whose scalar drives the crossing gives "a better best fit than" flat ΛCDM and Bayes factors "larger than unity" against ΛCDM with DES Y5, DESI DR2 BAO, compressed CMB and Gold-2017 RSD, the value depending on the prior normalisation (Roy et al. 2026, arXiv:2609.31113) [src: abstract]. For the earlier generalised Proca dark-energy model with a de Sitter attractor preceded by $w_{\rm DE}=-1-s$, background data (CMB, BAO, SN Ia, local $H_{0}$) give $s=0.254^{+0.118}_{-0.097}$ at 95% CL, and adding RSD growth data with the no-ghost and stability conditions gives $s=0.16^{+0.08}_{-0.08}$ (95 % CL), so that "the model with $s>0$ is still favored over the $\Lambda$CDM model" (De Felice, Heisenberg & Tsujikawa 2017, arXiv:1703.09573) [src: abstract]; with the model in a Boltzmann code, Planck + HST give $h=0.7334_{-0.0269}^{+0.0246}$ and the addition of BAO, RSD and other late-time data gives $h=0.7041_{-0.0087}^{+0.0094}$, read by the authors as a reduced $H_{0}$ tension (De Felice et al. 2020, arXiv:2002.06782) [src: abstract]. These fits predate DESI and use the data sets named; the Roy et al. fit is the only DESI-era one read in this run `[der]`. <!-- eq: notation -->
- **Status date:** 2026-11-04

### Einstein–aether theory
<!-- key: einstein-aether-theory -->
- **Defining equations:** $S=-\frac{1}{16\pi G}\int\sqrt{-g}~(R+K^{ab}_{mn}\nabla_{a}u^{m}\nabla_{b}u^{n})~d^{4}x.$ (arXiv:0801.1547) [src: Eq. 1], with the unit timelike aether $u^{a}$ and the tensor $K^{ab}_{mn}$ of Eq. 2, in the signature (+−−−); transcribed in `formalism.md#vector-tensor-theories`. Introduced in this form by Jacobson & Mattingly (arXiv:gr-qc/0007031) [src: abstract]. <!-- num: not a value -->
- **Parameters:** four dimensionless couplings $c_{i}$ ($i=1,2,3,4$), with $c_{ij}\equiv c_{i}+c_{j}$ (arXiv:1802.04303) [src: abstract]. <!-- num: not a value --> <!-- eq: notation -->
- **Predictions:** a dynamical preferred frame; on FLRW the expansion is governed by $G_{\rm cosmo}=\frac{G}{1+(c_{13}+3c_{2})/2}.$ (arXiv:0801.1547) [src: Eq. 10], which differs from $G_{\rm N}$ unless the PPN parameters $\alpha_{1,2}$ vanish (arXiv:0801.1547) [src: Sect. 3, text after Eq. 10].
- **Consistency:** the action restricted to $\nabla_{[a}u_{b]}$ develops gradient singularities (arXiv:gr-qc/0007031) [src: abstract]; the unit-norm constraint removes the wrong-sign kinetic term of the length-stretching mode (arXiv:0801.1547) [src: Sect. 1, text after Eq. 2]; reply: not applicable.
- **Observational status:** GW170817 with GRB 170817A restricts $- 3\times 10^{-15} < c_T -1 < 7\times 10^{-16}$, which for Einstein–aether implies $\left|c_{13}\right| \le 10^{-15}$; the remaining constraints lie in the $(c_{1},c_{14})$ and $(c_{2},c_{14})$ planes, and the strong-field constraints depend on neutron-star sensitivities "which are not known at present in the new ranges of the parameters" (Oost, Mukohyama & Wang 2018, arXiv:1802.04303) [src: abstract]. Primordial helium bounds $|G_{\rm cosmo}/G_{\rm N}-1|$ to be ≲ 1/8 (arXiv:0801.1547) [src: Sect. 3, text after Eq. 10]. Because GW170817 constrains "only a combination of the theory's free parameters", "a significant part of the theory's parameter space remains unconstrained by observations"; gravitational-wave lensing modifies the wave speed through aether inhomogeneities, a modification "common to both gravitational polarizations" that "vanishes in the limit in which gravitational waves propagate with luminal speed", so "the potential to improve tests based on gravitational-wave speed is limited" (Streibert, Silva & Zumalacárregui 2024, arXiv:2404.07782) [src: abstract].
- **Status date:** 2026-11-04

### DGP braneworld (self-accelerating and normal branches)
<!-- key: dgp-braneworld-self-accelerating-and-normal -->
- **Defining equations:** $S=\frac{c^{4}}{16\pi G_{5}}\int_{\cal M}\mathrm{d}^{5}x\sqrt{-\gamma}R_{5}+\int_{\partial{\cal M}}\mathrm{d}^{4}x\sqrt{-g}\left[\frac{c^{4}}{16\pi G_{\rm N}}R+{\cal L}_{\rm m}\right]\,,$ (arXiv:2512.09748) [src: Eq. 45]; 4D gravity at short distances and 5D at large distances (arXiv:hep-th/0005016, Dvali et al. 2000) [src: abstract].
- **Parameters:** the cross-over scale $r_{\rm c}=G_{5}/(2G_{\rm N})$ and $\Omega_{\rm rc}\equiv c^{2}/(4r_{\rm c}^{2}H_{0}^{2})$ (arXiv:2512.09748) [src: Sect. 4.1.5, inline].
- **Predictions:** for the normal branch with a ΛCDM background, in the quasi-static approximation, $\Sigma=1$ and $\mu(a)=1+\frac{1}{3\beta}\,,\quad\beta(a)\equiv 1+\frac{H}{H_{0}}\frac{1}{\sqrt{\Omega_{\rm rc}}}\left(1+\frac{\dot{H}}{3H^{2}}\right)\,.$ (arXiv:2512.09748) [src: Eq. 46].
- **Consistency:** strong interactions at a length λ_3 ∼ (λ_DGP² / M_P)^{1/3}, about 1000 km if $\lambda_{DGP}$ is the Hubble length (Luty, Porrati & Rattazzi 2003, arXiv:hep-th/0303116) [src: abstract, inline]; a 4D ghost on the self-accelerating branch for any brane tension, while the normal branch is ghost-free (Charmousis et al. 2006, arXiv:hep-th/0604086) [src: abstract]; positivity: DGP cannot be embedded in a UV theory with canonical analyticity (arXiv:hep-th/0602178) [src: abstract].
- **Observational status:** normal branch: $\Omega_{\rm rc}<0.27$ from BOSS DR12 clustering wedges and growth rates (Barreira et al. 2016), and $\Omega_{\rm rc}<40$ at 95% from SDSS DR7 (Raccanelli et al. 2013), both as quoted in arXiv:2512.09748 [sec: Sect. 4.1.5]. Self-accelerating branch: abandoned on the ghost argument above.
- **Status date:** 2026-11-02

## Teleparallel, non-metricity and non-local models
<!-- key: teleparallel-non-metricity-and-non-local-models -->

### f(T) gravity
<!-- key: f-t-gravity -->
- **Defining equations:** $\mathcal{S}_{f(T)}:=\frac{1}{2\kappa^{2}}\int{\rm d}^{4}x\,e\,f(T)+\mathcal{S}_{\rm m}\,,$ (arXiv:2106.13793) [src: Eq. 5.48], in the (+−−−) review convention; tetrad and spin-connection field equations (Eqs. 5.53–5.54) and the flat-FLRW Friedmann equations (Eqs. 6.7a–6.7b) are transcribed in `formalism.md#teleparallel-and-non-metricity-theories`. Introduced for cosmic acceleration by Bengochea & Ferraro (arXiv:0812.1205) and Linder (arXiv:1005.3039) [src: abstracts].
- **Parameters:** the function f(T); power-law, exponential and hyperbolic-tangent forms are the representative models of a 2026 DESI DR2 analysis (arXiv:2610.20002, Zheng et al. 2026) [src: abstract].
- **Predictions:** modified background expansion and growth (arXiv:2106.13793) [src: abstract].
- **Consistency:** the action and field equations of algebraic f(T) "are not invariant under local Lorentz transformations" and the theories "appear to have extra degrees of freedom" (Li, Sotiriou & Barrow 2011, arXiv:1010.1041) [src: abstract]; reply: the covariant formulation with a spin connection, in which the spin-connection equation is the antisymmetric part of the tetrad equation and the spin connection is "a pure gauge DoF, and not a Stückelberg field" (arXiv:2106.13793) [src: Sect. 5.3.1, text after Eq. 5.56]. Strong coupling from an unstably broken local symmetry of the flat connection; linear perturbation treatments resemble a counting known to contain "a well-known mistake" (arXiv:2405.14184) [src: abstract]; reply: none found.
- **Observational status:** with DESI DR2 BAO, CMB and Pantheon+, the mild departure from ΛCDM of the power-law model disappears once SN Ia are included; the exponential model keeps a non-zero deformation parameter but without a clear statistical preference by information criteria (arXiv:2610.20002) [src: abstract].
- **Status date:** 2026-11-04

### f(Q) gravity (symmetric teleparallel)
<!-- key: f-q-gravity-symmetric-teleparallel -->
- **Defining equations:** $\mathcal{S}_{f(\mathbb{Q})}[g,\Gamma]\coloneqq-\frac{1}{2\kappa}\int_{\mathcal{M}}\mathrm{d}^{4}x\,\sqrt{|g|}\,f(\mathbb{Q})+\mathcal{S}_{\rm matter}[g,\Psi]$ (arXiv:2309.15958) [src: Eq. 5.40]; the field equations (Eqs. 5.41–5.42) and the coincident-gauge cosmology (Eqs. 6.1–6.4) are transcribed in `formalism.md#teleparallel-and-non-metricity-theories`. Foundations: coincident GR (arXiv:1710.03116) and the first f(Q) cosmology (Beltrán Jiménez et al. 2019, arXiv:1906.10027) [src: abstracts].
- **Parameters:** the function f(Q) and the choice of connection branch; there are three inequivalent spatially flat cosmologies (arXiv:2311.04201) [src: abstract].
- **Predictions:** the review states that f(Q) models may explain early and late-time phenomena without dark energy, an inflaton or dark matter, and may address cosmological tensions (arXiv:2309.15958) [src: abstract]. The family $f(\mathbb{Q})=\frac{1}{\kappa}\left(\mathbb{Q}+M\,\sqrt{\mathbb{Q}}\right)\,.$ (arXiv:2309.15958) [src: Eq. 6.8] has the GR background and differs only in perturbations [src: Sect. 6.1, text after Eq. 6.8]; tensor perturbations rescale Newton's constant and the scalar sector has two additional propagating modes (arXiv:1906.10027) [src: abstract]; f(Q) and f(T) "are indistinguishable at cosmological background level" (arXiv:2106.13793) [src: Sect. 5.3.1, text after Eq. 5.52].
- **Consistency:** Gomes et al. find that two of the three flat branches have reduced linear spectra and are infinitely strongly coupled, and that the third propagates seven gravitational degrees of freedom of which at least one is a ghost; "Our results rule out $f(\mathbb{Q})$ cosmologies" (Gomes et al. 2023, arXiv:2311.04201) [src: abstract]. In the wider quadratic non-metricity class (Newer GR), generic theories have ghosts or more degrees of freedom on FLRW than on Minkowski, the exceptions being STEGR and a transverse-diffeomorphism-invariant subclass (Ganz & Spinelli 2025, arXiv:2511.19101) [src: abstract]. Reply: none found in this run that restores a healthy f(Q) cosmology; see `open-questions.md`.
- **Observational status:** background fits to DESI DR2 exist (for example arXiv:2608.24676); `[der]` a background fit does not test the consistency problem above.
- **Status date:** 2026-11-04

### Non-local gravity: Deser–Woodard and RR models
<!-- key: non-local-gravity-deser-woodard-and-rr-models -->
- **Defining equations:** the RR term $m^2 R\,\Box^{-2}R$ added to the Einstein–Hilbert action (arXiv:1402.0448) [src: abstract], in the form $\Gamma_{\rm RR}=\int d^{4}x\sqrt{-g}\,\left[\frac{m_{\rm Pl}^{2}}{2}R-R\frac{\Lambda_{\rm\scriptscriptstyle RR}^{4}}{\Box^{2}}R\right]=\frac{m_{\rm Pl}^{2}}{2}\int d^{4}x\sqrt{-g}\,\left[R-\frac{1}{6}m^{2}R\frac{1}{\Box^{2}}R\right]\,,$ (arXiv:1712.07066) [src: Eq. 1.1]; the DW term $\sim R f(\Box^{-1}R)$ (arXiv:1901.07832) [src: abstract], from Deser & Woodard (arXiv:0706.2151) and reviewed in arXiv:1401.0254; the revised DW-2019 model with f(Y) (arXiv:1902.08075) [src: abstract]. Details in `formalism.md#non-local-gravity`.
- **Parameters:** RR: one mass m, fixed by the dark-energy density today (arXiv:1402.0448) [src: abstract], plus the boundary-condition parameter $u_{0}$ (arXiv:1712.07066) [src: Sect. 4]; DW: the function f, fixed by requiring the ΛCDM background (arXiv:1901.07832) [src: abstract]; DW-2019: f(Y), for which Ding & Deng reconstruct $f(Y)\simeq\boldsymbol{e}^{2.153(Y-16.97)}$ (arXiv:1908.11223, Ding & Deng 2019) [src: abstract]. <!-- eq: notation -->
- **Predictions:** self-acceleration with a phantom equation of state; for the RR model the abstract gives "a pure prediction" w_DE ≃ −1.14 (arXiv:1402.0448) [src: abstract]; well-behaved perturbations and luminal gravitational waves (arXiv:1712.07066) [src: abstract]. With Planck+BAO+SNe the minimal RR model gives $H_{0}=69.49\pm 0.80\,,$ (arXiv:1712.07066) [src: Eq. 3.50], a difference of "only 2.0σ" from the local $H_{0}=73.24\pm 1.74$, against 3.1σ in ΛCDM and νΛCDM, and $\sum_{\nu}m_{\nu}=0.219^{+0.083}_{-0.084}$ eV (arXiv:1712.07066) [src: Sect. 3.3.3, Eq. 3.51]. The DW model gives "a lower linear growth rate and a stronger lensing power as compared to ΛCDM, up to several percents" and a "significantly smaller" σ8 from Planck CMB+lensing (arXiv:1901.07832) [src: abstract]. A variant of the RT model with initial conditions set during inflation predicts a GW luminosity distance that at LISA or Einstein Telescope redshifts "can differ from that in GR by as much as 60%" (Belgacem et al. 2019, arXiv:1907.02047) [src: abstract].
- **Consistency:** the original DW models were presented as needing no screening for Solar-System tests (arXiv:1401.0254) [src: abstract]; reply: the Lunar Laser Ranging limit on $|\dot{G}|/G$ shows that "the mechanism of 'perfect screening for free' suggested for the DW model actually does not work" (Belgacem et al. 2018, arXiv:1812.11181) [src: abstract]. DW-2019 is built to switch off for $Y < 0$ in bound systems (arXiv:1902.08075) [src: abstract]; Solar-System light deflection, Shapiro delay, perihelion advance and geodetic precession give "a well-defined and sharply bounded allowed region" for the parameters $(\zeta,b)$ of a static spherically symmetric DW solution (Liu & Du 2025, arXiv:2511.07981) [src: abstract].
- **Observational status:**
  - RR, cosmology: the RR model "fits the CMB, BAO, SNe, structure formation data and local $H_0$ measurements at a level statistically equivalent to ΛCDM" (arXiv:1712.07066) [src: abstract]; with Planck+BAO+JLA, $\Delta\chi_{\rm min}^{2}$ relative to νΛCDM is 0.26 for ΛCDM, 3.62 for RR with $u_{0}=0$ and -0.10 for RR with $u_{0}=250$ (arXiv:1712.07066) [src: Table 1].
  - RR and DW, Solar System: confirming Barreira et al., the RR model is ruled out by Lunar Laser Ranging "under plausible assumptions such as the absence of strong backreaction from non-linear structures", the DW model "is also ruled out", and the RT model "passes all phenomenological consistency tests and is still a viable candidate" (arXiv:1812.11181) [src: abstract].
  - DW, growth: Woodard reports "the negative verdict of structure formation" (arXiv:1401.0254) [src: abstract]; recast in a localised model, the DW model "is not ruled out and actually gives a better fit to RSD data than ΛCDM" (Nersisyan et al. 2017, arXiv:1701.00434) [src: abstract]; with Planck CMB+lensing and RSD, model selection gives only "weak" evidence for ΛCDM against DW (arXiv:1901.07832) [src: abstract]; DW-2019 "is not ruled out by the $f\sigma_8$ data" (arXiv:1908.11223) [src: abstract].
  - `[der]` A phantom w without crossing, as the RR model predicts, differs from the crossing that DESI-based reconstructions prefer (arXiv:2407.15832) [src: abstract]; no DESI-era fit of RR, RT or DW was found in this run.
- **Status date:** 2026-11-04

## Not verified
<!-- key: not-verified -->

- Local-test bounds on $\omega_{\rm BD}$ (Cassini) and on chameleons from laboratory experiments were not read in this run.
- The verdict of Belgacem et al. on the RR model (arXiv:1712.07066) was read in the deepening run of 2026-11-04 (abstract, Table 1, Sect. 3.3.3); Barreira et al., whose Lunar Laser Ranging analysis arXiv:1812.11181 confirms, was not read, and no DESI-era fit of the RT model was searched.
- Euclid forecasts for JBD, k-mouflage and nDGP (arXiv:2512.09748, Sects. 4.2.3–4.2.5) were not read.
- Bigravity constraints from data and the status of the bigravity gradient instability beyond arXiv:1404.0008 were not read.
- Hořava gravity, mimetic gravity, Gauss–Bonnet couplings and Einstein–dilaton–Gauss–Bonnet cosmology are not carded.
