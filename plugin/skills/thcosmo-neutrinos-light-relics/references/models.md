# Models of light relics and non-standard neutrinos

Scope: the model landscape beyond three free-streaming Standard-Model neutrinos, one card per model or class, chosen by literature weight in the reviews of Dvorkin et al. (arXiv:2203.07943) and Lesgourgues & Pastor (arXiv:astro-ph/0603494) and in the 2024–2026 literature; formalism in `formalism.md`, model-independent results in `results.md`. Sterile neutrinos as dark matter (keV scale) are in `thcosmo-dark-matter-models`.

Snapshot: 2026-11-03

Bounds cited to Table 1 of Dvorkin et al. (arXiv:2203.07943) are its compilation for Planck 2018 TT,TE,EE + BAO at 95% C.L., with Standard-Model neutrinos fixed at N_eff,fs = 3.046 where stated [src: Table 1]; other Planck 2018 bounds in the cards (decay, majoron) are cited to their own papers. Measured values of $N_{\rm eff}$ and $\sum m_\nu$ belong to cosmoskill `cosmo-neutrinos-dark-matter`.

## Extra radiation
<!-- key: extra-radiation -->

### Free-streaming dark radiation and light thermal relics
<!-- key: free-streaming-dark-radiation-and-light-thermal -->
- **Defining equations:** a decoupled light species X adds $\Delta N_{\rm eff}=\frac{4}{7}g_{X,\star}\left(\frac{T_{X}}{T_{\nu}}\right)^{4}=\frac{4}{7}g_{X,\star}\left(\frac{43}{4g_{\star}(T_{F})}\right)^{4/3}\ ,$ (arXiv:2203.07943) [src: Eq. 2]; its perturbations free-stream like neutrinos.
- **Parameters:** spin (through $g_{X,\star}$), freeze-out temperature $T_F$ or the coupling to the Standard Model that sets it; for pseudo-Nambu–Goldstone bosons (axions, familons, majorons) the scale Λ of the dimension-5 coupling $\mathcal{L}\supset-\Lambda_{i}^{-1}\partial_{\mu}\phi\,\bar{\psi}_{i}\gamma^{\mu}\gamma^{5}\psi_{i}$ (arXiv:2203.07943) [src: Fig. 2 caption].
- **Predictions:** $\Delta N_{\rm eff}\geq 0.027$ for any species once in equilibrium, unless the thermal history changes (arXiv:2203.07943) [src: Sect. 2.1]; a drop by "about one order of magnitude" across the QCD transition at T_F ∼ 150 MeV [src: Fig. 1 caption]; a phase shift of the acoustic peaks (`formalism.md`).
- **Consistency:** a thermal abundance is avoided if T_R < T_F, so a null result bounds couplings only given a reheating temperature; recoupling bounds avoid that assumption (arXiv:1604.08614) [src: Sect. 1]; (arXiv:2203.07943) [src: Sect. 2.2]. Reply: none needed; these are conditions, not objections.
- **Observational status:** $\Delta N_{\rm eff,fs}<0.28$, Planck 2018 TT,TE,EE + BAO, 95% C.L. (as compiled in arXiv:2203.07943) [src: Table 1].
- **Status date:** 2026-11-03

### Fluid-like (self-interacting) dark radiation
<!-- key: fluid-like-self-interacting-dark-radiation -->
- **Defining equations:** none universal; the class is defined by perturbations that "propagate with a speed that does not exceed the sound speed of the photon-baryon plasma" and "therefore do not lead to a phase shift" (Dvorkin et al. 2022, arXiv:2203.07943) [src: Sect. 3].
- **Parameters:** $N_{\rm eff,fld}$ alongside $N_{\rm eff,fs}$; in decoupling or recoupling variants, the transition time (arXiv:2203.07943) [src: Sect. 3].
- **Predictions:** the same expansion rate as free-streaming radiation of equal density, different perturbations; "CMB data allows larger $\Delta N_{\rm eff,fld}$" (arXiv:2203.07943) [src: Sect. 3]. Arises from neutrino self-interactions, neutrino–dark-sector interactions or dark-radiation self-interactions [src: Sect. 3]. A 2026 dark-QCD model in which dark radiation confines into light dark pions behaves as "an imperfect fluid with nonzero viscosity" (Buckley, Fernandez & Putney 2026, arXiv:2609.16120) [src: abstract].
- **Consistency:** none found among the sources read.
- **Observational status:** $\Delta N_{\rm eff,fld}<0.38$ with N_eff,fs = 3.046; $N_{\rm eff,fld}<0.6$ when N_eff,fs + N_eff,fld = 3.046 or both vary; $N_{\rm eff,fld}<0.5$ and $<0.51$ with $\sum m_\nu$ varied; Planck 2018 TT,TE,EE + BAO, 95% C.L. (as compiled in arXiv:2203.07943) [src: Table 1]. The dark-QCD model reports $H_0 = 71.60\pm 0.63$ km/s/Mpc with "a 3σ residual tension" across Planck, ACT, BBN, Pantheon+, DESI DR2 and SH0ES (arXiv:2609.16120) [src: abstract]; its place among $H_0$ responses is for `thcosmo-tensions-model-building`.
- **Status date:** 2026-11-03

## Interacting and decaying neutrinos
<!-- key: interacting-and-decaying-neutrinos -->

### Self-interacting neutrinos ($G_{\rm eff}$)
<!-- key: self-interacting-neutrinos-g-rm-eff -->
- **Defining equations:** $\mathcal{L}_{\rm int}=g_{ij}\bar{\nu}_{i}\nu_{j}\varphi,$ (Kreisch, Cyr-Racine & Doré 2019, arXiv:1902.00534) [src: Eq. 1], with the universal choice $g_{ij}\equiv g_{\nu}\delta_{ij},$ [src: Eq. 2], which the authors call "likely unrealistic" but a simple benchmark [src: Sect. II]. In the contact limit $\displaystyle|\mathcal{M}|_{\nu_{i}}^{2}=\displaystyle\sum_{\rm spins}|\mathcal{M}|_{\nu_{i}+\nu_{j}\rightarrow\nu_{k}+\nu_{l}}^{2}=\displaystyle 2G_{\rm eff}^{2}\left(s^{2}+t^{2}+u^{2}\right),$ [src: Eq. 3], with $G_{\rm eff}\equiv|g_{\nu}|^{2}/m_{\varphi}^{2}$ [src: Sect. II, inline, text after Eq. 3].
- **Parameters:** $G_{\rm eff}$; arXiv:1902.00534 introduces the self-interactions "in the presence of a non-vanishing sum of neutrino masses" and fits $N_{\rm eff}$ with them [src: abstract].
- **Predictions:** delayed onset of free streaming; the absence of the phase shift "can be compensated by shifting the value of other cosmological parameters", "an important caveat" to its detections, and a localised feature in the matter power spectrum at scales entering the horizon at the onset of free streaming (arXiv:1902.00534) [src: abstract]. Two regions: G_eff < 1/(56 MeV)² and a strongly interacting mode around G_eff ≃ 1/(10 MeV)², with neutrinos scattering until z ∼ 10⁴ (Cyr-Racine & Sigurdson 2013, arXiv:1306.1536) [src: abstract].
- **Consistency:** building a model with the gauge and flavour structure of the Standard Model "likely requires" a light sterile species mixed with the active neutrinos and coupled to the mediator; for a mediator below 10 MeV, SN 1987A, BBN and IceCube "provide some of the strongest constraints" (arXiv:1902.00534) [src: Sect. II]. Reply: a type-I seesaw model with a keV-scale scalar in which active neutrinos convert resonantly into self-interacting dark radiation after BBN evades laboratory bounds, since cosmology "cannot distinguish between neutrinos and dark radiation with the same abundance and free-streaming properties" (Das et al. 2025, arXiv:2506.08085) [src: abstract]. Flavour-specific interactions treated with mixing weaken CMB bounds on the coupling by $\sqrt{2}$ (two flavours) or $\sqrt{6}$ (one flavour), the combined-fluid approach being "less reliable for only $\nu_e$ interacting" (Barenboim, Drewes & Oldengott 2026, arXiv:2609.13821) [src: abstract].
- **Observational status:** the strongly interacting mode was once favoured with $H_0=72.3 \pm 1.4$ km/s/Mpc and $N_{\rm eff} = 4.02 \pm 0.29$, but "traditional Bayesian analyses penalize the model" (arXiv:1902.00534) [src: abstract]. With the DESI DR1-only FS + BAO + Lyα dataset (no CMB), the moderately interacting region is bimodal, and its sharp intermediate mode near G_eff ≃ 10⁻³ MeV⁻² "is not penalized versus the weaker standard-like mode"; with DESI DR1 full shape + BAO + CMB-SPA (Planck, ACT, SPT), the evidence against the strongly interacting mode is "the strongest thus far (with odds of 5:100000)" (Noriega et al. 2026, arXiv:2610.26654) [src: abstract]. Phase-shift analyses of Planck, ACT and SPT find free streaming "since deep within the radiation-dominated epoch" (arXiv:2509.20363) [src: abstract].
- **Status date:** 2026-11-03

### Invisible neutrino decay
<!-- key: invisible-neutrino-decay -->
- **Defining equations:** a heavier neutrino $\nu_H$ couples to a lighter $\nu_l$ and a massless scalar φ through a Yukawa interaction, decay ν_H → ν_l + φ (Barenboim et al. 2020, arXiv:2011.01502; Chen et al. 2022, arXiv:2203.09075) [src: abstracts].
- **Parameters:** rest-frame lifetime $\tau_0$, parent mass $m_{\nu_H}$, mass gap $\Delta m_\nu^2$ to the daughter.
- **Predictions:** ultra-relativistic decays damp the neutrino anisotropic stress (arXiv:2011.01502) [src: abstract]; non-relativistic decays into dark radiation change the growth of structure over time (Chacko et al. 2020, arXiv:2002.08401) [src: abstract].
- **Consistency:** the commonly used anisotropy-loss rate Γ_T = (1/τ₀)(m_νH/E_νH)³ is wrong; the rate is ∼ (1/τ₀)(m_νH/E_νH)⁵, and the effective perturbation equations used for non-relativistic decay "formally violate momentum conservation and gauge invariance", an effect "likely small" (arXiv:2011.01502) [src: abstract]. A non-zero daughter mass adds a factor ∝ (Δm_ν²/m_νH²)²: Γ_T ∼ (Δm_ν²/m_νH²)² (m_νH/E_ν)⁵ (1/τ₀) (arXiv:2203.09075) [src: abstract].
- **Observational status:** BBN requires τ_ν > 10⁻³ s at 95% CL; Planck 2018 gave τ_ν > (1.3−0.3)×10⁹ s (m_ν/0.05 eV)³ at 95% CL with the old rate (Escudero & Fairbairn 2019, arXiv:1907.05425) [src: abstract]; with the corrected rate the limit becomes τ₀ ≳ (4×10⁵ → 4×10⁶) s (m_νH/50 meV)⁵ (arXiv:2011.01502) [src: abstract], and with mass-spectrum-consistent phase space τ⁰ ≳ (6 → 10)×10⁵ s (atmospheric gap, one channel), τ⁰ ≳ (400 → 500) s (solar gap) and τ⁰ ≳ (2 → 3)×10⁷ s (two channels), "remarkably independent of the parent mass" (Planck 2018, arXiv:2203.09075) [src: abstract].
- **Status date:** 2026-11-03

## Massive light relics
<!-- key: massive-light-relics -->

### Light but massive relics (LiMRs)
<!-- key: light-but-massive-relics-limrs -->
- **Defining equations:** $k_{\rm fs}\approx\frac{0.1\,h\rm Mpc^{-1}}{\sqrt{1+z}}\frac{1.95\,\rm K}{T_{X}}\frac{m_{X}}{0.1\,\rm eV}$ and $\omega_{X}=\Omega_{X}\,h^{2}\approx\frac{m_{X}}{93.14\,\rm eV}\left(\frac{T_{X}}{1.95\,\rm K}\right)^{3}$ (arXiv:2203.07943) [src: Eqs. 3–4].
- **Parameters:** mass $m_X$, temperature today $T_X^{(0)}$, spin; the minimally coupled thermal benchmark is T_X⁽⁰⁾ = 0.91 K (arXiv:2203.07943) [src: Sect. 4.3]. The review reports the constraints of its Ref. [82] on scalars, Weyl fermions, vectors and Dirac fermions [src: Sect. 4.3]. The abstract of arXiv:2107.09664 groups "Weyl (and higher-spin) fermions" with the gravitino [src: abstract]; the s=3/2 gravitino "is cosmologically equivalent to a s=1/2 Weyl fermion" because only two of its four modes are thermally populated at its relativistic decoupling [src: Sect. I; Sect. V].
- **Predictions:** radiation-like at early times, then a suppression of small-scale clustering like massive neutrinos (arXiv:2203.07943) [src: Sect. 4.2]. Future ground-based CMB observatories should distinguish LiMRs from massless dark radiation (**forecast**, arXiv:2607.12021) [src: abstract].
- **Consistency:** none found among the sources read.
- **Observational status:** at T_X⁽⁰⁾ = 0.91 K, the arXiv abstract excludes Weyl fermions with $m_X\geq 2.26$ eV at 95% C.L. and gives limits m_X ≤ 11.2, 1.06, 1.56 eV for scalar, vector and Dirac-fermion relics (Xu, Muñoz & Dvorkin 2021, arXiv:2107.09664) [src: abstract]; the body gives 11 eV for scalars, 2.3 eV for Weyl fermions, 1.6 eV for vectors and 1.1 eV for Dirac fermions [src: Sect. I; Sect. V], and Dvorkin et al. report vectors at 1.56 eV and Dirac fermions at 1.06 eV (arXiv:2203.07943) [src: Sect. 4.3]. Abstract and body disagree on which of the two limits is the vector one and which the Dirac one. Data: Planck 2018, BOSS DR12 full shape and CFHTLenS [src: Sect. III]; weak lensing is "critical for breaking parameter degeneracies" [src: abstract].
- **Status date:** 2026-11-03

### Light (eV-scale and sub-eV) sterile neutrinos
<!-- key: light-ev-scale-and-sub-ev-sterile-neutrinos -->
- **Defining equations:** a 3+1 scheme with a fourth, inert state and a 4×4 mixing matrix, mixing angles $\theta_{14}$, $\theta_{24}$, $\theta_{34}$ and mass splitting $\Delta m^2_{41}$ (arXiv:1905.11290) [src: abstract].
- **Parameters:** $\Delta m^2_{41}$ and the mixing angles; in cosmology the effective abundance ($N_{\rm eff}$) and the effective mass $m_s^{\rm eff}$, which differs from the physical mass when the state is not fully populated (arXiv:2606.21518) [src: abstract].
- **Predictions:** full thermalisation, N_eff ≃ 4, for the short-baseline preferred mixing (arXiv:1905.11290) [src: abstract].
- **Consistency:** the review of Dvorkin et al. reports "a tension between the measurements of $N_{\rm eff}$ and the expectation from light sterile neutrinos"; proposed ways out are large asymmetries, secret neutrino interactions and modified thermal histories (arXiv:2203.07943) [src: Sect. 6.2]. Reply: current data "do not generically exclude sterile neutrinos, but rather place strong pressure on fully thermalized or highly populated scenarios" (Ladeira et al. 2026, arXiv:2606.21518) [src: abstract].
- **Observational status:** with Planck, DESI DR2 BAO and supernovae, without a local $H_0$ prior, the fully thermalised case is "strongly disfavored" in ΛCDM and CPL, while Dodelson–Widrow-like and different-temperature realisations remain viable (arXiv:2606.21518) [src: abstract]. With DESI DR2, CMB, lensing, supernovae and SH0ES, $N_{\rm eff} = 3.43 \pm 0.13$ and sterile masses m_s ≃ 0.1–0.2 eV are favoured at $\gtrsim 3\sigma$, eV-scale masses remain "strongly excluded", and for $N_{\rm eff}=3.50$ the limit is $m_s < 0.17$ eV (95% CL) (García Escudero & Abazajian 2025, arXiv:2509.25478) [src: abstract]; the preference rests on SH0ES.
- **Status date:** 2026-11-03

### Majoron models
<!-- key: majoron-models -->
- **Defining equations:** the majoron is "a pseudo-Goldstone boson arising from the spontaneous breaking of global lepton number" (Escudero & Witte 2019, arXiv:1909.04044) [src: abstract]; the neutrino–majoron coupling has the form of Eq. 1 of arXiv:1902.00534, which "could also arise in models where neutrinos couple to a Majoron" [src: Sect. II].
- **Parameters:** majoron mass and the coupling λ; in the type-I seesaw, the lepton-number breaking scale $v_L$ (arXiv:1909.04044) [src: abstract].
- **Predictions:** majorons that thermalise with neutrinos after BBN through inverse neutrino decays leave imprints in the CMB (arXiv:1909.04044) [src: abstract]; depending on the majoron mass, neutrinos show decoupling (heavy majoron) or recoupling (light majoron) features (Dvorkin et al. 2022, arXiv:2203.07943) [src: Sect. 3].
- **Consistency:** the decoupling case "is disfavored by other terrestrial and cosmological constraints" (arXiv:2203.07943) [src: Sect. 3]; reply: none found.
- **Observational status:** Planck 2018 is sensitive to couplings "as small as λ ∼ 10⁻¹³", corresponding in the type-I seesaw to v_L ∼ O(100) GeV; with an extra $N_{\rm eff}$ the interactions "can ameliorate" the $H_0$ tension (arXiv:1909.04044) [src: abstract]; the recoupling case with an eV-scale majoron "may help mitigate" it (arXiv:2203.07943) [src: Sect. 3]. Its standing among $H_0$ responses is for `thcosmo-tensions-model-building`.
- **Status date:** 2026-11-03
