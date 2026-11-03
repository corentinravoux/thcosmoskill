# Formalism of neutrinos and light relics

Scope: definitions and governing equations of the cosmic neutrino background and other light relics: decoupling and $N_{\rm eff}$, massive-neutrino background and linear perturbations, free streaming, the phase shift, dark radiation and light thermal relics, interacting and decaying neutrinos.

Snapshot: 2026-11-03

## Conventions
<!-- key: conventions -->

The hub's atlas (`theoretical-cosmology/references/conventions.md`, sections "Units, Planck mass", "Gauge and names of the metric potentials" and "Fourier convention and power-spectrum normalisation") collects the general choices. The main sources of this skill use natural units (ħ = c = k_B = 1) and differ as follows. <!-- num: not a value -->

| Item | Lesgourgues & Pastor 2006 (arXiv:astro-ph/0603494) | Bennett et al. 2020 (arXiv:2012.02726) |
|---|---|---|
| Planck mass | full Planck mass $M_P$ in $H=\sqrt{\frac{8\pi\rho}{3M_{P}^{2}}}\,\,,$ (arXiv:astro-ph/0603494) [src: Eq. 8] | not needed for the definition |
| Temperature in $N_{\rm eff}$ | photon temperature today, through $\rho_\gamma$ in Eq. 11 (arXiv:astro-ph/0603494) [src: Sect. 3.2] | photon temperature T, in the limit T/m_e → 0 (arXiv:2012.02726) [src: Sect. 2, text after Eq. 1] |
| Neutrino distribution | Fermi–Dirac with chemical potential, Eq. 6 below | density matrix of the neutrino ensemble, evolved by the quantum kinetic equation [src: Sect. 2, text after Eq. 1] |

Perturbation conventions differ between the two standard references for massive-neutrino perturbations:

| Item | Lesgourgues & Pastor 2006 (arXiv:astro-ph/0603494) | Ma & Bertschinger 1995 (arXiv:astro-ph/9506072) |
|---|---|---|
| Signature | $(+,-,-,-)$, in $ds^{2}=g_{\mu\nu}dx^{\mu}dx^{\nu}=a^{2}(\tau)[(1+2\phi)d\tau^{2}-(1-2\psi)\delta_{ij}dx^{i}dx^{j}]~.$ (arXiv:astro-ph/0603494) [src: Eq. 25] | $(-,+,+,+)$, in $ds^{2}=a^{2}(\tau)\left\{-(1+2\psi)d\tau^{2}+(1-2\phi)dx^{i}dx_{i}\right\}\,.$ (arXiv:astro-ph/9506072) [src: Eq. 5] |
| Potential in $g_{00}$ | $\phi$ | $\psi$ |
| Spatial potential | $\psi$ | $\phi$ |
| Gauge | longitudinal (conformal Newtonian) [src: Sect. 4.3] | synchronous and conformal Newtonian [src: abstract] |
| Distribution function | $f(x^{i},P_{j},\tau)=f_{0}(q)[1+\Psi(x^{i},q_{j},\tau)]\qquad{\rm with}\qquad P_{j}=(1-\Psi)q_{j}~,$ (arXiv:astro-ph/0603494) [src: Eq. 89] | Legendre expansion $\Psi(\vec{k},\hat{n},q,\tau)=\sum_{l=0}^{\infty}(-i)^{l}(2l+1)\Psi_{l}(\vec{k},q,\tau)P_{l}(\hat{k}\cdot\hat{n})\,.$ (arXiv:astro-ph/9506072) [src: Eq. 54] |

- `[der]` The letters $\phi$ and $\psi$ swap roles between the two papers: the time–time potential is $\phi$ in Lesgourgues & Pastor and $\psi$ in Ma & Bertschinger. A hierarchy copied from one into code written in the notation of the other flips the potentials.

## Neutrino decoupling and the Standard-Model $N_{\rm eff}$
<!-- key: neutrino-decoupling-and-the-standard-model-n-rm -->

Equilibrium and decoupling (Lesgourgues & Pastor 2006, arXiv:astro-ph/0603494):

- Before decoupling the momentum spectrum is the Fermi–Dirac form $f_{\rm eq}(p)=\left[\exp\left(\frac{p-\mu_{\nu}}{T}\right)+1\right]^{-1}\,.$ (arXiv:astro-ph/0603494) [src: Eq. 6]; the BBN bounds on $\mu_{\nu_e}$ apply to all flavours because oscillations lead to approximate flavour equilibrium before BBN, so that "the contribution of a relic neutrino asymmetry can be safely ignored" [src: Sect. 3.1, text after Eq. 6].
- Decoupling is estimated by equating the weak rate $\Gamma_{\nu}=\langle\sigma_{\nu}\,n_{\nu}\rangle\,\,,$ (arXiv:astro-ph/0603494) [src: Eq. 7] with the expansion rate of Eq. 8; with numerical factors set to unity, $\Gamma_{\nu}\approx G_{F}^{2}T^{5}$ and $H\approx T^{2}/M_{P}$ give the "rough estimate" $T_{\rm dec}\approx 1$ MeV, and more accurate calculations give "slightly higher values" that are flavour dependent [src: Sect. 3.1, text after Eq. 8].
- In instantaneous decoupling, with the entropy of $e^{\pm}$ annihilation going to photons only, $T_{\gamma}/T_{\nu}=(11/4)^{1/3}\simeq 1.40102$ (arXiv:astro-ph/0603494) [src: Sect. 3.1, inline, text after Eq. 8]; the number density per flavour is $n_{\nu}=\frac{3}{11}\;n_{\gamma}=\frac{6\zeta(3)}{11\pi^{2}}\;T_{\gamma}^{3}~,$ [src: Eq. 9], "113 neutrinos and antineutrinos of each flavour per cm3" today [src: Sect. 3.1, text after Eq. 9].
- Energy density in the two limits: $\displaystyle\rho_{\nu}(m_{\nu}\ll T_{\nu})=\displaystyle\frac{7\pi^{2}}{120}\left(\frac{4}{11}\right)^{4/3}\;T_{\gamma}^{4}~,\displaystyle\rho_{\nu}(m_{\nu}\gg T_{\nu})=\displaystyle m_{\nu}n_{\nu}~.$ (arXiv:astro-ph/0603494) [src: Eq. 10]; in between it "should in principle be calculated numerically" [src: Sect. 3.1, text before Eq. 10].
- The relic density of active neutrinos does not depend on whether they are Dirac or Majorana, because wrong-helicity Dirac states are not brought into equilibrium at MeV temperatures [src: Sect. 3.1, text before Eq. 9]. <!-- num: not a value -->

Definition of $N_{\rm eff}$:

- Lesgourgues & Pastor: $\rho_{\rm R}=\left[1+\frac{7}{8}\left(\frac{4}{11}\right)^{4/3}\,N_{\rm eff}\right]\,\rho_{\gamma}\,\,,$ valid "when neutrino decoupling is complete" and "as long as all neutrinos are relativistic" (arXiv:astro-ph/0603494) [src: Eq. 11, text after].
- Bennett et al. define the Standard-Model benchmark by the ratio of energy densities in the limit $T/m_e\to 0$, with T the photon temperature: $\left.\frac{\rho_{\nu}}{\rho_{\gamma}}\right|_{T/m_{e}\to 0}\equiv\frac{7}{8}\Big(\frac{4}{11}\Big)^{4/3}N_{\rm eff}^{\rm SM},$ (arXiv:2012.02726) [src: Eq. 1].
- The precision computation solves the continuity equation for the total energy density and the quantum kinetic equation for the neutrino density matrix, with oscillations and scattering, over $T\sim{\cal O}(100)\to{\cal O}(0.01)$ MeV (arXiv:2012.02726) [src: Sect. 2, text after Eq. 1].
- Non-instantaneous decoupling: decoupling and $e^{\pm}$ annihilation are close in time, so residual interactions distort the spectra, more for larger energies, and the comoving photon temperature rises slightly less; with oscillations the comoving photon temperature is larger by a factor 1.3978 "instead of 1.40102 in the approximation of instantaneous decoupling" (arXiv:astro-ph/0603494) [src: Sect. 3.1, text after Fig. 3]. The distortions "only have small consequences on the evolution of cosmological perturbations, and for many purposes they can be safely neglected" [src: Sect. 3.1, last paragraph].

## Light thermal relics and $\Delta N_{\rm eff}$
<!-- key: light-thermal-relics-and-delta-n-rm-eff -->

- A light thermal relic X that decoupled at temperature $T_F$ contributes $\Delta N_{\rm eff}=\frac{4}{7}g_{X,\star}\left(\frac{T_{X}}{T_{\nu}}\right)^{4}=\frac{4}{7}g_{X,\star}\left(\frac{43}{4g_{\star}(T_{F})}\right)^{4/3}\ ,$ where $g_{X,\star}$ includes "an additional factor of 7/8 for fermionic particles" and $g_\star(T_F)$ counts the relativistic degrees of freedom in equilibrium at decoupling (Dvorkin et al. 2022, arXiv:2203.07943) [src: Eq. 2, text after]. The derivation rests on comoving entropy conservation after decoupling [src: Sect. 2.1, text before Eq. 2].
- In that review $T_{\nu}=(4/11)^{1/3}T_{\gamma}$ and the radiation-era expansion rate is $H^{2}=\frac{\pi^{2}}{90}g_{\star}(T)\frac{T^{4}}{M_{\mathrm{pl}}^{2}}$ (arXiv:2203.07943) [src: Sect. 2.1, inline, text after Eq. 2]. <!-- num: not a value -->
- Freeze-out by a higher-dimension operator: for $\Gamma\sim\lambda^{2}T^{2n+1}$, $\Gamma/H\sim\lambda^{2}T^{2n-1}M_{\mathrm{pl}}$, and for $n\geq 1$ the minimum coupling for equilibrium "scales as an inverse power of the temperature" (arXiv:2203.07943) [src: Sect. 2.1, inline, text after Eq. 2].
- Rethermalisation: below electroweak symmetry breaking, production through a massive Standard-Model fermion scales as $\Gamma_{n}\propto T^{2n+1}$ with $n\leq 0$, weaker than $H\propto T^{2}$, so an out-of-equilibrium species can recouple at low temperature; for the dimension-5 coupling $\partial_{\mu}\phi\,\bar{\psi}\gamma^{\mu}\gamma^{5}\psi$ of a pseudo-Nambu–Goldstone boson the rate is $\Gamma_{0}\propto T$ (arXiv:2203.07943) [src: Sect. 2.2, inline, text after Eq. 2]. Bounds from avoiding recoupling "are usually weaker than the freeze-out bounds" but "do not make any assumptions about the reheating temperature" [src: Sect. 2.2].

## Massive neutrinos: background
<!-- key: massive-neutrinos-background -->

- Today's density parameter: $\Omega_{\nu}=\frac{\rho_{\nu}}{\rho_{\rm c}}=\frac{\sum_{i}m_{i}}{93.14\,h^{2}~{\rm eV}}~,$ (Lesgourgues & Pastor 2006, arXiv:astro-ph/0603494) [src: Eq. 12]. It "can be safely applied" to non-degenerate masses, because oscillation data imply that at least two states are non-relativistic today [src: Sect. 3.3, text after Eq. 12]; for high precision the relation "must be evaluated numerically using the distorted distributions" [src: Sect. 3.3, footnote 1]. The same paper uses m_ν = (ω_ν/N_ν) 93.2 eV in its derivation of the power suppression [src: Sect. 4.5.6, text before Eq. 143]: the coefficient is printed as 93.14 in Eq. 12 and 93.2 there.
- Mass orderings: oscillations measure |Δm²₃₁| ≈ 2.55·10⁻³ eV² and Δm²₂₁ ≈ 7.5·10⁻⁵ eV²; in the normal ordering ($\Delta m^{2}_{31}>0$) $\sum m_{\nu}\gtrsim 0.06$ eV, in the inverted ordering ($\Delta m^{2}_{31}<0$) $\sum m_{\nu}\gtrsim 0.10$ eV (Di Valentino, Gariazzo & Mena 2024, arXiv:2404.19322) [src: Sect. III]. As printed, the review writes the atmospheric splitting as "|Δm²₃₁| = |m₃² − m₁²| = ≈" and says that "the sign of $\lvert\Delta m^{2}_{31}\rvert$ is unknown"; the sentence that follows defines the orderings by the sign of $\Delta m^{2}_{31}$ [src: Sect. III].
- The present relic density is 339 neutrinos and antineutrinos per cm³ for three flavours (arXiv:astro-ph/0603494) [src: Sect. 3.3].
- Non-relativistic transition: when $m=\langle p\rangle=3T_{\nu}$, at $a_{0}/a=(1+z)=2.0\times 10^{3}(m/1\,\mathrm{eV})$ (arXiv:astro-ph/0603494) [src: Sect. 4.5.2, inline, text after Eq. 96].
- Time of equality with neutrinos counted as radiation: $a_{\rm eq}=\frac{\omega_{\rm r}}{\omega_{\rm b}+\omega_{\rm cdm}}~,$ with $\omega_{\rm r}$ from Eq. 11 at $N_{\rm eff}=3.04$; at fixed $\omega_{\rm m}$, $a_{\rm eq}$ grows as $[1-f_{\nu}]^{-1}$ (arXiv:astro-ph/0603494) [src: Eq. 145, text after].
- Two effects of the mass can be separated: the background effect, tied to the energy in neutrino masses, and the "kinematic" effect on perturbations, tied to free streaming; Bertólez-Martínez et al. introduce two effective masses, $\sum m_\nu^\mathrm{Backg.}$ and $\sum m_\nu^\mathrm{Pert.}$, for them (arXiv:2411.14524) [src: abstract].

## Massive-neutrino perturbations and free streaming
<!-- key: massive-neutrino-perturbations-and-free -->

Vlasov equation (Lesgourgues & Pastor 2006, arXiv:astro-ph/0603494; their conventions, Eq. 25 above):

- $f$ obeys the collisionless Boltzmann equation ${Df\over d\tau}={\partial f\over\partial\tau}+{dx^{i}\over d\tau}{\partial f\over\partial x^{i}}+{dq\over d\tau}{\partial f\over\partial q}+{dn_{i}\over d\tau}{\partial f\over\partial n_{i}}=0\,.$ (arXiv:astro-ph/0603494) [src: Eq. 98]; at first order in Fourier space $\dot{\Psi}-i\,{q\over\epsilon}\,(\vec{k}\cdot\hat{n})\,\Psi=-\left(\dot{\psi}+i\,{\epsilon\over q}\,(\vec{k}\cdot\hat{n})\,\phi\right){\partial\ln f_{0}\over\partial\ln q}\,.$ [src: Eq. 100].

Legendre hierarchy (Ma & Bertschinger 1995, arXiv:astro-ph/9506072; their conventions, Eq. 5 above; $\epsilon=\epsilon(q,\tau)=\sqrt{q^{2}+m_{\nu}^{2}a^{2}}$ [src: Sect. 5.4, inline, text after Eq. 53]):

- Synchronous gauge: $\dot{\Psi}_{0}=-{qk\over\epsilon}\Psi_{1}+{1\over 6}\dot{h}{d\ln f_{0}\over d\ln q}\,,$ $\dot{\Psi}_{1}={qk\over 3\epsilon}\left(\Psi_{0}-2\Psi_{2}\right)\,,$ $\dot{\Psi}_{2}={qk\over 5\epsilon}\left(2\Psi_{1}-3\Psi_{3}\right)-\left({1\over 15}\dot{h}+{2\over 5}\dot{\eta}\right){d\ln f_{0}\over d\ln q}\,,$ $\dot{\Psi}_{l}={qk\over(2l+1)\epsilon}\left[l\Psi_{l-1}-(l+1)\Psi_{l+1}\right]\,,\quad l\geq 3\,.$ (arXiv:astro-ph/9506072) [src: Eq. 56].
- Conformal Newtonian gauge: $\dot{\Psi}_{0}=-{qk\over\epsilon}\Psi_{1}-\dot{\phi}{d\ln f_{0}\over d\ln q}\,,$ $\dot{\Psi}_{1}={qk\over 3\epsilon}\left(\Psi_{0}-2\Psi_{2}\right)-{\epsilon\,k\over 3q}\psi{d\ln f_{0}\over d\ln q}\,,$ $\dot{\Psi}_{l}={qk\over(2l+1)\epsilon}\left[l\Psi_{l-1}-(l+1)\Psi_{l+1}\right]\,,\quad l\geq 2\,.$ (arXiv:astro-ph/9506072) [src: Eq. 57].
- Truncation: $\Psi_{\nu\,(l_{\rm max}+1)}\approx{(2l_{\rm max}+1)\epsilon\over qk\tau}\,\Psi_{\nu\,l_{\rm max}}-\Psi_{\nu\,(l_{\rm max}-1)}\ .$ (arXiv:astro-ph/9506072) [src: Eq. 58]; the shear that enters the Einstein equations is $(\bar{\rho}_{h}+\bar{P}_{h})\sigma_{h}={8\pi\over 3}a^{-4}\int q^{2}dq\,{q^{2}\over\epsilon}f_{0}(q)\Psi_{2}\,.$ [src: Eq. 55, last row].

Free streaming (Lesgourgues & Pastor 2006, arXiv:astro-ph/0603494):

- $k_{FS}(t)=\left(\frac{4\pi G\bar{\rho}(t)a^{2}(t)}{v_{\rm th}^{2}(t)}\right)^{1/2},\qquad\lambda_{FS}(t)=2\pi\frac{a(t)}{k_{FS}(t)}=2\pi\sqrt{2\over 3}\frac{v_{\rm th}(t)}{H(t)}~.$ (arXiv:astro-ph/0603494) [src: Eq. 93], with the thermal velocity after the non-relativistic transition $v_{\rm th}\equiv\frac{\langle p\rangle}{m}\simeq\frac{3T_{\nu}}{m}=\frac{3T_{\nu}^{0}}{m}\left(\frac{a_{0}}{a}\right)\simeq 150(1+z)\left(\frac{1\,\mathrm{eV}}{m}\right){\rm km}\,{\rm s}^{-1}~,$ [src: Eq. 94].
- During matter or Λ domination: $\displaystyle\lambda_{FS}(t)=\displaystyle 7.7\frac{1+z}{\sqrt{\Omega_{\Lambda}+\Omega_{m}(1+z)^{3}}}\left(\frac{1\,\mathrm{eV}}{m}\right)h^{-1}\mathrm{Mpc}~,$ $\displaystyle k_{FS}(t)=\displaystyle 0.82\frac{\sqrt{\Omega_{\Lambda}+\Omega_{m}(1+z)^{3}}}{(1+z)^{2}}\left(\frac{m}{1\,\mathrm{eV}}\right)h\,\mathrm{Mpc}^{-1},$ (arXiv:astro-ph/0603494) [src: Eqs. 95–96].
- The comoving free-streaming wavenumber passes through a minimum at the non-relativistic transition, $k_{\rm nr}\simeq 0.018\,\,\Omega_{\rm m}^{1/2}\left(\frac{m}{1\,\mathrm{eV}}\right)^{1/2}h\,\mathrm{Mpc}^{-1}~.$ (arXiv:astro-ph/0603494) [src: Eq. 97]; modes with k < k_nr "are never affected by free-streaming" [src: Sect. 4.5.2, last paragraph].
- Growth on scales $k\gg k_{\rm nr}$ after the transition, for a time-independent $f_\nu$: $\delta_{\rm cdm}\propto a^{p_{+}}\simeq a^{1-\frac{3}{5}f_{\nu}}~,$ (arXiv:astro-ph/0603494) [src: Eq. 134], and $\delta_{\rm cdm}\propto[a\,g(a)]^{p_{+}}\simeq[a\,g(a)]^{1-\frac{3}{5}f_{\nu}}~.$ during dark-energy domination [src: Eq. 136]; the constant-$f_\nu$ approximation "is not strictly valid in the case of several massive non-degenerate neutrinos" [src: Sect. 4.5.6, text after Eq. 136].
- Ratio of CDM perturbations today, "in a crude approximation": $\frac{\delta_{\rm cdm}^{f_{\nu}}[a_{0}]}{\delta_{\rm cdm}^{f_{\nu}=0}[a_{0}]}=(1-f_{\nu})^{1/2}\left(\frac{a_{0}\,g(a_{0})}{a_{\rm nr}}\right)^{-\frac{3}{5}f_{\nu}}.$ (arXiv:astro-ph/0603494) [src: Eq. 141]. The power-spectrum suppression that follows is in `results.md`.

## The phase shift from free-streaming radiation
<!-- key: the-phase-shift-from-free-streaming-radiation -->

Conventions of Baumann et al. 2015 (arXiv:1508.06342): conformal Newtonian gauge with $(-,+,+,+)$ signature, ${\rm d}s^{2}=a^{2}(\tau)\left[(-1-2\Phi){\rm d}\tau^{2}+(1-2\Psi)\delta_{ij}{\rm d}x^{i}{\rm d}x^{j}\right]\,,$ [src: Eq. 1.4] and $\Phi_{\pm}\equiv\Phi\pm\Psi\,.$ [src: Eq. 1.5]; $d_a$ is the number overdensity per coordinate volume, d_a ≡ δ_a − 3Ψ, following Bashinsky & Seljak [src: Sect. 1, Notation and Conventions]. <!-- num: not a value -->

- Photon density, baryons neglected ($c_{\gamma}^{2}\approx\frac{1}{3}$): $\ddot{d}_{\gamma}-c_{\gamma}^{2}\thinspace\nabla^{2}d_{\gamma}=\nabla^{2}\Phi_{+}\,,$ (arXiv:1508.06342) [src: Eq. 2.1; Sect. 2.2, text before Eq. 2.17].
- Solution with $y=c_\gamma k\tau$: $d_{\gamma}(y)=\Big[d_{\gamma,{\rm in}}+c_{\gamma}^{-2}A(y)\Big]\cos y-c_{\gamma}^{-2}B(y)\sin y\,,$ (arXiv:1508.06342) [src: Eq. 2.18], with $A(y)\equiv\int^{y}_{0}{\rm d}y^{\prime}\,\Phi_{+}(y^{\prime})\hskip 1.0pt\sin y^{\prime}\,,$ [src: Eq. 2.19] and $B(y)\equiv\int^{y}_{0}{\rm d}y^{\prime}\,\Phi_{+}(y^{\prime})\hskip 1.0pt\cos y^{\prime}\,.$ [src: Eq. 2.20]. A non-zero $B$ in the limit $y\to\infty$ gives a constant phase shift $\sin\theta=\frac{B}{\sqrt{\left(A+c_{\gamma}^{2}\hskip 1.0ptd_{\gamma,{\rm in}}\right)^{2}+B^{2}}}\,.$ [src: Eq. 2.21], the limit and radiation domination being "a good approximation" for the high-ℓ modes [src: Sect. 2.2, text before Eq. 2.21].
- Conditions (arXiv:1508.06342) [src: Sect. 2.2]: $B=0$ as long as the even part $\Phi^{(S)}_{+}(y)$ is analytic and $e^{iy}\Phi^{(S)}_{+}(y)$ falls faster than $y^{-1}$; a phase shift therefore requires either (i) a mode travelling faster than $c_\gamma$, or (ii) non-analytic behaviour, i.e. non-adiabatic fluctuations. Adiabatic initial conditions are analytic at kτ = 0 [src: Sect. 2.2]. For adiabatic modes a phase shift thus needs free-streaming relativistic particles, neutrinos or other dark radiation, while isocurvature fluctuations are the other route [src: abstract].
- Free-streaming fraction $\epsilon_{X}\equiv\frac{\rho_{X}}{\rho_{\gamma}+\rho_{X}}\,=\,\frac{N_{\rm eff}}{a_{\nu}+N_{\rm eff}}\,.$ (arXiv:1508.06342) [src: Eq. 2.53], and at leading order $\theta\approx 0.191\pi\,\epsilon_{X}+\mathcal{O}(\epsilon_{X}^{2})\,,$ [src: Eq. 2.67], "consistent with the result of Bashinsky & Seljak" [src: Sect. 2.4.2, text after Eq. 2.67].
- Multipole shift: $\delta\ell\simeq(\theta/\pi)\,\Delta\ell_{\text{peak}}$ with $\Delta\ell_{\text{peak}}\sim 330$; for $N_{\rm eff}=3.046$ the shift from ordinary neutrinos relative to a neutrinoless universe is $\delta\ell_{\nu}\approx 26$, and $\delta\ell_{\delta N_{\rm eff}}\approx 5.0\times\delta N_{\rm eff}\,,$ (arXiv:1508.06342) [src: Eq. 2.68, text before], a result "likely subject to a 20 to 30 percent error" [src: Sect. 2.4.2, text after Eq. 2.68]. The E-mode spectrum shows "precisely the same phase shift" [src: Sect. 2.4.2, text after Eq. 2.67].
- The shift was identified by Bashinsky & Seljak as a "unique phase shift" that "for adiabatic initial conditions cannot be caused by any other standard physics", traced to "neutrino free-streaming velocity exceeding the sound speed of the photon-baryon plasma"; the gravity of neutrino perturbations also suppresses the acoustic peaks for $l\gtrsim 200$ (arXiv:astro-ph/0310198) [src: abstract].
- Interactions: for temperature-dependent scattering rates with gradual decoupling, the phase shift "maintains the same functional form as the free-streaming template, with only the asymptotic amplitude decreasing" for stronger interactions (Montefalcone et al. 2025, arXiv:2509.20363) [src: abstract]. Compared with free streaming, self-interacting radiation shifts the spectra to higher ℓ; scattering of radiation with dark matter amplifies the shift, in proportion to the interacting dark-matter abundance when the radiation dominates the interacting pair around equality (Ghosh, Ho & Tsai 2024, arXiv:2405.08064) [src: abstract].

## Interacting and decaying neutrinos
<!-- key: interacting-and-decaying-neutrinos -->

The models and their status are in `models.md`; this section gives the pieces of formalism that enter a Boltzmann code.

- Self-interactions through a scalar φ, $\mathcal{L}_{\rm int}=g_{ij}\bar{\nu}_{i}\nu_{j}\varphi,$ (Kreisch et al. 2019, arXiv:1902.00534) [src: Eq. 1], reduce in the contact limit to the effective coupling $G_{\rm eff}\equiv|g_{\nu}|^{2}/m_{\varphi}^{2}$ [src: Sect. II, inline, text after Eq. 3]. The contact limit is "an excellent approximation at the energy scale probed by the CMB for $m_{\varphi}\gtrsim 1$ keV" [src: Sect. II].
- In the Boltzmann hierarchy the collision term "is projected onto momentum-averaged multipoles" with coefficients $\alpha_\ell$; for scattering mediated by a light scalar, Mogensen, Hannestad & Tram give an exact "rational-plus-$\pi^2$" expression for every multipole and an approximation for CLASS (arXiv:2606.03395) [src: abstract].
- Flavour-specific self-interactions with mixing: from the quantum kinetic equations one obtains Boltzmann hierarchies for the mass states, and most scenarios are "well approximated by a combined fluid approach" (arXiv:2609.13821) [src: abstract].
- Decay ν_H → ν_l + φ: the complete Boltzmann equations for $\nu_H$, $\nu_l$ and φ with decays and inverse decays, at background and first-order level, are derived from first principles by Barenboim et al. (arXiv:2011.01502) [src: abstract]. The anisotropy-loss rate in the ultra-relativistic limit is ∼ (1/τ₀)(m_νH/E_νH)⁵ [src: abstract], with the daughter-mass factor of arXiv:2203.09075 [src: abstract] (`models.md`).

## Light but massive relics and light sterile neutrinos
<!-- key: light-but-massive-relics-and-light-sterile -->

- A relic that decoupled while relativistic keeps its Fermi–Dirac or Bose–Einstein shape, with $T_{X}(z)=T_{X}^{(0)}(1+z)$ and $p_{X}\approx 3T_{X}$; it becomes non-relativistic when $p_{X}(z)\approx m_{X}$ and moves from the radiation budget ($\Delta N_{\rm eff}$) to the matter budget, behaving as hot dark matter (Dvorkin et al. 2022, arXiv:2203.07943) [src: Sect. 4.2, inline, text after Eq. 2]. <!-- num: not a value -->
- Free-streaming scale, for a fiducial Planck 2018 cosmology: $k_{\rm fs}\approx\frac{0.1\,h\rm Mpc^{-1}}{\sqrt{1+z}}\frac{1.95\,\rm K}{T_{X}}\frac{m_{X}}{0.1\,\rm eV}$ (arXiv:2203.07943) [src: Eq. 3]; abundance $\omega_{X}=\Omega_{X}\,h^{2}\approx\frac{m_{X}}{93.14\,\rm eV}\left(\frac{T_{X}}{1.95\,\rm K}\right)^{3}$ [src: Eq. 4]. The position of the suppression ($k_{\rm fs}$) and its depth (proportional to $\omega_X$) together give $m_X$ and $T_X$ [src: Sect. 4.2, text after Eq. 4].
- Model-insensitive parametrisation: three independent physical quantities govern the dominant effects of a LiMR on observables, and the "Squished Relics" family spans different phase-space distributions; Planck "is not sensitive to the shape" of the distribution for relics that become non-relativistic at $z_{NR}<10^5$ (DePorzio, Imig & Shelton 2026, arXiv:2607.12021) [src: abstract].
- Light sterile neutrinos are produced by active–sterile oscillations, which start when $\Delta m^{2}/2E$ exceeds $H(t)$, and by collisions; with large enough mixing they thermalise and contribute to $N_{\rm eff}$ (arXiv:2203.07943) [src: Sect. 6.2]. In the 3+1 scheme with the full 4×4 mixing matrix and momentum-dependent kinetic equations, the fourth state is "fully thermalised (N_eff ≃ 4)" for the mixing preferred by short-baseline experiments (Gariazzo et al. 2019, arXiv:1905.11290) [src: abstract].

## Not verified
<!-- key: not-verified -->

- The quantum kinetic equations for the neutrino density matrix (arXiv:2012.02726, Sect. 2.2) were not transcribed; only their collision integrals were seen.
- The relaxation-time form of the self-interaction collision term and the coefficients $\alpha_\ell$ (arXiv:2606.03395) were not read beyond the abstract.
- Neutrino asymmetries: the bounds on the degeneracy parameter quoted in arXiv:astro-ph/0603494 (Sect. 3.1) date from 2006 and were not updated.
