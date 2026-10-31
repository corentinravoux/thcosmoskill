Scope: formalism of primordial correlators — in-in calculation of the single-field scalar bispectrum, the squeezed-limit consistency relation, and one QFT-in-de-Sitter result (P0 probe, three subtopics only).

Snapshot: 2026-10-31

## Conventions

The conventions below are those of the main source for each subtopic, as that source states them; they are not converted into one another.

- **Metric signature (in-in, slow roll):** Chen 2010 (arXiv:1002.1416) uses the signature $(-1,1,1,1)$ [src: Sect. 4, text after Eq. 4.1]. <!-- num: not a value -->
- **ADM line element:** $ds^{2}=-N^{2}dt^{2}+h_{ij}(dx^{i}+N^{i}dt)(dx^{j}+N^{j}dt)~$ (Chen 2010, arXiv:1002.1416) [src: Eq. 4.3].
- **Planck mass:** Chen 2010 (arXiv:1002.1416) uses the reduced Planck mass $M_{\rm P}$, defined as $(8\pi G)^{-1/2}$, and then sets it to one [src: Sect. 4, text after Eq. 4.1]. <!-- num: not a value -->
- **Slow-roll parameters:** Chen 2010 (arXiv:1002.1416) uses the Hubble-flow parameters $\epsilon=-\frac{\dot{H}}{H^{2}}~,~~~\eta=\frac{\dot{\epsilon}}{\epsilon H}~$ [src: Eq. 4.2].
- **Slow-roll parameters (Maldacena).** Maldacena 2002 (arXiv:astro-ph/0210603) defines $\epsilon$ and $\eta$ from the potential, so its $\eta$ is not the $\eta$ of arXiv:1002.1416 [src: unnumbered display, no section or number in the rendering]; see "Not verified".
- **Gauge and curvature variable:** Chen 2010 (arXiv:1002.1416) works in comoving (uniform-inflaton) gauge, $h_{ij}=a^{2}e^{2\zeta}\delta_{ij}~$ [src: Eq. 4.7], in which the inflaton fluctuation vanishes.
- **Fourier convention:** Chen 2010 (arXiv:1002.1416) writes $u_{k}=\int d^{3}x\zeta(t,{\bf x})e^{-i{\bf k}\cdot{\bf x}}~$ [src: Eq. 4.13].
- **Time variable:** Chen 2010 (arXiv:1002.1416) uses cosmic time $t$ in the action and conformal time $\tau$, approximately minus the comoving Hubble radius, in the mode functions [src: Sect. 4, text after Eq. 4.14].
- **Power-spectrum normalisation:** Chen 2010 (arXiv:1002.1416) defines $P_{\zeta}$ through $\langle\zeta({\bf k}_{1})\zeta({\bf k}_{2})\rangle=\frac{P_{\zeta}}{2k_{1}^{3}}(2\pi)^{5}\delta^{3}({\bf k}_{1}+{\bf k}_{2})~$ [src: Eq. 4.17].
- **de Sitter conventions (QFT in dS):** see the subsection below; Penedones et al. work in $(d+1)$-dimensional de Sitter space with isometry group $SO(1,d+1)$ (arXiv:2301.04146) [src: abstract]. <!-- num: not a value -->

## In-in formalism and the single-field scalar bispectrum
<!-- subtopic: inin-bispectrum -->

### The in-in expectation value

- Chen 2010 (arXiv:1002.1416), following Weinberg's presentation, writes the expectation value of an operator $Q$ at the end of inflation in the interacting vacuum as $\langle Q\rangle=\langle\Omega|F^{-1}(t,t_{0})Q^{I}(t)F(t,t_{0})|\Omega\rangle~$ [src: Eq. 3.23, first row]; the second row of the same display writes $F$ and $F^{-1}$ as anti-time-ordered and time-ordered exponentials of the interaction Hamiltonian.
- The interaction-picture evolution operator is $F(t,t_{0})=T\exp\left(-i\int_{t_{0}}^{t}H_{I}(t)dt\right)~$ (Chen 2010, arXiv:1002.1416) [src: Eq. 3.22].
- At first order in the cubic interaction Hamiltonian, the three-point function is the commutator $\langle\zeta_{n}^{3}\rangle=-i\langle 0|\int_{t_{0}}^{t}dt[\zeta_{n}({\bf k}_{1})\zeta_{n}({\bf k}_{2})\zeta_{n}({\bf k}_{3}),H_{I,3}]|0\rangle~$ (Chen 2010, arXiv:1002.1416) [src: Eq. 4.20].
- For single-field models the cubic interaction Hamiltonian is minus the cubic Lagrangian (Chen 2010, arXiv:1002.1416) [src: Sect. 4, text after Eq. 4.18].

### Quadratic and cubic actions in comoving gauge

- The canonical single-field action of Chen 2010 (arXiv:1002.1416) is printed as $S=\int d^{4}x\sqrt{-g}\left[\frac{M_{\rm P}}{2}R+X-V(\phi)\right]~$ [src: Eq. 4.1]. The rendering prints $M_{\rm P}$ without a square in front of $R$; the paper sets the Planck mass to one right after, so the slip has no effect on later equations; it is transcribed as printed (see "Not verified").
- In that action $X$ is the canonical kinetic term, $X=-\frac{1}{2}g^{\mu\nu}\partial_{\mu}\phi\partial_{\nu}\phi$ (arXiv:1002.1416) [src: Sect. 4, inline, text after Eq. 4.1]. <!-- eq: notation -->
- The quadratic action for $\zeta$ is $S_{2}=\int dtd^{3}x~\left[a^{3}\epsilon\dot{\zeta}^{2}-a\epsilon(\partial\zeta)^{2}\right]~$ (Chen 2010, arXiv:1002.1416) [src: Eq. 4.8].
- The cubic action, copied row by row as the three rows of the display, is $S_{3}=\int dtd^{3}x\bigg[a^{3}\epsilon^{2}\zeta\dot{\zeta}^{2}+a\epsilon^{2}\zeta(\partial\zeta)^{2}-2a\epsilon\dot{\zeta}(\partial\zeta)(\partial\chi)$ $+\frac{a^{3}\epsilon}{2}\dot{\eta}\zeta^{2}\dot{\zeta}+\frac{\epsilon}{2a}(\partial\zeta)(\partial\chi)\partial^{2}\chi+\frac{\epsilon}{4a}(\partial^{2}\zeta)(\partial\chi)^{2}$ $+f(\zeta)\frac{\delta L}{\delta\zeta}\bigg|_{1}\bigg]~$ (Chen 2010, arXiv:1002.1416) [src: Eq. 4.9].
- The auxiliary field is $\chi=a^{2}\epsilon\partial^{-2}\dot{\zeta}~$ (Chen 2010, arXiv:1002.1416) [src: Eq. 4.10].
- The last term of the cubic action is removed by a field redefinition from $\zeta$ to $\zeta_{n}$ (arXiv:1002.1416) [src: Sect. 4, text after Eq. 4.18].
- Of the redefinition function, only $f(\zeta)=\frac{\eta}{4}\zeta^{2}+{\rm terms~with~derivatives~on~\zeta}~$ contributes outside the horizon (Chen 2010, arXiv:1002.1416) [src: Eq. 4.12].

### Mode function and power spectrum

- With Bunch–Davies initial conditions the mode function is $u_{k}=u({\bf k},\tau)=\frac{iH}{\sqrt{4\epsilon k^{3}}}(1+ik\tau)e^{-ik\tau}~$ (Chen 2010, arXiv:1002.1416) [src: Eq. 4.14].
- The tree-level power spectrum, in units of the reduced Planck mass and evaluated at horizon exit, is $P_{\zeta}=\frac{H^{2}}{8\pi^{2}\epsilon}~$ (Chen 2010, arXiv:1002.1416) [src: Eq. 4.18].

### The slow-roll bispectrum

- Chen 2010 (arXiv:1002.1416) writes the full slow-roll result as $\langle\zeta(\textbf{k}_{1})\zeta(\textbf{k}_{2})\zeta(\textbf{k}_{3})\rangle=(2\pi)^{7}\delta^{3}(\textbf{k}_{1}+\textbf{k}_{2}+\textbf{k}_{3})P_{\zeta}^{2}\frac{1}{\prod_{i}k_{i}^{2}}~S~$ [src: Eq. 4.22].
- This is the review's rendering of the computation of Maldacena 2002 (arXiv:astro-ph/0210603), whose own equations could not be read with a place (see "Not verified").
- The shape function, copied as the two rows of the display, is $S=\frac{\epsilon}{8}\left[-\left(\frac{k_{1}^{2}}{k_{2}k_{3}}+{\rm 2~perm.}\right)+\left(\frac{k_{1}}{k_{2}}+{\rm 5~perm.}\right)+\frac{8}{K}\left(\frac{k_{1}k_{2}}{k_{3}}+{\rm 2~perm.}\right)\right]$ $+\frac{\eta}{8}\left(\frac{k_{1}^{2}}{k_{2}k_{3}}+{\rm 2~perm.}\right)~$ (Chen 2010, arXiv:1002.1416) [src: Eq. 4.23]; $K$ is the sum of the three wavenumbers and $\eta$ the Hubble-flow parameter of the conventions above.
- The $\eta$ term comes entirely from the field redefinition (arXiv:1002.1416) [src: Sect. 4, text after Eq. 4.21].

## Squeezed-limit consistency relation
<!-- subtopic: consistency-relation -->

- **Non-linear curvature variable.** Creminelli & Zaldarriaga 2004 (arXiv:astro-ph/0407059) use the non-linear $\zeta$ for which, once a mode is frozen outside the horizon, the metric is $ds^{2}=-dt^{2}+e^{2\zeta(x)}a(t)^{2}dx_{i}dx_{i}\;$ [src: Eq. 2].
- **Power spectrum (Creminelli & Zaldarriaga normalisation).** The same paper defines $\langle\zeta_{\vec{k}_{i}}\zeta_{\vec{k}_{j}}\rangle=(2\pi)^{3}\delta^{3}(\vec{k}_{i}+\vec{k}_{j})P_{k_{i}}\;$ (arXiv:astro-ph/0407059) [src: Eq. 3].
- This normalisation is not the one of arXiv:1002.1416 given in the conventions above [der]; no paper read in this probe states the relation, so none is given.
- **Local non-linearity parameter.** Creminelli & Zaldarriaga 2004 define $f_{\rm NL}$ through $\zeta(x)=\zeta_{g}(x)-\frac{3}{5}f_{\rm NL}(\zeta_{g}(x)^{2}-\left<\zeta_{g}^{2}\right>)\;$ (arXiv:astro-ph/0407059) [src: Eq. 5]; the factor $3/5$ comes from defining $f_{\rm NL}$ for the Newtonian potential in matter domination [src: footnote 3]. <!-- num: not a value -->


## QFT in de Sitter space
<!-- subtopic: qft-de-sitter -->

- **Setting and units.** Penedones et al. 2023 (arXiv:2301.04146) study QFT in $(d+1)$-dimensional de Sitter space, whose isometry group is $\text{SO}(1,d+1)$ [src: abstract], and take the de Sitter radius to be one [src: Sect. 2, text after Eq. 2.1]. <!-- num: not a value -->
- **Labels of a representation.** In that paper an infinite-dimensional representation of $\text{SO}(1,d+1)$ is fixed by a complex scaling dimension $\Delta$ and, for the symmetric traceless tensors considered, a spin $s$; its quadratic Casimir is $\Delta(d-\Delta)-s(d+s-2)$ (arXiv:2301.04146) [src: Sect. 2.1, inline, first paragraph]. <!-- num: not a value -->
- **The four families for $d\geq 3$** (arXiv:2301.04146) [src: Sect. 2.1, inline list of the four series]: principal series ${\cal P}_{\Delta,s}$ with $\Delta\in\frac{d}{2}+i\mathbb{R}$; complementary series $\mathcal{C}_{\Delta,s}$ with $0<\Delta<d$ for $s=0$ and $1<\Delta<d-1$ for $s\geq 1$; type I exceptional series ${\cal V}_{p,0}$ with $\Delta=d+p-1$, $s=0$, $p\geq 1$; type II exceptional series ${\cal U}_{s,t}$ with $\Delta=d+t-1$, $s\geq 1$, $t=0,1,2\cdots,s-1$. <!-- num: not a value -->
- **Field content.** ${\cal F}_{\Delta,s}$ (principal or complementary) describes a spin-$s$ massive field of mass $m^{2}=\Delta(d-\Delta)$ when $s=0$ (arXiv:2301.04146) [src: Sect. 2.1, inline, paragraph after the list]; ${\cal U}_{s,t}$ describes partially massless gauge fields of spin $s$ and depth $t$, with $t=s-1$ the massless gauge fields [src: Sect. 2.1, paragraph after the list]; ${\cal V}_{1,0}$ is the scalar with gauged shift symmetry $\phi(x)\to\phi(x)+c$ [src: Sect. 2.1, paragraph after the list] (arXiv:2301.04146). <!-- num: not a value -->
- **Pedagogical source.** Sun 2021 (arXiv:2111.04591) is a pedagogical introduction to the unitary irreducible representations of $\text{SO}(1,d+1)$ from the de Sitter QFT viewpoint, including Harish-Chandra characters [src: abstract]; arXiv:2301.04146 cites it for the classification [src: Sect. 2.1, refs. 29, 36, 43]. <!-- num: not a value -->

## Not verified

- **Maldacena 2002 (arXiv:astro-ph/0210603) at source.** The arXiv HTML rendering of this paper carries no equation numbers and no sections (plain-TeX harvmac source), so no equation of it can be given with a checkable place. The slow-roll bispectrum above is transcribed from the review arXiv:1002.1416, which reproduces it in its own conventions; the primary equation (PDF) is left for a maintainer.
- **Slip in arXiv:1002.1416, Eq. 4.1.** The Einstein–Hilbert coefficient is printed without the square of the Planck mass; no corrected version or erratum was found (latest version read). No corrected equation is given here.
