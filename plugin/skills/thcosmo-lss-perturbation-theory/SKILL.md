---
name: thcosmo-lss-perturbation-theory
description: Use when deriving, checking or reviewing perturbative large-scale-structure theory — SPT kernels and loops, LPT and Zel'dovich, EFTofLSS counterterms and stochastic terms, IR resummation and BAO damping, galaxy bias bases, Kaiser to EFT redshift-space models, TNS, LSS consistency relations, scale-dependent bias and b_phi, momentum and velocity statistics, intrinsic-alignment shape bias, one-point PDFs and large deviations, field-level perturbative forward models, two-loop calculations.
---

# Large-scale-structure perturbation theory — expert reference

Snapshot 2026-10-31. Every equation and number names its paper and
the place it was read; no equation or number is derived by an agent.
Conventions: Bernardeau et al. (arXiv:astro-ph/0112551) put the factor $(2\pi)^{3}$ in the forward Fourier transform [src: Eq. 36] and none in front of the Dirac delta of the power spectrum; Ivanov (arXiv:2212.08488) puts it in the inverse and in front of the polyspectra [src: Sect. 3.1, footnote 1; Eq. 33]; kernels in the EdS approximation; lengths in $h^{-1}$Mpc. <!-- num: not a value --> Re-read the cited paper before
an equation or a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Fourier and time conventions, SPT equations and kernels, EFT counterterms and power counting, LPT, IR resummation, bias operators, redshift-space mapping, consistency relations, PNG bias, velocity and momentum, IA operators, large deviations, field-level models | `references/formalism.md` |
| One card per scheme: SPT, LPT, Eulerian EFT, Lagrangian EFT, TSPT, TNS, Galileon bias basis, PNG bias, EFT of IA, LDT one-point statistics, LSS bootstrap; their status in survey analyses | `references/models.md` |
| Computed coefficients ($S_3$, UV coefficients), two-loop results, bias measurements in simulations, code comparisons, history of the state of the art | `references/results.md` |
| Range of validity ($k_{\rm max}$ table), EdS approximation, IR split, FoG, universality of $b_\phi$, convention traps, printing slips, numerical issues, referee checklist | `references/approximations.md` |
| Debates (two loops and σ8, prior-volume effects, EdS with neutrinos, $b_\phi$, equivalence-principle tests), unresolved calculations, stale claims | `references/open-questions.md` |
| How the one-loop matter spectrum follows from the $F_n$ recursion, why $P_{13}$ and $P_{22}$ are UV sensitive, and how the sound-speed and stochastic counterterms remove the cutoff dependence (cutoff, dimensional regularisation, FFTLog) | `deep/one-loop-eft-power-spectrum.md` |
| Which IR-resummation scheme to use (Lagrangian, equivalence-principle formula, TSPT, LPT with $k_{\rm IR}$, redshift space) and how their damping factors and residuals compare | `deep/ir-resummation.md` |
| How the one-loop redshift-space spectrum is built in the EFT: $Z_n$ kernels, contact-operator counterterms, fingers-of-god term, stochastic terms, IR resummation, multipoles | `deep/redshift-space-eft.md` |
| How bias operators are renormalised (δ² counterterms, Galileon non-renormalisation, renormalised bias parameters) and how coefficients convert between Galileon, Lagrangian, convective-trace and McDonald–Roy bases | `deep/bias-renormalisation-and-bases.md` |
| How the PNG scale-dependent bias is derived (peak shift, peak–background split, separate universe, EFT with ψ) and what fixes or breaks the universality of $b_\phi$ | `deep/png-scale-dependent-bias.md` |
| How velocity, momentum and pairwise-velocity spectra are computed in PT and EFT (mass weighting, vector modes, vorticity, velocity bias, IR resummation) and where PT fails for them | `deep/velocity-momentum-statistics.md` |
| Bibliography with versions read; subtopics and where they come from | `references/sources.tsv`, `references/subtopics.tsv` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- The second-order EdS density kernel has a dipole coefficient one half: $F_{2}({\bf q}_{1},{\bf q}_{2})=\frac{5}{7}+\frac{1}{2}\frac{{\bf q}_{1}\cdot{\bf q}_{2}}{q_{1}q_{2}}(\frac{q_{1}}{q_{2}}+\frac{q_{2}}{q_{1}})+\frac{2}{7}\frac{({\bf q}_{1}\cdot{\bf q}_{2})^{2}}{q_{1}^{2}q_{2}^{2}}$ (arXiv:astro-ph/0112551) [src: Eq. 45]; Ivanov's review (v1, Eq. 28) drops the one half.
- The UV part of $P_{13}$ has the shape $k^{2}P_{11}(k)$ and is absorbed by the sound-speed counterterm; its coefficient is $-61/(630\pi^{2})$ (arXiv:2212.08488) [src: Eqs. 72–73]. <!-- num: not a value -->
- The stochastic term of matter starts at $k^{4}$, while that of a biased tracer is constant as k goes to zero, because tracers do not conserve mass and momentum (Cabass et al. 2022, arXiv:2203.08232) [src: Sect. 3.6]. <!-- num: not a value -->
- Bulk flows damp the BAO through the long-wavelength displacement, an equivalence-principle effect calculable to all orders in the long modes; the one-loop IR-resummed spectrum is $\tilde{P}(k)=P_{\rm lin}^{nw}(k)+P_{\rm 1-loop}^{nw}(k)\\[8.0pt] +e^{-\Sigma^{2}_{\epsilon k}k^{2}}(1+\Sigma^{2}_{\epsilon k}k^{2})P^{w}_{\rm lin}(k)+e^{-\Sigma^{2}_{\epsilon k}k^{2}}P^{w}_{\rm 1-loop}(k),$ (Baldauf et al. 2015, arXiv:1504.04366) [src: Eq. 21].
- Eulerian, Lagrangian and time-sliced EFTs agree within their overlapping domains to the order computed (arXiv:2203.08232) [src: Sect. 3.5].
- A consistent bias expansion needs the tidal operator at second order and the velocity potential at third; Galileon operators are not renormalised at leading order in derivatives (Assassi et al. 2014, arXiv:1402.5916) [src: abstract].
- The local-in-time bias expansion is exact only in the EdS approximation, quoted as $\mathcal{O}(0.1\div 1)\%$ accurate (arXiv:2203.08232) [src: Sect. 3.6, footnote 5]; exact time dependence moves the one-loop redshift-space quadrupole by a factor of about 1.007 at z = 0.57 (Donath & Senatore 2020, arXiv:2005.04805) [src: abstract].
- Redshift space adds counterterms because density and velocity multiply at the same point: two new ones for one-loop matter (Senatore & Zaldarriaga 2014, arXiv:1409.1225) [src: abstract].
- Local PNG gives $\Delta b(k)=2(b-1)f_{\rm NL}\delta_{c}\frac{3\Omega_{m}}{2a\,g(a)r_{H}^{2}k^{2}}$ (Dalal et al. 2008, arXiv:0710.4560) [src: Eq. 9]; $b_{\phi}$ is fully degenerate with $f_{\rm NL}$ and universality fails for realistic galaxies (de S. Nascimento & Dalal 2026, arXiv:2607.18229) [src: abstract].
- The consistency relations of LSS follow from Galilean invariance (Peloso & Pietroni 2013, arXiv:1302.0223) [src: abstract]; they fail with equivalence-principle violation and in DHOST/GLPV dark energy, not in Galileon models (Creminelli et al. 2013, arXiv:1312.6074) [src: abstract; arXiv:2203.08232, Sect. 4.5].
- Two loops: 49 coefficients for the redshift-space galaxy spectrum, $k_{\rm max}$ from 0.20 to 0.34 h/Mpc for an LRG-like sample at z = 0.5, but no significant gain on σ8 (Philcox 2026, arXiv:2610.13867) [src: abstract]; a two-loop analysis of galaxy–galaxy and galaxy–matter spectra reports about 40% gain on σ8 over one loop with conservative priors (arXiv:2606.30713) [src: abstract].
- EFT full-shape fits suffer prior-volume projection, multi-σ in $H_0$, $w_0$, $w_a$ for DESI DR1 with baseline priors (Bonici et al. 2026, arXiv:2607.02498) [src: abstract].
- The one-loop EFT of intrinsic alignments (8 parameters) fits halo shapes to k_max = 0.30 h/Mpc at z = 0, NLA and TATT only to 0.05 h/Mpc (Bakx et al. 2023, arXiv:2303.15565) [src: abstract].
- Large-deviation one-point PDFs from spherical collapse, with a log-density, are accurate to a few percent (Uhlemann et al. 2016, arXiv:1512.05793) [src: abstract]; they assume no shell crossing (arXiv:1511.08641) [src: abstract].

## Checks a referee makes
<!-- key: checks-a-referee-makes -->

- Fourier convention stated, and loop integrals consistent with it.
- Kernels quoted from a source without the $F_2$ dipole slip; EdS approximation stated and its size estimated at the lowest redshift used.
- All counterterms and stochastic terms of the order computed, in real and redshift space.
- IR resummation for any statistic with BAO, adapted for velocity statistics (Chen et al. 2025, arXiv:2508.00066).
- Complete bias basis; each tidal bias given with its operator; co-evolution relations flagged as assumptions.
- $k_{\rm max}$ justified on simulations of the tracer, statistic and redshift used.
- Priors on EFT parameters and projection effects discussed.
- For PNG, the treatment of $b_\phi$ stated; for consistency-relation tests, the equivalence-principle assumption stated.
- Forecasts labelled as forecasts. Details: `references/approximations.md`, last section.

## Errors that recur
<!-- key: errors-that-recur -->

- Copying $F_2$ or $G_2$ from Ivanov's Eq. 28 (dipole coefficient one instead of one half), or $P_{13}$ from his Eq. 32 (printed with the second-order field in place of the third); quote Bernardeau et al. (arXiv:astro-ph/0112551) [src: Eqs. 45–46, 165–166]. <!-- num: not a value -->
- Moving a loop coefficient between papers with different Fourier conventions without the factors of $2\pi$. <!-- num: not a value -->
- Quoting a tidal bias without its operator: the co-evolution value is $-2/7$ of $b_1-1$ for $b_s$ in velocileptors and $-4/7$ for $b_{s^2}$ in FOLPS (Maus et al. 2024, arXiv:2404.07272) [src: Sect. 3.5, Eqs. 15–16]. <!-- num: not a value -->
- Using the Eulerian bias b where the Lagrangian $b_L=b-1$ enters the PNG term (arXiv:0710.4560) [src: Eqs. 8–9]. <!-- num: not a value -->
- Using a phenomenological FoG damping and quoting percent-level growth: Taruya et al. estimate 1–2% systematic errors on distances and about 5% on the growth rate from such models (arXiv:1006.0699) [src: abstract] (forecast).
- Assuming the universality relation b_φ = 2δ_c(b_1 − 1) for any galaxy sample (arXiv:2607.18229, arXiv:2009.06622) [src: abstracts]. <!-- num: not a value -->
- Taking a $k_{\rm max}$ validated for one tracer or one loop order to another; using NLA or TATT in the quasi-linear regime.
- Treating EdS kernels as exact in interacting dark sectors, where one-loop deviations can significantly exceed the percent level (Wolney et al. 2026, arXiv:2603.12431) [src: abstract].
- Citing the 2022 state-of-the-art table (redshift-space tracers at one loop) as current: superseded in 2026 (`references/results.md`, history).

## Related skills
<!-- key: related-skills -->

- `thcosmo-nonlinear-structure`: halo model, spherical and ellipsoidal collapse, excursion sets, halo bias from the mass function, N-body theory; the large-deviation machinery here uses spherical collapse but the mass-function theory lives there.
- `thcosmo-relativistic-cosmology`: wide-angle and relativistic corrections to redshift-space distortions beyond the plane-parallel mapping used here.
- `thcosmo-cosmological-perturbations`: linear relativistic perturbations and gauges, the starting point of the Newtonian-motion-gauge method cited here.
- `thcosmo-primordial-correlators`: shapes and templates of primordial non-Gaussianity and inflationary consistency relations; late-time consistency relations and scale-dependent bias stay here.
- `thcosmo-modified-gravity`: DHOST, GLPV and Horndeski theories whose LSS consistency-relation violation is summarised here.
- `thcosmo-neutrinos-light-relics`: linear massive-neutrino perturbations; their non-linear perturbative treatment stays here.
- `thcosmo-dark-matter-models`: mixed and ultra-light dark matter as candidates; their EFTofLSS treatment stays here.
- cosmoskill `cosmo-galaxy-clustering` (full-shape fits, measured parameters), `cosmo-peculiar-velocities` (velocity and momentum data, field-level velocity likelihoods), `cosmo-inflation-primordial` (measured $f_{\rm NL}$), `cosmo-weak-lensing` (measured IA amplitudes), `cosmo-statistics-inference` (prior choices, samplers), `cosmo-theory-foundations` (conventions adopted by survey analyses).

<!-- thcosmoskill:block:start — generated by tools/sync_blocks.py, do not edit by hand -->
## Levels and layers
<!-- key: levels-and-layers -->

Answer at the lowest level that answers the question, then stop.

| Level | Read | Holds |
|---|---|---|
| L1 | this file only | the headline equations and values, the state of the domain, the checks a referee makes, the errors that recur |
| L2 | one file of `references/` | what this file does not hold: the formalism and its conventions, the model landscape, other results and their history, the validity of each approximation, open questions |
| L3 | one dossier of `deep/` | how a result is obtained and how to choose a method |
| L4 | the cited paper itself | what L1 to L3 quote; required before an equation or a number goes into a manuscript, a proposal or a referee report, and when two statements of the skills disagree |

Sizes, in thousands of tokens: L1 5k; approximations 4k; formalism 13k; models 6k; open 3k; results 3k; deep/bias-renormalisation-and-bases 10k; deep/ir-resummation 8k; deep/one-loop-eft-power-spectrum 10k; deep/png-scale-dependent-bias 7k; deep/redshift-space-eft 9k; deep/velocity-momentum-statistics 7k.

- L2: when the file map names several files, search them for the term
  before reading, and read only the passage.
- L4 starts from the L2 entry: its citation and flag say where to look. Read
  the paper with
  `python3 "${CLAUDE_SKILL_DIR}"/../*theoretical-cosmology/scripts/fetch_paper.py <arXiv id>`
  (`--abstract`, `--outline`, `--section`, `--grep`). `${CLAUDE_SKILL_DIR}` is
  the folder of this file; if it reaches you unexpanded, write that folder's
  path in its place. If the script cannot run, or reports that arXiv cannot
  be reached, do not run it again: read `https://arxiv.org/abs/<id>` or
  `https://arxiv.org/html/<id>` with a web tool if you have one. If the paper
  cannot be read, say that L4 was required and not done; never give its
  content from memory.
- Quote a number or an equation only with its paper and the place it was
  read (an equation with its equation number), or, for a code fact, its
  `[doc]` page and read date, as the skill gives them; the skill holds no
  number and no equation of its own making. State the conventions the
  equation assumes (metric signature, units, Fourier and normalisation
  conventions) when the skill gives them. A formula may be applied, or a
  derivation carried out, for the asker; label the result as derived.

Local layers: if a directory `.thcosmoskill/` exists in the working directory,
in one of its parents, or in the home directory, or if `THCOSMOSKILL_HOME` is
set, run
`python3 "${CLAUDE_SKILL_DIR}"/../*theoretical-cosmology/scripts/layers.py thcosmo-lss-perturbation-theory`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. An
override replaces its base section for this researcher: use it, and quote
the base value beside it, both labelled. A suppressed section is left out
and named as suppressed; use it only when the question asks for that
section's own content, and then say that the layer hides it. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[thcosmoskill L<level> · <base, personal, project, or several joined by +> · thcosmo-lss-perturbation-theory/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- thcosmoskill:block:end -->
