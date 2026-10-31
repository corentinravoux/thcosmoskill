Scope: model-independent results of the P0 probe subtopics — the single-field consistency relation and one QFT-in-de-Sitter result — and their history.

Snapshot: 2026-10-31

## Theorems and consistency conditions

### Single-field consistency relation (squeezed limit)

- **Statement.** Creminelli & Zaldarriaga 2004 (arXiv:astro-ph/0407059) show that, if the inflaton is the only dynamical field, the three-point function with one momentum much smaller than the other two is fixed by the power spectrum and its tilt, independently of the inflaton Lagrangian [src: abstract].
- **Equation.** The relation reads $\lim_{k_{1}\rightarrow 0}\langle\zeta_{\vec{\kappa}_{1}}\zeta_{\vec{\kappa}_{2}}\zeta_{\vec{\kappa}_{3}}\rangle=-(2\pi)^{3}\delta^{3}(\sum_{i}\vec{k}_{i})(n_{s}-1)P_{k_{1}}P_{k_{3}}\;$ (arXiv:astro-ph/0407059) [src: Eq. 1], with $P_{k}$ defined by Eq. 3 of the same paper (see formalism.md). The paper prints $\vec{\kappa}_{i}$ on the left and $\vec{k}_{i}$ on the right; it is copied as printed.
- **Local template in the same limit.** For the local $f_{\rm NL}$ of Eq. 5 of that paper, the squeezed limit is $\lim_{k_{1}\rightarrow 0}\langle\zeta_{\vec{\kappa}_{1}}\zeta_{\vec{\kappa}_{2}}\zeta_{\vec{\kappa}_{3}}\rangle=(2\pi)^{3}\delta^{3}(\sum_{i}\vec{k}_{i})\;4f_{\rm NL}P_{k_{1}}P_{k_{3}}\;$ (arXiv:astro-ph/0407059) [src: Eq. 6].
- **Original slow-roll statement.** Maldacena 2002 (arXiv:astro-ph/0210603) states that in a particular limit the three-point functions are determined completely by the tilt of the spectrum [src: abstract].
- **Multi-soft generalisation (2026).** Ullah 2026 (arXiv:2604.09765) derives tree-level multi-soft theorems at leading order in the soft expansion for scalar and tensor correlators with the background-wave method [src: abstract]. Its single-soft scalar theorem in terms of stripped correlators is $\lim_{\vec{k}_{1}\rightarrow 0}\langle\zeta(\vec{k}_{1}\dots\zeta(\vec{k_{N}})\rangle^{\prime}=\langle\zeta(\vec{k_{1}})\zeta(-\vec{k}_{1})\rangle^{\prime}\delta_{\zeta}\langle\zeta(\vec{k}_{2})\dots\zeta(\vec{k}_{N})\rangle^{\prime}$ (arXiv:2604.09765) [src: Eq. 14], with $\delta_{\zeta}$ the operator defined in Sect. 2 of that paper (not transcribed here); the unbalanced parenthesis is the paper's.
- **What a violation would mean.** Ullah 2026 (arXiv:2604.09765) states that a violation of the scalar soft theorem would rule out all attractor single-field models and point to multi-field dynamics or a non-attractor phase [src: abstract].

### Observability of the squeezed limit

- Pajer, Schmidt & Zaldarriaga 2013 (arXiv:1305.0824) show, using conformal Fermi coordinates, that Maldacena's squeezed scalar bispectrum and the tensor–scalar–scalar bispectrum of slow-roll single-field inflation lead to no deviation from a Gaussian universe except projection effects: the primordial contributions to the squeezed CMB bispectrum and to scale-dependent halo bias vanish [src: abstract].

## QFT in de Sitter

### Hilbert-space decomposition (Penedones et al. 2023)

- **Method and scope.** arXiv:2301.04146 decomposes the Hilbert space of QFT in $\text{dS}_{d+1}$ into unitary irreducible representations of $\text{SO}(1,d+1)$, using Harish-Chandra characters and numerical diagonalisation of the truncated quadratic Casimir; results are complete for $d=1$ and $d=2$ [src: abstract]. <!-- num: not a value --> <!-- eq: notation -->
- **Complementary series in two-particle states, $d\geq 3$.** For each pair $(n,s)$ of non-negative integers with $\Delta_{1}+\Delta_{2}-d-s-2n>\frac{d}{2}$, the tensor product $\mathcal{C}_{\Delta_{1},0}\otimes\mathcal{C}_{\Delta_{2},0}$ of $\text{SO}(1,d+1)$ contains a complementary series (arXiv:2301.04146) [src: Table 1.3, footnote 6]. The table lists it as $\mathcal{C}_{\Delta_{1}+\Delta_{2}-d-s-2n,s}$ [src: Table 1.3]. <!-- num: not a value -->
- **Photon inside two massless scalars.** The tensor product ${\cal V}_{1,0}\otimes{\cal V}_{1,0}$ contains the type II exceptional series ${\cal U}_{1,0}$: the two-particle Hilbert space of two different massless scalars has an invariant subspace that is a photon, shown in $\text{dS}_{4}$ and stated to hold in higher dimensions (arXiv:2301.04146) [src: Sect. 4.4]. The coefficients of the photon state solve the recurrence with the general solution $c_{n}=\frac{A}{(n+1)(n+2)}$ (arXiv:2301.04146) [src: Eq. 4.26], and the state is normalisable, ${}_{a,b}\langle\chi|\chi\rangle_{a,b}=2|A|^{2}\sum_{n\geq 1}\frac{1}{n(n+2)}<\infty$ (arXiv:2301.04146) [src: Eq. 4.27]. The paper calls this an example of a novel result [src: Sect. 1].
- **Earlier results it builds on.** For $\text{SO}(1,3)$, Naimark found that $\mathcal{C}_{\Delta_{1}}\otimes\mathcal{C}_{\Delta_{2}}$ can contain one complementary series $\mathcal{C}_{\Delta_{1}+\Delta_{2}-2}$ when $\Delta_{1}+\Delta_{2}>3$, as reported by arXiv:2301.04146 [sec: Sect. 1, Brief literature review]; Naimark's papers predate arXiv and were not read. <!-- num: not a value -->
- **Källén–Lehmann representation.** Hogervorst et al. 2021 (arXiv:2107.13871) recover the Källén–Lehmann spectral decomposition of the scalar bulk two-point function from the Hilbert-space decomposition, relate poles of the spectral densities to boundary CFT data, and derive an inversion formula for the spectral density by continuation from the sphere [src: abstract].
- **Recent use (2026).** Belrhali, Poisson, Renaux-Petel & Werth 2026 (arXiv:2601.15228) build a momentum space for QFT in $\text{dS}_{d+1}$ in Poincaré slicing in which the dS frequency is the unitary-representation label of $\text{SO}(1,d+1)$, reformulate in-in perturbation theory in it, and accommodate principal and complementary series in the Källén–Lehmann decomposition of composite operators [src: abstract]. <!-- num: not a value -->

## History of the key results

| Year | Result | Paper | Status |
|---|---|---|---|
| 2002 | Slow-roll bispectrum computed; squeezed limit fixed by the tilt | Maldacena, arXiv:astro-ph/0210603 [src: abstract] | Standard; equations read here through the review arXiv:1002.1416 [src: Eqs. 4.22–4.23] |
| 2004 | Squeezed-limit relation for any single-field Lagrangian | Creminelli & Zaldarriaga, arXiv:astro-ph/0407059 [src: abstract] | Standard |
| 2013 | Relation is a coordinate (projection) effect; no primordial squeezed signal in observables | Pajer, Schmidt & Zaldarriaga, arXiv:1305.0824 [src: abstract] | Refines how the 2002/2004 results are read, does not supersede them |
| 2021 | Källén–Lehmann decomposition of dS two-point functions from the Hilbert space | Hogervorst et al., arXiv:2107.13871 [src: abstract] | Basis of the non-perturbative dS bootstrap |
| 2023 | UIR content of free multi-particle and CFT Hilbert spaces in dS | Penedones et al., arXiv:2301.04146 [src: abstract] | Complete for $d=1,2$; open for $d\geq 3$ [src: Sect. 1] <!-- eq: notation --> |
| 2026 | Multi-soft theorems for scalars and tensors, tree level, leading soft order | Ullah, arXiv:2604.09765 [src: abstract] | Recent, single-author; no reply found |

## Not verified

- The general-$d$ results of arXiv:2301.04146 for spinning complementary series are described by the paper as very incomplete [src: Table 1.3 caption]; none is given here.
- Naimark's $\text{SO}(1,3)$ result is quoted only through arXiv:2301.04146; no primary paper or DOI was read. <!-- num: not a value -->

- The squeezed-limit $f_{\rm NL}$ value implied by comparing Eqs. 1 and 6 of arXiv:astro-ph/0407059: the sentence that states it was not located with the tool (a grep for the fraction returned nothing), and no agent-made value is given.
- No date-sorted search from 2025-06-01 returned a correction to the tree-level slow-roll bispectrum itself; two searches were run (in-in bispectrum; squeezed limit and soft theorems).
