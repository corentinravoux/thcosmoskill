# G2 re-read sheet — thcosmo-dark-energy

Re-read each item in the cited paper at the place named (L4). Verdict: `ok`, `wrong` (say what), `unclear`. Pass: no `wrong` left in parts 1–2 after fixes; zero `wrong` in part 3.

## 1. SKILL.md and conventions block (all)

| # | file:line | kind | tool status | statement | verdict | note |
|---|---|---|---|---|---|---|
| 1 | plugin/skills/thcosmo-dark-energy/SKILL.md:8 | SKILL.md | marked | Snapshot 2026-11-03. Every equation and number names its paper and the place it was read; no equation or number is derived by an agent. Conventions: Copeland, Sami & Tsujikawa use the full Planck mass m_pl = 1.22 × 10¹⁹  | | |
| 2 | plugin/skills/thcosmo-dark-energy/SKILL.md:28 | SKILL.md | ok | Cut-off estimate: $\rho_{\rm vac}\approx\frac{k_{\rm max}^{4}}{16\pi^{2}}\,.$ with $k_{\rm max}=m_{\rm pl}$ gives $\rho_{\rm vac}\approx 10^{74}\,{\rm GeV}^{4}\,,$ against $\rho_\Lambda\approx 10^{-47}$ GeV⁴ (arXiv:hep-t | | |
| 3 | plugin/skills/thcosmo-dark-energy/SKILL.md:30 | SKILL.md | ok | A canonical field has $-1\leq w_{\phi}\leq 1$ (arXiv:hep-th/0603057) [src: Sect. V.1, text after Eq. 106]; for an exponential potential the field-dominated attractor has $w_{\phi}=-1+\lambda^{2}/3$ and accelerates for $\ | | |
| 4 | plugin/skills/thcosmo-dark-energy/SKILL.md:32 | SKILL.md | ok | k-essence stability needs $\xi_{1}\,\equiv\,p_{,X}+2Xp_{,XX}\,\geq\,0,~~\xi_{2}\,\equiv\,p_{,X}\,\geq\,0,$ (arXiv:hep-th/0603057) [src: Eq. 145], with $c_{s}^{2}\equiv\frac{p_{,X}}{\rho_{,X}}=\frac{\xi_{2}}{\xi_{1}}\,,$  | | |
| 5 | plugin/skills/thcosmo-dark-energy/SKILL.md:33 | SKILL.md | ok | No-go: one perfect fluid, or one field $L(\phi,\partial\phi)$ minimally coupled in GR, cannot cross w = −1 stably (arXiv:astro-ph/0407107; arXiv:2606.01360) [src: abstract; text before Eq. 2]; the adiabatic sound speed $ | | |
| 6 | plugin/skills/thcosmo-dark-energy/SKILL.md:35 | SKILL.md | ok | An interaction mimics a crossing: $w_{\rm de}^{\rm eff}=w-\frac{aQ}{3\mathcal{H}\rho_{\rm de}},$ (arXiv:2606.21826) [src: Eq. 9]. | | |
| 7 | plugin/skills/thcosmo-dark-energy/SKILL.md:37 | SKILL.md | ok | Axion-like early dark energy $V(\theta)=m^{2}f^{2}[1-\cos(\theta)]^{n},$ (arXiv:2302.09032) [src: Eq. 6] is a "toy potential" that needs cancelled lower harmonics [src: Sects. III.1, VII.2]. | | |
| 8 | plugin/skills/thcosmo-dark-energy/SKILL.md:38 | SKILL.md | ok | The post-DESI shape is $w_0>-1$, $w_a<0$, Quintom-B, robust to the parameterisation but with a significance that depends on the SN compilation (arXiv:2606.21826) [src: Sect. II.2]; one critical review traces the DES Y5 p | | |
| 9 | plugin/skills/thcosmo-dark-energy/SKILL.md:55 | SKILL.md | ok | Quoting "120 orders of magnitude" as the Standard-Model prediction for the vacuum energy (arXiv:1205.3365) [src: abstract]. | | |
| 10 | plugin/skills/thcosmo-dark-energy/references/formalism.md:14 | conventions | ok | \vert  Signature \vert  mostly plus: the Newtonian limit is written with $g_{00}=-1-2\Phi$ [src: Sect. IV.1, text after Eq. 59] \vert  | | |
| 11 | plugin/skills/thcosmo-dark-energy/references/formalism.md:15 | conventions | ok | \vert  Planck mass \vert  full Planck mass $m_{\rm pl}=1.22\times 10^{19}$ GeV [src: Sect. IV.2, text after Eq. 69]; Friedmann equation with 8πG in Sect. V (Eq. 102) and with κ² in Sects. VI–IX (Eq. 180) \vert  | | |
| 12 | plugin/skills/thcosmo-dark-energy/references/formalism.md:18 | conventions | ok | \vert  Equation of state \vert  $w_{\phi}=p/\rho$ of the field; Λ has $w=-1$ <!-- eq: notation --> \vert  | | |
| 13 | plugin/skills/thcosmo-dark-energy/references/formalism.md:16 | conventions | ok | \vert  Kinetic term \vert  $(\nabla\phi)^{2}=g^{\mu\nu}\partial_{\mu}\phi\partial_{\nu}\phi$ in the quintessence action [src: Sect. V.1, text after Eq. 97]; k-essence uses $X$, see below \vert  | | |
| 14 | plugin/skills/thcosmo-dark-energy/references/formalism.md:17 | conventions | ok | \vert  Time variable \vert  e-folds $N={\rm ln}\,(a)$ in the dynamical-system analysis [src: Sect. VI.1.2, text after Eq. 168] \vert  | | |

## 2. Items the tools could not pass (all)

| # | file:line | kind | tool status | statement | verdict | note |
|---|---|---|---|---|---|---|
| 1 | plugin/skills/thcosmo-dark-energy/references/approximations.md:40 | equation | contained | $m_{\rm pl}=1.22\times 10^{19}$ (arXiv:hep-th/0603057, Eq. 69) | | |
| 2 | plugin/skills/thcosmo-dark-energy/references/formalism.md:26 | equation | contained | $m_{\rm pl}=1.22\times 10^{19}$ (arXiv:hep-th/0603057, Eq. 69) | | |
| 3 | plugin/skills/thcosmo-dark-energy/references/formalism.md:27 | equation | contained | $\rho_{\rm vac}=\frac{1}{2}\int_{0}^{\infty}\frac{{\rm d}^{3}{\bf k}}{(2\pi)^{3}}\sqrt{k^{2}+m^{2}}=\frac{1}{4\pi^{2}}\int_{0}^{\infty}{\rm d}k\,k^{2}\sqrt{k^{2}+m^{2}}\,.$ (arXiv:hep-th/0603057, Eq. 68) | | |
| 4 | plugin/skills/thcosmo-dark-energy/references/formalism.md:27 | equation | contained | $k_{\rm max}=m_{\rm pl}$ (arXiv:hep-th/0603057, Eq. 70) | | |
| 5 | plugin/skills/thcosmo-dark-energy/references/formalism.md:27 | equation | contained | $\rho_{\rm vac}\approx 10^{74}\,{\rm GeV}^{4}\,,$ (arXiv:hep-th/0603057, Eq. 70) | | |
| 6 | plugin/skills/thcosmo-dark-energy/references/formalism.md:28 | equation | contained | $\rho_{\rm vac}=\frac{1}{2}(-1)^{2j}(2j+1)\int_{0}^{\infty}\frac{{\rm d}^{3}{\bf k}}{(2\pi)^{3}}\sqrt{k^{2}+m^{2}}=\frac{(-1)^{2j}(2j+1)}{4\pi^{2}}\int_{0}^{\infty}{\rm d}k\,k^{2}\sqrt{k^{2}+m^{2}}\,.$ (arXiv:hep-th/0603057, Eq. 71) | | |
| 7 | plugin/skills/thcosmo-dark-energy/references/formalism.md:29 | equation | contained | $\mu\simeq 3\times 10^{-25}$ (arXiv:1205.3365, Eq. 516) | | |
| 8 | plugin/skills/thcosmo-dark-energy/references/formalism.md:29 | equation | contained | $\rho_{{}_{\rm vac}}\simeq-2\times 10^{8}\,\mbox{GeV}^{4}+\rho_{{}_{\rm B}}+\rho_{{}_{\rm vac}}^{{}_{\rm EW}}+\rho_{{}_{\rm vac}}^{{}_{\rm QCD}}+\cdots.$ (arXiv:1205.3365, Eq. 516) | | |
| 9 | plugin/skills/thcosmo-dark-energy/references/formalism.md:39 | equation | contained | $a\propto t^{p}$ (arXiv:hep-th/0603057, Eq. 111) | | |
| 10 | plugin/skills/thcosmo-dark-energy/references/formalism.md:39 | equation | contained | $V(\phi)=V_{0}\exp\left(-\sqrt{\frac{16\pi}{p}}\frac{\phi}{m_{\rm pl}}\right)\,,$ (arXiv:hep-th/0603057, Eq. 111) | | |
| 11 | plugin/skills/thcosmo-dark-energy/references/formalism.md:45 | equation | contained | $\frac{{\rm d}\lambda}{{\rm d}N}=-\sqrt{6}\lambda^{2}(\Gamma-1)x\,,$ (arXiv:hep-th/0603057, Eq. 186) | | |
| 12 | plugin/skills/thcosmo-dark-energy/references/formalism.md:53 | equation | unreadable | $\lambda^{2}>24\gamma^{2}/(9\gamma-2)$ (arXiv:hep-th/0603057, Eq. ) | | |
| 13 | plugin/skills/thcosmo-dark-energy/references/formalism.md:66 | equation | contained | $S=\int{\rm d}^{4}x\sqrt{-g}\,p(\phi,X)\,,$ (arXiv:hep-th/0603057, Eq. 115) | | |
| 14 | plugin/skills/thcosmo-dark-energy/references/formalism.md:66 | equation | contained | $X\equiv-(1/2)(\nabla\phi)^{2}$ (arXiv:hep-th/0603057, Eq. 115) | | |
| 15 | plugin/skills/thcosmo-dark-energy/references/formalism.md:78 | equation | unreadable | $L=L(\phi,\partial_{\mu}\phi\partial^{\mu}\phi)$ (arXiv:2606.01360, Eq. 2) | | |
| 16 | plugin/skills/thcosmo-dark-energy/references/formalism.md:90 | equation | contained | $Q=H\xi(\rho_{d}+\rho_{c})$ (arXiv:1603.08299, Eq. 15) | | |
| 17 | plugin/skills/thcosmo-dark-energy/references/formalism.md:90 | equation | contained | $\frac{dr}{dt}=-3\Gamma Hr,\qquad\qquad\Gamma=-\omega_{d}-\xi^{2}\frac{(\rho_{c}+\rho_{d})^{2}}{3\rho_{c}\rho_{d}},$ (arXiv:1603.08299, Eq. 15) | | |
| 18 | plugin/skills/thcosmo-dark-energy/references/formalism.md:107 | equation | contained | $V(\theta)=m^{2}f^{2}[1-\cos(\theta)]^{n},$ (arXiv:2302.09032, Eq. 6) | | |
| 19 | plugin/skills/thcosmo-dark-energy/references/formalism.md:107 | equation | contained | $\theta\equiv\phi/f$ (arXiv:2302.09032, Eq. 6) | | |
| 20 | plugin/skills/thcosmo-dark-energy/references/formalism.md:113 | equation | contained | $c_{s}^{2}\equiv\frac{p_{,X}}{\rho_{,X}}$ (arXiv:hep-th/0603057, Eq. 147) | | |
| 21 | plugin/skills/thcosmo-dark-energy/references/models.md:53 | equation | contained | $c_{s}^{2}\equiv\frac{p_{,X}}{\rho_{,X}}$ (arXiv:hep-th/0603057, Eq. 147) | | |
| 22 | plugin/skills/thcosmo-dark-energy/references/results.md:10 | equation | contained | $\rho_{\rm vac}\approx 10^{74}$ (arXiv:hep-th/0603057, Eq. 67,68,69,70) | | |
| 23 | plugin/skills/thcosmo-dark-energy/references/approximations.md:28 | number | unreadable | The thawing slow-roll limit of Scherrer & Sen gives a w(a) accurate to δw ≲ 0.005 for w < −0.9 for the potentials they tested (arXiv:0712.3450) [src: abstract]; the Caldwell–Linder thawing and freezing bounds are valid f | | |
| 24 | plugin/skills/thcosmo-dark-energy/references/approximations.md:64 | number | found-elsewhere | Λ problem: a paper quoting "120 orders of magnitude" says which estimate it uses (arXiv:1205.3365) [src: abstract]. | | |
| 25 | plugin/skills/thcosmo-dark-energy/references/formalism.md:30 | number | unreadable | Martin's statement of the problem is a mismatch of "something like 54 orders of magnitude (but much less than the 122 orders of magnitude often quoted in the literature)" between Eq. 516 and the measured value (arXiv:120 | | |
| 26 | plugin/skills/thcosmo-dark-energy/references/models.md:32 | number | unreadable | **Predictions:** w starts at −1 and grows, w' > 0 (arXiv:astro-ph/0505494) [src: text after Fig. 1]; with Ω_de ≈ 0.7, thawing models must satisfy 1 + w ≳ 0.004 (arXiv:astro-ph/0505494) [src: text after Fig. 2]; for nearl | | |
| 27 | plugin/skills/thcosmo-dark-energy/references/models.md:94 | number | unreadable | **Observational status:** Q = βH₀ρ_de with SPT + DESI DR2 + DES Y5: β = −0.4170 ± 0.1220, a 3.4σ deviation from zero, weakening to 2.1σ with Pantheon+ (Li et al., arXiv:2510.11363) [src: abstract]. Constant w with the sa | | |
| 28 | plugin/skills/thcosmo-dark-energy/references/open-questions.md:13 | number | unreadable | Size: the quoted 120–122 orders of magnitude use a cut-off; renormalised estimates give a smaller but still huge mismatch (arXiv:1205.3365, Sect. X.2; arXiv:2606.20778, abstract). | | |
| 29 | plugin/skills/thcosmo-dark-energy/references/open-questions.md:36 | number | unreadable | Against: 2.1σ with Pantheon+ instead (arXiv:2510.11363) [src: abstract]; sign-switching solutions imply negative past dark-energy densities "which may be unphysical" (arXiv:2601.03122) [src: abstract]; with GRBs and DESI | | |
| 30 | plugin/skills/thcosmo-dark-energy/references/open-questions.md:57 | number | unreadable | "The vacuum energy is 120 (or 122) orders of magnitude too large": a cut-off estimate; renormalised estimates give a smaller but still huge mismatch (arXiv:1205.3365, Sect. X.2; arXiv:2606.20778, abstract). | | |
| 31 | plugin/skills/thcosmo-dark-energy/references/results.md:10 | number | unreadable | Size of the mismatch: a Planck-scale cut-off gives $\rho_{\rm vac}\approx 10^{74}$ GeV⁴ against ρ_Λ ≈ 10⁻⁴⁷ GeV⁴ (Copeland et al., arXiv:hep-th/0603057) [src: Eqs. 67, 70]. A properly renormalised free-field estimate is  | | |
| 32 | plugin/skills/thcosmo-dark-energy/references/results.md:35 | number | unreadable | Size of the preference, as one critical review states it: "mild-to-moderate", "below the 3σ level in most cases", up to ∼3.8σ with DESI DR2 + CMB + DES Y5 or Union3; the DES Y5 driven preference is attributed to low-z SN | | |
| 33 | plugin/skills/thcosmo-dark-energy/references/results.md:51 | number | unreadable | \vert  2012 \vert  "122 orders of magnitude" replaced by a renormalised estimate \vert  arXiv:1205.3365 [src: abstract] \vert  standing (arXiv:2606.20778) \vert  | | |

## 3. Random draw from tool-passed items (seed 1106)

| # | file:line | kind | tool status | statement | verdict | note |
|---|---|---|---|---|---|---|
| 1 | plugin/skills/thcosmo-dark-energy/references/formalism.md:104 | equation | exact | $\rho_{\rm EDE}(a)=\rho_{\rm EDE,0}e^{3\int_{a}^{1}[1+w_{\rm EDE}(a)]da/a}\,.$ (arXiv:2302.09032, Eq. 20) | | |
| 2 | plugin/skills/thcosmo-dark-energy/references/formalism.md:88 | equation | exact | $w_{\rm c}^{\rm eff}=\frac{aQ}{3\mathcal{H}\rho_{\rm c}}.$ (arXiv:2606.21826, Eq. 10) | | |
| 3 | plugin/skills/thcosmo-dark-energy/references/formalism.md:79 | equation | exact | $c_{s}^{2}=\frac{\delta\hat{p}}{\delta\hat{\rho}}.$ (arXiv:2606.01360, Eq. 5) | | |
| 4 | plugin/skills/thcosmo-dark-energy/references/formalism.md:36 | equation | exact | $S=\int{\rm d}^{4}x\sqrt{-g}\left[-\frac{1}{2}(\nabla\phi)^{2}-V(\phi)\right]\,,$ (arXiv:hep-th/0603057, Eq. 97) | | |
| 5 | plugin/skills/thcosmo-dark-energy/references/models.md:158 | number | found-at-place | **Observational status:** with a hard 2σ lower prior on $H_0$ from local measurements, Δχ²_bf ∼ −41.08 against ΛCDM (arXiv:1906.08275) [src: abstract]; the result rests on that prior. | | |
| 6 | plugin/skills/thcosmo-dark-energy/references/formalism.md:104 | equation | exact | $w_f=(n-1)/(n+1)$ (arXiv:2302.09032, Eq. 20) | | |
| 7 | plugin/skills/thcosmo-dark-energy/references/formalism.md:66 | equation | exact | $p=-X-V(\phi)$ (arXiv:hep-th/0603057, Eq. 147) | | |
| 8 | plugin/skills/thcosmo-dark-energy/references/models.md:54 | equation | exact | $\vert X\vert \gg X^2$ (arXiv:hep-th/0603057, Eq. 147) | | |
| 9 | plugin/skills/thcosmo-dark-energy/references/approximations.md:33 | equation | exact | $w(a)=w_{0}+w_{a}(1-a)$ (arXiv:2606.01360, Eq. 1) | | |
| 10 | plugin/skills/thcosmo-dark-energy/references/models.md:138 | number | found-at-place | **Predictions:** with $\Omega_\Lambda=0.73$ as input, w = −0.90 today (arXiv:hep-th/0403127) [src: abstract]; with the Hubble or particle horizon as cut-off the model does not accelerate, which is why the event horizon i | | |
| 11 | plugin/skills/thcosmo-dark-energy/references/formalism.md:40 | equation | exact | $\epsilon=-\dot{H}/H^{2}$ (arXiv:hep-th/0603057, Eq. 104) | | |
| 12 | plugin/skills/thcosmo-dark-energy/references/formalism.md:37 | equation | exact | $\frac{\ddot{a}}{a}=-\frac{8\pi G}{3}\left[\dot{\phi}^{2}-V(\phi)\right]\,.$ (arXiv:hep-th/0603057, Eq. 103) | | |
| 13 | plugin/skills/thcosmo-dark-energy/references/formalism.md:45 | equation | exact | $x\equiv\frac{\kappa\dot{\phi}}{\sqrt{6}H}\,,~~y\equiv\frac{\kappa\sqrt{V}}{\sqrt{3}H}\,,$ (arXiv:hep-th/0603057, Eq. 183) | | |
| 14 | plugin/skills/thcosmo-dark-energy/references/formalism.md:76 | equation | exact | $p=-X-V(\phi)$ (arXiv:hep-th/0603057, Eq. 147) | | |
| 15 | plugin/skills/thcosmo-dark-energy/references/formalism.md:26 | equation | exact | $\Lambda\approx H_{0}^{2}=(2.13h\times 10^{-42}\,{\rm GeV})^{2}\,.$ (arXiv:hep-th/0603057, Eq. 66) | | |
| 16 | plugin/skills/thcosmo-dark-energy/references/formalism.md:117 | number | found-at-place | First constraint on c_s² for time-varying w with DESI DR2 + Planck 2018 + Union3, in the PPF framework: log₁₀ c_s² = −3.00 (+2.9, −0.99), with constant-w models "unconstrained"; an EFT analysis favours c_s² ∼ 0.3 or 0.4  | | |
| 17 | plugin/skills/thcosmo-dark-energy/references/formalism.md:67 | equation | exact | $w_{\phi}=\frac{p}{\rho}=\frac{1-X}{1-3X}\,.$ (arXiv:hep-th/0603057, Eq. 125) | | |
| 18 | plugin/skills/thcosmo-dark-energy/references/formalism.md:108 | equation | exact | $V(\psi,\phi)=\frac{\lambda}{4}\psi^{4}+\frac{1}{2}\beta M^{2}\psi^{2}-\frac{1}{3}\alpha M\psi^{3}+\frac{1}{2}m^{2}\phi^{2}+\frac{1}{2}\gamma\phi^{2}\psi^{2}.$ (arXiv:2302.09032, Eq. 10) | | |
| 19 | plugin/skills/thcosmo-dark-energy/references/formalism.md:89 | equation | exact | $\dot{\rho}_{c}+3H\rho_{c}=Q,$ (arXiv:1603.08299, Eq. 12) | | |
| 20 | plugin/skills/thcosmo-dark-energy/references/formalism.md:104 | equation | exact | $f_{\rm EDE}\equiv\rho_{\rm EDE}/\rho_{\rm tot}$ (arXiv:2302.09032, Eq. 21) | | |
| 21 | plugin/skills/thcosmo-dark-energy/references/formalism.md:105 | equation | exact | $h_v=\psi_N$ (arXiv:2302.09032, Eq. 23) | | |
| 22 | plugin/skills/thcosmo-dark-energy/references/formalism.md:88 | equation | exact | $w_{\rm de}^{\rm eff}=w-\frac{aQ}{3\mathcal{H}\rho_{\rm de}},$ (arXiv:2606.21826, Eq. 9) | | |
| 23 | plugin/skills/thcosmo-dark-energy/references/models.md:43 | number | found-at-place | **Observational status:** Planck + DESI DR2 BAO: support at 2.5σ against 3.1σ for the CPL fit; with SN above 3σ for Union3 and DES Y5, 2.1σ with Pantheon+, 1.7σ adding DESI full-shape power spectrum and bispectrum (arXiv | | |
| 24 | plugin/skills/thcosmo-dark-energy/references/open-questions.md:52 | number | found-at-place | SN Ia calibration at the few×10⁻² mag level is a stated requirement for claims of evolving w (arXiv:2602.05368) [src: abstract]. | | |
| 25 | plugin/skills/thcosmo-dark-energy/references/formalism.md:55 | equation | exact | $w_{\rm eff}=w_{\phi}=-1+\lambda^{2}/3$ (arXiv:hep-th/0603057, Eq. 196) | | |
| 26 | plugin/skills/thcosmo-dark-energy/references/formalism.md:44 | equation | exact | ${\cal L}=\frac{1}{2}\epsilon\dot{\phi}^{2}+V(\phi)\,,$ (arXiv:hep-th/0603057, Eq. 179) | | |
| 27 | plugin/skills/thcosmo-dark-energy/references/models.md:165 | number | found-at-place | **Predictions:** z† ≳ 1.1 for monotonic expansion when consistent with the CMB; H0 ≈ 74.5 km s⁻¹ Mpc⁻¹ for z† = 1.5 (arXiv:2108.09239) [src: abstract]. | | |
| 28 | plugin/skills/thcosmo-dark-energy/references/formalism.md:106 | equation | exact | $c_{a}^{2}=\frac{\rho^{\prime}_{\rm EDE}}{P^{\prime}_{\rm EDE}}=w_{\rm EDE}-\frac{1}{3}\frac{dw_{\rm EDE}/d\ln a}{1+w_{\rm EDE}}$ (arXiv:2302.09032, Eq. 24) | | |
| 29 | plugin/skills/thcosmo-dark-energy/references/formalism.md:86 | equation | exact | ${\rho}_{\rm de}^{\prime}+3\mathcal{H}(1+w)\rho_{\rm de}=aQ,$ (arXiv:2606.21826, Eq. 3) | | |
| 30 | plugin/skills/thcosmo-dark-energy/references/formalism.md:45 | equation | exact | $\epsilon x^{2}+y^{2}+\frac{\kappa^{2}\rho_{m}}{3H^{2}}=1\,.$ (arXiv:hep-th/0603057, Eq. 187) | | |
| 31 | plugin/skills/thcosmo-dark-energy/references/formalism.md:106 | equation | exact | $\dot{p}=c_{a}^{2}\dot{\rho}$ (arXiv:2302.09032, Eq. 24) | | |
| 32 | plugin/skills/thcosmo-dark-energy/references/models.md:78 | equation | exact | $S=\int d^{4}x\sqrt{-g}\left[-\frac{1}{2}\nabla_{\mu}\phi\nabla^{\mu}\phi+\frac{1}{2}\nabla_{\mu}\sigma\nabla^{\mu}\sigma-V(\phi,\sigma)\right].$ (arXiv:2606.01360, Eq. 11) | | |
| 33 | plugin/skills/thcosmo-dark-energy/references/formalism.md:26 | equation | exact | $\rho_{\Lambda}=\frac{\Lambda m_{{\rm pl}}^{2}}{8\pi}\approx 10^{-47}\,{\rm GeV}^{4}\,.$ (arXiv:hep-th/0603057, Eq. 67) | | |
| 34 | plugin/skills/thcosmo-dark-energy/references/models.md:54 | equation | exact | $p=-X+X^2$ (arXiv:hep-th/0603057, Eq. 147) | | |
| 35 | plugin/skills/thcosmo-dark-energy/references/formalism.md:68 | equation | exact | $\xi_{3}\,\equiv\,-p_{,\phi\phi}\,\geq\,0\,.$ (arXiv:hep-th/0603057, Eq. 146) | | |
| 36 | plugin/skills/thcosmo-dark-energy/references/formalism.md:79 | equation | exact | $\theta^{\prime}=-\Big(\mathcal{H}+\frac{\bar{p}^{\prime}}{\bar{\rho}+\bar{p}}\Big)\theta+k^{2}\Big(\frac{\delta p}{\bar{\rho}+\bar{p}}+\Psi\Big)~,$ (arXiv:2606.01360, Eq. 3) | | |
| 37 | plugin/skills/thcosmo-dark-energy/references/formalism.md:45 | equation | exact | $w_{\phi}\equiv\frac{p_{\phi}}{\rho_{\phi}}=\frac{\epsilon x^{2}-y^{2}}{\epsilon x^{2}+y^{2}}\,,$ (arXiv:hep-th/0603057, Eq. 188) | | |
| 38 | plugin/skills/thcosmo-dark-energy/references/formalism.md:45 | equation | exact | $\Omega_{\phi}\equiv\frac{\kappa^{2}\rho_{\phi}}{3H^{2}}=\epsilon x^{2}+y^{2}\,.$ (arXiv:hep-th/0603057, Eq. 189) | | |
| 39 | plugin/skills/thcosmo-dark-energy/references/formalism.md:67 | equation | exact | $p(\phi,X)=K(\phi)X+L(\phi)X^{2}\,.$ (arXiv:hep-th/0603057, Eq. 121) | | |
| 40 | plugin/skills/thcosmo-dark-energy/references/open-questions.md:35 | number | found-at-place | For: Q = βH₀ρ_de at 3.4σ with SPT + DESI DR2 + DES Y5 (arXiv:2510.11363) [src: abstract]. | | |
| 41 | plugin/skills/thcosmo-dark-energy/references/formalism.md:79 | equation | exact | $c_{a}^{2}=\frac{\delta p}{\delta\rho}\Big\vert _{\rm{adiabatic}}=\frac{\bar{p}^{\prime}}{\bar{\rho}^{\prime}}=w-\frac{w^{\prime}}{3\mathcal{H}(1+w)}.$ (arXiv:2606.01360, Eq. 4) | | |
| 42 | plugin/skills/thcosmo-dark-energy/references/results.md:20 | number | found-at-place | "Limits of quintessence": with Ω_de ≈ 0.7, thawing models must satisfy 1 + w ≳ 0.004 and freezing models 1 + w ≳ 0.01, about a 0.2% difference from Λ in distance to z = 1 (Caldwell & Linder, arXiv:astro-ph/0505494) [src: | | |
| 43 | plugin/skills/thcosmo-dark-energy/references/formalism.md:37 | equation | exact | $\dot{\phi}^{2}<V(\phi)$ (arXiv:hep-th/0603057, Eq. 103) | | |
| 44 | plugin/skills/thcosmo-dark-energy/references/approximations.md:27 | equation | exact | $\epsilon=-\dot{H}/H^{2}$ (arXiv:hep-th/0603057, Eq. 104) | | |
| 45 | plugin/skills/thcosmo-dark-energy/references/formalism.md:105 | equation | exact | $\frac{d}{d\eta}\left(\frac{\delta_{\rm EDE}}{1+w_{\rm EDE}}\right)=-\left(\theta_{\rm EDE}+h_{\delta}^{\prime}\right)-3\frac{a^{\prime}}{a}(c_{s}^{2}-c_{a}^{2})\left(\frac{\delta_{\rm EDE}}{1+w_{\rm E$ (arXiv:2302.09032, Eq. 22) | | |
| 46 | plugin/skills/thcosmo-dark-energy/references/models.md:90 | equation | exact | $Q=\beta H_{0}\rho_{\rm c},\qquad Q=\beta H_{0}\rho_{\rm de}.$ (arXiv:2606.21826, Eq. 6) | | |
| 47 | plugin/skills/thcosmo-dark-energy/references/models.md:113 | equation | exact | $V(\theta)=m^{2}f^{2}[1-\cos(\theta)]^{n},$ (arXiv:2302.09032, Eq. 6) | | |
| 48 | plugin/skills/thcosmo-dark-energy/references/models.md:14 | equation | exact | $w_{\rm eff}=w_{\phi}=-1+\lambda^{2}/3$ (arXiv:hep-th/0603057, Eq. 196) | | |
| 49 | plugin/skills/thcosmo-dark-energy/references/formalism.md:67 | equation | exact | $p(\phi,X)=f(\phi)(-X+X^{2})\,,$ (arXiv:hep-th/0603057, Eq. 123) | | |
| 50 | plugin/skills/thcosmo-dark-energy/references/formalism.md:89 | equation | exact | $\dot{\rho}_{d}+3H(1+\omega_{d})\rho_{d}=-Q\,,$ (arXiv:1603.08299, Eq. 13) | | |
| 51 | plugin/skills/thcosmo-dark-energy/references/formalism.md:79 | equation | exact | $\delta p=c_{s}^{2}\delta\rho+(c_{s}^{2}-c_{a}^{2})\Big[3\mathcal{H}(1+w)\bar{\rho}\Big]\frac{\theta}{k^{2}}.$ (arXiv:2606.01360, Eq. 8) | | |
| 52 | plugin/skills/thcosmo-dark-energy/references/formalism.md:87 | equation | exact | $Q=\beta H\rho_{\rm c},\qquad Q=\beta H\rho_{\rm de},$ (arXiv:2606.21826, Eq. 5) | | |
| 53 | plugin/skills/thcosmo-dark-energy/references/formalism.md:88 | equation | exact | ${\rho}_{\rm de}^{\prime}=aQ$ (arXiv:2606.21826, Eq. 6) | | |
| 54 | plugin/skills/thcosmo-dark-energy/references/models.md:146 | number | found-at-place | **Parameters:** ν and $\tilde\nu$, "expected to be ≲ O(10⁻⁴–10⁻²)" from the masses and non-minimal couplings of the fields, "ultimately determined from observations"; many analyses assume $\tilde{\nu}=\nu/2$ (arXiv:2504. | | |
| 55 | plugin/skills/thcosmo-dark-energy/references/models.md:90 | equation | exact | ${\rho}_{\rm c}^{\prime}+3\mathcal{H}\rho_{\rm c}=-aQ,$ (arXiv:2606.21826, Eq. 3,4) | | |
| 56 | plugin/skills/thcosmo-dark-energy/references/formalism.md:36 | equation | exact | $\ddot{\phi}+3H\dot{\phi}+\frac{{\rm d}V}{{\rm d}\phi}=0\,.$ (arXiv:hep-th/0603057, Eq. 98) | | |
| 57 | plugin/skills/thcosmo-dark-energy/references/formalism.md:123 | number | found-at-place | Freezing-region upper bound of Caldwell & Linder (arXiv:astro-ph/0505494): only the "possible lower bound" w' = 1.5w(1+w) was read [src: Fig. 2 caption]. | | |
| 58 | plugin/skills/thcosmo-dark-energy/references/formalism.md:36 | equation | exact | $\rho=-T_{0}^{0}=\frac{1}{2}\dot{\phi}^{2}+V(\phi)\,,~~~p=T_{i}^{i}=\frac{1}{2}\dot{\phi}^{2}-V(\phi)\,.$ (arXiv:hep-th/0603057, Eq. 101) | | |
| 59 | plugin/skills/thcosmo-dark-energy/references/formalism.md:44 | equation | exact | $\epsilon\ddot{\phi}+3H\dot{\phi}+\frac{{\rm d}V}{{\rm d}\phi}=0\,.$ (arXiv:hep-th/0603057, Eq. 182) | | |

Upper bound on the error rate of tool-passed items with 0 errors in 59: 5.0 % (95 %, one-sided).
