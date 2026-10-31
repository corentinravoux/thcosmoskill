# Approximations of large-scale-structure perturbation theory

Scope: the approximations perturbative LSS calculations rely on, their validated range and quoted error, how they fail, convention traps and numerical issues.

Snapshot: 2026-10-31

## Physical approximations
<!-- key: physical-approximations -->

### Pressureless perfect fluid (single stream)
<!-- key: pressureless-perfect-fluid-single-stream -->

- **Assumes:** structure formation driven by matter with negligible velocity dispersion, so that the stress tensor, which measures the deviation of particle motions from a single coherent flow, is set to zero (Bernardeau et al. 2002, arXiv:astro-ph/0112551) [src: Sect. 2.2].
- **Fails:** at shell crossing, where the Lagrangian Jacobian vanishes and the density becomes singular (arXiv:astro-ph/0112551) [src: Sect. 2.5]. Ivanov calls the fluid "a wrong but useful model" and shows that its loop integrals are sensitive to UV modes, the UV part of $P_{13}$ scaling as $k^{2}P_{11}(k)$ times an integral of the linear spectrum up to the cut-off (arXiv:2212.08488) [src: Sect. 3 title; Eq. 72].
- **Fix:** the effective stress tensor of the EFTofLSS, a sound-speed term at leading order (`formalism.md`, section "Effective field theory").
- **Cite:** Bernardeau et al. (arXiv:astro-ph/0112551) for the fluid equations; Ivanov's review or Cabass et al. (arXiv:2203.08232) for the EFT.

### Einstein–de Sitter approximation for the time dependence
<!-- key: einstein-de-sitter-approximation-for-the-time -->

- **Assumes:** kernels computed for Ω_m = 1 and applied to ΛCDM through Ω_m/f² = 1 (Ivanov 2022, arXiv:2212.08488) [src: Sect. 3.2]. The local-in-time bias expansion is exact only in this approximation (Cabass et al. 2022, arXiv:2203.08232) [src: Sect. 3.6, footnote 5].
- **Validated:** accurate to $\mathcal{O}(0.1\div 1)\%$ for the redshifts of current and future surveys (arXiv:2203.08232) [src: Sect. 3.6, footnote 5]. Donath and Senatore find exact-to-EdS ratios of about 1.003 for the one-loop redshift-space galaxy monopole and about 1.007 for the quadrupole at $z=0.57$, sharply increasing at lower redshift, and a substantial part survives a shift of the bias coefficients; they conclude that the EdS approximation fits data only to roughly the precision of the next generation of surveys (arXiv:2005.04805) [src: abstract].
- **Fails:** for interacting dark sectors, where even weak interactions give kernels a non-trivial time dependence and one-loop deviations that can significantly exceed the percent level (Wolney et al. 2026, arXiv:2603.12431) [src: abstract]. Cosmologies whose growth is scale dependent (massive neutrinos, modified gravity) need the extensions of `formalism.md` and of `thcosmo-modified-gravity`.
- **Cite:** Donath & Senatore (arXiv:2005.04805) for ΛCDM; the atlas section "Perturbation-theory kernels" of the hub for the codes that keep exact time dependence.

### Perturbative expansion and its range: $k_{\rm max}$
<!-- key: perturbative-expansion-and-its-range-k-rm-max -->

- **Assumes:** k ≪ k_NL; the power counting of the scaling universe is in `formalism.md`, section "Effective field theory", with n = −1.5 and k_NL ~ 0.3 h/Mpc at z = 0 for ΛCDM (Ivanov 2022, arXiv:2212.08488) [src: Sect. 4.4].
- **Validated ranges quoted in the sources read:**

| Statistic and model | $k_{\rm max}$ | Redshift | Source |
|---|---|---|---|
| Redshift-space LRG-like galaxy power spectrum, one loop → two loops | 0.20 → 0.34 $h\,{\rm Mpc}^{-1}$ | 0.5 | Philcox 2026, arXiv:2610.13867 [src: abstract] |
| Redshift-space ELG-like galaxy power spectrum, one loop → two loops | 0.27 → 0.42 $h\,{\rm Mpc}^{-1}$ | 1.1 | arXiv:2610.13867 [src: abstract] |
| IR-resummed two-loop matter power spectrum, within 1% | about 0.6 h/Mpc | not stated in the abstract | Senatore & Zaldarriaga 2014, arXiv:1404.5954 [src: abstract] |
| Halo intrinsic-alignment spectra, one-loop EFT of IA | 0.30 h/Mpc | 0 | Bakx et al. 2023, arXiv:2303.15565 [src: abstract] |
| Halo IA spectra, NLA and TATT | 0.05 h/Mpc | 0 | arXiv:2303.15565 [src: abstract] |
| Halo IA bispectrum multipoles, tree level | $\lesssim 0.11$ h/Mpc | 0 | Bakx et al. 2025, arXiv:2507.06818 [src: abstract] |
| Matter–momentum bispectrum dipole, one loop, within 5% | 0.23 h/Mpc | 0.5 | Raikman et al. 2026, arXiv:2609.15750 [src: abstract] |
| Same, tree level | 0.07 h/Mpc | 0.5 | arXiv:2609.15750 [src: abstract] |
| Field-level Lyα forest model, 3D (1D) power within 1% (5%) | 0.3 (1.0) h/Mpc | 2.0–3.2 | de Belsunce et al. 2026, arXiv:2606.26234 [src: abstract] |

- **Fails:** a model pushed beyond its $k_{\rm max}$ biases the parameters; a higher loop order extends $k_{\rm max}$ but adds coefficients that can absorb the gain, as for $\sigma_8$ at two loops (arXiv:2610.13867) [src: abstract].

### Infrared resummation and the wiggle/no-wiggle split
<!-- key: infrared-resummation-and-the-wiggle-no-wiggle -->

- **Assumes:** a split of the linear spectrum into smooth and wiggly parts, $P_{11}(k)=P_{smooth}(k)+P_{w}(k)\,,$ (arXiv:2212.08488) [src: Eq. 37], and a separation scale $k_{S}$ between soft and hard modes in the damping $\Sigma^{2}$ (Eq. 109).
- **Why needed:** the IR limit of the one-loop spectrum, $P_{{\rm 1-loop}}\Big|_{q\ll k}=\left(\frac{569}{735}-\frac{47}{105}kP^{\prime}_{11}(k)+\frac{1}{10}k^{2}P^{\prime\prime}_{11}(k)\right)\sigma^{2}_{l}(k)\,,$ (arXiv:2212.08488) [src: Eq. 36], is large for an oscillating spectrum; earlier Eulerian EFT calculations showed a 2% BAO-related residual removed by the resummation (Senatore & Zaldarriaga 2014, arXiv:1404.5954) [src: abstract].
- **Variants:** for velocity statistics the bulk-flow dependence differs, and the IR resummation must be modified, recursively in powers of the velocity (Chen et al. 2025, arXiv:2508.00066) [src: abstract]. In LPT the long displacements are kept exponentiated, which resums them without a wiggle/no-wiggle split (Chen et al. 2020, arXiv:2012.04636) [src: abstract].
- **Fails:** resummation schemes that break Galilean invariance are susceptible to non-physical IR effects (Peloso & Pietroni 2013, arXiv:1302.0223) [src: abstract].
- **Cite:** Senatore & Zaldarriaga (arXiv:1404.5954), Baldauf et al. (arXiv:1504.04366), Blas et al. (arXiv:1605.02149).

### Phenomenological fingers of god
<!-- key: phenomenological-fingers-of-god -->

- **Assumes:** a damping function $D_{\rm FoG}$ with a velocity dispersion, replacing an exponential prefactor of the exact mapping (Taruya et al. 2010, arXiv:1006.0699) [src: Sect. IV.1, text after Eq. 24].
- **Error quoted:** phenomenological models without the A and B corrections give 1–2% systematic errors on distances and about 5% on the growth rate (arXiv:1006.0699) [src: abstract] (Fisher forecast).
- **Alternative:** EFT counterterms in $k^{2}\mu^{2n}$ and stochastic terms (Chen et al. 2020, arXiv:2012.04636) [src: Sect. 3, text after Eq. 4] <!-- num: not a value -->.

### Universality of the PNG bias
<!-- key: universality-of-the-png-bias -->

- **Assumes:** $b_{\phi}=2\delta_{c}(b_{1}-p)$ with p = 1 (Barreira 2020, arXiv:2009.06622) [src: abstract, inline].
- **Fails:** for realistic galaxy populations, through PNG assembly bias (de S. Nascimento & Dalal 2026, arXiv:2607.18229) [src: abstract].
- **Error quoted:** a 0.5σ to 1σ bias on $f_{\rm NL}$ in an idealised forecast when $p=1$ is assumed and the true value is 0.55 (arXiv:2009.06622) [src: abstract].

### No shell crossing in large-deviation statistics
<!-- key: no-shell-crossing-in-large-deviation-statistics -->

- **Assumes:** the spherical shells do not cross (Bernardeau 2015, arXiv:1511.08641) [src: abstract].
- **Validated:** PDFs accurate to a few percent against numerical integration and in excellent agreement with simulations over a wide range of densities, using the log-density (Uhlemann et al. 2016, arXiv:1512.05793) [src: abstract].

## Convention traps
<!-- key: convention-traps -->

- **Fourier factors.** Bernardeau et al. put the $(2\pi)^{3}$ in the forward transform and none in front of the Dirac delta of the power spectrum (arXiv:astro-ph/0112551) [src: Eq. 36; Sect. 3.2.2]; Ivanov puts $\int d^{3}k/(2\pi)^{3}$ in the inverse and $(2\pi)^{3}\delta_{D}$ in front of the polyspectra (arXiv:2212.08488) [src: Sect. 3.1, footnote 1; Eq. 33]. A loop integral copied from one into the other changes by powers of 2π. <!-- num: not a value -->
- **The $F_{2}$ dipole slip.** Ivanov's Eq. 28 prints the dipole of $F_{2}$ and $G_{2}$ without the factor one half of Bernardeau et al.'s Eqs. 45–46 (hub `stale-claims.md`); quote the kernels from arXiv:astro-ph/0112551. <!-- num: not a value -->
- **Two further printing slips in Ivanov's review (v1).** Eq. 32 writes $P_{13}$ as twice the correlator of the first- and second-order fields, where the third-order field is meant (the integral on the right-hand side contains $F_{3}$); Eq. 39, the UV limit of the one-loop terms, carries the label of the IR limit while its integrals run over k ≪ q (arXiv:2212.08488) [src: Eqs. 32, 39]. Both are described here in words, as printed; no correction is published as of the snapshot. Use Bernardeau et al. (arXiv:astro-ph/0112551, Eqs. 165–166) for the one-loop integrals and Ivanov's Eqs. 72 and 76 for the UV coefficients. <!-- num: not a value -->
- **Velocity divergence sign.** $\Theta=\frac{\theta}{f}=-\frac{\partial_{i}v^{i}}{f\mathcal{H}}\,,\quad\text{where}\quad f\equiv\frac{d\ln D_{+}}{d\ln a}$ (arXiv:2212.08488) [src: Eq. 23]. `[der]` Θ is minus the normalised divergence of the peculiar velocity, so a converging flow has positive Θ.
- **Tidal-bias normalisation.** In the co-evolution case Maus et al. write $b_{2}^{\rm E}=b_{2}^{\rm L}+\frac{8}{21}b_{1}^{\rm L}\quad,\quad b_{s}^{\rm E}=-\frac{2}{7}(b_{1}^{\rm E}-1)\quad,\quad b_{3}^{\rm E}=b_{1}^{\rm E}-1.$ (arXiv:2404.07272) [src: Sect. 3.5, Eq. 15] for velocileptors, and $b_{s^{2}}=-\frac{4}{7}(b^{\rm E}_{1}-1)\quad\text{and}\quad b_{3\rm nl}=\frac{32}{315}(b^{\rm E}_{1}-1).$ [src: Eq. 16] for FOLPS: the tidal operator is normalised differently in the two codes, and a tidal bias is meaningless without its operator.
- **Lagrangian and Eulerian bias.** Dalal et al. write the PNG term with the Lagrangian bias $b_{L}$ in Eq. 8 and with $b-1$ in the Eulerian form of Eq. 9 (arXiv:0710.4560) [src: Eqs. 8–9]. <!-- num: not a value -->
- `[der]` Inserting the Eulerian bias where the Lagrangian one is meant overestimates the scale-dependent term.
- **Units.** The reviews read quote lengths in $h^{-1}$Mpc and wavenumbers in $h\,{\rm Mpc}^{-1}$ (`formalism.md`, conventions table); the hub atlas, section "Units of lengths and wavenumbers", records the arguments against $h^{-1}$Mpc units. <!-- num: not a value -->

## Numerical issues
<!-- key: numerical-issues -->

- **FFTLog.** Loop integrals are evaluated by FFTLog; by 2022 it had been worked out to one loop for biased tracers in redshift space, for the two-loop matter power spectrum and one-loop matter bispectrum in real space, and for BAO resummation (Cabass et al. 2022, arXiv:2203.08232) [src: Sect. 3.11].
- **Two-loop evaluation.** The two-loop matter spectrum is evaluated fast by expanding the difference between the linear spectrum and a reference spectrum in a cosmology-independent basis resembling massive propagators, with local UV subtractions and local cancellation of IR singularities in the integrands (Anastasiou et al. 2025, arXiv:2509.05187) [src: abstract]; the two-loop redshift-space galaxy spectrum precomputes the loop integrals with the VEGAS algorithm so that the likelihood is evaluated in milliseconds (Philcox 2026, arXiv:2610.13867) [src: abstract].
- **IR cancellations.** The individual SPT kernels are IR enhanced as $\mathcal{O}(\varepsilon^{l-n})$ when momenta go soft (arXiv:2212.08488) [src: Eq. 29]; numerical integration must arrange the cancellation between $P_{22}$ and $P_{13}$ in the integrand, or work with IR-safe integrands (arXiv:2509.05187) [src: abstract].
- **Prior-volume effects.** Weakly constrained EFT nuisance parameters shift marginalised posteriors from the maximum; mitigations are reparameterisation (Tsedrik et al. 2025, arXiv:2509.09562) [src: abstract] and a Jeffreys prior or nonlinear orthogonalisation (Bonici et al. 2026, arXiv:2607.02498) [src: abstract].

## Referee checklist for a perturbation-theory paper
<!-- key: referee-checklist-for-a-perturbation-theory -->

1. Fourier convention stated, and loop integrals written consistently with it.
2. Kernels quoted from a source without the known $F_{2}$ dipole slip; EdS approximation stated, and its size estimated at the lowest redshift used (arXiv:2005.04805).
3. All counterterms and stochastic terms of the order computed included, in real and redshift space (arXiv:1409.1225 for the two new redshift-space counterterms at one loop).
4. IR resummation included for any statistic with BAO, and adapted for velocity statistics (arXiv:2508.00066).
5. Bias basis complete at the order computed (arXiv:1402.5916), the operator of each tidal bias stated, and any co-evolution relation flagged as an assumption.
6. $k_{\rm max}$ justified against simulations for the tracer, statistic and redshift used, not taken from another sample.
7. Priors on EFT parameters and their projection effects discussed (arXiv:2607.02498, arXiv:2509.09562).
8. For PNG: $b_{\phi}$ treatment stated, universality not assumed for galaxies without justification (arXiv:2607.18229, arXiv:2009.06622).
9. For consistency-relation tests: the equivalence-principle assumption stated (arXiv:1312.6074).
10. Forecasts labelled as forecasts.

## Not verified
<!-- key: not-verified -->

- The accuracy of the TNS model for biased tracers and of RegPT-type resummations was not read.
- The UV sensitivity of the two-loop counterterm structure beyond the abstracts of arXiv:2509.05187 and arXiv:2610.13867.
- The treatment of massive neutrinos in the EFT ("fast" and "slow" split) was read only in the Snowmass summary (arXiv:2203.08232, Sect. 3.10), not in the primary papers.
