# Results on cosmological gravitational waves

Scope: results that hold independently of one source model: amplitudes of the irreducible backgrounds, theorems on propagation and causality, spectral shapes fixed by general arguments, bounds that hold for any source; then the history of key results.

Snapshot: 2026-11-12

## Integrated bound from extra radiation
<!-- key: integrated-bound-from-extra-radiation -->

From Caprini & Figueroa 2018 (arXiv:1801.04268), Sect. 4.1. A background well inside the horizon adds radiation, $H^{2}(a)=H_{0}^{2}~\left[\left(\frac{\rho_{\rm GW}^{0}}{\rho_{c}^{0}}+\Omega^{0}_{\rm rad}\right)\left(\frac{a_{0}}{a}\right)^{4}+\Omega^{0}_{\rm mat}\left(\frac{a_{0}}{a}\right)^{3}+\Omega^{0}_{\Lambda}\right]\,.$ (arXiv:1801.04268) [src: Eq. 121], so that $\left(\frac{h^{2}\rho_{\rm GW}}{\rho_{c}}\right)_{0}\leq h^{2}\Omega_{\gamma}^{0}\left(\frac{g_{S}(T_{0})}{g_{S}(T)}\right)^{4/3}\frac{7}{8}\,\Delta N_{\nu}=5.6\times 10^{-6}\Delta N_{\nu}\,,$ [src: Eq. 127], equivalently $\left(\frac{h^{2}\rho_{\rm GW}}{\rho_{c}}\right)_{0}\leq h^{2}\Omega_{\gamma}^{0}~\frac{7}{8}\,\left(\frac{4}{11}\right)^{4/3}\Delta N_{\rm eff}=5.6\times 10^{-6}\,\Delta N_{\rm eff}\,,$ [src: Eq. 129], on the integrated density $\left(\frac{h^{2}\rho_{\rm GW}}{\rho_{c}}\right)_{0}=\int\frac{df}{f}\,h^{2}\,\Omega_{\rm GW}(f)\,.$ [src: Eq. 130].
- Conditions printed with it: the bound reads as one on the amplitude "Except in the extreme case of a GW spectrum with a very narrow peak of width $\Delta f\ll f$"; it applies only to wavelengths "well inside the horizon" when the bound on $\Delta N_\nu$ is set, and only to backgrounds produced before BBN or CMB decoupling (arXiv:1801.04268) [src: Sect. 4.1, text after Eq. 130]. The review uses $N_{\rm eff}=3.046$ for the Standard Model [src: Sect. 4.1, inline, text after Eq. 127]; the current value is in `thcosmo-neutrinos-light-relics`.
- In pure Abelian axion inflation the GW signals within reach of interferometers are in conflict with the $\Delta N_{\rm eff}$ bound (arXiv:2508.00798) [src: abstract].
- BBN form of the bound, "the well-known “standard Big Bang Nucleosynthesis” (sBBN) constraint [71, 72, 73, 74, 75, 76]", quoted, not derived, by Boyle & Buonanno 2008 (arXiv:0708.2279) [src: Sect. VII, text before Eq. 44]: $\int_{f_{{\rm bbn}}}^{f_{{\rm end}}}\Omega_{0}^{{\rm gw}}(f)\frac{df}{f}\leq 1.5\times 10^{-5}.$ (arXiv:0708.2279) [src: Eq. 44]. It "only applies to the part of the present-day gravitational-wave spectrum that was generated prior to Big Bang Nucleosynthesis", and the integral runs only over modes "already 'inside the Hubble horizon' ($k>a_{{\rm bbn}}H_{{\rm bbn}}$)" at BBN, "at photon temperature $T\sim 1~{\rm MeV}$", so that its lower limit is $f_{{\rm bbn}}\approx 1.8\times 10^{-11}~{\rm Hz}$; $f_{\rm end}$ is the high-frequency cutoff of the primordial spectrum [src: Sect. VII, text after Eq. 44].
- "in practice it effectively acts as an algebraic constraint (local in frequency space) of the form $\Omega_{0}^{{\rm gw}}(f)<1.5\times 10^{-5}$ for $f_{{\rm bbn}}<f<f_{{\rm end}}$"; the spectrum "can only exceed this bound by having a very narrow spike with $(\delta f)/f_{0}\ll 1$", for which "(as far as we are aware) there are no known mechanisms", a possibility the paper neglects (arXiv:0708.2279) [src: Sect. VII, text after Eq. 44]. `[der]` The notation section of arXiv:0708.2279 (Sect. II) does not say whether $h^{2}$ is absorbed in $\Omega_{0}^{\rm gw}$; the bounds below are printed for $\Omega_{\rm gw}h^{2}$.
- The CMB extends the bound to lower frequencies (Smith, Pierpaoli & Kamionkowski 2006, arXiv:astro-ph/0603144). Waves with "frequencies $\gtrsim 10^{-15}$ Hz contribute to the radiation density of the Universe at the time of decoupling", with effects on the CMB and matter power spectra "identical to those due to massless neutrinos, unless the initial density-perturbation amplitude for the gravitational-wave gas is non-adiabatic, as may occur if such GWs are produced during inflation or some post-inflation phase transition"; at 95% confidence level "$\Omega_{\mathrm{gw}}h^{2}\lesssim 6.9\times 10^{-6}$ for homogeneous (i.e., non-adiabatic) initial conditions" [src: abstract, inline], from current CMB, galaxy-survey and Lyman-α data "under the assumption that the number of neutrino degrees of freedom is $N_{\nu}=3.04$ and that neutrino masses are free to vary" [src: text before Fig. 2, inline]. The BBN limit they quote, "the equivalent of 1.4 neutrino degrees of freedom", "translates to a limit to a current CGWB energy density $\Omega_{\mathrm{gw}}h^{2}\lesssim 7.8\times 10^{-6}$", with a lower frequency limit of "$\sim 10^{-10}$ Hz" set by the comoving horizon at BBN [src: second paragraph after the abstract; abstract, inline].
- Planck 2018 (Clarke, Copeland & Moss 2020, arXiv:2004.11396), from TT,TE,EE + lowE + lensing + BAO (BOSS DR12, 6dFGS, SDSS-MGS) [src: Sect. 3], in ΛCDM plus $\Omega_{\rm gw}h^{2}$, 95% upper limits in the shortwave approximation: $\Omega_{\textnormal{gw}}h^{2}<1.7\times 10^{-6}\quad\text{(Shortwave, adiabatic)}\,,$ (arXiv:2004.11396) [src: Eq. 14] and $\Omega_{\textnormal{gw}}h^{2}<2.9\times 10^{-7}\quad\text{(Shortwave, homogeneous)}\,.$ [src: Eq. 15]; "these results, in contrast to the direct reconstruction, are integrated constraints across the range of frequencies" [src: Sect. 4.2]. "Assuming adiabatic initial conditions", the Planck 2018 + BAO value $N_{\textnormal{eff}}=2.99^{+0.34}_{-0.33}$ ($2\sigma$), "using the upper limit, corresponds to" $\Omega_{\textnormal{gw}}h^{2}<1.6\times 10^{-6}$, "(although a proper analysis should use $\Omega_{\textnormal{gw}}h^{2}$ with a prior $\Omega_{\textnormal{gw}}h^{2}\geq 0$)" [src: Sect. 2.2]. Near the horizon at recombination, with second-order back-reaction, $\Omega_{\textnormal{gw}}h^{2}<8.4\times10^{-7}$ without and $<8.6\times10^{-7}$ with neutrino anisotropic stress, "valid for $10^{-15}\,\text{Hz}\gtrsim f\gtrsim 3\times 10^{-16}\,\text{Hz}$" [src: abstract].
- CMB-SPA (Planck, SPT, ACT) with DESI BAO (Wang & Zhao 2025, arXiv:2507.06930), uniform prior $0<\Omega_{\rm gw}h^{2}<4\times 10^{-6}$, 95% CL [src: Sect. 3; Table 2]:

| Model | Initial conditions | $10^{6}\Omega_{\mathrm{gw}}h^{2}$ (uniform prior, Table 2) | $10^{6}\Omega_{\mathrm{gw}}h^{2}$ (log-uniform prior $10^{-12}$–$4\times 10^{-6}$, Table 3) |
|---|---|---|---|
| ΛCDM | adiabatic | <1.04 | <0.28 |
| ΛCDM | homogeneous | <0.27 | <0.07 |
| CPL | adiabatic | <0.72 | <0.13 |
| CPL | homogeneous | <0.24 | <0.06 |

- With a log-uniform prior "these constraints can become tighter by a factor of $\sim4$, suggesting the results to be prior-sensitive" (arXiv:2507.06930) [src: abstract, inline]; they are offered as "critical benchmarks for exploring the cosmological origins of gravitational waves within the frequency band $f \gtrsim 10^{-15}$ Hz" [src: abstract, inline]. Forecast, LiteBIRD & CMB Stage-IV with CSST BAO: 68% CL uncertainties "$σ= 2.5 \times 10^{-7}$ (adiabatic) and $σ= 1.0 \times 10^{-7}$ (homogeneous)" [src: abstract, inline].
- For the PTA band (Ben-Dayan, Kumar & Verma 2025, arXiv:2508.15134): "current NANOGrav 15-year dataset, sensitive up to 60 nHz, gives a negligible contribution to $ΔN_{eff}$"; forecast, for future PTAs "reaching upto 1 $μ$Hz, even with our conservative estimate", inflation, scalar-induced waves and metastable cosmic strings "can induce a $ΔN_{eff}$ large enough for $>3.5σ$ detection by the Simons Observatory" [src: abstract, inline].
- Gauge preheating after axion inflation: "gravitational waves generated by efficient gauge preheating after axion inflation generically contribute significantly to the effective number of relativistic degrees of freedom $N_\mathrm{eff}$", and "with existing Planck limits" they "already place the strongest constraints on the inflaton's possible axial coupling to Abelian gauge fields" (Adshead, Giblin, Pieroni & Weiner 2019, arXiv:1909.12843) [src: abstract]; details in the preheating section below.

## Primordial tensors
<!-- key: primordial-tensors -->

- The vacuum background from slow-roll inflation, for modes entering in radiation domination: $\Omega_{\rm GW}\simeq 5\cdot 10^{-16}\left({H_{k}\over H_{\rm max}}\right)^{2}\,,$ (Caprini & Figueroa 2018, arXiv:1801.04268) [src: Eq. 204], "way below the sensitivity of present and future GW observatories as PTA, LISA, and advanced LIGO/Virgo" [src: Sect. 5.2, text after Eq. 230].
- A stiff epoch lasting "until just before BBN, say with $f_{\rm RD}\sim 10^{-10}$ Hz", with $w\simeq+1$, enhances the spectrum at LISA frequencies by $\sim 10^{7}$, giving $\Omega_{\rm GW}\big|_{\rm stiff}(f\simeq f_{\rm LISA})\sim 5\cdot 10^{-9}$ for inflation saturating the CMB bound (arXiv:1801.04268) [src: Sect. 5.2, inline, text after Eq. 230].
- Changes of $g_*$ in the Standard Model leave features in the spectrum that "must exist", because the calculation is "solely based on the standard model of cosmology and particle physics" (Watanabe & Komatsu 2006, arXiv:astro-ph/0604176) [src: abstract].
- Neutrino free streaming: the squared amplitude is reduced "by 35.6 %" for modes entering in radiation domination (Weinberg 2003, arXiv:astro-ph/0306304) [src: abstract]; the review states "a damping in the GW energy density power spectrum of about ∼35%" for $10^{-17}\,{\rm Hz}\lesssim f\lesssim 10^{-11}$ Hz (arXiv:1801.04268) [src: Sect. 5.2, text after Eq. 235].
- Late-time acceleration: the apparent suppression by $\Omega_{\rm mat}\simeq 0.3$ of modes entering in matter domination "is however a calculation artefact", and the $k^4$ claim for modes entering after the onset of acceleration "must be therefore considered only as indicative" (arXiv:1801.04268) [src: Sect. 5.2, text after Eq. 231].
- One-loop corrections from a non-canonical spectator field: an "$\mathcal{O}(1)$ correction to $r_{\mathrm{eff}}$" for a Gaussian dip in the coupling and an enhancement "by several orders of magnitude" for an oscillatory coupling (Li, Yuan & Huang 2026, arXiv:2601.08675) [src: abstract].

## Sources beyond vacuum fluctuations
<!-- key: sources-beyond-vacuum-fluctuations -->

- Gauge-field production by an axion inflaton gives a chiral background, $\mathcal{P}_{h,-}^{\rm(pp)}\simeq 2.1\cdot 10^{-3}\mathcal{P}_{h,+}^{\rm(pp)}$ (arXiv:1801.04268) [src: Sect. 6.1.2, inline, text after Eq. 241], and a one-to-one relation between the tensor power spectrum and the equilateral tensor bispectrum [src: Sect. 6.1.2, text after Eq. 241]. <!-- num: not a value -->
- Planck non-Gaussianity limits the coupling at CMB scales to $\xi\lesssim 2.5$ at 95% C.L. (as quoted in arXiv:1801.04268) [src: Sect. 6.1.2, text after Eq. 239]; a detectable signal requires amplification "at a level that induces significant backreaction" (arXiv:2510.17207) [src: abstract], and in pure Abelian axion inflation signals within reach of future interferometers come only with "strong backreaction" (arXiv:2508.00798) [src: abstract].
- The GW peak of preheating by parametric resonance decreases with the resonance parameter, and sits near $10^{8}$ Hz for $\frac{1}{2}m^2\phi^2$ preheating (arXiv:1801.04268) [src: Sect. 7.1, text after Eq. 298; Eq. 299]. <!-- num: not a value -->
- The peak amplitude at the end of production carries the power $q^{-\frac{1}{2}+\delta}$ of the resonance parameter (Figueroa & Torrenti 2017, arXiv:1707.04533) [src: Eq. 41]; their lattice signal "can be rather large, as $h^2Ω_{\rm GW}(f_p) \lesssim 10^{-11}$, but it is always peaked at high frequencies $f_p \gtrsim 10^{7}$ Hz" [src: abstract]. <!-- num: not a value -->
- For preheating after chaotic inflation, frequency and amplitude of the peak "depend in a relatively simple way on the characteristic spatial scale amplified during preheating" (Dufaux et al. 2007, arXiv:0707.0875) [src: abstract]; for tachyonic preheating after hybrid inflation, in what the paper calls "preliminary estimates" [src: Sect. VII], the peak "may fall into the range accessible to interferometric direct detection experiments, $f_{*}<10^{2}\,\mathrm{Hz}$, only for extremely small values of the coupling constant, $\lambda<10^{-28}$", for the overshooting trajectory of their Eq. 83 [src: Sect. VII, text after Eq. 86]; the other trajectory they consider "generally leads to higher amplitude and smaller frequency" and needs $\lambda<2\times 10^{-11}$ [src: Sect. VII, text after Eq. 90].
- "Typically, $\beta=\mathcal{O}(10^{-2}-10^{-3})$", so that for efficient preheating after GUT-scale inflation the peak lies at "$f_{0}\sim 10^{10}-10^{11}\,\rm{Hz}$", above "the highest frequency ranges $10^{3}-10^{4}\,\rm{Hz}$ of planned gravitational wave detectors" (Lozanov 2019, arXiv:1907.04402) [src: Sect. 8.3.1, text after Eq. 110].
- Gauge preheating: the waves "already place the strongest constraints on the inflaton's possible axial coupling to Abelian gauge fields" through $N_{\rm eff}$ with existing Planck limits (arXiv:1909.12843) [src: abstract]; for axial coupling the background is "helically polarized" (arXiv:1805.04550) [src: abstract].
- Oscillons: an isolated one "does not radiate gravitational waves" (arXiv:1304.6094) [src: abstract]; the "dominant, growing high frequency peak" reported for the fiducial asymmetric "hill-top model" "is a numerical artifact" (arXiv:1803.08047) [src: abstract]; the induced waves from the decay of an oscillon-dominated phase "can saturate" the $N_{\rm eff}$ bound (arXiv:2601.11360) [src: abstract].

## Phase-transition spectra
<!-- key: phase-transition-spectra -->

- Causality: a source at $t_p$ "cannot be correlated on length/time scales larger than $H_{p}^{-1}$", so the peak "certainly satisfies $x_{k}\geq 1$" (Caprini & Figueroa 2018, arXiv:1801.04268) [src: Sect. 3.3, inline, text after Eq. 103], and super-horizon scales at the transition scale as $f^3$ "because the source is uncorrelated" (Caprini et al. 2024, arXiv:2403.03723) [src: Sect. 2.1, text after Eq. 7]. <!-- num: not a value -->
- "If the coupling between the bubble walls and plasma particles is large enough, the latent heat is transferred also to the bulk motion of the fluid" (Caprini et al. 2024, arXiv:2403.03723) [src: Sect. 2.2.1].
- The sound-wave amplitude scales as $K^2 H_*R_*$ for a source lasting a Hubble time and as $K^{3/2}(H_*R_*)^2$ when shocks form within one (Caprini et al. 2019, arXiv:1910.13125) [src: Eqs. 25–26]. <!-- num: not a value -->
- Kinetic-energy deficit in strong deflagrations: "in the most extreme case by a factor of $10^{3}$" overestimate of the signal by current modelling (Cutting, Hindmarsh & Weir 2019, arXiv:1906.00480) [src: abstract].
- Expanding-universe simulations of slow strong transitions find a normalised amplitude "of order $\mathcal{O}(10^{-2})$, in alignment with Minkowski-spacetime results", sound-wave spectra with "two peaks located at the mean bubble separation and the sound-shell width", spectra that "differ markedly" from Minkowski ones, and an effective sound-wave lifetime that "increases for slower PTs, decreasing for faster PT with larger $\beta/H$ and rising with smaller $\alpha$" (Zou et al. 2026, arXiv:2610.14806) [src: abstract].
- Theory error from the thermal potential: "two to three orders-of-magnitude uncertainty in the peak gravitational wave amplitude" in the daisy-resummed approach (Croon et al. 2020, arXiv:2009.10080) [src: abstract].

## Defect spectra
<!-- key: defect-spectra -->

- A long-string network produces loops at a rate "of the order of few$\times 10$ larger than the Hubble rate" (Caprini & Figueroa 2018, arXiv:1801.04268) [src: Sect. 9.2, text after Eq. 379].
- Field-theory loops decaying within a Hubble time "emit much less gravitational radiation than in the Nambu-Goto scenario" (Hindmarsh et al. 2017, arXiv:1703.06696) [src: abstract].
- NANOGrav 15-year: "with the exception of stable cosmic strings of field theory origin", all the cosmological models tested "can reproduce the observed signal" (arXiv:2306.16219) [src: abstract].
- Multi-band (NANOGrav, EPTA, LVK) inference with four loop-distribution models leaves one model able to explain the PTA common signal (Zhang et al. 2026, arXiv:2610.02590) [src: abstract].

## Scalar-induced waves
<!-- key: scalar-induced-waves -->

- "The spectrum is scale-invariant on small scales", and the induced contribution "can be computed directly from the observed scalar perturbations and general relativity" (Baumann et al. 2007, arXiv:hep-th/0703290) [src: abstract].
- The infrared tail goes as $k^3$ for modes entering in radiation domination and as $k^{3-2\lvert b\rvert}$ in an intermediate range for a constant-$w$ epoch (Domènech 2021, arXiv:2109.01398) [src: Eqs. 2.22–2.23]; the scaling survives higher orders and non-Gaussianity (Yuan 2026, arXiv:2609.17928) [src: abstract]. <!-- num: not a value -->
- Synchronous and Newtonian gauges, properly fixed, give the same induced spectrum in radiation domination and for any constant equation of state other than dust (arXiv:2109.01398) [src: Sect. 7.2, text after Eq. 7.11]. <!-- num: not a value -->
- In an early matter era driven by PBHs, the no-backreaction requirement at third order gives $Ω_{\mathrm{PBH},f}\lesssim4.6\times10^{-7}\, (m_{\mathrm{PBH}}/10^{7}\,\mathrm{g})^{-0.48}$ (Zhou 2026, arXiv:2610.08045) [src: abstract].

## Propagation
<!-- key: propagation -->

- Modified GW propagation "dominates over that of $w_{\rm DE}(z)$" for standard sirens in generic modified-gravity models, "even in theories where the speed of gravity is equal to $c$" (Belgacem et al. 2018, arXiv:1805.08731) [src: abstract].
- A weakly modelled reconstruction of $d_L^{\rm GW}/d_L^{\rm EM}$ applied "to GWTC-5 data" finds "no deviations from GR"; "O5-like GW data will not resolve deviations from GR smaller than 30%", while third-generation detectors "can confidently detect deviations of order 5% to 3$σ$ significance" (forecast, Colangeli et al. 2026, arXiv:2608.18310) [src: abstract].
- Neutrino free streaming reduces the squared tensor amplitude "by 35.6 % for wavelengths that enter the horizon during the radiation-dominated phase, independent of any cosmological parameters" (Weinberg 2003, arXiv:astro-ph/0306304) [src: abstract]; "At the longest wavelengths the decrease in the tensor correlation functions due to neutrino free streaming ranges from 10.7% for Ω_M h^2 = 0.1 to 9.0% for Ω_M h^2 = 0.15" [src: abstract].
- The speed-of-tensors bound and what it implies for theories: `thcosmo-modified-gravity`, `results.md` and `deep/speed-of-tensors-constraints.md`.

## History of key results
<!-- key: history-of-key-results -->

| Year | Result | Paper and place | Status |
|---|---|---|---|
| 1997 | GWs from the classical waves of preheating | Khlebnikov & Tkachev, arXiv:hep-ph/9701423 [src: abstract] | current as mechanism; amplitudes now from lattice runs "for a wide range of $q$" (arXiv:1707.04533) [src: abstract] |
| 2003 | Neutrino free streaming reduces the squared tensor amplitude by 35.6 % | Weinberg, arXiv:astro-ph/0306304 [src: abstract] | current |
| 2006 | Standard-Model $g_*$ features in the inflationary spectrum | Watanabe & Komatsu, arXiv:astro-ph/0604176 [src: abstract] | current |
| 2006 | CMB bound on the integrated background, homogeneous initial conditions | Smith et al., arXiv:astro-ph/0603144 [src: abstract] | superseded by Planck 2018 (arXiv:2004.11396) [src: Eqs. 14–15] and CMB-SPA + DESI (arXiv:2507.06930) [src: Table 2]; its homogeneous mode revised (arXiv:2004.11396) [src: Sect. 4.1] |
| 2007 | Preheating GWs: no-go theorem, peak set by $k_*$; $\Omega_{\rm gw}\propto\lambda/g^{2}$ not observed | Dufaux et al., arXiv:0707.0875 [src: Sect. II.2; Sect. VI.2, inline] | current |
| 2007 | Scalar-induced background over all scales | Ananda et al., arXiv:gr-qc/0612013; Baumann et al., arXiv:hep-th/0703290 [src: abstract] | current; gauge question refined (arXiv:2109.01398) [src: Sect. 7.2] |
| 2010 | Energy budget κ of bubble growth in all regimes | Espinosa et al., arXiv:1004.4187 [src: abstract] | current; corrected by a factor 0.6 for bulk flow in the 2024 template (arXiv:2403.03723) [src: Sect. 2.2.1, text after Eq. 11] |
| 2011 | Chiral tensors from a pseudoscalar inflaton | Sorbo, arXiv:1101.1525 [src: abstract] | current; backreaction regime disputed (arXiv:2411.16368; arXiv:2510.17207) [src: abstract] |
| 2011 | Continuum and lattice TT projections give spectra that "only differ marginally" | Figueroa et al., arXiv:1110.0337 [src: abstract] | current |
| 2017 | Preheating peak amplitude with the power $q^{-\frac{1}{2}+\delta}$ of the resonance parameter, and fitted peaks | Figueroa & Torrenti, arXiv:1707.04533 [src: Eq. 41; Sect. 5] | current |
| 2017 | Oscillons in asymmetric potentials: a peak exceeding linear preheating | Antusch et al., arXiv:1607.01314 [src: abstract] | the "dominant, growing high frequency peak" of its fiducial "hill-top model" called "a numerical artifact" (arXiv:1803.08047) [src: abstract] |
| 2017 | Field-theory string loops decay within a Hubble time | Hindmarsh et al., arXiv:1703.06696 [src: abstract] | disputed by the Nambu–Goto loop picture (arXiv:1309.6637) [src: abstract] |
| 2019 | Sound-wave template with the shock-time reduction, Eq. 32 | Caprini et al., arXiv:1910.13125 [src: Eq. 32] | superseded by the double broken power law of arXiv:2403.03723 [src: Eq. 8] |
| 2019 | Gauge preheating waves "generically contribute significantly" to $N_{\rm eff}$; with Planck, "the strongest constraints" on the axial coupling | Adshead et al., arXiv:1909.12843 [src: abstract] | current |
| 2020 | Planck 2018 shortwave bounds, adiabatic and homogeneous | Clarke et al., arXiv:2004.11396 [src: Eqs. 14–15] | superseded in data by arXiv:2507.06930 [src: Table 2] |
| 2019 | Strong deflagrations overestimated by up to $10^{3}$ | Cutting et al., arXiv:1906.00480 [src: abstract] | current |
| 2023 | NANOGrav 15-year: cosmological models fit; stable field-theory strings do not | arXiv:2306.16219 [src: abstract] | current; "should not be regarded as evidence for new physics" [src: abstract] |
| 2024 | "the collided part of the bubble walls has recently been found to be essential for a correct estimation of the SGWB spectrum", against the envelope approximation | Caprini et al., arXiv:2403.03723 [src: Sect. 2.1, text after Eq. 6] | current |
| 2026 | Expanding-universe PT amplitudes of the Minkowski order, with spectra of a different shape (version 2; version 1 had reported amplitudes an order of magnitude lower) | Zou et al., arXiv:2610.14806 [src: abstract] | new, not yet confirmed among the sources read |

## Not verified
<!-- key: not-verified -->

- The current measured bounds on r and on PTA amplitudes were not read; they belong to cosmoskill. The measured $N_{\rm eff}$ itself is in `thcosmo-neutrinos-light-relics`; only the GW-specific CMB analyses above were read.
- The 2012 WMAP7 update (Sendra & Smith) and the Planck 2015 analysis cited by arXiv:2004.11396 [src: Sect. 2.2] were not read; their values are quoted there only.
- The consistency relation n_T = −r/8 beyond single-field slow roll was not checked.
