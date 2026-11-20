# Results on cosmological perturbations

Scope: theorems and results that hold independently of one model: conservation of curvature perturbations, gauge-invariance results, isocurvature mode counting, code-comparison accuracies, second-order results; then the history of key results.

Snapshot: 2026-11-20

## Conservation of curvature perturbations
<!-- key: conservation-of-curvature-perturbations -->

| Result | Assumptions as the paper states them | Paper and place |
|---|---|---|
| ζ conserved on super-Hubble scales | adiabatic perturbations (δP_nad = 0), super-Hubble scales (k/𝓗 ≪ 1), "so long as Ψ remains finite"; linear order | Malik & Wands, arXiv:0809.4944 [src: Sect. 8.2.2, Eq. 8.35 and text after Eq. 8.36] |
| uniform-density curvature perturbation conserved, from energy-momentum conservation alone | "sufficiently large scales", non-adiabatic pressure "negligible"; linear perturbations about FRW | Wands et al., arXiv:astro-ph/0003278 [src: abstract] |
| non-linear ζ conserved | universe "smooth over a sufficiently large comoving scale" (gradient expansion); "the pressure is a unique function of the energy density" | Lyth, Malik & Sasaki, arXiv:astro-ph/0411220 [src: abstract; Sect. IV, Eq. 37] |
| non-perturbative, coordinate-free uniform-density and comoving curvature perturbations, evolution on all scales | geometric definitions; recovery of first- and second-order results "on large scales" | Langlois & Vernizzi, arXiv:astro-ph/0503416 [src: abstract] |
| Newtonian-gauge field equations "always have an adiabatic solution" with ℛ non-zero and constant in all eras at large wavelength, plus a second adiabatic mode with ℛ vanishing there | "whatever the constituents of the universe, under only a mild technical assumption about the wavelength dependence of the field equations for large wave length"; universal formulas in terms of the scale factor "in the absence of anisotropic inertia" | Weinberg 2003, arXiv:astro-ph/0302326 [src: abstract] |
| one-loop conservation of superhorizon ζ, loop momenta on all scales | spatially flat gauge, decoupling limit ε → 0, non-linear δN relation between inflaton fluctuation and ζ, boundary terms included | Inomata 2026, arXiv:2606.28247 [src: abstract] |
| second-order comoving curvature perturbation protected from infrared enhancement, $\lim_{k \rightarrow 0} \left( k^2 R_2 \right) = 0$ | second-order cosmological perturbation theory; follows "from a conservation law in the soft limit" | Ireland 2026, arXiv:2608.09897 [src: abstract, inline] |

- Weinberg (arXiv:astro-ph/0302326) also discusses "an apparent discrepancy" with "what appears to be a conservation law in all modes found for large wavelength in synchronous gauge", and concludes that "although equivalent, synchronous and Newtonian gauges suggest inequivalent assumptions about the behavior of the perturbations for large wavelength" [src: abstract].

## Mode counting and gauge results
<!-- key: mode-counting-and-gauge-results -->

- The metric perturbation has 10 degrees of freedom after the SVT split and its constraints (arXiv:0809.4944) [src: Sect. 2.2.2]; scalar, vector and tensor types decouple at linear order and mix through quadratic sources at second order [src: same place]. <!-- num: not a value -->
- The first-order tensor perturbation is gauge invariant (arXiv:0809.4944) [src: Sect. 6.4.1, Eq. 6.43]; in the synchronous gauge "it is not possible to define gauge-invariant quantities in general" [src: Sect. 7.3].
- In linearized perturbation theory, with photons, baryons, neutrinos and a hypothetical CDM component, the most general regular primordial perturbation has one adiabatic and four isocurvature modes, and its quadratic observables are fixed by "a 5×5, real, symmetric matrix-valued function of co-moving wavenumber" (Bucher et al., arXiv:astro-ph/9904231) [src: abstract]; the authors distinguish modes "regular at early times, singular at early times, or pure gauge" [src: abstract]. <!-- num: not a value -->
- Isocurvature vanishes outside the Hubble horizon when $\mathcal{R}_{\varphi}$ freezes out for an inflaton thermalizing with a plasma, under the assumptions of Laine & Procacci (arXiv:2607.06983) [src: Sect. 8.3]; see `formalism.md`.
- A conventional Newtonian N-body simulation "includes all first-order relativistic contributions (in the absence of radiation)" if its coordinates are identified with those of the relativistic N-body gauge, in which the first-order relativistic correction to Zel'dovich initial displacements vanishes (Fidler et al. 2015, arXiv:1505.04756) [src: abstract]; Chisari & Zaldarriaga (arXiv:1101.3555) show that the simulations "are still solving the dynamics correctly even for long modes" and give the conversion to conformal Newtonian gauge [src: abstract].
- With the TT gauge chosen at first order, "the second order tensor mode would be gauge invariant"; the vacuum condition "is the key to guarantee the existence of the TT gauge on cosmological backgrounds" (Xue & Cao, arXiv:2509.26159) [src: abstract].

## Accuracy of the linear calculation
<!-- key: accuracy-of-the-linear-calculation -->

| Claim | Setting | Paper and place |
|---|---|---|
| line-of-sight integration cuts CPU time by "about two orders of magnitude" | compared "to standard methods" in 1996 | Seljak & Zaldarriaga, arXiv:astro-ph/9603033 [src: abstract] |
| precision file cl_3permille.pre "ensures a 0.3% precision on the $C_{l}$'s till l = 3000" | CLASS, basic ΛCDM, the approximations of CLASS II | Blas et al., arXiv:1104.2933 [src: Fig. 10 caption] |
| the ultra-relativistic fluid approximation gives "simultaneously … a 10% faster execution and … more accurate results" | precision file cl_permille.pre with $l_{\rm max}=(k\tau)_{\rm ufa}=18$ | Blas et al., arXiv:1104.2933 [src: Table 3 caption, inline] |
| SymBoltz agrees with modified CLASS at "0.1%–1% … at most scales" | single-interaction dark-sector models | Figueruelo & Sletmoen, arXiv:2611.17384 [src: abstract] |
| ABCMB "sub-percent-level agreement with CLASS" | linear-order ΛCDM CMB | Zhou et al., arXiv:2602.15104 [src: abstract] |
| nanoCMB "sub-percent agreement with CAMB across the multipole range $2 \le \ell \le 2500$" | unlensed TT, EE, TE, flat ΛCDM | Moss, arXiv:2602.23466 [src: abstract] |
| generalized Boltzmann hierarchy plus dispersive fluid approximation reproduce the matter power spectrum "to better than permille accuracy" and parameter constraints "to better than 0.05 sigma" | massive neutrinos in CLASS | Nasiri et al., arXiv:2610.40275 [src: abstract] |
| intrinsic CMB bispectrum biases local $f_{\rm nl}$ by $f_{\rm nl}\sim 0.5$ | second-order Einstein–Boltzmann, all effects "but lensing and time-delay" | Pettinari et al., arXiv:1302.0832 [src: abstract, inline] |

## History of key results
<!-- key: history-of-key-results -->

| Year (arXiv) | Result | Paper | Status |
|---|---|---|---|
| 1995 | Synchronous and conformal Newtonian gauge equations for all species relevant to "any flat CDM, HDM, or CDM+HDM models (including a possible cosmological constant)"; hierarchy truncation scheme; adiabatic initial conditions | Ma & Bertschinger, arXiv:astro-ph/9506072 [src: Sects. 1, 5.3, 7] | current |
| 1995 | δN: spectrum and index of density perturbations with several degrees of freedom | Sasaki & Stewart, arXiv:astro-ph/9507001 [src: abstract] | current; generalised non-linearly by Lyth, Malik & Sasaki (arXiv:astro-ph/0411220, Sect. IV) |
| 1996 | Line-of-sight integration | Seljak & Zaldarriaga, arXiv:astro-ph/9603033 [src: abstract] | current; the method of present codes, for example nanoCMB (arXiv:2602.23466) [src: abstract] |
| 1996 | Gauge transformations and gauge invariance at second order and beyond | Bruni et al., arXiv:gr-qc/9609040 [src: abstract] | current |
| 1999 | Five regular primordial modes, two neutrino isocurvature modes new | Bucher et al., arXiv:astro-ph/9904231 [src: abstract] | current |
| 2000 | ζ conservation from energy conservation alone; separate-universe picture | Wands et al., arXiv:astro-ph/0003278 [src: abstract] | current |
| 2003 | Weinberg's adiabatic modes in all eras | Weinberg, arXiv:astro-ph/0302326 [src: abstract] | current |
| 2004–2005 | Non-linear conservation of ζ (gradient expansion; covariant) | arXiv:astro-ph/0411220; arXiv:astro-ph/0503416 [src: abstracts] | current |
| 2011 | CLASS and its approximation schemes | arXiv:1104.2932; arXiv:1104.2933 [src: abstracts] | current; new approximation-free and differentiable codes since (arXiv:2611.17384; arXiv:2602.15104) [src: abstracts] |
| 2025–2026 | Validity limits of the separate universe (ultra-slow roll, non-minimal coupling, anisotropic backgrounds) and gradient-corrected δN | arXiv:2506.23571; arXiv:2609.34788; arXiv:2607.11814; arXiv:2602.00902 [src: abstracts] | open (see `open-questions.md`) |
| 2025–2026 | Large-scale white noise claimed at second order, then argued by one of the co-authors not to reach $R_2$ | arXiv:2511.13866; arXiv:2511.15803; arXiv:2608.09897 [src: abstracts] | disputed (see `open-questions.md`) |

## Not verified
<!-- key: not-verified -->

- No reply by Barenboim et al. to arXiv:2608.09897 was searched for beyond the date-sorted searches of this run.
- The numerical size of the error of plain hierarchy truncation in modern codes, beyond the 1995 statement quoted by Ma & Bertschinger (Sect. 1) and the CLASS II comparison, was not read.
- Weinberg's theorem (arXiv:astro-ph/0302326) is given from its abstract only; its technical assumption was not read in the body.
