# Open questions on primordial black holes and topological defects

Scope: live debates with both sides cited, unresolved calculations, what the next calculation or data will decide, and the stale claims that still circulate, each with the paper that corrects it. Open questions on the gravitational-wave spectra are in `thcosmo-cosmological-gravitational-waves`; on PBHs as dark matter in `thcosmo-dark-matter-models`; on loop corrections from PBH-scale modes in `thcosmo-primordial-correlators`.

Snapshot: 2026-11-13

## Live debates
<!-- key: live-debates -->

### Is the collapse threshold universal?
<!-- key: is-the-collapse-threshold-universal -->
- For: the threshold "from an initial spherically symmetric perturbation is, to an excellent approximation, universal, whenever given in terms of the compaction function averaged over a sphere of radius $r_m$" (arXiv:1907.13311) [src: abstract]; the dependence of $\delta_c$ only "upon the curvature of the compaction function around its peak value", shown for radiation, "generalizes to all $w\gtrsim 1/3$" (arXiv:2007.05564) [src: abstract].
- Against or qualified: "there is no universal threshold for primordial black hole formation", although a well-defined criterion exists in terms of the averaged mass excess or the peak amplitude (arXiv:1809.02127) [src: abstract, inline]; for $w<1/3$ "the knowledge of the full shape of the compaction function is necessary" (arXiv:2007.05564) [src: abstract, inline]; with neighbouring peaks "the maximum curvature amplitude alone does not determine the collapse outcome" (arXiv:2609.03051) [src: abstract, inline].
- `[der]` The two sides use different variables (averaged against local peak), so the disagreement is partly one of definition.

### Which statistics turn $\mathcal P_\zeta$ into an abundance?
<!-- key: which-statistics-turn-mathcal-p-zeta-into-an -->
- Press–Schechter and peak theory agree for monochromatic spectra but "differ in the case of a broad primordial power spectrum" (arXiv:2603.23025) [src: abstract]; the PS factor 2 does not carry over from haloes to PBHs (arXiv:2509.25871) [src: abstract].
- Spiky stochastic profiles: "The results call for redoing collapse simulations to determine the collapse criterion for spiky profiles", and "convergence issues for the mass function remain" (arXiv:2510.09303) [src: abstract]. The public code pbhstat "Currently" handles only "nearly Gaussian initial conditions" (Cole & Fumagalli 2025, arXiv:2509.14326) [src: abstract].

### Can PBHs form in single-field inflation without spoiling CMB scales?
<!-- key: can-pbhs-form-in-single-field-inflation-without -->
- Against: "in a model with sharp transition of the second slow-roll parameter", "models producing an appreciable amount of primordial black holes induce nonperturbative coupling on a large scale" (arXiv:2211.03395) [src: abstract].
- For: "Based on general arguments", loop corrections "are small" and "the scenario is not ruled out" (arXiv:2301.00599) [src: abstract]. The review of Escrivà, Kühnel & Tada notes that "It is, however, still under discussion whether loop corrections remain negligible when including quartic or higher couplings in a more general model" (arXiv:2211.05767) [src: Sect. II.10.4, text after Eq. II.162]. Full treatment: `thcosmo-primordial-correlators`, `deep/loop-corrections.md`.

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
- "clear evidence of logarithmic violations of the scaling properties" and "the presence of small logarithmic corrections to the spectrum shape could completely alter" the conclusion that the extrapolated spectrum gives "a negligible number density of relic axions from strings" (arXiv:1806.04677) [src: abstract]; Kim & Son find "a logarithmically growing spectral index" (arXiv:2411.08455) [src: abstract]. The extrapolation to physical $\log(m_r/H)$ remains the open step; the axion mass that follows is in `thcosmo-dark-matter-models`.
- Against a genuine logarithmic growth: the apparent corrections to $\zeta$ "are artefacts of the initial conditions, rather than a property of the scaling network" (arXiv:1908.03522) [src: abstract]; runs far from the fixed point are "accounted for by a VOS model" with a constant asymptote (arXiv:2102.07723) [src: abstract]; at $16384$ points per side, "the growth tends to slow down" as the fixed point is approached, read as "a transient" (arXiv:2410.18064) [src: abstract]. Reply from the other side: the 2020 analysis again finds "Clear evidence of scaling violations" (arXiv:2007.04990) [src: abstract].
- Further systematics: the string density "is sensitive to" the tension ratio (arXiv:1912.08058) [src: abstract]; friction with the bath "delays the onset of scaling" in DFSZ-like models (arXiv:2603.00237) [src: abstract].

### Monopole networks: Coulomb modelling and global monopoles
<!-- key: monopole-networks-coulomb-modelling-and-global -->

- The index $\alpha$ of the Coulomb term in monopole one-scale models "is the subject of some disagreement" between Martins & Achúcarro and Sousa & Avelino (Refs. [27, 28] of arXiv:2511.14204) [src: Sect. II.1, inline, text after Eq. 9]; simulations without plasma interactions are "consistent with there being no modification" but "cannot constrain the index of the power law well" (arXiv:2511.14204) [src: Sect. I, eleventh and twelfth paragraphs].
- Global monopoles: their density fraction was described as dropping "inversely with scale factor", from the simulations of its Refs. [31, 32] (arXiv:2511.14204) [src: Sect. I, eighth paragraph]; Nakano & Yin find instead "a logarithmic-like evolution" and conclude that "analytic studies based on the assumption of constant scaling should be revisited" (arXiv:2607.05517) [src: abstract]. Reply: none found.

### Are PBHs born clustered beyond Poisson?
<!-- key: are-pbhs-born-clustered-beyond-poisson -->

- Clustered: "With minimal assumptions, we show that PBHs created in the radiation era are highly clustered" (Chisholm 2005, arXiv:astro-ph/0509141) [src: abstract].
- Poisson on small scales: "we do not expect clustering on very small scales beyond what is expected from a random, Poisson distribution", for PBHs from "the gravitational collapse of large density fluctuations" (arXiv:1805.05912) [src: abstract]; the earlier conclusion came from extrapolating the large-separation formula "to $r\rightarrow 0$" (arXiv:1805.05912) [src: Sect. III, inline, fourth paragraph after Eq. 18].
- Qualified: Desjacques & Riotto "emphasized that, while the zero-lag correlation includes a Poissonian self-pair contribution, this does not mean that PBHs are necessarily Poisson distributed at small scales. Therefore, we also disagree with some of the arguments presented in [20]" (Ali-Haïmoud 2018), while for a narrow feature clustering is "not relevant" (arXiv:1806.10414) [src: Sect. V; References, Ref. 20].
- Beyond Gaussian statistics: super-Hubble clustering needs a local trispectrum (arXiv:1906.04958) [src: abstract]; with exponential tails "the clustering would then exceed the Poissonian prediction" (arXiv:2610.28723) [src: abstract]. The general bias formula for arbitrary local non-Gaussianity is in arXiv:2609.11306 [src: abstract].

### How large is the PBH spin at formation?
<!-- key: how-large-is-the-pbh-spin-at-formation -->

- First order: the spin "is a first-order effect in perturbation theory", from tidal torques and asphericity (arXiv:1903.01179) [src: abstract].
- Second order: "the spin also vanishes at first order in $ζ_{\rm rms}$, suggesting the dimensionless spin parameter $a_{\rm rms} \sim ζ_{\rm rms}^2$" (arXiv:1901.05963) [src: abstract, inline]. De Luca et al. reply, of their Ref. [29] (Mirbabayi et al.), that the second-order result "is a consequence of the choice of a Lagrangian sphere to describe the collapsing object", and that "When the ellipsoidal shape of the density profile around the peaks is taken into account, the spin can grow at first order for generic power spectra" (arXiv:1903.01179) [src: Sect. 9, fifth paragraph; References, Ref. 29]; the two "coincide" "as far as the percent level of PBH spin is concerned" and agree that the spin "should vanish in the limit of very narrow power spectra, even though for a different reason" [src: Sect. 9, fifth paragraph].
- Harada et al. find that "the first-order effect can be numerically comparable to the second-order one" (arXiv:2011.00710) [src: abstract].
- Matter era: near-extremal spins if the era "lasts sufficiently long" (arXiv:1707.03595) [src: abstract]; against: "in contrast to the previous estimates, the PBH spin is very small for $σ_h^*\ll 1$ but could be larger for larger $σ_h^*$ and broader power spectra" (Ye et al. 2025, arXiv:2508.10070) [src: abstract, inline]; in 3+1 simulations accretion of non-rotating matter lowers the spin, and "Unless the matter era is short, we argue that the final dimensionless spin will be negligible" (arXiv:2306.11810) [src: abstract].

## Unresolved calculations
<!-- key: unresolved-calculations -->

- Thresholds for softer equations of state and time-dependent $w$ (QCD epoch): $\delta_{\mathrm{c,max}}=f(w)$ fails below $w=1/3$ "for which a numerical approach is required" (arXiv:2211.05767) [src: Sect. II.4, inline, text after Fig. 2]. <!-- num: not a value -->
- Matter-dominated collapse: with dust the computation "crashes" unless the singularity "is hidden well inside the apparent horizon", while with collisionless particles "the threshold of black hole formation is significantly smaller than the previous analytic estimation by an order of magnitude" (arXiv:2609.14218) [src: abstract].
- Collapse of PBH clusters and clustering with non-perturbative non-Gaussianity: a general bias formula exists under its stated assumptions (arXiv:2609.11306) [src: abstract].
- Delayed-decay PBHs: $\delta(t_\mathrm{H})$ as a criterion is "highly sensitive to wall structure and model details" (arXiv:2601.21878) [src: abstract].
- Monopole networks with a thermal bath: "Further work is needed to quantify the effect of the thermal bath" (arXiv:2511.14204) [src: abstract].
- Domain-wall area parameter: the initial-condition dependence is "argued to be of non-physical origin", "likely" a lattice-boundary effect (arXiv:2509.25367) [src: abstract].
- Metastable strings: the GUT relation behind $\sqrt\kappa$ "is an open question that remains to be investigated" (arXiv:2307.04691) [src: Sect. 5, third paragraph].

## What the next calculations and data decide
<!-- key: what-the-next-calculations-and-data-decide -->

- `[der]` Nonspherical three-dimensional collapse with stochastic profiles decides the threshold for spiky, clustered peaks (see arXiv:2608.13206; arXiv:2609.03051; arXiv:2510.09303).
- A gravitational-wave background at PTA or interferometer frequencies decides between stable, metastable and field-theory strings and biased walls; templates and fits are in `thcosmo-cosmological-gravitational-waves`. <!-- num: not a value -->
- For light PBHs surviving under memory burden, "the fact that these black holes emit energetic quanta motivates the possibility of high-energy cosmic-ray searches" (arXiv:2211.05767) [src: Sect. V.2, fifth paragraph]; the window "below $10^{10}\,\rm{g}$" is opened under that hypothesis (arXiv:2402.17823) [src: abstract].
- No forecast was read in this build.

## Stale claims and misconceptions
<!-- key: stale-claims-and-misconceptions -->

- **"Carr's Jeans-length value is the threshold."** The estimate $\delta_{\mathrm{c},\mspace{1.5mu}\rm Carr}=w$ is quoted as "the first analytical approximation" (arXiv:2211.05767) [src: Eq. II.31; Sect. II.6, inline, text before Eq. II.31]; the HYK formula "shows a much better agreement with the result of recent numerical simulations" (arXiv:1309.4201) [src: abstract, inline], and the threshold depends on the profile through $q$ (arXiv:2211.05767) [src: Sect. II.4]. <!-- num: not a value -->
- **"The curvature perturbation can be thresholded directly."** A threshold on $\zeta$ "depends significantly on environmental effects" (arXiv:1805.03946) [src: abstract]; using $\mathcal{R}_c$ "in the standard way vastly overestimates the number of PBHs" (arXiv:1405.7023) [src: abstract].
- **"Gaussian $\zeta$ means Gaussian PBH statistics."** The overdensity statistics are "unavoidably non-Gaussian" (arXiv:1904.00970) [src: abstract].
- **"The Press–Schechter factor 2 applies to PBHs as to haloes."** Not for the non-Markovian PBH case (arXiv:2509.25871) [src: abstract].
- **"All PBHs lighter than $\sim 5\times 10^{14}$ g have evaporated."** This holds only if the semiclassical description holds throughout; memory burden would lead "to the survival of black holes with mass around $M_{*}$" (arXiv:2211.05767) [src: Sect. V.2, inline, third paragraph].
- **"GUT-scale strings can explain the PTA signal."** Stable GUT-scale strings are "firmly excluded"; metastable ones can fit, as found in its Refs. [32, 37] (arXiv:2307.04691) [src: Sect. 1, fourth paragraph; Sect. 1, text after Eq. 1].
- **"Nambu–Goto bounds on $G\mu$ apply to Abelian-Higgs strings."** Not robustly (arXiv:2103.16248) [src: abstract].
- **"Single-field PBH formation is ruled out by one-loop corrections."** Disputed (arXiv:2211.03395; arXiv:2301.00599) [src: abstract]; see `thcosmo-primordial-correlators`.
- **"PBHs are born in clusters."** Not for PBHs formed from "the gravitational collapse of large density fluctuations", by the general argument of arXiv:1805.05912 [src: abstract]; in its Gaussian illustration, the large-separation correlation was "extrapolated to $r\rightarrow 0$", "where it does not hold" (arXiv:1805.05912) [src: Sect. III, inline, fourth paragraph after Eq. 18]; the clustering length of a narrow feature is "significantly smaller than the mean comoving PBH separation" in the estimates of arXiv:1806.10414 [src: Sect. V].
- **"PBHs from radiation-era collapse can be highly spinning."** For horizon-size collapse of density perturbations, PBHs "are known to have very small spins" (arXiv:2106.03237) [src: abstract]; typical first-order values "are at the percent level" (arXiv:1903.01179) [src: abstract]. `[der]` The large spins in the papers read come from other channels (a long matter era, accretion, assembly of matter-like objects, confinement), listed in `results.md#initial-clustering-and-spin`.
- **"Debye shielding bounds the cosmological monopole abundance."** "Debye shielding cannot be employed to constrain the cosmological abundance of magnetic monopoles, contrary to what is stated in the previous literature" (arXiv:2404.04926) [src: abstract].
- **"Only inflation solves the monopole problem."** "Theories of inflation eliminate this problem by diluting the cosmological energy density of monopoles into insignificance", but for monopoles produced after inflation the proposals listed include "an intermediate phase of electromagnetic symmetry-breaking" and "monopole dissociation on domain walls" (arXiv:2511.14204) [src: Sect. I, fourth paragraph]; a Langacker–Pi realisation in an SU(5) GUT broken to a special subgroup is proposed in arXiv:2606.12874 [src: abstract].

## Not verified
<!-- key: not-verified -->

- No forecast paper was read; the "What the next calculations and data decide" items are pointers, not forecasts.
