# Approximations in dark-matter model building

Scope: the approximations that relic-abundance and linear-signature calculations rely on, their validated regime, how they fail, convention traps, and the referee checklist.

Snapshot: 2026-11-03

## Freeze-out calculations
<!-- key: freeze-out-calculations -->

### Instantaneous freeze-out and the s-wave expansion
<!-- key: instantaneous-freeze-out-and-the-s-wave -->

- What it assumes: the abundance is frozen at a single $x_{\rm fo}$ and $\sigma v$ is expanded in velocity, $\sigma v\sim v^{2L}$ (arXiv:2303.02169) [src: Sect. 4.1.1, inline].
- How it fails: Frumkin et al. give an analytic criterion for "when instantaneous freezeout is appropriate and how it can be corrected when freezeout is slow" (arXiv:2207.01635) [src: abstract]. Safdi's own estimate equates $g_{*s}$ at freeze-out and equality, although for a TeV relic they may differ by "around 10 - 30 times" (arXiv:2303.02169) [src: Sect. 4.1, text after Eq. 18]; precise values come from solving the Boltzmann equation with the full $g_{*}$ and $g_{*s}$ (arXiv:1204.3622) [src: abstract].
- Cite: Steigman, Dasgupta & Beacom (arXiv:1204.3622) for the thermal cross-section; Jungman, Kamionkowski & Griest (arXiv:hep-ph/9506380) for the standard relic-abundance calculation, which the review covers "in detail" [src: abstract].

### Exceptions to the standard calculation: coannihilation, resonances, Sommerfeld enhancement, bound states
<!-- key: exceptions-to-the-standard-calculation -->

- Coannihilation: "multiple particles that freeze-out together with nearly degenerate masses"; the abundance "is then set by the mutual evolution of the ensemble of particles" and coannihilations "play an important role in determining the abundances of higgsinos and winos" (arXiv:2303.02169) [src: Sect. 4.1.1].
- Sommerfeld enhancement: with a long-range force the cross-section is enhanced "by a factor ∼ $\alpha_{D}/v$", saturating "when the relative momentum of the DM particles falls below the mediator mass" (arXiv:2303.02169) [src: Sect. 4.1.1].
- Bound-state formation affects the relic abundance of dark matter with a long-range interaction "if the dark matter mass is above a few TeV" (arXiv:1407.7874) [src: abstract]. A 2026 semi-analytic prescription based on "the analytic limits of the relevant rates" lets standard freeze-out codes include Sommerfeld and bound-state effects (Biondini & Vogl, arXiv:2610.03718) [src: abstract].
- Hidden-sector temperature: if dark matter freezes out in a sector decoupled from the Standard Model, the standard thermal cross-section does not apply (arXiv:2007.03696) [src: abstract].

### Standard radiation-dominated history at production
<!-- key: standard-radiation-dominated-history-at -->

- What it assumes: radiation domination, with entropy conserved, from production to BBN.
- How it fails: a kination or early-matter phase, or a late-decaying field, changes the abundance by orders of magnitude; Arbey and Mahmoudi conclude that relic-density limits "cannot be used to constrain particle physics scenarios" without this caveat (arXiv:2104.11488) [src: Sect. 8.1]. The reheating temperature enters directly in ultraviolet freeze-in (arXiv:1410.6157) [src: abstract] and in freeze-in at stronger coupling (arXiv:2306.13061) [src: abstract].
- Cite: Arbey & Mahmoudi (arXiv:2104.11488, Sect. 8) for the review; the paper of the specific history used.

## Freeze-in calculations
<!-- key: freeze-in-calculations -->

### Maxwell–Boltzmann statistics, no back-reaction, constant degrees of freedom
<!-- key: maxwell-boltzmann-statistics-no-back-reaction -->

- What it assumes: Eq. 7 of Bernal et al. neglects the back-reaction term, valid "if the initial DM number density is small compared to the equilibrium number density", and uses Maxwell–Boltzmann statistics for the parent; Eq. 8 assumes the number of relativistic degrees of freedom "remains constant during DM production" (arXiv:1706.07442) [src: Sect. 3.3, text around Eqs. 7–8].
- How it fails: if the initial abundance was not negligible, the coupling of Eq. 10 is only an upper bound [src: Sect. 3.3, text after Eq. 10]; with non-renormalisable operators the yield is ultraviolet-dominated (arXiv:1410.6157) [src: abstract]; with $T_R$ below the dark-matter mass production is Boltzmann-suppressed and the coupling must be larger (arXiv:2306.13061) [src: abstract].
- Cite: Hall et al. (arXiv:0911.1120) for the mechanism; Bernal et al. (arXiv:1706.07442) for the review.

## Misalignment calculations
<!-- key: misalignment-calculations -->

### Linearised, homogeneous misalignment with a power-law axion mass
<!-- key: linearised-homogeneous-misalignment-with-a -->

- What it assumes: $|\theta_{i}|\ll\pi$ so that the potential can be linearised, no gradients (pre-inflationary breaking), and the power law of Eq. 61, "reasonable so long as one is not interested in the precise form of $m_{a}(T)$ right around $T\sim\Lambda$" (arXiv:2303.02169) [src: Sect. 6.4, Sect. 6.4.1].
- How it fails: for $\theta_{i}\sim\pi$ "the dynamics ... are non-trivial" (arXiv:2303.02169) [src: Sect. 6.4.1, text after Eq. 62]; for $f_{a}\gtrsim 10^{16}$ GeV oscillation starts below Λ, outside the validity of Eq. 61 [src: Sect. 6.4.1, text after Eq. 71]; Eq. 72 equates the $g_{*s}$ factors, "not a great approximation" [src: Sect. 6.4.1, text after Eq. 72]; with post-inflationary breaking the gradients, non-linearities and strings dominate (arXiv:2303.02169) [src: Sect. 6.4.2], see `open-questions.md`.
- Cite: Marsh (arXiv:1510.07633) for the review; the lattice calculation of the topological susceptibility the paper uses.

## Linear-signature fits
<!-- key: linear-signature-fits -->

### The warm-dark-matter transfer-function fit
<!-- key: the-warm-dark-matter-transfer-function-fit -->

- What it assumes: thermal relics, or non-resonant sterile neutrinos with a rescaled thermal distribution; ν = 1.12 fitted for k < 5 h Mpc⁻¹ (arXiv:astro-ph/0501562) [src: Sect. II, text after Eq. 6].
- How it fails: non-thermal momentum distributions are "not captured by the common $αβγ$-parametrization" (arXiv:2606.20815) [src: abstract]; Shi–Fuller spectra need a refitted mapping (arXiv:2507.18752) [src: abstract].
- Cite: Viel et al. (arXiv:astro-ph/0501562); the paper that gives the mapping for the momentum distribution used.

### The fuzzy-dark-matter transfer-function fit
<!-- key: the-fuzzy-dark-matter-transfer-function-fit -->

- What it assumes: a single free scalar that is all the dark matter; the fit was found "numerically" (arXiv:astro-ph/0003365) [src: text before Eq. 8].
- How it fails: mixed, self-interacting or multi-field models (arXiv:2507.00705) [src: abstract]; precise work uses axionCAMB, axionECAMB or AxiCLASS (arXiv:2507.00705) [src: Sect. V.2].
- Trap: the 2025 review prints the fit with $T^{2}$ and $m_{22}^{-1/18}$ (arXiv:2507.00705, Eq. 78); the original is $T_{\rm F}$ with $m_{22}^{1/18}$ (arXiv:astro-ph/0003365, Eq. 8). See `formalism.md`.

### Interacting dark matter as a fluid
<!-- key: interacting-dark-matter-as-a-fluid -->

- What it assumes: Maxwellian velocity distributions for dark matter and baryons and a drag term proportional to the velocity difference (arXiv:1801.08609) [src: Sect. III.1].
- How it fails: for operators with strong velocity dependence the temperature and velocity evolution matter (arXiv:1801.08609) [src: abstract].

## Convention traps
<!-- key: convention-traps -->

- Self-conjugate versus non-self-conjugate dark matter: the unitarity bound differs, 140 TeV against below 100 TeV (arXiv:1904.11503) [src: abstract], and so does the thermal cross-section quoted by different papers.
- $m_{\rm pl}$ in Safdi's lectures is the reduced Planck mass (arXiv:2303.02169) [src: Sect. 3.1]; Bernal et al. write $M_{\rm P}$ in Eqs. 9 and 13 (arXiv:1706.07442). `[der]` Check which Planck mass enters a numerical coefficient before combining formulas from different papers.
- Safdi writes the scale factor R and the axion field a; Hu et al. write the scale factor a (arXiv:2303.02169, Eq. 60; arXiv:astro-ph/0003365, Eq. 2). <!-- num: not a value -->
- Thermal-relic and sterile-neutrino warm masses are different numbers for the same suppression (arXiv:astro-ph/0501562) [src: Eq. 5]; a "keV bound" must say which mass.
- Free-streaming scale: "there exist different definitions" (arXiv:astro-ph/0501562) [src: Sect. II, text after Eq. 3].
- Thermal-relic Lyman-α bounds depend on the scales and thermal-history priors used: 5.7 keV against 4.1 keV in the same data (arXiv:2309.04533) [src: abstract].

## What a referee checks in a dark-matter model paper
<!-- key: what-a-referee-checks-in-a-dark-matter-model -->

- The production mechanism is solved with the Boltzmann equation, with $g_{*}(T)$ and $g_{*s}(T)$, not with the parametric estimate (arXiv:1204.3622; arXiv:2303.02169, Sect. 4.1).
- Coannihilation, resonances, thresholds, Sommerfeld and bound-state effects are included where the spectrum allows them (arXiv:2303.02169, Sect. 4.1.1; arXiv:1407.7874).
- The expansion history and the reheating temperature are stated; ultraviolet sensitivity is discussed for freeze-in and gravitational production (arXiv:2104.11488, Sect. 8; arXiv:2602.10215).
- The gravitational-production background is estimated for non-thermal models (arXiv:2306.13061).
- For light or non-thermal candidates, the momentum distribution is propagated to a transfer function, not mapped by mass alone (arXiv:2507.18752; arXiv:2606.20815).
- For axions: pre- or post-inflationary breaking stated, isocurvature for the former, the string contribution and domain-wall number for the latter (arXiv:2303.02169, Sect. 6.4).
- Status claims name the dataset, the confidence level and the date; limits are taken from cosmoskill.

