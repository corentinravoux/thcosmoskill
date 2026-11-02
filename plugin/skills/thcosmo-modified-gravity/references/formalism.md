# Formalism of modified gravity

Scope: definitions and governing equations of theories that modify gravity on cosmological scales: scalar–tensor (Horndeski, beyond Horndeski, DHOST), f(R), massive gravity and bigravity, vector–tensor, teleparallel and non-metricity theories, non-local gravity, screening, the EFT of dark energy and parameterised frameworks, and the tensor sector.

Snapshot: 2026-11-02

## Conventions
<!-- key: conventions -->

The skill's main sources all use the signature (−+++); they differ in which Newtonian-gauge potential sits in $g_{00}$, in the definition of the kinetic variable X, in the sign of the cubic Horndeski term, in keeping c, and in time variables. The hub atlas (`theoretical-cosmology/references/conventions.md`, sections "Metric signature and curvature signs", "Units, Planck mass and where 8πG appears", "Gauge and names of the metric potentials" and "Dark-energy and modified-gravity parameterisations and their signs") collects the choices of other works, among them Clifton et al. (arXiv:1106.2476), whose (−+++) signature and Misner–Thorne–Wheeler curvature conventions are transcribed there.

| Item | Kobayashi 2019 (arXiv:1901.07183) | Bellini & Sawicki 2014 (arXiv:1404.3713) | Euclid review 2025 (arXiv:2512.09748) | Planck 2015 XIV (arXiv:1502.01590) |
|---|---|---|---|---|
| Signature | (−+++), from his line element (arXiv:1901.07183) [src: Eq. 87] | (−+++) (hub atlas) | (−+++), from its line element (arXiv:2512.09748) [src: Eq. 28] | (−+++), conformal time (hub atlas) |
| Potential in $g_{00}$ | Φ (arXiv:1901.07183) [src: Eq. 87] | — | Ψ (arXiv:2512.09748) [src: Eq. 28] | Ψ (hub atlas) |
| Slip | $\eta(t):=\frac{\Psi}{\Phi}$ (arXiv:1901.07183) [src: Eq. 101] | — | $\eta(a,k)=\Phi/\Psi$ (arXiv:2512.09748) [src: Sect. 4.1.1, inline, text after Eq. 30] | Φ/Ψ (hub atlas) |
| Kinetic variable | $X:=-g^{\mu\nu}\phi_{\mu}\phi_{\nu}/2$ (arXiv:1901.07183) [src: Sect. 4.1, inline, text after Eq. 118] | Horndeski functions K, $G_{i}$ of φ and X (arXiv:1404.3713) [src: App. A] | $X=-\tfrac{1}{2}\nabla_{\mu}\phi\nabla^{\mu}\phi$ (arXiv:2512.09748) [src: Sect. 4.1.2, inline, text after Eq. 34] | — |
| Cubic Horndeski term | $-G_{3}\Box\phi$ (arXiv:1901.07183) [src: Eq. 8] | — | $+G_{3}\Box\phi$ (arXiv:2512.09748) [src: Eq. 34] | — |
| Planck mass | absorbed in $G_{4}$ (arXiv:1901.07183) [src: Eq. 8] | effective $M_{*}^{2}$ (arXiv:1404.3713) [src: Eq. 51] | $M_{\rm Pl}$ and $G_{\rm N}$ with c kept (arXiv:2512.09748) [src: Eqs. 34, 48] | $m_{0}^{2}$ in the EFT action (hub atlas) |
| Speed of tensors | $c_{\rm GW}^{2}$ (arXiv:1901.07183) [src: Eq. 123] | $c_{\text{T}}^{2}=1+\alpha_{\textrm{T}}>0\,.$ (arXiv:1404.3713) [src: Sect. 3.3, unnumbered display after Eq. 15] | $c_{\rm GW}^{2}/c^{2}=1+\alpha_{\rm T}$ (arXiv:2512.09748) [src: Sect. 4.1.2, inline, text after Eq. 33] | — |

- f(R) is written as $R+f(R)$ in the Euclid review (arXiv:2512.09748, Eq. 48) and as f(Q) for the whole Lagrangian in the f(Q) review (arXiv:2309.15958, Eq. 6.3): a sign or an additive R must be checked before comparing papers.
- Fourier conventions do not enter the equations of this skill except through $k^{2}$ in the Poisson-type equations (arXiv:2512.09748, Eqs. 29–30), which are written for one Fourier mode.
- Time: Kobayashi and Bellini & Sawicki use cosmic time t and its Hubble rate H; Ezquiaga & Zumalacárregui's tensor equation uses conformal time and $\mathcal{H}$ (arXiv:1807.09241, Eq. 55); hi_class uses conformal time (hub atlas).
- Gauge: the EFT of dark energy is written in unitary gauge, uniform-field hypersurfaces (arXiv:1210.0201; arXiv:1411.3712) [src: abstracts]; quasi-static results are given in Newtonian gauge (arXiv:1901.07183, Sect. 3.4.2).

## Horndeski, beyond Horndeski and DHOST
<!-- key: horndeski-beyond-horndeski-and-dhost -->

Kobayashi's review (arXiv:1901.07183, Kobayashi 2019) is the reference for this section. He writes $X:=-g^{\mu\nu}\phi_{\mu}\phi_{\nu}/2$ (arXiv:1901.07183) [src: Sect. 4.1, inline, text after Eq. 118], subscripts on φ denoting covariant derivatives; other definitions of X are listed in the hub atlas (`theoretical-cosmology/references/conventions.md`, "Dark-energy and modified-gravity parameterisations and their signs").

Horndeski theory (generalised Galileons):

- Lagrangian, the two rows of one display: ${\cal L}=G_{2}(\phi,X)-G_{3}(\phi,X)\Box\phi+G_{4}(\phi,X)R+G_{4X}\left[(\Box\phi)^{2}-\phi^{\mu\nu}\phi_{\mu\nu}\right]\quad+G_{5}(\phi,X)G^{\mu\nu}\phi_{\mu\nu}-\frac{G_{5X}}{6}\left[(\Box\phi)^{3}-3\Box\phi\phi^{\mu\nu}\phi_{\mu\nu}+2\phi_{\mu\nu}\phi^{\nu\lambda}\phi_{\lambda}^{\mu}\right],$ with $G_{2},\ldots,G_{5}$ arbitrary functions of φ and X (arXiv:1901.07183) [src: Eq. 8].
- Deffayet et al. obtained the most general scalar theories with second-order field equations on flat space-time and their curved space-time extensions, which include k-essence, Galileons, k-mouflage and kinetically braided scalars (arXiv:1103.3260, Deffayet et al. 2011) [src: abstract]; Kobayashi, Yamaguchi and Yokoyama showed in an appendix that Horndeski theory and the generalised Galileons are equivalent (arXiv:1105.5723, Kobayashi et al. 2011) [src: abstract]. Horndeski's original 1974 paper is pre-arXiv and was not read (see "Not verified").
- Tensor perturbations on a flat FLRW background are governed by ${\cal G}_{T}:=2\left[G_{4}-2XG_{4X}-X\left(H\dot{\phi}G_{5X}-G_{5\phi}\right)\right],$ [src: Eq. 42] and ${\cal F}_{T}:=2\left[G_{4}-X\left(\ddot{\phi}G_{5X}+G_{5\phi}\right)\right],$ (arXiv:1901.07183) [src: Eq. 43].
- Speed of gravitational waves in Horndeski theory: $c_{\rm GW}^{2}=\frac{G_{4}-X(\ddot{\phi}G_{5X}+G_{5\phi})}{G_{4}-2XG_{4X}-X(H\dot{\phi}G_{5X}-G_{5\phi})}.$ (arXiv:1901.07183) [src: Eq. 123]; it equals one irrespective of the background if $G_{4X}=0,\quad G_{5}=0.$ [src: Eq. 124].

Quasi-static limit in Horndeski theory (Kobayashi's Newtonian gauge puts Φ in $g_{00}$ and Ψ in $g_{ij}$, the reverse of Planck 2015 XIV, arXiv:1502.01590, Eq. 1):

- Metric: ${\rm d}s^{2}=-[1+2\Phi(t,\vec{x})]{\rm d}t^{2}+a^{2}[1-2\Psi(t,\vec{x})]\delta_{ij}{\rm d}x^{i}{\rm d}x^{j},$ (arXiv:1901.07183) [src: Eq. 87].
- Modified Poisson equation: $\frac{1}{a^{2}}\partial^{2}\Phi=4\pi G_{\rm eff}(t)\delta\rho,\quad 8\pi G_{\rm eff}:=\frac{b_{0}{\cal F}_{T}-b_{1}^{2}}{b_{0}{\cal G}_{T}^{2}+2b_{1}b_{2}{\cal G}_{T}+b_{2}^{2}{\cal F}_{T}}.$ (arXiv:1901.07183) [src: Eq. 100], with $b_{1}:=\frac{1}{H}\left[\dot{\cal G}_{T}+H({\cal G}_{T}-{\cal F}_{T})\right],$ [src: Eq. 93] and $b_{2}:=\frac{1}{H}\left(H{\cal G}_{T}-\Theta\right).$ [src: Eq. 94].
- Slip: $\eta(t):=\frac{\Psi}{\Phi}=\frac{b_{0}{\cal G}_{T}+b_{1}b_{2}}{b_{0}{\cal F}_{T}-b_{1}^{2}}$ (arXiv:1901.07183) [src: Eq. 101]. Kobayashi warns that these expressions cannot be used for f(R) and chameleon models, because the mass term was dropped [src: Sect. 3.4.2, text after Eq. 101].
- The growth equation keeps its form, $\ddot{\delta}+2H\dot{\delta}=\frac{1}{a^{2}}\partial^{2}\Phi,$ (arXiv:1901.07183) [src: Eq. 104].

Beyond Horndeski and DHOST:

- Disformal transformation $g_{\mu\nu}\to\tilde{g}_{\mu\nu}=C(\phi,X)g_{\mu\nu}+D(\phi,X)\phi_{\mu}\phi_{\nu}.$ (arXiv:1901.07183) [src: Eq. 112], invertible if $C(C-XC_{X}+2X^{2}D_{X})\neq 0.$ [src: Eq. 113]; a Horndeski theory transformed with X-dependent C or D has higher-order field equations but keeps 2+1 degrees of freedom [src: Sect. 4.1, text after Eq. 113].
- Quadratic DHOST Lagrangian ${\cal L}=f(\phi,X)R+\sum_{I=1}^{5}A_{I}(\phi,X)L_{I},$ (arXiv:1901.07183) [src: Eq. 114], with the two rows $L_{1}=\phi_{\mu\nu}\phi^{\mu\nu},\quad L_{2}=(\Box\phi)^{2},\quad L_{3}=\Box\phi\phi^{\mu}\phi^{\nu}\phi_{\mu\nu}\quad L_{4}=\phi^{\mu}\phi_{\mu\alpha}\phi^{\alpha\nu}\phi_{\nu},\quad L_{5}=(\phi^{\mu}\phi^{\nu}\phi_{\mu\nu})^{2}.$ [src: Eq. 115]. Horndeski is the case $A_{2}=-A_{1}=f_{X}$ and $A_{3}=A_{4}=A_{5}=0$ [src: Sect. 4.1, inline, text after Eq. 115]; three degeneracy conditions leave three free functions [src: Sect. 4.1, text after Eq. 115].
- The systematic classification of degenerate theories is Langlois & Noui's (arXiv:1510.06930, Langlois & Noui 2015) [src: abstract].
- Class Ia, which contains Horndeski: $A_{2}=-A_{1},$ (arXiv:1901.07183) [src: Eq. 116], with $A_{4}$ and $A_{5}$ fixed by Eqs. 117–118 and f, $A_{1}$, $A_{3}$ free [src: Sect. 4.1, text after Eq. 118].
- GLPV ("beyond Horndeski") theory, the two rows of one display: ${\cal L}_{\rm GLPV}=fR+f_{X}\left[(\Box\phi)^{2}-\phi_{\mu\nu}\phi^{\mu\nu}\right]\quad+A_{3}\left\{X\left[(\Box\phi)^{2}-\phi_{\mu\nu}\phi^{\mu\nu}\right]+\Box\phi\phi^{\mu}\phi^{\nu}\phi_{\mu\nu}-\nabla_{\mu}X\nabla^{\mu}X\right\}.$ (arXiv:1901.07183) [src: Eq. 120]; Gleyzes et al. introduced it and showed that the propagating degrees of freedom obey second-order equations, and that the scalar affects the sound speed of minimally coupled matter (arXiv:1404.6495, Gleyzes et al. 2014) [src: abstract].
- In quadratic DHOST the tensor action is $S^{(2)}_{\rm tensor}=\frac{1}{4}\int{\rm d}t{\rm d}^{3}xa^{3}\left[(f+2XA_{1})\dot{h}_{ij}^{2}-\frac{f}{a^{2}}(\partial_{k}h_{ij})^{2}\right].$ (arXiv:1901.07183) [src: Eq. 126], so that $c_{\rm GW}^{2}=\frac{f}{f+2XA_{1}},$ [src: Eq. 127].

## f(R) gravity
<!-- key: f-r-gravity -->

Reviews: Sotiriou & Faraoni cover the metric, Palatini and metric-affine formalisms, equivalence with other theories and viability criteria (arXiv:0805.1726, Sotiriou & Faraoni 2010) [src: abstract]; De Felice & Tsujikawa cover inflation, dark energy, local gravity constraints, perturbations and spherically symmetric solutions (arXiv:1002.4928, De Felice & Tsujikawa 2010) [src: abstract]. Only the metric formalism is treated below.

- Action, as the Euclid review writes it (the function added to R): $S=\frac{c^{4}}{16\pi G_{\rm N}}\int{\mathrm{d}^{4}x\sqrt{-g}\left[R+f(R)\right]}\,,$ (arXiv:2512.09748, Euclid Collaboration 2025) [src: Eq. 48], with $f_{R}=\mathrm{d}f/\mathrm{d}R$ [src: Sect. 5.1, inline, text after Eq. 48]. The fifth force is screened in the Solar System by the chameleon mechanism [src: Sect. 5.1].
- Hu–Sawicki model: $f(R)=-m^{2}{c_{1}(R/m^{2})^{n}\over c_{2}(R/m^{2})^{n}+1}\,,$ with $c_{1}$, $c_{2}$ dimensionless (arXiv:0705.1158, Hu & Sawicki 2007) [src: Eq. 3]. For n = 1 and $|f_{R}|\ll1$ the Euclid review uses $f(R)=-6\Omega_{\mathrm{DE},0}\frac{H_{0}^{2}}{c^{2}}+|f_{R0}|\frac{\bar{R}_{0}^{2}}{R}\,,$ with $f_{R0}<0$ the free parameter and ΛCDM recovered as $f_{R0}\rightarrow 0$ (arXiv:2512.09748) [src: Eq. 49].
- Linear growth (Pogosian & Silvestri, arXiv:0709.0296, as quoted by the Euclid review, for negligible matter anisotropic stress): $\mu(a,k)=\frac{1}{1+f_{R}(a)}\frac{1+4k^{2}a^{-2}m_{f_{R}}^{-2}(a)}{1+3k^{2}a^{-2}m_{f_{R}}^{-2}(a)}\,,$ (arXiv:2512.09748) [src: Eq. 50], with the fifth-force scale $m_{f_{R}}(a)=\frac{H_{0}}{c\sqrt{2|f_{R0}|}}\frac{\left(4\Omega_{\mathrm{DE},0}+\Omega_{\mathrm{m},0}a^{-3}\right)^{3/2}}{4\Omega_{\mathrm{DE},0}+\Omega_{\mathrm{m},0}}\,,$ [src: Eq. 51] and $\Sigma(a)=\frac{1}{1+f_{R}(a)}\,.$ [src: Eq. 52]. Growth is scale-dependent [src: Sect. 5.1].
- Pogosian & Silvestri find that growth in f(R) is enhanced with no small-scale instability from the attractive fifth force, and that viable models must closely mimic ΛCDM in the background (arXiv:0709.0296) [src: abstract].
- In the α basis, f(R) has no kineticity: $\alpha_{\rm K}$ "is not present at all" in f(R) (arXiv:1404.3713) [src: Sect. 3.1].

## Massive gravity and bigravity
<!-- key: massive-gravity-and-bigravity -->

De Rham's Living Review (arXiv:1401.4173, de Rham 2014) is the reference; "Massive Gravity @ 15" (arXiv:2607.15507, de Rham 2026) is the 2026 status review. <!-- num: not a value -->

- Ghost-free (dRGT) massive gravity, written as the review prints it (called a Lagrangian, with the integral): $\mathcal{L}_{\rm mGR}=\frac{M_{\rm Pl}^{2}}{2}\int\,\mathrm{d}^{4}x\sqrt{-g}\left(R+\frac{m^{2}}{2}\left(\mathcal{L}_{2}[\mathcal{K}]+\alpha_{3}\mathcal{L}_{3}[\mathcal{K}]+\alpha_{4}\mathcal{L}_{4}[\mathcal{K}]\right)\right)\,,$ (arXiv:1401.4173) [src: Eq. 5.37]; for a general reference metric $f_{\mu\nu}$, $\mathcal{K}^{\mu}_{\nu}=\delta^{\mu}_{\nu}-\sqrt{g^{\mu\alpha}f_{\alpha\nu}}$ [src: Sect. 8.2.1, inline].
- De Rham, Gabadadze and Tolley constructed covariant non-linear theories ghost-free in the decoupling limit to all orders, with the Hamiltonian constraint kept up to quartic order away from it (arXiv:1011.1232, de Rham et al. 2010) [src: abstract]. The theory propagates exactly five degrees of freedom and its strong-coupling scale is raised to its maximal value (arXiv:2607.15507) [src: abstract].
- Bigravity: giving dynamics to the reference metric keeps the theory free of the Boulware–Deser ghost, a massless spin-2 field interacting with a massive one (arXiv:1109.3515, Hassan & Rosen 2011) [src: abstract].
- Higuchi bound: on de Sitter the linear theory is free of ghosts and tachyons only for m ≡ 0 or $m^{2}>2H^{2}$; in d dimensions $m^{2}>(d-2)H^{2}$; for $0<m^{2}<2H^{2}$ the helicity-0 mode is a ghost (arXiv:1401.4173) [src: Sect. 8.3.6, "Linearized theory and Higuchi bound", inline]. The partially massless point $m^{2}=2H^{2}$ is a linear artefact, infinitely strongly coupled non-linearly [src: same place].
- Cosmology: there are no non-trivial spatially flat (or closed) FLRW solutions in massive gravity with a Minkowski reference metric (arXiv:1401.4173) [src: Sect. 12.2.1]; D'Amico et al. found that the constraint removing the Boulware–Deser ghost forbids homogeneous and isotropic solutions, while approximately FRW domains of the size of the inverse graviton mass exist (arXiv:1108.5231, D'Amico et al. 2011) [src: abstract].
- In bigravity with two fluids, each coupled to one metric, the Higuchi-ghost condition is guaranteed on the healthy branch of background solutions, and avoiding the gradient instability constrains the parameters weakly (arXiv:1404.0008, De Felice et al. 2014) [src: abstract].

## Vector–tensor theories
<!-- key: vector-tensor-theories -->

- Generalised Proca: a vector field with derivative self-interactions whose coefficients are fixed by the degeneracy of the Hessian, so that only three physical degrees of freedom propagate; its longitudinal mode carries the Galileon interactions, and the curved space-time extension ("Horndeski Proca") has second-order equations (arXiv:1402.7026, Heisenberg 2014) [src: abstract]. The cubic term on flat space-time is $\mathcal{L}_{3}=f_{3}(A^{2})\;\;\partial\cdot A$ (arXiv:1402.7026) [src: Sect. 2, unnumbered display].
- Cosmology up to quintic order: with a temporal vector component and a matter fluid there are de Sitter solutions for late-time acceleration, with no-ghost and no-Laplacian-instability conditions for tensor, vector and scalar modes in the small-scale limit; in the concrete examples, which include vector Galileons, the de Sitter fixed point is always a stable attractor (arXiv:1603.05806, De Felice et al. 2016) [src: abstract].
- Einstein–aether: a dynamical unit timelike vector $u^{a}$ breaks local Lorentz invariance "spontaneously"; the action restricted to $\nabla_{[a}u_{b]}$ develops gradient singularities, which the symmetrised derivative may cure (arXiv:gr-qc/0007031, Jacobson & Mattingly 2000) [src: abstract].
- The EFT of dark energy has been extended to accommodate scalar–tensor and vector–tensor theories in one description, with the boundaries between classes parameterised universally (arXiv:2405.04265, Aoki et al. 2024) [src: abstract].

## Teleparallel and non-metricity theories
<!-- key: teleparallel-and-non-metricity-theories -->

The "geometrical trinity" describes gravity by curvature (GR), torsion (teleparallel equivalent, TEGR, and f(T)) or non-metricity (symmetric teleparallel equivalent, STEGR, and f(Q)). Reviews: Bahamonde et al. place teleparallel gravity within the metric-affine approach and survey f(T)-type theories, their astrophysics and cosmology (arXiv:2106.13793, Bahamonde et al. 2021) [src: abstract]; Heisenberg reviews f(Q) gravity (arXiv:2309.15958, Heisenberg 2023) [src: abstract].

- Coincident GR: an exceptional symmetric teleparallel class is consistent with a vanishing affine connection, giving a formulation of GR whose action is the Hilbert action purged of its boundary term; its generalisations admit analytic self-accelerating solutions (arXiv:1710.03116, Beltrán Jiménez et al. 2017) [src: abstract].
- f(Q) cosmology in the coincident gauge with $\Gamma^{\alpha}{}_{\mu\nu}=0$ and a flat FLRW metric with lapse N(t) (arXiv:2309.15958) [src: Eq. 6.1]: the non-metricity scalar is $\mathbb{Q}=6\frac{H^{2}}{N^{2}}\,,$ (arXiv:2309.15958) [src: Eq. 6.2], and the symmetry-reduced action is $\mathcal{S}[N,a]\coloneqq-\frac{1}{2\kappa}\int_{\mathcal{M}}\mathrm{d}t\,\mathrm{d}^{3}\vec{x}\,a(t)^{3}\,N(t)\,f(\mathbb{Q})\,,$ [src: Eq. 6.3], which keeps a time-reparametrisation invariance [src: Sect. 6.1, text after Eq. 6.3].
- `[der]` In this convention f carries the whole gravitational Lagrangian, with the sign printed in Eq. 6.3; check it before comparing with an f(R) written as R + f(R) (arXiv:2512.09748, Eq. 48).
- Degrees of freedom: in the most popular modified teleparallel models the local symmetry of the flat connection is broken "but not stably so", hence strong coupling; Hamiltonian analyses give contradictory results (arXiv:2405.14184, Golovnev 2024) [src: abstract].

## Non-local gravity
<!-- key: non-local-gravity -->

- Deser–Woodard: non-local modifications inspired by quantum loop corrections allow a delayed response to the transition from radiation to matter domination and avoid the usual fine tuning, with negligible Solar-System effects (arXiv:0706.2151, Deser & Woodard 2007) [src: abstract]. Woodard's review covers causal and conserved field equations, reconstruction of a given expansion history, why no elaborate screening is needed, degrees of freedom and kinetic stability (arXiv:1401.0254, Woodard 2014) [src: abstract].
- RR model (Maggiore–Mancarella): a term $m^2 R\,\Box^{-2}R$ added to the Einstein–Hilbert action affects only the non-radiative sector; the graviton stays massless, with no propagating ghost, no vDVZ discontinuity and no Vainshtein radius (arXiv:1402.0448, Maggiore & Mancarella 2014) [src: abstract]. Belgacem et al. motivate the non-local terms as an infrared mass scale generated dynamically in the quantum effective action, which selects the RR model as a dynamical mass for the conformal mode (arXiv:1712.07066, Belgacem et al. 2017) [src: abstract].
- Local limit of non-local gravity (a teleparallel extension of GR with a "gravitational susceptibility" S(x)): every GR dark-energy model with w(z) has a counterpart with w = −1 and a suitable S(z), indistinguishable in the background, and a cosmological constant is not allowed (arXiv:2609.26517, Hemmatian et al. 2026) [src: abstract].

## Screening mechanisms
<!-- key: screening-mechanisms -->

Joyce, Jain, Khoury and Trodden classify screening by the field quantity that becomes large near matter: deep potentials (chameleon, symmetron; their Sect. 5) and higher-derivative interactions (kinetic screening and the Vainshtein mechanism; their Sect. 6) (arXiv:1407.0059, Joyce et al. 2014) [src: outline, Sects. 3.1–3.2, 5, 6].

Screening by the value of the field:

- With a conformal coupling A(φ) to matter, the scalar obeys $\square\phi=V_{{\rm eff}\,,\phi}(\phi)~~~~~~~~~~~~{\rm where}~~~~~~~~V_{\rm eff}(\phi)=V(\phi)+A(\phi)\rho~.$ (arXiv:1407.0059) [src: Eq. 5.8], with ρ the density conserved in the Einstein frame [src: Sect. 5, text before Eq. 5.8].
- Chameleon: the mass of the field depends on the local density, large on Earth and small in the Solar System (arXiv:astro-ph/0309300, Khoury & Weltman 2003) [src: abstract].
- Symmetron: $V_{\rm eff}(\phi)=\frac{1}{2}\left(\frac{\rho}{M^{2}}-\mu^{2}\right)\phi^{2}+\frac{\lambda}{4}\phi^{4}~.$ (arXiv:1407.0059) [src: Eq. 5.45]; at high density the field is drawn to φ = 0, where its coupling vanishes and the $\phi\to-\phi$ symmetry is restored; at low density it couples with gravitational strength (arXiv:1001.4525, Hinterbichler & Khoury 2010) [src: abstract].

Screening by derivatives of the field:

- k-mouflage: a scalar mixed with the graviton makes gravity stronger at large distances and is screened at small distances, large curvature, by an analogue of the Vainshtein mechanism (arXiv:0905.2943, Babichev et al. 2009) [src: abstract].
- Vainshtein (cubic galileon around a spherical source): $\phi^{\prime}(r)=\frac{3\Lambda^{3}r}{4}\left(-1+\sqrt{1+\frac{1}{9\pi}\left(\frac{r_{\rm V}}{r}\right)^{3}}\right)\,,$ [src: Eq. 6.39] with $r_{\rm V}\equiv\frac{1}{\Lambda}\left(\frac{gM}{M_{\rm Pl}}\right)^{1/3}\ .$ (arXiv:1407.0059) [src: Eq. 6.40]. Outside $r_{\rm V}$ the field mediates a long-range force; the classical theory is predictive between the inverse cutoff and $r_{\rm V}$ [src: Fig. 9 caption]. As printed, the caption writes that intermediate regime as $\Lambda\ll r\ll r_{\rm V}$, while the same caption calls $\Lambda^{-1}$ the inverse cutoff and places the non-predictive region at $r\ll\Lambda^{-1}$.
- Beyond Horndeski, outside and near the source the two potentials coincide, with the cosmological, time-dependent coupling, but inside the source the attraction is not set by the enclosed mass alone and the potentials differ: the screening is broken inside matter (arXiv:1411.4130, Kobayashi et al. 2014) [src: abstract].
- Beyond spherical symmetry, in the EFT of dark energy with generic "beyond Horndeski" parameters, the multipole moments of the fifth force are not screened where the monopole is, and oscillate (arXiv:2607.09098, Kobayashi & Takadera 2026) [src: abstract].
- Coexisting mechanisms: a chameleon added to a Vainshtein-screened theory resolves the galileon void pathology, suppresses or removes the Vainshtein radius around massive sources, and the Vainshtein term shrinks the chameleon's screened core (arXiv:2610.36166, Sirera et al. 2026) [src: abstract].

## The EFT of dark energy and parameterised frameworks
<!-- key: the-eft-of-dark-energy-and-parameterised -->

Effective field theory of dark energy (EFT of DE):

- Gubitosi, Piazza and Vernizzi write the most general unitary-gauge action consistent with the residual spatial diffeomorphisms, for the metric universally coupled to matter; the background depends on three operators only and all others start at quadratic order in the perturbations (arXiv:1210.0201, Gubitosi et al. 2013) [src: abstract]. Their action and the one of Planck 2015 XIV (arXiv:1502.01590) are transcribed side by side in the hub atlas (`theoretical-cosmology/references/conventions.md`, "Dark-energy and modified-gravity parameterisations and their signs"): the sign of Λ and the name of the coefficient of R differ between the two.
- Gleyzes, Langlois and Vernizzi's ADM formulation on uniform-field hypersurfaces covers quintessence, F(R), scalar–tensor, Horndeski and beyond, and Hořava–Lifshitz theories; linear perturbations are characterised by five time-dependent functions (arXiv:1411.3712, Gleyzes et al. 2014) [src: abstract].

Frusciante & Perenon review the EFT of dark energy as a Lagrangian description of perturbations depending on functions of time, some of which are non-minimal couplings representing deviations from GR (arXiv:1907.03150, Frusciante & Perenon 2019) [src: abstract].

The α basis (Bellini & Sawicki, arXiv:1404.3713, signature −+++):

- Linear structure in Horndeski theory is fixed by four dimensionless functions of time $\alpha_{i}(t)$ together with $H(t)$ and the matter density today; no linear measurement can say anything about the theory beyond these (arXiv:1404.3713) [src: Sect. 3.1]. This holds when the scalar rolls monotonically, $\dot\phi\neq0$ [src: Sect. 3.1].
- Effective Planck mass and its run rate: $M_{*}^{2}\equiv 2\left(G_{4}-2XG_{4X}+XG_{5\phi}-\dot{\phi}HXG_{5X}\right)$ [src: Eq. 51] and $HM_{*}^{2}\alpha_{\textrm{M}}\equiv\frac{\mathrm{d}}{\mathrm{d}t}M_{*}^{2}$ (arXiv:1404.3713) [src: Eq. 52]. Kineticity $\alpha_{\rm K}$ and braiding $\alpha_{\rm B}$ are defined in Eqs. 53–54 (multi-row displays, not transcribed here).
- Meaning (arXiv:1404.3713) [src: Sect. 3.1]: $\alpha_{\rm K}$, kineticity, the only contribution of perfect-fluid models, absent in f(R); $\alpha_{\rm B}$, braiding, mixing of scalar and metric kinetic terms, makes dark energy cluster; $\alpha_{\rm M}$, Planck-mass run rate, creates anisotropic stress; $\alpha_{\rm T}$, tensor speed excess, also creates anisotropic stress. `[der]` Bellini & Sawicki's own words are "Contributions from" $G_3$, $G_4$, $G_5$ for $\alpha_{\rm B}$ and from $G_4$, $G_5$ for $\alpha_{\rm M}$ and $\alpha_{\rm T}$.
- Quadratic action of the propagating modes, as printed: $S_{2}=\int\mathrm{d}t\mathrm{d}^{3}xa^{3}\left[Q_{\text{S}}\left(\dot{\zeta}^{2}-\frac{c_{\text{s}}^{2}}{a^{2}}(\partial_{i}\zeta)\right)+Q_{\text{T}}\left(\dot{h}_{ij}^{2}-\frac{c_{\text{T}}^{2}}{a^{2}}(\partial_{k}h_{ij})^{2}\right)\right]\,,$ (arXiv:1404.3713) [src: Eq. 13]; as printed in v3 the scalar gradient term $(\partial_{i}\zeta)$ carries no square, while the tensor term $(\partial_{k}h_{ij})^{2}$ does.
- Scalar stability, the two rows of one display: $Q_{\text{S}}=\frac{2M_{*}^{2}D}{(2-\alpha_{\textrm{B}})^{2}}>0\,,\qquad D\equiv\alpha_{\textrm{K}}+\frac{3}{2}\alpha_{\textrm{B}}^{2}\,,\quad c_{\text{s}}^{2}=-\frac{\left(2-\alpha_{\textrm{B}}\right)\left[\dot{H}-\frac{1}{2}H^{2}\alpha_{\textrm{B}}\left(1+\alpha_{\textrm{T}}\right)-H^{2}\left(\alpha_{\textrm{M}}-\alpha_{\textrm{T}}\right)\right]-H\dot{\alpha}_{\textrm{B}}+\tilde{\rho}_{\textrm{m}}+\tilde{p}_{\textrm{m}}}{H^{2}D}>0\,,$ (arXiv:1404.3713) [src: Eq. 14].
- Tensor stability, the two rows of one display: $Q_{\text{T}}=\frac{M_{*}^{2}}{8}>0\,,\quad c_{\text{T}}^{2}=1+\alpha_{\textrm{T}}>0\,.$ (arXiv:1404.3713) [src: Eq. 15]. The no-ghost condition for scalars reduces to D > 0, and $c_{\rm s}$ is the eikonal-limit speed, a function of time only, not the scale-dependent $C^{2}$ of $\delta\mathcal{P}\equiv C^{2}\delta\mathcal{E}$ [src: Sect. 3.3].
- The hi_class normalisation of the Horndeski functions and its $M_{*}^{2}$ (arXiv:1605.06102, Eq. 2.9) are in the hub atlas; hi_class writes the time derivative of the field in the $G_{5X}$ term with conformal time, $H\phi^{\prime}/a$, where Bellini & Sawicki write $\dot{\phi}H$.

Phenomenological functions:

- μ (Poisson equation of the time–time potential), Σ (lensing potential), η (slip) and Q are defined in Planck 2015 XIV (arXiv:1502.01590, Sect. 3.2.2, Eqs. 3–6); the definitions and the metric they assume are transcribed in the hub atlas. Planck 2015 XIV's Ψ sits in $g_{00}$ (arXiv:1502.01590, Eq. 1), Kobayashi's Φ sits in $g_{00}$ (arXiv:1901.07183, Eq. 87): the slip η is Φ/Ψ in the first and Ψ/Φ in the second, each the ratio of the spatial to the temporal potential.
- In Horndeski theory the quasi-static $G_{\rm eff}$ and η are those of `formalism.md`, Horndeski section (arXiv:1901.07183, Eqs. 100–101).

The Euclid review's forms (arXiv:2512.09748, Newtonian gauge with Ψ in $g_{00}$, units with c):

- Line element $\mathrm{d}s^{2}=-(1+2\Psi)\,c^{2}\,\mathrm{d}t^{2}+a^{2}(t)\,(1-2\Phi)\,\delta_{ij}\,\mathrm{d}x^{i}\,\mathrm{d}x^{j}\,,$ (arXiv:2512.09748) [src: Eq. 28].
- μ with matter anisotropic stress σ, following Silvestri et al. 2013: $-k^{2}\Psi=\frac{4\pi\,G_{\rm N}}{c^{2}}\,a^{2}\mu(a,k)\left[\bar{\rho}\Delta+3\left(\bar{\rho}+\frac{\bar{p}}{c^{2}}\right)\sigma\right]\,,$ (arXiv:2512.09748) [src: Eq. 29]; Σ is defined by Eq. 30, a two-row display not transcribed here.
- With $\eta(a,k)=\Phi/\Psi$ and no matter anisotropic stress, $\Sigma=\frac{1}{2}\mu(1+\eta)\,.$ (arXiv:2512.09748) [src: Eq. 31]; all three equal one in GR [src: Sect. 4.1.1].
- Late-time parameterisation (from DES, Abbott et al. 2019): $\mu(z)=1+\mu_{0}\,\frac{\Omega_{\rm DE}(z)}{\Omega_{\rm DE}(z=0)}\,,$ [src: Eq. 32] and $\Sigma(z)=1+\Sigma_{0}\,\frac{\Omega_{\rm DE}(z)}{\Omega_{\rm DE}(z=0)}\,,$ (arXiv:2512.09748) [src: Eq. 33], with a ΛCDM background for $\Omega_{\rm DE}(z)$ [src: Sect. 4.1.1].
- The Euclid EFT case: luminal Horndeski with no coupling to R, ${\cal L}_{\rm H}=G_{2}(\phi,X)+G_{3}(\phi,X)\Box\phi+\frac{1}{2}M_{\rm Pl}^{2}R\,.$ with $X=-\tfrac{1}{2}\nabla_{\mu}\phi\nabla^{\mu}\phi$ (arXiv:2512.09748) [src: Eq. 34]; the $G_{3}$ term carries a plus sign here and a minus sign in Kobayashi's Eq. 8 (arXiv:1901.07183). The braiding is parameterised as $\alpha_{\rm B}=\alpha_{\rm B,0}\,a\,,$ with $\alpha_{\rm T}=0$ from GW170817 and $\alpha_{\rm M}=0$ for simplicity (arXiv:2512.09748) [src: Eq. 36, Sect. 4.1.2]; Euclid writes $c_{\rm GW}^{2}/c^{2}=1+\alpha_{\rm T}$ [src: Sect. 4.1.2, inline, text after Eq. 33].
- Jordan–Brans–Dicke: $S_{\rm BD}=\int\mathrm{d}^{4}x\sqrt{-g}\left[\frac{c^{4}}{16\pi}\left({\phi}R-\frac{\omega_{\rm BD}}{\phi}g^{\mu\nu}\partial_{\mu}\phi\partial_{\nu}\phi-2\Lambda\right)+\mathcal{L}_{\rm m}\right]\,,$ with $\omega_{\rm BD}$ its only dimensionless parameter (arXiv:2512.09748) [src: Eq. 37].

Parameterised post-Friedmann (PPF): three regimes (large scales tied to the expansion history, an intermediate scalar–tensor regime with a modified Poisson equation, and small scales where modifications are suppressed), described by three free functions and two transition scales; it reproduces linear f(R) and DGP calculations, and its non-linear halo-model description "remains an ansatz" (arXiv:0708.1190, Hu & Sawicki 2007) [src: abstract].

## The tensor sector
<!-- key: the-tensor-sector -->

- Parameterised propagation on FLRW, conformal time: $h^{\prime\prime}_{ij}+(2+\nu)\mathcal{H}h^{\prime}_{ij}+(c_{g}^{2}k^{2}+m^{2}a^{2})h_{ij}=\Pi_{ij}\,,$ with ν an extra friction, $c_{g}$ the propagation speed, m an effective mass and $\Pi_{ij}$ a source from the additional fields (arXiv:1807.09241, Ezquiaga & Zumalacárregui 2018) [src: Eq. 55]. In Horndeski theory the speed is Eq. 123 of Kobayashi and in the α basis $c_{\text{T}}^{2}=1+\alpha_{\textrm{T}}>0\,.$ (arXiv:1404.3713) [src: Sect. 3.3, unnumbered display after Eq. 15]; the friction from a running Planck mass is noted by Kobayashi (arXiv:1901.07183) [src: Sect. 4.2, last paragraph]. Modified luminosity distances of standard sirens belong to `thcosmo-cosmological-gravitational-waves`.
- Ezquiaga & Zumalacárregui's review classifies theories into those that break fundamental assumptions, those with additional fields and those with massive gravitons, and lists the propagation tests: anomalous speed, massive graviton, Lorentz-violating dispersion, modified GW luminosity distance, extra polarisations and GW oscillations (arXiv:1807.09241) [src: abstract].

## Not verified
<!-- key: not-verified -->

- Horndeski's 1974 paper and Vainshtein's 1972 paper are pre-arXiv and were not read; Horndeski theory is quoted from Kobayashi's review (arXiv:1901.07183) and the Vainshtein solution from Joyce et al. (arXiv:1407.0059).
- The kineticity and braiding definitions in terms of the Horndeski functions (arXiv:1404.3713, Eqs. 53–54) and the Σ equation of the Euclid review (arXiv:2512.09748, Eq. 30) are multi-row displays not transcribed.
- A factor or sign relating the $\alpha_{\rm B}$ of Bellini & Sawicki to that of hi_class or EFTCAMB was not found in a paper in this run; none is given.
- The f(T) and f(Q) field equations and Friedmann equations beyond Eqs. 6.1–6.3 of arXiv:2309.15958 were not transcribed; the generalised Proca Lagrangians beyond the cubic term were not transcribed.
- The DHOST class Ia coefficients $A_{4}$ and $A_{5}$ (arXiv:1901.07183, Eqs. 117–118) were read but not transcribed here.
