# Screening mechanisms — thcosmo-modified-gravity dossier

Scope: how the chameleon thin shell, the symmetron, k-mouflage and the Vainshtein mechanism are derived around a spherical source (thin-shell factor, screening radius, k-mouflage and Vainshtein radii), the criterion each imposes on the Newtonian potential, and which theory screens by which mechanism.
Snapshot: 2026-11-04.
From: Joyce et al. arXiv:1407.0059, Sects. 3, 5 and 6; Kobayashi arXiv:1901.07183, Sect. 5; Euclid review arXiv:2512.09748, Sect. 4.1.4 — `references/subtopics.tsv`, row `screening`.
Audit questions: (3) How do chameleon, symmetron, k-mouflage and Vainshtein screening work (thin shell, Vainshtein radius), and which applies to which theory?

Already in the reference files, and not repeated here: the effective potential with a conformal coupling (Joyce et al. Eq. 5.8), the symmetron effective potential (Eq. 5.45), the cubic-galileon profile and Vainshtein radius (Eqs. 6.39–6.40) with the slip of the Fig. 9 caption, the breaking of Vainshtein screening inside matter beyond Horndeski, the unscreened multipoles and the chameleon–Vainshtein symbiosis (`formalism.md#screening-mechanisms`); f(R) as a chameleon and its μ, Σ (`formalism.md#f-r-gravity`); the chameleon no-go theorem (`results.md#theorems-and-no-go-results`); screening in N-body codes (`approximations.md#screening-in-simulations`); the k-mouflage, Galileon and DGP model cards (`models.md#k-mouflage`, `models.md#covariant-galileons-cubic-quartic-quintic`, `models.md#dgp-braneworld-self-accelerating-and-normal`).

## Conventions
<!-- key: conventions -->

- Joyce, Jain, Khoury and Trodden (arXiv:1407.0059) take a linear conformal coupling, $A(\phi)\simeq 1+\xi\frac{\phi}{M_{\rm Pl}}\,.$ (arXiv:1407.0059) [src: Eq. 5.10], for the chameleon, and a matter coupling $\frac{g}{M_{\rm Pl}}\phi T$ for kinetic and Vainshtein screening, with $g\sim{\cal O}(1)$ "for gravitational strength coupling" [src: Sect. 6.2.1, text after Eq. 6.32]; the cubic galileon carries the kinetic normalisation $-3(\partial\phi)^2$, chosen "so that the decoupling limit of the DGP model corresponds to exactly g=1" [src: Sect. 6.2.1]. <!-- eq: notation -->
- Burrage and Sakstein (arXiv:1709.09071, Burrage & Sakstein 2017) write the coupling as β(φ), the fifth force as $F_{5}=-\frac{\beta(\phi)}{{M_{\rm{pl}}}}\nabla\phi$ (arXiv:1709.09071) [src: Eq. 2.5], and use $g_{00}=-a^{2}(1+2\Phi)$ in their f(R) discussion [src: Sect. 3.1.1].
- Brax and Valageas (arXiv:1403.5420, Brax & Valageas 2014) write the fluctuation Lagrangian with a kinetic function Z, a mass m and a coupling β, and the coupling as $\beta(\varphi)=M_{\rm Pl}\frac{\mathrm{d}\ln A(\varphi)}{\mathrm{d}\varphi}$ (arXiv:1403.5420) [src: Eq. 4]; their total potential is $\Psi=\Psi_{\rm N}+{\beta(\varphi_{0})}\frac{\delta\varphi}{M_{\rm Pl}},$ (arXiv:1403.5420) [src: Eq. 2], with $\Psi_{\rm N}$ the Newtonian potential.
- Koyama (arXiv:1504.04623, Koyama 2016) writes the DGP Vainshtein solution with $r_{g}=2GM$ (arXiv:1504.04623) [src: Sect. 3.5, inline, text after Eq. 108] and β the DGP branch parameter. <!-- eq: notation -->
- The coupling normalisations ξ, g, β of these papers are not converted into each other here.

## The derivation
<!-- key: the-derivation -->

### Step 1 — one classification: which quantity becomes large
<!-- key: step-1-one-classification-which-quantity -->

Joyce et al. sort mechanisms by "the nature of the screening criterion": screening "set by the local field value φ", "by the first derivative ∂φ" and "by the second derivative ∂²φ" (arXiv:1407.0059) [src: Sect. 3.2]. In terms of the source, they shut off the fifth force "when the gravitational potential Φ exceeds some critical value", Φ ≳ Λ [src: Eq. 3.5]; "when the local gravitational acceleration … exceeds some critical value", |∇Φ| ≳ Λ² [src: Eq. 3.6]; and "when the local curvature or density, R ∼ ∇²Φ, exceeds some critical value", |∇²Φ| ≳ Λ³ [src: Eq. 3.7]. Koyama, following the same reference, phrases the three routes through the fluctuation Lagrangian $-\frac{1}{2}Z^{\mu\nu}\partial_\mu\phi\partial_\nu\phi-V+\beta T$: "Large mass" (chameleon), "Small coupling" (dilaton and symmetron) and "Large kinetic term", by the first derivative (k-mouflage) or the second (Vainshtein) (arXiv:1504.04623) [src: Sect. 3.2, Eq. 78]. <!-- eq: notation -->

Brax and Valageas make the criteria quantitative from the linear quasi-static solution. With $Z=1$, $\Psi=\left[1+\frac{2\beta^{2}(\varphi_{0})}{1+m^{2}(\varphi_{0})a^{2}/k^{2}}\right]\,\Psi_{\rm N},$ (arXiv:1403.5420) [src: Eq. 6], and non-linear screening sets in when $|\delta\varphi|\sim|\varphi_{0}|$ (arXiv:1403.5420) [src: Sect. II.2, inline, text after Eq. 6], that is $\left|2\beta(\varphi_{0})\Psi_{\rm N}\right|\gtrsim\left|\frac{\varphi_{0}}{M_{\rm Pl}}\right|.$ (arXiv:1403.5420) [src: Eq. 7]. For kinetic models, $\Psi=\left[1+\frac{2\beta^{2}(\varphi_{0})}{Z(\varphi_{0})}\right]\,\Psi_{\rm N},$ [src: Eq. 10], screening when $Z(\varphi_{0})\gtrsim 1.$ [src: Eq. 11], with the expansion $Z(\varphi)=1+a(\varphi)\frac{(\partial\varphi)^{2}}{{\cal M}^{4}}+b(\varphi)L^{2}\frac{\Box\varphi}{M_{\rm Pl}}+\dots,$ (arXiv:1403.5420) [src: Eq. 12]; "Cubic and higher order derivatives are forbidden as they would induce equations of motions of the order larger than two", so this expansion "captures the essence of the possible screening mechanisms for theories with second order equations of motion" [src: Sect. II.3].

### Step 2 — chameleon: the thin shell
<!-- key: step-2-chameleon-the-thin-shell -->

For a sphere of radius R and constant density in an ambient medium, the static equation is $\phi^{\prime\prime}+\frac{2}{r}\phi^{\prime}=V_{,\phi}+\xi\frac{\rho}{M_{\rm Pl}}~,$ (arXiv:1407.0059) [src: Eq. 5.15], with the step density $\rho(r)=\left\{\begin{array}[]{l}\rho_{\rm obj.}~,~~~~~~~~r<R\\ \rho_{\rm amb.}~,~~~~~~~r>R\end{array}\right.~.$ [src: Eq. 5.16], regularity at the origin and $\phi\to\phi_{\rm amb.}$ at infinity [src: Sect. 5.1.2]. "For a sufficiently large body" the field sits at the interior minimum, $\phi\simeq\phi_{\rm obj.}~;~~~~~~~~~~~~r<R\,.$ [src: Eq. 5.17]; outside, within an ambient Compton wavelength, $\phi\simeq\frac{A}{r}+B~;~~~~~~~~~~~~R<r<m^{-1}_{\rm amb.}\,.$ (arXiv:1407.0059) [src: Eq. 5.18], and matching gives $\phi\simeq-\frac{R}{r}(\phi_{\rm amb.}-\phi_{\rm obj.})+\phi_{\rm amb.}\,.$ (arXiv:1407.0059) [src: Eq. 5.19].

The charge sits in a shell of thickness ΔR, "as in electrostatics": $\left.\frac{{\rm d}\phi}{{\rm d}r}\right|_{r=R_{+}}=\frac{\xi\rho}{M_{\rm Pl}}\Delta R\,.$ [src: Eq. 5.20]. Combining Eqs. 5.19 and 5.20 gives the thin-shell factor $\frac{\Delta R}{R}=\frac{\phi_{\rm amb.}-\phi_{\rm obj.}}{6\xi M_{\rm Pl}\Phi}\,,$ (arXiv:1407.0059) [src: Eq. 5.21], with Φ ≡ M/8πM²_Pl R the surface potential [src: Sect. 5.1.2, text after Eq. 5.21]. The exterior field is then that of a massive scalar with a coupling reduced by ΔR/R, $\phi(r>R)\simeq-\frac{3\xi}{4\pi M_{\rm Pl}}\frac{\Delta R}{R}\frac{Me^{-m_{\rm amb.}(r-R)}}{r}+\phi_{\rm amb.}~,~~~~~~~~({\rm screened})\,,$ [src: Eq. 5.22], against $\phi(r>R)\simeq-\frac{\xi}{4\pi M_{\rm Pl}}\frac{Me^{-m_{\rm amb.}(r-R)}}{r}~,~~~~~~~~~~~~~~~~~~({\rm unscreened})\,.$ (arXiv:1407.0059) [src: Eq. 5.23] when the thin-shell factor would exceed one, "a weak source (i.e., one with small Φ)" [src: Sect. 5.1.2]. <!-- num: not a value -->

For the Ratra–Peebles potential $V(\phi)=\frac{M^{4+n}}{\phi^{n}}~,$ [src: Eq. 5.11] the minimum and the mass are $\bar{\phi}(\rho)\approx\left(\frac{nM^{4+n}M_{\rm Pl}}{\xi\rho}\right)^{\frac{1}{n+1}}~,$ [src: Eq. 5.12] and $m_{\rm eff}^{2}(\rho)\approx n(n+1)M^{-\frac{4+n}{1+n}}\left(\frac{\xi\rho}{nM_{\rm Pl}}\right)^{\frac{n+2}{n+1}}~.$ (arXiv:1407.0059) [src: Eq. 5.13]: the mass "increases with increasing density, exactly as desired" [src: Sect. 5.1.1].

The same result for a general density profile (Burrage & Sakstein): the field sits at its interior minimum up to a screening radius $r_{\rm s}$, and outside it $F_{5}=\frac{2\beta^{2}(\bar{\phi})G\left[\mathcal{M}(r)-\mathcal{M}(r_{\rm s})\right]}{r^{2}}.$ (arXiv:1709.09071) [src: Eq. 3.6], so that unscreened objects ($r_s\ll R$) have $\frac{F_{5}}{F_{\rm N}}\approx 2\beta^{2}(\bar{\phi})$ [src: Eq. 3.7]. The screening radius solves $\chi\equiv\frac{\bar{\phi}}{2\beta(\bar{\phi}){M_{\rm{pl}}}}=4\pi G\int_{r_{\rm s}}^{\infty}r^{\prime}\delta\rho(r^{\prime})\,{\rm d}r^{\prime},$ [src: Eq. 3.10], equivalently $\chi=-\Phi_{\rm N}(r_{\rm s})-r_{\rm s}\Phi_{\rm N}^{\prime}(r_{\rm s}).$ (arXiv:1709.09071) [src: Eq. 3.11]; "only objects where $\chi<G\mathcal{M}/R$ can be partially (or fully for $\chi\ll G\mathcal{M}/R$ ) screened" [src: Sect. 3.1, inline, text after Eq. 3.11]. Hence the rule that the Newtonian potential decides, with the potentials of the Numbers table.

### Step 3 — f(R) as a chameleon
<!-- key: step-3-f-r-as-a-chameleon -->

The f(R) action $S=\frac{M^{2}_{\rm Pl}}{2}\int{\rm d}^{4}x\sqrt{-g}\Big(R+f(R)\Big)+S_{\rm matter}[g_{\mu\nu},\psi]~,$ (arXiv:1407.0059) [src: Eq. 5.24] has a scalar $f_R$ obeying $\square f_{R}=\frac{1}{3}\left(R+2f-f_{R}R+\frac{1}{M_{\rm Pl}^{2}}T\right)\equiv\frac{{\rm d}V_{\rm eff}(f_{R})}{{\rm d}f_{R}}~,$ [src: Eq. 5.28] with mass $m_{\rm eff}^{2}(f_{R})=\frac{1}{3}\left(\frac{1+f_{R}}{f_{RR}}-R\right)~,$ (arXiv:1407.0059) [src: Eq. 5.29]. The conformal transformation and field redefinition $\tilde{g}_{\mu\nu}=\left(1+\frac{{\rm d}f}{{\rm d}\Phi}\right)g_{\mu\nu}~,~~~~~~~~~~~~~~\phi=-\sqrt{\frac{3}{2}}M_{\rm Pl}\log\left(1+\frac{{\rm d}f}{{\rm d}\Phi}\right)~.$ [src: Eq. 5.30] turn it into a canonical scalar with matter coupled to $e^{\sqrt{2/3}\phi/M_{\rm Pl}}\tilde{g}_{\mu\nu}$, i.e. $A^{2}(\phi)=e^{\sqrt{2/3}\phi/M_{\rm Pl}}$, which "for a suitable choice of V(φ) will exhibit chameleon screening" (arXiv:1407.0059) [src: Sect. 5.1.3, inline, text after Eq. 5.32]. Burrage & Sakstein state it as "a chameleon with $M_{c}=\sqrt{6}{M_{\rm{pl}}}$", the Hu–Sawicki model covering only $-1<n<-1/2$ of the chameleon index (arXiv:1709.09071) [src: Sect. 2.1.1]. <!-- eq: notation --> On scales below the Compton wavelength of an unscreened object "the Newtonian potential is enhanced by a factor of 4/3", and objects "must be partially screened if $f_{R0}<2\Phi/3$", so "$f_{R0}$ is the f(R) equivalent of the χ" (arXiv:1709.09071) [src: Sect. 3.1.1]. <!-- eq: notation -->

`[der]` As printed in Sect. 3.1.1 of arXiv:1709.09071, the GR (screened) limit is attributed to δf_R ≪ f_R0 and the linearisation δR ≈ δf_R/f_RR (unscreened) to δf_R ≫ f_R0, the reverse of what their closing condition for partial screening implies; read the two limits from that closing condition.

### Step 4 — symmetron: vanishing coupling
<!-- key: step-4-symmetron-vanishing-coupling -->

With $V(\phi)=-\frac{\mu^{2}}{2}\phi^{2}+\frac{\lambda}{4}\phi^{4}~,$ [src: Eq. 5.43] and $A(\phi)=1+\frac{1}{2M^{2}}\phi^{2}+{\cal O}\left(\frac{\phi^{4}}{M^{4}}\right)~.$ (arXiv:1407.0059) [src: Eq. 5.44], the density acts as a mass term (Eq. 5.45, in `formalism.md`). At low density $\bar{\phi}=\sqrt{\frac{\mu^{2}}{\lambda}}~.$ [src: Eq. 5.46]; at high density, $\rho\gg M^{2}\mu^{2}$, the symmetry is restored, and since the coupling of fluctuations is $\frac{\phi^{2}}{M^{2}}T\sim\frac{\bar{\phi}}{M^{2}}\delta\phi~\rho~.$ (arXiv:1407.0059) [src: Eq. 5.47] "in high density regions, where φ has no VEV, the fluctuations δφ do not couple to matter" [src: Sect. 5.2.1]. The symmetron has a thin shell controlled by $\alpha\equiv\frac{\rho R^{2}}{M^{2}}=6\frac{M_{\rm Pl}^{2}}{M^{2}}\Phi\,.$ (arXiv:1407.0059) [src: Eq. 5.48]: objects with α ≫ 1 are screened and the force on a test particle "is suppressed by 1/α compared to the gravitational force"; for α ≪ 1 "the symmetron gives an ${\cal O}(1)$ correction to the gravitational attraction" [src: Sect. 5.2.1, inline, text after Eq. 5.48].

### Step 5 — k-mouflage: the first derivative
<!-- key: step-5-k-mouflage-the-first-derivative -->

The simplest shift-symmetric model is ${\cal L}=-\frac{1}{2}(\partial\phi)^{2}+\frac{\alpha}{4\Lambda^{4}}(\partial\phi)^{4}+\frac{g}{M_{\rm Pl}}\phi T\ ,$ (arXiv:1407.0059) [src: Eq. 6.2], with α = ±1 [src: Sect. 6.1]. <!-- num: not a value --> Around a point source the shift symmetry gives a first integral, $\phi^{\prime}-\frac{\alpha}{\Lambda^{4}}\phi^{\prime\,3}=\frac{1}{4\pi r^{2}}\frac{gM}{M_{\rm Pl}}\ .$ (arXiv:1407.0059) [src: Eq. 6.6], a cubic in φ′ whose crossover sits at $r_{\star}=\frac{1}{\Lambda}\left(\frac{gM}{M_{\rm Pl}}\right)^{1/2}~.$ [src: Eq. 6.8], with $\phi^{\prime}(r)\sim\left\{\begin{array}[]{lr}\frac{\Lambda^{2}}{4\pi}\left(\frac{r_{\star}}{r}\right)^{2}&~~~~~~~~~~~~~~~~~~{\rm for}~~~~~~r\gg r_{\star}\\ (-\alpha)^{1/3}\Lambda^{2}\left(\frac{r_{\star}}{r}\right)^{2/3}&~~~~~~~~~~~{\rm for}~~~~~~r\ll r_{\star}\end{array}\right.\ .$ (arXiv:1407.0059) [src: Eq. 6.9]. "a consistent continuous solution is only possible if we choose α = −1" [src: Sect. 6.1.1, text after Eq. 6.9]; inside $r_\star$ the ratio of scalar to gravitational force goes to zero "as ∼ r^{4/3}" [src: Sect. 6.1.1, text after Eq. 6.10]. <!-- num: not a value -->

Brax and Valageas write the same radius for a general k-mouflage model, $R_{K}=\left(\frac{\beta m}{4\pi M_{\rm Pl}{\cal M}^{2}}\right)^{1/2}.$ (arXiv:1403.5420) [src: Eq. 21], and find that for quasi-linear structures screening needs $\frac{k}{H_{0}}\lesssim\sqrt{\frac{3}{\Omega_{\Lambda 0}}}\Omega_{\rm m0}A(\varphi_{0})\beta(\varphi_{0})\delta,$ (arXiv:1403.5420) [src: Eq. 23], "superhorizon scales if δ ∼ 1. As a result, quasilinear objects in the Universe are not screened in K-mouflage models" [src: Sect. II.3.2]. <!-- num: not a value -->

### Step 6 — Vainshtein: the second derivative
<!-- key: step-6-vainshtein-the-second-derivative -->

The cubic galileon ${\cal L}=-3(\partial\phi)^{2}-\frac{1}{\Lambda^{3}}\Box\phi(\partial\phi)^{2}+\frac{g}{M_{\rm Pl}}\phi T^{\mu}_{\;\mu}\ ,$ (arXiv:1407.0059) [src: Eq. 6.32] has the second-order equation $6\Box\phi+\frac{2}{\Lambda^{3}}\bigg((\Box\phi)^{2}-(\partial_{\mu}\partial_{\nu}\phi)^{2}\bigg)=-\frac{g}{M_{\rm Pl}}T^{\mu}_{\;\mu}\,.$ (arXiv:1407.0059) [src: Eq. 6.33]. For a static point source it integrates to the algebraic equation $6\phi^{\prime}+\frac{4}{\Lambda^{3}}\frac{\phi^{\prime 2}}{r}=\frac{gM}{4\pi r^{2}M_{\rm Pl}}\,.$ (arXiv:1407.0059) [src: Eq. 6.38], whose branch decaying at infinity is Eq. 6.39 with the Vainshtein radius of Eq. 6.40 (`formalism.md#screening-mechanisms`); the other branch "matches asymptotically to a self-accelerated solution and has unstable (i.e., ghost-like) perturbations" [src: Sect. 6.2.2, footnote 28].

- Far outside, $\phi^{\prime}(r\gg r_{\rm V})\simeq\frac{g}{3}\cdot\frac{M}{8\pi M_{\rm Pl}r^{2}}\,.$ [src: Eq. 6.41] and $\left.\frac{F_{\phi}}{F_{\rm gravity}}\right|_{r\gg r_{\rm V}}\simeq\frac{g^{2}}{3}\,.$ (arXiv:1407.0059) [src: Eq. 6.42], "For DGP, where g=1, this reproduces the famous 1/3 enhancement" [src: Sect. 6.2.2, text after Eq. 6.42].
- Deep inside, $\phi^{\prime}(r\ll r_{\rm V})\simeq\frac{\Lambda^{3}r_{\rm V}}{2}\sqrt{\frac{r_{\rm V}}{r}}\sim\frac{1}{\sqrt{r}}\,.$ [src: Eq. 6.44] and $\left.\frac{F_{\phi}}{F_{\rm gravity}}\right|_{r\ll r_{\rm V}}\sim\left(\frac{r}{r_{\rm V}}\right)^{3/2}\ll 1\,,$ (arXiv:1407.0059) [src: Eq. 6.45].- The EFT stays predictive in between: the classical parameter $\alpha_{\rm cl}\equiv\frac{\partial^{2}\phi}{\Lambda^{3}}\,,$ [src: Eq. 6.35] is large while the quantum one, $\alpha_{\rm q}\equiv\frac{\partial^{2}}{\Lambda^{2}}\,,$ (arXiv:1407.0059) [src: Eq. 6.36], stays small for $\Lambda^{-1}\ll r\ll r_{\rm V}$ [src: Sect. 6.2.2]. Perturbations inside $r_{\rm V}$ acquire a kinetic term enhanced by $(r_{\rm V}/r)^{3/2}$, so that $g_{\rm eff}\sim\left(\frac{r}{r_{\rm V}}\right)^{3/4}g\ll g\,;$ [src: Eq. 6.55] and $\Lambda^{\rm eff}\sim\left(\frac{r_{\rm V}}{r}\right)^{3/4}\Lambda~\gg\Lambda\,,$ (arXiv:1407.0059) [src: Eq. 6.56].

`[der]` As printed, the prefactor of Eq. 6.44 is not the one obtained by taking the limit r ≪ r_V of Eq. 6.39; the scaling with r agrees. Use Eq. 6.39 when a coefficient matters.

Brax and Valageas's general Vainshtein radius, for the $b\neq0$ term of Eq. 12, is $R_{V}=\left(\frac{3\beta L^{2}m}{4\pi M^{2}_{\rm Pl}}\right)^{1/3}.$ (arXiv:1403.5420) [src: Eq. 15], and with L of the order of the size of the present Universe, screening needs $\delta\gtrsim\frac{1}{3\Omega_{\rm m0}A(\varphi_{0})\beta(\varphi_{0})},$ (arXiv:1403.5420) [src: Eq. 18], so "all quasilinear structures in the Universe are screened in the Vainshtein models and nonlinear effects must be taken into account even on mildly nonlinear scales" [src: Sect. II.3.1].

DGP in Koyama's form: $\frac{d\phi}{dr}=\frac{2r_{g}}{3\beta r^{2}}\left(\frac{r}{r_{V}}\right)^{3}\left(\sqrt{1+\left(\frac{r_{V}}{r}\right)^{3}}-1\right),\quad r_{V}=\left(\frac{8r_{c}^{2}r_{g}}{9\beta^{2}}\right)^{1/3},$ (arXiv:1504.04623) [src: Eq. 108]; inside $r_V$, $\Phi=\frac{GM}{r}\pm\sqrt{\frac{r_{g}r}{2r_{c}^{2}}},\quad\Psi=-\frac{GM}{r}\pm\sqrt{\frac{r_{g}r}{2r_{c}^{2}}}.$ [src: Eq. 109], the upper sign for the normal branch, and outside, $\Phi=\frac{GM}{r}\left(1-\frac{1}{3\beta}\right),\quad\Psi=-\frac{GM}{r}\left(1+\frac{1}{3\beta}\right).$ (arXiv:1504.04623) [src: Eq. 110]. The residual correction inside $r_V$ gives a perihelion advance per orbit $\frac{\Delta\phi}{P}=\frac{3}{8r_{c}}=5\times 10^{-4}\left(\frac{r_{c}}{5\mbox{Gpc}}\right)^{-1}{\rm arcseccond\;per\;century}.$ (arXiv:1504.04623) [src: Eq. 112], "independent of mass so it is universal" [src: Sect. 3.5]. For general Horndeski, Koyama gives the spherical equation $P(x,A)\equiv\xi A(r)+\left(\frac{\eta}{2}+3\xi^{2}\right)x+\Big(\mu+6\alpha\xi-3\beta A(r)\Big)x^{2}+\Big(\nu+2\alpha^{2}+4\beta\xi\Big)x^{3}-3\beta^{2}x^{5}=0,$ (arXiv:1504.04623) [src: Eq. 114], with $A(r)=\Big(\frac{r_{V}}{r}\Big)^{3},\quad r_{V}=\Big(\frac{M}{8\pi M_{\rm Pl}\Lambda_{3}^{3}}\Big)^{1/3},$ (arXiv:1504.04623) [src: Eq. 118] outside the source.

## Which mechanism applies to which theory
<!-- key: which-mechanism-applies-to-which-theory -->

| Theory | Mechanism | Criterion | Paper and place |
|---|---|---|---|
| Chameleon (inverse power law) | thin shell, large mass | Newtonian potential | arXiv:1407.0059 [src: Sects. 3.2, 5.1] |
| f(R), Hu–Sawicki | chameleon, $M_c=\sqrt6M_{\rm pl}$ <!-- eq: notation --> | $f_{R0}$ against Φ | arXiv:1709.09071 [src: Sects. 2.1.1, 3.1.1] |
| Symmetron, dilaton | small coupling | Newtonian potential (α of Eq. 5.48) | arXiv:1504.04623 [src: Sect. 3.2]; arXiv:1407.0059 [src: Sect. 5.2] |
| k-mouflage, P(X), DBI | kinetic | gravitational acceleration | arXiv:1407.0059 [src: Sect. 3.2] |
| Galileons, DGP decoupling limit, massive gravity | Vainshtein | curvature, density | arXiv:1407.0059 [src: Sect. 3.2] |
| Horndeski with derivative self-interactions | Vainshtein, general spherical solution | Eq. 114 of Koyama | arXiv:1504.04623 [src: Sect. 3.5] |
| Beyond Horndeski | Vainshtein outside, broken inside matter | — | `formalism.md#screening-mechanisms` (arXiv:1411.4130) |
| Canonical Brans–Dicke | none: "lacks any screening mechanism" | — | arXiv:1909.01828 [src: Sect. 3.3.2, Brans–Dicke paragraph] |
| RR non-local model | "no Vainshtein radius" | — | `formalism.md#non-local-gravity` (arXiv:1402.0448) |

`[der]` Screening by the field value (chameleon, symmetron) works through the matter coupling of a potential; screening by derivatives (k-mouflage, Vainshtein) needs derivative self-interactions, which is why a canonical Brans–Dicke scalar, with neither, is not screened.

## Variants and what they cost
<!-- key: variants-and-what-they-cost -->

- **Thin shell by matching (Joyce et al.) against screening radius by integration (Burrage & Sakstein).** The first assumes constant densities and a sharp shell; the second handles a profile δρ(r) through Eqs. 3.10–3.11 and is "the method" behind "the current astrophysical constraints"; "Other derivations using slightly different procedures recover the same results" (arXiv:1709.09071) [src: Sect. 3.1].
- **Environment.** A single object in a background is not enough: "In practice, one also needs to worry about environmental screening" (arXiv:1709.09071) [src: Sect. 3.1, text after Table 1].
- **Linear criteria (Brax & Valageas).** Eqs. 7, 14 and 20 of arXiv:1403.5420 give necessary conditions from the linear solution; they compare mechanisms on one footing but are order-of-magnitude statements, the k-mouflage and Vainshtein ones holding "when β is a slowly varying function of φ" (arXiv:1403.5420) [src: Sects. II.3.1–II.3.2].
- **Composite and non-spherical sources.** Modelling a nucleon with "a constant-density core and an $r^{-6}$ pion tail" instead of a uniform sphere changes laboratory bounds: "symmetron constraints from neutron interferometry at $μ=1\,\mathrm{keV}$ reach maximal self-couplings about 1.4 orders of magnitude higher than for a uniform-sphere neutron" and the hydrogen 1s–2s chameleon bound "reaches couplings 1.8 orders of magnitude weaker than for a uniform-sphere proton" (arXiv:2611.02213, Brax et al. 2026) [src: abstract]. <!-- eq: notation --> Non-spherical Vainshtein sources are in `formalism.md#screening-mechanisms` (arXiv:2607.09098).
- **Time evolution of screened galileons.** In a Galileon EFT evolved non-linearly in spherical symmetry, the ghost-free model "develops ill-posed regions during evolution only when the derivative expansion breaks down", and in a regularised version "the ghost term naturally dominates over the Galileon term in the screening regime, contrary to common expectation" (arXiv:2609.05407, Thaalba et al. 2026) [src: abstract].

## Numbers
<!-- key: numbers -->

| Quantity | Value | Assumptions | Source | Place read |
|---|---|---|---|---|
| Eöt-Wash range of a gravitational-strength fifth force | "upper limit of ≈ 50 μm" | gravitational-strength coupling | arXiv:1407.0059 | [src: Sect. 5.1.1] |
| Chameleon scale | $M\lesssim10^{-3}$ eV, "remarkably, coincides with the dark energy scale" <!-- eq: notation --> | Ratra–Peebles chameleon, Eöt-Wash in vacuum | arXiv:1407.0059 | [src: Eq. 5.14, text after] |
| Newtonian potentials $\Phi_{\rm N}$ | Earth $10^{-9}$, Moon $10^{-11}$, main-sequence stars ($M_\odot$) $10^{-6}$, post-main-sequence ($1$–$10M_\odot$) $10^{-7}$–$10^{-8}$, spiral and elliptical galaxies $10^{-6}$, dwarf galaxies $10^{-8}$ | — | arXiv:1709.09071 | [src: Table 1] |
| Reach of unscreened dwarfs | $\chi_0\gtrsim10^{-8}$ "in theory" <!-- eq: notation --> | chameleon | arXiv:1709.09071 | [src: Sect. 3.1, text after Eq. 3.14] |
| f(R) unscreened enhancement | "a factor of 4/3" on the Newtonian potential | below the Compton wavelength | arXiv:1709.09071 | [src: Sect. 3.1.1] |
| Galileon force outside $r_V$ | $g^2/3$; DGP (g = 1) "the famous 1/3 enhancement" <!-- eq: notation --> | cubic galileon, point source | arXiv:1407.0059 | [src: Eq. 6.42 and text after] |
| Radial sound speed inside $r_V$ | $c_{\rm s}^{\rm radial}=\sqrt{\frac{4}{3}}\,.$ | cubic galileon, $r\ll r_V$ | arXiv:1407.0059 | [src: Eq. 6.57] |
| DGP Vainshtein radius of the Sun | $r_g$ = 2.95 km, $r_V$ = 130 pc | $r_c\sim H_0$ <!-- eq: notation --> | arXiv:1504.04623 | [src: Sect. 3.5] |
| DGP $r_c$ from planetary precession | $r_c>130$ Mpc, from Δφ/P < 0.02 arcsec per century <!-- eq: notation --> | test-body treatment | arXiv:1504.04623 | [src: Sect. 3.5] |
| DGP $r_c$ from lunar laser ranging | $r_c>162$ Mpc, from δΨ/Ψ < 2.4 × 10⁻¹¹ <!-- eq: notation --> | test-body treatment; Earth–Moon correction "small (4 %)" | arXiv:1504.04623 | [src: Sect. 3.5] |
| Chameleon range | "less than 1 Mpc", from Milky Way and Solar System screening | chameleon-like models | arXiv:1403.5420 | [src: Sect. II.2] |
| Variation of Newton's constant | $\lvert\dot{\cal G}_{\rm N}/{\cal G}_{\rm N}\rvert\leq0.2H_0$ <!-- eq: notation --> | lunar ranging, as quoted | arXiv:1403.5420 | [src: Sect. II.1] |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Screening without a healthy UV.** The k-mouflage branch that screens (α = −1) makes radial perturbations superluminal at all distances, $c_{r}^{2}=1-\frac{2\alpha\bar{\phi}^{\prime\,2}}{\Lambda^{4}-\alpha\bar{\phi}^{\prime\,2}}\,.$ (arXiv:1407.0059) [src: Eq. 6.28], and the forward 2 → 2 amplitude has the sign that analyticity forbids, "circumstantial evidence that theories which admit kinetic screening cannot arise as" (the sentence continues beyond the passage read) [src: Sect. 6.1.4]. <!-- num: not a value --> The cubic galileon is superluminal radially inside $r_V$ (Numbers table); "This conclusion only holds for asymptotically flat solutions" [src: Sect. 6.2.3, footnote 31]. Positivity bounds are in `results.md#theorems-and-no-go-results`.
- **Using a linear μ inside screened regions.** Vainshtein screening reaches all quasi-linear structures with δ of order one (arXiv:1403.5420, Eq. 18), while k-mouflage leaves them unscreened (Eq. 23); a linear μ–Σ prediction is only safe for the second. Check: the criterion of Step 1 for the scales fitted.
- **Chameleon self-acceleration.** Chameleon-like scalars "cannot self-accelerate" and have a negligible effect on linear growth (`results.md#theorems-and-no-go-results`, arXiv:1208.4612); a chameleon model that drives the expansion needs a cosmological constant or another field.
- **Uniform-sphere sources.** Laboratory bounds that model nucleons as uniform spheres shift by the orders of magnitude quoted under Variants (arXiv:2611.02213) [src: abstract].
- **Test-body assumption in Vainshtein tests.** The DGP Solar-System bounds "are obtained by treating the planets or the Moon as a test body. This assumption is not necessarily valid", because of "the non-superimposability of the field" (arXiv:1504.04623) [src: Sect. 3.5].
- **Printed slips.** The prefactor of Eq. 6.44 of arXiv:1407.0059 and the two limits of Sect. 3.1.1 of arXiv:1709.09071 are described under Steps 6 and 3. Koyama's quadratic action for perturbations around Vainshtein solutions prints the radial term without a square, $K_{r}(r)(\partial_{r}\varphi)$ (arXiv:1504.04623) [src: Eq. 119], while the time and angular terms carry one; copy it as printed. <!-- eq: notation -->

## Reading list
<!-- key: reading-list -->

- Joyce, Jain, Khoury & Trodden 2014, arXiv:1407.0059 (review, derivation) — Sect. 3.2 for the classification, Sects. 5.1–5.2 for the thin shell and symmetron, Sect. 6 for kinetic and Vainshtein screening.
- Khoury & Weltman 2003, arXiv:astro-ph/0309300 (foundation) — the chameleon.
- Hinterbichler & Khoury 2010, arXiv:1001.4525 (foundation) — the symmetron.
- Babichev, Deffayet & Ziour 2009, arXiv:0905.2943 (foundation) — k-mouflage.
- Burrage & Sakstein 2017, arXiv:1709.09071 (review) — Sect. 3.1: screening radius for a general profile, astrophysical potentials, f(R) as a chameleon.
- Brax & Valageas 2014, arXiv:1403.5420 (derivation) — Sect. II: the three criteria from one Lagrangian, k-mouflage and Vainshtein radii, which cosmic structures are screened.
- Koyama 2016, arXiv:1504.04623 (review) — Sects. 3.2 and 3.5: DGP Vainshtein solution and Solar-System bounds, general Horndeski spherical equation.
- Brax, Burrage & Moss 2026, arXiv:2611.02213 (critique) — source modelling in laboratory screening bounds.
- Thaalba et al. 2026, arXiv:2609.05407 (critique) — well-posedness of screened galileon evolution.

## Not verified
<!-- key: not-verified -->

- Vainshtein's 1972 paper is pre-arXiv and was not read; the Vainshtein solution is quoted from Joyce et al. and Koyama.
- The Khoury–Weltman, Hinterbichler–Khoury and Babichev–Deffayet–Ziour bodies were not read in this run; their mechanisms are derived here from Joyce et al., Burrage & Sakstein and Brax & Valageas.
- The coefficients α, β, η, μ, ν, ξ of Koyama's Eq. 114 are defined by his effective action (his Eq. 52), not read.
- Joyce et al.'s 1-loop radiative-stability section (Sect. 5.4) and the massive-gravity Vainshtein sections (Sect. 6.3) were not read.
- The two `[der]` slip readings (Joyce et al. Eq. 6.44, Burrage & Sakstein Sect. 3.1.1) are an agent's reading of the printed equations; a maintainer should confirm them against the PDFs.
