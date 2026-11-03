# Results on neutrinos and light relics

Scope: results that hold independently of one model: the Standard-Model $N_{\rm eff}$, relic densities, free-streaming and phase-shift results, generic bounds on light relics, with the model assumed; history of the key results. Measured $\Sigma m_\nu$ and $N_{\rm eff}$ themselves live in cosmoskill `cosmo-neutrinos-dark-matter`.

Snapshot: 2026-11-03

## The Standard-Model value of $N_{\rm eff}$
<!-- key: the-standard-model-value-of-n-rm-eff -->

- Recommended benchmark $N_{\rm eff}^{\rm SM} = 3.0440 \pm 0.0002$, with flavour oscillations, finite-temperature QED to ${\cal O}(e^3)$ and the full neutrino–neutrino collision integral; the uncertainty is attributed "predominantly to errors incurred in the numerical solution procedure" (|δN_eff| ∼ 10⁻⁴), "augmented by measurement errors in the solar mixing angle" $\sin^2\theta_{12}$ (|δN_eff| ∼ 10⁻⁴) (Bennett et al. 2020, arXiv:2012.02726) [src: abstract]. The calculation assumes a normal mass ordering [src: Sect. 6].
- Independent calculation with the full collision term, on- and off-diagonal, and an averaged-oscillation scheme: N_eff = 3.0440 (Froustey, Pitrou & Volpe 2020, arXiv:2008.01074) [src: abstract].
- Leading-digit breakdown of $N_{\rm eff}^{\rm SM}-3$ (arXiv:2012.02726) [src: Table 5]:

| Correction | Leading-digit contribution |
|---|---|
| $m_e/T_d$ correction | +0.04 |
| ${\cal O}(e^2)$ finite-temperature QED correction to the QED equation of state | +0.01 |
| Non-instantaneous decoupling + spectral distortion | −0.005 |
| ${\cal O}(e^3)$ finite-temperature QED correction to the QED equation of state | −0.001 |
| Flavour oscillations | +0.0005 |
| Type (a) finite-temperature QED corrections to the weak rates | $\lesssim 10^{-4}$ |

  The non-instantaneous term is defined relative to instantaneous decoupling at $T_d=1.3453$ MeV (arXiv:2012.02726) [src: Table 5 caption].
- The older value 3.046 "also misses the ${\cal O}(e^{3})$ correction" and has a nominal uncertainty of $\pm 0.002$; relative to the 2016 calculation the benchmark shifted by δN_eff ≃ −0.001 (arXiv:2012.02726) [src: Sect. 6].
- NLO QED corrections to the weak rates: Cielo et al. find a reduction of $-0.0007$ and N_eff^SM = 3.043 "with a theoretical uncertainty that is much smaller than any projected observational sensitivity" (arXiv:2306.05460) [src: abstract]. Drewes et al. find the fractional change from the rate correction "of order $10^{-5}$ or below, i.e., about a factor of 30 smaller" than Cielo et al. claim, restricting their analysis to the enhanced t-channel contributions but including the electron mass, and conclude that $3.0440 \pm 0.0002$ remains the benchmark (arXiv:2402.18481) [src: abstract]. Jackson & Laine find, for massless electrons, NLO corrections to the energy-transfer rates that "only have a small influence" on $N_{\rm eff}$ (arXiv:2412.03958) [src: abstract]. See `open-questions.md`.
- Positronium formation: in an out-of-equilibrium scenario with instantaneous equilibration, a variation of "at most" |ΔN_eff| ∼ 10⁻⁴, though "a more gradual formation could however yield a larger change"; in an equilibrium scenario the ${\cal O}(e^4)$ contribution is capped at $|\Delta N_{\rm eff}| \lesssim 10^{-6}$ (Binder et al. 2024, arXiv:2411.14091) [src: abstract].

## Light thermal relics: the minimal contribution
<!-- key: light-thermal-relics-the-minimal-contribution -->

- Any new light species that was ever in thermal equilibrium with the Standard-Model plasma gives $\Delta N_{\rm eff}\geq 0.027$ "(unless there are changes to the thermal history)" (Dvorkin et al. 2022, arXiv:2203.07943) [src: Sect. 2.1, last paragraph].
- For a thermally decoupled Goldstone boson, decoupling before the QCD phase transition suppresses the contribution "by an order of magnitude", to $0.05\geq\Delta N_{\rm eff}\geq 0.027$ (Baumann, Green & Wallisch 2016, arXiv:1604.08614) [src: Sect. 1]. The argument assumes that the effective description holds up to T_F ≪ Λ, no significant dilution after freeze-out, and Δg_*(T_F) ≲ g_*^SM(T_F) ≈ 10² [src: Sect. 1]; a thermal abundance is avoided if the reheating temperature is below the would-be freeze-out temperature, T_R < T_F [src: Sect. 1].
- The map from model parameters to $N_{\rm eff}$ for minimal models of new light species in effective field theory was surveyed by Brust, Kaplan & Walters (arXiv:1303.5379) [src: abstract].
- Robustness of the neutrino-mass bound to the neutrino abundance: with Planck, Planck and ACT lensing and DESI BAO, the 95% limit for the degenerate ordering moves from $\sum m_\nu<0.0691$ eV (standard thermal history) to $\sum m_\nu<0.0652$ eV with decays into photons only and $\sum m_\nu<0.0710$ eV with additional dark radiation; a model-agnostic neutrino-to-photon ratio gives $\sum m_\nu<0.0724$ eV; the neutrino temperature and $\sum m_\nu$ are positively correlated (Figueroa, Sobotka & Erickcek 2026, arXiv:2609.15970) [src: abstract]. The bound values belong to cosmoskill `cosmo-neutrinos-dark-matter`; the point here is that lowering the pre-recombination neutrino density "will only worsen" the tension with the mass splittings [src: abstract].

## Massive neutrinos: suppression of the matter power spectrum
<!-- key: massive-neutrinos-suppression-of-the-matter -->

All at fixed $(\omega_{\rm m},\Omega_\Lambda)$, degenerate masses (Lesgourgues & Pastor 2006, arXiv:astro-ph/0603494):

- Small-scale plateau: $\frac{P(k)^{f_{\nu}}}{P(k)^{f_{\nu}=0}}=\left(1-f_{\nu}\right)^{3}\left[1.9\times 10^{5}\,g(a_{0})\,\omega_{\rm m}\,f_{\nu}/N_{\nu}\,\right]^{-\frac{6}{5}f_{\nu}}~.$ (arXiv:astro-ph/0603494) [src: Eq. 143], "a very good approximation of the exact numerical result" [src: Sect. 4.5.6, text after Eq. 143]; g(a₀) ≃ 0.8 "can even be replaced by one" without changing the result significantly [src: Sect. 4.5.7].
- Linear approximation, printed as $\frac{P(k)^{f_{\nu}}}{P(k)^{f_{\nu}=0}}\simeq-8\,f_{\nu}~.$ (arXiv:astro-ph/0603494) [src: Eq. 144], "a reasonable first-order approximation for $0<f_{\nu}<0.07$" [src: Sect. 4.5.7]. As printed, the left side is the ratio itself, which cannot be negative; Fig. 12 of the same paper calls $-8\,f_{\nu}$ "the linear approximation" to the ratio plotted against Eq. 143 [src: Fig. 12 caption]. Read as a fractional change, the printed relation lacks a "$1-$" or a Δ; no correction appears in v2.
- The ratio "smoothly interpolates between one for $k<k_{\rm nr}$ and a plateau given by Eq. (143) for $k\gg k_{\rm eq}$" (arXiv:astro-ph/0603494) [src: Sect. 4.5.6, text after Eq. 144]. Two causes: equality is later, and $\delta_{\rm cdm}$ grows more slowly than the scale factor after $a_{\rm nr}$ [src: Sect. 4.5.7].
- CMB: for $f_{\nu}\leq 0.1$ neutrinos are relativistic at decoupling, and the effect of the mass on the temperature spectrum is indirect, through the background (time of equality, sound horizon); masses above "a few eV" would be non-relativistic at decoupling, with "more complicated consequences" (arXiv:astro-ph/0603494) [src: Sect. 4.6.1].
- Origin of current CMB bounds: the neutrino-mass bound from CMB data "is mostly a background measurement", "mostly a measurement of the neutrino equation of state"; the bound on the kinematic (free-streaming) mass is "largely relaxed", $\sum m_\nu^\mathrm{Pert.} < 0.8\,\mathrm{eV}$ (Bertólez-Martínez et al. 2024, arXiv:2411.14524) [src: abstract].

## The neutrino phase shift: detections
<!-- key: the-neutrino-phase-shift-detections -->

- First detection of the phase shift from the cosmic neutrino background in the Planck temperature spectrum (Follin et al. 2015, arXiv:1503.07863) [src: abstract].
- Template analyses detect the neutrino-induced phase shift "at about 10σ" with Planck and "roughly 14σ" with ACT and SPT added, consistent with three free-streaming neutrinos; **forecast**: 1σ uncertainties of "roughly 4.3% and 2.5%" for the Simons Observatory and CMB-S4 (Montefalcone, Wallisch & Freese 2025, arXiv:2501.13788) [src: abstract].
- Planck, ACT and SPT indicate that "neutrinos have been freely streaming since deep within the radiation-dominated epoch" (arXiv:2509.20363) [src: abstract].

## Light but massive relics: bounds
<!-- key: light-but-massive-relics-bounds -->

- At the minimal temperature T_X⁽⁰⁾ = 0.91 K: Weyl and higher-spin fermions (for example the gravitino) with $m_X\geq 2.26$ eV are ruled out at 95% C.L.; limits m_X ≤ 11.2, 1.06, 1.56 eV for scalar, vector and Dirac-fermion relics (arXiv:2107.09664) [src: abstract]. The body gives vectors 1.6 eV and Dirac fermions 1.1 eV [src: Sect. I; Sect. V], and arXiv:2203.07943 gives vectors 1.56 eV and Dirac fermions 1.06 eV [src: Sect. 4.3]: abstract and body disagree on the vector and Dirac assignments. Data Planck 2018, BOSS DR12 full shape, CFHTLenS (arXiv:2107.09664) [src: Sect. III].
- Planck is insensitive to the shape of the LiMR phase-space distribution for $z_{NR}<10^5$, which makes the limit "model-insensitive and readily reinterpretable" (arXiv:2607.12021) [src: abstract].

## History of the key results
<!-- key: history-of-the-key-results -->

| Date | Result | Paper | Status |
|---|---|---|---|
| 1995 | Full Boltzmann hierarchy for massive neutrinos in synchronous and conformal Newtonian gauges | Ma & Bertschinger, arXiv:astro-ph/9506072 [src: abstract; Eqs. 56–57] | current reference for the linear equations |
| 2003 | Free-streaming neutrinos produce a "unique phase shift" of the acoustic oscillations for adiabatic initial conditions | Bashinsky & Seljak, arXiv:astro-ph/0310198 [src: abstract] | current; generalised by arXiv:1508.06342 |
| 2005 | $N_{\rm eff}=3.046$ with flavour oscillations; oscillations "do not essentially modify" the total change in neutrino energy density | Mangano et al., arXiv:hep-ph/0506164 [src: abstract] | superseded: misses the ${\cal O}(e^3)$ QED correction (arXiv:2012.02726) [src: Sect. 6] |
| 2006 | $\frac{P(k)^{f_{\nu}}}{P(k)^{f_{\nu}=0}}\simeq-8\,f_{\nu}~.$ for $0<f_{\nu}<0.07$, as printed | Lesgourgues & Pastor, arXiv:astro-ph/0603494 [src: Eq. 144], range [src: Sect. 4.5.7] | current as a first-order rule; printed without "$1-$" (`results.md` above) |
| 2013 | Self-interacting neutrinos: G_eff < 1/(56 MeV)² and a strongly interacting mode near $1/(10\ {\rm MeV})^{2}$ | Cyr-Racine & Sigurdson, arXiv:1306.1536 [src: abstract] | strongly interacting mode increasingly disfavoured (arXiv:2610.26654) [src: abstract] |
| 2015 | First detection of the neutrino phase shift in the CMB | Follin et al., arXiv:1503.07863 [src: abstract] | current; about 14σ with ACT and SPT (arXiv:2501.13788) [src: abstract] |
| 2016 | ΔN_eff = 0.027 as the minimal thermal target | Baumann, Green & Wallisch, arXiv:1604.08614 [src: Sect. 1] | current |
| 2019 | CMB bound on invisible neutrino decay τ_ν > (1.3−0.3)×10⁹ s (m_ν/0.05 eV)³ | Escudero & Fairbairn, arXiv:1907.05425 [src: abstract] | superseded: wrong damping rate (arXiv:2011.01502) [src: abstract] |
| 2020 | N_eff^SM = 3.0440, two independent calculations | Bennett et al., arXiv:2012.02726 [src: abstract]; Froustey et al., arXiv:2008.01074 [src: abstract] | current benchmark |
| 2023 | N_eff^SM = 3.043 from NLO QED rates | Cielo et al., arXiv:2306.05460 [src: abstract] | disputed by arXiv:2402.18481 [src: abstract] |
| 2024 | CMB mass bound is "mostly a background measurement" | Bertólez-Martínez et al., arXiv:2411.14524 [src: abstract] | current |
| 2026 | Fully thermalised light sterile neutrinos strongly disfavoured, partially populated ones viable | Ladeira et al., arXiv:2606.21518 [src: abstract] | current |

## Not verified
<!-- key: not-verified -->

- The Planck 2018 and later measured values of $N_{\rm eff}$ and $\sum m_\nu$ were not read: they belong to cosmoskill `cosmo-neutrinos-dark-matter`.
- The value of $a_\nu$ in Eq. 2.53 of arXiv:1508.06342 was not read.
- The DESI BAO measurement of the neutrino phase shift (Whitford et al. 2024) was found by search but its abstract was not read.
- The CMB bound on neutrino self-interactions and the BAO phase shift from DESI DR2 were not read; the self-interaction status above rests on DESI DR1 (arXiv:2610.26654).
