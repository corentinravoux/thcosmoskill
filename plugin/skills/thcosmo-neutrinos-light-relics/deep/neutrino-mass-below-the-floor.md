# Massive neutrinos in Boltzmann codes and masses below the oscillation floor — thcosmo-neutrinos-light-relics dossier

Scope: how a Boltzmann code samples and closes the momentum-dependent massive-neutrino hierarchy and when it switches to a fluid, and how the "effective", "negative" or split neutrino-mass parameters used when data pull $\sum m_\nu$ below the oscillation floor are defined, at fixed what, and what each one changes.
Snapshot: 2026-11-05.
From: Lesgourgues & Pastor arXiv:astro-ph/0603494, Sects. 4.5–4.6; Dvorkin et al. arXiv:2203.07943, Sect. 4.2 — `references/subtopics.tsv`, rows `massive-neutrino-perturbations` and `massive-neutrino-background`.
Audit questions: (2) How are massive-neutrino perturbations solved in Boltzmann codes (momentum grid, hierarchy truncation, fluid approximation), and how are effective or negative neutrino masses defined when the data pull $\sum m_\nu$ below the oscillation floor?

Already in the reference files, and not repeated here: the Ma–Bertschinger hierarchy in both gauges, its truncation Eq. 58 and the shear integral (`formalism.md#massive-neutrino-perturbations-and-free`); their 128-point grid with $l_{\rm max}=50$, the abstract-level CLASS speed-up and the 2025–2026 dispersive-fluid and quasi-stationary approximations (`approximations.md#massive-neutrinos-in-boltzmann-codes-momentum`); the $\Omega_\nu$ relation and its 93.14 eV coefficient (`formalism.md#massive-neutrinos-background`, `approximations.md#convention-traps`); the theory responses to the tension at abstract level (`open-questions.md#the-neutrino-mass-tension-as-seen-from-theory`). Measured values of $\sum m_\nu$ and of the effective parameters belong to cosmoskill `cosmo-neutrinos-dark-matter` (two-home rule) and are not given here. <!-- num: not a value -->

## Conventions
<!-- key: conventions -->

- Lesgourgues & Tram (arXiv:1104.2935, CLASS IV, v3) "follow the notations" of Ma & Bertschinger except that momentum and energy are divided by the present temperature of the relic, $q\equiv\frac{q_{\text{\tt MB}}}{T_{{\tt ncdm},0}}~,\qquad\epsilon\equiv\frac{\epsilon_{\text{\tt MB}}}{T_{{\tt ncdm},0}}=\left(q^{2}+a^{2}\frac{m^{2}}{T_{{\tt ncdm},0}^{2}}\right)^{\frac{1}{2}},$ (arXiv:1104.2935) [src: Eq. 1], which leaves the perturbation equations unchanged "since they depend only on the ratio" of q to ε [src: Sect. 2]; dots are conformal-time derivatives, and the paper works "exclusively in the synchronous gauge" [src: Sect. 2.1, text after Eq. 3].
- Bertólez-Martínez et al. (arXiv:2411.14524, v2) use conformal time with primes and the conformal Newtonian gauge with potentials φ and ψ [src: Sect. II.1; Sect. II.2, text after Eq. 10]; their distribution carries the factor $(2\pi)^{-3}$ (Eq. 4).
- Elbers et al. (arXiv:2407.10965, v2) write the hierarchy in conformal Newtonian gauge after Ma & Bertschinger, with x the comoving momentum over $T_\nu$ in the background integral (Eq. 1) and q the momentum in the hierarchy (Eqs. 4–6) [src: Sect. II].
- `[der]` The potential names follow Ma & Bertschinger in arXiv:2407.10965 and arXiv:2411.14524 (ψ in the time–time part); the swap with Lesgourgues & Pastor is in `formalism.md#conventions`.

## The derivation
<!-- key: the-derivation -->

### Part A — solving the hierarchy in a Boltzmann code
<!-- key: part-a-solving-the-hierarchy-in-a-boltzmann-code -->

#### Step A1 — what is needed from the hierarchy
<!-- key: step-a1-what-is-needed-from-the-hierarchy -->

Only four momentum integrals of the multipoles enter the Einstein equations, the density, pressure, energy-flux and shear perturbations; the shear is $\left(\bar{\rho}_{\tt ncdm}+\bar{p}_{\tt ncdm}\right)\sigma_{\tt ncdm}=\frac{8\pi}{3}\left(\frac{T_{{\tt ncdm},0}}{a}\right)^{4}\int_{0}^{\infty}f_{0}(q)\mathrm{d}q\frac{q^{4}}{\epsilon}\Psi_{2}.$ (arXiv:1104.2935) [src: Eq. 2d], the others being Eqs. 2a–2c. $\Psi_0$ and $\Psi_1$ "are gauge-dependent quantities, while higher momenta are not"; the dipole transforms as $\Psi_{1,\text{Con.}}=\Psi_{1,\text{Syn.}}-\frac{1}{3}\alpha k\frac{\epsilon}{q}\frac{d\ln f_{0}}{d\ln q}~,$ (arXiv:1104.2935) [src: Eq. 3], with α built from the synchronous-gauge h and η [src: Sect. 2.1, text after Eq. 3]. The synchronous-gauge hierarchy (Eqs. 4a–4d) is that of Ma & Bertschinger, Eq. 56 of arXiv:astro-ph/9506072, in `formalism.md`. <!-- num: not a value -->

The homogeneous part is $\mathbf{\dot{\Psi}}=\frac{qk}{\epsilon}A\mathbf{\Psi}\equiv\alpha\left(\tau\right)A\mathbf{\Psi},$ (arXiv:1104.2935) [src: Eq. 5], whose largest eigenvalue tends to ±i, so that the fastest phase is $\phi_{\omega_{\text{max}}}\left(\tau\right)\simeq k\int_{\tau_{i}}^{\tau}\mathrm{d}\tau^{\prime}\left(1+\frac{M^{2}}{q^{2}}a\left(\tau^{\prime}\right)^{2}\right)^{-\frac{1}{2}}.$ (arXiv:1104.2935) [src: Eq. 9].

`[der]` Each momentum bin oscillates at a frequency set by its own q/ε, which is why the hierarchy cannot be momentum-integrated exactly and every bin is evolved separately.

#### Step A2 — the momentum grid
<!-- key: step-a2-the-momentum-grid -->

"There is no coupling between the momentum bins", so the task is a quadrature of integrals of the form $\mathcal{I}=\int_{0}^{\infty}\mathrm{d}qf_{0}\left(q\right)g\left(q\right),$ (arXiv:1104.2935) [src: Eq. 10], with g "reasonably well described by a polynomial in q", checked for the functions of Eq. 2 [src: Sect. 2.2]. CLASS chooses, among several rules, the one that computes a test integral $\mathcal{J}=\int_{0}^{\infty}\mathrm{d}qf_{0}\left(q\right)t\left(q\right),$ (arXiv:1104.2935) [src: Eq. 11] to the tolerance `tol_ncdm` "using the fewest possible points" [src: Sect. 2.2]; Gauss–Laguerre and adaptive sampling are in its App. A. The optimisation is run twice per species, with a tighter tolerance for background integrals than for perturbations, because "reducing the number of sampling points for perturbations is crucial for reducing the total computing time" [src: Sect. 2.2]. <!-- num: not a value -->

Code facts, read in `include/precisions.h` and `explanatory.ini` of the `class_public` master branch (version string v3.4.2 in `include/common.h`): `tol_ncdm_synchronous` = 1.e-3, `tol_ncdm_newtonian` = 1.e-5, `tol_ncdm_bg` = 1.e-5 [doc: github.com/lesgourg/class_public master, include/precisions.h, 2026-11-05]; `ncdm_quadrature_strategy` default 0, "the automatic method", with 1 Gauss–Laguerre and 2–3 trapezoidal rules [doc: github.com/lesgourg/class_public master, explanatory.ini, 2026-11-05].

#### Step A3 — truncating the hierarchy
<!-- key: step-a3-truncating-the-hierarchy -->

The Ma–Bertschinger free-streaming truncation (Eq. 58 of arXiv:astro-ph/9506072, in `formalism.md`) is "valid for $l_{\text{max}}>3$: in this case, all quantities are gauge-invariant" (arXiv:1104.2935) [src: Sect. 3.3]. Lesgourgues & Tram note that the recurrence is "better motivated theoretically" in the massless limit, where $\Psi_l$ follows a spherical Bessel function, whereas in the massive case the formal solution oscillates with "arguments going from $\sim k\tau$ in the massless limit to $\sim\left(k\tau\right)^{-1}$ in the massive limit" [src: Sect. 3.3, footnote 2]. In the paper's reference precision file `l_max_ncdm` is 51; the two fast files use 16 and 12 [src: Table 1]. Current default: `l_max_ncdm` = 17 [doc: github.com/lesgourg/class_public master, include/precisions.h, 2026-11-05].

#### Step A4 — the fluid approximation inside the Hubble radius
<!-- key: step-a4-the-fluid-approximation-inside-the -->

After Hubble crossing "there is an effective decoupling between high multipoles" and "low multipoles (just sourced by metric perturbation)", so when kτ exceeds a threshold the hierarchy is cut to $l_{\rm max}=2$; in the massless case this "allows simultaneously to save computing time" and "to increase precision (by avoiding artificial reflection of power at some large cut-off value $l_{\rm max}$)" (arXiv:1104.2935) [src: Sect. 3.1]. <!-- num: not a value -->

The fluid obeys, in synchronous gauge with the comoving-frame sound speed $c_{\rm eff}$, $\dot{\delta}=-\left(1+w\right)\left(\theta+\frac{\dot{h}}{2}\right)-3\frac{\dot{a}}{a}\left(c_{\text{eff}}^{2}-w\right)\delta+9\left(\frac{\dot{a}}{a}\right)^{2}(1+w)\left(c_{\text{eff}}^{2}-c_{g}^{2}\right)\frac{\theta}{k^{2}},$ (arXiv:1104.2935) [src: Eq. 13a] and $\dot{\theta}=-\frac{\dot{a}}{a}\left(1-3c_{\text{eff}}^{2}\right)\theta+\frac{c_{\text{eff}}^{2}}{1+w}k^{2}\delta-k^{2}\sigma.$ (arXiv:1104.2935) [src: Eq. 13b]. The shear equation follows from differentiating Eq. 2d and closing with the truncation rewritten for $l_{\rm max}=3$ in synchronous gauge, $\Psi_{3}\approx\frac{5\epsilon}{qk\tau}\Psi_{2}-\left(\Psi_{1}-\frac{1}{3}\alpha k\frac{\epsilon}{q}\frac{d\ln f_{0}}{d\ln q}\right).$ (arXiv:1104.2935) [src: Eq. 16], "Asssuming that the truncation law holds for gauge-invariant quantities" [src: Sect. 3.3, text before Eq. 16]; Newtonian-gauge equations follow with α = 0 [src: Sect. 3.3, text after Eq. 16]. <!-- num: not a value -->

Three closures were implemented, all with $c_{\rm eff}=c_g$ in Eqs. 13a–13b [src: Sect. 3.5]; the default one, named CLASS, is $\dot{\sigma}_{\text{\tt{CLASS}}}=-3\left(\frac{1}{\tau}+\frac{\dot{a}}{a}\left[\frac{2}{3}-c_{g}^{2}-\frac{1}{3}\frac{\mathfrak{p}}{p}\right]\right)\sigma+\frac{4}{3}\frac{c_{\text{vis}}^{2}}{1+w}\left[2\theta+\dot{h}\right],c_{\text{vis}}^{2}=3wc_{g}^{2}.$ (arXiv:1104.2935) [src: Eq. 26c], identical to the MB closure (Eq. 26a) "except for the omission" of the $\dot\eta$ term, by analogy with the massless case, where removing it "leads to slightly better results for the matter power spectrum" [src: Sect. 3.5]; the Hu closure (Eq. 26b) "corresponds exactly to the prescription" of the paper's Ref. 8 [src: Sect. 3.5]. The three "work very well as long as the neutrinos are light and become non-relativistic after photon decoupling", and CLASS is "slightly better for predicting the matter power spectrum on small scales" [src: Sect. 3.5]. <!-- num: not a value -->

The switch is set by kτ: the paper's fast precision files use a kτ trigger of 30 or 16, reducing the neutrino equations from 136 or 65 to 3 [src: Table 1]. Current defaults: `ncdm_fluid_approximation` = `ncdmfa_CLASS` and `ncdm_fluid_trigger_tau_over_tau_k` = 31.0 [doc: github.com/lesgourg/class_public master, include/precisions.h, 2026-11-05].

### Part B — neutrino masses below the oscillation floor
<!-- key: part-b-neutrino-masses-below-the-oscillation -->

#### Step B1 — where the mass enters, and why a sign can be continued
<!-- key: step-b1-where-the-mass-enters-and-why-a-sign -->

The mass enters the background only through the equation of state of the neutrinos, $w_{\nu}(a,m_{\nu})=\frac{1}{3}\frac{\int\mathrm{d}^{3}p\,\frac{p^{2}}{\sqrt{p^{2}+m_{\nu}^{2}}}f_{0}(ap)}{\int\mathrm{d}^{3}p\,\sqrt{p^{2}+m_{\nu}^{2}}f_{0}(ap)}\,,$ (arXiv:2411.14524) [src: Eq. 3], which controls the dilution $\frac{1}{\rho_{\nu}}\frac{\mathrm{d}\rho_{\nu}}{\mathrm{d}\ln a}=-3[1+w_{\nu}(a)]\,,$ (arXiv:2411.14524) [src: Eq. 2]; "the only background effect of increasing neutrino masses, with other parameters fixed, is to increase the expansion rate of the Universe" [src: Sect. II.1]. Equivalently, "Formally, the Friedmann equations that govern the expansion of space depend only on the neutrino masses squared", through $\Omega_{\nu}(a)=\sum_{i=1}^{N_{\nu}}\frac{8GT_{\nu}^{4}}{3\pi H_{0}^{2}}\int_{0}^{\infty}\frac{x^{2}\sqrt{x^{2}+a^{2}m_{i}^{2}/T_{\nu}^{2}}}{1+e^{x}}\mathrm{d}x,$ (arXiv:2407.10965) [src: Eq. 1], which reduces at late times to $\Omega_{\nu}\approx\frac{\textstyle\sum m_{\nu}}{93.14h^{2}}.$ (arXiv:2407.10965) [src: Eq. 2].

In perturbations the mass sets the comoving sound speed and the anisotropic stress: Bertólez-Martínez et al. write the fluid equations with the gauge-invariant $c_{\mathrm{eff}}^{2}\equiv\frac{k^{2}c_{s}^{2}\delta+3\frac{a^{\prime}}{a}(1+w_{\nu})c_{\mathrm{ad}}^{2}\theta}{k^{2}\delta+3\frac{a^{\prime}}{a}(1+w_{\nu})\theta}\,.$ (arXiv:2411.14524) [src: Eq. 12], "the sound speed in a frame comoving with neutrinos", for which adiabatic perturbations "behave as background as $k\rightarrow 0$ regardless of the values" of $c_{\rm eff}^2$, σ and $w_\nu$ [src: Sect. II.2, text after Eq. 12]; "the anisotropic stress contains the leading 'kinematic' effects" of the mass [src: Sect. II.2]. <!-- num: not a value -->

The size of the late-time effect that the data constrain is set by $P^{\left(\sum m_{\nu}\right)}\left(k\gg k_{\mathrm{fs}},z\right)\approx\left(1-2f_{\nu}-\frac{6}{5}f_{\nu}\log\frac{1+z_{\nu}}{1+z}\right)P^{\left(\sum m_{\nu}=0\right)}\left(k\gg k_{\mathrm{fs}},z\right)\,.$ (arXiv:2407.07878) [src: Eq. 2.2], whose logarithm enhances the suppression "by a factor of approximately 7.5", so that "even a minimum sum of neutrino masses leaves a two percent suppression of power" [src: Sect. 2.1, text after Eq. 2.2].

`[der]` Below the floor, "negative mass" therefore means more lensing or a different expansion history than massless neutrinos give; the definitions below differ in which of these they continue to negative values.

#### Step B2 — the effective mass continued in the Boltzmann equations (Elbers et al.)
<!-- key: step-b2-the-effective-mass-continued-in-the -->

A term $\Omega_{\nu,\text{eff}}(a)=\kappa\Omega_{\nu}(a)$ with κ < 0 would reduce "the radiation density at early times and the matter density at late times", and is reinterpreted as $\sum m_{\nu,\text{eff}}\equiv 93.14h^{2}\,\Omega_{\nu,\text{eff}}$ (arXiv:2407.10965) [src: Sect. II, inline, text after Eq. 2]. The authors stress that "it is the energy (depending on the absolute value of the mass) that enters the Friedmann equations", so negative masses "more accurately correspond to negative energies", and the word effective emphasises "that negative values are unphysical and rather signal the presence of systematic errors, a non-standard cosmological evolution or new neutrino properties" [src: Sect. II, footnote 2].

The continuation to all orders in perturbation theory replaces the energy by $\epsilon_{\text{eff}}=\text{sgn}(m_{\nu})\sqrt{x^{2}+a^{2}m_{\nu}^{2}/T_{\nu}^{2}},$ (arXiv:2407.10965) [src: Eq. 3], so that the conformal-Newtonian hierarchy becomes $\dot{\Psi}_{0}=-\frac{qk}{\epsilon_{\text{eff}}}\Psi_{1}-\dot{\phi}\frac{\mathrm{d}\ln\bar{f}}{\mathrm{d}\ln q},$ [src: Eq. 4], $\dot{\Psi}_{1}=\frac{qk}{3\epsilon_{\text{eff}}}(\Psi_{0}-2\Psi_{2})-\frac{\epsilon_{\text{eff}}k}{3q}\psi\frac{\mathrm{d}\ln\bar{f}}{\mathrm{d}\ln q},$ [src: Eq. 5] and $\dot{\Psi}_{\ell}=\frac{qk}{(2\ell+1)\epsilon_{\text{eff}}}\left[\ell\Psi_{\ell-1}-(\ell+1)\Psi_{\ell+1}\right],\;\;\;(\ell\geq 2),$ (arXiv:2407.10965) [src: Eq. 6].

Their operational definition, for "all masses either positive or negative", at fixed $\omega_{\rm b}$, $\omega_{\rm c}$, $\theta_{\rm s}$, τ, $A_s$ and $n_s$, is the antisymmetric extrapolation $X_{\bm{\theta}}^{\sum\!m_{\nu,\text{eff}}}\!\equiv\!X_{\bm{\theta}}^{\sum\!m_{\nu}=0}\!+\text{sgn}(\textstyle\sum m_{\nu,\text{eff}})\left[X_{\bm{\theta}}^{\rvert\sum\!m_{\nu,\text{eff}}\rvert}\!-\!X_{\bm{\theta}}^{\sum\!m_{\nu}=0}\right],$ (arXiv:2407.10965) [src: Eq. 7], for any observable X. The two methods were implemented in CLASS and cobaya and "agree to excellent precision"; for ±0.15 eV the extrapolation agrees with the exact linear-theory calculation "to within 0.1%" for the dark-matter power spectrum at z = 0, the one case shown [src: Sect. II; Fig. 1 caption]. The construction "recovers exactly the physical neutrino model" for non-negative values and needs no Gaussian assumption on the posterior [src: Sect. II]. In the oscillation-blind analysis the spectrum is degenerate, three species with a uniform prior $m_{\nu,\text{eff}}\in[-1.5,1.5]$ eV [src: Sect. II]. <!-- num: not a value -->

#### Step B3 — the lensing-only parameter (Craig et al.; Green & Meyers)
<!-- key: step-b3-the-lensing-only-parameter-craig-et-al -->

Craig et al. note that CAMB and CLASS "model neutrino mass in a way that is subject to the physicality constraint" and introduce $\sum\tilde{m}_{\nu}$, which "simply scales the CMB lensing power spectrum in the same manner that would be expected from" the physical mass (arXiv:2405.00836) [src: Sect. 2.2]. The scaling is the ratio $A_{\ell}(\sum\tilde{m}_{\nu})\equiv C_{\ell}^{\kappa\kappa}[\sum m_{\nu}]/C_{\ell}^{\kappa\kappa}[\sum m_{\nu}=0]$ (arXiv:2405.00836) [src: Sect. 2.2, inline, text after Eq. 2.10], computed "at fixed values of $H_{0}$, $\omega_{m}$, and $\omega_{b}$", calibrated on positive masses and continued to negative ones; all other observables use the physical $\sum m_\nu=0$, and the lensed TT, TE, EE spectra are computed with the modified lensing spectrum "self-consistently" [src: Sect. 2.2]. The prescription is "very similar, though not identical" to the physical mass for positive values: it adds no neutrino contribution to $\Omega_m$, so slightly weaker constraints are expected, which the paper finds [src: Sect. 2.2]. Green & Meyers use "the same prescription", applied "consistently" to $C_L^{\phi\phi}$ and the lensed spectra, in a modified CAMB (arXiv:2407.07878) [src: Sect. 2].

#### Step B4 — two masses for two effects
<!-- key: step-b4-two-masses-for-two-effects -->

- **Expansion against clustering, by Taylor expansion** (Graham, Green & Meyers, arXiv:2508.20999): two parameters, each "constructed to match the effect of physical neutrino mass on the appropriate observables in the regime $\sum m_{\nu}>0$", each allowed to be negative and independent of the other, defined by $C_{L}^{\phi\phi}=\left.C_{L}^{\phi\phi}\right|_{\sum m_{\nu}=0}+\left.\frac{\partial C_{L}^{\phi\phi}}{\partial\sum m_{\nu}}\right|_{\sum m_{\nu}=0}\sum m_{\nu}^{\mathrm{clustering}}\,,$ (arXiv:2508.20999) [src: Eq. 2.4] and $(D_{X}(z)/r_{d})=\left.(D_{X}(z)/r_{d})\right|_{\sum m_{\nu}=0}+\left.\frac{\partial(D_{X}(z)/r_{d})}{\partial\sum m_{\nu}}\right|_{\sum m_{\nu}=0}\sum m_{\nu}^{\mathrm{BAO}}\,,$ (arXiv:2508.20999) [src: Eq. 2.5]. The derivatives are taken "holding fixed $\theta_{\star}$, $\Omega_{\mathrm{b}}h^{2}$, and $\Omega_{\mathrm{c}}h^{2}$", "subtly different" from $\sum\tilde m_\nu$, defined "with fixed $H_{0}$ and $\Omega_{m}h^{2}$", a choice made "to ensure that there is a non-vanishing impact" of the BAO parameter on BAO observables; the difference "has little impact" in their MCMC [src: Sect. 2.1, footnote 5]. "By construction, predictions of physical neutrino mass are recovered" for equal positive values [src: Sect. 2.1, text after Eq. 2.5]. `[der]` The expansion is linear in the mass, so this recovery holds to the order of the Taylor expansion, not exactly as in Eq. 7 of arXiv:2407.10965.
- **Background against perturbations, at the level of the equations** (Bertólez-Martínez et al., arXiv:2411.14524): the background mass $\sum m_\nu^{\rm Backg.}$ enters only through $w_\nu$, $\rho_{\nu}(a)=\rho_{\nu}(a_{1})\exp\left[-3\int_{a_{1}}^{a}\frac{1+w_{\nu}(a,\sum m_{\nu}^{\mathrm{Backg.}})}{a}\,\mathrm{d}a\right]\,,$ (arXiv:2411.14524) [src: Eq. 19], with the standard initial density of three light species set while they are ultra-relativistic [src: Sect. III.1, text after Eq. 20]; the perturbation mass $\sum m_\nu^{\rm Pert.}$ sets $c_{\rm eff}^2$ and σ in the fluid equations, Eqs. 9–10, implemented in CLASS [src: Sect. III.1]. `[der]` This split keeps both masses non-negative; it locates where a bound comes from rather than continuing the mass below zero. The resulting statement that the CMB bound "is mostly a background measurement" is in `results.md#massive-neutrinos-suppression-of-the-matter`.
- **Geometry against growth inside a Boltzmann code** (Ge et al. 2026, arXiv:2610.20977): splitting the expansion rate at the Boltzmann-code level, with a null test of ΛCDM; abstract only, in `open-questions.md#the-neutrino-mass-tension-as-seen-from-theory`.

## Variants and what they cost
<!-- key: variants-and-what-they-cost -->

| Parameter | What is continued | Held fixed | Exact for positive masses? | Paper and place |
|---|---|---|---|---|
| $\sum m_{\nu,\rm eff}$, exact | sign of the energy in background and Boltzmann hierarchy | — | yes | arXiv:2407.10965 [src: Eqs. 3–6] |
| $\sum m_{\nu,\rm eff}$, extrapolated | every observable, antisymmetrically about zero | $\omega_{\rm b},\omega_{\rm c},\theta_{\rm s},\tau,A_s,n_s$ | yes, "recovers exactly" | arXiv:2407.10965 [src: Eq. 7; Sect. II] |
| $\sum\tilde m_\nu$ | lensing spectrum only; $\Omega_m$ has no neutrino part | $H_0$, $\omega_m$, $\omega_b$ | "very similar, though not identical" | arXiv:2405.00836 [src: Sect. 2.2] |
| $\sum m_\nu^{\rm clustering}$, $\sum m_\nu^{\rm BAO}$ | lensing and BAO distances, separately, to first order | $\theta_\star$, $\Omega_{\rm b}h^2$, $\Omega_{\rm c}h^2$ | "by construction" | arXiv:2508.20999 [src: Eqs. 2.4–2.5; footnote 5] |
| $\sum m_\nu^{\rm Backg.}$, $\sum m_\nu^{\rm Pert.}$ | nothing continued; background and perturbation masses separated | — | yes when equal | arXiv:2411.14524 [src: Sect. II.1; Sect. III.1] |

- Pulido-Hernández & Cervantes-Cota use "a symmetric extension wrapper that allows for effective negative masses" "To mitigate prior-driven biases near the physical boundary" (arXiv:2603.13208) [src: abstract].
- Cozzumbo et al. introduce $\sum\tilde m_\nu$ "allowed to take negative values" together with two lensing parameters, one for the peak smoothing and one rescaling the lensing potential amplitude, and attribute the preference for negative masses "to an excess of gravitational lensing detected by late-time cosmological probes compared to that inferred from" Planck spectra (arXiv:2511.01967) [src: abstract].
- Graham, Green & Meyers state that "Both effects can be interpreted as negative neutrino mass, one describing the change to the expansion history and the other one describing enhanced lensing" (arXiv:2508.20999) [src: abstract].

For the massive-neutrino solver, the alternatives to the momentum grid with a fluid switch (the dispersive fluid and generalised hierarchy, the quasi-stationary approximation) are in `approximations.md#massive-neutrinos-in-boltzmann-codes-momentum`.

## Numbers
<!-- key: numbers -->

| Quantity | Value | Assumptions | Source | Place read |
|---|---|---|---|---|
| CLASS fluid approximation, CMB error | "only 0.02%" at l = 2750 | three species of 1 eV | arXiv:1104.2935 | [src: Sect. 3.5] |
| CLASS fluid approximation, P(k) error | "1 to 3%" for k in [0.05; 1] h/Mpc | three 1 eV neutrinos | arXiv:1104.2935 | [src: Sect. 3.5] |
| Momenta in the fast precision files | 8 or 5 (perturbations), 11 (background) | chi2pl0.1.pre, chi2pl1.pre | arXiv:1104.2935 | [src: Table 1; App. B] |
| Mass above which the fluid error "starts increasing significantly" | around 2 eV | default trigger | arXiv:1104.2935 | [src: App. B] |
| Extrapolation Eq. 7 against exact negative-mass calculation | within 0.1% | $\sum m_{\nu,\text{eff}}$ = −0.15 eV, linear theory, dark-matter P(k), z = 0 | arXiv:2407.10965 | [src: Fig. 1 caption] |
| Enhancement factor of the late-time suppression | approximately 7.5 | z_ν ≈ 100 | arXiv:2407.07878 | [src: Sect. 2.1, text after Eq. 2.2] |
| Suppression for the minimal sum | "two percent" | CMB-lensing context | arXiv:2407.07878 | [src: Sect. 2.1, text after Eq. 2.2] |
| Suppression of today's P(k) for 58 meV | "about 3%" | k ≫ k_fs, present day | arXiv:2508.20999 | [src: Sect. 2.1, text after Eq. 2.3] |

## What goes wrong
<!-- key: what-goes-wrong -->

- **Fluid approximation at large mass or for P(k).** The fluid switch "alters the CMB spectra on small angular scales ( $l\geq 2500$ )" only slightly, but P(k) is off by "1 to 3%" for three 1 eV neutrinos; the authors recommend it "for any value of the mass when computing CMB anisotropies, and only below a total mass of one or two eV's when computing the matter power spectrum" (arXiv:1104.2935) [src: Sect. 3.5]. Near 2 eV "the user should either turn off the approximation, or increase the value of the kτ trigger" [src: App. B]. The fast precision files give P(k) errors "of the order of a few per cents" for k in [0.05; 1] h/Mpc, and the permille files are needed for matter spectra [src: App. B].
- **Truncation at low $l_{\rm max}$ in synchronous gauge.** At $l_{\rm max}=3$ the dipole is gauge dependent, and the Ma–Bertschinger closure must be written for gauge-invariant quantities, Eq. 16 (arXiv:1104.2935) [src: Sect. 3.3]. <!-- num: not a value -->
- **Fixed parameters differ between negative-mass definitions.** $\sum\tilde m_\nu$ fixes $H_0$, $\omega_m$, $\omega_b$ (arXiv:2405.00836) [src: Sect. 2.2]; the split parameters fix $\theta_\star$, $\Omega_{\rm b}h^2$, $\Omega_{\rm c}h^2$ (arXiv:2508.20999) [src: Sect. 2.1, footnote 5]; Eq. 7 of Elbers et al. fixes $\omega_{\rm b}$, $\omega_{\rm c}$, $\theta_{\rm s}$, τ, $A_s$, $n_s$ (arXiv:2407.10965) [src: Sect. II]. Posteriors in two of these parameters are not directly comparable; a referee asks which one was used.
- **Lensing-only parameters miss the background.** With $\sum\tilde m_\nu$ "there is no neutrino contribution to" $\Omega_m$ (arXiv:2405.00836) [src: Sect. 2.2]; the expansion-history route is the separate $\sum m_\nu^{\rm BAO}$ (arXiv:2508.20999) [src: Eq. 2.5].
- **Two printed sizes of the minimal-mass suppression.** Green & Meyers write "a two percent suppression" in the CMB-lensing context (arXiv:2407.07878) [src: Sect. 2.1], and Craig et al. print the 58 meV spectrum as (1 − 0.02) times the massless one at general z (arXiv:2405.00836) [src: Eq. 2.7], while Graham, Green & Meyers give "about 3%" for the present-day spectrum (arXiv:2508.20999) [src: Sect. 2.1].
- `[der]` The suppression formula of Green & Meyers depends on z through its logarithm, so the two figures refer to different redshifts; quote the redshift with the number.
- **The optical depth.** Jhaveri, Karwal & Hu find that the tension "largely arises from the CMB lensing constraints on the calibration of the sound horizon" and "relies on the measurement of the reionization optical depth" τ; dropping these constraints "removes the neutrino tension at" the oscillation minimum "entirely" in ΛCDM (arXiv:2504.21813) [src: abstract]. A definition of a negative mass does not separate this from new physics.

## Reading list
<!-- key: reading-list -->

- Foundation of the equations: Ma & Bertschinger 1995, arXiv:astro-ph/9506072 — hierarchy, truncation, grid (Sects. 5.4, 8; in `formalism.md`).
- Code method: Lesgourgues & Tram 2011, arXiv:1104.2935 — quadrature, fluid approximation, shear closures, precision settings (Sects. 2–3, App. B).
- Background against perturbations: Bertólez-Martínez et al. 2024, arXiv:2411.14524 — $w_\nu$, $c_{\rm eff}^2$ and σ as the carriers of the mass (Sects. II, III.1).
- Effective mass continued to negative values: Elbers et al. 2024, arXiv:2407.10965 — Eqs. 3–7 (Sect. II).
- Lensing-only negative mass: Craig, Green, Meyers & Rajendran 2024, arXiv:2405.00836 (Sect. 2.2); Green & Meyers 2024, arXiv:2407.07878 (Sects. 2–2.1).
- Two-parameter split: Graham, Green & Meyers 2025, arXiv:2508.20999 (Sect. 2.1).
- Critique through the optical depth: Jhaveri, Karwal & Hu 2025, arXiv:2504.21813 (abstract read).
- Lensing anomaly as the driver: Cozzumbo et al. 2025, arXiv:2511.01967 (abstract read).

## Not verified
<!-- key: not-verified -->

- The quadrature rules of App. A of arXiv:1104.2935 (Gauss–Laguerre weights, adaptive sampling) and the sound-speed approximations of its Sects. 3.2 and 3.4 were not read.
- How CAMB samples momenta and truncates the massive-neutrino hierarchy was not read; no CAMB `[doc]` fact is given.
- The derivation of Eq. 2.2 of arXiv:2407.07878 (App. A of arXiv:2405.00836, "The Suppression of Clustering") was not read.
- The bodies of arXiv:2610.20977, arXiv:2603.13208, arXiv:2511.01967 and arXiv:2504.21813 were not read; their definitions are known from their abstracts only.
- Whether the effective-mass implementation of arXiv:2407.10965 is in the public CLASS was not checked.
