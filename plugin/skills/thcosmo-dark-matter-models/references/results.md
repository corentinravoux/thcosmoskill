# Results on dark-matter models

Scope: results that hold beyond one candidate: relic-abundance benchmarks, unitarity and phase-space bounds, cut-off scales of non-cold candidates, and the history of the key results.

Snapshot: 2026-11-03

## Model-independent bounds on a dark-matter particle
<!-- key: model-independent-bounds-on-a-dark-matter -->

### Mass: phase space and quantum pressure
<!-- key: mass-phase-space-and-quantum-pressure -->

- Tremaine–Gunn argument for fermions, as presented by Safdi: the Fermi velocity of a degenerate sphere, $\begin{split}v_{f}={1\over m_{\chi}}\left({9\pi\over 4}{M\over m_{\chi}R^{3}}\right)^{1/3}\,.\end{split}$ (arXiv:2303.02169) [src: Eq. 10], must stay below the escape velocity; for a dwarf galaxy with $M\sim 5\times 10^{7}M_{\odot}$ and $R\sim 2.5$ kpc this "restricts $m_{\chi}\gtrsim 100$ eV, which is close to what one finds from a more careful analysis" [src: Sect. 3.1].
- Below "roughly a keV" the dark matter "needs to be a boson because the quantum occupation numbers will necessarily be greater than unity in dense systems like dwarf galaxies" (arXiv:2303.02169) [src: Sect. 3.1].
- Bosons: the uncertainty principle gives $\begin{split}v\gtrsim{1\over R\,m_{\chi}}\sim 20\,\,{{\rm km}\over{\rm s}}{10^{-22}\,\,{\rm eV}\over m_{\chi}}\,,\end{split}$ (arXiv:2303.02169) [src: Eq. 12], so that for $m_{\chi}\lesssim 10^{-22}$ eV quantum pressure prevents structures as compact as dwarf galaxies; in 2023 the lectures state that pseudo-scalar dark matter with masses "roughly below few × $10^{-19}$ eV appear excluded" [src: Sect. 3.1]. The current status of this bound is in `models.md`, card "Ultralight (fuzzy) dark matter".
- Upper end for point particles: above $m_{\chi}\gtrsim G^{-1/2}\sim 10^{19}$ GeV a particle can be localised within its own Schwarzschild radius, which "motivates only thinking about fundamental point particles at masses below the Planck scale"; heavier candidates (primordial black holes, bound states) must be extended (arXiv:2303.02169) [src: Sect. 3.1, inline].
- Free streaming of a thermal relic that decouples semi-relativistically at $T=m_{\chi}$: comoving horizon $\sim 50\,{\rm kpc}\,(1\,{\rm keV}/m_{\chi})$, an estimate made under "the very rough and not completely correct assumption" of semi-relativistic decoupling (arXiv:2303.02169) [src: Sect. 3.1, inline]. Proper cut-off scales are in `formalism.md`, section "Linear signatures".

### Unitarity bound on thermal relics
<!-- key: unitarity-bound-on-thermal-relics -->

- Partial-wave unitarity caps the annihilation cross-section and hence the mass of a thermal relic made of point particles. von Harling and Petraki (arXiv:1407.7874) argue that the unitarity limit on the inelastic cross-section "is realized only if dark matter annihilates via a long-range interaction" and put the upper bound at "about 197 (139) TeV for (non)-self-conjugate dark matter" [src: abstract].
- Smirnov and Beacom (arXiv:1904.11503) include bound-state formation and Sommerfeld enhancement, which "lower the unitarity bound from 139 TeV to below 100 TeV for non-self-conjugate dark matter and from 195 TeV (the oft-quoted value of 340 TeV assumes $Ω_{DM} h^2 = 1$) to 140 TeV for the self-conjugate case"; for composite dark matter the largest allowed mass is 1 PeV [src: abstract, inline].
- The bound is evaded by freeze-out processes other than self-annihilation: going beyond "WIMP-like, $m_{\rm DM}\gg\mathcal{O}(100~\rm TeV)$" predicts nearly degenerate states and generically metastable dark matter, and thermal freeze-out "may allow for dark matter masses up to the Planck scale" (Frumkin et al., arXiv:2207.01635) [src: abstract, inline].

## Relic-abundance benchmarks
<!-- key: relic-abundance-benchmarks -->

| Quantity | Value as printed | Assumptions | Source |
|---|---|---|---|
| "Canonical" thermal cross-section | "usually stated as 3*10^-26 cm^3s^-1, with unspecified uncertainty" | generic WIMP, mass-independent | Steigman et al., arXiv:1204.3622 [src: abstract] |
| Precise thermal cross-section, $m>10$ GeV | 2.2*10^-26 cm^3s^-1 "with feeble mass-dependence" | generic WIMP | arXiv:1204.3622 [src: abstract] |
| Maximum of the required cross-section | 5.2*10^-26 cm^3s^-1 at masses around 0.3 GeV | same | arXiv:1204.3622 [src: abstract] |
| Order-of-magnitude estimate | $\langle\sigma v\rangle\sim 10^{-9}$ GeV⁻² $\sim 10^{-26}$ cm³ s⁻¹; "more precisely" $\sim 2\times 10^{-26}$ cm³ s⁻¹ | Safdi's parametric estimate | arXiv:2303.02169 [src: Sect. 4.1, text after Eq. 19] |
| Freeze-out time | $x_{\rm fo}\sim 10$ | non-relativistic freeze-out | arXiv:2303.02169 [src: Sect. 4.1, inline] |
| Decoupled (hidden-sector) freeze-out | differs from the canonical value by an amount "generally sizeable" that "can reach orders of magnitude" | hidden sector with its own temperature | Bringmann et al., arXiv:2007.03696 [src: abstract] |

## Bounds on non-cold dark matter from linear and small-scale structure
<!-- key: bounds-on-non-cold-dark-matter-from-linear-and -->

Measured limits belong to cosmoskill (`cosmo-neutrinos-dark-matter`, `cosmo-lyman-alpha`); the table gives the bound each model paper relies on, with its assumptions.

| Model | Bound as printed | Data and assumptions | Source |
|---|---|---|---|
| Thermal-relic WDM | lower limit "of $5.7\;\mathrm{keV}$ (at 95\% C.L.)" | high-z Lyman-α, $k_{\rm max}=0.2$ km⁻¹ s; 4.1 keV for $k_{\rm max}<0.1$ km⁻¹ s and earlier priors | arXiv:2309.04533 [src: abstract] |
| Thermal-relic WDM (2005) | $m_{\rm wdm}>550$ eV (2σ); sterile neutrinos $> 2.0$ keV (2σ) | WMAP + Lyman-α | arXiv:astro-ph/0501562 [src: abstract] |
| Ultralight axion, all the dark matter | "a 95% lower limit $m_\text{a} > 2 \times 10^{-20}\,\text{eV}$" | Lyman-α, emulator of hydrodynamical simulations | arXiv:2007.12705 [src: abstract, inline] |
| Ultralight dark matter, all the dark matter | $m > 3 \times 10^{-19}$ eV; $m > 8 \times 10^{-18}$ eV at 95% confidence if Ursa Major III/UNIONS I is a galaxy | ultra-faint dwarf kinematics, perturbative heating rate | arXiv:2509.02781 [src: abstract, inline] |
| ALP, all the dark matter | $m_a \gtrsim 10^{-17}$ eV "for most cases considered"; relaxable to $\sim 6\times 10^{-19}$ eV only post-inflationary with a strongly temperature-dependent mass; up to $m_a > 5\times 10^{-7}$ eV from CMB tensor modes for small reheating efficiencies | isocurvature, superradiance, free streaming | arXiv:2511.15790 [src: abstract, inline] |
| Fermionic Higgs-portal freeze-in at stronger coupling | masses "below about $100 -180\,\mathrm{keV}$" excluded | Lyman-α, depending on the reheating history | arXiv:2606.20815 [src: abstract] |
| Dark matter–proton scattering | upper limits on each operator of the non-relativistic EFT for masses above 15 keV | Planck 2015 temperature, polarisation and lensing | arXiv:1801.08609 [src: abstract] |
| PBHs (compact objects), all the dark matter | excluded for $10^{-11} \lesssim M/M_{\odot} \lesssim 10^{4}$ "under standard assumptions" | stellar microlensing | arXiv:2602.15974 [src: abstract] |

## History of the key results
<!-- key: history-of-the-key-results -->

| Date | Result | Paper | Status |
|---|---|---|---|
| 1993 | Sterile neutrinos produced by oscillations can be hot, warm or cold dark matter; warm for $M\simeq$ 0.1–1.0 keV | Dodelson & Widrow, arXiv:hep-ph/9303287 [src: abstract, inline] | non-resonant production "tightly constrained" (arXiv:2609.04650) [src: abstract, inline] |
| 1998 | Resonant, lepton-asymmetry-driven sterile-neutrino production gives colder spectra | Shi & Fuller, arXiv:astro-ph/9810076 [src: abstract] | revived in 2025 with $L \gtrsim 0.5$ (arXiv:2507.18752) [src: abstract] |
| 1998 | Superheavy dark matter from gravitational production at the end of inflation | Chung, Kolb & Riotto, arXiv:hep-ph/9802238 [src: abstract] | current; catalogued by spin in arXiv:2312.09042 |
| 2000 | Fuzzy dark matter at m ∼ $10^{-22}$ eV for cores and the cut-off of small-scale power | Hu, Barkana & Gruzinov, arXiv:astro-ph/0003365 [src: abstract] | canonical range disfavoured (arXiv:2007.12705) [src: abstract]; (arXiv:2509.02781) [src: abstract] |
| 2009 | Freeze-in: IR-dominated yield independent of the reheat temperature | Hall et al., arXiv:0911.1120 [src: abstract] | current; ultraviolet (arXiv:1410.6157) and stronger-coupling (arXiv:2306.13061) variants added |
| 2012 | Thermal cross-section 2.2*10^-26 cm^3s^-1 above 10 GeV, not the canonical 3*10^-26 | Steigman, Dasgupta & Beacom, arXiv:1204.3622 [src: abstract] | current for standard histories; decoupled sectors differ (arXiv:2007.03696) |
| 2014 | Unitarity bound on thermal relics with bound states, about 197 (139) TeV | von Harling & Petraki, arXiv:1407.7874 [src: abstract] | lowered to 140 and below 100 TeV (arXiv:1904.11503) [src: abstract] |
| 2014 | SIMP: 3 → 2 freeze-out in a hidden sector, sub-GeV dark matter | Hochberg et al., arXiv:1402.5143 [src: abstract, inline] | current |
| 2018–2020 | 3.5 keV line ruled out as decaying dark matter by blank-sky XMM-Newton data; reply that the bounds are overestimated | arXiv:1812.06976 [src: abstract]; arXiv:2004.06601 [src: abstract] | disputed |
| 2021–2026 | Post-inflationary axion mass: 40–180 μeV, 95–450 μeV, 17.46(84) μeV in a minimal scaling model | arXiv:2108.05368 [src: abstract]; arXiv:2401.17253 [src: abstract]; arXiv:2609.20801 [src: abstract] | disputed (`open-questions.md`) |
| 2026 | Strong-lensing hint of gravothermal core collapse in SIDM | Gilman et al., arXiv:2610.40766 [src: abstract] | a hint; no independent confirmation read |

## Not verified
<!-- key: not-verified -->

- Pre-arXiv foundations were not read: Lee–Weinberg, Gondolo–Gelmini and Griest–Seckel on relic abundances, Griest–Kamionkowski on unitarity, and Preskill–Wise–Wilczek, Abbott–Sikivie and Dine–Fischler on misalignment. No tool returned their DOIs (the INSPIRE reference list of arXiv:1204.3622 lists them without DOIs), so they are not in `sources.tsv`; their content enters only through the reviews cited.
- The Bogoliubov number-density formula of gravitational production and the spin-by-spin abundances catalogued by Kolb & Long (arXiv:2312.09042) were not transcribed.
- The momentum-transfer cross-section parametrisation σ ∝ vⁿ of dark matter–baryon scattering and the ETHOS parameters were not transcribed.
- The isocurvature bound on the Hubble scale of inflation for pre-inflationary axions (Safdi Sect. 6.4.1, Eqs. 73–79) was not transcribed, and no current number for it was read.
- No observational status was verified for atomic or dissipative dark matter, asymmetric dark matter, or dark acoustic oscillations.
- Unitarity-bound and thermal cross-section values are read from abstracts; the figures and tables of arXiv:1204.3622 and arXiv:1904.11503 were not read.
- The isocurvature and non-Gaussianity constraints on post-inflationary axion-like particles of arXiv:2511.15790 were read from the abstract only.
