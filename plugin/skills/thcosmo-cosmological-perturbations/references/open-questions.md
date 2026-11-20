# Open questions on cosmological perturbations

Scope: live debates, unresolved calculations, and stale claims in relativistic perturbation theory.

Snapshot: 2026-11-20

## Large-scale white noise at second order
<!-- key: large-scale-white-noise-at-second-order -->

- **Claim.** Barenboim, Ireland & Stebbins (arXiv:2511.13866) argue that non-linearities make unresolved small-scale dynamics act as a white-noise contribution to large-scale dynamics, which dominates the largest-scale power "in cases where the power spectrum is sub-Poissonian on large scales", "no matter the amplitude of the inhomogeneities"; for a near Harrison–Zel'dovich spectrum, "the non-observation of white noise on the Hubble scale precludes the extrapolation of this power law below the comoving 1 pc scale" [src: abstract, inline]. A companion paper adds a white-noise term $k_\mathrm{BH}/k$ to the primordial spectrum in CLASS and finds $k_\mathrm{BH} \leq 1.80 \times 10^{-13}~\mathrm{Mpc}^{-1}$ at 99 % confidence, implying a cutoff at $k_{\mathrm{cut}} \lesssim 3~\mathrm{pc}^{-1}$ or a running $α_s \lesssim -0.015$ (arXiv:2511.15803) [src: abstract, inline].
- **Reply.** Ireland (arXiv:2608.09897), a co-author of both papers, agrees that the "kurvature density variable Δρ does indeed develop LSWN at second order", but finds that it is not inherited as an infrared pole of the second-order comoving curvature perturbation $R_2$: the enhancement "was an artifact of using a linear Poisson equation to relate two genuinely second order quantities", and the constraint of arXiv:2511.15803 "and its implications for the small-scale primordial power spectrum are therefore invalid" [src: abstract].
- **State.** No further reply to arXiv:2608.09897 was found in this run.
- `[der]` The disagreement is over which second-order variable carries the white noise into observables; it is a gauge and variable question of the kind listed in `approximations.md`.

## Where the separate universe stops
<!-- key: where-the-separate-universe-stops -->

- Ultra-slow-roll transitions: the breakdown at the first transition is "well known"; Raveendran (arXiv:2506.23571) adds a breakdown for Π at the second transition, reads the curvature term of the extended δN formalism it cites as Artigas:2024ajh as a contribution of Π, and restricts "this modification of the local Hubble parameter" to a small and "strictly constant" first slow-roll parameter [src: abstract]. Ahmadi & Ahmadi (arXiv:2602.00902) propose gradient-corrected δN [src: abstract].
- `[der]` No paper read here compares the two prescriptions.
- Non-minimal coupling: the lower bounds derived in the Jordan frame are compared with those of "the classically equivalent Einstein frame description", for a Higgs-like toy model in the large-field limit (arXiv:2609.34788) [src: abstract]; the abstract does not say whether the bounds agree.
- Anisotropic backgrounds: for linear superhorizon perturbations of Bianchi I with a scalar coupled to a U(1) gauge field, the separate universe extends with an extra intrinsic-curvature contribution and a "nonlinear extension of the formalism" is discussed (arXiv:2607.11814) [src: abstract].
- `[der]` What would decide: explicit comparisons of δN with linear and second-order perturbation theory through the transitions.
- The loop-level question of whether ζ stays conserved through them belongs to `thcosmo-primordial-correlators` (Inomata, arXiv:2606.28247, for the decoupling limit) [src: abstract].

## Gauge of second-order observables
<!-- key: gauge-of-second-order-observables -->

- Second-order tensors: with the TT gauge at first order the second-order tensor "would be gauge invariant", the TT gauge existing under a vacuum condition (arXiv:2509.26159) [src: abstract]; the scalar-induced-wave debate, its resolution for radiation domination and the missing second-order description of the detector are in `thcosmo-cosmological-gravitational-waves`.
- Observers at second order: the light-cone formalism removes divergences at the observer position "in a completely model independent way" for the luminosity distance (arXiv:2510.25690) [src: abstract].
- `[der]` Whether this agrees with standard-gauge second-order distance calculations is not tested in the abstract read.
- Localized sources: Compère & Hoque (arXiv:2610.26623) obtain gauge-invariant multipoles without the non-local SVT projection [src: abstract]; their relation to the standard variables is given in that paper [src: abstract].

## Unresolved or not computed here
<!-- key: unresolved-or-not-computed-here -->

- Isocurvature from a thermal inflaton: Laine & Procacci show that isocurvature vanishes outside the horizon for their system, while stating that they do not succeed in offering "an intuitively clear physical phenomenon" behind it (arXiv:2607.06983) [src: Sect. 8.3, first paragraph].
- Dark-sector isocurvature transferred to the inflaton sector without direct interactions, if the dark sector "is radiation-like and constitutes a significant fraction of the energy density", and its use to discriminate freeze-in from freeze-out by future isocurvature measurements (arXiv:2510.21917) [src: abstract] (**forecast** in the sense of "can potentially discriminate").
- Ultralight-axion isocurvature: "Given the tensor bound, any primary CMB detection in these two lightest regimes would indicate a non-inflationary origin of the isocurvature modes or a breakdown of the standard frozen-field misalignment scenario" (arXiv:2608.07803) [src: abstract].

## Misconceptions and stale claims
<!-- key: misconceptions-and-stale-claims -->

- "The longitudinal gauge is the physical gauge": Malik & Wands write that "it may therefore appear that this gauge is somehow preferred", but "any unambiguous choice of time-slicing and threading can be used to define explicitly gauge-invariant perturbations" (arXiv:0809.4944) [src: Sect. 7.1.1].
- "ζ is always conserved outside the horizon": only for negligible non-adiabatic pressure and shear (arXiv:0809.4944, Eq. 8.35) or P(ρ) (arXiv:astro-ph/0411220) [src: abstract]; at "transitions to an ultra-slow-roll phase", "gradient interactions induce a significant non-conservation of the comoving curvature perturbation" (arXiv:2602.00902) [src: abstract].
- "δN equals the curvature perturbation in any sign convention": ζ = δN holds for Malik & Wands' sign of ζ (arXiv:0809.4944, Eq. 11.1); Lyth, Malik & Sasaki equate the e-fold difference from flat to uniform-density slicing with ψ on the final slice (arXiv:astro-ph/0411220, Sect. IV, Eq. 35), and denote ψ on uniform-density slices by −ζ (arXiv:astro-ph/0411220, Sect. III.1).
- `[der]` In their sign convention the e-fold difference is therefore minus their ζ.
- "Isocurvature modes are only CDM and baryon modes": two neutrino modes, density and velocity, complete the regular set (arXiv:astro-ph/9904231) [src: abstract].
- "Synchronous-gauge growth outside the horizon is growth": the super-horizon δ are "strongly gauge-dependent" (arXiv:astro-ph/9506072) [src: Sect. 8].

