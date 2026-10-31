# Conventions to pin down in a theory text

Scope: the conventions a theoretical-cosmology text must state, the choices
in use for each, which reference works adopt which choice (with the source
and the place read), and the relations between conventions that a paper
states. The atlas is built (step P4 of `docs/plans/2026-10-30-plan-v2.md`).

Snapshot: 2026-10-31

How to read the tables: one row per reference work, so that every row names
one paper and the place read. Equations are copied as the cited paper's
HTML rendering prints them, in that paper's own conventions; nothing is
converted from one convention to another here. A relation between two
conventions is listed only where a paper states it. Code conventions are
`[doc]` facts with the address and the date read.

## Spacetime and gravity
<!-- key: spacetime-and-gravity -->

### Metric signature and curvature signs
<!-- key: metric-signature-and-curvature-signs -->

| Reference work | Signature | Curvature tensors | Place read |
|---|---|---|---|
| Baumann 2009, TASI lectures on inflation, arXiv:0907.5424 | (−+++) | not stated in the notation section | [src: Sect. "Notation"] |
| Malik & Wands 2009, review of cosmological perturbations, arXiv:0809.4944 | sign convention (+++) in the classification of Misner, Thorne and Wheeler | same classification | [src: App. A.1] |
| Clifton et al. 2012, modified-gravity review, arXiv:1106.2476 | (−+++), the "space-like convention": $ds^{2}=\eta_{\mu\nu}dx^{\mu}dx^{\nu}=-dt^{2}+dx^{2}+dy^{2}+dz^{2}$ | Riemann and Einstein tensors of Misner, Thorne and Wheeler | [src: Sect. 1, Eq. 2] |
| Copeland, Sami & Tsujikawa 2006, dark-energy review, arXiv:hep-th/0603057 | (−,+,+,+) | not stated in the introduction | [src: Sect. I] |
| Chen 2010, non-Gaussianity review, arXiv:1002.1416 | (−1,1,1,1) | not stated | [src: Sect. 4] |
| Kinney 2009, TASI lectures on inflation, arXiv:0902.1529 | (+−−−), read from his Minkowski line element | not stated | [src: Sect. I.1, Eq. 5] |

- Clifton et al. (arXiv:1106.2476) write the Einstein tensor as $G_{\mu\nu}=R_{\mu\nu}-\frac{1}{2}g_{\mu\nu}R$ [src: Eq. 4], with the Riemann tensor of their Eq. 3.
- Clifton et al. (arXiv:1106.2476) contract the Riemann tensor as $R_{\mu\nu}=R^{\alpha}_{\phantom{\alpha}\mu\alpha\nu}$ [src: Sect. 1, inline, text after Eq. 4].
- Clifton et al. (arXiv:1106.2476) define the energy-momentum tensor from the matter Lagrangian density as $T^{\mu\nu}=\frac{2}{\sqrt{-g}}\frac{\delta\mathcal{L}_{m}}{\delta g_{\mu\nu}}$ [src: Eq. 5].
- Kinney (arXiv:0902.1529) writes the scalar-field Lagrangian of the (+−−−) signature as ${\mathcal{L}}_{\phi}=\frac{1}{2}g^{\mu\nu}\partial_{\mu}\phi\partial_{\nu}\phi-V\left(\phi\right)$ [src: Eq. 84].

### Units, Planck mass and where 8πG appears
<!-- key: units-planck-mass-and-where-8-g-appears -->

| Reference work | Units | Planck mass written | Place read |
|---|---|---|---|
| Baumann, arXiv:0907.5424 | $c=\hbar\equiv 1$ | reduced, $M_{\rm pl}=(8\pi G)^{-1/2}$, often set to one | [src: Sect. "Notation", unnumbered display] |
| Malik & Wands, arXiv:0809.4944 | $c=\hbar=1$ | reduced Planck mass written in lower case, $m_{\rm{Pl}}^{2}=(8\pi G)^{-1}$; upper-case $M_{\rm Pl}$ is the full Planck mass in the list of symbols | [src: List of Symbols; Sect. 11, unnumbered display (inline)] |
| Copeland, Sami & Tsujikawa, arXiv:hep-th/0603057 | $c=\hbar=1$ | full Planck mass in lower case, $m_{\rm pl}=G^{-1/2}=1.22\times 10^{19}\,{\rm GeV}$; reduced in upper case, $M_{\rm pl}=(8\pi G)^{-1/2}=2.44\times 10^{18}\,{\rm GeV}$; $\kappa^{2}=8\pi G=8\pi m_{\rm pl}^{-2}=M_{\rm pl}^{-2}$ | [src: Sect. I, unnumbered display (inline)] |
| Kinney, arXiv:0902.1529 | natural units | full Planck mass: $S_{\rm tot}=\int{d^{4}x\sqrt{-g}\left[\frac{m_{\rm Pl}^{2}}{16\pi}R+{\mathcal{L}}_{\phi}\right]}$ | [src: Eq. 86] |
| Chen, arXiv:1002.1416 | — | reduced, $M_{\rm P}=(8\pi G)^{-1/2}$, set to one | [src: Sect. 4, unnumbered display (inline)] |
| Martin et al., Encyclopaedia Inflationaris, arXiv:1303.3787 | — | reduced (Friedmann equation with $3M_{\rm Pl}^{2}$): $H^{2}=\frac{1}{3M_{\scriptscriptstyle{\mathrm{Pl}}}^{2}}\left[\frac{\dot{\phi}^{2}}{2}+V(\phi)\right]$ | [src: Sect. 3.1, Eq. 4] |
| CLASS input file | — | scalar-field initial values "in units of the reduced planck mass m_Pl" | [doc: https://raw.githubusercontent.com/lesgourg/class_public/master/explanatory.ini, 2026-10-31] |

- The same symbol means opposite things in two anchors: lower-case $m_{\rm Pl}$ is the reduced mass in Malik & Wands (arXiv:0809.4944, List of Symbols) and the full mass in Copeland et al. (arXiv:hep-th/0603057, Sect. I) and Kinney (arXiv:0902.1529, Eq. 86). `[der]` A text must define its symbol.
- Kinney's Friedmann equation with the full Planck mass is $H^{2}=\left(\frac{\dot{a}}{a}\right)^{2}=\frac{8\pi}{3m_{\rm Pl}^{2}}\left[\frac{1}{2}\dot{\phi}^{2}+V\left(\phi\right)\right]$ (arXiv:0902.1529) [src: Eq. 96].

### Time variable and the direction of e-folds
<!-- key: time-variable-and-the-direction-of-e-folds -->

| Reference work | Conformal time | e-fold variable and direction | Place read |
|---|---|---|---|
| Baumann, arXiv:0907.5424 | $\tau$; $\eta$ reserved for the second slow-roll parameter | ${\rm d}N=H{\rm d}t$ in the definition of $\varepsilon$ (text after Eq. 70); the number of e-folds left counts back from the end of inflation (Eq. 82, list below) | [src: Sect. "Notation"; Sect. 6.2, inline, text after Eq. 70] |
| Kinney, arXiv:0902.1529 | — | $dN\equiv-Hdt$; N increases going backward in time from the end of inflation | [src: Sect. IV, Eq. 95] |
| Martin et al., arXiv:1303.3787 | $\eta$ (mode equation) | N counted from an initial value: $N-N_{\mathrm{ini}}=-\frac{1}{M_{\scriptscriptstyle{\mathrm{Pl}}}^{2}}\int_{\phi_{\mathrm{ini}}}^{\phi}\frac{V(\chi)}{V_{\chi}(\chi)}\,\mathrm{d}\chi$ | [src: Sect. 3.1, Eq. 14] |
| Malik & Wands, arXiv:0809.4944 | $\eta$, with $ds^{2}=a^{2}\left[-d\eta^{2}+\delta_{ij}dx^{i}dx^{j}\right]$ | — | [src: Sect. 2.2.2, Eq. 2.7] |
| Clifton et al., arXiv:1106.2476 | $\tau=\int dt/a(t)$; dot for physical time, prime for conformal time | — | [src: Sect. 1, inline, text after Eq. 6] |
| Ma & Bertschinger 1995, synchronous and conformal Newtonian gauges, arXiv:astro-ph/9506072 | $\tau$: $ds^{2}=a^{2}(\tau)\{-d\tau^{2}+(\delta_{ij}+h_{ij})dx^{i}dx^{j}\}$ | — | [src: Sect. 2, Eq. 1] |

- Baumann (arXiv:0907.5424) defines the number of e-folds before the end of inflation as $N(\phi)\equiv\ln\frac{a_{\rm end}}{a}=\int_{t}^{t_{\rm end}}H{\rm d}t=\int_{\phi}^{\phi_{\rm end}}\frac{H}{\dot{\phi}}{\rm d}\phi\approx\int_{\phi_{\rm end}}^{\phi}\frac{V}{V_{,\phi}}{\rm d}\phi$ [src: Sect. 6.2, Eq. 82].
- `[der]` The sign in front of $d\varepsilon/dN$ in the second Hubble slow-roll parameter follows the direction of N: compare Baumann's form (arXiv:0907.5424, Eq. 73) with Kinney's (arXiv:0902.1529, Eq. 103) in the slow-roll table below.

### Spatial curvature and the sign of Ω_K
<!-- key: spatial-curvature-and-the-sign-of-omegak -->

| Reference work | Curvature constant in the metric | Place read |
|---|---|---|
| Baumann, arXiv:0907.5424 | $k$ in ${\rm d}s^{2}=-{\rm d}t^{2}+a^{2}(t)\left(\frac{{\rm d}r^{2}}{1-kr^{2}}+r^{2}({\rm d}\theta^{2}+\sin^{2}\theta{\rm d}\phi^{2})\right)$ | [src: Sect. 3.1, Eq. 1] |
| Clifton et al., arXiv:1106.2476 | Gaussian curvature $\kappa$ in $ds_{(3)}^{2}=q_{ij}dx^{i}dx^{j}=\frac{dr^{2}}{1-\kappa r^{2}}+r^{2}d\theta^{2}+r^{2}\sin^{2}\theta d\phi^{2}$ | [src: Sect. 1, Eq. 8] |
| CLASS input file | input parameter `Omega_k`, default 0 | [doc: https://raw.githubusercontent.com/lesgourg/class_public/master/explanatory.ini, 2026-10-31] |

- The relation between $\Omega_K$ and the curvature constant, and hence its sign for a closed universe, was not found stated in the sources read (see "Not verified").

## Perturbations
<!-- key: perturbations -->

### Gauge and names of the metric potentials
<!-- key: gauge-and-names-of-the-metric-potentials -->

| Reference work | Potential in $g_{00}$ | Potential in $g_{ij}$ | Line element as printed | Place read |
|---|---|---|---|---|
| Ma & Bertschinger, arXiv:astro-ph/9506072 | $\psi$ | $\phi$ | $ds^{2}=a^{2}(\tau)\left\{-(1+2\psi)d\tau^{2}+(1-2\phi)dx^{i}dx_{i}\right\}$ (conformal Newtonian gauge); the synchronous gauge with $h_{ij}$ is Eq. 1 | [src: Sect. 2, Eq. 5] |
| Baumann, arXiv:0907.5424 | $\Phi$ | $\Psi$ | ${\rm d}s^{2}=-(1+2\Phi){\rm d}t^{2}+2a(t)B_{i}{\rm d}x^{i}{\rm d}t+a^{2}(t)[(1-2\Psi)\delta_{ij}+2E_{ij}]{\rm d}x^{i}{\rm d}x^{j}$ (cosmic time, any gauge) | [src: App. A.1.1, Eq. A.1; the multi-row display of Sect. 9.2.1 prints $E_{ij}$ there without the factor of two] |
| Clifton et al., arXiv:1106.2476 | $\Psi$ | $\Phi$ | $ds^{2}=a^{2}(\tau)\left[-(1+2\Psi)d\tau^{2}+(1-2\Phi)q_{ij}dx^{i}dx^{j}\right]$ (conformal Newtonian gauge, the review's default) | [src: Sect. 1, Eq. 7] |
| Malik & Wands, arXiv:0809.4944 | $\phi$ | $\psi$ (with $B$, $E$) | $\delta g_{00}=-2a^{2}{\phi}$ and $C_{ij}=-\psi\;\delta_{ij}+E_{,ij}+F_{(i,j)}+\frac{1}{2}h_{ij}$, where $\delta g_{ij}$ is $2a^{2}C_{ij}$ | [src: Sect. 2.2.2, Eqs. 2.8, 2.12] |
| CLASS input file | — | — | `gauge = synchronous` by default; `newtonian` selects the Newtonian/longitudinal gauge | [doc: https://raw.githubusercontent.com/lesgourg/class_public/master/explanatory.ini, 2026-10-31] |

- The four anchors use four labelings of the two scalar potentials: lower-case $\psi$ in $g_{00}$ (arXiv:astro-ph/9506072, Eq. 5), upper-case $\Phi$ in $g_{00}$ (arXiv:0907.5424, Eq. A.1), upper-case $\Psi$ in $g_{00}$ (arXiv:1106.2476, Eq. 7) and lower-case $\phi$ in $g_{00}$ (arXiv:0809.4944, Eq. 2.8). `[der]` A potential named without its line element is ambiguous.
- Baumann (arXiv:0907.5424) defines the Bardeen potential $\Psi_{\rm B}\equiv\psi+a^{2}H(\dot{E}-B/a)$ [src: Eq. 142].

### Curvature perturbation: ζ or ℛ, and its sign
<!-- key: curvature-perturbation-or-r-and-its-sign -->

| Reference work | Definition as printed | Place read |
|---|---|---|
| Malik & Wands, arXiv:0809.4944 | comoving curvature perturbation ${{\cal{R}}}\equiv\widetilde{\psi_{1{\rm{com}}}}=\psi_{1}-{\cal H}\left(v_{1}+B_{1}\right)$ | [src: Sect. 7.4, Eq. 7.46] |
| Malik & Wands, arXiv:0809.4944 | uniform-density curvature perturbation $-\zeta_{1}\equiv\widetilde{\psi_{1{\delta\rho}}}=\psi_{1}+{\cal H}\frac{\delta\rho_{1}}{\rho_{0}^{\prime}}$, sign chosen to agree with the ζ of their Refs. 8 and 9 | [src: Sect. 7.6.1, Eq. 7.61] |
| Baumann, arXiv:0907.5424 | $-\zeta\equiv\Psi+\frac{H}{\dot{\bar{\rho}}}\delta\rho$ | [src: Sect. 9.2.3, Eq. 136] |
| Baumann, arXiv:0907.5424 | ${\cal R}\equiv\Psi-\frac{H}{\bar{\rho}+\bar{p}}\delta q$ | [src: Sect. 9.2.3, Eq. 139] |
| Riotto 2002, lectures on inflation and perturbations, arXiv:hep-ph/0210162 | $\zeta=\Psi+\,{\cal H}\frac{\delta\rho}{\rho^{\prime}}=\Psi+H\frac{\delta\rho}{\dot{\rho}}$ (written with ζ, not −ζ, on the left; his metric conventions were not read) | [src: Sect. 7.7, unnumbered display] |
| Martin et al., arXiv:1303.3787 | $\zeta_{\boldsymbol{k}}=\frac{1}{M_{\scriptscriptstyle{\mathrm{Pl}}}}\frac{v_{\boldsymbol{k}}}{a\sqrt{2\epsilon_{1}}}$ (from the Mukhanov–Sasaki variable) | [src: Sect. 3.1, Eq. 16] |

Relations stated by the papers:

- Malik & Wands (arXiv:0809.4944) relate the two variables at first order by $\zeta_{1}=-{{\cal{R}}}_{1}-\frac{{\cal H}}{\rho_{0}^{\prime}}\delta\rho_{1{\rm{com}}}$ [src: Eq. 7.63], and state that they differ only by an overall minus sign on large scales [src: Sect. 7.6.1, text after Eq. 7.63].
- Malik & Wands (arXiv:0809.4944) state that their $\zeta_{1}$ is related to the $\zeta_{\rm SBB}$ of their Ref. 143 by $\zeta_{\rm{SBB}}\equiv 3\zeta_{1}$ [src: Sect. 7.6.1, footnote 3, inline, text after Eq. 7.61].
- Baumann (arXiv:0907.5424) relates them through the Einstein equations as $-\zeta={\cal R}+\frac{k^{2}}{(aH)^{2}}\frac{2\bar{\rho}}{3(\bar{\rho}+\bar{p})}\Psi_{\rm B}$ [src: Eq. 141].
- Baumann (arXiv:0907.5424, Sect. 9.2.3, text after Eq. 142) then calls ζ and ℛ "equal on superhorizon scales", whereas his Eq. 141 as printed relates $-\zeta$ to ℛ there, and his Eqs. 138 and 140 give $-\zeta$ and ℛ the same slow-roll form. `[der]` Read "equal" as equal up to the sign convention of his Eq. 136.
- Riotto (arXiv:hep-ph/0210162) states ${\cal R}_{\bf k}\simeq{\zeta}_{\bf k}$ on super-Hubble scales, with his sign of ζ [src: Sect. 7.13, unnumbered display].
- Planck 2018 IX (arXiv:1905.05697) defines the potential used in its templates by $\Phi\equiv(3/5)\zeta$ on superhorizon scales, Bardeen's potential in matter domination [src: Sect. 2.1, inline, text after Eq. 2].
- Komatsu 2010 (arXiv:1003.6097) writes $\zeta=\frac{5}{3}\Phi$ for Bardeen's curvature perturbation in matter domination [src: Sect. 3.3, unnumbered display (inline) before Eq. 24].
- Komatsu 2010 (arXiv:1003.6097) writes the Sachs–Wolfe limit as $\Delta T/T=-\frac{1}{3}\Phi=-\frac{1}{5}\zeta$ [src: Sect. 3.3, unnumbered display (inline) before Eq. 24].

### Fourier convention and power-spectrum normalisation
<!-- key: fourier-convention-and-power-spectrum -->

| Reference work | Forward transform | Power spectrum | Dimensionless spectrum | Place read |
|---|---|---|---|---|
| Baumann, arXiv:0907.5424 | ${\cal R}_{\bf k}=\int{\rm d}^{3}{\bf x}\,{\cal R}({\bf x})e^{-i{\bf k}\cdot{\bf x}}$ | $(2\pi)^{3}$ in front of the Dirac delta | $\Delta_{\cal R}^{2}(k)\equiv\frac{k^{3}}{2\pi^{2}}P_{\cal R}(k)$ | [src: Sect. "Notation", unnumbered display] |
| Ivanov 2022, EFT of LSS review, arXiv:2212.08488 | $\delta({\bf k})=\int d^{3}x~\delta({\bf x})e^{-i{\bf k}\cdot{\bf x}}$, with $\int_{\bf k}\equiv\int\frac{d^{3}k}{(2\pi)^{3}}$ in the inverse | — | — | [src: footnote 1, unnumbered display (inline)] |
| Bernardeau et al. 2002, PT review, arXiv:astro-ph/0112551 | $\tilde{A}({\bf k},\tau)=\int{{\rm d}^{3}{\bf x}\over{(2\pi)^{3}}}\exp(-i{\bf k}\cdot{\bf x})\ A({\bf x},\tau)$: the $(2\pi)^{3}$ sits in the forward transform | no $(2\pi)^{3}$ in front of the Dirac delta (Sect. 3.2.2) | see the list below | [src: Sect. 2.4.1, Eq. 36] |
| CAMB 2.0.5 Python wrapper | k in ${\rm Mpc}^{-1}$ for the primordial spectrum; matter power by default in $({\rm Mpc}/h)^{3}$ as a function of $k/h$ (`hubble_units=True`, `k_hunit=True`) | | | [doc: https://raw.githubusercontent.com/cmbant/CAMB/master/camb/initialpower.py for k in Mpc⁻¹, https://raw.githubusercontent.com/cmbant/CAMB/master/camb/results.py for the matter-power defaults, 2026-10-31] |

- Bernardeau et al. (arXiv:astro-ph/0112551) define the dimensionless power as $\Delta=4\pi k^{3}P(k)$ [src: Sect. 1, notation table, unnumbered display].
- Martin et al. (arXiv:1303.3787) define the dimensionless spectrum of the mode functions as $\mathcal{P}_{\zeta}(k)\equiv\frac{k^{3}}{2\pi^{2}}\left|\zeta_{\boldsymbol{k}}\right|^{2}$ [src: Sect. 3.1, Eq. 17].
- Bernardeau et al. (arXiv:astro-ph/0112551) write the inverse transform as $\delta({\bf x})=\int{{\rm d}^{3}{\bf k}}\,\delta({\bf k})\,\exp({\rm i}{\bf k}\cdot{\bf x})$ [src: Eq. 116].
- Bernardeau et al. (arXiv:astro-ph/0112551) write the correlation function as $\xi(r)=\int{\rm d}^{3}{\bf k}\,P(k)\exp({\rm i}{\bf k}\cdot{\bf r})$ [src: Eq. 120].
- Bernardeau et al. (arXiv:astro-ph/0112551) define the power spectrum by $\big<\delta({\bf k})\delta({\bf k}^{\prime})\big>\equiv\delta_{D}({\bf k}+{\bf k}^{\prime})\,P(k)$ [src: Sect. 3.2.2, unnumbered display, last line of the display that opens with Eq. 119].
- Baumann (arXiv:0907.5424) writes the same statement for ℛ with the $(2\pi)^{3}$ factor, $\langle{\cal R}_{\bf k}{\cal R}_{{\bf k}^{\prime}}\rangle=(2\pi)^{3}\delta({\bf k}+{\bf k}^{\prime})P_{\cal R}(k)$ [src: Sect. "Notation", unnumbered display].
- `[der]` The prefactor of the dimensionless spectrum follows the Fourier convention: compare Baumann's notation section and Martin et al.'s Eq. 17 with Bernardeau et al.'s notation table.

### Initial conditions: adiabatic or isocurvature
<!-- key: initial-conditions-adiabatic-or-isocurvature -->

| Reference work | Choice | Place read |
|---|---|---|
| Baumann, arXiv:0907.5424 | adiabatic perturbations defined by a vanishing non-adiabatic pressure, $\delta p_{en}\equiv\delta p-\frac{\dot{\bar{p}}}{\dot{\bar{\rho}}}\delta\rho$ | [src: Sect. 9.2.3, Eq. 137] |
| CLASS input file | `ic = ad` by default; isocurvature modes `bi` (baryon), `cdi` (CDM), `nid` (neutrino density), `niv` (neutrino velocity), combinable as `ad&bi&nid` | [doc: https://raw.githubusercontent.com/lesgourg/class_public/master/explanatory.ini, 2026-10-31] |

## Early universe
<!-- key: early-universe -->

### Slow-roll parameters: Hubble-flow or potential definitions
<!-- key: slow-roll-parameters-hubble-flow-or-potential -->

| Reference work | Parameter | Definition as printed | Place read |
|---|---|---|---|
| Baumann, arXiv:0907.5424 | first Hubble parameter | $\varepsilon\equiv\frac{3}{2}(w_{\phi}+1)=\frac{1}{2}\frac{\dot{\phi}^{2}}{H^{2}}$, boxed in Eq. 70 as minus $\dot{H}/H^{2}$ | [src: Sect. 6.2, Eq. 69] |
| Baumann, arXiv:0907.5424 | second Hubble parameter | $\eta=-\frac{\ddot{\phi}}{H\dot{\phi}}=\varepsilon-\frac{1}{2\varepsilon}\frac{d\varepsilon}{dN}$, with N growing forward in time (text after Eq. 70) | [src: Sect. 6.2, Eq. 73] |
| Baumann, arXiv:0907.5424 | first potential parameter | $\epsilon_{\rm v}(\phi)\equiv\frac{M_{\rm pl}^{2}}{2}\left(\frac{V_{,\phi}}{V}\right)^{2}$ | [src: Sect. 6.2, Eq. 74] |
| Baumann, arXiv:0907.5424 | second potential parameter | $\eta_{\rm v}(\phi)\equiv M_{\rm pl}^{2}\frac{V_{,\phi\phi}}{V}$ | [src: Sect. 6.2, Eq. 75] |
| Kinney, arXiv:0902.1529 | first Hubble parameter | $\epsilon=-\frac{d\ln{H}}{d\ln{a}}=\frac{1}{H}\frac{dH}{dN}$, with N counted backward in time (Eq. 95) | [src: Sect. IV, Eq. 99] |
| Kinney, arXiv:0902.1529 | second Hubble parameter | $\eta\equiv-\frac{\ddot{\phi}}{H\dot{\phi}}=\epsilon+\frac{1}{2\epsilon}\frac{d\epsilon}{dN}$ | [src: Sect. IV, Eq. 103] |
| Martin et al., arXiv:1303.3787 | first Hubble-flow parameter, exact | $\epsilon_{1}=\dfrac{1}{2M_{\scriptscriptstyle{\mathrm{Pl}}}^{2}}\left(\dfrac{\mathrm{d}\phi}{\mathrm{d}N}\right)^{2}$; hierarchy in the list below | [src: Sect. 3.1, Eq. 11] |
| Planck 2018 X, inflation, arXiv:1807.06211 | Hubble-flow parameters | $\epsilon_{1}=-{\dot{H}}/{H^{2}}$ and the higher ones by $\epsilon_{n+1}={\dot{\epsilon}_{n}}/(H\epsilon_{n})$ | [src: Table 1, unnumbered display] |
| Planck 2018 X, arXiv:1807.06211 | potential parameters | $\epsilon_{V}={M_{\mathrm{pl}}^{2}V_{\phi}^{2}}/(2V^{2})$, $\eta_{V}={M_{\mathrm{pl}}^{2}V_{\phi\phi}}/V$, $\xi^{2}_{V}={M_{\mathrm{pl}}^{4}V_{\phi}V_{\phi\phi\phi}}/{V^{2}}$ | [src: Table 1, unnumbered display] |

- Martin et al. (arXiv:1303.3787) define the Hubble-flow hierarchy by $\epsilon_{n+1}\equiv\frac{\mathrm{d}\ln\left|\epsilon_{n}\right|}{\mathrm{d}N},\quad n\geq 0$ [src: Sect. 3.1, Eq. 6].
- `[der]` Baumann's second parameter η (arXiv:0907.5424, Eq. 73) and Kinney's (arXiv:0902.1529, Eq. 103) are the same expression in the field, minus the ratio of the field's second derivative to its first times H; the opposite sign in front of the e-fold derivative follows the opposite direction of N in the two texts. Neither is the second Hubble-flow parameter of Martin et al. or of Planck 2018 X.

Relations between Hubble and potential parameters stated by the papers:

- Baumann (arXiv:0907.5424) states, in the slow-roll approximation, $\varepsilon\approx\epsilon_{\rm v}\,,\hskip 18.49988pt\eta\approx\eta_{\rm v}-\epsilon_{\rm v}$ [src: Sect. 6.2, Eq. 80].
- Kinney (arXiv:0902.1529), with the full Planck mass, gives $\epsilon=\frac{4\pi}{m_{\rm Pl}^{2}}\left(\frac{\dot{\phi}}{H}\right)^{2}\simeq\frac{m_{\rm Pl}^{2}}{16\pi}\left(\frac{V^{\prime}\left(\phi\right)}{V\left(\phi\right)}\right)^{2}$ [src: Sect. IV, Eq. 104].
- Martin et al. (arXiv:1303.3787) give, at leading order in slow roll, $\epsilon_{1}\simeq\frac{M_{\scriptscriptstyle{\mathrm{Pl}}}^{2}}{2}\left(\frac{V_{\phi}}{V}\right)^{2}$ [src: Sect. 3.1, Eq. 7].
- Martin et al. (arXiv:1303.3787) give $\epsilon_{2}\simeq 2M_{\scriptscriptstyle{\mathrm{Pl}}}^{2}\left[\left(\frac{V_{\phi}}{V}\right)^{2}-\frac{V_{\phi\phi}}{V}\right]$ [src: Sect. 3.1, Eq. 8].
- Martin et al. (arXiv:1303.3787) give $\epsilon_{2}\epsilon_{3}\simeq 2M_{\scriptscriptstyle{\mathrm{Pl}}}^{4}\left[\frac{V_{\phi\phi\phi}V_{\phi}}{V^{2}}-3\frac{V_{\phi\phi}}{V}\left(\frac{V_{\phi}}{V}\right)^{2}+2\left(\frac{V_{\phi}}{V}\right)^{4}\right]$ [src: Sect. 3.1, Eq. 9].
- Planck 2018 X (arXiv:1807.06211) obtains its constraints on the potential parameters "by an exact remapping" of those on the Hubble-flow parameters [src: Sect. 4.1].
- The CLASS input file computes the tensor tilt, when `n_t = scc`, from the single-field slow-roll self-consistency condition, written there as -r/8*(2-r/8-n_s) [doc: https://raw.githubusercontent.com/lesgourg/class_public/master/explanatory.ini, 2026-10-31].

### Sign and normalisation of f_NL, and the shape template
<!-- key: sign-and-normalisation-of-fnl-and-the-shape -->

| Reference work | Variable expanded | Definition as printed | Place read |
|---|---|---|---|
| Komatsu 2010, CMB non-Gaussianity review, arXiv:1003.6097 | Bardeen's curvature perturbation Φ of the matter era, with $\zeta=\frac{5}{3}\Phi$ [src: Sect. 3.3, inline, text after Eq. 23] | $\Phi=\Phi_{L}+f_{\rm NL}^{\rm local}\Phi^{2}_{L}$ [src: Sect. 3.3, inline, text after Eq. 25] | Sect. 3.3 |
| Planck 2018 IX, arXiv:1905.05697 | Φ, three fifths of ζ on superhorizon scales (Sect. 2.1) | local bispectrum of Φ in Eq. 3; equilateral and orthogonal templates in Eqs. 1–2 | [src: Sects. 2.1–2.2, Eqs. 1–3] |
| Baumann, arXiv:0907.5424 | ℛ | ${\cal R}({\bf x})={\cal R}_{g}({\bf x})+\frac{3}{5}f_{\rm NL}^{\cal R}\star{\cal R}_{g}^{2}({\bf x})$ | [src: Sect. 17.1.3, Eq. 273] |
| Malik & Wands, arXiv:0809.4944 | ζ in their sign convention (Eq. 7.61) | $\zeta=\zeta_{1}+\frac{3}{5}f_{NL}\zeta_{1}^{2}+\frac{9}{25}g_{NL}\zeta_{1}^{3}+\ldots$ | [src: Sect. 11, Eq. 11.13] |
| Chen, arXiv:1002.1416 | ζ, through a dimensionless shape function S | $S(k_{1},k_{2},k_{3})\xrightarrow[\rm limit]{k_{1}=k_{2}=k_{3}}\frac{9}{10}f_{NL}$ | [src: Sect. 5.2, Eq. 5.10] |

- Baumann (arXiv:0907.5424) gives the local bispectrum of ℛ as $B_{\cal R}(k_{1},k_{2},k_{3})=\frac{6}{5}f_{\rm NL}^{\cal R}\Bigl[P_{\cal R}(k_{1})P_{\cal R}(k_{2})+P_{\cal R}(k_{2})P_{\cal R}(k_{3})+P_{\cal R}(k_{3})P_{\cal R}(k_{1})\Bigr]$ [src: Sect. 17.1.3, Eq. 274].
- Malik & Wands (arXiv:0809.4944) give the bispectrum of ζ with the same coefficient, $B_{\zeta}(\mathbf{k}_{1},\mathbf{k}_{2},\mathbf{k}_{3})=\frac{6}{5}{f_{NL}}\left[P_{\zeta}(k_{1})P_{\zeta}(k_{2})+P_{\zeta}(k_{2})P_{\zeta}(k_{3})+P_{\zeta}(k_{3})P_{\zeta}(k_{1})\right]$ [src: Sect. 11, Eq. 11.7].
- Komatsu (arXiv:1003.6097) writes the bispectrum of Φ as $\langle\Phi({\bm{k}_{1}})\Phi({\bm{k}_{2}})\Phi({\bm{k}_{3}})\rangle=(2\pi)^{3}\delta^{D}(\bm{k}_{1}+\bm{k}_{2}+\bm{k}_{3})F(k_{1},k_{2},k_{3})$ [src: Sect. 3.3, Eq. 24].
- Komatsu (arXiv:1003.6097) gives the squeezed limit of the local form as $F_{\rm local}(k_{1},k_{1},k_{3}\to 0)=4f_{\rm NL}^{\rm local}P_{\Phi}(k_{1})P_{\Phi}(k_{3})$ [src: Sect. 3.3, Eq. 26].
- Komatsu (arXiv:1003.6097) quotes, for single-field slow-roll inflation with a canonical kinetic term (Maldacena; Acquaviva et al.), $F_{\rm local}(k_{1},k_{1},k_{3}\to 0)=\frac{5}{3}(1-n_{s})P_{\Phi}(k_{1})P_{\Phi}(k_{3})$ [src: Sect. 3.3, Eq. 27].
- Planck 2018 IX (arXiv:1905.05697) writes the local template as $B^{\rm local}_{\Phi}(k_{1},k_{2},k_{3})=2f^{\rm local}_{\rm NL}\Big[P_{\Phi}(k_{1})P_{\Phi}(k_{2})+P_{\Phi}(k_{1})P_{\Phi}(k_{3})+P_{\Phi}(k_{2})P_{\Phi}(k_{3})\Big]=2A^{2}f^{\rm local}_{\rm NL}\left[\frac{1}{k_{1}^{4-n_{\rm s}}k_{2}^{4-n_{\rm s}}}+{\rm cycl.}\right]$ [src: Sect. 2.2, Eq. 3].
- Chen (arXiv:1002.1416) normalises the bispectrum by $\langle\zeta^{3}\rangle\equiv S(k_{1},k_{2},k_{3})\frac{1}{(k_{1}k_{2}k_{3})^{2}}\tilde{P}_{\zeta}^{2}(2\pi)^{7}\delta^{3}(\sum_{i=1}^{3}{\bf k}_{i})$ [src: Sect. 5.2, Eq. 5.9], with the fiducial $\tilde{P}_{\zeta}$ fixed to $6.1\times 10^{-9}$ at $k_{\rm wmap}=0.027$ Mpc⁻¹ (arXiv:1002.1416) [src: Sect. 5.2, text after Eq. 5.9]. <!-- eq: notation -->
- `[der]` The variables expanded differ in sign between these works (Malik & Wands' ζ of Eq. 7.61, Riotto's ζ of Sect. 7.7, Baumann's ℛ of Eq. 139) and in normalisation (Φ of the matter era against ζ or ℛ), so an f_NL value is quoted with its variable. No paper read here states the conversion of the sign of f_NL between these conventions (see "Not verified").

### Tensor-to-scalar ratio and the pivot scale
<!-- key: tensor-to-scalar-ratio-and-the-pivot-scale -->

| Reference work | Pivot and definition | Place read |
|---|---|---|
| Planck 2018 X, arXiv:1807.06211 | all primordial quantities at $k_{*}=0.05$ Mpc⁻¹ unless stated; r also quoted as $r_{0.002}$ at $k_{*}=0.002$ Mpc⁻¹ to compare with earlier tensor constraints | [src: Table 1 caption; Sect. 2.1, footnote 3] |
| Planck 2018 X, arXiv:1807.06211 | scalar spectrum $\ln\mathcal{P_{R}}(k)=\ln A_{\mathrm{s}}+(n_{\mathrm{s}}-1)\ln(k/k_{*})\equiv\ln\mathcal{P}_{0}(k)$ | [src: Sect. 2.1, Eq. 3] |
| Planck 2018 X, arXiv:1807.06211 | tensor spectrum normalised by r at the pivot: $\ln\mathcal{P}_{\mathrm{t}}(k)=\ln(rA_{\mathrm{s}})+n_{\mathrm{t}}\ln(k/k_{*})+\ldots$ | [src: Sect. 2.1, Eq. 5] |
| BICEP/Keck XIII 2021, arXiv:2110.00483 | quotes its tensor bound as $r_{0.05}$, the ratio at 0.05 Mpc⁻¹ | [src: abstract] |
| CLASS input file | `k_pivot = 0.05` (Mpc⁻¹) by default; `r` is the tensor-to-scalar ratio at the pivot | [doc: https://raw.githubusercontent.com/lesgourg/class_public/master/explanatory.ini, 2026-10-31] |
| CAMB 2.0.5 `InitialPowerLaw.set_params` | `pivot_scalar=0.05` and `pivot_tensor=0.05` (Mpc⁻¹) by default; `nt=None` uses the inflation consistency relation | [doc: https://raw.githubusercontent.com/cmbant/CAMB/master/camb/initialpower.py, 2026-10-31] |

- Martin et al. (arXiv:1303.3787) normalise the tensor spectrum of the mode functions as $\mathcal{P}_{h}(k)=\frac{2k^{3}}{\pi^{2}}\left|\frac{\mu_{\boldsymbol{k}}}{a}\right|^{2}$ [src: Sect. 3.1, Eq. 20].
- Martin et al. (arXiv:1303.3787) give the leading-order amplitudes $\mathcal{P}_{\zeta{{}_{0}}}=\frac{H^{2}}{8\pi^{2}\epsilon_{1}M_{\scriptscriptstyle{\mathrm{Pl}}}^{2}}\,,\qquad\mathcal{P}_{h{{}_{0}}}=\frac{2H^{2}}{\pi^{2}M_{\scriptscriptstyle{\mathrm{Pl}}}^{2}}$ [src: Sect. 3.1, Eq. 22].
- `[der]` The two pivots of Planck 2018 X differ by a factor of the ratio of scales, and r at one pivot equals r at the other only for a scale-invariant tensor-to-scalar ratio; state the pivot with every r.

## Structure formation and dark sector
<!-- key: structure-formation-and-dark-sector -->

### Bias basis and the normalisation of each operator
<!-- key: bias-basis-and-the-normalisation-of-each -->

| Reference work | Basis | Place read |
|---|---|---|
| Ivanov, arXiv:2212.08488 | galaxy density as a time integral over the fluid trajectory of operators built from δ, the tidal field $t^{ij}$ and their derivatives; at leading order the linear bias $b_{1}$, a Wilson coefficient fixed by data | [src: Sect. 7, Eqs. 122–123] |
| Maus et al. 2024, EFT-model comparison for DESI, arXiv:2404.07272 | velocileptors, Lagrangian bias at the initial position: $F(\bm{q})=1+b_{1}\delta_{0}+\frac{1}{2}b_{2}(\delta_{0}(\bm{q})^{2}-\left\langle\delta_{0}^{2}\right\rangle)+b_{s}(s_{0}^{2}(\bm{q})-\left\langle s^{2}\right\rangle)$ | [src: Sect. 3.1, Eq. 10] |
| Maus et al., arXiv:2404.07272 | PyBird: four bias parameters $b_{1},b_{2},b_{3},b_{4}$, related to the CLASS-PT basis by linear transformations | [src: Sect. 3.3] |
| Chudaykin, Ivanov & Philcox 2025, DESI DR1 reanalysis, arXiv:2507.13433 | linear, quadratic, tidal and third-order biases $b_{1},b_{2},b_{\mathcal{G}_{2}},b_{\Gamma_{3}}$ | [src: Sect. V.3, Eq. 57] |

Relations stated by the papers:

- Maus et al. (arXiv:2404.07272) give the Eulerian biases of the "co-evolution" case, with Lagrangian $b_{s}^{\rm L}$ and $b_{3}^{\rm L}$ set to zero, as $b_{2}^{\rm E}=b_{2}^{\rm L}+\frac{8}{21}b_{1}^{\rm L}\quad,\quad b_{s}^{\rm E}=-\frac{2}{7}(b_{1}^{\rm E}-1)\quad,\quad b_{3}^{\rm E}=b_{1}^{\rm E}-1$ [src: Sect. 3.5, Eq. 15].
- Maus et al. (arXiv:2404.07272) give the co-evolution values used by FOLPS as $b_{s^{2}}=-\frac{4}{7}(b^{\rm E}_{1}-1)\quad\text{and}\quad b_{3\rm nl}=\frac{32}{315}(b^{\rm E}_{1}-1)$ [src: Sect. 3.5, Eq. 16].
- Maus et al. map velocileptors onto PyBird in the co-evolution case, with $b_{3}^{\rm L}$ and $b_{s}^{\rm L}$ zero, by $\tilde{b}_{1}=b_{1}^{\rm v}+1$ $\tilde{b}_{2}=\frac{7}{2}\left(\frac{2}{7}+b_{s}^{\rm L}\right)=1$ $\tilde{b}_{3}=\frac{7(42-145b_{1}^{v}-21b_{3}^{v}+630b_{s}^{\rm L})}{441}=\frac{294-1015(b_{1}-1)}{441}$ $\tilde{b}_{4}=-\frac{7}{5}(b_{1}-1)-\frac{7}{10}b_{2}^{\rm v}$ (arXiv:2404.07272) [src: Sect. 3.5, Eq. 17], the rows of one display.
- Maus et al. (arXiv:2404.07272) state that a direct mapping between the bias schemes of two codes is not always possible, because one code can group terms in ways another cannot reproduce by a transformation of its bias parameters [src: Sect. 3.5].
- Chudaykin, Ivanov & Philcox (arXiv:2507.13433) state that the official DESI analyses set $b_{\Gamma_{3}}$, $a_{0}$ and $\tilde{c}$ to zero, whereas they vary them [src: Sect. V.3].
- As printed, the co-evolution coefficient of the tidal bias is −2/7 for $b_{s}$ in Eq. 15 and −4/7 for $b_{s^{2}}$ in Eq. 16 of arXiv:2404.07272 [src: Sect. 3.5, Eqs. 15–16]: the tidal operator is normalised differently in the two codes, and a tidal bias is quoted with its operator.

### Perturbation-theory kernels: the time dependence assumed
<!-- key: perturbation-theory-kernels-the-time-dependence -->

| Reference work | Choice | Place read |
|---|---|---|
| Bernardeau et al., arXiv:astro-ph/0112551 | second-order density kernel in an Einstein–de Sitter universe: $F_{2}({\bf q}_{1},{\bf q}_{2})=\frac{5}{7}+\frac{1}{2}\frac{{\bf q}_{1}\cdot{\bf q}_{2}}{q_{1}q_{2}}(\frac{q_{1}}{q_{2}}+\frac{q_{2}}{q_{1}})+\frac{2}{7}\frac{({\bf q}_{1}\cdot{\bf q}_{2})^{2}}{q_{1}^{2}q_{2}^{2}}$ | [src: Eq. 45] |
| Ivanov, arXiv:2212.08488 | the "Einstein-de-Sitter" approximation: $\Omega_{m}/f^{2}=1$ at zeroth order, justified by $\Omega_{m}\approx f^{2}$ in ΛCDM | [src: Sect. 3.2, inline, text after Eq. 24] |
| Ivanov, arXiv:2212.08488 | kernels $F_{2}$, $G_{2}$ in that approximation | [src: Sect. 3.2, Eq. 28] |
| Wolney et al. 2026, interacting dark sector, arXiv:2603.12431 | kernels with their full time dependence; even weak dark-sector interactions break the EdS approximation, with one-loop deviations that can exceed the percent level | [src: abstract] |
| Verhoeve et al. 2026, PyBird for screened Horndeski, arXiv:2607.26945 | exact time-dependent kernel functions computed by a direct ODE method; exact time dependence retained at modest computational cost | [src: abstract] |

- As printed, Ivanov's review gives the second-order kernel as $F_{2}({\bf q}_{1},{\bf q}_{2})=\frac{5}{7}+\frac{({\bf q}_{1}\cdot{\bf q}_{2})}{q_{1}q_{2}}\left(\frac{q_{1}}{q_{2}}+\frac{q_{2}}{q_{1}}\right)+\frac{2}{7}\frac{({\bf q}_{1}\cdot{\bf q}_{2})^{2}}{q_{1}^{2}q_{2}^{2}}$ (arXiv:2212.08488, v1) [src: Sect. 3.2, Eq. 28], without the factor one half in front of the dipole term that the Bernardeau et al. review prints (arXiv:astro-ph/0112551, Eq. 45, in the first table row above). Quote the kernel from Bernardeau et al., not from this display.

### Dark-energy and modified-gravity parameterisations and their signs
<!-- key: dark-energy-and-modified-gravity -->

Effective field theory of dark energy, unitary-gauge action:

| Reference work | Action as printed | Place read |
|---|---|---|
| Gubitosi, Piazza & Vernizzi 2013, arXiv:1210.0201 | $S=\int d^{4}x\sqrt{-g}\left[\frac{M_{*}^{2}}{2}f(t)R-\Lambda(t)-c(t)g^{00}\right]+S_{DE}^{(2)}$ | [src: Sect. 2.2, Eq. 12] |
| Planck 2015 XIV, arXiv:1502.01590 | $S=\int d^{4}x\sqrt{-g}\left\{\frac{m_{0}^{2}}{2}\left[1+\Omega(\tau)\right]R+\Lambda(\tau)-a^{2}c(\tau)\delta g^{00}\right.$ $\left.+\ \frac{M_{2}^{4}(\tau)}{2}\left(a^{2}\delta g^{00}\right)^{2}-\bar{M}_{1}^{3}(\tau){2}a^{2}\delta g^{00}\delta{K}^{\mu}_{\mu}\right.$ $\left.-\ \frac{\bar{M}_{2}^{2}(\tau)}{2}\left(\delta K^{\mu}_{\mu}\right)^{2}-\frac{\bar{M}_{3}^{2}(\tau)}{2}\delta K^{\mu}_{\nu}\delta K^{\nu}_{\mu}+\frac{a^{2}\hat{M}^{2}(\tau)}{2}\delta g^{00}\delta R^{(3)}\right.$ $\left.+\ m_{2}^{2}(\tau)\left(g^{\mu\nu}+n^{\mu}n^{\nu}\right)\partial_{\mu}\left(a^{2}g^{00}\right)\partial_{\nu}\left(a^{2}g^{00}\right)\vphantom{\frac{m_{0}^{2}}{2}}\right\}$ $+\ S_{\rm{m}}\big[\chi_{i},g_{\mu\nu}\big]$ (the rows of one display; the $\bar{M}_{1}^{3}(\tau){2}$ factor as printed) | [src: Sect. 3.2.1, Eq. 2] |

- As printed, Λ enters with a minus sign in Gubitosi et al. (arXiv:1210.0201, Eq. 12) and with a plus sign in Planck 2015 XIV (arXiv:1502.01590, Eq. 2), and the coefficient of the Ricci scalar is $f(t)$ in the first and $1+\Omega(\tau)$ in the second.
- `[der]` An EFT coefficient is quoted with its action.

The α basis (Bellini & Sawicki):

| Reference work | Choice | Place read |
|---|---|---|
| Bellini & Sawicki 2014, arXiv:1404.3713 | four functions of time: $\alpha_{\textrm{K}}$ kineticity, $\alpha_{\textrm{B}}$ braiding, $\alpha_{\textrm{M}}$ Planck-mass run rate, $\alpha_{\textrm{T}}$ tensor speed excess, with the background $H(t)$ and the matter density today; signature (−+++) | [src: Sect. 3.1; Sect. 2, footnote 1] |
| Zumalacárregui et al. 2017, hi_class, arXiv:1605.06102 | Horndeski functions normalised by factoring out $1/(8\pi G_{\rm N})$, so that GR is the case where $G_{4}$ is one half and the other $G_{i}$ vanish; $\alpha_{\textrm{B}}$ enters the background through $M_{*}^{2}$ | [src: Sect. 2, footnote 1, unnumbered display (inline) before Eq. 2.1] |

- hi_class (arXiv:1605.06102) writes the cubic Horndeski term as ${\cal L}_{3}=-G_{3}(\phi,\,X)\Box\phi$ [src: Sect. 2, Eq. 2.3].
- hi_class (arXiv:1605.06102) defines the effective Planck mass as $M_{*}^{2}\equiv 2\left(G_{4}-2XG_{4X}+XG_{5\phi}-\frac{H\phi^{\prime}}{a}XG_{5X}\right)$ [src: Sect. 2.1, Eq. 2.9].

Kinetic term X (Horndeski, k-inflation, EFT):

| Reference work | Definition as printed | Place read |
|---|---|---|
| Kobayashi 2019, Horndeski review, arXiv:1901.07183 | $X:=-g^{\mu\nu}\phi_{\mu}\phi_{\nu}/2$ | [src: Sect. 2.1, inline, text after Eq. 7] |
| Chen, arXiv:1002.1416 | $X=-\frac{1}{2}g^{\mu\nu}\partial_{\mu}\phi\partial_{\nu}\phi$ | [src: Sect. 4, unnumbered display (inline)] |
| Planck 2018 IX, arXiv:1905.05697 | $X=g^{\mu\nu}\partial_{\mu}\phi\thinspace\partial_{\nu}\phi$, in $\mathcal{L}=P(X,\phi)$ | [src: Sect. 2.1, inline, text after Eq. 2] |
| Gubitosi et al., arXiv:1210.0201 | $X\equiv(\partial\phi)^{2}$ | [src: Sect. 2.2, inline, text after Eq. 12] |

- `[der]` With the (−+++) signature these differ in sign and by a factor of two; derivatives of a Lagrangian with respect to X, such as a sound speed, are quoted with the definition of X used.

Phenomenological functions of the potentials (μ, Σ, η):

| Reference work | Definition as printed | Place read |
|---|---|---|
| Planck 2015 XIV, arXiv:1502.01590 | line element with Ψ in $g_{00}$ and Φ in $g_{ij}$: $ds^{2}=a^{2}\left[-(1+2\Psi)d\tau^{2}+(1-2\Phi)dx^{2}\right]$ | [src: Sect. 3, Eq. 1] |
| Planck 2015 XIV, arXiv:1502.01590 | μ modifies the Poisson equation of Ψ: $-k^{2}\Psi\equiv 4\pi Ga^{2}\mu(a,\mathbf{k})\rho\Delta$ | [src: Sect. 3.2.2, Eq. 4] |
| Planck 2015 XIV, arXiv:1502.01590 | Σ modifies the lensing (Weyl) potential: $-k^{2}(\Phi+\Psi)\equiv 8\pi Ga^{2}\Sigma(a,\mathbf{k})\rho\Delta$ | [src: Sect. 3.2.2, Eq. 5] |
| Planck 2015 XIV, arXiv:1502.01590 | gravitational slip $\eta(a,\mathbf{k})\equiv\Phi/\Psi$, called γ in MGCAMB | [src: Sect. 3.2.2, Eq. 6, footnote 2] |
| Planck 2015 XIV, arXiv:1502.01590 | Q modifies the Poisson equation of Φ: $-k^{2}\Phi\equiv 4\pi Ga^{2}Q(a,\mathbf{k})\rho\Delta$ | [src: Sect. 3.2.2, Eq. 3] |

Background equation of state:

| Reference work | Parameterisation | Place read |
|---|---|---|
| Linder 2003, arXiv:astro-ph/0208512 | $w(a)=w_{0}+w_{a}(1-a)$ | [src: Sect. II.2, Eq. 6] |
| Planck 2015 XIV, arXiv:1502.01590 | $(w_{0},w_{a})$ as the first-order Taylor expansion among its background parameterisations | [src: Sect. 3.1] |

### Units of lengths and wavenumbers: Mpc or Mpc/h
<!-- key: units-of-lengths-and-wavenumbers-mpc-or-mpc-h -->

| Reference work | Choice | Place read |
|---|---|---|
| Planck 2018 X, arXiv:1807.06211 | primordial wavenumbers in Mpc⁻¹, pivot $k_{*}=0.05$ Mpc⁻¹ | [src: Table 1 caption; Sect. 2.1] |
| Maus et al., arXiv:2404.07272 | PyBird's default derivative-suppression scale $k_{\rm M}$, set to 0.7 h Mpc⁻¹ | [src: Sect. 3.3] |
| Sánchez 2020, arXiv:2002.07829 | argues against $h^{-1}$ Mpc units: the reference radius of $\sigma_{8}$, 8 $h^{-1}$ Mpc, depends on h; proposes $\sigma_{12}$, defined at 12 Mpc | [src: abstract; Sect. IV] |
| CAMB 2.0.5 Python wrapper | matter power in $({\rm Mpc}/h)^{3}$ against $k/h$ and $\sigma_{R}$ with R in $h^{-1}$ Mpc by default (`hubble_units=True`) | [doc: https://raw.githubusercontent.com/cmbant/CAMB/master/camb/initialpower.py for k in Mpc⁻¹, https://raw.githubusercontent.com/cmbant/CAMB/master/camb/results.py for the matter-power defaults, 2026-10-31] |
| CLASS input file | maximum wavenumber passed either as `P_k_max_h/Mpc` (h/Mpc) or `P_k_max_1/Mpc` (1/Mpc); pivot in Mpc⁻¹ | [doc: https://raw.githubusercontent.com/lesgourg/class_public/master/explanatory.ini, 2026-10-31] |

- Sánchez (arXiv:2002.07829) writes the inferred $\sigma_{8}$ as an average over the posterior of h, $\sigma_{8}=\int\sigma\left(R=\left(8/h\right)\,{\rm Mpc}\,|\,h\right)\mathcal{P}(h)\,{\rm d}h$ [src: Sect. IV, Eq. 6].

## Not verified
<!-- key: not-verified -->

- The definition of $\Omega_K$ in terms of the curvature constant, and so its sign for a closed universe, was not found in the sources read (Planck 2018 VI, Clifton et al., Copeland et al. were searched).
- Riemann and Ricci sign conventions: only Clifton et al. (arXiv:1106.2476, Sect. 1) and Malik & Wands (arXiv:0809.4944, App. A.1) state theirs; the other anchors state only the signature.
- Desjacques, Jeong & Schmidt, the large-scale bias review (arXiv:1611.09787), has no HTML rendering (the ar5iv fallback returns no content): its bias bases and conversion formulae were not read. A maintainer may read the PDF.
- The operator definitions of the $b_{\mathcal{G}_{2}}$, $b_{\Gamma_{3}}$ basis (Galileon operators) were not read in a source; only the parameter set of arXiv:2507.13433 (Eq. 57).
- The sign relation between f_NL defined with ζ of opposite sign conventions, or with Maldacena's convention, was not found stated in a paper read.
- Expressions of $n_{\rm s}$, r and $n_{\rm t}$ in slow-roll parameters beyond leading order were not read.
- The normalisation of isocurvature modes (amplitudes, correlation angle) in Planck 2018 X was not read.
- The definitions of the α functions in terms of the Horndeski functions (Bellini & Sawicki, their App. A) and the conversion of $\alpha_{\textrm{B}}$ between the Bellini–Sawicki and Gleyzes et al. conventions were not read.
- The anchors on the EFT of inflation (Cheung et al.) and on CLASS (Lesgourgues) were not read for conventions within the budget; the original Chevallier–Polarski paper was not read (only Linder's Eq. 6).
- Textbook conventions (Misner–Thorne–Wheeler, Weinberg, Dodelson, Mukhanov) were not read through a secondary source, beyond the two reviews above that state they follow Misner, Thorne and Wheeler.
