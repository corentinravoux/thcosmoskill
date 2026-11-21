---
name: thcosmo-cosmological-perturbations
description: Use when deriving, checking or reviewing relativistic cosmological perturbation theory — FLRW and Friedmann equations, curvature and Omega_k, distances and horizons, SVT decomposition, gauge transformations, Bardeen potentials, synchronous, Newtonian, flat and comoving gauges, zeta and R signs and conservation, separate universe and delta-N, isocurvature modes and initial conditions, Boltzmann hierarchy and line-of-sight codes, second-order gauge issues, Bianchi backgrounds.
---

# Cosmological perturbations — expert reference

Snapshot 2026-11-20. Every equation and number names its paper and
the place it was read; no equation or number is derived by an agent.
Conventions: signature (−+++) in the main sources; conformal time is η in Malik & Wands (arXiv:0809.4944) and τ in Laine & Procacci (arXiv:2607.06983) and Ma & Bertschinger (arXiv:astro-ph/9506072), while τ is cosmic time in Malik & Wands' synchronous-gauge paragraph; potential names and the sign of ζ differ between papers (hub atlas `conventions.md` and `references/formalism.md`, "Conventions"). Re-read the cited paper before
an equation or a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Conventions of the main sources; FLRW background and Friedmann equations with curvature; distances and horizons; SVT decomposition; gauge transformations, gauges and gauge-invariant variables; first-order Einstein equations, vectors and tensors; ζ and ℛ, their conservation, linear and non-linear; separate universe and δN; adiabatic and entropy perturbations; Boltzmann hierarchy, truncation, line-of-sight integration, codes; second-order gauge transformations and mode mixing | `references/formalism.md` |
| Cards for constant-w backgrounds, curved FLRW, Bianchi backgrounds in outline, and the adiabatic, CDM, curvaton-type and neutrino isocurvature modes with their Planck and recent status | `references/models.md` |
| Conservation theorems with their assumptions, mode counting and gauge results, accuracy of linear codes, history of key results | `references/results.md` |
| Super-Hubble and gradient expansion, separate universe, hierarchy truncation, tight coupling and fluid approximations, Newtonian limit of simulations; convention traps; gauge artefacts; referee checklist | `references/approximations.md` |
| Large-scale white noise at second order, limits of the separate universe, gauge of second-order observables, unresolved items, stale claims | `references/open-questions.md` |
| Bibliography with versions read; subtopics and where they come from | `references/sources.tsv`, `references/subtopics.tsv` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- Friedmann equation with curvature in conformal time: $\mathcal{H}^{2}+\kappa\overset{{\mbox{\tiny\rm{(\ref{eq_ee-b-00})}}}}{=}\;\frac{8\pi G}{3}\bar{e}a^{2}\,,$ (arXiv:2607.06983) [src: Sect. 1.3, Eq. 1.39]; Laine & Procacci define $\Omega_K$ with $\lvert\kappa\rvert$, Hogg by a sum rule (arXiv:astro-ph/9905116) [src: Sect. 2, Eq. 7].
- First-order gauge transformation of the curvature potential: $\widetilde{\psi}_{1}=\psi_{1}-{\cal H}\alpha_{1}\,,$ (arXiv:0809.4944) [src: Sect. 6.4.1, Eq. 6.38]; the first-order tensor is gauge invariant [src: Eq. 6.43].
- Bardeen potentials: $\Psi\equiv\psi_{1}-{\cal H}\left(B_{1}-E_{1}^{\prime}\right)\,.$ (arXiv:0809.4944) [src: Sect. 7.1.1, Eq. 7.2], with $\Psi-\Phi=8\pi Ga^{2}\Pi\,,$ [src: Sect. 8.2.1, Eq. 8.29], so Ψ = Φ only without anisotropic stress.
- Synchronous gauge leaves residual gauge freedom; "it is not possible to define gauge-invariant quantities in general using this gauge condition" (arXiv:0809.4944) [src: Sect. 7.3; the authors cite their Ref. 114].
- ζ evolves as $\zeta^{\prime}=-{\cal H}\frac{\delta P_{\rm nad}}{\rho+P}-{\Sigma_{V}}\,,$ (arXiv:0809.4944) [src: Sect. 8.2.2, Eq. 8.35]: constant "for adiabatic perturbations (δP_nad = 0) on super-Hubble scales (k/𝓗 ≪ 1), so long as Ψ remains finite" [src: Sect. 8.2.2, text after Eq. 8.37].
- In a gradient expansion, "assuming that the universe is smooth over a sufficiently large comoving scale" (arXiv:astro-ph/0411220) [src: abstract], to first order in ε with the anisotropic stress negligible at that order [src: Sect. III.1], non-linear conservation holds if P is a unique function of ρ, with $-\zeta(x^{i})\equiv\psi(t,x^{i})+\frac{1}{3}\int_{\rho(t)}^{\rho(t,x^{i})}\frac{d\rho}{\rho+P}\,.$ (arXiv:astro-ph/0411220) [src: Sect. IV, Eq. 37].
- The sign of ψ in the spatial metric differs between Lyth, Malik & Sasaki and Malik & Wands, who both call ψ on uniform-density slices −ζ: compare signs of ζ, ℛ or $f_{\rm NL}$ only after reading each paper's metric (`references/approximations.md`, "Convention traps"). No paper read states the relation between the two ζ.
- δN in Malik & Wands' sign: $\zeta=\delta N\,,$ (arXiv:0809.4944) [src: Sect. 11, Eq. 11.1; the authors cite their Refs. 156, 157, 146, 98]; from the initial field values on a flat slice, $\zeta=\sum_{I}N_{I}\delta\varphi_{I{\rm{flat}}}\,,$ [src: Sect. 11, Eq. 11.3], which rests on the expansion being a function of the initial local field values, stated "in the slow-roll approximation" and, "more generally we expect this to hold whenever we can neglect the decaying mode for the field perturbations on super-Hubble scales" [src: Sect. 11, text before Eq. 11.3].
- It is "well known" that gradient terms make the separate universe fail, "particularly at the transition from slow-roll to ultra-slow-roll phase", and Raveendran finds a breakdown for Π at the transition back (arXiv:2506.23571) [src: abstract]; with non-minimal coupling it holds above lower bounds on the wavelength (arXiv:2609.34788) [src: abstract].
- Weinberg: in Newtonian gauge there is always an adiabatic mode with ℛ non-zero and constant at large wavelength in all eras, "under only a mild technical assumption" (arXiv:astro-ph/0302326) [src: abstract].
- In linearized theory with photons, baryons, neutrinos and CDM, the most general regular primordial perturbation has a growing adiabatic and four isocurvature modes (CDM, baryon, neutrino density, neutrino velocity), and all its quadratic correlators of observables are determined by a 5 × 5 matrix (arXiv:astro-ph/9904231) [src: abstract]. <!-- num: not a value -->
- Planck 2018: $\beta_{\mathrm{iso}}<0.00095$ for fully correlated CDI at 95 % CL, TT,TE,EE+lowE+lensing (arXiv:1807.06211) [src: Sect. 9.4.2, Eq. 92].
- Boltzmann hierarchy truncation by setting $F_{l}=0$ is "simple but inaccurate"; Ma & Bertschinger's Eq. 51 extrapolates instead (arXiv:astro-ph/9506072) [src: Sect. 5.3].
- Line of sight: $\Delta^{(S)}_{(T,P)l}(k,\tau=\tau_{0})=\int_{0}^{\tau_{0}}S^{(S)}_{T,P}(k,\tau)j_{l}[k(\tau_{0}-\tau)]d\tau,$ (arXiv:astro-ph/9603033) [src: Sect. 2.2, Eq. 13], in longitudinal gauge and conformal time [src: Sect. 2.1] and "for a spatially flat universe", to which they "restrict the analysis" [src: Sect. 2, first paragraph]; CLASS's cl_3permille.pre gives 0.3 % on the $C_l$ up to l = 3000 (arXiv:1104.2933) [src: Fig. 10 caption].
- At second order the perturbation types mix: in the Einstein–de Sitter model, primordial density perturbations source gravitational waves and primordial gravitational waves give second-order density fluctuations (arXiv:astro-ph/9707278) [src: abstract].

## Checks a referee makes
<!-- key: checks-a-referee-makes -->

- Line element written; names of the potentials, the time variable and the sign of ζ and ℛ stated against it.
- Gauge of every variable stated; synchronous-gauge residual freedom fixed.
- Conservation of ζ and use of δN only with their conditions (super-Hubble, non-adiabatic pressure and shear negligible, no transition breaking the separate universe).
- Initial conditions named (adiabatic or which isocurvature mode); consistent initial conditions beyond general relativity (arXiv:2506.17411) [src: abstract].
- Boltzmann-code truncation, approximation switches and precision settings; agreement with a second code with its range.
- Second-order work: generator, expansion convention and gauge of observables stated. Details: `references/approximations.md`, last section.

## Errors that recur
<!-- key: errors-that-recur -->

- Comparing ζ or $f_{\rm NL}$ between Malik & Wands (arXiv:0809.4944, Eqs. 2.12, 7.61) and Lyth, Malik & Sasaki (arXiv:astro-ph/0411220, Eqs. 5, 37) without the sign of ψ in each metric.
- Using Φ = (3/5)ζ from one paper with Φ = −(3/5)ζ from another (arXiv:0809.4944, Sect. 11, footnote 5, "on large scales in the matter era"; hub atlas).
- Setting Ψ = Φ while an anisotropic stress is present (arXiv:0809.4944, Eq. 8.29), for example the neutrino shear $\sigma_\nu$, non-zero already in the adiabatic initial conditions of Ma & Bertschinger (arXiv:astro-ph/9506072, Eq. 96).
- Reading super-horizon growth of δ in synchronous gauge as physical (arXiv:astro-ph/9506072) [src: Sect. 8], or the growth of the flat-gauge shear as instability (arXiv:0809.4944, Sect. 7.2.1).
- Reading τ as conformal time in Malik & Wands' synchronous-gauge paragraph, where it is cosmic time (arXiv:0809.4944, Sect. 7.3).
- Calling the Newtonian gauge "the Poisson gauge" when vectors or tensors are present (arXiv:0809.4944, Sect. 7.1.1; arXiv:2607.06983, Sect. 4.2).
- Subtracting angular-diameter distances between two redshifts, or using Hogg's Eq. 19 for negative $\Omega_k$ (arXiv:astro-ph/9905116) [src: Sect. 6].
- Copying Seljak & Zaldarriaga's Eq. 11 with its doubled $e^{-\kappa}$ as printed in the v1 rendering (arXiv:astro-ph/9603033) [src: Sect. 2.2].
- Taking large-scale white noise in the primordial spectrum as established: Ireland, a co-author of the original papers, argues that it does not reach $R_2$ (arXiv:2608.09897) [src: abstract].

## Related skills
<!-- key: related-skills -->

- `thcosmo-inflation`: ζ during inflation, multi-field δN, turns and isocurvature transfer, stochastic δN and the tails; here only the general formalism.
- `thcosmo-primordial-correlators`: mode quantisation, Mukhanov–Sasaki variable, in-in formalism, EFT of inflation, loop corrections to ζ and their debate.
- `thcosmo-lss-perturbation-theory`: Newtonian SPT, LPT and EFTofLSS, and the Newtonian-motion-gauge method; here the relativistic linear theory it starts from.
- `thcosmo-neutrinos-light-relics`: the massive-neutrino hierarchy and free streaming; `thcosmo-modified-gravity`: quasi-static perturbations beyond general relativity.
- `thcosmo-cosmological-gravitational-waves`: the gauge question of scalar-induced waves and tensor transfer functions.
- `thcosmo-cmb-physics` and `thcosmo-thermal-history` (not built): CMB source physics, recombination and BBN; `thcosmo-relativistic-cosmology` (not built): inhomogeneous exact solutions and backreaction.
- cosmoskill `cosmo-theory-foundations` (conventions adopted by survey analyses), `cosmo-inflation-primordial` and `cosmo-cmb` (measured isocurvature and curvature), `cosmo-software-ecosystem` (Boltzmann-code versions).

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

Sizes, in thousands of tokens: L1 5k; approximations 4k; formalism 17k; models 4k; open 2k; results 3k; deep/einstein-boltzmann-system 10k; deep/gauge-transformations-and-invariants 10k; deep/zeta-conservation 9k.

Not swept for newer papers since the snapshot at the top of this file.

- L2: when the file map names several files, search them for the term
  before reading, and read only the passage.
- L4 starts from the L2 entry: its citation and flag say where to look. Read
  the paper with
  `python3 "${CLAUDE_SKILL_DIR}"/../*theoretical-cosmology/scripts/fetch_paper.py <arXiv id>`
  (`--abstract`, `--outline`, `--section`, `--grep`). `${CLAUDE_SKILL_DIR}` is
  the folder of this file; if it reaches you unexpanded, write that folder's
  path in its place. If the script reports that the paper has no HTML
  rendering, and a tool named `get_paper_latex` or `read_paper` is among
  your tools (loaded or deferred), read the paper with that tool. Otherwise,
  if the script cannot run, or reports that arXiv cannot be reached, do not
  run it again: read `https://arxiv.org/abs/<id>` or
  `https://arxiv.org/html/<id>` with a web tool if you have one. If the paper
  cannot be read, say that L4 was required and not done; never give its
  content from memory.
- Papers newer than the sweep date above, papers that cite a given paper,
  and papers not on arXiv are outward tasks. Only when the question asks for
  them, follow `references/adapters.md` of the hub `theoretical-cosmology`.
  Never name a tool that is not among your tools.
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
`python3 "${CLAUDE_SKILL_DIR}"/../*theoretical-cosmology/scripts/layers.py thcosmo-cosmological-perturbations`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. An
override replaces its base section for this researcher: use it, and quote
the base value beside it, both labelled. A suppressed section is left out
and named as suppressed; use it only when the question asks for that
section's own content, and then say that the layer hides it. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[thcosmoskill L<level> · <base, personal, project, or several joined by +> · thcosmo-cosmological-perturbations/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- thcosmoskill:block:end -->
