---
name: thcosmo-modified-gravity
description: Use when deriving, checking or reviewing theories that modify gravity in cosmology — Horndeski, beyond Horndeski, DHOST, Galileons, f(R), Brans–Dicke, k-mouflage, DGP, massive gravity, bigravity, generalised Proca, Einstein–aether, f(T), f(Q), non-local gravity, screening, ghosts, gradient instability, strong coupling, positivity bounds, EFT of dark energy, α_i, μ–Σ, PPF, quasi-static approximation, GW170817 and the speed of tensors, graviton decay, modified-gravity N-body.
---

# Modified gravity — expert reference

Snapshot 2026-11-02. Every equation and number names its paper and
the place it was read; no equation or number is derived by an agent.
Conventions: signature (−+++) in all main sources; Kobayashi (arXiv:1901.07183, Eq. 87) puts Φ in $g_{00}$ while Planck 2015 XIV and the Euclid review (arXiv:2512.09748, Eq. 28) put Ψ there; X carries −1/2 in Kobayashi and Euclid; the sign of the $G_{3}$ term differs between them (table in `references/formalism.md`). Re-read the cited paper before
an equation or a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Conventions; Horndeski, GLPV and DHOST Lagrangians; quasi-static $G_{\rm eff}$ and slip; f(R) and Hu–Sawicki; dRGT and bigravity; generalised Proca and aether; f(Q) cosmology; non-local models; screening equations; EFT of DE, α basis, stability conditions, μ–Σ, PPF; tensor propagation | `references/formalism.md` |
| One card per model: Horndeski, GLPV/DHOST, f(R), Galileons, k-mouflage, Brans–Dicke, dRGT, bigravity, generalised Proca, DGP, f(T), f(Q), non-local; consistency objections, replies and status | `references/models.md` |
| No-go theorems (chameleon, Ostrogradski), positivity, stability conditions, GW170817 consequences, bounds on α and μ–Σ, history of key results | `references/results.md` |
| Quasi-static approximation and its limits, EFT validity and cutoff, screening in simulations, convention traps, referee checklist | `references/approximations.md` |
| Phantom crossing in Horndeski, health of f(Q), sub- or superluminal tensors, evidence for non-minimal coupling, Vainshtein beyond spherical symmetry, Euclid forecasts, stale claims | `references/open-questions.md` |
| How the α_i follow from the Horndeski $G_i$, the stability conditions, and how the α conventions of Bellini–Sawicki, EFTCAMB and hi_class relate | `deep/eft-dark-energy-alpha-basis.md` |
| How μ and Σ are derived in the quasi-static limit from the α_i, and where the quasi-static approximation fails | `deep/quasi-static-mu-sigma.md` |
| How chameleon, symmetron, k-mouflage and Vainshtein screening work, and which theory uses which | `deep/screening-mechanisms.md` |
| Which scalar–tensor, vector–tensor and bimetric theories survive GW170817 and graviton decay, under which assumptions (EFT cutoff, tuning), and the status of the cutoff objection | `deep/speed-of-tensors-constraints.md` |
| Bibliography with versions read; subtopics and where they come from | `references/sources.tsv`, `references/subtopics.tsv` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- Horndeski Lagrangian with four free functions $G_{2..5}(\phi,X)$ (arXiv:1901.07183) [src: Eq. 8]; it equals the generalised Galileons (arXiv:1105.5723) [src: abstract].
- In Horndeski, $c_{\rm GW}=1$ on any background requires $G_{4X}=0,\quad G_{5}=0.$ (arXiv:1901.07183) [src: Eq. 124]; the bound used is $-3\times 10^{-15}<c_{\rm GW}-1<7\times 10^{-16}.$ [src: Eq. 122]. All cubic DHOST are excluded [src: Sect. 4.2].
- Graviton decay forces $\alpha_{\rm H}=0$ and, with luminal tensors, excludes quartic and quintic GLPV (arXiv:1809.03484) [src: abstract]; the LIGO band may lie near the cutoff of these theories (arXiv:1806.09417) [src: abstract].
- Linear structure in Horndeski is fixed by $H(t)$, the matter density today and four $\alpha_i(t)$ (arXiv:1404.3713) [src: Sect. 3.1]; tensors obey $c_{\text{T}}^{2}=1+\alpha_{\textrm{T}}>0\,.$ [src: Sect. 3.3, unnumbered display after Eq. 15] and scalars need a positive $D\equiv\alpha_{\textrm{K}}+\frac{3}{2}\alpha_{\textrm{B}}^{2}\,,$ and a positive $c_{\rm s}^{2}$ [src: Eq. 14].
- The stability prior shapes the $w_0w_a$ posterior in EFT of DE fits (arXiv:2606.31977) [src: abstract].
- Chameleon-like scalars cannot self-accelerate; their Compton wavelength today is at most Mpc (arXiv:1208.4612) [src: abstract].
- Hu–Sawicki f(R): $\Sigma(a)=\frac{1}{1+f_{R}(a)}\,.$ and scale-dependent μ (arXiv:2512.09748) [src: Eqs. 50–52]; galaxy morphology rules out astrophysically relevant Hu–Sawicki f(R) (arXiv:2009.08743) [src: abstract].
- Vainshtein radius $r_{\rm V}\equiv\frac{1}{\Lambda}\left(\frac{gM}{M_{\rm Pl}}\right)^{1/3}\ .$ (arXiv:1407.0059) [src: Eq. 6.40]; beyond Horndeski the screening breaks inside matter (arXiv:1411.4130) and multipoles stay unscreened for generic EFT parameters (arXiv:2607.09098) [src: abstracts].
- dRGT has no flat FLRW solution with a Minkowski reference metric (arXiv:1401.4173) [src: Sect. 12.2.1]; Higuchi bound $m^{2}>2H^{2}$ on de Sitter [src: Sect. 8.3.6].
- The self-accelerating DGP branch has a ghost (arXiv:hep-th/0604086) [src: abstract]; the cubic Galileon is in 7.8σ tension with ISW data (arXiv:1707.02263) [src: abstract].
- f(Q) cosmologies: two flat branches infinitely strongly coupled, the third with a ghost (arXiv:2311.04201) [src: abstract].
- Quasi-static approximation holds at best inside the dark-energy sound horizon; never for ISW (arXiv:1503.06831) [src: abstract].
- DESI-era reconstructions: a 2.8σ hint of non-minimal coupling (arXiv:2605.12415) [src: abstract]; EFT of DE fits find the dynamical-dark-energy significance "greatly reduced" (arXiv:2509.13804) [src: abstract].

## Checks a referee makes
<!-- key: checks-a-referee-makes -->

- Conventions stated: potential in $g_{00}$, X, sign of $G_{3}$, c kept or not.
- $c_{\rm GW}=1$ and $\alpha_{\rm H}=0$ imposed, or the cutoff argument made. <!-- num: not a value -->
- Stability (ghost, gradient, strong coupling) checked on the background used, new branches included; positivity priors with their UV assumption.
- Quasi-static use justified against the sound speed; screening prescription (unscreened or super-screened) stated for non-linear scales.
- f(R) and chameleon parameters compared with astrophysical, not only cosmological, bounds. Details: `references/approximations.md`, referee checklist.

## Errors that recur
<!-- key: errors-that-recur -->

- Swapping Φ and Ψ, and so inverting the slip η, between Kobayashi (arXiv:1901.07183, Eq. 87, Eq. 101) and Planck 2015 XIV or Euclid (arXiv:2512.09748, Eq. 28; slip in Sect. 4.1.1).
- Comparing $G_{3}$ coefficients across papers that write $-G_{3}\Box\phi$ (arXiv:1901.07183, Eq. 8) and $+G_{3}\Box\phi$ (arXiv:2512.09748, Eq. 34).
- Using Kobayashi's quasi-static $G_{\rm eff}$ (arXiv:1901.07183, Eq. 100) for f(R) or chameleons: it drops the mass term [src: Sect. 3.4.2].
- Presenting quartic or quintic Horndeski, GLPV or the self-accelerating DGP branch as viable dark-energy models (arXiv:1710.05901; arXiv:1809.03484; arXiv:hep-th/0604086) [src: abstracts].
- Calling a chameleon or f(R) model "self-accelerating modified gravity" (arXiv:1208.4612) [src: abstract].
- Treating a background fit to DESI as a test of a modified-gravity class (arXiv:2609.26517) [src: abstract].
- Fitting f(Q) or f(T) cosmologies without addressing strong coupling and ghosts (arXiv:2311.04201; arXiv:2405.14184) [src: abstracts].
- Reading the scalar gradient term of Bellini & Sawicki's Eq. 13 as unsquared: it is printed without the square (arXiv:1404.3713) [src: Eq. 13].

## Related skills
<!-- key: related-skills -->

- `thcosmo-dark-energy`: quintessence, k-essence, phantom fields, interacting and early dark energy; the EFT of dark energy stays here.
- `thcosmo-cosmological-gravitational-waves`: GW propagation templates, standard-siren distances and modified friction as signals; the speed of tensors as a constraint on theories stays here.
- `thcosmo-nonlinear-structure`: halo model and collapse in general; screening in N-body is here. `thcosmo-theory-codes` (if built): hi_class, EFTCAMB, MGCAMB, ECOSMOG and other codes.
- `thcosmo-cosmological-perturbations`: gauges and gauge-invariant potentials; `thcosmo-fundamental-theory`: UV embeddings and swampland; `thcosmo-tensions-model-building`: modified gravity as a tension response.
- cosmoskill `cosmo-dark-energy-modified-gravity` (measured $w_0w_a$, μ–Σ, $E_G$), `cosmo-multimessenger` (standard sirens, GW170817 data), `cosmo-simulations-mocks` (simulation suites and emulators).

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

Sizes, in thousands of tokens: L1 4k; approximations 3k; formalism 15k; models 9k; open 3k; results 4k; deep/eft-dark-energy-alpha-basis 10k; deep/quasi-static-mu-sigma 9k; deep/screening-mechanisms 9k; deep/speed-of-tensors-constraints 16k.

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
`python3 "${CLAUDE_SKILL_DIR}"/../*theoretical-cosmology/scripts/layers.py thcosmo-modified-gravity`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. An
override replaces its base section for this researcher: use it, and quote
the base value beside it, both labelled. A suppressed section is left out
and named as suppressed; use it only when the question asks for that
section's own content, and then say that the layer hides it. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[thcosmoskill L<level> · <base, personal, project, or several joined by +> · thcosmo-modified-gravity/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- thcosmoskill:block:end -->
