# Pilot review — thcosmo-lss-perturbation-theory

For each item: verdict `correct`, `wrong` or `unclear`, and a comment. Then up to five general remarks at the end. About two hours.

## Equation (8 of 72)

### 1. thcosmo-lss-perturbation-theory/references/formalism.md:19

| Units of lengths | not stated in the sections read (arXiv:astro-ph/0112551) | $\langle s_{i}(0)s^{i}(0)\rangle\approx[6~h^{-1}\text{Mpc}]^{2}\,.$ (arXiv:2212.08488) [src: Eq. 18] |

- Verdict: 
- Comment: 

### 2. thcosmo-lss-perturbation-theory/references/formalism.md:29

Bernardeau et al. (arXiv:astro-ph/0112551) write the continuity equation in Fourier space for a pressureless fluid as ${\partial\tilde{\delta}({\bf k},\tau)\over{\partial\tau}}+\tilde{\theta}({\bf k},\tau)=-\int{\rm d}^{3}{\bf k}_{1}{\rm d}^{3}{\bf k}_{2}\delta_{D}({\bf k}-{\bf k}_{12})\alpha({\bf k}_{1},{\bf k}_{2})\tilde{\theta}({\bf k}_{1},\tau)\tilde{\delta}({\bf k}_{2},\tau),$ [src: Eq. 37]; the Euler equation (Eq. 38) has the same structure with the coupling β acting on two velocity divergences.

- Verdict: 
- Comment: 

### 3. thcosmo-lss-perturbation-theory/references/formalism.md:23

Ivanov (arXiv:2212.08488) normalises the velocity divergence by the growth rate, $\Theta=\frac{\theta}{f}=-\frac{\partial_{i}v^{i}}{f\mathcal{H}}\,,\quad\text{where}\quad f\equiv\frac{d\ln D_{+}}{d\ln a}$ [src: Eq. 23]: the sign of Θ is opposite to the sign of the divergence of the peculiar velocity, which is the convention that makes $G_{1}=1$.

- Verdict: 
- Comment: 

### 4. thcosmo-lss-perturbation-theory/references/formalism.md:106

In the DHOST example of the Snowmass white paper the tree-level bispectrum keeps the standard form $B_{t}({\bf q},{\bf k}_{1},{\bf k}_{2})=2F_{2}({\bf q},{\bf k}_{1})P_{11}(q)P_{11}(k_{1})+\text{2 perms.}\ ,$ (arXiv:2203.08232) [src: Eq. 4.38], with deviations from ΛCDM parameterised as $A_{\alpha}=1+\Delta A_{\alpha}\ ,\quad\text{and}\quad A_{\gamma}=A_{\gamma}^{\Lambda\text{CDM}}+\Delta A_{\gamma}\ .$ [src: Eq. 4.40].

- Verdict: 
- Comment: 

### 5. thcosmo-lss-perturbation-theory/references/formalism.md:44

The EFTofLSS adds to the Euler equation the divergence of an effective stress tensor of the long-wavelength fluid: $\frac{\partial}{\partial\tau}\delta_{\ell}+\partial_{i}[(1+\delta_{\ell})v^{i}_{\ell}]=0\,,\\ \frac{\partial}{\partial\tau}v^{i}_{\ell}+\mathcal{H}v^{i}_{\ell}+v^{j}_{\ell}\partial_{j}v^{i}_{\ell}+\partial_{i}\Phi_{\ell}=-\frac{1}{\rho_{\ell}}[\partial_{j}\sigma^{ij}]_{\Lambda}\,,$ (arXiv:2212.08488) [src: Eq. 53].

- Verdict: 
- Comment: 

### 6. thcosmo-lss-perturbation-theory/references/formalism.md:76

At next-to-leading order (one hard loop), Baldauf et al. write the IR-resummed spectrum as $\tilde{P}(k)=P_{\rm lin}^{nw}(k)+P_{\rm 1-loop}^{nw}(k)\\[8.0pt] +e^{-\Sigma^{2}_{\epsilon k}k^{2}}(1+\Sigma^{2}_{\epsilon k}k^{2})P^{w}_{\rm lin}(k)+e^{-\Sigma^{2}_{\epsilon k}k^{2}}P^{w}_{\rm 1-loop}(k),$ (arXiv:1504.04366) [src: Eq. 21], with the counterterm included in $P_{\rm 1-loop}(k)=P_{13}(k)+P_{22}(k)-2R^{2}k^{2}P_{\rm lin}(k),$ [src: Eq. 22].

- Verdict: 
- Comment: 

### 7. thcosmo-lss-perturbation-theory/references/formalism.md:63

The 2LPT positions are ${\bf x}({\bf q})={\bf q}-D_{1}\ \nabla_{q}\phi^{(1)}+D_{2}\ \nabla_{q}\phi^{(2)},$ (arXiv:astro-ph/0112551) [src: Eq. 98], with $\nabla_{q}^{2}\phi^{(2)}({\bf q})=\sum_{i>j}[\phi_{,ii}^{(1)}({\bf q})\ \phi_{,jj}^{(1)}({\bf q})-(\phi_{,ij}^{(1)}({\bf q}))^{2}].$ [src: Eq. 103].

- Verdict: 
- Comment: 

### 8. thcosmo-lss-perturbation-theory/references/formalism.md:50

Ivanov approximates the quasi-linear ΛCDM spectrum by a power law with n = −1.5 and k_NL ~ 0.3 h/Mpc at z = 0, and for k ~ 0.1 writes $\Delta^{2}_{\rm linear}<\Delta^{2}_{\rm one-loop}<\Delta^{2}_{\rm counterterm}\ll\Delta^{2}_{\rm two-loop}<\Delta^{2}_{\rm stochastic}\,.$ (arXiv:2212.08488) [src: Sect. 4.4, Eq. 83], as printed: the text that follows concludes that the stochastic term can be neglected at one loop, so the display is meant as an ordering by decreasing size, with the inequality signs printed the other way. He adds that the scaling-universe estimates are quite accurate for ΛCDM (Sect. 4.4).

- Verdict: 
- Comment: 

## Conventions (4 of 6)

### 9. thcosmo-lss-perturbation-theory/references/formalism.md:18

| Kernels | EdS kernels (arXiv:astro-ph/0112551) [src: Sect. 2.4.2]; other cosmologies in Sect. 2.4.4 | EdS approximation Ω_m/f² = 1 applied to ΛCDM (arXiv:2212.08488) [src: Sect. 3.2] |

- Verdict: 
- Comment: 

### 10. thcosmo-lss-perturbation-theory/references/formalism.md:10

The two main sources of this skill use different Fourier conventions, and a coefficient read in one cannot be moved to the other without its convention. The hub's atlas (`theoretical-cosmology/references/conventions.md`, sections "Fourier convention and power-spectrum normalisation" and "Perturbation-theory kernels") collects the choices of other works.

- Verdict: 
- Comment: 

### 11. thcosmo-lss-perturbation-theory/references/formalism.md:12

| Item | Bernardeau et al. 2002 | Ivanov 2022 |

- Verdict: 
- Comment: 

### 12. thcosmo-lss-perturbation-theory/references/formalism.md:17

| Velocity variable | velocity divergence θ (arXiv:astro-ph/0112551) [src: Eq. 37] | Θ = θ/f, defined below (arXiv:2212.08488) [src: Eq. 23] |

- Verdict: 
- Comment: 

## Model or result (4 of 73)

### 13. thcosmo-lss-perturbation-theory/references/results.md:17

Quadratic Lagrangian tidal bias of halos: a significant negative detection; cubic tidal biases broadly consistent with the Lagrangian local-in-matter-density ansatz, with indications of a positive Lagrangian coefficient of the time derivative of the tidal field (Lazeyras & Schmidt 2018, arXiv:1712.07531) [src: abstract].

- Verdict: 
- Comment: 

### 14. thcosmo-lss-perturbation-theory/references/results.md:44

| 2007 | Scale-dependent bias from local PNG, confirmed in N-body simulations | current; universality of $b_{\phi}$ disputed (`models.md`) | Dalal et al., arXiv:0710.4560 [src: abstract] |

- Verdict: 
- Comment: 

### 15. thcosmo-lss-perturbation-theory/references/results.md:13

The renormalised two-loop dark-matter power spectrum in the EFTofLSS needs eight counterterms, including the effect of generated vorticity (Anastasiou et al. 2025, arXiv:2509.05187) [src: abstract].

- Verdict: 
- Comment: 

### 16. thcosmo-lss-perturbation-theory/references/results.md:48

| 2025 | Fast evaluation of the renormalised two-loop matter power spectrum, eight counterterms | current | Anastasiou et al., arXiv:2509.05187 [src: abstract] |

- Verdict: 
- Comment: 

## Approximation (4 of 54)

### 17. thcosmo-lss-perturbation-theory/references/approximations.md:66

**Fails:** for realistic galaxy populations, through PNG assembly bias (de S. Nascimento & Dalal 2026, arXiv:2607.18229) [src: abstract].

- Verdict: 
- Comment: 

### 18. thcosmo-lss-perturbation-theory/references/approximations.md:78

**Fourier factors.** Bernardeau et al. put the $(2\pi)^{3}$ in the forward transform and none in front of the Dirac delta of the power spectrum (arXiv:astro-ph/0112551) [src: Eq. 36; Sect. 3.2.2]; Ivanov puts $\int d^{3}k/(2\pi)^{3}$ in the inverse and $(2\pi)^{3}\delta_{D}$ in front of the polyspectra (arXiv:2212.08488) [src: Sect. 3.1, footnote 1; Eq. 33]. A loop integral copied from one into the other changes by powers of 2π. <!-- num: not a value -->

- Verdict: 
- Comment: 

### 19. thcosmo-lss-perturbation-theory/references/approximations.md:39

| Halo IA bispectrum multipoles, tree level | $\lesssim 0.11$ h/Mpc | 0 | Bakx et al. 2025, arXiv:2507.06818 [src: abstract] |

- Verdict: 
- Comment: 

### 20. thcosmo-lss-perturbation-theory/references/approximations.md:14

**Fails:** at shell crossing, where the Lagrangian Jacobian vanishes and the density becomes singular (arXiv:astro-ph/0112551) [src: Sect. 2.5]. Ivanov calls the fluid "a wrong but useful model" and shows that its loop integrals are sensitive to UV modes, the UV part of $P_{13}$ scaling as $k^{2}P_{11}(k)$ times an integral of the linear spectrum up to the cut-off (arXiv:2212.08488) [src: Sect. 3 title; Eq. 72].

- Verdict: 
- Comment: 

## General remarks

1. 
2. 
3. 
4. 
5. 
