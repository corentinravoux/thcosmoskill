# Open questions in large-scale-structure perturbation theory

Scope: live debates with both sides, unresolved calculations, what the next data or calculation will decide, and stale claims with the paper that corrects them.

Snapshot: 2026-10-31

## Live debates
<!-- key: live-debates -->

### Do higher loops buy cosmological information?
<!-- key: do-higher-loops-buy-cosmological-information -->

- For: the two-loop redshift-space galaxy power spectrum raises $k_{\rm max}$ from $0.20h\,\mathrm{Mpc}^{-1}$ to $0.34h\,\mathrm{Mpc}^{-1}$ for an LRG-like sample at $z=0.5$, and from $0.27h\,\mathrm{Mpc}^{-1}$ to $0.42h\,\mathrm{Mpc}^{-1}$ for an ELG-like sample at $z=1.1$ (Philcox 2026, arXiv:2610.13867) [src: abstract]; a two-loop matter spectrum is ready for lensing analyses with eight counterterms (Anastasiou et al. 2025, arXiv:2509.05187) [src: abstract].
- Against: the same paper finds that the 49 coefficients, including fifth-order biases, absorb much of the additional information, so that $\sigma_8$ constraints are not significantly enhanced (arXiv:2610.13867) [src: abstract]. The implications for parameter inference are left to future work [src: abstract].
- For, with galaxy–galaxy and galaxy–matter spectra: Ivanov's two-loop galaxy power spectrum needs 21 additional parameters per sample relative to one loop, agrees with the galaxy–galaxy and galaxy–matter spectra of the PT Challenge simulation at the per-mille level up to k = 0.85 h/Mpc at $z=0.61$, and, even with conservative priors, measures $σ_8$ without bias, with an improvement of about 40% over the one-loop model and error bars three times narrower than linear theory (Ivanov 2026, arXiv:2606.30713) [src: abstract].
- The two results differ in setting (galaxy–galaxy and galaxy–matter spectra, with no redshift space named in the abstract, against redshift-space multipoles) and in the number of free coefficients. `[der]` Whether the redshift-space counterterms and fingers of god account for the different gains is not settled by the abstracts.
- What decides it: parameter inference with both models on the same simulations, and priors on higher-order biases from simulations.

### Priors and projection effects in EFT full-shape fits
<!-- key: priors-and-projection-effects-in-eft-full-shape -->

- Claim: with baseline priors, DESI DR1 power-spectrum fits show multi-σ projection in $H_{0}$, $w_{0}$ and $w_{a}$, because weakly constrained EFT nuisance parameters shift the marginalised posteriors away from the maximum (Bonici et al. 2026, arXiv:2607.02498) [src: abstract].
- Responses differ: a reparameterisation that absorbs the amplitude-setting cosmological parameters into the nuisance parameters (Tsedrik, Carrilho & Moretti 2025, arXiv:2509.09562) [src: abstract]; a reparameterisation-invariant Jeffreys prior over all EFT coefficients, combined with Gaussian priors in a hybrid configuration (arXiv:2607.02498) [src: abstract]; simulation-based priors on bias parameters, which tighten non-local PNG constraints in the DESI reanalysis (Chudaykin, Ivanov & Philcox 2025, arXiv:2512.04266) [src: abstract]. Which choice the community adopts is open; the theory question is which priors are physical (naturalness, halo-occupation predictions).

### Is the EdS approximation good enough?
<!-- key: is-the-eds-approximation-good-enough -->

- Snowmass white paper: $\mathcal{O}(0.1\div 1)\%$ accurate for current and future surveys (Cabass et al. 2022, arXiv:2203.08232) [src: Sect. 3.6, footnote 5].
- Donath and Senatore: for the one-loop redshift-space galaxy spectrum the ratio of the spectrum with exact time dependence to the EdS approximation is about 1.003 for the monopole and 1.007 for the quadrupole at $z=0.57$, grows at lower redshift and is only partly absorbed by the biases; they argue it is comparable to the precision of next-generation surveys (arXiv:2005.04805) [src: abstract].
- Beyond ΛCDM the approximation fails at more than the percent level for interacting dark sectors (Wolney et al. 2026, arXiv:2603.12431) [src: abstract]. What decides it: parameter shifts in full analyses with exact time dependence.
- With massive neutrinos, the EdS-kernel EFT has been argued to suffice for Stage-III surveys; a Newtonian-motion-gauge calculation finds deviations below 0.7% in the real-space one-loop spectrum for $M_\nu<0.30$ eV but 1.7% in the redshift-space quadrupole at k = 0.3 h/Mpc and z = 0 (Fidler et al. 2026, arXiv:2605.05114) [src: abstract].

### Universality of $b_{\phi}$ and local PNG from scale-dependent bias
<!-- key: universality-of-b-phi-and-local-png-from-scale -->

- The universality relation is the default in $f_{\rm NL}$ analyses; it breaks down for realistic galaxy populations through PNG assembly bias, and $b_{\phi}$ is completely degenerate with $f_{\rm NL}$ in the power spectrum (de S. Nascimento & Dalal 2026, arXiv:2607.18229) [src: abstract].
- Mitigations: free p with priors Δp ≈ 0.5 suffice in an idealised forecast (Barreira 2020, arXiv:2009.06622) [src: abstract] (forecast); the time-evolution estimator of $b_{\phi}$ from number counts, extended to photometric selections (arXiv:2607.18229) [src: abstract]; multi-tracer scale-dependent bias, which the field-level Cramér–Rao bound shows can exceed conservative higher-point analyses (Chen, Green & Lee 2026, arXiv:2603.22415) [src: abstract] (forecast).

### Testing the equivalence principle with consistency relations
<!-- key: testing-the-equivalence-principle-with -->

- The consistency relations fail if the equivalence principle is violated; galaxy surveys can probe violations of order $10^{-3}$ to $10^{-4}$ with the squeezed bispectrum of two populations (Creminelli et al. 2013, arXiv:1312.6074) [src: abstract] (forecast).
- Quadratic estimators of the anti-symmetric modulation of the cross-power of two tracers are competitive with the direct bispectrum for a DESI-like survey up to k_max ≈ 0.15 h/Mpc (Dam & Darwish 2025, arXiv:2510.13803) [src: abstract] (forecast).
- DHOST and GLPV theories violate the relations through a relative velocity, which leaves an IR-dominant one-loop term and a BAO signature proportional to $A_{\alpha}$ (Cabass et al. 2022, arXiv:2203.08232) [src: Sect. 4.5]. What decides it: a measured squeezed bispectrum of two tracers with controlled systematics.

## Unresolved calculations
<!-- key: unresolved-calculations -->

- **Redshift-space bispectrum beyond tree level for galaxies.** The 2022 state of the art stopped at the tree-level bispectrum for biased tracers in redshift space (Cabass et al., arXiv:2203.08232) [src: Table 1]; the two-loop power-spectrum model of 2026 encodes all deterministic and counterterm contributions of the one-loop bispectrum and trispectrum (Philcox, arXiv:2610.13867) [src: abstract]; a tree-level EFT model of the redshift-space galaxy trispectrum, validated on 25 AbacusSummit simulations, can improve constraints on $ω_{\rm cdm}$ by up to $15\%$ in a DESI-like volume (Tucci & Philcox 2026, arXiv:2610.08908) [src: abstract] (forecast).
- **Field-level EFT likelihoods for data.** The EFT at the field level is established for comparisons with simulations; inference from the full field without summary statistics is in progress (arXiv:2203.08232) [src: Sect. 3.9]. Recent field-level models cover the Lyα forest (arXiv:2606.26234) [src: abstract] and intrinsic alignments (arXiv:2610.36027) [src: abstract].
- **Velocity and momentum statistics at higher order.** The matter–momentum bispectrum at one loop needs transverse counterterms, one generated by vorticity (Raikman et al. 2026, arXiv:2609.15750) [src: abstract]; the paper computes the pure dark-matter version of the galaxy–galaxy–electron-momentum bispectrum that kSZ measures [src: abstract].
- **Large deviations after shell crossing.** The LDP derivation assumes no shell crossing (Bernardeau 2015, arXiv:1511.08641) [src: abstract]; how the PDF behaves for cells where shells cross was not addressed in the sources read.

## Stale claims and misconceptions
<!-- key: stale-claims-and-misconceptions -->

| Statement still met | Correction | Source |
|---|---|---|
| "$F_{2}$ has a dipole term $\hat{q}_{1}\cdot\hat{q}_{2}(q_{1}/q_{2}+q_{2}/q_{1})$ with coefficient one" (copied from Ivanov 2022, Eq. 28) | the coefficient is one half | Bernardeau et al., arXiv:astro-ph/0112551 [src: Eq. 45]; hub `stale-claims.md` |
| "SPT loops converge to the non-linear spectrum" | loop integrals are UV sensitive; the UV part of $P_{13}$ renormalises the sound speed | Ivanov, arXiv:2212.08488 [src: Eqs. 72–73] |
| "Eulerian and Lagrangian EFTs give different predictions" | they agree within overlapping domains to the order computed | Cabass et al., arXiv:2203.08232 [src: Sect. 3.5] |
| "Local bias in density is enough at one loop" | renormalisation requires the tidal operator at second order and the velocity potential at third | Assassi et al., arXiv:1402.5916 [src: abstract] |
| "Redshift-space biased tracers are known only to one loop in the power spectrum and tree level in the bispectrum" (Snowmass 2022 table) | two-loop redshift-space galaxy power spectrum computed in 2026 | Philcox, arXiv:2610.13867 [src: abstract] |
| "Phenomenological FoG models are adequate for BAO and RSD" | they bias distances by 1–2% and the growth rate by about 5% (forecast) | Taruya et al., arXiv:1006.0699 [src: abstract] |
| "NLA/TATT describe halo alignments in the quasi-linear regime" | valid only to 0.05 h/Mpc, against 0.30 h/Mpc for the one-loop EFT of IA, at $z=0$ | Bakx et al., arXiv:2303.15565 [src: abstract] |
| "b_φ = 2δ_c(b_1 − 1) holds for any tracer" | broken by PNG assembly bias for realistic galaxies | de S. Nascimento & Dalal, arXiv:2607.18229 [src: abstract] |

## Not verified
<!-- key: not-verified -->

- Whether the two-loop galaxy models of arXiv:2606.30713 and arXiv:2610.13867 agree term by term: only the abstracts were read.
- The status of RPT, RegPT and other resummations named by Peloso and Pietroni.
