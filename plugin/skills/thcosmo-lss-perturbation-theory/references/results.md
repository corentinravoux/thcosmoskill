# Results of large-scale-structure perturbation theory

Scope: theorems, computed coefficients, ranges of validity and comparisons with simulations that hold independently of one scheme, then the history of the key results.

Snapshot: 2026-10-31

## Computed coefficients and theorems
<!-- key: computed-coefficients-and-theorems -->

- The skewness of the unsmoothed density field at tree level is $\big<\delta^{3}\big>={(34/7)}\big<\delta^{2}\big>^{2}$ (Bernardeau et al. 2002, arXiv:astro-ph/0112551) [src: Sect. 5.1.1, inline]; with top-hat smoothing it becomes $S_{3}={34\over 7}+{{\rm d}\log\sigma^{2}(R)\over{\rm d}\log R}.$ (arXiv:astro-ph/0112551) [src: Eq. 238], which for a power-law spectrum $P(k)\propto k^{n}$ is $S_{3}={34/7}-(n+3)$ [src: Sect. 5.1.2, inline, text after Eq. 238]. Bernardeau et al. report that comparisons with simulations show Eq. 238 to be very accurate (Sect. 5.1.2, Fig. 27).
- The UV-sensitive part of the one-loop $P_{13}$ has coefficient $-61/(630\pi^{2})$ in front of $k^{2}P_{11}(k)\int dq\,P_{11}(q)$, and the UV part of $P_{22}$ has coefficient $9/(196\pi^{2})$ in front of $k^{4}$ (Ivanov 2022, arXiv:2212.08488) [src: Eqs. 72, 76]: the first renormalises the sound-speed counterterm, the second the $k^{4}$ stochastic term. <!-- num: not a value -->
- Uniqueness of the EFT formulations: Eulerian, Lagrangian and time-sliced formulations agree within their overlapping domains; at a given order in the IR and UV small parameters the differences appear only at higher order (Cabass et al. 2022, Snowmass white paper, arXiv:2203.08232) [src: Sect. 3.5].
- The renormalised two-loop dark-matter power spectrum in the EFTofLSS needs eight counterterms, including the effect of generated vorticity (Anastasiou et al. 2025, arXiv:2509.05187) [src: abstract].
- A complete two-loop model of the redshift-space galaxy power spectrum has 49 free coefficients, including fifth-order bias; it raises $k_{\rm max}$ from $0.20h\,\mathrm{Mpc}^{-1}$ to $0.34h\,\mathrm{Mpc}^{-1}$ for a luminous-red-galaxy sample at $z=0.5$ and from $0.27h\,\mathrm{Mpc}^{-1}$ to $0.42h\,\mathrm{Mpc}^{-1}$ for an emission-line-galaxy sample at $z=1.1$, validated on high-resolution simulations, but the constraints on $\sigma_8$ are not significantly enhanced because the extra information is absorbed by the new biases and counterterms (Philcox 2026, arXiv:2610.13867) [src: abstract].

- The two-loop galaxy power spectrum compared with galaxy–galaxy and galaxy–matter spectra needs 21 additional bias, higher-derivative and stochastic parameters per sample relative to one loop; it agrees with PT Challenge galaxy–galaxy and galaxy–matter spectra at the per-mille level up to k = 0.85 h/Mpc at $z=0.61$ and improves $σ_8$ by about 40% over one loop with conservative priors (Ivanov 2026, arXiv:2606.30713) [src: abstract]. Compare the redshift-space result above, where $σ_8$ does not improve significantly (arXiv:2610.13867) [src: abstract]; `open-questions.md` discusses the difference.
- Quadratic Lagrangian tidal bias of halos: a significant negative detection; cubic tidal biases broadly consistent with the Lagrangian local-in-matter-density ansatz, with indications of a positive Lagrangian coefficient of the time derivative of the tidal field (Lazeyras & Schmidt 2018, arXiv:1712.07531) [src: abstract].
- Bias operators of halos and galaxies up to quartic order have been detected in simulations (Cabass et al. 2022, arXiv:2203.08232) [src: Sect. 3.6].
- The constant large-scale limit of tracer stochasticity follows from the non-conservation of mass and momentum for tracers counted with equal weight; for matter the stochastic spectrum starts at $k^{4}$ (arXiv:2203.08232) [src: Sect. 3.6; arXiv:2212.08488, Eq. 64].
- Large-deviation one-point PDFs from spherical collapse with a log-density transformation are accurate to a few percent against numerical integration and agree with N-body simulations over a wide range of densities (Uhlemann et al. 2016, arXiv:1512.05793) [src: abstract].

- Massive neutrinos and EdS kernels: with the Newtonian-motion-gauge method, the real-space one-loop power spectrum deviates from the standard EdS-kernel calculation by less than 0.7% for $M_\nu<0.30$ eV, but the one-loop redshift-space quadrupole deviates by 1.7% at k = 0.3 h/Mpc and z = 0, mainly through the effect of the cosmological constant on the growth of the velocity field (Fidler et al. 2026, arXiv:2605.05114) [src: abstract].
- Mixed dark matter: the extended EFTofLSS with a non-cold component as a fluid with finite sound speed gives somewhat weaker bounds on the energy density in ultra-light axions from Planck and BOSS than earlier analyses (Verdiani et al. 2025, arXiv:2507.08792) [src: abstract].
- LSS bootstrap from data: BOSS DR12 LRG power spectrum and bispectrum monopole constrain the fractional growth-rate deviation $\varepsilon_f$ to about 7% and the quadratic-kernel deviation $\varepsilon_{d_γ}$ to about 57% (Biselli et al. 2026, arXiv:2605.13298) [src: abstract].
- Galaxy trispectrum: adding the tree-level redshift-space trispectrum to the one-loop power spectrum and tree-level bispectrum can improve the constraint on $ω_{\rm cdm}$ by up to 15% in a DESI-like volume (Tucci & Philcox 2026, arXiv:2610.08908) [src: abstract] (forecast).

## Validity ranges against simulations
<!-- key: validity-ranges-against-simulations -->

The table of $k_{\rm max}$ values with sources is in `approximations.md`, section "Perturbative expansion and its range". Comparisons of codes:

- Velocileptors, PyBird and Folps$\nu$ give consistent constraints on AbacusSummit mocks in both full-shape and ShapeFit fits, agree with each other's synthetic data within the scales where one-loop theory applies, and show no modelling systematic for the DESI Y1 volume (Maus et al. 2024, arXiv:2404.07272) [src: abstract].
- The one-loop LPT model with full IR resummation describes halo and mock-galaxy power spectra and correlation functions at the percent level on quasi-linear scales (Chen et al. 2020, arXiv:2012.04636) [src: abstract].
- One-loop pairwise velocity statistics recover the growth rate to better than percent precision against N-body simulations (Chen et al. 2025, arXiv:2508.00066) [src: abstract].
- The tree-level redshift-space galaxy trispectrum, with improved FoG treatment, allows k_max = 0.12 h/Mpc depending on the tracer, validated on 25 AbacusSummit simulations (Tucci & Philcox 2026, arXiv:2610.08908) [src: abstract].
- The EdS approximation shifts the one-loop redshift-space galaxy monopole by a factor about 1.003 and the quadrupole by about 1.007 at $z=0.57$ (Donath & Senatore 2020, arXiv:2005.04805) [src: abstract].

## History of the key results
<!-- key: history-of-the-key-results -->

| Date | Result | Status | Source |
|---|---|---|---|
| 2002 | Review of SPT, LPT, tree-level and one-loop statistics, one-point cumulants | reference for kernels and cumulants | Bernardeau et al., arXiv:astro-ph/0112551 [src: Sects. 2, 4, 5] |
| 2007 | Scale-dependent bias from local PNG, confirmed in N-body simulations | current; universality of $b_{\phi}$ disputed (`models.md`) | Dalal et al., arXiv:0710.4560 [src: abstract] |
| 2010 | TNS redshift-space model with A and B corrections | partly superseded by EFT counterterms for FoG | Taruya et al., arXiv:1006.0699 [src: abstract] |
| 2014 | IR-resummed EFT; renormalised bias with tidal and velocity-potential operators; EFT redshift-space counterterms | current | arXiv:1404.5954, arXiv:1402.5916, arXiv:1409.1225 [src: abstracts] |
| 2022 | State of the art: matter in real space to three loops (power spectrum), two loops (bispectrum), one loop (trispectrum); biased tracers in real space at one loop; biased tracers in redshift space at one loop (power spectrum) and tree level (bispectrum) | superseded for redshift-space tracers (rows below) | Cabass et al., arXiv:2203.08232 [src: Sect. 3.11, Table 1] |
| 2025 | Fast evaluation of the renormalised two-loop matter power spectrum, eight counterterms | current | Anastasiou et al., arXiv:2509.05187 [src: abstract] |
| 2026 | Two-loop galaxy power spectrum, 21 added parameters, TSPT IR resummation | current | Ivanov, arXiv:2606.30713 [src: abstract] |
| 2026 | Two-loop redshift-space galaxy power spectrum, 49 coefficients | current | Philcox, arXiv:2610.13867 [src: abstract] |
| 2026 | Tree-level EFT model of the redshift-space galaxy trispectrum | current | Tucci & Philcox, arXiv:2610.08908 [src: abstract] |

## Not verified
<!-- key: not-verified -->
