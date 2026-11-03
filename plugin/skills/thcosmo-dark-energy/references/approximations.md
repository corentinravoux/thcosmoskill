# Approximations, traps and the referee checklist for dark energy

Scope: approximations the dark-energy literature relies on, their validity, convention traps, numerical issues, and the checks a referee makes.

Snapshot: 2026-11-03

## The fluid treatment of an interacting dark sector
<!-- key: the-fluid-treatment-of-an-interacting-dark -->

- What it assumes: a dark-energy fluid with constant w and a rest-frame sound speed set by hand; Wang et al. take $C_e^2=1$, correct for scalar fields but "not obvious" for a fluid (arXiv:1603.08299) [src: Sect. 4.2].
- How it fails: constant w with "a simple interaction with dark matter" (proportional to ρ_c in the model of Sect. III, Eq. 38) gives "an instability in the dark sector perturbations at early times: the curvature perturbation blows up on super-Hubble scales", "regardless of how weak the coupling is" (arXiv:0804.0232) [src: abstract]; background fits alone are therefore "not sufficient" (arXiv:2606.21826) [src: Sect. III.1].
- Remedies: Q ∝ Hρ_de, "provided the coupling is made small enough for a given equation of state parameter" (arXiv:0901.3272) [src: abstract]; the ePPF framework of IDECAMB (arXiv:2606.21826) [src: Sect. III.1].
- Cite: Valiviita, Majerotto & Maartens (arXiv:0804.0232) for the instability; the ePPF papers through arXiv:2606.21826.
- Trap: the sign of Q and of β is convention-dependent (Li et al. arXiv:2606.21826, Eqs. 3–4, against Wang et al. arXiv:1603.08299, Eqs. 12–13).

## Smooth dark energy and the fluid closure
<!-- key: smooth-dark-energy-and-the-fluid-closure -->

- What it assumes: dark energy as a fluid with w(a) and a rest-frame sound speed; Wang et al. note that $C_{e}^{2}=1$ "is correct for scalar fields, but it is not obvious for other cases, especially for a fluid with a constant equation of state" (arXiv:1603.08299) [src: Sect. 4.2, inline, paragraph after the perturbation equations].
- How it fails: through w = −1 the adiabatic sound speed diverges and the perturbation system "becomes ill-defined around the crossing point" (arXiv:2606.01360) [src: text after Eq. 10]; models that cross "require additional degrees of freedom to ensure gravitational stability" (arXiv:0808.3125) [src: abstract].
- Regime of validity of the remedy: the PPF closure is exact in the metric evolution well above and below the transition scale to smoothness and "a well controlled approximation for a wide range of smooth dark energy models" (arXiv:0808.3125) [src: abstract].
- Cite: Fang, Hu & Lewis (arXiv:0808.3125) whenever a crossing w(a) is run through a Boltzmann code.

## Slow roll applied to dark energy
<!-- key: slow-roll-applied-to-dark-energy -->

- The inflationary slow-roll conditions "are not completely trustworthy" for dark energy because dark matter is present; $\epsilon=-\dot{H}/H^{2}$ is the measure that includes both (arXiv:hep-th/0603057) [src: Sect. V.1, text after Eq. 104].
- The thawing slow-roll limit of Scherrer & Sen gives a w(a) that, "for a variety of potentials", is "typically accurate to within delta w < 0.005 for w<-0.9" (arXiv:0712.3450) [src: abstract]; the Caldwell–Linder thawing and freezing bounds are valid for (1+w) ≪ 1, with w ≲ −0.8 "a practical limit of applicability" (arXiv:astro-ph/0505494) [src: text after Fig. 1].

## Parameterisations of w(a)
<!-- key: parameterisations-of-w-a -->

- What they assume: a two-parameter form of w(a), such as $w(a)=w_{0}+w_{a}(1-a)$ (Ren et al., arXiv:2606.01360) [src: Eq. 1]. For thawing quintessence with nearly flat potentials, "for redshift z < 1", w(a) "is well-fit by the Chevallier-Polarski-Linder parametrization" (arXiv:0712.3450) [src: abstract].
- How they fail: a crossing of w = −1 read from a fit is not a model property; physically self-consistent models (thawing quintessence with curvature) fit the same data without it (arXiv:2504.15190) [src: abstract]. The contour shapes and degeneracy directions change between CPL, JBP, BA, EXP, LOG and SIN, while "the preference for DDE does not disappear when the CPL assumption is relaxed" (arXiv:2606.21826) [src: Sect. II.2].
- Prior dependence: evidence for thawing quintessence depends on whether priors are informed by the data (arXiv:2411.13637, v4) [src: abstract]; Toomey et al. map CPL chains back to the KMIX parameters through "a theory-informed prior" on $(w_0,w_a)$ learnt from KMIX realisations (arXiv:2511.23463) [src: abstract].

## Convention traps
<!-- key: convention-traps -->

- Planck mass: Copeland et al. use the full Planck mass $m_{\rm pl}=1.22\times 10^{19}$ GeV (arXiv:hep-th/0603057) [src: Sect. IV.2, inline, text after Eq. 69]; the hub's atlas lists reduced-mass works.
- Kinetic term X: X ≡ −(1/2)(∇φ)² in Copeland et al. (arXiv:hep-th/0603057) [src: Sect. V.2, text before Eq. 115]; other definitions differ in sign and by a factor of two (hub atlas, "Kinetic term X"). A sound speed $p_{,X}/\rho_{,X}$ is quoted with its X.
- Sign of the interaction: Q > 0 feeds dark energy in arXiv:2606.21826 (Eqs. 3–4) and dark matter in arXiv:1603.08299 (Eqs. 12–13).
- Phantom divide versus null-energy-condition boundary: with a negative dark-energy density w = −1 is not the meaningful separator (arXiv:2602.21169) [src: abstract].
- Quintom-A and Quintom-B name the direction of crossing (arXiv:2606.01360) [src: text before Eq. 1]; the DESI-preferred shape is Quintom-B (arXiv:2606.21826) [src: Sect. II.2].
- Printed slips to copy, not correct: the quintessence Lagrangian density with $+V$ (arXiv:hep-th/0603057, Eq. 179); "$10^{121}$ orders of magnitude" (arXiv:hep-th/0603057, Sect. IV.2); the adiabatic sound speed printed as $\rho'/P'$ (arXiv:2302.09032, Eq. 24).
- Early dark energy parameters: $f_{\rm EDE}$ and $z_c$ are phenomenological stand-ins for m and f; sampling one set or the other changes the effective priors (arXiv:2302.09032) [src: Sect. III.1].

## Numerical issues
<!-- key: numerical-issues -->

- Fluid closures through w = −1: use PPF (arXiv:0808.3125) [src: abstract]; for interacting fluids the ePPF of IDECAMB (arXiv:2606.21826) [src: Sect. III.1].
- Early dark energy perturbations: the effective sound speed depends on k and a for oscillating fields (arXiv:2302.09032) [src: Sect. IV.1]; the general behaviour of axion-like EDE "is well-described by cycle-averaging the evolution of the background and perturbative field dynamics" [src: Sect. III.1].

## Referee checklist
<!-- key: referee-checklist -->

- Conventions stated: Planck mass, the definition of X, the sign of Q, the meaning of β.
- A claimed phantom phase: is it a property of a model or of the parameterisation? Is the field a ghost, and if so what is the cutoff (arXiv:hep-ph/0311312)?
- A claimed crossing of w = −1 in a single-field, minimally coupled model: does it evade the no-go (arXiv:astro-ph/0407107; arXiv:2606.01360)?
- Interacting dark energy: perturbations treated consistently, large-scale stability shown (arXiv:0804.0232), not only the background fitted (arXiv:2606.21826, Sect. III.1); sign-switching solutions checked for negative densities (arXiv:2601.03122).
- Dark-energy perturbations: sound speed stated; PPF or equivalent for crossings (arXiv:0808.3125).
- Model evidence: prior dependence shown (arXiv:2411.13637); dependence on the SN Ia compilation shown (arXiv:2512.10585; arXiv:2606.21826).
- Early dark energy: priors on $f_{\rm EDE}$, $z_c$ against m, f; radiative stability of the potential (arXiv:2302.09032, Sect. VII.2); status questions sent to `thcosmo-tensions-model-building`.
- Λ problem: a paper quoting "122 orders of magnitude" (arXiv:1205.3365) [src: abstract] or "120 orders of magnitude" (arXiv:2606.20778) [src: abstract] says which estimate it uses.

## Not verified
<!-- key: not-verified -->

- A paper validating the quasi-static approximation for interacting dark energy: none read; for modified gravity see `thcosmo-modified-gravity`.
