# Approximations in primordial-correlator calculations

Scope: the approximations calculations of primordial correlators rely on, their validated range and quoted error, how they fail, convention traps and numerical issues.

Snapshot: 2026-11-02

## Physical approximations
<!-- key: physical-approximations -->

### Leading order in slow roll
<!-- key: leading-order-in-slow-roll -->
- **Assumes:** the cubic action and the bispectrum are kept at leading order in the Hubble-flow parameters $\epsilon$ and $\eta$, all evaluated at horizon exit (Chen 2010, arXiv:1002.1416) [src: Sect. 4, text after Eq. 4.18]; the result is Eqs. 4.22–4.23 of that review (formalism.md). <!-- num: not a value -->
- **Size:** the bispectrum is of order the slow-roll parameters, $f_{NL}\sim{\cal O}(0.01)$ for these models (arXiv:1002.1416) [src: Sect. 4, text after Eq. 4.23].
- **Fails:** when a slow-roll parameter becomes large transiently, at a feature in the potential (Chen, Easther & Lim 2006, arXiv:astro-ph/0611645) [src: abstract], or in a non-attractor phase where decaying modes are not negligible (Namjoo et al. 2012, arXiv:1210.3692) [src: abstract].
- **Cite:** Maldacena (arXiv:astro-ph/0210603) for the original calculation, through a readable review for equations (formalism.md, "Not verified").

### Decoupling limit of the EFT of inflation
<!-- key: decoupling-limit-of-the-eft-of-inflation -->
- **Assumes:** the mixing of the Goldstone with gravity is negligible, valid at energies above $E_{\rm mix}\simeq M_{2}^{2}/M_{\rm Pl}$, which for observables at energies of order H means $\epsilon/c_{s}^{2}\ll 1$ (Cheung et al. 2007, arXiv:0709.0293) [src: Sect. 4.2, inline, text after Eq. 39]. <!-- num: not a value -->
- **Fails:** otherwise the Goldstone action is not assured to contain the leading effects [src: Sect. 4.2, text after Eq. 39].
- **Cite:** arXiv:0709.0293.

### Perturbativity at small sound speed
<!-- key: perturbativity-at-small-sound-speed -->
- **Assumes:** the Goldstone self-interactions stay weakly coupled up to H; they become strongly coupled at the scale of Eq. 50 of arXiv:0709.0293 (formalism.md). <!-- num: not a value -->
- **Fails:** for fluctuations $\zeta\gtrsim c_{S}^{2}$, non-linear corrections become of order one and the perturbative expansion breaks down, which matters for very rare large fluctuations such as those forming primordial black holes (arXiv:0709.0293) [src: Sect. 4.2, inline, footnote 7]. <!-- num: not a value -->
- **Cite:** arXiv:0709.0293.

### Bunch–Davies initial state
<!-- key: bunch-davies-initial-state -->
- **Assumes:** the positive-frequency solution in the asymptotic past, $\phi^{+}\sim e^{ic_{s}k\eta}$, whose Hermitian analyticity underlies the cosmological cutting rules (Baumann et al. 2022, arXiv:2203.08121) [src: Sect. 3.1, inline, text after Eq. 3.1].
- **Fails:** for excited states built over Bunch–Davies, which enhance folded configurations even when Hadamard (Holman & Tolley 2008, arXiv:0710.1302) [src: abstract]; the loop renormalisation of Braglia et al. likewise requires an initial adiabatic phase continuously related to Bunch–Davies (arXiv:2603.12216) [src: abstract].
- **Cite:** arXiv:2203.08121; arXiv:0710.1302.

### Weak mixing with massive fields (cosmological collider)
<!-- key: weak-mixing-with-massive-fields-cosmological -->
- **Assumes:** the coupling between the massive field and the Goldstone is treated perturbatively, which gives the amplitude estimate $f_{\mathrm{NL}}^{\mathrm{ex}}\sim\varepsilon\mu^{n}\mathrm{e}^{-\pi\mu}$ (Achúcarro et al. 2022, arXiv:2203.08128) [src: Sect. 3.1, inline, text after Eq. 3.8].
- **Fails:** Philcox 2026 shows the weak-mixing assumption is incompatible with current datasets except at the smallest masses (arXiv:2607.18369) [src: abstract]; at strong mixing the Boltzmann suppression is halved (arXiv:2608.23243) [src: abstract]. <!-- num: not a value -->
- **Cite:** arXiv:2607.18369; arXiv:2608.23243.

### Factorisable templates
<!-- key: factorisable-templates -->
- **Assumes:** the exact shape is replaced by a factorisable template, which approximates the equilateral shape of higher-derivative models very well (Creminelli et al. 2006, arXiv:astro-ph/0509029) [src: abstract].
- **Fails:** for shapes with essentially no overlap with the standard templates, such as resonant non-Gaussianity (arXiv:1002.0833) [src: abstract], or collider shapes, which are searched after orthogonalisation against the equilateral and orthogonal templates (arXiv:2512.22085) [src: abstract]. Planck 2018 also fits the exact non-separable EFT, DBI and ghost shapes (arXiv:1905.05697) [src: Sect. 2.1].
- **Cite:** arXiv:astro-ph/0509029; arXiv:0905.3746.

### Sudden decay and the curvaton
<!-- key: sudden-decay-and-the-curvaton -->
- **Assumes:** the curvaton decays instantaneously, which defines the decay fraction $r_{\rm D}$ (Planck 2018 IX, arXiv:1905.05697) [src: Sect. 2.2, inline, text after Eq. 3]. <!-- eq: notation -->
- **Fails:** a different modelling of the curvaton scenario changes the prediction (arXiv:1905.05697) [src: Sect. 2.2].

### Separation of scales for loop back-reaction
<!-- key: separation-of-scales-for-loop-back-reaction -->
- **Assumes:** separation between long and enhanced short scales, and adiabaticity of the long mode; then the one-loop back-reaction on large scales is not observable (Iacconi 2026, arXiv:2605.04815) [src: abstract].
- **Fails:** the proceedings close with scenarios to which the result does not apply (arXiv:2605.04815) [src: abstract]; they were not read.

### Leading-order stochastic inflation
<!-- key: leading-order-stochastic-inflation -->
- **Assumes:** the Fokker–Planck equation of Eq. 2.2 of arXiv:2106.09728 (formalism.md), valid for light fields whose superhorizon interactions are at most marginal (Cohen & Green 2020, arXiv:2007.03693) [src: abstract]. <!-- num: not a value -->
- **Corrections:** non-Gaussian quantum fluctuations enter at NNLO (arXiv:2106.09728) [src: abstract]; the diffusion term receives a two-loop correction (arXiv:2604.14283) [src: abstract].
- **Cite:** arXiv:2007.03693; arXiv:2106.09728.

### Markovian (time-local) environment in decoherence
<!-- key: markovian-time-local-environment-in-decoherence -->
- **Assumes:** the environment acts through a Lindblad equation (Martin & Vennin 2018, arXiv:1801.09949) [src: abstract].
- **Validated:** for gravitational environments, the interactions driving decoherence become time-local and Gaussian deep in the super-Hubble regime, which allows a reliable late-time purity where naive perturbation theory breaks down (Burgess et al. 2026, arXiv:2607.22914) [src: abstract].
- **Fails:** purity alone misjudges quantum correlations when interactions also de-squeeze the state (arXiv:2512.17622) [src: abstract].

## Convention traps
<!-- key: convention-traps -->

- **Two normalisations of the power spectrum.** Chen 2010 writes $\langle\zeta({\bf k}_{1})\zeta({\bf k}_{2})\rangle=\frac{P_{\zeta}}{2k_{1}^{3}}(2\pi)^{5}\delta^{3}({\bf k}_{1}+{\bf k}_{2})~$ (arXiv:1002.1416) [src: Eq. 4.17].
- Creminelli & Zaldarriaga write $\langle\zeta_{\vec{k}_{i}}\zeta_{\vec{k}_{j}}\rangle=(2\pi)^{3}\delta^{3}(\vec{k}_{i}+\vec{k}_{j})P_{k_{i}}\;$ (arXiv:astro-ph/0407059) [src: Eq. 3]. A coefficient moved from one to the other needs the relation, which neither paper states.
- **$f_{\rm NL}$ variable.** Planck templates are written for $\Phi\equiv(3/5)\zeta$ (arXiv:1905.05697) [src: Sect. 2.1, inline, text after Eq. 2]; the hub's atlas lists the variables and signs of other works. <!-- num: not a value -->
- **Second slow-roll parameter.** Chen 2010 uses the Hubble-flow $\eta$ of Eq. 4.2 (arXiv:1002.1416), not the potential parameter $\eta_V$; the hub's atlas collects the definitions. <!-- num: not a value -->
- **"Tilt" in Cheung et al.** Eq. 41 of arXiv:0709.0293 is labelled $n_{s}$ but is the logarithmic derivative of the spectrum (formalism.md, "Effective field theory of inflation"); do not compare it with an $n_{s}-1$ without checking. <!-- num: not a value -->
- **Mass parameter.** $\mu=\sqrt{m^{2}/H^{2}-9/4}$ in the four-dimensional reviews (arXiv:2203.08128) [src: Sect. 3.1, inline, text after Eq. 3.7]; de Sitter representation papers use $\Delta$ with $m^{2}=\Delta(d-\Delta)$ in units of the de Sitter radius (arXiv:2301.04146) [src: Sect. 2.1, inline, paragraph after the list]. No paper read states the relation between the two labels.
- **Printing slips copied as printed.** Chen 2010 Eq. 4.1 lacks the square of the Planck mass; Creminelli & Zaldarriaga 2004 Eq. 1 mixes κ and k subscripts; Ullah 2026 Eq. 14 has an unbalanced parenthesis; Achúcarro et al. 2022 Sect. 4.1 prints the condition for a sharp feature with the slow-roll inequality. None has a published correction as of the snapshot. <!-- num: not a value -->

## Numerical issues
<!-- key: numerical-issues -->

- **Nested time integrals.** Feature bispectra need regularised numerical integrals; Chen, Easther & Lim give an improved regularisation (arXiv:0801.3295) [src: abstract]. Frequency-space (arXiv:2607.05327) and Laplace-space (arXiv:2608.23243) representations replace the nested integrals by series [src: abstracts]; Philcox solves strongly mixed bispectra numerically with CosmoFlow (arXiv:2607.18369) [src: abstract].
- **Binning of folded shapes.** Finite Fourier-space binning degrades folded-shape constraints once the enhanced region is narrower than the bin (Yang & Philcox 2026, arXiv:2607.15337) [src: abstract].
- **Look-elsewhere effect.** Scans over collider or feature parameters must correct for it: the Planck feature hints fall to at most $2.6σ$ global significance (arXiv:2605.30236) [src: abstract], the collider maximum is $2.35σ$ after correction (arXiv:2512.22085) [src: abstract].
- **Background cosmology.** A logarithmic feature preference at ≃ 3σ in DESI DR1 with fixed Planck cosmology disappears when cosmology is varied (arXiv:2610.10530) [src: abstract].
- **Projection effects.** The squeezed limit of single-field models is a coordinate effect; computing an observable from it needs the full projection, not the primordial bispectrum alone (Pajer et al. 2013, arXiv:1305.0824) [src: abstract].

## Referee checklist for a primordial-correlator paper
<!-- key: referee-checklist-for-a-primordial-correlator -->

1. Normalisation of the power spectrum and the variable of $f_{\rm NL}$ stated (ζ, ℛ or Φ), with sign (hub atlas).
2. Slow-roll parameters defined (Hubble-flow or potential), and the order in slow roll stated.
3. Vacuum stated; any departure from Bunch–Davies justified, and folded enhancements discussed (arXiv:0710.1302).
4. For small $c_{s}$: decoupling limit and strong-coupling scale checked (arXiv:0709.0293, Eqs. 39 and 50). <!-- num: not a value -->
5. For collider signals: weak or strong mixing stated and justified against data (arXiv:2607.18369); Boltzmann suppression not assumed when mixing is strong or masses oscillate.
6. Squeezed-limit claims distinguish primordial from projection effects (arXiv:1305.0824); single-field consistency relations used only with an attractor background.
7. Loop calculations: regularisation, counterterms, tadpoles and boundary terms included (arXiv:0912.2734, arXiv:2305.19263); claims about large-scale effects of small-scale enhancement compared with the replies (arXiv:2408.08296, arXiv:2605.04815).
8. Decoherence calculations include all environments at the order computed, scalar and tensor together (arXiv:2607.22914).
9. Template searches: overlap with standard templates, orthogonalisation, look-elsewhere correction.
10. Forecasts labelled as forecasts.

## Not verified
<!-- key: not-verified -->

- The size of the error of the factorisable equilateral template was not read beyond the abstract of arXiv:astro-ph/0509029.
- The validity range of the separate-universe decoupling argument (arXiv:2605.04815) beyond its abstract.
- Maldacena's own slow-roll definitions (arXiv:astro-ph/0210603), unreadable in the rendering.
