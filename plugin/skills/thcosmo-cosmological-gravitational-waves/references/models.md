# Models of cosmological gravitational-wave sources

Scope: the source landscape of cosmological stochastic gravitational-wave backgrounds, one card per model or class, chosen by literature weight in the reviews of Caprini & Figueroa (arXiv:1801.04268), Roshan & White (arXiv:2401.04388) and Domènech (arXiv:2109.01398) and in the 2025–2026 literature; formalism in `formalism.md`, model-independent results in `results.md`. The dynamics of the transitions and the evolution of defect networks belong to `thcosmo-baryogenesis-phase-transitions` and `thcosmo-pbh-defects` (both planned); measured backgrounds belong to cosmoskill `cosmo-early-universe-exotica`.

Snapshot: 2026-11-12

## Inflationary sources
<!-- key: inflationary-sources -->

### Single-field slow-roll inflation (irreducible background)
<!-- key: single-field-slow-roll-inflation-irreducible -->
- **Defining equations:** $\mathcal{P}_{h}(k)\simeq~\frac{2}{\pi^{2}}\,\frac{H_{k}^{2}}{m_{\mathrm{Pl}}^{2}}\,~,\hskip 14.22636pt\mbox{ for }\hskip 14.22636ptk=a_{k}H_{k}\,.$ (Caprini & Figueroa 2018, arXiv:1801.04268) [src: Eq. 195]; formalism in `formalism.md`.
- **Parameters:** $H$ at horizon exit (or $r$) and $\epsilon$.
- **Predictions:** red tilt with $n_{T}(k)=-\frac{r_{k}}{8}\,.$ (arXiv:1801.04268) [src: Eq. 203]; $\Omega_{\rm GW}\simeq 5\cdot 10^{-16}\left({H_{k}\over H_{\rm max}}\right)^{2}\,,$ [src: Eq. 204] for modes entering in radiation domination, with $H_{\rm max}\simeq 9\cdot 10^{13}$ GeV from the CMB [src: Sect. 5.2, text after Eq. 230]; the amplitude is "too small" to expect detection with "aLIGO/Virgo, LISA, ET and others", while "futuristic GW detectors such as BBO may perhaps have a chance" "If the energy scale of inflation is sufficiently high" [src: Sect. 5, introduction].
  - A one-loop calculation with a non-canonical spectator field finds "a $\mathcal{O}(1)$ correction to $r_{\mathrm{eff}}$" for a localized Gaussian dip in the coupling, and an enhancement "by several orders of magnitude" for a rapidly oscillatory coupling (Li, Yuan & Huang 2026, arXiv:2601.08675) [src: abstract].
- **Consistency:** none found among the sources read.
- **Observational status:** only the CMB B-mode bound on $r$ applies; its value is in cosmoskill `cosmo-cmb` and `cosmo-inflation-primordial`, and the model building in `thcosmo-inflation`.
- **Status date:** 2026-11-05

### Axion inflation with gauge-field production
<!-- key: axion-inflation-with-gauge-field-production -->
- **Defining equations:** $\Delta{\cal L}=-\frac{1}{4\,\Lambda}\,\phi\,F_{\mu\nu}\,\tilde{F}^{\mu\nu}\,,$ (arXiv:1801.04268) [src: Eq. 238], with ξ defined in Eq. 239 of the same review.
  - Introduced as a GW source in Sorbo 2011 (arXiv:1101.1525), whose tensor modes are chiral and give "non-vanishing TB and EB correlation functions" in the CMB [src: abstract].
- **Parameters:** $\Lambda$ (or the axion decay constant), the potential, which fixes the growth of $\xi$.
- **Predictions:** a blue, chiral, non-Gaussian tensor background, $h^{2}\Omega_{\rm GW}^{\rm(pp)}\simeq 1.5\cdot 10^{-13}(H/m_{\rm Pl})^{4}(e^{4\pi\xi}/{\xi^{6}})$ for $\xi>1$ (arXiv:1801.04268) [src: Sect. 6.1.2, inline, text after Eq. 241]; LISA probes "e.g. $\xi\gtrsim 3.5$" [src: Sect. 6.1.2, text after Fig. 5].
  - "For an axion decay constant < 10^{-2} M_p", gauge-quanta production "typically dominates over the standard fluctuations from the vacuum, and saturates the current observational bounds on nongaussianity" (Barnaby & Peloso 2011, arXiv:1011.1500) [src: abstract].
- **Consistency:** a detectable signal needs gauge-field amplification "at a level that induces significant backreaction" (Barbon, Ijaz & Peloso 2025, arXiv:2510.17207) [src: abstract]. Lattice simulations show that the homogeneous-backreaction approximation "fails to accurately describe the truly local dynamics of strong backreaction" (Figueroa et al. 2024, arXiv:2411.16368) [src: abstract]; inhomogeneity attenuates the inflaton-velocity oscillations and smooths out the oscillatory features of the gauge spectrum (Figueroa et al. 2023, arXiv:2303.17436) [src: abstract]. Reply: within homogeneous backreaction, examples exist "with a detectable SGWB and with an inflaton gradient energy that remains subdominant to the inflaton zero-mode kinetic energy throughout inflation" (arXiv:2510.17207) [src: abstract].
- **Observational status:** in pure Abelian axion inflation with a quadratic potential near the minimum, signals "within the reach of future GW interferometers can only be realized in parameter regions that also lead to strong backreaction and that are in conflict with the upper limit on $\Delta N_{\rm eff}$" (von Eckardstein, Schmitz & Sobol 2025, arXiv:2508.00798) [src: abstract]; $\xi\lesssim 2.5$ at 95% C.L. at CMB scales from Planck non-Gaussianity (as quoted in arXiv:1801.04268) [src: Sect. 6.1.2, text after Eq. 239].
- **Status date:** 2026-11-05

## Post-inflationary sources
<!-- key: post-inflationary-sources -->

### Preheating by parametric resonance
<!-- key: preheating-by-parametric-resonance -->
- **Defining equations:** a daughter field coupled as $g^2\phi^2X^2$, Eqs. 283 and 287–288 of Caprini & Figueroa 2018 (arXiv:1801.04268), in `formalism.md`. <!-- num: not a value -->
- **Parameters:** resonance parameter $q_{\rm i}$, inflaton mass or self-coupling, equation of state $w$ after production.
- **Predictions:** one peak at $f_{p}=\epsilon_{\rm f}^{1/4}\left(\frac{q_{\rm i}}{10^{4}}\right)^{0.67}\times 2.0\cdot 10^{8}\ {\rm Hz}\,,$ for $\frac{1}{2}m^2\phi^2$ preheating (arXiv:1801.04268) [src: Eq. 299]; the peak amplitude decreases with $q_{\rm i}$ [src: Sect. 7.1, text after Eq. 298].
  - With a localised one-loop Coleman–Weinberg correction to an α-attractor T-model, self-resonance gives a peaked spectrum, or "a smooth and enhanced spectrum" if the quadratic term turns negative; the signals "lie in the ultra-high-frequency regime at frequencies above the kHz range" (Inada et al. 2026, arXiv:2607.18381) [src: abstract].
  - Foundation: waves are "produced quite efficiently in interactions of classical waves created by resonant decay of a coherently oscillating field"; for simple chaotic models with a second scalar, today's ratio "can be as large as $10^{-12}$ at the maximal wavelength of order $10^{5}$ cm" (Khlebnikov & Tkachev 1997, arXiv:hep-ph/9701423) [src: abstract].
  - Fits from expanding-lattice simulations over a wide range of $q$ (Figueroa & Torrenti 2017, arXiv:1707.04533). For $V=\frac{1}{4}\lambda\phi^{4}$, $q\equiv g^{2}/\lambda$, $\lambda=9\cdot 10^{-14}$ and $q>1$, peaks at $f_{1}\approx 1.5\cdot 10^{7}\ {\rm Hz}\ ,$ [src: Eq. 102] and $f_{2}\approx 2.8\cdot 10^{7}\ {\rm Hz}\ ,$ [src: Eq. 103] with $3.4\cdot 10^{-12}\left(\frac{q}{100}\right)^{-0.42}\lesssim h^{2}\Omega_{\rm GW}(f_{1,2})\lesssim 2.4\cdot 10^{-11}\left(\frac{q}{100}\right)^{-0.56}\ ,$ [src: Eq. 105]. For $V=\frac{1}{2}m^{2}\phi^{2}$, $q\equiv g^{2}\phi_{\rm i}^{2}/(4m^{2})$, one peak, $f_{p}=\epsilon_{\rm f}^{1/4}\left(\frac{q}{10^{4}}\right)^{0.67}\times 2.0\cdot 10^{8}\ {\rm Hz}\,,$ [src: Eq. 107] and $h^{2}\Omega_{\rm GW}(f_{p})=\epsilon_{\rm f}\left(\frac{q}{10^{4}}\right)^{-0.43}\times 1.5\cdot 10^{-11}\ ,\hskip 8.5359pt(q\gtrsim 6\cdot 10^{3})\ ,$ [src: Eq. 108], with $\epsilon_{\rm f}\equiv(a_{\rm f}/a_{{}_{\rm RD}})^{1-3w}$ "the unknown period (with equation of state $w$) between the end of GW production and the onset of a RD universe" [src: Sect. 5, text after Eq. 108]. Spectator fields give a background that is "very subdominant with respect the background expected from preheating" [src: Sect. 5].
  - For $\lambda\phi^4$ with $q=1.2$, $120$, $128$ and $1130$ on $256^{3}$ lattices, the largest peak observed was "for $q=1.2$", with "a peak amplitude of $h^{2}\,\Omega_{\mathrm{gw}}\sim 5\times 10^{-10}$ at a frequency of order $5\times 10^{6}\,\mathrm{Hz}$" (Dufaux et al. 2007, arXiv:0707.0875) [src: Sect. VI.2, inline].
- **Consistency:** the earlier scaling $\Omega_{\mathrm{gw}}\propto\lambda/g^{2}$ is not seen on the lattice: "we don't observe the dependence in $\Omega_{\mathrm{gw}}\propto\lambda/g^{2}$ derived in [18] and quoted in [19]"; "the peak amplitude in gravitational waves depends only mildly on the value of $q$ for the cases that we considered" (arXiv:0707.0875) [src: Sect. VI.2, inline]. A quantum in-in calculation, which numerically estimates the density "in a simple scalar field model, neglecting backreaction", finds that "In the cases in which parametric resonance is effective, our results agree with the predictions expected from numerical simulations, as anticipated", but "At sufficiently low values of the resonance parameter, however, numerical simulations fail, while our approach remains applicable" (Armendariz-Picon 2019, arXiv:1905.05724) [src: abstract]. The lattice TT-projection objection was answered in arXiv:1110.0337 [src: abstract] (`formalism.md#preheating-and-non-perturbative-sources`). <!-- num: not a value -->
- **Observational status:** "The GW signal can be rather large, as $h^2Ω_{\rm GW}(f_p) \lesssim 10^{-11}$, but it is always peaked at high frequencies $f_p \gtrsim 10^{7}$ Hz" (arXiv:1707.04533) [src: abstract]; no detector band reaches the predicted frequencies; the review's band list stops at $10^{3}$ Hz for ground-based interferometers (arXiv:1801.04268) [src: Fig. 1 caption]. The integrated amplitude is bounded by $\Delta N_{\rm eff}$ (`results.md#integrated-bound-from-extra-radiation`).
- **Status date:** 2026-11-12

### Gauge preheating (Abelian, dilatonic or axial coupling)
<!-- key: gauge-preheating-abelian-dilatonic-or-axial -->
- **Defining equations:** scalar and pseudoscalar inflatons "coupled directly to Abelian gauge fields via either a dilatonic coupling to the gauge-field kinetic term or an axial coupling to a Chern-Simons term" (Adshead, Giblin & Weiner 2018, arXiv:1805.04550) [src: abstract]; `[der]` the axial coupling has the form of Eq. 238 of arXiv:1801.04268 (`formalism.md#inflationary-sources-beyond-vacuum-fluctuations`). <!-- num: not a value -->
- **Parameters:** the energy scale and the shape of the inflaton potential (Adshead, Giblin, Pieroni & Weiner 2019, arXiv:1909.12842) [src: abstract], and the axion–gauge coupling, written $\alpha/f$ in arXiv:1909.12843 [src: text after Fig. 1]. <!-- num: not a value -->
- **Predictions:** "gravitational waves are produced efficiently during the preheating phase, with a signature louder than most cosmological signals", and "For axially coupled fields the resulting gravitational wave spectrum is helically polarized" (arXiv:1805.04550) [src: abstract]. Preheating into Abelian gauge fields "generically leads to a large gravitational wave background that contributes significantly" to $N_\mathrm{eff}$, with an efficiency "correlated with the tensor-to-scalar ratio, $r$" (arXiv:1909.12842) [src: abstract]. For preheating backgrounds in general, "unless the inflationary scale is especially low, this stochastic gravitational wave background would reside at high frequencies (typically $10^{6}\lesssim f\lesssim 10^{9}$)", the range printed without a unit (arXiv:1909.12843) [src: second paragraph of the text, inline].
- **Consistency:** none found among the sources read.
- **Observational status:** "with existing Planck limits, gravitational waves from preheating already place the strongest constraints on the inflaton's possible axial coupling to Abelian gauge fields" (arXiv:1909.12843) [src: abstract]. Forecast: "for inflationary potentials whose tensor-to-scalar ratios would be observable by CMB-S4 experiments, the entire regime of efficient gauge preheating ($\gtrsim 80$ % efficiency) will be probed via the contribution of gravitational waves to $\Delta N_{\mathrm{eff}}$" [src: text after Fig. 1].
- **Status date:** 2026-11-12

### Oscillon formation and oscillon domination
<!-- key: oscillon-formation-and-oscillon-domination -->
- **Defining equations:** none in closed form; oscillons are "long-lived, localized excitations of nonlinear scalar fields which may be copiously produced during preheating after inflation", for example after axion monodromy inflation (Zhou et al. 2013, arXiv:1304.6094) [src: abstract], and in "field potentials that are asymmetric around the minimum" (Antusch, Cefala & Orani 2017, arXiv:1607.01314) [src: abstract].
- **Parameters:** the inflaton mass and its cubic and quartic self-couplings (Lozanov, Sasaki & Tränkle 2026, arXiv:2601.11360) [src: abstract].
- **Predictions:** "An isolated oscillon is spherically symmetric and does not radiate gravitational waves", the flux "generated between oscillons is also small", and "a significant stochastic gravitational wave background may be generated during preheating itself (i.e, when oscillons are forming)", with the oscillon size imprinted as "multiple, distinct peaks" (arXiv:1304.6094) [src: abstract]. For asymmetric potentials "associated with a phase transition" oscillons "can generate a pronounced peak in the spectrum of gravitational waves, that largely exceeds the linear preheating spectrum" (arXiv:1607.01314) [src: abstract]. "Under certain conditions" the inflaton condensate fragments into oscillons, which "can dominate the Universe for several $e$-folds of expansion", and their "rapid final decay" gives induced waves "whose energy density can saturate the observational bound on the effective number of relativistic species" (arXiv:2601.11360) [src: abstract].
- **Consistency:** a GPU convergence study finds that "the dominant, growing high frequency peak of the gravitational wave signals in the fiducial 'hill-top model' in [arXiv:1607.01314] is a numerical artifact", numerical errors being "significant in low-resolution scenarios, or in scenarios where the run-time causes the resolution to drop below the relevant scales in the problem" (Amin et al. 2018, arXiv:1803.08047) [src: abstract]. No reply was read.
- **Observational status:** the $\Delta N_{\rm eff}$ bound constrains the inflaton mass, cubic and quartic couplings "in generic models that admit oscillon formation", "in regions of parameter space that are inaccessible with cosmic microwave background observations alone" (arXiv:2601.11360) [src: abstract].
- **Status date:** 2026-11-12

## Phase transitions
<!-- key: phase-transitions -->

### Thermal first-order phase transition with sound waves (weak to intermediate strength)
<!-- key: thermal-first-order-phase-transition-with-sound -->
- **Defining equations:** the parameters $\alpha$, $\beta/H_*$, $v_{\rm w}$, $T_*$ and the sound-wave templates, Eqs. 1–32 of Caprini et al. 2019 (arXiv:1910.13125) and Eqs. 8–12 of Caprini et al. 2024 (arXiv:2403.03723), in `formalism.md`. <!-- num: not a value -->
- **Parameters:** $K$ (from $\alpha$ and $\kappa$), $H_*R_*$ (from $\beta/H_*$ and $v_{\rm w}$), $\xi_w$, $T_*$ (arXiv:2403.03723) [src: Sect. 2.2.1, text after Eq. 12].
- **Predictions:** a double broken power law with slopes 3, 1, −3 and breaks at the bubble size and the sound-shell thickness (arXiv:2403.03723) [src: Table 1; Eq. 9]. In the 2026 expanding-universe lattice simulations of slow, strong transitions, sound waves "significantly" dominate over bubble collisions, the sound-wave spectra show "two peaks located at the mean bubble separation and the sound-shell width", and the normalised amplitude is "of order $\mathcal{O}(10^{-2})$, in alignment with Minkowski-spacetime results", while the spectra "differ markedly from those scenarios" (Zou et al. 2026, arXiv:2610.14806) [src: abstract].
- **Consistency:** for strong deflagrations, "Current modelling therefore substantially overestimates the gravitational wave signal for strong transitions with deflagrations, in the most extreme case by a factor of $10^{3}$. Detonations are less affected." (Cutting, Hindmarsh & Weir 2019, arXiv:1906.00480) [src: abstract]. Perturbative thermal calculations in the daisy-resummed approach carry "two to three orders-of-magnitude uncertainty in the peak gravitational wave amplitude", which dimensional reduction "drastically reduces" (Croon et al. 2020, arXiv:2009.10080) [src: abstract]. Reply: the 2024 template adopts $K\simeq 0.6\,\kappa\,\alpha/(1+\alpha)$, "a conservative estimate" relative to the 2019 report, and cuts the source at the shock time (arXiv:2403.03723) [src: Sect. 2.2.1, inline, text after Eq. 11]; whether this covers the strong-deflagration deficit is not stated among the sources read.
- **Observational status:** a forecast target for LISA; LISA would reconstruct a region of parameter space "with better than ∼10 % accuracy, if certain experimental and theoretical uncertainties are solved by the time LISA flies" (forecast, arXiv:2403.03723) [src: abstract]. The Standard-Model electroweak and QCD transitions are not first order; model status is in `thcosmo-baryogenesis-phase-transitions` (planned).
- **Status date:** 2026-11-05

### Strongly supercooled transition (bubble collisions, relativistic fluid shells)
<!-- key: strongly-supercooled-transition-bubble -->
- **Defining equations:** Template I of Caprini et al. 2024 (arXiv:2403.03723), Eqs. 4 and 7, in `formalism.md`. <!-- num: not a value -->
- **Parameters:** $\tilde{K}\equiv\alpha/(1+\alpha)$, $\beta/H_*$, $T_*$ (arXiv:2403.03723) [src: Sect. 2.1, text after Eq. 7].
- **Predictions:** $\Omega_{p}\propto(H_{*}/\beta)^{2}$ for bubble collisions, against $\Omega_{\mathrm{int}}\propto(H_{*}R_{*})\propto(H_{*}/\beta)$ for sound waves lasting about a Hubble time (arXiv:2403.03723) [src: Sect. 2.2.1, text after Eq. 11].
- **Consistency:** "the strongly supercooled and ultraslow transition regime" is where "conventional approximations break down and the most promising GW signals are expected"; TransitionListener v2.0 treats the true-vacuum fraction, its backreaction on the expansion and reheating during percolation self-consistently (Matuszak & Tasillo 2026, arXiv:2605.15259) [src: abstract]. In most strong transitions the runaway regime "will modify expectations for the gravity wave signal" (Espinosa et al. 2010, arXiv:1004.4187) [src: abstract].
- **Observational status:** see the PTA discussion in `open-questions.md`; measured values in cosmoskill `cosmo-early-universe-exotica`.
- **Status date:** 2026-11-05

## Topological defects
<!-- key: topological-defects -->

### Cosmic strings (Nambu–Goto loops)
<!-- key: cosmic-strings-nambu-goto-loops -->
- **Defining equations:** loop number density and spectrum, Eqs. 379–383 of Caprini & Figueroa 2018 (arXiv:1801.04268), in `formalism.md`. <!-- num: not a value -->
- **Parameters:** $G\mu$, loop size at birth α, spectral index q, cut-off $n_*$, intercommutation probability p (arXiv:1801.04268) [src: Sect. 9.2]; in multi-band analyses also the average cusp and kink numbers (arXiv:2610.02590) [src: abstract].
- **Predictions:** a broad spectrum with a scale-invariant plateau (arXiv:2610.02590) [src: abstract]; the high-frequency tail of loops formed before BBN "can deviate from its usual flat shape" if the expansion was not radiation dominated (arXiv:1801.04268) [src: Sect. 9.2.1].
- **Consistency:** Abelian-Higgs simulations find loops decaying "by the emission of massive radiation within a Hubble time", which makes them "subject to much weaker gravitational wave constraints on their tension" (Hindmarsh et al. 2017, arXiv:1703.06696) [src: abstract]. Reply: the loop number density "can be accurately predicted using recently acquired detailed knowledge of the loop production function" from Nambu–Goto simulations (Blanco-Pillado, Olum & Shlaer 2013, arXiv:1309.6637) [src: abstract].
- **Observational status:** "with the exception of stable cosmic strings of field theory origin", all cosmological models tested "can reproduce the observed signal" of NANOGrav 15-year (NANOGrav, arXiv:2306.16219) [src: abstract]; "the stringent LVK bounds preclude three of these models from explaining the observed PTA common signal" among four loop-distribution models (Zhang et al. 2026, arXiv:2610.02590) [src: abstract]. Earlier PTA bounds: Gμ ≤ 2.8×10^-9 (arXiv:1309.6637) [src: abstract]; the review gives (arXiv:1801.04268) $G\mu<5.3\times 10^{-7}\,,$ [src: Eq. 384], a 95% bound "for the specific set of parameters", and, for large loops, a constraint "of the order of $G\mu\lesssim 10^{-10}-10^{-11}$, depending on the details" [src: Sect. 9.2.1, inline, text after Eq. 384]. Measured backgrounds: cosmoskill `cosmo-early-universe-exotica`.
- **Status date:** 2026-11-05

### Domain walls with biased annihilation
<!-- key: domain-walls-with-biased-annihilation -->
- **Defining equations:** Eqs. 114–124 of Roshan & White 2024 (arXiv:2401.04388), in `formalism.md`. <!-- num: not a value -->
- **Parameters:** tension σ, bias $V_{\rm bias}$ (potential bias) or $\mathcal{B}_s$ (population bias) (arXiv:2607.18107) [src: abstract].
- **Predictions:** a peaked spectrum set by the annihilation time; lattice spectra for both bias mechanisms "that Pulsar Timing Arrays (PTAs) and ground-based interferometers (LIGO-Virgo-KAGRA) can readily use" (Barbini et al. 2026, arXiv:2607.18107) [src: abstract].
- **Consistency:** a stable network would dominate; "a very large energy difference from the beginning will not allow the formation of DWs at the first place" (arXiv:2401.04388) [src: Sect. IV.2, text after Eq. 120]; the Zel'dovich–Kobzarev–Okun bound applies to surface energy density above $\mathcal{O}(\text{MeV}^{3})$ [src: Sect. IV.2, text after Eq. 120]. The 2026 lattice study states that it clarifies "existing disagreements in the recent literature" (arXiv:2607.18107) [src: abstract].
- **Observational status:** can reproduce the NANOGrav 15-year signal (arXiv:2306.16219) [src: abstract].
- **Status date:** 2026-11-05

## Scalar-induced sources
<!-- key: scalar-induced-sources -->

### Scalar-induced waves from an enhanced small-scale curvature spectrum
<!-- key: scalar-induced-waves-from-an-enhanced-small -->
- **Defining equations:** Eqs. 10.2–10.6 of Domènech 2021 (arXiv:2109.01398), in `formalism.md`; the input is $\mathcal{P}_\mathcal{R}(k)$ (peaked, log-normal, broken power law). <!-- num: not a value -->
- **Parameters:** peak scale, amplitude and width of $\mathcal{P}_\mathcal{R}$; equation of state $w$ and sound speed $c_s$ of the epoch when the peak enters; non-Gaussianity (arXiv:2109.01398) [src: Sects. 5.2–5.6, outline]. <!-- num: not a value -->
- **Predictions:** an infrared tail $k^{3}$ for radiation domination and $k^{3-2\lvert b\rvert}$ for intermediate scales in a constant-$w$ era (arXiv:2109.01398) [src: Eqs. 2.22–2.23]; a PBH counterpart from the same peak (arXiv:2109.01398) [src: Sect. 2.3, outline], whose abundance belongs to `thcosmo-pbh-defects` (planned). <!-- num: not a value -->
- **Consistency:** single-field models usually need a transient non-attractor phase, and analytic Hubble-flow parametrisations "can hide sharp, localised spikes in higher-order derivatives of the potential", which "question the robustness of simple analytical Hubble-flow parametrisation" (Barnert et al. 2026, arXiv:2606.28005) [src: abstract]. Reply: none found among the sources read.
- **Observational status:** can reproduce the NANOGrav 15-year signal (NANOGrav, arXiv:2306.16219) [src: abstract].
- **Status date:** 2026-11-05

## Not verified
<!-- key: not-verified -->

- SU(2) gauge fields during inflation, spectator-field and EFT-of-inflation enhanced tensors, and alternatives to inflation were not read.
- Kinetic preheating (arXiv:2402.16152), Higgs preheating (arXiv:2605.04670), the oscillon follow-up of Antusch et al. (arXiv:1712.03231) and oscillon formation in deformed attractors (arXiv:2602.07972) were found by search but not read; whether arXiv:1712.03231 replies to arXiv:1803.08047 was not checked.
- Metastable and current-carrying cosmic strings, superconducting strings and monopoles were found by search (2026) but not read.
- The PTA posterior regions of each model were not read; they belong to cosmoskill `cosmo-early-universe-exotica`.
