# Models of large-scale-structure perturbation theory

Scope: perturbative schemes, bias models and redshift-space models of the large-scale structure, one card per scheme; a "model" here is a calculational scheme or a parameterisation of tracers, not a cosmological model.

Snapshot: 2026-10-31

The schemes are chosen by their weight in the two reviews that structure this skill (Ivanov's 2022 review and Cabass et al. 2022, arXiv:2203.08232) and in the 2025–2026 literature searched. Their formalism is in `formalism.md`; their range of validity in `approximations.md`. Observational status means here whether a scheme is used in, and validated for, a survey analysis; measured cosmological values belong to cosmoskill `cosmo-galaxy-clustering`.

## Perturbative schemes for matter
<!-- key: perturbative-schemes-for-matter -->

### Standard perturbation theory (SPT)
<!-- key: standard-perturbation-theory-spt -->
- **Defining equations:** pressureless perfect fluid, continuity equation ${\partial\tilde{\delta}({\bf k},\tau)\over{\partial\tau}}+\tilde{\theta}({\bf k},\tau)=-\int{\rm d}^{3}{\bf k}_{1}{\rm d}^{3}{\bf k}_{2}\delta_{D}({\bf k}-{\bf k}_{12})\alpha({\bf k}_{1},{\bf k}_{2})\tilde{\theta}({\bf k}_{1},\tau)\tilde{\delta}({\bf k}_{2},\tau),$ (arXiv:astro-ph/0112551) [src: Eq. 37] and the Euler equation (Eq. 38), solved order by order with kernels $F_{n}$, $G_{n}$ (Eqs. 43–46).
- **Parameters:** none beyond the linear power spectrum and the growth history; the EdS kernels assume Ω_m/f² = 1 (arXiv:2212.08488, Sect. 3.2).
- **Predictions:** tree-level skewness $S_{3}={34\over 7}+{{\rm d}\log\sigma^{2}(R)\over{\rm d}\log R}.$ (arXiv:astro-ph/0112551) [src: Eq. 238]; one-loop power spectrum $P^{(1)}(k,\tau)=P_{22}(k,\tau)+P_{13}(k,\tau),$ [src: Eq. 164].
- **Consistency:** the loop integrals depend on modes beyond the non-linear scale, where the fluid description fails; the UV part of $P_{13}$ is $-\frac{61}{630\pi^{2}}k^{2}P_{11}(k)\int^{\Lambda}_{q_{\rm trust}}dq~P_{11}(q)$ (Ivanov 2022, arXiv:2212.08488) [src: Eq. 72], cut-off dependent; reply: the EFTofLSS absorbs it in the sound-speed counterterm (same review, Eq. 73). Many resummation schemes built on SPT violate Galilean invariance and are therefore susceptible to non-physical infrared effects (Peloso & Pietroni 2013, arXiv:1302.0223) [src: abstract]; reply: none found for the schemes named there.
- **Observational status:** not used alone in current full-shape analyses of the sources read; its renormalised form is the EFTofLSS card below. The tree-level matter–momentum bispectrum breaks down beyond k_max = 0.07 h/Mpc at $z=0.5$ against simulations (Raikman et al. 2026, arXiv:2609.15750) [src: abstract].
- **Status date:** 2026-10-31

### Lagrangian perturbation theory and the Zel'dovich approximation
<!-- key: lagrangian-perturbation-theory-and-the-zel -->
- **Defining equations:** ${\bf x}(\tau)={\bf q}+{\bf\Psi}({\bf q},\tau).$ (arXiv:astro-ph/0112551) [src: Eq. 88], with $1+\delta({\bf x})=\frac{1}{{\rm Det}\Big(\delta_{ij}+\Psi_{i,j}\Big)}\equiv\frac{1}{J({\bf q},\tau)},$ [src: Eq. 91] and the Zel'dovich solution $\nabla_{q}\cdot{\bf\Psi}^{(1)}=-D_{1}(\tau)\ \delta({\bf q}),$ [src: Eq. 92].
- **Parameters:** linear spectrum and growth; second-order growth $D_{2}(\tau)\approx-\frac{3}{7}D_{1}^{2}(\tau),$ (arXiv:astro-ph/0112551) [src: Eq. 95].
- **Predictions:** the Zel'dovich power spectrum, $P_{\rm Zel}(k)=4\pi\sum_{n=0}^{\infty}\int dq\,q^{2}\ e^{-\frac{1}{2}k^{2}(X+Y)}\Big(\frac{kY}{q}\Big)^{n}j_{n}(kq)$ (Chen et al. 2020, arXiv:2012.04636) [src: Eq. 8], which damps the BAO through the exponentiated displacement cumulant.
- **Consistency:** at shell crossing the Jacobian vanishes, the density becomes singular and the mapping description no longer holds; after shell crossing the Zel'dovich approximation lets matter flow through pancakes and washes out small-scale structure (Bernardeau et al., arXiv:astro-ph/0112551) [src: Sects. 2.5, 2.8]; reply: the Lagrangian EFT adds counterterms for the small-scale physics (arXiv:2012.04636, Sect. 3). The LDP derivation of one-point statistics shares the no-shell-crossing assumption (arXiv:1511.08641) [src: abstract].
- **Observational status:** basis of the Lagrangian EFT card below; the Zel'dovich approximation alone is not used as a full-shape model in the sources read.
- **Status date:** 2026-10-31

### EFT of large-scale structure (Eulerian, IR-resummed)
<!-- key: eft-of-large-scale-structure-eulerian-ir -->
- **Defining equations:** fluid equations with an effective stress tensor (Ivanov 2022, Eq. 53), at leading order $\frac{1}{\rho_{\ell}}[\partial_{j}\sigma^{ij}]_{\Lambda}=c_{s}^{2}(\tau)\partial^{i}\delta({\bf x},\tau)\,,$ (arXiv:2212.08488) [src: Eq. 56], giving $P_{\text{non-linear}}(k)=P_{11}(k,\eta)+P_{22}^{\Lambda}(k,\eta)+P_{13}^{\Lambda}(k,\eta)-2\gamma_{\Lambda}k^{2}P_{11}(k,\eta)+P_{J}(k)\,.$ [src: Eq. 70], with IR resummation of the wiggly part $P_{w}^{\text{IR res, LO}}=e^{-\Sigma^{2}k^{2}}P_{w}(\eta;k)\quad\text{where}\\ \Sigma^{2}=\frac{4\pi}{3}\int_{0}^{k_{S}}dqP_{\rm smooth}(q)\left[1-j_{0}\left(qr_{\rm BAO}\right)+2j_{2}\left(qr_{\rm BAO}\right)\right]\,.$ [src: Eq. 109].
- **Parameters:** for matter at one loop the counterterm $\gamma$ (or $c_{s}^{2}$) and the $k^{4}$ stochastic amplitude; for galaxies in real space $b_{1},b_{2},b_{\mathcal{G}_{2}},b_{\nabla^{2}\delta},b_{\Gamma_{3}}$ and the stochastic field (Cabass et al. 2022, arXiv:2203.08232, Eq. 3.24); redshift space adds counterterms (two new ones for matter at one loop, Senatore & Zaldarriaga 2014, arXiv:1409.1225, abstract). Two loops: eight counterterms for matter (arXiv:2509.05187, abstract) and 49 coefficients for redshift-space galaxies (arXiv:2610.13867, abstract) <!-- num: not a value -->.
- **Predictions:** Senatore and Zaldarriaga's IR-resummed two-loop matter spectrum agrees with simulations within 1% up to k ~ 0.6 h/Mpc (arXiv:1404.5954) [src: abstract]; the two-loop redshift-space galaxy spectrum reaches k_max = 0.34 h/Mpc for an LRG-like sample at $z=0.5$ against $0.20h\,\mathrm{Mpc}^{-1}$ at one loop (Philcox 2026, arXiv:2610.13867) [src: abstract].
- **Consistency:** prior-volume projection effects: weakly constrained EFT nuisance parameters shift marginalised posteriors away from the posterior maximum, by several σ in $H_{0}$, $w_{0}$, $w_{a}$ with baseline priors in DESI DR1 power-spectrum fits (Bonici et al. 2026, arXiv:2607.02498) [src: abstract]; reply: reparameterisation of the nuisance parameters (Tsedrik, Carrilho & Moretti 2025, arXiv:2509.09562) [src: abstract] or a Jeffreys prior over all EFT coefficients (arXiv:2607.02498) [src: abstract]. The EdS approximation of the kernels biases the redshift-space monopole by a factor about 1.003 and the quadrupole by about 1.007 at $z=0.57$, rising at lower redshift (Donath & Senatore 2020, arXiv:2005.04805) [src: abstract]; reply: exact time dependence is not demanding to implement (same paper, abstract).
- **Observational status:** in use for DESI. Maus et al. found consistent constraints from velocileptors, PyBird and Folps$\nu$ on AbacusSummit mocks and no systematic error from the modelling of the redshift-space galaxy power spectrum for the DESI Y1 volume (arXiv:2404.07272) [src: abstract]. The independent DESI DR1 reanalysis with power spectrum and bispectrum gives $Ω_m=0.284\pm 0.011$ and $σ_8=0.811\pm 0.030$ in ΛCDM with external priors on the baryon density and the tilt (Chudaykin, Ivanov & Philcox 2025, arXiv:2507.13433) [src: abstract]; measured values belong to cosmoskill `cosmo-galaxy-clustering`.
- **Status date:** 2026-10-31

### Lagrangian EFT and convolution LPT (velocileptors family)
<!-- key: lagrangian-eft-and-convolution-lpt -->
- **Defining equations:** $1+\delta_{m}(\textbf{x})=\int d^{3}\textbf{q}\ \delta_{D}(\textbf{x}-\textbf{q}-\boldsymbol{\Psi}(\textbf{q}))\quad,\quad(2\pi)^{3}\delta_{D}(\textbf{k})+\tilde{\delta}_{m}(\textbf{k})=\int d^{3}\textbf{q}\ e^{i\textbf{k}\cdot(\textbf{q}+\boldsymbol{\Psi})}$ (Chen et al. 2020, arXiv:2012.04636) [src: Eq. 1], with the linear displacement cumulant kept exponentiated, $\left\langle e^{i\textbf{k}\cdot\Delta^{(1)}}\right\rangle=e^{-\frac{1}{2}k_{i}k_{j}A^{(11)}_{ij}}$ [src: Eq. 6].
- **Parameters:** Lagrangian biases $b_{1},b_{2},b_{s},b_{3}$, counterterms $\alpha_{0},\alpha_{2},\alpha_{4},\alpha_{6}$ and stochastic terms $R_{h}^{3}$, $\sigma_{2}$, $\sigma_{4}$ (arXiv:2012.04636) [src: Sect. 3, text after Eq. 4] <!-- num: not a value -->.
- **Predictions:** the one-loop redshift-space model with full IR resummation of displacements and velocities predicts halo and mock-galaxy power spectra and correlation functions at the percent level on quasi-linear scales, including BAO damping, and recovers unbiased cosmological parameters in mocks larger than future surveys (arXiv:2012.04636) [src: abstract].
- **Consistency:** the earlier convolution LPT agreed with simulations for real-space correlation functions and the redshift-space monopole, but worse for higher multipoles of the redshift-space halo correlation function (Carlson, Reid & White 2013, arXiv:1209.0780) [src: abstract]; reply: the 2020 model resums the velocities as well and compares favourably with the moment expansion and the Gaussian streaming model (arXiv:2012.04636) [src: abstract]. Uniqueness: Eulerian and Lagrangian EFTs agree within their overlapping domains to the order computed (Cabass et al., arXiv:2203.08232) [src: Sect. 3.5].
- **Observational status:** one of the three pipelines validated for DESI Y1 full-shape fits, with no modelling systematic found for that volume (Maus et al., arXiv:2404.07272) [src: abstract].
- **Status date:** 2026-10-31

### Time-sliced perturbation theory (TSPT)
<!-- key: time-sliced-perturbation-theory-tspt -->
- **Defining equations:** a path integral over the velocity-divergence field at fixed time, $Z[J_{\delta},J;\eta]=\int[\mathcal{D}\Theta]\mathcal{P}[\Theta;\eta]\exp\left\{\int_{\bf k}\Theta({\bf k})J(-{\bf k})+\int_{\bf k}\delta[\Theta;\eta,{\bf k}]J_{\delta}(-{\bf k})\right\}\,.$ (Ivanov 2022, arXiv:2212.08488) [src: Eq. 89], with the distribution function evolved by $\partial_{\eta}\mathcal{P}[\Theta,\tau]+\int_{\bf k}\frac{\delta}{\delta\Theta({\bf k})}(\mathcal{P}[\Theta,\tau]\mathcal{I}[\Theta;\eta])=0\,.$ [src: Eq. 91].
- **Parameters:** as for the EFTofLSS (counterterms), plus the IR separation scale $k_{S}$ of Eq. 109.
- **Predictions:** resummed matter power spectrum to next-to-leading order and bispectrum at leading order; the two-point correlation function agrees well with N-body data at BAO scales, and the non-linear BAO peak shift can be assessed reliably (Blas et al. 2016, arXiv:1605.02149) [src: abstract].
- **Consistency:** the TSPT vertices are IR safe, $\lim_{\varepsilon\to 0}\bar{\Gamma}_{n}({\bf k}_{1},...,{\bf k}_{l},\varepsilon{\bf q}^{\prime}_{1},...,\varepsilon{\bf q}^{\prime}_{n-l})=\mathcal{O}(\varepsilon^{0})\,.$ (arXiv:2212.08488) [src: Eq. 103], unlike the SPT kernels; critique: none found.
- **Observational status:** its IR resummation is the one written in the Eulerian EFT card above (Ivanov 2022, Sect. 5.3); a separate data verdict was not found in the sources read.
- **Status date:** 2026-10-31

## Redshift-space models
<!-- key: redshift-space-models -->

### TNS model
<!-- key: tns-model -->
- **Defining equations:** $P^{\rm(S)}(k,\mu)=D_{\rm FoG}[k\mu\,f\,\sigma_{\rm v}]\,\Bigl\{P_{\delta\delta}(k)+2\,f\,\mu^{2}\,P_{\delta\theta}(k)\qquad+f^{2}\,\mu^{4}\,P_{\theta\theta}(k)+A(k,\mu)+B(k,\mu)\Bigr\}.$ (Taruya, Nishimichi & Saito 2010, arXiv:1006.0699) [src: Eq. 24].
- **Parameters:** the velocity dispersion $\sigma_{\rm v}$ and the functional form of $D_{\rm FoG}$, in addition to the cosmology entering $P_{\delta\delta}$, $P_{\delta\theta}$, $P_{\theta\theta}$ and the corrections A, B.
- **Predictions:** excellent agreement with the monopole and quadrupole of N-body simulations over BAO scales; phenomenological models without the A and B terms produce systematic errors of 1–2% on the angular diameter distance and the Hubble parameter and about 5% on the growth rate (arXiv:1006.0699) [src: abstract] (Fisher forecast).
- **Consistency:** the FoG damping function is phenomenological (it replaces an exponential prefactor, Sect. IV.1); the EFT treats the same physics with counterterms and stochastic terms (Chen et al. 2020, arXiv:2012.04636) [src: Sect. 3, text after Eq. 4]; reply: none found.
- **Observational status:** not among the DESI full-shape pipelines compared by Maus et al. (arXiv:2404.07272) [src: abstract].
- **Status date:** 2026-10-31

## Tracer models
<!-- key: tracer-models -->

### Eulerian bias expansion in the Galileon basis
<!-- key: eulerian-bias-expansion-in-the-galileon-basis -->
- **Defining equations:** $\delta_{g}=b_{1}\delta+\frac{b_{2}}{2}\delta^{2}+b_{\mathcal{G}_{2}}\mathcal{G}_{2}+b_{\nabla^{2}\delta}\nabla^{2}\delta+b_{\Gamma_{3}}\Gamma_{3}+\varepsilon+...\,,$ (Cabass et al. 2022, arXiv:2203.08232) [src: Eq. 3.24], with $\mathcal{G}_{2}(\Phi)\equiv(\partial_{i}\partial_{j}\Phi)^{2}-(\Delta\Phi)^{2}\,,\quad\Gamma_{3}\equiv\mathcal{G}_{2}(\Phi)-\mathcal{G}_{2}(\Phi_{v})\,,$ [src: Eq. 3.25].
- **Parameters:** the time-dependent Wilson coefficients $b_{1},b_{2},b_{\mathcal{G}_{2}},b_{\nabla^{2}\delta},b_{\Gamma_{3}}$, the scale $R_{*}$ and the stochastic amplitude (arXiv:2203.08232, Sect. 3.6).
- **Predictions:** for halos and galaxies, bias parameters up to quartic order have been detected in simulations (arXiv:2203.08232) [src: Sect. 3.6]; the quadratic Lagrangian tidal bias of halos is significantly negative, and the cubic tidal parameters are broadly consistent with the Lagrangian local-in-matter-density ansatz (Lazeyras & Schmidt 2018, arXiv:1712.07531) [src: abstract].
- **Consistency:** the basis is complete and closed under renormalisation only with tidal, velocity-potential and higher-derivative operators (Assassi et al. 2014, arXiv:1402.5916; Mirbabayi, Schmidt & Zaldarriaga 2014, arXiv:1412.5169) [src: abstracts]; the local-in-time form holds only in the EdS approximation (arXiv:2203.08232) [src: Sect. 3.6, footnote 5]; reply: Donath and Senatore give the irreducible basis with exact time dependence, still seven-dimensional at one loop but slightly different (arXiv:2005.04805) [src: abstract].
- **Observational status:** the bispectrum of DESI DR1 improves the measurement of the quadratic biases, which are consistent with predictions from halo occupation models (Chudaykin et al. 2025, arXiv:2507.13433) [src: abstract].
- **Status date:** 2026-10-31

### Scale-dependent bias from local PNG with the universality relation
<!-- key: scale-dependent-bias-from-local-png-with-the -->
- **Defining equations:** $\Delta b(k)=2(b-1)f_{\rm NL}\delta_{c}\frac{3\Omega_{m}}{2a\,g(a)r_{H}^{2}k^{2}}$ (Dalal et al. 2008, arXiv:0710.4560) [src: Eq. 9].
- **Parameters:** $f_{\rm NL}$ and $b_{\phi}$; the universality relation fixes $b_{\phi}=2\delta_{c}(b_{1}-p)$ with p = 1 (Barreira 2020, arXiv:2009.06622) [src: abstract, inline].
- **Predictions:** a $k^{-2}$ enhancement of the tracer power spectrum on large scales, confirmed in N-body simulations (arXiv:0710.4560) [src: abstract].
- **Consistency:** $b_{\phi}$ is completely degenerate with $f_{\rm NL}$ in the power spectrum and universality breaks down for realistic galaxies through PNG assembly bias (de S. Nascimento & Dalal 2026, arXiv:2607.18229) [src: abstract]; assuming $p=1$ when the true value is 0.55 biases $f_{\rm NL}$ by $0.5σ$ to $1σ$ in an idealised forecast, and priors Δp ≈ 0.5 suffice to remove the bias (arXiv:2009.06622) [src: abstract]; reply: the time-evolution estimator infers $b_{\phi}$ from the redshift evolution of number counts (arXiv:2607.18229) [src: abstract].
- **Observational status:** DESI DR1 power spectra and bispectra in a one-loop EFT give $f^{\rm loc}_{\rm NL}=-0.1\pm 7.4$ at 68% CL (Chudaykin, Ivanov & Philcox 2025, arXiv:2512.04266) [src: abstract]; measured values belong to cosmoskill `cosmo-inflation-primordial`.
- **Status date:** 2026-10-31

### EFT of intrinsic alignments (versus NLA and TATT)
<!-- key: eft-of-intrinsic-alignments-versus-nla-and-tatt -->
- **Defining equations:** $g_{ij}(\mathbf{x},\eta)=\text{TF}(S)_{ij}(\mathbf{x},\eta)=\sum_{\mathcal{O^{\prime}}}b_{\mathcal{O^{\prime}}}(\eta)\mathcal{O}^{\prime}_{ij}(\mathbf{x},\eta).$ (Bakx et al. 2023, arXiv:2303.15565) [src: Eq. 16], with operators built from $\Pi^{[1]}_{ij}(\mathbf{x},\eta):=\frac{\partial_{i}\partial_{j}}{\nabla^{2}}\delta(\mathbf{x},\eta)=K_{ij}(\mathbf{x},\eta)+\frac{1}{3}\delta_{ij}\delta(\mathbf{x},\eta);$ [src: Eq. 12].
- **Parameters:** 8 free bias parameters at one loop (arXiv:2303.15565) [src: abstract].
- **Predictions:** describes dark-matter halo shape multipoles up to k_max = 0.30 h/Mpc at $z=0$, against k_max = 0.05 h/Mpc for NLA and TATT, and describes the B-mode auto-spectrum (arXiv:2303.15565) [src: abstract].
- **Consistency:** the first- and second-order EFT parameters from the tree-level IA bispectrum agree with those from the one-loop power spectrum without priors (Bakx et al. 2025, arXiv:2507.06818) [src: abstract]; critique: none found.
- **Observational status:** validated on simulations only in the sources read (arXiv:2303.15565, arXiv:2507.06818, arXiv:2610.36027) [src: abstracts]; measured IA amplitudes belong to cosmoskill `cosmo-weak-lensing`.
- **Status date:** 2026-10-31

## Non-perturbative and symmetry-based schemes
<!-- key: non-perturbative-and-symmetry-based-schemes -->

### Large-deviation one-point statistics (spherical collapse)
<!-- key: large-deviation-one-point-statistics-spherical -->
- **Defining equations:** $\lim_{\epsilon\to 0}\epsilon\,\log\left[P_{\epsilon}(\{\alpha_{i}\}\in A)\right]=-\inf_{\underline{\alpha}\in A}I(\underline{\alpha})$ (Bernardeau 2015, arXiv:1511.08641) [src: Eq. 4] and $\Psi({\underline{\rho}})=\inf_{{\underline{\rho}}=\zeta({\underline{\tau}})}I({\underline{\tau}})\,,$ [src: Eq. 9].
- **Parameters:** the linear variance at the cell radius and the spherical-collapse mapping ζ; tracers add a non-linear bias and stochasticity (Vos-Gines & Uhlemann 2026, arXiv:2607.06526) [src: abstract].
- **Predictions:** one- and two-cell PDFs accurate to a few percent against numerical integration and in excellent agreement with N-body simulations over a wide range of densities (Uhlemann et al. 2016, arXiv:1512.05793) [src: abstract].
- **Consistency:** requires the absence of shell crossing (arXiv:1511.08641) [src: abstract]; reply: none found.
- **Observational status:** forecast-level for HI intensity mapping, where the PDF breaks the degeneracy between linear bias and clustering amplitude (arXiv:2607.06526) [src: abstract] (forecast).
- **Status date:** 2026-10-31

### LSS bootstrap
<!-- key: lss-bootstrap -->
- **Defining equations:** not transcribed; the bootstrap fixes the form of the kernels from symmetries and the equivalence principle at the field level (Cabass et al. 2022, arXiv:2203.08232) [src: Sect. 3.9].
- **Parameters:** fractional deviations $\varepsilon_f$ of the linear growth rate and $\varepsilon_{d_γ}$ of the quadratic kernel (Biselli et al. 2026, arXiv:2605.13298) [src: abstract].
- **Predictions:** separates changes to the background expansion from changes to non-linear structure formation (arXiv:2605.13298) [src: abstract].
- **Consistency:** none found.
- **Observational status:** BOSS DR12 LRG power spectrum plus bispectrum monopole give about 7% on $\varepsilon_f$ and 57% on $\varepsilon_{d_γ}$; the PT Challenge simulations, about 100 times the volume, give about 1% and 25% (arXiv:2605.13298) [src: abstract].
- **Status date:** 2026-10-31

## Not verified
<!-- key: not-verified -->

- The operator definitions of Desjacques, Jeong and Schmidt (arXiv:1611.09787) and their conversion to the Galileon basis: no HTML rendering.
- The Kaiser formula in Kaiser's original 1987 paper (not on arXiv); only Ivanov's transcription (arXiv:2212.08488, Eq. 127) was read.
- Renormalised perturbation theory, RegPT and other resummation schemes named in Bernardeau et al. and Peloso–Pietroni were not given cards: their equations were not read.
