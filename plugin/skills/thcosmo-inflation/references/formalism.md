# Formalism of inflation

Scope: definitions and governing equations of inflationary dynamics: slow roll and the flow parameters, attractors, beyond slow roll, multi-field dynamics, reheating, stochastic inflation.

Snapshot: 2026-11-02

## Conventions
<!-- key: conventions -->

The two main sources of this skill are Baumann's TASI lectures (arXiv:0907.5424) and the Encyclopaedia Inflationaris of Martin, Ringeval and Vennin (arXiv:1303.3787). Both use the reduced Planck mass; they differ in the direction in which the number of e-folds is counted. The hub's atlas (`theoretical-cosmology/references/conventions.md`, sections "Units, Planck mass", "Time variable and the direction of e-folds", "Slow-roll parameters" and "Tensor-to-scalar ratio and the pivot scale") collects the choices of other works, among them Kinney's full-Planck-mass convention.

| Item | Baumann 2009 | Martin, Ringeval & Vennin 2013 |
|---|---|---|
| Planck mass | reduced, set to one after Eq. 75; reintroduced in $\epsilon_{\rm v}(\phi)\equiv\frac{M_{\rm pl}^{2}}{2}\left(\frac{V_{,\phi}}{V}\right)^{2}$ (arXiv:0907.5424) [src: Eq. 74] | reduced, in $H^{2}=\frac{1}{3M_{\scriptscriptstyle{\mathrm{Pl}}}^{2}}\left[\frac{\dot{\phi}^{2}}{2}+V(\phi)\right]$ (arXiv:1303.3787) [src: Eq. 4] |
| e-folds in the flow parameters | ${\rm d}N=H{\rm d}t$, N grows forward in time (arXiv:0907.5424) [src: Sect. 6.2, inline, text after Eq. 70] | $N\equiv\ln(a/a_{\mathrm{ini}})$, N grows forward from an initial time (arXiv:1303.3787) [src: Sect. 3.1, inline, text after Eq. 6] |
| e-folds to the end of inflation | $N(\phi)\equiv\ln\frac{a_{\rm end}}{a}$, counted backward from the end (arXiv:0907.5424) [src: Eq. 82] | $N-N_{\mathrm{ini}}$ along the trajectory, Eq. 14 below |
| Second slow-roll parameter | η = −φ̈/(Hφ̇), not a flow parameter (Eq. 73 below) | flow hierarchy $\epsilon_{n}$ (Eq. 6 below) |
| Power spectra | dimensionless $\Delta^{2}_{\rm s}$, $\Delta^{2}_{\rm t}$ (Eq. 235 below) | dimensionless $\mathcal{P}_{\zeta}$, $\mathcal{P}_{h}$ (Eqs. 17, 20 below) |
| Pivot | horizon crossing k = aH (Eq. 235) | $k_{*}=\mathcal{H}(\eta_{*})$ at Hubble crossing; another choice of pivot time changes the constants of Eqs. 23–28 (arXiv:1303.3787) [src: Sect. 3.1, text after Eq. 28] |

- `[der]` Baumann uses N in both directions within one section: forward in Eq. 70 and backward in Eq. 82. The sign in front of $d\varepsilon/dN$ in his Eq. 73 belongs to the forward convention.
- The time variable η of the mode equation in Martin et al. is conformal time (arXiv:1303.3787, Eq. 15); in Baumann η is the second slow-roll parameter and conformal time is τ (arXiv:0907.5424, Eq. 5). <!-- num: not a value -->

## Slow roll and the flow parameters
<!-- key: slow-roll-and-the-flow-parameters -->

Background:

- Martin et al. write the Klein–Gordon equation as $\ddot{\phi}+3H\dot{\phi}+V_{\phi}=0,$ (arXiv:1303.3787) [src: Eq. 5].
- Baumann writes the acceleration equation as $\frac{\ddot{a}}{a}=-\frac{1}{6}(\rho_{\phi}+3p_{\phi})=H^{2}(1-\varepsilon)\,,$ (arXiv:0907.5424) [src: Eq. 68], so that inflation is $\varepsilon<1$ [src: Sect. 6.2, inline, text after Eq. 70].
- Exact field equation in e-folds: $\dfrac{1}{3-\epsilon_{1}}\frac{\mathrm{d}^{2}\phi}{\mathrm{d}N^{2}}+\dfrac{\mathrm{d}\phi}{\mathrm{d}N}=-M_{\scriptscriptstyle{\mathrm{Pl}}}^{2}\dfrac{\mathrm{d}\ln V}{\mathrm{d}\phi}\,,$ (arXiv:1303.3787) [src: Eq. 10]; Martin et al. note that the potential driving the field is $\ln V$ [src: Sect. 3.1, text after Eq. 10].
- Equivalently, $\left(1+\dfrac{\epsilon_{2}}{6-2\epsilon_{1}}\right)\dfrac{\mathrm{d}\phi}{\mathrm{d}N}=-M_{\scriptscriptstyle{\mathrm{Pl}}}^{2}\dfrac{\mathrm{d}\ln V}{\mathrm{d}\phi}\,.$ (arXiv:1303.3787) [src: Eq. 12], which reduces in slow roll to $\dfrac{\mathrm{d}\phi}{\mathrm{d}N}\simeq-M_{\scriptscriptstyle{\mathrm{Pl}}}^{2}\dfrac{\mathrm{d}\ln V}{\mathrm{d}\phi}\,.$ [src: Eq. 13].
- Slow-roll trajectory: $N-N_{\mathrm{ini}}=-\frac{1}{M_{\scriptscriptstyle{\mathrm{Pl}}}^{2}}\int_{\phi_{\mathrm{ini}}}^{\phi}\frac{V(\chi)}{V_{\chi}(\chi)}\,\mathrm{d}\chi\,.$ (arXiv:1303.3787) [src: Eq. 14].
- Baumann's slow-roll background is $H^{2}\approx{1\over 3}V(\phi)\approx\text{const.}$ and $\dot{\phi}\approx-\frac{V_{,\phi}}{3H}$ with $M_{\rm pl}=1$ (arXiv:0907.5424) [src: Eqs. 77–78].

Hubble-flow parameters (Martin et al.):

- Hierarchy $\epsilon_{n+1}\equiv\frac{\mathrm{d}\ln\left|\epsilon_{n}\right|}{\mathrm{d}N},\quad n\geq 0,$ (arXiv:1303.3787) [src: Eq. 6], with $\epsilon_{0}\equiv H_{\mathrm{ini}}/H$ [src: Sect. 3.1, inline, text after Eq. 6]; inflation ends at $\epsilon_{1}=1$, and slow roll means that all the $\epsilon_{n}$ are much smaller than one [src: Sect. 3.1, text after Eq. 6].
- Exact first parameter: $\epsilon_{1}=\dfrac{1}{2M_{\scriptscriptstyle{\mathrm{Pl}}}^{2}}\left(\dfrac{\mathrm{d}\phi}{\mathrm{d}N}\right)^{2},$ (arXiv:1303.3787) [src: Eq. 11].
- In slow roll, $\epsilon_{1}\simeq\frac{M_{\scriptscriptstyle{\mathrm{Pl}}}^{2}}{2}\left(\frac{V_{\phi}}{V}\right)^{2},$ (arXiv:1303.3787) [src: Eq. 7], $\epsilon_{2}\simeq 2M_{\scriptscriptstyle{\mathrm{Pl}}}^{2}\left[\left(\frac{V_{\phi}}{V}\right)^{2}-\frac{V_{\phi\phi}}{V}\right],$ [src: Eq. 8] and $\epsilon_{2}\epsilon_{3}\simeq 2M_{\scriptscriptstyle{\mathrm{Pl}}}^{4}\left[\frac{V_{\phi\phi\phi}V_{\phi}}{V^{2}}-3\frac{V_{\phi\phi}}{V}\left(\frac{V_{\phi}}{V}\right)^{2}+2\left(\frac{V_{\phi}}{V}\right)^{4}\right].$ [src: Eq. 9].

Hubble and potential parameters (Baumann):

- $\varepsilon\equiv\frac{3}{2}(w_{\phi}+1)=\frac{1}{2}\frac{\dot{\phi}^{2}}{H^{2}}\,.$ (arXiv:0907.5424) [src: Eq. 69], and $\varepsilon=-\frac{\dot{H}}{H^{2}}=-\frac{d\ln H}{dN}$ (boxed in part) [src: Eq. 70].
- $\eta=-\frac{\ddot{\phi}}{H\dot{\phi}}=\varepsilon-\frac{1}{2\varepsilon}\frac{d\varepsilon}{dN}\,,$ (arXiv:0907.5424) [src: Eq. 73], with $\vert\eta\vert<1$ keeping the fractional change of ε per e-fold small [src: Sect. 6.2, text after Eq. 73].
- Potential parameters $\epsilon_{\rm v}$ (Eq. 74, in the conventions table) and $\eta_{\rm v}(\phi)\equiv M_{\rm pl}^{2}\frac{V_{,\phi\phi}}{V}$ (arXiv:0907.5424) [src: Eq. 75].
- Relation in slow roll: $\varepsilon\approx\epsilon_{\rm v}\,,\hskip 18.49988pt\eta\approx\eta_{\rm v}-\epsilon_{\rm v}\,.$ (arXiv:0907.5424) [src: Eq. 80].
- End of inflation: $\varepsilon(\phi_{\rm end})\equiv 1\,,\hskip 18.49988pt\epsilon_{\rm v}(\phi_{\rm end})\approx 1\,.$ (arXiv:0907.5424) [src: Eq. 81].
- e-folds before the end: $N(\phi)=\int_{\phi_{\rm end}}^{\phi}\frac{{\rm d}\phi}{\sqrt{2\varepsilon}}\approx\int_{\phi_{\rm end}}^{\phi}\frac{{\rm d}\phi}{\sqrt{2\epsilon_{\rm v}}}$ (arXiv:0907.5424) [src: Eq. 83]; the CMB scales leave the horizon at $\int_{\phi_{\rm end}}^{\phi_{\rm cmb}}\frac{{\rm d}\phi}{\sqrt{2\epsilon_{\rm v}}}=N_{\rm cmb}\approx 40-60\,.$ [src: Eq. 85], the value depending on reheating and the later thermal history [src: Sect. 6.2, text after Eq. 84].

Power spectra and observables at leading order:

- Baumann: $\Delta^{2}_{\rm s}(k)\approx\left.\frac{1}{24\pi^{2}}\frac{V}{M_{\rm pl}^{4}}\frac{1}{\epsilon_{\rm v}}\right|_{k=aH}\,,\hskip 18.49988pt\Delta^{2}_{\rm t}(k)\approx\left.\frac{2}{3\pi^{2}}\frac{V}{M_{\rm pl}^{4}}\right|_{k=aH}\,.$ (arXiv:0907.5424) [src: Eq. 235].
- Baumann: $n_{\rm s}-1=2\eta_{\rm v}^{\star}-6\epsilon_{\rm v}^{\star}$ [src: Eq. 236], $n_{\rm t}=-2\epsilon_{\rm v}^{\star}$ [src: Eq. 237], $r=16\epsilon_{\rm v}^{\star}$ [src: Eq. 238] and the single-field consistency relation $r=-8n_{\rm t}$ [src: Eq. 239] (arXiv:0907.5424), each boxed in the source.
- Martin et al., first order in the Hubble-flow parameters: $n_{\scriptscriptstyle{\mathrm{S}}}=1-2\epsilon_{1}-\epsilon_{2},\quad n_{\scriptscriptstyle{\mathrm{T}}}=-2\epsilon_{1}.$ (arXiv:1303.3787) [src: Eq. 31] and $r\equiv\frac{\mathcal{P}_{h}}{\mathcal{P}_{\zeta}}=16\epsilon_{1}.$ [src: Eq. 32].
- Martin et al. define the spectral indices and runnings at the pivot by $n_{\scriptscriptstyle{\mathrm{S}}}-1\equiv\left.\frac{\mathrm{d}\ln\mathcal{P}_{\zeta}}{\mathrm{d}\ln k}\right|_{k_{*}},\qquad n_{\scriptscriptstyle{\mathrm{T}}}\equiv\left.\frac{\mathrm{d}\ln\mathcal{P}_{h}}{\mathrm{d}\ln k}\right|_{k_{*}}.$ (arXiv:1303.3787) [src: Eq. 29] and $\alpha_{\scriptscriptstyle{\mathrm{S}}}\equiv\left.\frac{\mathrm{d}^{2}\ln\mathcal{P}_{\zeta}}{\mathrm{d}(\ln k)^{2}}\right|_{k_{*}},\qquad\alpha_{\scriptscriptstyle{\mathrm{T}}}\equiv\left.\frac{\mathrm{d}^{2}\ln\mathcal{P}_{h}}{\mathrm{d}(\ln k)^{2}}\right|_{k_{*}},$ [src: Eq. 30].
- Second order (Martin et al.): the spectra are expanded about the pivot as $\frac{\mathcal{P}(k)}{\mathcal{P}_{{}_{0}}}=a_{0}+a_{1}\ln\left(\dfrac{k}{k_{*}}\right)+\frac{a_{2}}{2}\ln^{2}\left(\dfrac{k}{k_{*}}\right)+\dots\,,$ (arXiv:1303.3787) [src: Eq. 21] with $\mathcal{P}_{\zeta{{}_{0}}}=\frac{H^{2}}{8\pi^{2}\epsilon_{1}M_{\scriptscriptstyle{\mathrm{Pl}}}^{2}}\,,\qquad\mathcal{P}_{h{{}_{0}}}=\frac{2H^{2}}{\pi^{2}M_{\scriptscriptstyle{\mathrm{Pl}}}^{2}}\,,$ [src: Eq. 22]; the scalar coefficients are $a_{1}^{{\scriptscriptstyle{(\mathrm{S})}}}=-2\epsilon_{1}-\epsilon_{2}+2(2C+1)\epsilon_{1}^{2}+(2C-1)\epsilon_{1}\epsilon_{2}+C\epsilon_{2}^{2}-C\epsilon_{2}\epsilon_{3}\,,$ [src: Eq. 24] and $a_{2}^{{\scriptscriptstyle{(\mathrm{S})}}}=4\epsilon_{1}^{2}+2\epsilon_{1}\epsilon_{2}+\epsilon_{2}^{2}-\epsilon_{2}\epsilon_{3}\,,$ [src: Eq. 25], the tensor ones $a_{1}^{{\scriptscriptstyle{(\mathrm{T})}}}=-2\epsilon_{1}+2(2C+1)\epsilon_{1}^{2}-2(C+1)\epsilon_{1}\epsilon_{2}\,,$ [src: Eq. 27] and $a_{2}^{{\scriptscriptstyle{(\mathrm{T})}}}=4\epsilon_{1}^{2}-2\epsilon_{1}\epsilon_{2}\,.$ [src: Eq. 28]. The constants C and f are defined in the source around Eq. 23; the expansions are known to third order (their Ref. 29) [src: Sect. 3.1, text after Eq. 28].
- Normalisation (Martin et al.): writing $V(\phi)=M^{4}v(\phi)$, the CMB normalisation fixes $\left(\dfrac{M}{M_{\scriptscriptstyle{\mathrm{Pl}}}}\right)^{4}=24\pi^{2}\dfrac{\epsilon_{1*}}{v(\phi_{*})}\,P_{*}\,,$ (arXiv:1303.3787) [src: Eq. 35; $V=M^{4}v$ in Sect. 3.1, text before Eq. 33], with $P_{*}$ the scalar amplitude at the pivot.
- Arbitrary order: Giarè (2026) gives the scalar and tensor spectra at any finite order in the slow-roll expansion, for canonical single-field and k-inflation, with consistency relations linking $n_t$ and its runnings to r, $n_s$ and its runnings; explicit results are extended to N10LO (arXiv:2610.28608) [src: abstract]. <!-- num: not a value -->

Mode equations (Martin et al.): $v_{\boldsymbol{k}}^{\prime\prime}+\left[k^{2}-\frac{\left(a\sqrt{\epsilon_{1}}\right)^{\prime\prime}}{a\sqrt{\epsilon_{1}}}\right]v_{{\boldsymbol{k}}}=0.$ (arXiv:1303.3787) [src: Eq. 15] with $\zeta_{\boldsymbol{k}}=\frac{1}{M_{\scriptscriptstyle{\mathrm{Pl}}}}\frac{v_{\boldsymbol{k}}}{a\sqrt{2\epsilon_{1}}}\,.$ [src: Eq. 16]; tensors obey $\mu_{\boldsymbol{k}}^{\prime\prime}+\left(k^{2}-\frac{a^{\prime\prime}}{a}\right)\mu_{\boldsymbol{k}}=0.$ [src: Eq. 19]; the Bunch–Davies initial condition is $\lim_{k\eta\rightarrow-\infty}v_{\boldsymbol{k}}=\frac{1}{\sqrt{2k}}e^{-ik\eta}\,,$ [src: Eq. 18]. The quantisation itself belongs to `thcosmo-primordial-correlators`.

Energy scale and field range (Baumann):

- $r\equiv\frac{\Delta_{\rm t}^{2}(k)}{\Delta_{\rm s}^{2}(k)}\,.$ (arXiv:0907.5424) [src: Eq. 217]; then $V^{1/4}\sim\left(\frac{r}{0.01}\right)^{1/4}\,10^{16}\,{\rm GeV}$ (boxed) [src: Eq. 218].
- Lyth bound: $\frac{\Delta\phi}{M_{\rm pl}}\simeq{\cal O}(1)\left(\frac{r}{0.01}\right)^{1/2}\,,$ (arXiv:0907.5424) [src: Eq. 356]; for r above 0.01 the potential must stay flat over a super-Planckian range [src: Sect. 28.3, text after Eq. 356].

## Attractors
<!-- key: attractors -->

"Attractor" names two different things in the literature: the convergence of classical trajectories onto the slow-roll solution (treated with the initial-conditions problem, `results.md`), and classes of models whose predictions are insensitive to the potential. This section is about the second.

- Einstein-frame Lagrangian of α-attractors: $\mathcal{L}_{\rm E}=\sqrt{-g}\left[{1\over 2}R-\frac{\alpha}{(1-\phi^{2}/6)^{2}}{(\partial\phi)^{2}\over 2}-\alpha f^{2}(\phi/\sqrt{6})\right]\,.$ (Galante et al. 2015, arXiv:1412.3797) [src: Eq. 1.3]; the Starobinsky model is the special choice $\alpha=1$ for one function f [src: Sect. 1, text after Eq. 1.3].
- Pole structure: the predictions of a model whose kinetic term is a Laurent series are fixed by the order and the residue of its leading pole; the order fixes $n_s$ and the residue fixes r (arXiv:1412.3797) [src: Sect. 1; Sect. 2.1].
- Kallosh, Linde & Roest introduce α inversely proportional to the curvature of the inflaton Kähler manifold; for small α the predictions converge to n_s = 1 − 2/N and r = 12α/N², for large α to those of chaotic inflation (arXiv:1311.0472) [src: abstract].
- For the T-models $\tanh^{2n}(\varphi/\sqrt{6\alpha})$, the large-N expansion is $n_{s}\approx 1-\frac{2}{N}+\frac{\sqrt{3\alpha(4n^{2}+3\alpha)}-3n\alpha}{2nN^{2}}\,,\qquad r\approx\frac{12\alpha}{N^{2}}-\frac{6\alpha\sqrt{3\alpha(4n^{2}+3\alpha)}}{nN^{3}}\,.$ (arXiv:1311.0472) [src: Eq. 5.7]; the Kähler curvature is R_K = −2/(3α) and the n-independence holds only for α up to about 3 [src: Sect. 5, inline, text after Eq. 5.7].
- ξ-attractors are defined by a non-minimal coupling to gravity and include Higgs inflation; a special class of them is fully equivalent to α-attractors with α = 1 + 1/(6ξ), and in this class there is no theoretical lower bound on r (arXiv:1412.3797) [src: abstract].

## Beyond slow roll: ultra-slow roll and constant roll
<!-- key: beyond-slow-roll-ultra-slow-roll-and-constant -->

- Ultra-slow roll: Kinney's model with Hubble slow-roll parameter η = 3 predicts a scale-invariant scalar spectrum while the curvature perturbation evolves rapidly on super-horizon scales, violating the condition for the horizon-crossing formalism; the solutions have not yet relaxed to the inflationary attractor (arXiv:gr-qc/0503017) [src: abstract]. Motohashi et al. describe ultra-slow roll as the case where $\partial V/\partial\phi=0$ holds for an extended period (arXiv:1411.5021) [src: Sect. I, inline, text after Eq. 1].
- Constant roll (Motohashi, Starobinsky & Yokoyama): with $S=\int d^{4}x\sqrt{-g}\left[\frac{M_{\rm Pl}^{2}}{2}R-\frac{1}{2}g^{\mu\nu}\partial_{\mu}\phi\partial_{\nu}\phi-V(\phi)\right],$ [src: Eq. 2] and flow parameters $\epsilon_{1}\equiv-\frac{\dot{H}}{H^{2}},\quad\epsilon_{n+1}\equiv\frac{\dot{\epsilon}_{n}}{H\epsilon_{n}}.$ [src: Eq. 6], the rate of roll is held fixed, $\ddot{\phi}=-(3+\alpha)H\dot{\phi},$ (arXiv:1411.5021) [src: Eq. 7]. In the Hamilton–Jacobi form $\dot{\phi}=-2M_{\rm Pl}^{2}\frac{dH}{d\phi}.$ [src: Eq. 8] this gives $\frac{d^{2}H}{d\phi^{2}}=\frac{3+\alpha}{2M_{\rm Pl}^{2}}H.$ [src: Eq. 9] with general solution $H(\phi)=C_{1}\exp\left(\sqrt{\frac{3+\alpha}{2}}\frac{\phi}{M_{\rm Pl}}\right)+C_{2}\exp\left(-{\sqrt{\frac{3+\alpha}{2}}\frac{\phi}{M_{\rm Pl}}}\right).$ [src: Eq. 10].
- `[der]` The parameter α of constant roll is the rate-of-roll constant of that paper, not the α of α-attractors.
- In constant roll the would-be decaying mode of the curvature perturbation may not be negligible and can grow for some parameters, but only on solutions that are not attractors; viable cases are quadratic hilltop with a cutoff and natural inflation with a negative cosmological constant (arXiv:1411.5021) [src: abstract].
- Wands duality: perturbation spectra from massless or self-interacting fields are invariant under a two-parameter family of transformations of the background, relating slow roll to solutions far from it; a scale-invariant spectrum follows from a ∝ e^{Ht} or from a collapsing a ∝ (−t)^{2/3} (arXiv:gr-qc/9809062) [src: abstract].
- Hubble-flow parametrisations of a transient ultra-slow-roll phase can hide sharp spikes in higher derivatives of the reconstructed potential at the transition back to slow roll; after a Fourier UV filter, models typically respect Wands duality on the way back, and spurious UV effects may affect non-Gaussianity and loops (Barnert et al. 2026, arXiv:2606.28005) [src: abstract]. Loop corrections from such phases and their debate belong to `thcosmo-primordial-correlators`.

## Multi-field dynamics
<!-- key: multi-field-dynamics -->

Covariant formalism of Achúcarro et al. (arXiv:1010.3693), with signature (−+++) [src: Eq. 2.5] and reduced Planck mass:

- Action of $\mathcal{N}$ fields on a field space with metric $\gamma_{ab}$: $S=\int\!\!\sqrt{-g}\,d^{4}x\left[\frac{M_{\rm Pl}^{2}}{2}R-\frac{1}{2}\gamma_{ab}g^{\mu\nu}\partial_{\mu}\phi^{a}\partial_{\nu}\phi^{b}-V(\phi)\right]\,.$ (arXiv:1010.3693) [src: Eq. 2.1], with Christoffel symbols $\Gamma^{a}_{bc}=\frac{1}{2}\gamma^{ad}\left(\partial_{b}\gamma_{dc}+\partial_{c}\gamma_{bd}-\partial_{d}\gamma_{bc}\right)\,,$ [src: Eq. 2.2].
- Background: $\frac{D}{dt}\dot{\phi}_{0}^{a}+3H\dot{\phi}_{0}^{a}+V^{a}=0\,,$ [src: Eq. 2.6], $H^{2}=\frac{1}{3M_{\rm Pl}^{2}}\left(\frac{1}{2}\dot{\phi}_{0}^{2}+V\right)\,,$ [src: Eq. 2.7], $\dot{H}=-\frac{\dot{\phi}_{0}^{2}}{2M_{\rm Pl}^{2}}\,,$ [src: Eq. 2.8] (arXiv:1010.3693).
- Along the trajectory, with tangent $T^{a}$ and normal $N^{a}$: $\ddot{\phi}_{0}+3H\dot{\phi}_{0}+V_{\phi}=0\,,$ [src: Eq. 2.12] and $\frac{DT^{a}}{dt}=-\frac{V_{N}}{\dot{\phi}_{0}}N^{a}\,,$ [src: Eq. 2.13] (arXiv:1010.3693).
- Slow-roll vector: $\eta^{a}\equiv-\frac{1}{H\dot{\phi}_{0}}\frac{D\dot{\phi}_{0}^{a}}{dt}\,.$ [src: Eq. 2.15], split as $\eta^{a}=\eta_{||}T^{a}+\eta_{\bot}N^{a}\,,$ [src: Eq. 2.16] with $\eta_{||}\equiv-\frac{\ddot{\phi}_{0}}{H\dot{\phi}_{0}}\,,$ [src: Eq. 2.17] and the turn rate $\eta_{\bot}\equiv\frac{V_{N}}{\dot{\phi}_{0}H}\,,$ [src: Eq. 2.18], so that $\frac{DT^{a}}{dt}=-H\eta_{\bot}N^{a}\,.$ [src: Eq. 2.19] (arXiv:1010.3693). The sign function $s_N$ of their Eq. 2.9 keeps $\eta_{\bot}$ continuous; other papers fix its sign [src: Sect. 2, text after Eq. 2.19, footnote 6].
- Turns are defined with respect to the geodesics of the field-space metric; fast turns without interrupting slow roll leave damped oscillations on the power spectrum, and for a heavy second field the effective theory of the adiabatic mode has a reduced speed of sound set by the turns (arXiv:1010.3693) [src: abstract]. Non-Gaussianity from these couplings and the cosmological collider: `thcosmo-primordial-correlators`.
- Geometrical destabilisation: the curvature of field space can overcome the stabilising mass of a heavy field and destabilise the trajectory, possibly ending inflation early (Renaux-Petel & Turzyński 2016, arXiv:1510.01281) [src: abstract].
- Hybrid inflation ends by the rapid "waterfall" of a second field σ triggered by the inflaton φ (Linde 1994, arXiv:astro-ph/9307002) [src: abstract].
- Curvaton: the curvature perturbation is generated after inflation by the decay of a light field that carries an initially isocurvature perturbation; complete decay into thermalised radiation erases the isocurvature mode, and any residual isocurvature is fully correlated with the curvature (Lyth & Wands 2002, arXiv:hep-ph/0110002) [src: abstract].
- Stochastic effects make the number of fields relevant in $O(d)$-symmetric models, where it is irrelevant classically; requiring inflation to end bounds the number of fields from above (Takahashi & Tokeshi 2026, arXiv:2605.10656) [src: abstract].

## Reheating and the number of e-folds
<!-- key: reheating-and-the-number-of-e-folds -->

The number of e-folds between the exit of the pivot scale and the end of inflation, which fixes where a model sits in the $(n_s,r)$ plane, depends on the post-inflationary history.

Martin et al. (Encyclopaedia Inflationaris):

- Energy conservation during reheating: $\rho\left(N\right)=\rho_{\mathrm{end}}\exp\left\{-3\int_{N_{\mathrm{end}}}^{N}\left[1+w_{\mathrm{reh}}\left(n\right)\right]{\mathrm{d}}n\right\},$ (arXiv:1303.3787) [src: Eq. 41], with the mean equation of state $\overline{w}_{\mathrm{reh}}\equiv\frac{1}{\Delta N}\int_{N_{\mathrm{end}}}^{N_{\mathrm{reh}}}w_{\mathrm{reh}}(n)\mathrm{d}n,$ [src: Eq. 42].
- Reheating parameter: $R_{\mathrm{rad}}\equiv\dfrac{a_{\mathrm{end}}}{a_{\mathrm{reh}}}\left(\dfrac{\rho_{\mathrm{end}}}{\rho_{\mathrm{reh}}}\right)^{1/4},$ (arXiv:1303.3787) [src: Eq. 44], equivalently $\ln R_{\mathrm{rad}}\equiv\frac{\Delta N}{4}\left(-1+3\,\overline{w}_{\mathrm{reh}}\right),$ [src: Eq. 45] or $\ln R_{\mathrm{rad}}=\frac{1-3\,\overline{w}_{\mathrm{reh}}}{12(1+\overline{w}_{\mathrm{reh}})}\ln\left(\frac{\rho_{\mathrm{reh}}}{\rho_{\mathrm{end}}}\right).$ [src: Eq. 46]; a radiation-like reheating, $\overline{w}_{\mathrm{reh}}=1/3$, gives $R_{\mathrm{rad}}=1$ and cannot be distinguished from the radiation era [src: Sect. 3.2, text after Eq. 45].
- e-folds at the pivot: $\Delta N_{*}=\ln R_{\mathrm{rad}}-N_{{}_{0}}-\dfrac{1}{4}\ln\left[\dfrac{9}{\epsilon_{1*}(3-\epsilon_{1\mathrm{end}})}\dfrac{V_{\mathrm{end}}}{V_{*}}\right]+\dfrac{1}{4}\ln(8\pi^{2}P_{*}),$ (arXiv:1303.3787) [src: Eq. 48], with $N_{{}_{0}}\equiv\ln\left(\dfrac{k_{*}/a_{{}_{0}}}{\tilde{\rho}_{\gamma}^{1/4}}\right),$ [src: Eq. 50]. $\ln R_{\mathrm{rad}}$ is bounded because $-1/3<\overline{w}_{\mathrm{reh}}<1$ and $\rho_{\mathrm{nuc}}<\rho_{\mathrm{reh}}<\rho_{\mathrm{end}}$, so $\Delta N_{*}$ varies in a model-dependent range [src: Sect. 3.2, text after Eq. 50].

Planck 2018 X writes the same relation in another form:

- $N_{*}\simeq\; 67-\ln\left(\frac{k_{*}}{a_{0}H_{0}}\right)+\frac{1}{4}\ln{\left(\frac{V_{*}^{2}}{M_{\mathrm{pl}}^{4}\thinspace\rho_{\mathrm{end}}}\right)}+\frac{1-3w_{\mathrm{int}}}{12(1+w_{\mathrm{int}})}\ln{\left(\frac{\rho_{\mathrm{th}}}{\rho_{\mathrm{end}}}\right)}-\frac{1}{12}\ln(g_{\mathrm{th}})\;,$ (arXiv:1807.06211) [src: Eq. 47], the rows of one display, with $g_{\mathrm{th}}=10^{3}$ fixed in its model comparison [src: Sect. 4.2, text after Eq. 47].

Preheating (Amin et al. review):

- Fluctuations of a daughter field χ coupled to an oscillating inflaton obey Hill's equation $\frac{d^{2}y_{\bf{k}}}{dz^{2}}+\left[A_{k}+qF(z)\right]y_{\bf{k}}(z)=0,$ (arXiv:1410.3808) [src: Eq. 29], with, for the model of that section, $z=m_{\phi}t$, $A_{k}=(k^{2}+m_{\chi}^{2}+{1\over 2}g^{2}\Phi^{2})/m_{\phi}^{2}$ and $q=g^{2}\Phi^{2}/(2m_{\phi}^{2})$; for harmonic F it is the Mathieu equation [src: Sect. 3.2, text after Eq. 29].
- Floquet solutions $y_{k}(z)=e^{\tilde{\mu}_{k}z}g_{1}(z)+e^{-\tilde{\mu}_{k}z}g_{2}(z),$ (arXiv:1410.3808) [src: Eq. 30]: modes with $\Re[\tilde{\mu}_{k}]>0$ grow exponentially, in bands [src: Sect. 3.2, text after Eq. 30].
- The non-perturbative and non-linear stage, its particle-physics realisations, thermalisation before BBN and the numerical tools are reviewed in arXiv:1410.3808 [src: abstract].

## Stochastic inflation
<!-- key: stochastic-inflation -->

Stochastic inflation describes the coarse-grained field on super-Hubble scales as a classical random walk driven by the small-scale quantum modes; combined with the δN formalism it gives non-perturbative expressions for all correlation functions of scalar perturbations in single-field slow roll (Vennin & Starobinsky 2015, arXiv:1506.04732) [src: abstract]. The separate-universe and δN background is in `thcosmo-cosmological-perturbations`; QFT in de Sitter as a framework is in `thcosmo-primordial-correlators`.

- Langevin equation in e-folds: $\frac{\mathrm{d}\varphi}{\mathrm{d}N}=-\frac{V^{\prime}}{3H^{2}}+\frac{H}{2\pi}\xi\left(N\right)\,.$ (arXiv:1506.04732) [src: Eq. 1], with ξ the noise term of that paper; the e-fold number is the time variable for which the equation holds, the subject of their Sect. 2 and App. A.
- Dimensionless potential: $v=\frac{V}{24\pi^{2}M_{\scriptscriptstyle{\mathrm{Pl}}}^{4}}\approx\frac{H^{2}}{8\pi^{2}M_{\scriptscriptstyle{\mathrm{Pl}}}^{2}}$ (arXiv:1506.04732) [src: Eq. 2].
- First-passage time: the mean number of e-folds $\left\langle\mathcal{N}\right\rangle=f\left(\phi_{*}\right)\,.$ [src: Eq. 32] solves $f^{\prime\prime}\left(\varphi\right)v\left(\varphi\right)-f^{\prime}\left(\varphi\right)\frac{v^{\prime}\left(\varphi\right)}{v\left(\varphi\right)}=-\frac{1}{M_{\scriptscriptstyle{\mathrm{Pl}}}^{2}}\,,$ (arXiv:1506.04732) [src: Eq. 30], with solution $f\left(\varphi\right)=\int^{\varphi}_{\phi_{1}}\frac{\mathrm{d}x}{M_{\scriptscriptstyle{\mathrm{Pl}}}}\int^{\bar{\phi}\left(\phi_{1},\phi_{2}\right)}_{x}\frac{\mathrm{d}y}{M_{\scriptscriptstyle{\mathrm{Pl}}}}\frac{1}{v\left(y\right)}\exp\left[\frac{1}{v\left(y\right)}-\frac{1}{v\left(x\right)}\right]\,,$ [src: Eq. 33] between two absorbing boundaries.
- Classical limit of the power spectrum: $\left.\mathcal{P}_{\zeta}\right|_{\mathrm{cl}}\left(\phi_{*}\right)=\frac{2}{M_{\scriptscriptstyle{\mathrm{Pl}}}^{2}}\frac{v^{3}\left(\phi_{*}\right)}{{v^{\prime}}^{2}\left(\phi_{*}\right)}\,,$ (arXiv:1506.04732) [src: Eq. 52]; first stochastic correction in the classical regime $\left.\mathcal{P}_{\zeta}\right|_{\eta_{\mathrm{cl}}\ll 1}\left(\phi_{*}\right)\simeq\left.\mathcal{P}_{\zeta}\right|_{\mathrm{cl}}\left(\phi_{*}\right)\left[1+5v\left(\phi_{*}\right)-4\frac{v^{2}\left(\phi_{*}\right)v^{\prime\prime}\left(\phi_{*}\right)}{{v^{\prime}}^{2}\left(\phi_{*}\right)}\right]\,,$ [src: Eq. 53], where $\eta_{\mathrm{cl}}$ is the classicality parameter of that paper; the general spectral index is $n_{\scriptscriptstyle{\mathrm{S}}}=1-\frac{g^{\prime\prime}\left(\phi\right)}{f^{\prime}\left(\phi\right)g^{\prime}\left(\phi\right)}+\frac{f^{\prime\prime}\left(\phi\right)}{{f^{\prime}}^{2}\left(\phi\right)}\,.$ [src: Eq. 51], with g the second moment function of their Sect. 3.3.3.
- Classicality criterion: stochastic effects are small only if the potential is sub-Planckian and not too flat; the ratio of quantum to classical field displacement is not the right criterion (arXiv:1506.04732) [src: abstract; Sect. 3.1].

Eternal inflation:

- For slow roll, Creminelli et al. find a critical classical inflaton speed, φ̇²/H⁴ = 3/(2π²), at which the distribution of the reheating volume changes sharply; for sub-critical speeds all its moments are infinite and the probability of an infinite reheating volume becomes non-zero (arXiv:0802.1067) [src: abstract].

## Not verified
<!-- key: not-verified -->

- Starobinsky's 1980 paper and the original $R^{2}$ predictions of Mukhanov & Chibisov are pre-arXiv; only Planck 2018 X's lowest-order transcription (arXiv:1807.06211, Eq. 48) was read.
- The constants C and f of the second-order slow-roll spectra (arXiv:1303.3787, Eq. 23) and the zeroth-order coefficients $a_0$ were not transcribed.
- Kinney's backward-N conventions are summarised from the hub atlas, not re-read in this run.
- Lyth's original paper on the field-range bound was not read; only Baumann's statement (arXiv:0907.5424, Eq. 356).
- The full stochastic power spectrum (arXiv:1506.04732, Eq. 50, a multi-row display) and the definition of the classicality parameter $\eta_{\rm cl}$ were not transcribed.
- The broad-resonance regime and the stability chart of the Mathieu equation (arXiv:1410.3808, Sect. 3.2) were not read beyond Eqs. 29–30.
- The hybrid-inflation potential (arXiv:astro-ph/9307002) and the δN formalism itself were not read; δN belongs to `thcosmo-cosmological-perturbations`.
- Warm inflation (dissipative damping, named by Planck 2018 X, Sect. 4.2) was not researched.
