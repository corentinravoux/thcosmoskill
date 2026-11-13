# Approximations, conventions and traps in cosmological gravitational waves

Scope: the approximations the domain relies on, the regime in which a paper validates each and the error it quotes, how each fails; normalisation and gauge traps; the list a referee checks.

Snapshot: 2026-11-12

## Sub-Hubble and short-wavelength averaging
<!-- key: sub-hubble-and-short-wavelength-averaging -->

- **What it assumes:** $\rho_{\rm GW}$ is defined only after an average over several wavelengths or periods; "the energy-momentum tensor of GWs cannot be localized inside a volume smaller than the GW typical wavelength" (Caprini & Figueroa 2018, arXiv:1801.04268) [src: Sect. 3.2, text after Eq. 87]. The relation ${h^{\prime}_{c}}^{2}(k,\eta)\simeq k^{2}\,h_{c}^{2}(k,\eta)\,.$ [src: Eq. 89] neglects the $\mathcal{H}^2$ term "since in the case under analysis, $k\gg\mathcal{H}$" [src: Sect. 3.2, text before Eq. 89].
- **How it fails:** for super-horizon modes there is no wave and no energy density in this sense; the radiation bound "only applies to GWs with characteristic wavelength well inside the horizon" (arXiv:1801.04268) [src: Sect. 4.1, text after Eq. 130]. For induced waves the same condition is the first of the conditions of Domènech (arXiv:2109.01398) [src: Sect. 7.2].
- **Linearity:** "for most practical purposes there is no need to go beyond linear order in perturbation theory" once a mode is sub-Hubble and free (arXiv:1801.04268) [src: Sect. 3.3].

## Transfer function of the inflationary background
<!-- key: transfer-function-of-the-inflationary-background -->

- **Instantaneous radiation–matter transition:** the matched solution is "valid only for modes with wavelength much larger than the duration of this transition"; WKB or numerical solutions remove the restriction (arXiv:1801.04268) [src: Sect. 5.2, text after Fig. 4].
- **Oscillation average:** Eq. 223 inserts "a factor 1/2" for the oscillations, and its prefactor is chosen to recover a published fit (arXiv:1801.04268) [src: Sect. 5.2, text after Eq. 223]. The older transfer function compared there, $[T^{\prime}(k,\eta_{0})]^{2}_{\rm TWL}=\left[\left(\frac{3\,j_{1}(k\eta_{0})}{k\eta_{0}}\right)^{\prime}\right]^{2}\left(1+1.34\frac{k}{k_{\rm eq}}+2.5\frac{k}{k_{\rm eq}}\right)\,.$ [src: Eq. 224], is printed with two terms linear in $k/k_{\rm eq}$; as printed, the original fit was not read.
- **Constant $g_*$:** neglecting the Standard-Model changes of $g_*$ and $g_S$ misses a suppression given by Eq. 227 for modes that entered before each change (arXiv:1801.04268) [src: Eq. 227]; the full calculation is arXiv:astro-ph/0604176 [src: abstract]. <!-- num: not a value -->
- **Neutrino damping:** neglected in the free equation; Eq. 235 adds it, and it affects modes entering between neutrino decoupling and equality (arXiv:1801.04268) [src: Sect. 5.2, text after Eq. 235].
- **Viscosity:** shear viscosity of the plasma gives a fractional effect "of order $10^{-3}$" for the electron–photon–baryon plasma (arXiv:2512.04011) [src: abstract].

## Homogeneous backreaction in axion inflation
<!-- key: homogeneous-backreaction-in-axion-inflation -->

- **What it assumes:** the gauge-field backreaction acts only on the inflaton zero mode, neglecting inflaton gradients (Barbon, Ijaz & Peloso 2025, arXiv:2510.17207) [src: abstract].
- **How it fails:** lattice simulations find that it "fails to accurately describe the truly local dynamics of strong backreaction" (Figueroa et al. 2024, arXiv:2411.16368) [src: abstract]; the inhomogeneous treatment attenuates the inflaton-velocity oscillations, smooths out the oscillatory features of the helicity spectrum and excites the non-tachyonic helicity, "reducing the chiral asymmetry, now scale dependent" (Figueroa et al. 2023, arXiv:2303.17436) [src: abstract]. The peaks in the SGWB spectrum of homogeneous studies follow from the inflaton-velocity oscillations (arXiv:2510.17207) [src: abstract].
- **Regime defended:** examples in which the inflaton gradient energy stays subdominant to the zero-mode kinetic energy, computed perturbatively within the homogeneous assumption (arXiv:2510.17207) [src: abstract].
- **Expected citations:** arXiv:2303.17436 and arXiv:2411.16368 for the lattice; the gradient expansion formalism benchmark arXiv:2508.00798 for the parameter scan near the onset of strong backreaction [src: abstract].

## Phase-transition templates
<!-- key: phase-transition-templates -->

- **Sound-wave ansatz of 2019:** "most reliable when the sound shell surrounding the bubble wall is large", i.e. wall speeds far from the Chapman–Jouguet speed: $v_{\text{w}}<v_{\text{CJ}}=c_{\text{s}}$ for deflagrations and $v_{\text{w}}>v_{\text{CJ}}\simeq c_{\text{s}}(1+\sqrt{2\alpha_{\theta}})$ for detonations (Caprini et al. 2019, arXiv:1910.13125) [src: Sect. 3.3, inline, text after Eq. 28]; near $v_{\rm CJ}$ "the spectral shape ansatz in (30) fails to describe these scenarios well" [src: Sect. 3.3, text after Eq. 31]. Bubbles in the calibrating simulations "are nucleated simultaneously" [src: Sect. 3.3].
- **Source lifetime:** Eq. 29 assumes $\tau_{\text{v}}\sim 1/H_{*}$; if $H_{*}\tau_{\text{sh}}<1$ the power is reduced by $H_{*}\tau_{\text{sh}}=H_{*}R_{*}/K^{1/2}$ (arXiv:1910.13125) [src: Sect. 3.3, inline, text after Eq. 31]. The 2024 template uses $\bar{v}_{f}^{2}=\Gamma^{-1}\,K$, "valid in the subrelativistic bulk velocity limit" (arXiv:2403.03723) [src: Sect. 2.2.1, text after Eq. 11].
- **Turbulence:** the 2019 report neglects GWs from turbulence "altogether, in order to be conservative" [src: Sect. 3.2]; its fraction ε = 0.05 of the earlier report "is accurate at low RMS fluid velocities, $\bar{U}_{\rm f}\lesssim 0.05$, but $\varepsilon$ is likely larger than 0.05 at higher fluid velocities" (arXiv:1910.13125) [src: Sect. 3.2].
- **Kinetic-energy deficit in strong transitions:** the efficiency "falls below theoretical expectations as we increase the transition strength", probably from "reheated droplets of the metastable phase" (Cutting, Hindmarsh & Weir 2019, arXiv:1906.00480) [src: abstract].
- **Flat spacetime:** in expanding-universe simulations the normalised GW amplitude is "of order $\mathcal{O}(10^{-2})$, in alignment with Minkowski-spacetime results", while "the resulting GW spectra differ markedly from those scenarios"; the effective lifetime of the sound-wave source "increases for slower PTs" (Zou et al. 2026, arXiv:2610.14806) [src: abstract]. Version 1 of the paper reported amplitudes "roughly an order of magnitude smaller"; version 2 no longer does (hub `stale-claims.md`).
- **Thermal effective potential:** renormalisation-scale dependence of the daisy-resummed potential gives "two to three orders-of-magnitude uncertainty in the peak gravitational wave amplitude"; dimensional reduction is gauge invariant and "avoids an uncontrolled derivative expansion in the bubble nucleation rate" (Croon et al. 2020, arXiv:2009.10080) [src: abstract].
- **Expected citations:** arXiv:1910.13125 and arXiv:2403.03723 for templates, arXiv:1004.4187 for κ, arXiv:1906.00480 for the deficit, arXiv:2009.10080 for the potential.

## Defect-network modelling
<!-- key: defect-network-modelling -->

- **Nambu–Goto versus field theory:** Nambu–Goto simulations "underestimate the mean string separation by about 25%, and overestimate $\bar v^2$ by about 10%" relative to Abelian-Higgs simulations, and neglect the massive-radiation channel (Hindmarsh et al. 2017, arXiv:1703.06696) [src: abstract]. The GW bound on $G\mu$ depends on which picture is assumed. `[der]`
- **Harmonic tail:** $P_{n}\propto 1/n^{q+1}$ assumed down to n = 1 (arXiv:1801.04268) [src: Sect. 9.2, text after Eq. 383]; the harmonic and burst formalisms diverge on the rising branch, and using harmonics "strengthens the LVK bounds by $21\%-31\%$ for three of these models" (arXiv:2610.02590) [src: abstract].
- **Bursts:** removing rare bursts has "practically no effect on the present-day GW spectrum" for large initial loops, "at least when the number of cusps and kinks per loop oscillation period is $\mathcal{O}(1)$" (arXiv:1801.04268) [src: Sect. 9.2, text after Eq. 383].
- **Comparing bounds:** analyses "make different assumptions about cusps, kinks, gravitational back-reaction, and other aspects, so it is difficult to compare the results among them" (arXiv:1801.04268) [src: Sect. 9.2.1, text after Eq. 384].
- **Lattice infrared tails:** wiggles in the infrared of lattice GW spectra from domain walls "are nonphysical" when obtained directly from the two-point correlation function (Dankovsky & Gorbunov 2026, arXiv:2607.25073) [src: abstract].

## Scalar-induced waves: Gaussianity, gauge and perturbative order
<!-- key: scalar-induced-waves-gaussianity-gauge-and -->

- **Gauge:** "a gauge invariant formulation of the equations of motion of induced GWs (3.15) does not help at all. There are infinitely many ways to define gauge invariant variables, each definition corresponding to a particular gauge choice" (Domènech 2021, arXiv:2109.01398) [src: Sect. 7.2]. With the synchronous gauge properly fixed, it and the Newtonian gauge "yield the same prediction in a radiation dominated universe", and this "also holds for any cosmological background with a constant equation of state [161] if it is not dust" [src: Sect. 7.2, text after Eq. 7.11]. The conditions under which the energy density is meaningful start with "really subhorizon scales ($k\gg{\cal H}$)" and a (barely) absent source [src: Sect. 7.2, inline, text after Eq. 7.11]. Full treatment: `thcosmo-cosmological-perturbations` (planned).
- **Instantaneous reheating:** the general formulas assume a constant-w epoch, a peak entering during it and an instantaneous transition; "If the transition to radiation domination is gradual, then we only expect a change in the IR tail" (arXiv:2109.01398) [src: Sect. 10.1, text after Eq. 10.5].
- **Perturbative order in a matter era:** third-order kernels grow secularly in matter domination; requiring no backreaction bounds the initial PBH abundance "about three orders of magnitude stronger than the second-order-only bound" (Zhou 2026, arXiv:2610.08045) [src: abstract].
- **Dirac-delta spectra:** give a slope $2-2\vert b\vert$ "due to the unphysical divergence" at the peak (arXiv:2109.01398) [src: Sect. 2.2.1, text after Eq. 2.22].

## Normalisation traps
<!-- key: normalisation-traps -->

- **Polarisation normalisation:** $e_{ij}^{r}(\mathbf{\hat{k}})\,e_{ij}^{r^{\prime}}(\mathbf{\hat{k}})=2\,\delta_{rr^{\prime}}\,,$ in Caprini & Figueroa (arXiv:1801.04268) [src: Eq. 64]; their $h_c$ convention "differs by a factor 2" from their Ref. [54], and Eq. 94 carries "the factor two difference with respect to e.g. [54]" [src: Sect. 3.2, text after Eq. 85 and text before Eq. 94]. <!-- num: not a value -->
- **Two spectra in one review:** $h_c^2$ (Eq. 84, with a factor 2 in Eq. 85) and $\mathcal{P}_h$ (Eq. 192, no factor 2 in Eq. 193) are normalised differently in arXiv:1801.04268 [src: Eqs. 84–85, 192–193]. `[der]` <!-- num: not a value -->
- **Planck mass:** Caprini & Figueroa use $m_{\mathrm{Pl}}=1/\sqrt{8\pi G}$ in Sect. 5 [src: Sect. 5.1, text after Eq. 165] while writing $G$ elsewhere, and their axion bispectrum carries $M_{\rm Pl}$ (arXiv:1801.04268) [src: Sect. 6.1.2]; Domènech uses $M_{\rm pl}$ in Eq. 5.1 (arXiv:2109.01398) [src: Eq. 5.1]. Check which Planck mass a coefficient assumes before reusing it. `[der]` <!-- num: not a value -->
- **$h^2\Omega_{\rm GW}$ versus $\Omega_{\rm GW}$ and the redshift prefactor:** $1.6\times 10^{-5}(100/g_*)^{1/3}$ in arXiv:1801.04268 [src: Eq. 104]; $(3.57\pm 0.05)\times 10^{-5}(100/g_*)^{1/3}$ for $F_{\rm gw,0}$ (without $h^2$) in arXiv:1910.13125 [src: Eq. 20]; $1.62\times 10^{-5}$ with $g_*$ normalised to 106.75 in arXiv:2109.01398 [src: Eq. 5.2].
- `[der]` The three prefactors above are different normalisations, not different predictions.
- **α means three things:** the PT strength (arXiv:1910.13125) [src: Eq. 9], the loop size at birth in units of the horizon (arXiv:1801.04268) [src: Sect. 9.2]; and $\eta$ is both conformal time and a slow-roll parameter in arXiv:1801.04268 [src: Eqs. 168, 242]. <!-- num: not a value -->
- **Friction sign:** ν enters as $(2+\nu)\mathcal{H}$ in arXiv:1807.09241 [src: Eq. 55] and δ as $2\mathcal{H}[1-\delta]$ in arXiv:1805.08731 [src: Eq. 12]; no relation between them is stated in either paper. <!-- num: not a value -->
- **Polarisation pattern of a binary:** Eq. 61 of arXiv:1807.09241 prints $h_{+}\propto\frac{(1+\cos\iota)^{2}}{2d_{L}^{\text{gw}}}\quad\text{and}\quad h_{\times}\propto\frac{\cos\iota}{d_{L}^{\text{gw}}}\,,$ (arXiv:1807.09241) [src: Eq. 61], with the square outside the bracket; as printed, no erratum found.
- `[der]` Face-on, the two printed amplitudes are not equal, while a face-on binary emits circularly polarised waves.

## Classical lattice simulations of preheating
<!-- key: classical-lattice-simulations-of-preheating -->

- **What it assumes:** the fields are evolved as classical inhomogeneities on a lattice, which source the tensor equation; existing predictions "mostly rely on computer simulations in which the matter field inhomogeneities essentially behave classically" (Armendariz-Picon 2019, arXiv:1905.05724) [src: abstract]. The tensor perturbations are evolved as unphysical fields and projected with a lattice TT projector consistent with the lattice derivative used (Baeza-Ballesteros et al. 2025, arXiv:2512.15627) [src: Sect. 8.2].
- **Regime validated:** "In the cases in which parametric resonance is effective", the quantum in-in results "agree with the predictions expected from numerical simulations" (arXiv:1905.05724) [src: abstract]; the continuum-based TT projection differs "only marginally in amplitude and shape" from the lattice one (Figueroa, García-Bellido & Rajantie 2011, arXiv:1110.0337) [src: abstract]; the fits of arXiv:1707.04533 hold for the ranges printed with them, $q>1$ for $\lambda\phi^4$ and $q\gtrsim 6\cdot 10^{3}$ for the amplitude of $\frac{1}{2}m^2\phi^2$ [src: Sect. 5; Eq. 108]. <!-- num: not a value -->
- **How it fails:** "At sufficiently low values of the resonance parameter, however, numerical simulations fail" (arXiv:1905.05724) [src: abstract]. Long runs lose resolution in an expanding grid: for oscillons, "numerical errors accumulated with time are significant in low-resolution scenarios, or in scenarios where the run-time causes the resolution to drop below the relevant scales in the problem" (Amin et al. 2018, arXiv:1803.08047) [src: abstract]. Amplitudes at production need the post-production equation of state to be redshifted, carried by $\epsilon_{\rm f}$ in the fits (arXiv:1707.04533) [src: Sect. 5, text after Eq. 108]; the hybrid-inflation estimates of arXiv:0707.0875 are "preliminary estimates" extrapolated from the $\lambda\phi^4$ bubbly stage [src: Sect. VII].
- **Expected citations:** arXiv:0707.0875 for the method and the analytic checks, arXiv:1707.04533 for the $q$ dependence, arXiv:1110.0337 for the TT projection, arXiv:1803.08047 for convergence with oscillons, arXiv:1905.05724 for the quantum treatment.

## Radiation bound: shortwave approximation, initial conditions and prior
<!-- key: radiation-bound-shortwave-approximation-initial -->

- **What it assumes:** the waves behave as a massless species with $w_{\textnormal{gw}}=1/3$, which holds when "the perturbation is well inside the horizon and that it is oscillating much faster than the background time-scale" (Clarke, Copeland & Moss 2020, arXiv:2004.11396) [src: Sect. 4]. The BBN form integrates only over modes inside the horizon at BBN and only over waves generated before it (Boyle & Buonanno 2008, arXiv:0708.2279) [src: Sect. VII, text after Eq. 44].
- **Regime validated:** for a cosmic-variance-limited experiment, requiring $\delta C_{\ell}/C_{\ell}<0.2\%$ for all $\ell$ with a $\delta$-function source of $\Omega_{\textnormal{gw}}h^{2}=5.6\times 10^{-6}$, "corresponding to $\Delta N_{\rm eff}=1$ in the SWA", "a source with $k>1\,{\rm Mpc}^{-1}$ is required", which "corresponds to the mode undergoing 50 oscillations by the epoch of equality"; arXiv:astro-ph/0603144 used "a factor of $\sim 20$ wavelengths", and "Our analysis suggests that a slightly more conservative limit is required" (arXiv:2004.11396) [src: Sect. 5.2, inline].
- **How it fails (1), initial conditions:** with adiabatic initial conditions "existing cosmic microwave background+baryon acoustic oscillations constraints on $N_{\rm eff}$, can be directly translated into constraints on the energy density of gravitational waves" (Wang & Zhao 2025, arXiv:2507.06930) [src: Sect. 2]; with homogeneous ones "the degeneracy between the CGWB and massless neutrinos is thus broken" and "The bound to the CGWB then turns out to be stronger than in the adiabatic case" (Smith, Pierpaoli & Kamionkowski 2006, arXiv:astro-ph/0603144) [src: text before Fig. 2]. Which applies is set by the source: the homogeneous case is the one for a mechanism "that leaves its primordial density uncorrelated with the curvature perturbation—e.g., inflation or perhaps some post-inflation phase-transition mechanism" [src: text before Fig. 2]. The homogeneous mode of arXiv:2004.11396 "differs from the one quoted in [33] and consequently the one used in [19]" (their [19] is arXiv:astro-ph/0603144 [src: References]), because the earlier mode "is a linear sum of the homogeneous mode given here and the neutrino density isocurvature mode" (arXiv:2004.11396) [src: Sect. 4.1].
- **How it fails (2), the prior:** with a log-uniform prior on $\Omega_{\rm gw}h^{2}$ "these constraints can become tighter by a factor of $\sim4$, suggesting the results to be prior-sensitive" (Wang & Zhao 2025, arXiv:2507.06930) [src: abstract, inline]; translating a measured $N_{\rm eff}$ into a bound ignores the physical prior $\Omega_{\textnormal{gw}}h^{2}\geq 0$ (arXiv:2004.11396) [src: Sect. 2.2, inline].
- **How it fails (3), narrow spikes:** the integral bound reads as a bound on $\Omega_{\rm GW}(f)$ itself except for "a very narrow spike with $(\delta f)/f_{0}\ll 1$" (arXiv:0708.2279) [src: Sect. VII, text after Eq. 44].
- **How it fails (4), sources after BBN or decoupling, and long modes:** waves produced after BBN escape the BBN form (arXiv:0708.2279) [src: Sect. VII, text after Eq. 44]; arXiv:2004.11396 uses the shortwave approximation only "On small scales, $f \gtrsim10^{-15}\,\mbox{Hz}$", second-order back-reaction for $10^{-15}\,\text{Hz}\gtrsim f\gtrsim 3\times 10^{-16}\,\text{Hz}$ and, "On large scales, $f \lesssim 10^{-16}\, \text{Hz}$", a reconstruction of the initial tensor power spectrum "in logarithmic frequency bins" [src: abstract].
- **Expected citations:** arXiv:astro-ph/0603144 for the CMB bound and the initial-condition question, arXiv:2004.11396 for the shortwave validity and the corrected homogeneous mode, a current data bound (arXiv:2507.06930), and arXiv:0708.2279 for the BBN form.

## Referee checklist
<!-- key: referee-checklist -->

1. Which normalisation of $h_c$, $\mathcal{P}_h$ and the polarisation tensors, and which Planck mass, does each coefficient assume (`formalism.md#conventions`)?
2. Is the spectrum given as $\Omega_{\rm GW}$ or $h^2\Omega_{\rm GW}$, and with which $g_*$ and $g_S$ at production?
3. Is the source sub-horizon at production, and is the causal $f^3$ tail respected below the horizon scale?
4. For phase transitions: which template (2019 Eq. 29 or 32, 2024 Template I or II), is $v_{\rm w}$ away from the Chapman–Jouguet speed, is the shock time compared with the Hubble time, is turbulence included, which $K$ (with or without the 0.6 factor), and is the thermal potential computed with dimensional reduction? <!-- num: not a value -->
5. For strings: Nambu–Goto or field-theory loops, which loop distribution, harmonic or burst formalism, cusps and kinks per oscillation; for walls: which bias mechanism.
6. For axion inflation: homogeneous or local backreaction, and is the $\Delta N_{\rm eff}$ bound checked?
7. For scalar-induced waves: gauge, Gaussian or not, constant-w assumption and reheating transition, perturbative order in a matter era, a Dirac-delta input.
8. For propagation: friction parameterisation stated with its sign; speed-of-tensors constraints taken from `thcosmo-modified-gravity`.
9. Is any PTA or interferometer bound quoted with its dataset, and are forecasts labelled?
10. For any source before BBN or decoupling: is the integrated $\Delta N_{\rm eff}$ bound checked, with adiabatic or homogeneous initial conditions stated, the integration range stated ($f_{\rm bbn}$ for BBN, arXiv:0708.2279 [src: Sect. VII, text after Eq. 44]; $f\gtrsim10^{-15}$ Hz for the CMB in the shortwave approximation, arXiv:2004.11396 [src: abstract]), and $\Omega_{\rm GW}$ or $h^{2}\Omega_{\rm GW}$ kept apart?
11. For preheating: which resonance parameter (definitions differ between potentials, arXiv:1707.04533 [src: Sect. 5]), which post-production equation of state ($\epsilon_{\rm f}$), a convergence test when oscillons or long runs are involved, and the $\Delta N_{\rm eff}$ bound for gauge preheating.

## Not verified
<!-- key: not-verified -->

- The Planck 2018 and later bounds on r, and the measured PTA spectra, were not read; they belong to cosmoskill.
- Error estimates for the sound-shell model itself were not read.
