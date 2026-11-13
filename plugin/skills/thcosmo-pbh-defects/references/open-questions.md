# Open questions on primordial black holes and topological defects

Scope: live debates with both sides cited, unresolved calculations, what the next calculation or data will decide, and the stale claims that still circulate, each with the paper that corrects it. Open questions on the gravitational-wave spectra are in `thcosmo-cosmological-gravitational-waves`; on PBHs as dark matter in `thcosmo-dark-matter-models`; on loop corrections from PBH-scale modes in `thcosmo-primordial-correlators`.

Snapshot: 2026-11-13

## Live debates
<!-- key: live-debates -->

### Is the collapse threshold universal?
<!-- key: is-the-collapse-threshold-universal -->
- For: the threshold "is, to an excellent approximation, universal, whenever given in terms of the compaction function averaged over a sphere of radius $r_m$" (arXiv:1907.13311) [src: abstract], a property that "generalizes to all $w\gtrsim 1/3$" (arXiv:2007.05564) [src: abstract].
- Against or qualified: "there is no universal threshold for primordial black hole formation", although a well-defined criterion exists in terms of the averaged mass excess or the peak amplitude (arXiv:1809.02127) [src: abstract, inline]; for $w<1/3$ "the knowledge of the full shape of the compaction function is necessary" (arXiv:2007.05564) [src: abstract, inline]; with neighbouring peaks "the maximum curvature amplitude alone does not determine the collapse outcome" (arXiv:2609.03051) [src: abstract, inline].
- `[der]` The two sides use different variables (averaged against local peak), so the disagreement is partly one of definition.

### Which statistics turn $\mathcal P_\zeta$ into an abundance?
<!-- key: which-statistics-turn-mathcal-p-zeta-into-an -->
- Press–Schechter and peak theory agree for monochromatic spectra but "differ in the case of a broad primordial power spectrum" (arXiv:2603.23025) [src: abstract]; the PS factor 2 does not carry over from haloes to PBHs (arXiv:2509.25871) [src: abstract].
- Spiky stochastic profiles: "The results call for redoing collapse simulations to determine the collapse criterion for spiky profiles", and "convergence issues for the mass function remain" (arXiv:2510.09303) [src: abstract]. The public code pbhstat "Currently" handles only "nearly Gaussian initial conditions" (Cole & Fumagalli 2025, arXiv:2509.14326) [src: abstract].

### Can PBHs form in single-field inflation without spoiling CMB scales?
<!-- key: can-pbhs-form-in-single-field-inflation-without -->
- Against: models producing appreciable PBHs "induce nonperturbative coupling on a large scale" (arXiv:2211.03395) [src: abstract].
- For: loop corrections "are small" and "the scenario is not ruled out" (arXiv:2301.00599) [src: abstract]. The review of Escrivà, Kühnel & Tada notes that "It is, however, still under discussion whether loop corrections remain negligible when including quartic or higher couplings in a more general model" (arXiv:2211.05767) [src: Sect. II.10.4, text after Eq. II.162]. Full treatment: `thcosmo-primordial-correlators`, `deep/loop-corrections.md`.

### PBHs from slow first-order transitions
<!-- key: pbhs-from-slow-first-order-transitions -->
- Against: once gauge ambiguities are resolved, PBHs "are unlikely to be produced by these super-horizon inhomogeneities" (arXiv:2601.14412) [src: abstract].
- For: viable if slow reheating gives "an early matter-dominated era, during which even small overdensities grow and collapse" (arXiv:2605.11332) [src: abstract].
- Precision of nucleation: "reliable theoretical PBH predictions require precise nucleation dynamics within realistic extensions of the Standard Model" (arXiv:2506.15496) [src: abstract].

### Memory burden and light PBHs
<!-- key: memory-burden-and-light-pbhs -->
- The deviation from Hawking evaporation sets in "at the latest after losing half of the mass" (arXiv:2006.00011) [src: abstract], but "What happens beyond this time is currently not known" (arXiv:2402.14069) [src: abstract]; "it remains unclear how long PBHs will eventually survive" (arXiv:2211.05767) [src: Sect. V.2, fourth paragraph]. Bounds on light PBHs depend on how the crossover is modelled: "Specifying the rate-combination rule is therefore essential" (arXiv:2606.04707) [src: abstract].

### Field-theory against Nambu–Goto string loops
<!-- key: field-theory-against-nambu-goto-string-loops -->
- Field theory: network loops decay fast, "one can estimate that $f_\text{NG}<0.1$ at $95$% confidence level" (arXiv:2103.16248) [src: abstract]; Nambu–Goto: the loop densities used in GW bounds are defended in `thcosmo-cosmological-gravitational-waves` (`deep/cosmic-string-spectra.md`, Step 6). The resolution sets whether PTA and LVK bounds on $G\mu$ apply to field-theory strings.

### Global-string scaling
<!-- key: global-string-scaling -->
- "clear evidence of logarithmic violations of the scaling properties" and "the presence of small logarithmic corrections to the spectrum shape could completely alter" the axion number from strings (arXiv:1806.04677) [src: abstract]; Kim & Son find "a logarithmically growing spectral index" (arXiv:2411.08455) [src: abstract]. The extrapolation to physical $\log(m_r/H)$ remains the open step; the axion mass that follows is in `thcosmo-dark-matter-models`.

## Unresolved calculations
<!-- key: unresolved-calculations -->

- Thresholds for softer equations of state and time-dependent $w$ (QCD epoch): $\delta_{\mathrm{c,max}}=f(w)$ fails below $w=1/3$ "for which a numerical approach is required" (arXiv:2211.05767) [src: Sect. II.4, inline, text after Fig. 2]. <!-- num: not a value -->
- Matter-dominated collapse with realistic matter: thresholds differ between dust and collisionless descriptions by large factors (arXiv:2609.14218) [src: abstract].
- Collapse of PBH clusters and clustering with non-perturbative non-Gaussianity: a general bias formula exists under its stated assumptions (arXiv:2609.11306) [src: abstract].
- Delayed-decay PBHs: $\delta(t_\mathrm{H})$ as a criterion is "highly sensitive to wall structure and model details" (arXiv:2601.21878) [src: abstract].
- Monopole networks with a thermal bath: "Further work is needed to quantify the effect of the thermal bath" (arXiv:2511.14204) [src: abstract].
- Domain-wall area parameter: the initial-condition dependence is "argued to be of non-physical origin", "likely" a lattice-boundary effect (arXiv:2509.25367) [src: abstract].
- Metastable strings: the GUT relation behind $\sqrt\kappa$ "is an open question that remains to be investigated" (arXiv:2307.04691) [src: Sect. 5, third paragraph].

## What the next calculations and data decide
<!-- key: what-the-next-calculations-and-data-decide -->

- `[der]` Nonspherical three-dimensional collapse with stochastic profiles decides the threshold for spiky, clustered peaks (see arXiv:2608.13206; arXiv:2609.03051; arXiv:2510.09303).
- A gravitational-wave background at PTA or interferometer frequencies decides between stable, metastable and field-theory strings and biased walls; templates and fits are in `thcosmo-cosmological-gravitational-waves`. <!-- num: not a value -->
- High-energy cosmic rays and neutrinos probe memory-burdened PBHs below $10^{10}$ g, a window opened under that hypothesis (arXiv:2402.17823) [src: abstract].
- No forecast was read in this build.

## Stale claims and misconceptions
<!-- key: stale-claims-and-misconceptions -->

- **"Carr's Jeans-length value is the threshold."** The estimate $\delta_{\mathrm{c},\mspace{1.5mu}\rm Carr}=w$ is quoted as "the first analytical approximation" (arXiv:2211.05767) [src: Eq. II.31; Sect. II.6, inline, text before Eq. II.31]; the HYK formula "shows a much better agreement with the result of recent numerical simulations" (arXiv:1309.4201) [src: abstract, inline], and the threshold depends on the profile through $q$ (arXiv:2211.05767) [src: Sect. II.4]. <!-- num: not a value -->
- **"The curvature perturbation can be thresholded directly."** A threshold on $\zeta$ "depends significantly on environmental effects" (arXiv:1805.03946) [src: abstract]; using $\mathcal{R}_c$ "in the standard way vastly overestimates the number of PBHs" (arXiv:1405.7023) [src: abstract].
- **"Gaussian $\zeta$ means Gaussian PBH statistics."** The overdensity statistics are "unavoidably non-Gaussian" (arXiv:1904.00970) [src: abstract].
- **"The Press–Schechter factor 2 applies to PBHs as to haloes."** Not for the non-Markovian PBH case (arXiv:2509.25871) [src: abstract].
- **"All PBHs lighter than $\sim 5\times 10^{14}$ g have evaporated."** This holds only if the semiclassical description holds throughout; memory burden would lead "to the survival of black holes with mass around $M_{*}$" (arXiv:2211.05767) [src: Sect. V.2, inline, third paragraph].
- **"GUT-scale strings can explain the PTA signal."** Stable GUT-scale strings are "firmly excluded"; metastable ones can fit, as found in its Refs. [32, 37] (arXiv:2307.04691) [src: Sect. 1, text before and after Eq. 1].
- **"Nambu–Goto bounds on $G\mu$ apply to Abelian-Higgs strings."** Not robustly (arXiv:2103.16248) [src: abstract].
- **"Single-field PBH formation is ruled out by one-loop corrections."** Disputed (arXiv:2211.03395; arXiv:2301.00599) [src: abstract]; see `thcosmo-primordial-correlators`.

## Not verified
<!-- key: not-verified -->

- No forecast paper was read; the "What the next calculations and data decide" items are pointers, not forecasts.
