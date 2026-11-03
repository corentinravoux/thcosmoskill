# Models of dark matter

Scope: the dark-matter candidate landscape, one card per candidate class, chosen by literature weight; production formalism in `formalism.md`, model-independent results in `results.md`.

Snapshot: 2026-11-03

The cards are chosen by the weight of each class in the TASI lectures of Safdi (arXiv:2303.02169), the review of Arbey and Mahmoudi (arXiv:2104.11488) and the Snowmass 2021 report on cosmic probes of dark matter (arXiv:2209.08215). Laboratory and indirect searches are out of the scope of this skill; an observational status that rests on them is given in one line with its paper, and the measured limits themselves belong to cosmoskill (`cosmo-neutrinos-dark-matter`).

## Thermal relics
<!-- key: thermal-relics -->

### Thermal WIMP (freeze-out of self-annihilating dark matter)
<!-- key: thermal-wimp-freeze-out-of-self-annihilating -->
- **Defining equations:** $\begin{split}{dn_{\chi}\over dt}+3Hn_{\chi}=-\langle\sigma v\rangle(n_{\chi}^{2}-n_{\rm eq}^{2})\,,\end{split}$ (arXiv:2303.02169) [src: Eq. 16].
- **Parameters:** mass $m_{\chi}$, annihilation cross-section and its velocity dependence (s-wave or p-wave), final states.
- **Predictions:** for masses above 10 GeV the required cross-section is 2.2*10^-26 cm^3s^-1 "with feeble mass-dependence" (Steigman et al., arXiv:1204.3622) [src: abstract]. In the higgsino benchmark, a Dirac SU(2) doublet, the correct abundance is reached for "$m_{\chi}=1.08\pm 0.02$ TeV" (arXiv:2303.02169) [src: Sect. 4.2]; the minimal higgsino is excluded by direct detection "by more than 5 orders of magnitude" unless a Majorana mass splitting "$\delta\gtrsim 200$ keV" makes the Z-exchange scattering inelastic [src: Sect. 4.2].
- **Consistency:** perturbative unitarity bounds the mass of a point-like thermal relic, at 140 TeV (self-conjugate) and below 100 TeV (non-self-conjugate) once bound states and Sommerfeld enhancement are included (Smirnov & Beacom, arXiv:1904.11503) [src: abstract]; reply: other freeze-out processes evade it, up to the Planck scale (arXiv:2207.01635) [src: abstract].
- **Observational status:** for the $b\bar{b}$ channel, Fermi-LAT Galactic-Centre limits "rule out the thermal relic cross section up to approximately 300 GeV" (Abazajian et al. 2020, arXiv:2003.10416) [src: abstract]; Safdi's 2023 lectures hold that "WIMP DM remains a well-motivated paradigm" and that next-generation indirect searches "will discover or rule out" the higgsino (arXiv:2303.02169) [src: Sect. 1.1]. Current limits: cosmoskill `cosmo-neutrinos-dark-matter`.
- **Status date:** 2026-11-03

### FIMP (freeze-in)
<!-- key: fimp-freeze-in -->
- **Defining equations:** $\frac{{\rm d}n_{\chi}}{{\rm d}t}+3\,H\,n_{\chi}=2\,\Gamma_{\sigma\to\chi\chi}\frac{K_{1}(m_{\sigma}/T)}{K_{2}(m_{\sigma}/T)}n_{\sigma}^{\rm eq}\,,$ (arXiv:1706.07442) [src: Eq. 7]; more in `formalism.md`, section "Freeze-in".
- **Parameters:** feeble coupling y (or a non-renormalisable operator scale for ultraviolet freeze-in, arXiv:1410.6157), masses of the dark matter and of the parent bath particle, and, for ultraviolet or Boltzmann-suppressed freeze-in, the reheating temperature.
- **Predictions:** coupling $y\simeq 10^{-12}$ for decays, Eq. 10 of arXiv:1706.07442 [src: Eq. 10], and $\zeta\simeq 10^{-11}$ for 2 → 2 scattering (arXiv:1706.07442) [src: Eq. 12], both scaled to $\Omega_{\chi}h^{2}=0.12$; the IR yield "is independent of unknown UV physics, such as the reheat temperature after inflation" (arXiv:0911.1120) [src: abstract]. Signals proposed by Hall et al. include metastable coloured or charged particles at the LHC and altered BBN [src: abstract].
- **Consistency:** gravitational production is a background that "mars" the predictivity of non-thermal models; a low reheating temperature dilutes it (Cosme et al., arXiv:2306.13061) [src: abstract]; reply: none needed — this motivates freeze-in at stronger coupling, below.
- **Observational status:** feeble couplings make the minimal scenario hard to test; with $T_R$ below the dark-matter mass the production is Boltzmann-suppressed, the coupling has to be larger, and "direct DM detection experiments already probe such freeze-in models, excluding significant parts of parameter space" (arXiv:2306.13061) [src: abstract]. For fermionic Higgs-portal freeze-in at stronger coupling, the Lyman-α constraint "excludes DM masses below about $100 -180\,\mathrm{keV}$, depending on the reheating history", and the momentum distribution "is not captured by the common $αβγ$-parametrization" (Feiteira & Oliveira 2026, arXiv:2606.20815) [src: abstract]. During a non-adiabatic matter-dominated reheating the coupling must be enhanced, yet a 2026 study finds detectable direct-detection signals "only under low reheating and low inflationary vacuum energy", with the model becoming non-perturbative near the exclusion limits (arXiv:2610.29543) [src: abstract].
- **Status date:** 2026-11-03

## Wave-like and coherent-field dark matter
<!-- key: wave-like-and-coherent-field-dark-matter -->

### QCD axion (misalignment and strings)
<!-- key: qcd-axion-misalignment-and-strings -->
- **Defining equations:** $\begin{split}\ddot{a}+3H\dot{a}-{1\over R^{2}}\nabla^{2}a+{\partial V(a,T)\over\partial a}=0\,,\end{split}$ (arXiv:2303.02169) [src: Eq. 60], with the temperature-dependent mass of Eq. 61 (`formalism.md`, section "Misalignment").
- **Parameters:** decay constant $f_{a}$ (with $m_{a}f_{a}\approx 75$ MeV fixed, arXiv:2303.02169 [src: Sect. 6.4.1, inline]), initial angle $\theta_{i}$ (pre-inflationary case only), domain-wall number N, Hubble rate during inflation for isocurvature.
- **Predictions:** pre-inflationary PQ breaking: $\begin{split}\Omega_{a}h^{2}\sim 0.1\theta_{i}^{2}\left({f_{a}\over 3\times 10^{11}\,\,{\rm GeV}}\right)^{1+{1\over n+2}}\sim 0.1\theta_{i}^{2}\left({f_{a}\over 3\times 10^{11}\,\,{\rm GeV}}\right)^{1.1}\,.\end{split}$, i.e. a mass "around 10 to 20 μeV" for θ_i of order unity (arXiv:2303.02169) [src: Eq. 72 and text after]. Post-inflationary breaking predicts one mass, but the computations disagree (`open-questions.md`): "(40,180) microelectronvolts" from adaptive-mesh simulations (Buschmann et al. 2021, arXiv:2108.05368) [src: abstract]; "$m_a \approx 95$-$450\,μ\mathrm{eV}$" from static lattices up to $11264^3$ (Saikawa et al. 2024, arXiv:2401.17253) [src: abstract]; "17.46(84) μeV" in a minimal scaling model on $12\,288^3$ grids (Correia et al. 2026, arXiv:2609.20801) [src: abstract].
- **Consistency:** N > 1 post-inflationary models suffer a domain-wall problem (arXiv:2303.02169) [src: Sect. 6.4.2]; reply: Gorghetto et al. find "a region of phenomenologically viable parameter space" with additional PQ-violating operators (arXiv:2608.27553) [src: abstract]. Large isocurvature constrains the pre-inflationary case with high-scale inflation (arXiv:2303.02169) [src: Sect. 6.4.1].
- **Observational status:** in 2023 "the vast majority of the axion's parameter space remains open", with small slivers excluded by ADMX (arXiv:2303.02169) [src: Sect. 1.1]. Haloscope limits: cosmoskill `cosmo-neutrinos-dark-matter`.
- **Status date:** 2026-11-03

### Ultralight (fuzzy) dark matter
<!-- key: ultralight-fuzzy-dark-matter -->
- **Defining equations:** a minimally coupled scalar, $\Box\phi=m^{2}\phi\,,$ (arXiv:astro-ph/0003365) [src: Eq. 1]; linear suppression $T_{\rm F}(k)\approx{\cos x^{3}\over 1+x^{8}}$ [src: Eq. 8] (`formalism.md`).
- **Parameters:** the mass m, quoted as $m_{22}$ in units of $10^{-22}$ eV; the fraction of dark matter; extensions in the 2025 review are "higher spin, self-coupled, multiple field, and mixed models" (arXiv:2507.00705) [src: abstract].
- **Predictions:** halo cores and a sharp cut-off of small-scale linear power for m ∼ $10^{-22}$ eV (arXiv:astro-ph/0003365) [src: abstract]; the review covers the range $10^{-24} \, \mathrm{eV} \lesssim m \lesssim 10^{-18} \, \mathrm{eV}$ (arXiv:2507.00705) [src: abstract].
- **Consistency:** the constraint from stellar heating in ultra-faint dwarfs assumes a diffusion approximation "valid only when the de Broglie wavelength is much smaller than the galaxy's half-light radius"; at low masses tidal heating dominates, and a reduced soliton or a stripped halo can suppress heating, so "the structure and environment of the FDM halo must be carefully considered" (Liu & Li 2026, arXiv:2604.26393) [src: abstract]; reply: May, Dalal and Kravtsov find the perturbative bounds "indeed conservative" against Schrödinger–Poisson simulations and unaffected by tidal stripping for satellites like Segue 1 (arXiv:2509.02781) [src: abstract].
- **Observational status:** as all the dark matter, the canonical range $10^{-22}$–$10^{-21}$ eV is strongly disfavoured: Lyman-α forest, "a 95% lower limit $m_\text{a} > 2 \times 10^{-20}\,\text{eV}$", ">99.7% credibility" against the canonical range (Rogers & Peiris, arXiv:2007.12705) [src: abstract, inline]; ultra-faint dwarf kinematics, $m > 3 \times 10^{-19}$ eV, strengthened to $m > 8 \times 10^{-18}$ eV at 95% confidence "if the recently discovered system Ursa Major III/UNIONS I is a galaxy" (arXiv:2509.02781) [src: abstract, inline]. For ALPs as all the dark matter, combining isocurvature, superradiance and free streaming gives $m_a \gtrsim 10^{-17}$ eV "for most cases considered" (Chathirathas & Schwetz, arXiv:2511.15790) [src: abstract, inline].
- **Status date:** 2026-11-03

## Warm and non-cold relics
<!-- key: warm-and-non-cold-relics -->

### Thermal-relic warm dark matter (benchmark)
<!-- key: thermal-relic-warm-dark-matter-benchmark -->
- **Defining equations:** $T(k)=[1+(\alpha k)^{2\nu}]^{-5/\nu}$ with α of Eq. 7 (Viel et al., arXiv:astro-ph/0501562) [src: Eqs. 6–7]; temperature from Eq. 1 [src: Eq. 1].
- **Parameters:** mass $m_{x}$ (or $m_{\rm th}$) of a relic that decoupled while relativistic; $T_{x}/T_{\nu}$ fixed by the density.
- **Predictions:** a step-like suppression of power below the free-streaming scale, which with a cold component present is only partial (arXiv:astro-ph/0501562) [src: Sect. II]. The benchmark is a parametrisation onto which other models are mapped (sterile neutrinos, Eq. 5; Shi–Fuller, arXiv:2507.18752).
- **Consistency:** the mapping fails for non-thermal momentum distributions (arXiv:2606.20815; arXiv:2507.00705) [src: abstract; Sect. V.2, Fig. 4 caption].
- **Observational status:** high-redshift Lyman-α forest, lower limit "of $5.7\;\mathrm{keV}$ (at 95\% C.L.)", lowered to 4.1 keV when restricted to $k_{\rm max}<0.1$ km⁻¹ s and earlier thermal-history priors (Iršič et al., arXiv:2309.04533) [src: abstract]; an early WMAP + Lyman-α limit was $m_{\rm wdm}>550$ eV at 2σ (Viel et al. 2005, arXiv:astro-ph/0501562) [src: abstract]. Current combined limits: cosmoskill `cosmo-neutrinos-dark-matter` and `cosmo-lyman-alpha`.
- **Status date:** 2026-11-03

### Sterile-neutrino dark matter
<!-- key: sterile-neutrino-dark-matter -->
- **Defining equations:** a right-handed neutrino with Dirac mass μ and Majorana mass M; for $M\gg\mu$ the number density is "proportional to $μ^2/M$ so that the energy density today is independent of M" (Dodelson & Widrow 1993, arXiv:hep-ph/9303287) [src: abstract]. Mass map to the thermal benchmark: Eq. 5 of arXiv:astro-ph/0501562 [src: Eq. 5].
- **Parameters:** mass $m_{s}$, active–sterile mixing $\sin^{2}(2\theta)$, and for resonant production the lepton asymmetry L. <!-- num: not a value -->
- **Predictions:** non-resonant (Dodelson–Widrow) production by oscillations can give hot, warm or cold dark matter, warm for "$M\simeq 0.1-1.0 {\rm ~keV}$" in the 1993 paper (arXiv:hep-ph/9303287) [src: abstract, inline]. Resonant (Shi–Fuller) MSW production with lepton asymmetries "from 10$^{-3}$ to 10$^{-1}$ of the photon number" gives a non-thermal, colder spectrum (arXiv:astro-ph/9810076) [src: abstract, inline]. Radiative decay gives an X-ray line; Abazajian's review discusses "recent candidate ∼3.5 keV X-ray line detections consistent with the decay of a ∼7 keV sterile neutrino" (arXiv:1705.01837) [src: abstract, inline].
- **Consistency:** none at the level of the theory; production other than by mixing is reviewed by Boyarsky et al. (arXiv:1807.07938) [src: abstract].
- **Observational status:** "conventional production through active-sterile mixing is tightly constrained by X-ray searches and structure-formation observations" (Chun, Kadota & Yun 2026, arXiv:2609.04650) [src: abstract, inline]. Shi–Fuller revived: lepton asymmetries $L \gtrsim 0.5$ at high temperature, shown compatible with BBN and the CMB, open "significant viable parameter space in the $m_s \gtrsim 10\,\mathrm{keV}$ and $\sin^2 (2θ) \lesssim 10^{-14}$ regime", compatible with NuSTAR and INTEGRAL/SPI and with $m_{\mathrm{th}} \approx 4.1\,\mathrm{keV}$ Lyman-α inferences (Vogel et al. 2025, arXiv:2507.18752) [src: abstract, inline]. Production inside a sterile sector, decoupled from the mixing, is a 2026 alternative (arXiv:2609.04650) [src: abstract, inline].
- **Status date:** 2026-11-03

## Interacting dark matter
<!-- key: interacting-dark-matter -->

### Self-interacting dark matter (SIDM)
<!-- key: self-interacting-dark-matter-sidm -->
- **Defining equations:** scattering rate $R_{\rm scat}=\sigma v_{\rm rel}\rho_{\rm dm}/m\approx 0.1\;{\rm Gyr}^{-1}\times\Big(\frac{\rho_{\rm dm}}{0.1\;{\rm\,M}_{\odot}/{\rm pc}^{3}}\Big)\Big(\frac{v_{\rm rel}}{50\;{\rm km/s}}\Big)\Big(\frac{\sigma/m}{1\;{\rm cm^{2}/g}}\Big)\,,$ (Tulin & Yu 2017, arXiv:1705.02358) [src: Eq. 1]; an effect on halos requires $\sigma/m\sim 1\;{\rm cm^{2}/g}\approx 2\times 10^{-24}\;{\rm cm^{2}/GeV}$ [src: Eq. 2], "at least one scattering per particle over 10 Gyr".
- **Parameters:** $\sigma/m$ and its velocity dependence; for a light mediator, the dark-matter mass, the mediator mass and the coupling. Above a velocity scale w set by these, elastic scattering through a light mediator gives $σ\propto v^{-4}$ (Gurian et al. 2026, arXiv:2610.28745) [src: abstract, inline].
- **Predictions:** heat transfer into the inner halo gives "a shallower density profile and a more spherical halo shape" for $\sigma/m=1$ cm²/g (arXiv:1705.02358) [src: Sect. I.3, Fig. 2 caption]; self-interactions "rapidly fall out of equilibrium" in the early Universe, so SIDM "retains the success of large-scale structure formation from ΛCDM" [src: Sect. I.3, text after Eq. 2]. At late times cores can undergo gravothermal collapse; for idealised NFW halos "the collapse time can be predicted from the Knudsen number at the scale radius", while halos from cosmological simulations differ "by up to a factor of a few" (arXiv:2610.28745) [src: abstract].
- **Consistency:** none at the level of the theory; the linear power spectrum is unaffected (above), so SIDM is a non-linear signature, treated in `thcosmo-nonlinear-structure`.
- **Observational status:** a 2026 analysis of 29 quadruply imaged quasars "hints at dark matter halo densities consistent with gravothermal core collapse"; combined with cluster and Milky-Way-satellite upper limits, favoured models have masses of 20–80 GeV, MeV-scale mediators and cross-sections of $10^2$–$10^4$ cm² g⁻¹ at 10 km s⁻¹ (Gilman et al. 2026, arXiv:2610.40766) [src: abstract]. A hint, not a detection; cluster and satellite limits: cosmoskill `cosmo-neutrinos-dark-matter`.
- **Status date:** 2026-11-03

### Atomic and dissipative dark matter
<!-- key: atomic-and-dissipative-dark-matter -->
- **Defining equations:** two fermions with opposite charges under a dark U(1), coupled to a bath of dark photons until they "recombine into neutral atom-like bound states" (Cyr-Racine & Sigurdson 2013, arXiv:1209.5752) [src: abstract].
- **Parameters:** masses of the two fermions, dark fine-structure constant, dark-photon temperature; for partially interacting models, the fraction of dark matter (Fan et al. 2013, arXiv:1303.1521) [src: abstract].
- **Predictions:** delayed kinetic decoupling "imprints a new length scale, the Dark-Acoustic-Oscillation (DAO) scale" that shapes the small-scale power spectrum and sets the minimal halo mass; atomic dark matter is also self-interacting "with a velocity-dependent cross section"; the thermal history needs "significant improvements over the standard atomic hydrogen calculation" (arXiv:1209.5752) [src: abstract]. A subdominant dissipative component can cool and form a dark disk ("Double-Disk Dark Matter"), "comparable to the baryonic fraction" in density (arXiv:1303.1521) [src: abstract].
- **Consistency:** none found in the sources read. For dissipative self-interactions of inelastic dark matter, the gravothermal fluid framework has been extended with "the effective cooling rate for dark matter upscattering to an excited state followed by decay" (Batteas et al. 2026, arXiv:2610.37852) [src: abstract].
- **Observational status:** not verified in this run (see `results.md`, "Not verified").
- **Status date:** 2026-11-03

## Dark sectors
<!-- key: dark-sectors -->

### Hidden-sector thermal relics: SIMPs and decoupled freeze-out
<!-- key: hidden-sector-thermal-relics-simps-and -->
- **Defining equations:** freeze-out by a number-changing 3 → 2 annihilation inside a nearly secluded dark sector thermalised with the Standard Model after reheating (Hochberg et al. 2014, arXiv:1402.5143) [src: abstract, inline]; the general freeze-out of a decoupled sector with its own temperature (arXiv:2007.03696) [src: abstract, inline].
- **Parameters:** dark-matter mass, dark-sector coupling, ratio of dark to visible temperature, portal coupling.
- **Predictions:** the SIMP mechanism "points to sub-GeV dark matter", and "3 → 2 annihilations typically predict sizable 2 → 2 self-interactions" (arXiv:1402.5143) [src: abstract, inline]. For a decoupled sector the required cross-section differs from the canonical value by up to "orders of magnitude" (arXiv:2007.03696) [src: abstract, inline]. Sub-GeV thermal relics need light mediators "due to the Lee-Weinberg bound"; for vector mediators of anomaly-free U(1) extensions the thermal targets are listed by Han & Krnjaic (arXiv:2603.03444) [src: abstract, inline].
- **Consistency:** none found in the sources read.
- **Observational status:** the couplings that keep the sector in equilibrium "imply measurable signals" in direct, indirect and collider searches (arXiv:1402.5143) [src: abstract]; electron-recoil experiments "are beginning to test" the vector-mediator targets (arXiv:2603.03444) [src: abstract].
- **Status date:** 2026-11-03

### Asymmetric dark matter
<!-- key: asymmetric-dark-matter -->
- **Defining equations:** a dark-matter particle–antiparticle asymmetry generated or transferred between the dark and visible sectors (Zurek 2014 review, arXiv:1308.0338) [src: abstract].
- **Parameters:** the asymmetry, the dark-matter mass, the transfer operator.
- **Predictions:** an asymmetric thermal relic "requires a larger annihilation cross-section compared to symmetric dark matter" to deplete the antiparticles (Baldes & Petraki 2017, arXiv:1703.00478) [src: abstract]; the asymmetry "may be erased at late times through oscillations" (arXiv:1308.0338) [src: abstract].
- **Consistency:** none found in the sources read.
- **Observational status:** Zurek reviews constraints "from the cosmic microwave background, neutron stars, the Sun, and brown and white dwarves" (arXiv:1308.0338) [src: abstract]; no current status was verified in this run.
- **Status date:** 2026-11-03

### Interacting dark matter (with baryons or dark radiation)
<!-- key: interacting-dark-matter-with-baryons-or-dark -->
- **Defining equations:** drag terms $R_{\chi}(\theta_{b}-\theta_{\chi})$ in the fluid equations, Eq. 14 of arXiv:1801.08609 [src: Eq. 14] (`formalism.md`); ETHOS parameters for dark radiation (arXiv:1512.05344) [src: abstract].
- **Parameters:** cross-section normalisation and power of the relative velocity, dark-matter mass; for dark radiation, the ETHOS effective parameters.
- **Predictions:** the effect of dark matter–proton scattering "is most prominent on small scales in the CMB power spectra and in the matter power spectrum" (arXiv:1801.08609) [src: abstract].
- **Consistency:** none found in the sources read.
- **Observational status:** "the first cosmological constraints on interactions between dark matter and protons" within the non-relativistic effective theory, from Planck 2015 temperature, polarisation and lensing "for all dark matter masses above 15 keV", for every operator of the non-relativistic effective theory (arXiv:1801.08609) [src: abstract]. Current limits: cosmoskill `cosmo-neutrinos-dark-matter`.
- **Status date:** 2026-11-03

## Macroscopic dark matter
<!-- key: macroscopic-dark-matter -->

### Primordial black holes as dark matter (status)
<!-- key: primordial-black-holes-as-dark-matter-status -->
Formation, abundance theory and evaporation belong to `thcosmo-pbh-defects`; the measured limits to cosmoskill (`cosmo-neutrinos-dark-matter`). Here only the status as a dark-matter candidate.
- **Defining equations:** none specific to this skill; the dark-matter fraction in PBHs as a function of mass is the quantity constrained.
- **Parameters:** PBH mass (or mass function) and the fraction of dark matter; formation, abundance and signatures are reviewed by Villanueva-Domingo, Mena & Palomares-Ruiz (arXiv:2103.12087) [src: abstract].
- **Predictions:** PBHs are non-particle dark matter, beyond the Planck-scale bound on point particles (arXiv:2303.02169) [src: Sect. 3.1]; light PBHs evaporate and can themselves produce dark-sector particles, with isocurvature constraints (arXiv:2603.02322) [src: abstract].
- **Consistency:** single-field ultra-slow-roll production "is severely tuned", but "the claim that PBH dark matter is generically fine-tuned conflates the worst case with a landscape spanning every naturalness tier" (Profumo 2026, arXiv:2606.12775) [src: abstract]; production in axion inflation can give all the dark matter in the asteroidal range with a LISA-measurable gravitational-wave background (Franciolini, Ijaz & Peloso 2026, arXiv:2604.27496) [src: abstract].
- **Observational status:** the windows quoted differ between papers: Carr and Kühnel (2020) give $10^{16}$–$10^{17}$ g, $10^{20}$–$10^{24}$ g and 10–$10^{3}M_{\odot}$, the last "contentious" (arXiv:2006.02838) [src: abstract, inline]; in 2025–2026 the asteroid-mass window is quoted as "$10^{17}$-$10^{22}$ g" (arXiv:2606.12775) [src: abstract, inline] and "$\sim 10^{17}- 10^{21}$ grams" (Koivu et al., arXiv:2510.00246) [src: abstract, inline]. Stellar microlensing, "under standard assumptions", excludes compact objects with $10^{-11} \lesssim M/M_{\odot} \lesssim 10^{4}$ as all of the dark matter (Green 2026, arXiv:2602.15974) [src: abstract, inline].
- **Status date:** 2026-11-03

