# Open questions in modified gravity

Scope: live debates with both sides cited, unresolved calculations, what next data or calculations will decide, forecasts (labelled), and stale claims.

Snapshot: 2026-11-02

## Live debates
<!-- key: live-debates -->

### Can shift-symmetric Horndeski gravity cross the phantom divide?
<!-- key: can-shift-symmetric-horndeski-gravity-cross-the -->
- Tsujikawa: in shift-symmetric Horndeski and generalised Proca theories with luminal gravitational waves and no direct coupling to dark matter, a crossing from $w_{\rm DE}<-1$ to $w_{\rm DE}>-1$ is "generically difficult without theoretical pathologies"; breaking the shift symmetry allows it, and he builds a model with a potential, a Galileon term and a quadratic kinetic term that crosses without ghosts or Laplacian instabilities (arXiv:2508.17231) [src: abstract].
- Calderon & Linder: overturning "conventional thought", shift-symmetric Horndeski can cross, with two mechanisms identified in a dynamical-systems analysis of the ghost-free and stable regions (arXiv:2610.36063) [src: abstract].
- `[der]` The two papers differ in assumptions (Tsujikawa states luminal tensors and no coupling to dark matter); a reader comparing them checks the subclass each one treats.
- Why it matters: DESI BAO with CMB and SN Ia data prefer a crossing at low redshift, and Ye et al. read it as a hint of non-minimal coupling (arXiv:2407.15832; arXiv:2605.12415) [src: abstracts]. The measured $w_0w_a$ belong to cosmoskill `cosmo-dark-energy-modified-gravity`; quintessence and phantom fields to `thcosmo-dark-energy`.

### Is there evidence for a single scalar field beyond quintessence?
<!-- key: is-there-evidence-for-a-single-scalar-field -->
- García-García, Ferreira & Wolf: cosmological observations can at most constrain a small number of EFT parameters; quintessence is "only marginally distinguishable" from Λ; more general EFT extensions show "modest statistical preference", sensitive to data selection and priors, and predict fifth forces whose screening remains "theoretically non-trivial" (arXiv:2607.07777) [src: abstract].
- Ye et al. read the same class of data as a hint of non-minimal coupling at 2.8σ (arXiv:2605.12415) [src: abstract]; Zheng et al. find that the significance of dynamical dark energy is "greatly reduced" within the EFT of DE (arXiv:2509.13804) [src: abstract].

### Are f(Q) and f(T) cosmologies healthy?
<!-- key: are-f-q-and-f-t-cosmologies-healthy -->
- Against: f(Q) cosmologies are infinitely strongly coupled on two branches and carry a ghost on the third (arXiv:2311.04201) [src: abstract]; quadratic non-metricity theories generically show ghosts or strong coupling on FLRW (arXiv:2511.19101) [src: abstract]; in f(T) the broken local symmetry gives strong coupling and contradictory Hamiltonian counts (arXiv:2405.14184) [src: abstract].
- For: the f(Q) review presents f(Q) as able to address cosmological tensions and to describe early and late cosmology without dark components (arXiv:2309.15958) [src: abstract], and phenomenological fits to DESI DR2 continue (arXiv:2608.24676; arXiv:2610.20002) [src: abstracts].
- `[der]` No paper read in this run answers the ghost argument of arXiv:2311.04201 directly; a referee asks an f(Q) paper which connection branch it uses and how it treats that result.

### Must gravitational waves be subluminal or superluminal on cosmological backgrounds?
<!-- key: must-gravitational-waves-be-subluminal-or -->
- Melville & Noller use subluminal gravitational waves as an extra theoretical prior with positivity bounds, which leaves 1% of the parameter space of their example class (arXiv:1904.05874) [src: abstract].
- De Rham, Melville & Noller find, once matter couplings are included, that a standard UV completion of their EFT of dark energy model requires superluminal gravitational waves on cosmological backgrounds (arXiv:2103.06855) [src: abstract].
- `[der]` The two priors pull in opposite directions; GW170817 constrains the speed at LIGO frequencies, which may lie near the cutoff (arXiv:1806.09417) [src: abstract].

## Unresolved calculations
<!-- key: unresolved-calculations -->

- **Vainshtein screening beyond spherical symmetry.** Most arguments that DHOST theories and the EFT of dark energy screen the fifth force assume spherical symmetry; Kobayashi & Takadera find the multipoles unscreened for generic beyond-Horndeski parameters, and, when the parameters are tuned to remove graviton decay, a mechanism "not efficient enough" to screen the fifth force in the region they study (arXiv:2607.09098) [src: abstract]. `[der]` Whether this makes the luminal, decay-free DHOST subclass incompatible with local tests is not settled by the abstract.
- **Several screening mechanisms at once.** Realistic models can activate chameleon and Vainshtein screening together, an interplay Sirera et al. call overlooked until their study (arXiv:2610.36166) [src: abstract].

## What next data will decide
<!-- key: what-next-data-will-decide -->

- **Euclid, forecast.** For $\mu$–$\Sigma$ (Eqs. 32–33 of arXiv:2512.09748) around ΛCDM, the full 3×2pt + spectroscopic clustering combination gives relative uncertainties on $\bar{\mu}_{0}$ and $\bar{\Sigma}_{0}$ of "24% (23%) and 3% (3%), in the SS (US) case" with conservative scale cuts, and "of the order of 1%" with more optimistic cuts, which require accurate non-linear modelling (arXiv:2512.09748) [src: Sect. 4.2.1] (forecast). The review states that this improves current constraints "by one order of magnitude" [src: Sect. 4.2.1] (forecast).
- **The non-linear prescription decides the forecast.** The forecasts depend on whether screening is ignored (US, unscreened) or assumed complete at non-linear scales (SS, super-screened) (arXiv:2512.09748) [src: Sect. 4.1.1, Sect. 4.2.1]; see `approximations.md`, screening in simulations.
- **Non-minimal coupling.** The 2.8σ hint of arXiv:2605.12415 [src: abstract] and the 2.9σ deviation of the EFT of DE model of arXiv:2606.31977 [src: abstract] will be tested by later DESI, Euclid and LSST growth data.
- `[der]` The deciding quantity is the growth and lensing response, not the background $w(z)$, since background fits cannot separate the classes (arXiv:2609.26517) [src: abstract].
- **Gravitational-wave propagation.** Tests of $c_g$, extra friction ν, graviton mass and dispersion (arXiv:1807.09241, Eq. 55 and abstract) by future detectors belong, for their signal modelling, to `thcosmo-cosmological-gravitational-waves`.

## Stale claims and misconceptions
<!-- key: stale-claims-and-misconceptions -->

- **"f(R) and chameleons explain cosmic acceleration as a modified-gravity effect."** Stale: chameleon-like scalars cannot self-accelerate and act as a form of dark energy (arXiv:1208.4612) [src: abstract].
- **"The self-accelerating DGP branch is a benchmark of infrared modified gravity."** Stale: it carries a ghost (arXiv:hep-th/0604086) [src: abstract], and the cubic Galileon, its 4D limit, is in 7.8σ tension with ISW data (arXiv:1707.02263) [src: abstract].
- **"Quartic and quintic Horndeski or GLPV are viable dark-energy models."** Stale after GW170817 and graviton decay (arXiv:1901.07183, Sect. 4.2; arXiv:1809.03484) [src: Sect. 4.2; abstract], unless the cutoff argument of arXiv:1806.09417 [src: abstract] is invoked explicitly.
- **"The quasi-static approximation holds inside the Hubble horizon."** It holds, at best, inside the sound horizon of dark energy (arXiv:1503.06831) [src: abstract].
- **"Vainshtein screening hides the fifth force around any source in DHOST and the EFT of DE."** Shown for spherical symmetry; multipoles are unscreened for generic beyond-Horndeski parameters (arXiv:2607.09098) [src: abstract], and screening breaks inside matter (arXiv:1411.4130) [src: abstract].
- **"A DESI background fit tests a modified-gravity theory."** A background w(z) can be reproduced with w = −1 and a suitable function in the local limit of non-local gravity (arXiv:2609.26517) [src: abstract]; `[der]` the perturbation sector is what separates the classes.
- **"Shift-symmetric Horndeski cannot cross w = −1."** Contested (arXiv:2610.36063 against arXiv:2508.17231) [src: abstracts].

## Not verified
<!-- key: not-verified -->

- Replies to the f(Q) ghost result of arXiv:2311.04201 were not searched beyond one relevance search.
- Whether the 2.8σ (arXiv:2605.12415) [src: abstract] and 2.9σ (arXiv:2606.31977) [src: abstract] results use overlapping data was not checked beyond their abstracts.
