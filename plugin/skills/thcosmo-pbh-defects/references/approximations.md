# Approximations, their validity, and traps in PBH and defect theory

Scope: the approximations PBH-formation and defect-network calculations rely on, the regime in which a paper validates each and the error it quotes, how each fails, convention traps and printed slips, and the list a referee checks. The approximations of the gravitational-wave spectra (loop models, emission per loop, wall GW templates) are in `thcosmo-cosmological-gravitational-waves`; those of stochastic inflation and the tail of $\zeta$ in `thcosmo-inflation`.

Snapshot: 2026-11-13

## Spherical symmetry of the collapsing peak
<!-- key: spherical-symmetry-of-the-collapsing-peak -->

- **Assumes:** high peaks of a Gaussian field are close to spherical; thresholds are computed from spherically symmetric Misner–Sharp simulations (arXiv:2211.05767) [src: Sects. II.2–II.4].
- **Validated:** for radiation, "a recent work of numerical PBH formation beyond spherical symmetry ... has shown that the threshold is not substantially affected by slight deviations from sphericity" (arXiv:2211.05767) [src: Sect. II.4, inline, text after Eq. II.29]; a 3+1 code finds for a spherical Gaussian profile "a collapse threshold $\mu_c \simeq 0.7958$ ... consistent with previous spherically symmetric results" (arXiv:2608.13206) [src: abstract, inline].
- **Fails:** "The situation can be different when non-zero angular momentum is considered, or for a softer equation of state than that of a radiation fluid" (arXiv:2211.05767) [src: Sect. II.4, text after Eq. II.29]; for neighbouring peaks "the maximum curvature amplitude alone does not determine the collapse outcome" (arXiv:2609.03051) [src: abstract]; in matter domination with triaxial initial data the threshold moves by "a factor of 2" (dust, before the code crashes) or "an order of magnitude" (collisionless particles) against the analytic estimate (arXiv:2609.14218) [src: abstract]. Including non-sphericity "significantly increases the inferred amplitude of the primordial power spectrum" (arXiv:2603.23025) [src: abstract].
- **Cite:** arXiv:2211.05767; arXiv:2608.13206; arXiv:2609.03051.

## Gradient expansion and the leading-order compaction function
<!-- key: gradient-expansion-and-the-leading-order -->

- **Assumes:** the length scale of the perturbation is much larger than the Hubble radius, $\epsilon\ll 1$; "Essentially it considers that the characteristic length scale of the inhomogeneity, say $L$, is much larger than the Hubble horizon" (arXiv:2211.05767) [src: Sect. II.3, text before Eq. II.11].
- **Validated:** the compaction function at $\mathcal{O}(\epsilon^{2})$ is "a time-independent quantity for superhorizon fluctuations as long as $w$ is constant" (arXiv:2211.05767) [src: Sect. II.3, text after Eq. II.19]; higher orders are in its Ref. [77] [src: Sect. II.3, text after Eq. II.12e].
- **Fails:** when $w$ varies (QCD epoch, thermal history; arXiv:2211.05767, Sects. II.11–II.12, not read here). <!-- num: not a value -->
- **Cite:** Shibata & Sasaki 1999 (arXiv:gr-qc/9905064) for the formulation; arXiv:1809.02127.

## Critical scaling of the PBH mass
<!-- key: critical-scaling-of-the-pbh-mass -->

- **Assumes:** $M=\mathcal{K}M_{H}(t_{H})\big(\delta_{\mathrm{m}}-\delta_{\mathrm{c}}\big)^{\mspace{-2mu}\gamma}$ (arXiv:2211.05767) [src: Eq. II.30], a scaling law "according to the critical phenomena in gravitational collapse" [src: Sect. II.5, inline, text before Eq. II.30].
- **Validated:** "when the amplitude of the perturbation $\delta$ is close to the critical value $\delta_{\mathrm{m}}-\delta_{\mathrm{c}}\lesssim 10^{-2}$" (arXiv:2211.05767) [src: Sect. II.5, text before Eq. II.30].
- **Error quoted:** beyond the critical regime the deviation "have been estimated to be $\mathcal{O}(10\,\text{--}\,15)\%$", "usually neglected" because such fluctuations are "exponentially rarer" (arXiv:2211.05767) [src: Sect. II.5, inline, last paragraph]; the closed Press–Schechter form "assumed that the scaling law for the PBH mass is always accurate even when $\delta_{\mathrm{m}}\gg\delta_{\mathrm{c}}$, which is actually not true" [src: Sect. III.1, inline, text after Eq. III.6].
- **Fails:** for scalar-field collapse with discrete self-similarity, the scaling law is modulated, giving "approximately log-periodic features in mass" (arXiv:2608.21834) [src: abstract].
- **Cite:** arXiv:gr-qc/9402041; arXiv:astro-ph/9709072.

## Press–Schechter against peak theory; window functions
<!-- key: press-schechter-against-peak-theory-window -->

- **Assumes (PS):** a Gaussian distribution of the compaction peak and collapse above $\delta_{\mathrm c}$, with a factor 2 "introduced to avoid the well-know under-counting" (arXiv:2211.05767) [src: Sect. III.1, first paragraph and text after Eq. III.6].
- **Validated:** PS and peak theory "remain largely similar for the monochromatic case" (arXiv:2603.23025) [src: abstract]; using $\Delta$ rather than $\mathcal R_c$, PS and peaks theory are "in close agreement in the region of interest" (arXiv:1405.7023) [src: abstract].
- **Fails:** for a broad spectrum they "differ", "current constraints remain sensitive to the choice of statistical formalism" (arXiv:2603.23025) [src: abstract]; the factor 2 is not justified for PBHs because "the PBH case is non-Markovian, even when the sharp-k filter Window function is adopted" (arXiv:2509.25871) [src: abstract]; avoiding a window function removes "the suppresion associated with a window function" (as printed) and raises the abundance "by many orders of magnitude" (arXiv:1805.03946) [src: abstract].
- **Cite:** arXiv:1805.03946; arXiv:2603.23025; arXiv:2509.25871.

## Gaussian statistics and the nonlinear $\delta$–$\zeta$ relation
<!-- key: gaussian-statistics-and-the-nonlinear-delta -->

- **Assumes:** Gaussian $\zeta$ and a density contrast linear in the Laplacian of $\zeta$.
- **Error quoted:** the nonlinear relation alone requires the amplitude of $\mathcal P_\zeta$ to be larger "by a factor ${\cal O}(2÷3)$" (arXiv:1904.00970) [src: abstract, inline] or "a factor of $\sim2$" (arXiv:1904.00984) [src: abstract, inline] for the same abundance. A shift from $\zeta_{\mathrm G}=1$ to $0.7$ changes the Gaussian probability by $\frac{P_{\mathrm{G}}(\zeta_{\mathrm{G}}=0.7)}{P_{\mathrm{G}}(\zeta_{\mathrm{G}}=1)}\simeq 1.2\times 10^{11}$ (arXiv:2211.05767) [src: Eq. II.126], for the illustrative $\sigma_0^2=10^{-2}$ [src: Sect. II.10.1, inline, text before Eq. II.126].
- **Fails:** perturbative non-Gaussianity "is intrinsically flawed when considering broad spectra" (arXiv:2211.01728) [src: abstract]; stochastic kicks make compaction profiles "very spiky", with abundance changes "up to 36 orders of magnitude, depending on the mass range and collapse criterion" in the ultra-slow-roll models studied (arXiv:2510.09303) [src: abstract].
- **Cite:** arXiv:1904.00970; arXiv:1904.00984; arXiv:2211.01728.

## Monochromatic mass function and the horizon-mass factor
<!-- key: monochromatic-mass-function-and-the-horizon -->

- **Assumes:** "all have the same mass or at least a mass width $\Delta M$ no larger than $M$"; the mass at formation is a fraction $\gamma$ of the horizon mass, and "$\gamma$ is rather uncertain" (arXiv:2002.12778) [src: Sect. I.3, text after Eqs. 4 and 8].
- **Fails:** Eq. 4 "does not apply for PBHs which form in an early matter-dominated (dust-like) era or for the low mass PBHs forming through critical collapse"; the $\beta$–$\Omega_{\rm PBH}$ relation changes for "a dust-like stage, a second inflationary phase" and other non-standard histories (arXiv:2002.12778) [src: Sect. I.3, text after Eqs. 4 and 8]. Whether an extended mass function "makes it easier or more difficult for PBHs to provide the DM in the various mass windows has been the subject of some dispute" [src: Sect. I.1, fourth paragraph].
- **Cite:** arXiv:2002.12778.

## Semiclassical Hawking evaporation
<!-- key: semiclassical-hawking-evaporation -->

- **Assumes:** self-similar semiclassical evaporation throughout; "the evaporation constraints assume the validity of Hawking radiation, even though there is still no direct observational evidence for this" (arXiv:2002.12778) [src: Sect. I.1, fifth paragraph]; $f(M)$ in Eq. 15 "should really be the weighted average of $f(M)$ over the lifetime", "well approximated by $f(M)$ unless one is close to a particle mass threshold" [src: Sect. I.4.1, last paragraph].
- **Fails:** memory burden takes evaporation "out of the semiclassical regime latest by half-decay time" (arXiv:2402.14069) [src: abstract]; the onset is often modelled as instantaneous, and the rate-combination rule changes BBN bounds (arXiv:2606.04707) [src: abstract].
- **Cite:** arXiv:2006.00011; arXiv:2402.14069.

## Nambu–Goto approximation for strings
<!-- key: nambu-goto-approximation-for-strings -->

- **Assumes:** zero-thickness strings with action $S=-\mu\int d^{2}\sigma\sqrt{-\det(g_{\mu\nu}x^{\mu}_{,a}x^{\nu}_{,b})},$ (arXiv:0911.1345) [src: Eq. 10], loops decaying only by gravitational radiation.
- **Error quoted:** against Abelian-Higgs simulations, Nambu–Goto values "underestimate the mean string separation by about 25%, and overestimate $\bar v^2$ by about 10%" (arXiv:1703.06696) [src: abstract].
- **Fails:** loops "formed by intersections of infinite strings formed from random-field initial conditions" decay "with lifetime proportional to their initial rest-frame length"; "An implication is that one cannot use the Nambu-Goto model to derive robust constraints on the tension of field theory strings" (arXiv:2103.16248) [src: abstract]; whether gravitational radiation is the primary energy loss was already "an issue that needs to be resolved" in 2009 (arXiv:0911.1345) [src: Sect. 4, text after Eq. 23].
- **Cite:** arXiv:1703.06696; arXiv:2103.16248; the VOS model and its calibration in `thcosmo-cosmological-gravitational-waves`.

## Exact scaling of domain-wall networks
<!-- key: exact-scaling-of-domain-wall-networks -->

- **Assumes:** $\rho_{\rm wall}(t)=\mathcal{A}\frac{\sigma}{t},$ with constant $\mathcal A$ (arXiv:1703.02576) [src: Eq. 2.17]; the review carries out its analysis "by assuming that the evolution of domain walls is described by the exact scaling law" [src: Sect. 2.2, footnote 2].
- **Error quoted:** simulations give $\rho_{\rm wall}\propto t^{-\nu}$ with $\nu$ slightly off 1, "unclear whether this deviation represents some physical effect or just a numerical artifact" [src: Sect. 2.2, inline, footnote 2]; ignorance of initial conditions "may affect predictions for the energy density of gravitational waves by the factor five" (arXiv:2509.25367) [src: abstract, inline].
- **Fails:** with friction from light particles "we must carefully evaluate the effect of the friction force" (arXiv:1703.02576) [src: Sect. 2.2, text after Eq. 2.16]; the annihilation time rests on $C_{\rm ann}$, which depends on "the choice of the criterion to determine the decay time" [src: Sect. 2.3, text after Eq. 2.28].
- **Cite:** arXiv:1703.02576; arXiv:2509.25367; arXiv:2607.18107.

## Convention traps and printed slips
<!-- key: convention-traps-and-printed-slips -->

- **Three meanings of $\gamma$, two of $f(M)$:** in Carr et al. $\gamma$ is the fraction of the horizon mass (arXiv:2002.12778) [src: Eq. 4] and $f(M)$ is both the dark-matter fraction [src: Sect. I.1, fourth paragraph] and the number of emitted species in the mass-loss rate [src: Eq. 12]; in Escrivà, Kühnel & Tada $\gamma$ is the critical exponent (arXiv:2211.05767) [src: Eq. II.30] and in peak theory $\gamma_n$ is a spectral ratio [src: Eq. III.9a]; in Copeland & Kibble $\gamma=\xi/t$ (arXiv:0911.1345) [src: Sect. 4, second paragraph]. <!-- num: not a value -->
- **Area parameter:** $\mathcal{A}$ in Saikawa (arXiv:1703.02576) [src: Eq. 2.17], "$\xi$ commonly used in the literature" in Dankovsky et al. (arXiv:2509.25367) [src: abstract]; $\xi$ is also the string correlation length in Copeland & Kibble [src: Eq. 9]. <!-- num: not a value -->
- **Planck mass:** reduced, $M_{\rm Pl}\simeq 2.435\times 10^{18}$ GeV, in Saikawa (arXiv:1703.02576) [src: Sect. 2.2, text after Eq. 2.15]; $M_{\text{Pl}}=G^{-1/2}\approx 10^{19}$ GeV in Copeland & Kibble (arXiv:0911.1345) [src: Sect. 10.1, paragraph beginning "The deficit angle"].
- **Threshold variables:** a value of "$\delta_{\mathrm c}$" is meaningless without its variable (compaction peak, averaged compaction, density contrast on a given slice, or $\mu_{\mathrm c}$ of $\zeta$), its profile and its $w$; for example the monochromatic profile gives "$\delta_{\mathrm{c}}\approx 0.588$" and "$\mu_{\mathrm{c}}\!\approx\!0.628$" for the same perturbation (arXiv:2211.05767) [src: Sect. II.7.2, inline, Example B.1].
- **Printed slips, none published:** in arXiv:2211.05767 v5, Eq. III.7 is printed with the error function where the text says it is the limit of vanishing critical exponent of Eq. III.6, and the last row of Eq. III.6 keeps the Gaussian factor in the integration variable after the integral is done [src: Eqs. III.6–III.7; Sect. III.1, text after Eq. III.7]; in arXiv:2002.12778 v2, the second expression of Eq. 4 carries the horizon radius with a negative cubic power [src: Eq. 4]. Copy as printed, do not correct. <!-- num: not a value -->
- `[der]` Each of these reads as a slip in the paper's own notation.

## Referee checklist for a PBH or defect theory paper
<!-- key: referee-checklist-for-a-pbh-or-defect-theory -->

1. Which threshold variable, profile family and $q$; which $w$ at re-entry; is the averaged-compaction result used inside its validated range of $w$?
2. Nonlinear $\delta$–$\zeta$ relation included; non-Gaussianity treated non-perturbatively for broad spectra.
3. Statistical formalism (PS, peaks, compaction-function threshold statistics) and window function stated; the PS factor 2 justified or dropped.
4. Critical scaling used only near threshold; accretion and the horizon-mass factor stated.
5. Mass function extended or monochromatic; $\beta$ versus $f$ conversion and its thermal-history assumptions.
6. Evaporation: semiclassical or with memory burden; if the latter, the onset and rate-combination rule.
7. Strings: Nambu–Goto or field theory; loop-size model and $f_{\rm NG}$; intercommutation probability for superstrings; metastability parameter $\sqrt\kappa$.
8. Domain walls: area parameter and its initial-condition dependence, bias mechanism (potential or population), $C_{\rm ann}$ criterion, friction.
9. Status quoted with dataset, confidence level and date; GW spectra taken from `thcosmo-cosmological-gravitational-waves`, not rederived.
