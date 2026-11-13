# Models of primordial-black-hole formation and of topological defects

Scope: one card per formation channel of PBHs and per class of defect network, chosen by literature weight in the reviews read (arXiv:2211.05767, arXiv:2002.12778, arXiv:0911.1345, arXiv:1703.02576, arXiv:2307.04691). The inflationary models that produce a peak in the curvature spectrum (inflection point, ultra-slow roll, hybrid, curvaton, axion inflation) are in `thcosmo-inflation`; PBHs as dark matter in `thcosmo-dark-matter-models`; the gravitational-wave spectra of each source in `thcosmo-cosmological-gravitational-waves`. <!-- num: not a value -->

Snapshot: 2026-11-13

## PBH formation channels
<!-- key: pbh-formation-channels -->

### Collapse of large curvature perturbations in radiation domination
<!-- key: collapse-of-large-curvature-perturbations-in -->
- **Defining equations:** collapse when the peak of the compaction function, which "closely resembles the gravitational Schwarzschild potential" (arXiv:2211.05767) [src: Sect. II.3, inline, text after Eq. II.17], exceeds a threshold, with $\mathcal{C}(r)\simeq f(w)K(r)r^{2}=f(w)\mspace{-1.5mu}\left(1-\big[1+\tilde{r}\zeta^{\prime}(\tilde{r})\big]^{2}\right)$ at leading order of the gradient expansion (arXiv:2211.05767) [src: Eq. II.19] and mass $M=\mathcal{K}M_{H}(t_{H})\big(\delta_{\mathrm{m}}-\delta_{\mathrm{c}}\big)^{\mspace{-2mu}\gamma}$ near threshold [src: Eq. II.30]; details in `formalism.md`.
- **Parameters:** amplitude and shape of the peak of $\mathcal{P}_\zeta$ (through $q$), the equation of state $w$ at re-entry, the statistics of $\zeta$ (Gaussian or non-Gaussian).
- **Predictions:** for radiation, Escrivà, Germani & Sheth "argued, supported by the numerical simulations", an averaged threshold "$\delta_c = 0.40$" (arXiv:1907.13311) [src: abstract]; the abundance from a narrow peak "is exponentially smaller than in the case of a broad peak" at fixed amplitude, and the density "is dominated by masses roughly equal to the cosmological horizon mass measured at horizon crossing" (arXiv:1805.04087) [src: abstract].
- **Consistency:** the nonlinear $\delta$–$\zeta$ relation makes the statistics "unavoidably non-Gaussian" (arXiv:1904.00970) [src: abstract]; the one-loop claim that PBH-producing single-field models "induce nonperturbative coupling on a large scale probed by cosmic microwave background radiation" (Kristiano & Yokoyama 2022, arXiv:2211.03395) [src: abstract]; reply: "the loop corrections to the large-scale linear power spectrum from the short modes are small", "the scenario is not ruled out" (Riotto 2023, arXiv:2301.00599) [src: abstract]. The full debate is in `thcosmo-primordial-correlators` (`deep/loop-corrections.md`).
- **Observational status:** constrained through $\beta(M)$ and $f(M)$; "all of the limits come with caveats and few can be regarded as 100 % secure" (arXiv:2002.12778) [src: Sect. I.1, fifth paragraph]; the status as dark matter is kept in `thcosmo-dark-matter-models`.
- **Status date:** 2026-11-13

### Collapse in an early matter-dominated era
<!-- key: collapse-in-an-early-matter-dominated-era -->
- **Defining equations:** for "an infinitely long phase of matter domination, the PBH formation threshold formation is zero if non-spherical effects are neglected" (as printed), and the mass function goes as $\mathrm{d}n/\mathrm{d}M\propto M^{-2}\delta_{H}(M)^{5}$, from their Ref. [348] (arXiv:2211.05767) [src: Sect. II.14, inline, paragraph "Collapse in a Matter-Dominated Era"].
- **Parameters:** duration of the dust phase ($t_1$ to $t_2$), variance at horizon entry $\sigma_h^*$, angular momentum and non-sphericity.
- **Predictions:** "$\beta\simeq A_\gamma\sigma_h^{*5}$ for $\sigma_h^*\ll 1$", and the spin "very small for $\sigma_h^*\ll 1$" (Ye et al. 2025, arXiv:2508.10070) [src: abstract, inline].
- **Consistency:** the dust description in numerical relativity "crashes" unless the singularity is hidden inside the horizon; with collisionless particles the threshold "is significantly smaller than the previous analytic estimation by an order of magnitude" (Yoo, Escrivà, Harada & Kohri 2026, arXiv:2609.14218) [src: abstract]; reply: none found.
- **Observational status:** no verdict specific to this channel found in the papers read.
- **Status date:** 2026-11-13

### Delayed vacuum decay in a first-order transition
<!-- key: delayed-vacuum-decay-in-a-first-order-transition -->
- **Defining equations:** none transcribed; the mechanism is that "the vacuum decay is postponed in a whole Hubble volume", producing overdense regions that collapse (Liu, Bian, Cai, Guo & Wang 2021, arXiv:2106.05637) [src: abstract].
- **Parameters:** transition rate and duration ($\beta/H$), vacuum energy $\Delta V$, wall structure.
- **Predictions:** a mass function that "is nearly monochromatic"; joint PBH and GW predictions (arXiv:2106.05637) [src: abstract, inline]. In simulations, baby-universe (type B) PBHs "when $t_\mathrm{H}/t_\mathrm{V} \gtrsim 1$ (critical range $\sim 1.1 - 1.6$ in our survey)" (Ning, Zeng, Cai & Wang 2026, arXiv:2601.21878) [src: abstract, inline].
- **Consistency:** "reliable theoretical PBH predictions require precise nucleation dynamics", with "an universal lower bound on the transition timescale, $\beta/H_* \simeq 5$" and viable dark-matter parameter space "severely limited" for classically conformal gauge-Higgs theories (Kierkla, Ramberg, Schicho & Schmitt 2025, arXiv:2506.15496) [src: abstract, inline]; reply: none found.
- **Observational status:** no verdict in the papers read; the transition itself is in `thcosmo-baryogenesis-phase-transitions`.
- **Status date:** 2026-11-13

### False-vacuum remnants of strongly supercooled transitions
<!-- key: false-vacuum-remnants-of-strongly-supercooled -->
- **Defining equations:** collapse estimated "using the hoop conjecture" for remnants that "scale slower with the expansion of the Universe than their surroundings" (Lewicki, Toczek & Vaskonen 2023, arXiv:2305.04924) [src: abstract].
- **Parameters:** $\beta/H$, $\Delta V$, bubble-radius distribution.
- **Predictions:** PBH formation "implies $\beta/H \gtrsim 3.8$" if "$\Delta V \lesssim (10^{12} {\rm GeV})^4$"; all the dark matter in asteroid-mass PBHs "if $\beta/H \simeq 3.8$ and $10^5 {\rm GeV} \lesssim \Delta V^{1/4} \lesssim 10^8 {\rm GeV}$" (arXiv:2305.04924) [src: abstract, inline].
- **Consistency:** for slow transitions, PBHs "are unlikely to be produced by these super-horizon inhomogeneities" once gauge ambiguities are resolved (Wang, Balázs, Ding & Tian 2026, arXiv:2601.14412) [src: abstract]; reply: the mechanism "remains viable" because reheating "can be sufficiently slow that the Universe enters an early matter-dominated era" (Ai & Xie 2026, arXiv:2605.11332) [src: abstract].
- **Observational status:** no verdict in the papers read.
- **Status date:** 2026-11-13

### Collapse of cosmic-string loops
<!-- key: collapse-of-cosmic-string-loops -->
- **Defining equations:** $\beta\sim(G\mspace{1mu}\mu)^{2\mspace{1.5mu}\ell/s-4}$, "where $2<\ell/s<4$", from their Ref. [352] (arXiv:2211.05767) [src: Sect. II.14, inline, paragraph "Collapse of Cosmic Loops"].
- **Parameters:** $G\mu$, loop length $\ell$, string-correlation scale $s$.
- **Predictions:** PBHs form "with equal probability at every epoch", so with "an extended mass spectrum" (arXiv:2211.05767) [src: Sect. II.14, paragraph "Collapse of Cosmic Loops"].
- **Consistency:** none found in the papers read.
- **Observational status:** "avoiding overproduction of PBHs requires $G\mspace{1mu}\mu<10^{-7}$" (arXiv:2211.05767) [src: Sect. II.14, inline, paragraph "Collapse of Cosmic Loops"].
- **Status date:** 2026-11-13

### Collapse of domain walls and bubbles; particle trapping
<!-- key: collapse-of-domain-walls-and-bubbles-particle -->
- **Defining equations:** none transcribed (qualitative channels in arXiv:2211.05767, Sect. II.14).
- **Parameters:** wall tension and lifetime; bubble nucleation rate per Hubble volume; Yukawa coupling and mass gap for trapping.
- **Predictions:** wall-collapse PBH masses "might span a wide range depending on the specific scenario", possibly "significantly below the horizon mass" (arXiv:2211.05767) [src: Sect. II.14, paragraph "Collapse of Domain Walls"].
- **Consistency:** bubble collisions need a rate "finely tuned, not to be much larger than the Hubble rate" nor "much less" (arXiv:2211.05767) [src: Sect. II.14, paragraph "Collapse through Bubble Collisions"].
- **Observational status:** no verdict in the papers read.
- **Status date:** 2026-11-13

## Defect networks
<!-- key: defect-networks -->

### Stable local strings in the Nambu–Goto limit
<!-- key: stable-local-strings-in-the-nambu-goto-limit -->
- **Defining equations:** $S=-\mu\int d^{2}\sigma\sqrt{-\det(g_{\mu\nu}x^{\mu}_{,a}x^{\nu}_{,b})},$ (arXiv:0911.1345) [src: Eq. 10]; scaling $\frac{\rho_{\text{str}}}{\rho}=\frac{8\pi G\mu}{3\nu^{2}}\frac{\xi^{2}}{t^{2}}=\frac{8\pi G\mu\gamma^{2}}{3\nu^{2}},$ [src: Eq. 22]; VOS and loop densities in `thcosmo-cosmological-gravitational-waves` (`deep/cosmic-string-spectra.md`).
- **Parameters:** $G\mu$; intercommutation probability $P$ (1 for field-theory strings); loop-size distribution; $\Gamma$.
- **Predictions:** scaling with $\gamma=\xi/t$ "typically of order 0.3 and 0.55" in radiation and matter (arXiv:0911.1345) [src: Sect. 4, inline, second paragraph].
- **Consistency:** in field theory, "The scaling of the string separation implies that string loops decay by the emission of massive radiation within a Hubble time" (arXiv:1703.06696) [src: abstract], and "An implication is that one cannot use the Nambu-Goto model to derive robust constraints on the tension of field theory strings" (arXiv:2103.16248) [src: abstract]; reply: the Nambu–Goto loop-density side is in `thcosmo-cosmological-gravitational-waves` (`deep/cosmic-string-spectra.md`, Step 6).
- **Observational status:** Planck 2013, "$G\mu/c^2 < 1.5 x 10^{-7}$" at 95% for the Nambu–Goto model (arXiv:1303.5085) [src: abstract, inline]; GUT-scale tensions "$G\mu\simeq 10^{-(8\cdots 6)}$ are firmly excluded" by PTA results for stable strings, as stated by Buchmuller, Domcke & Schmitz (arXiv:2307.04691) [src: Sect. 1, inline, first paragraph]. Current limits: cosmoskill `cosmo-early-universe-exotica`.
- **Status date:** 2026-11-13

### Abelian-Higgs (field-theory) strings
<!-- key: abelian-higgs-field-theory-strings -->
- **Defining equations:** $L=D_{\mu}\phi^{*}D^{\mu}\phi-\tfrac{1}{4}F_{\mu\nu}F^{\mu\nu}-V(\phi).$ (arXiv:0911.1345) [src: Eq. 1], $\mu=F(\beta)\eta^{2},$ [src: Eq. 5].
- **Parameters:** $\eta$, the coupling ratio $\beta$ of Eq. 6 of arXiv:0911.1345; fraction $f_\text{NG}$ of Nambu–Goto-like loops.
- **Predictions:** scaling maintained by "classical radiation of the scalar and gauge fields" (arXiv:1703.06696) [src: abstract]; "one can estimate that $f_\text{NG}<0.1$ at $95$% confidence level" for network loops (arXiv:2103.16248) [src: abstract].
- **Consistency:** the decay mechanism "is non-linear, can only be suppressed by careful tuning of initial conditions, and is much stronger than gravitational radiation" ("We argue") (arXiv:2103.16248) [src: abstract]; reply: see `thcosmo-cosmological-gravitational-waves` for the Nambu–Goto side.
- **Observational status:** Planck 2013, "$G\mu_{AH}/c^2 < 3.2 x 10^{-7}$" (arXiv:1303.5085) [src: abstract, inline].
- **Status date:** 2026-11-13

### Metastable strings (monopole–string systems)
<!-- key: metastable-strings-monopole-string-systems -->
- **Defining equations:** $\Gamma_{d}=\frac{\mu}{2\pi}\exp\left(-\pi\kappa\right)\qquad\text{with}\qquad\kappa=\frac{m_{M}^{2}}{\mu}$ (arXiv:2307.04691) [src: Eq. 1], in the semiclassical approximation.
- **Parameters:** $G\mu$, $\sqrt\kappa$; the symmetry-breaking chain (for example $\text{SU}(2)_{R}\times\text{U}(1)_{B-L}\to\text{U}(1)_{Y}$ embedded in SO(10)) (arXiv:2307.04691) [src: Sect. 1, last paragraph]. <!-- num: not a value --> <!-- eq: notation -->
- **Predictions:** as summarised from its Refs. [43, 44, 45], for "$\sqrt{\kappa}\sim 8$" the network "survives for about an hour (redshift $z\sim 10^{7}$) until monopole production becomes efficient", giving a GW spectrum like stable strings at high frequencies and "strongly suppressed" at low frequencies (arXiv:2307.04691) [src: Sect. 1, text after Eq. 1].
- **Consistency:** "in all $\text{SO}(10)$ models the precise connection between GUT masses and couplings and the monopole-mass–string-tension ratio $\sqrt{\kappa}$ is an open question" (arXiv:2307.04691) [src: Sect. 5, third paragraph]; requires inflation between the two breakings [src: Sect. 5, second paragraph].
- **Observational status:** metastable strings "can not only provide a good fit to the PTA signal for GUT-scale string tensions", as found in its Refs. [32, 37], but also evade PTA bounds while giving a signal at higher frequencies (arXiv:2307.04691) [src: Sect. 1, text after Eq. 1]; fits in `thcosmo-cosmological-gravitational-waves`.
- **Status date:** 2026-11-13

### Cosmic superstrings (F-, D- and (p,q)-strings)
<!-- key: cosmic-superstrings-f-d-and-p-q-strings -->
- **Defining equations:** none transcribed; reconnection probability "of order $g^{2}_{s}$" for fundamental strings (Polchinski 1988, as quoted in arXiv:0911.1345) [src: Sect. 9.1, first paragraph].
- **Parameters:** $g_s$, compactification, tensions of the bound states.
- **Predictions:** "$0.1\lesssim P\lesssim 1$" for D-strings and "$10^{-3}\lesssim P\lesssim 1$" for F-strings, from Jackson et al. (2005) (arXiv:0911.1345) [src: Sect. 9.1, second paragraph]; "in most cases these strings can be distinguished from cosmic strings that arise as gauge theory solitons" (Jackson et al., arXiv:hep-th/0405229) [src: abstract].
- **Consistency:** how $\rho_{\rm str}$ scales with $P$ "is a matter of some debate" ($P^{-1}$ against $P^{-0.6}$ below $P=0.1$) (arXiv:0911.1345) [src: Sect. 9.1, third paragraph]. <!-- num: not a value -->
- **Observational status:** no dedicated verdict read; constraints through the same GW and CMB channels.
- **Status date:** 2026-11-13

### Global and axion strings
<!-- key: global-and-axion-strings -->
- **Defining equations:** none transcribed here; global strings arise "in theories with no gauge field" (arXiv:0911.1345) [src: Sect. 2, text after Eq. 8].
- **Parameters:** symmetry-breaking scale; the logarithm of the ratio of Hubble to core scale.
- **Predictions:** an attractor with "logarithmic violations of the scaling properties" (arXiv:1806.04677) [src: abstract].
- **Consistency:** how the attractor extrapolates to physical parameters sets the axion abundance; "a detailed understanding of the evolution of the axion spectrum is therefore crucial" (arXiv:1806.04677) [src: abstract].
- **Observational status:** through the axion dark-matter mass, kept in `thcosmo-dark-matter-models`.
- **Status date:** 2026-11-13

### Domain walls from discrete symmetries ($Z_2$, $Z_N$), with bias
<!-- key: domain-walls-from-discrete-symmetries-z2-zn -->
- **Defining equations:** $V(\phi)=\frac{\lambda}{4}\left(\phi^{2}-v^{2}\right)^{2}$ (arXiv:1703.02576) [src: Eq. 2.2] plus the bias $\Delta V(\phi)=\epsilon v\phi\left(\frac{1}{3}\phi^{2}-v^{2}\right),$ [src: Eq. 2.23].
- **Parameters:** $\sigma$, $V_{\rm bias}$ (or a population bias $\mathcal{B}_s$), $\mathcal{A}$, $C_{\rm ann}$.
- **Predictions:** scaling $\rho_{\rm wall}(t)=\mathcal{A}\frac{\sigma}{t},$ [src: Eq. 2.17]; annihilation at $t_{\rm ann}\propto\mathcal{A}\sigma/V_{\rm bias}$ as in Eq. 2.27 (`formalism.md`); for a population bias "$T_\text{ann}\sim T_s\,\mathcal{B}_s^{0.8}$" (arXiv:2607.18107) [src: abstract].
- **Consistency:** stable walls with "$\sigma^{1/3}\lesssim\mathcal{O}(\mathrm{MeV})$" violated "must not exist in the universe at the present time" (Zel'dovich–Kobzarev–Okun) (arXiv:1703.02576) [src: Sect. 2.2, text after Eq. 2.22]; the area parameter depends on initial conditions on the lattice, argued to be non-physical (arXiv:2509.25367) [src: abstract].
- **Observational status:** "recent results of pulser timing arrays and direct detection experiments partially exclude the relevant parameter space" (as printed, 2017) (arXiv:1703.02576) [src: abstract]; current GW status in `thcosmo-cosmological-gravitational-waves`.
- **Status date:** 2026-11-13

### GUT monopoles
<!-- key: gut-monopoles -->
- **Defining equations:** none transcribed; monopoles exist if $\pi_{2}(\mathcal{M})\neq\mathbf{1}$ (arXiv:0911.1345) [src: Sect. 2, text after Eq. 8].
- **Parameters:** monopole mass; formation after or before inflation.
- **Predictions:** with plasma interactions neglected, the density fraction stays constant in radiation and "decreases logarithmically" in matter (arXiv:2511.14204) [src: abstract].
- **Consistency:** analytic estimates allow standard cosmology "only if their mass is less than $10^{11}$ GeV" (arXiv:2511.14204) [src: abstract]; inflation after GUT breaking is the usual remedy, and if inflation comes first "the problem persists" (Hamada & Yamatsu 2026, arXiv:2606.12874) [src: abstract].
- **Observational status:** no measured bound read in this build.
- **Status date:** 2026-11-13
