---
name: thcosmo-dark-energy
description: Use when deriving, checking or reviewing dark-energy theory within general relativity — cosmological-constant problem and vacuum energy, quintessence (thawing, freezing, tracker, exponential, axion), k-essence, Chaplygin gas, phantom fields, crossing w = −1, quintom, interacting dark energy and its instabilities, early dark energy formalism, holographic, running-vacuum, emergent and sign-switching models, dark-energy sound speed and PPF, model building after DESI.
---

# Dark energy — expert reference

Snapshot 2026-11-03. Every equation and number names its paper and
the place it was read; no equation or number is derived by an agent.
Conventions: Copeland, Sami & Tsujikawa use the full Planck mass m_pl = 1.22 × 10¹⁹ GeV (arXiv:hep-th/0603057) [src: Sect. IV.2, text after Eq. 69], a mostly-plus signature and X ≡ −(1/2)(∇φ)² [src: Sect. V.2, text before Eq. 115]; the sign of the dark-sector coupling Q differs between reviews (arXiv:2606.21826, Eqs. 3–4; arXiv:1603.08299, Eqs. 12–13). <!-- num: not a value --> Re-read the cited paper before
an equation or a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Conventions; vacuum energy and the Λ problem; quintessence equations and the exponential fixed points; thawing, freezing, tracking; k-essence and its stability; Chaplygin gas; phantom fields, the no-go theorem for crossing w = −1 and quintom; interacting dark energy and its instability; early dark energy background and perturbations; sound speed and PPF | `references/formalism.md` |
| One card per model: exponential, tracker, thawing (PNGB/axion), axion–dilaton quintessence; k-essence; Chaplygin gas; phantom field; two-field quintom; coupled fluids and interacting vacuum; coupled quintessence; axion-like and new early dark energy; holographic, running vacuum, emergent, sign-switching Λ | `references/models.md` |
| Size of the Λ problem; generic quintessence results and the limits of quintessence; phantom-divide no-go results; what DESI asks of a theory; history of key results | `references/results.md` |
| Fluid treatment of interacting sectors; smooth dark energy and PPF; slow roll for dark energy; w(a) parameterisations and priors; convention traps; numerical issues; referee checklist | `references/approximations.md` |
| Debates (size of the Λ problem; thawing preference; is the DESI preference physical; which interaction kernel), unresolved calculations, next data, stale claims | `references/open-questions.md` |
| Bibliography with versions read; subtopics and where they come from | `references/sources.tsv`, `references/subtopics.tsv` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- Cut-off estimate: $\rho_{\rm vac}\approx\frac{k_{\rm max}^{4}}{16\pi^{2}}\,.$ with $k_{\rm max}=m_{\rm pl}$ gives $\rho_{\rm vac}\approx 10^{74}\,{\rm GeV}^{4}\,,$ against $\rho_\Lambda\approx 10^{-47}$ GeV⁴ (arXiv:hep-th/0603057) [src: Eqs. 67, 69, 70]; the renormalised Standard-Model estimate gives "something like 54 orders of magnitude" (arXiv:1205.3365) [src: Sect. X.2].
- Dynamical dark energy does not solve the Λ problem: the vacuum energy is assumed zero "due to some as yet unknown mechanism" (arXiv:hep-th/0603057) [src: Sect. IV.2].
- A canonical field has $-1\leq w_{\phi}\leq 1$ (arXiv:hep-th/0603057) [src: Sect. V.1, text after Eq. 106]; for an exponential potential the field-dominated attractor has $w_{\phi}=-1+\lambda^{2}/3$ and accelerates for $\lambda^{2}<2$ [src: Sect. VI.2.1, inline, text after Eq. 196].
- Thawing fields start at w ≈ −1 with w' > 0, while a freezing field "slows down and creeps to a halt as it comes to dominate the universe" (Caldwell & Linder, arXiv:astro-ph/0505494) [src: text after Fig. 1]; the results indicate "a desired measurement resolution of order σ(w') ≈ (1+w)" [src: abstract].
- k-essence stability needs $\xi_{1}\,\equiv\,p_{,X}+2Xp_{,XX}\,\geq\,0,~~\xi_{2}\,\equiv\,p_{,X}\,\geq\,0,$ (arXiv:hep-th/0603057) [src: Eq. 145], with $c_{s}^{2}\equiv\frac{p_{,X}}{\rho_{,X}}=\frac{\xi_{2}}{\xi_{1}}\,,$ [src: Eq. 147]; a phantom p = −X − V is quantum-mechanically unstable even with c_s² > 0 [src: Sect. V.5, text after Eq. 147].
- No-go, as Ren et al. state it: for "basic single perfect fluid models or single-field models" $L(\phi,\partial\phi)$ with a "single degree of freedom without higher derivatives", minimally coupled to GR in FRW, "the equation of state parameter w cannot cross the cosmological constant boundary -1" (arXiv:2606.01360) [src: text before Eq. 2]; Vikman finds such transitions "generally" physically implausible for a dominant dark energy, and without that assumption the result "still holds for a certain class of dark energy Lagrangians, in particular, for Lagrangians quadratic in field's first derivatives" (arXiv:astro-ph/0407107) [src: abstract]; the adiabatic sound speed $c_{a}^{2}=\frac{\delta p}{\delta\rho}\Big|_{\rm{adiabatic}}=\frac{\bar{p}^{\prime}}{\bar{\rho}^{\prime}}=w-\frac{w^{\prime}}{3\mathcal{H}(1+w)}.$ diverges there (arXiv:2606.01360) [src: Eq. 4].
- Ghosts: "assuming only that ghosts interact at least gravitationally", the Lorentz-violating cutoff satisfies Λ < 3 MeV "for consistency with the cosmic gamma ray background", and "theories of ghosts with a Lorentz-conserving cutoff are completely excluded" (arXiv:hep-ph/0311312) [src: abstract].
- Effective dark-energy equation of state under an interaction: $w_{\rm de}^{\rm eff}=w-\frac{aQ}{3\mathcal{H}\rho_{\rm de}},$ (arXiv:2606.21826) [src: Eq. 9]; an interaction "may even mimic a time-varying or phantom-crossing EoS" [src: Sect. III.1, text after Eq. 10].
- Constant-w coupled fluids with a coupling proportional to ρ_c [src: Sect. III, Eq. 38]: "the curvature perturbation blows up on super-Hubble scales", "regardless of how weak the coupling is" (arXiv:0804.0232) [src: abstract]. For Q ∝ ρ_de, Wang et al. find the system "stable for any constant ω_d < −1", while for ω_d > −1 it "could become unstable" when "the interaction parameter is ξ₂ ∼ 1", assuming C_e² = 1 (arXiv:1603.08299) [src: Sect. 4.2].
- Axion-like early dark energy $V(\theta)=m^{2}f^{2}[1-\cos(\theta)]^{n},$ (arXiv:2302.09032) [src: Eq. 6] is a "toy potential" [src: Sect. III.1]; it "may be generated by higher-order instanton corrections that require fine-tuning to cancel the leading contributions, or through the interaction of an axion and a dilaton" [src: Sect. III.1].
- Post-DESI shape: in the Li et al. review "the preferred parameter regions systematically lie in the quadrant" $w_0>-1$, $w_a<0$, "corresponding to a quintom-B type evolution"; across six parameterisations the preference "does not disappear when the CPL assumption is relaxed", while "the precise statistical significance of the DDE signal remains sensitive to the adopted dataset combination, especially the choice of SN compilation" (arXiv:2606.21826) [src: Sect. II.2]; one critical review finds that "the dynamical dark energy driven by the DES-SN5Y sample is in fact driven by the inclusion of low-z SNe Ia in DES-SN5Y" (arXiv:2512.10585) [src: Sect. V].
- Dinda & Maartens find that thawing quintessence with nonzero curvature "can fit the recent data as well as $w_0, w_a$ in a flat background", that "the data do not enforce phantom crossing", and call the crossing "an artifact of a parametrization that is not based on a physical model" (arXiv:2504.15190) [src: abstract].
- Thawing preference: "only if we use priors which are heavily informed by the data itself" per arXiv:2411.13637 (v4) [src: abstract]; "not sensitive to our choice of prior, but it is contingent on the inclusion of supernovae" per arXiv:2512.20832 [src: abstract].

## Checks a referee makes
<!-- key: checks-a-referee-makes -->

- Planck mass, the definition of X, the sign of Q and of β stated.
- A phantom phase or crossing: model property or parameterisation artefact; ghost and cutoff; how the no-go is evaded.
- Interacting dark energy: perturbations and large-scale stability, not the background alone; negative densities in sign-switching fits.
- Dark-energy sound speed stated; PPF through w = −1.
- Prior dependence and SN-compilation dependence of any model preference.
- Early dark energy: priors on $f_{\rm EDE}$, $z_c$; radiative stability. Details: `references/approximations.md`, last section.

## Errors that recur
<!-- key: errors-that-recur -->

- Quoting "122 orders of magnitude" (arXiv:1205.3365) [src: abstract] or "120 orders of magnitude" (arXiv:2606.20778) [src: abstract] as the Standard-Model prediction for the vacuum energy: Martin finds "the properly renormalized value of the zero-point energy density today (for a free theory)" "far from being 122 orders of magnitude larger than the critical energy density" [src: abstract], and Kaya & Lahey say the 120 rests on "an estimate that does not account for regularization and renormalization" [src: abstract].
- Reading a CPL crossing of w = −1 as evidence for a phantom field (arXiv:2504.15190; arXiv:2511.23463) [src: abstracts].
- Building a crossing from one minimally coupled field, or running a crossing w(a) through a single-fluid Boltzmann closure (arXiv:2606.01360, text after Eq. 10; arXiv:0808.3125, abstract).
- Comparing interaction couplings across papers with opposite signs of Q (arXiv:2606.21826, Eqs. 3–4; arXiv:1603.08299, Eqs. 12–13).
- Fitting constant-w coupled fluids at the background level only (arXiv:0804.0232) [src: abstract].
- Claiming that late dynamical dark energy raises $H_0$: per Capozziello et al., ω(z) > −1 "drives H0 towards lower values rather than higher ones", a behaviour they call "generic" (arXiv:2512.10585) [src: Sect. V].
- Using w = −1 as the phantom boundary when the dark-energy density changes sign (arXiv:2602.21169) [src: abstract].
- Correcting printed slips silently: Eq. 179 and Sect. IV.2 of arXiv:hep-th/0603057, Eq. 24 of arXiv:2302.09032 are copied as printed (`references/approximations.md`, convention traps).

## Related skills
<!-- key: related-skills -->

- `thcosmo-modified-gravity`: theories that modify gravity (Horndeski, DHOST, f(R), Proca, massive gravity), the EFT of dark energy and α, μ–Σ frameworks, screening, the speed of tensors, and phantom crossing in scalar–tensor theories. Here only minimally coupled fields, fluids and dark-sector interactions in GR.
- `thcosmo-tensions-model-building` (planned): early dark energy and other models as responses to the H0, S8 and DESI tensions, and their status. Here only the formalism of early dark energy.
- `thcosmo-dark-matter-models`: dark-matter candidates; dark matter–dark energy interactions belong here.
- `thcosmo-fundamental-theory`: de Sitter in string theory, swampland conjectures, string quintessence (arXiv:1806.08362; arXiv:2603.25797).
- `thcosmo-cosmological-perturbations`: gauge-invariant perturbation theory and Boltzmann hierarchies.
- cosmoskill `cosmo-dark-energy-modified-gravity` (measured $w_0w_a$, μ–Σ), `cosmo-supernovae` (SN compilations and calibration), `cosmo-tensions-anomalies` (H0 and DESI–CMB tensions).

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

Sizes, in thousands of tokens: L1 5k; approximations 3k; formalism 9k; models 8k; open 3k; results 4k; deep/dark-energy-perturbations-ppf 7k; deep/interacting-de-instabilities 8k; deep/thawing-quintessence-w0wa 9k.

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
`python3 "${CLAUDE_SKILL_DIR}"/../*theoretical-cosmology/scripts/layers.py thcosmo-dark-energy`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. An
override replaces its base section for this researcher: use it, and quote
the base value beside it, both labelled. A suppressed section is left out
and named as suppressed; use it only when the question asks for that
section's own content, and then say that the layer hides it. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[thcosmoskill L<level> · <base, personal, project, or several joined by +> · thcosmo-dark-energy/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- thcosmoskill:block:end -->
