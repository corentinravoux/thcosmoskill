---
name: thcosmo-pbh-defects
description: Use when deriving, checking or reviewing theory of primordial black holes or topological defects — collapse threshold, compaction function, critical collapse, Press-Schechter or peak theory, non-Gaussian PBH abundance, beta and f_PBH, clustering, Hawking evaporation, memory burden, PBHs from phase transitions or matter domination; cosmic strings, Nambu-Goto, Abelian-Higgs, scaling, loops, superstrings, metastable strings, domain walls, monopoles, global strings.
---

# Primordial black holes and topological defects — expert reference

Snapshot 2026-11-13. Every equation and number names its paper and
the place it was read; no equation or number is derived by an agent.
Conventions: each source keeps its own signature, units and Planck mass (reduced in Saikawa, non-reduced in Copeland & Kibble); table in `references/formalism.md` and the hub's `references/conventions.md`. Re-read the cited paper before
an equation or a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Conventions of the main sources; Misner–Sharp setting, compaction function, $q$, analytic thresholds, apparent horizon and critical scaling; Press–Schechter and peak-theory set-up, local non-Gaussianity, Poisson clustering; $\beta$, $f$, mass at formation; Hawking temperature, lifetime, $M_*$, memory burden; other formation channels; vacuum manifold and homotopy; Nambu–Goto, scaling, loops, intercommutation; domain walls, scaling, ZKO bound, bias; metastable strings, monopoles, global strings | `references/formalism.md` |
| One card per PBH channel (radiation-era collapse, matter era, delayed decay, supercooled remnants, string loops, walls and bubbles) and per defect class (Nambu–Goto, Abelian-Higgs, metastable, superstrings, global strings, walls, monopoles); their status | `references/models.md` |
| Threshold values and their assumptions; non-Gaussian and statistical systematics; clustering and spin; $\beta$ limits; evaporation numbers; memory-burden bounds; PT-PBH results; string scaling, reconnection, field theory against Nambu–Goto; wall area parameter and annihilation; monopole simulations; history of key results | `references/results.md` |
| Spherical symmetry, gradient expansion, critical scaling, PS against peaks, Gaussianity, monochromatic mass function, semiclassical evaporation, Nambu–Goto, exact wall scaling; notation clashes and printed slips; referee checklist | `references/approximations.md` |
| Threshold universality, statistics, single-field loop debate, PBHs from slow transitions, memory burden, field-theory loops, global-string scaling; unresolved calculations; stale claims | `references/open-questions.md` |
| Bibliography with versions read; subtopics and where they come from | `references/sources.tsv`, `references/subtopics.tsv` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- Threshold criterion: following its Ref. [56], the review takes "a good criterion" to be the peak of the compaction function [src: Sect. II.3, inline, text after Eq. II.17], at leading order of the gradient expansion $\mathcal{C}(r)\simeq f(w)K(r)r^{2}=f(w)\mspace{-1.5mu}\left(1-\big[1+\tilde{r}\zeta^{\prime}(\tilde{r})\big]^{2}\right)$ (arXiv:2211.05767) [src: Eq. II.19], with $f(w)\coloneqq\frac{3(1+w)}{(5+3\mspace{1.5mu}w)}$ [src: Eq. II.17].
- Profile dependence enters through $q =-\frac{\mathcal{C}^{\prime\prime}(r_{\mathrm{m}})r^{2}_{\mathrm{m}}}{4\mathcal{C}(r_{\mathrm{m}})}$ (arXiv:2211.05767) [src: Eq. II.25a]; as shown in its Ref. [78] "employing detailed numerical simulations", profiles with the same $q$ share $\delta_{\mathrm c}$ "upon deviation of $\mathcal{O}(2\,\text{--}\,3)\%$" in radiation domination [src: Sect. II.4, inline, text after Eq. II.25b].
- For radiation, Escrivà, Germani & Sheth "argued, supported by the numerical simulations", that the averaged-compaction limit "is $\delta_c = 0.40$" (arXiv:1907.13311) [src: abstract, inline]; HYK give $\tilde\delta_{c}\simeq 0.4135$ "For a radiation fluid", $\tilde\delta_c$ being "the amplitude measure used in numerical simulations" (arXiv:1309.4201) [src: abstract, inline]; Carr's $\delta_{\mathrm{c},\mspace{1.5mu}\rm Carr}=w$ (arXiv:2211.05767) [src: Eq. II.31] was obtained "using a Jeans-length approximation" [src: Sect. II.6, first paragraph].
- Near threshold $M=\mathcal{K}M_{H}(t_{H})\big(\delta_{\mathrm{m}}-\delta_{\mathrm{c}}\big)^{\mspace{-2mu}\gamma}$, valid for "$\delta_{\mathrm{m}}-\delta_{\mathrm{c}}\lesssim 10^{-2}$" (arXiv:2211.05767) [src: Eq. II.30; Sect. II.5, text before Eq. II.30]; for the spherical collapse of radiation fluid "A critical exponent $\beta\simeq 0.36$ is found for supercritical ($\eta>\eta_c$) models" (arXiv:gr-qc/9402041) [src: abstract, inline].
- Statistics are non-Gaussian even for Gaussian $\zeta$: "for both narrow and broad power spectra the gaussian case from threshold statistics is reproduced by increasing the amplitude of the power spectrum by a factor ${\cal O}(2÷3)$" (arXiv:1904.00970) [src: abstract]; perturbative non-Gaussianity "is intrinsically flawed when considering broad spectra" (arXiv:2211.01728) [src: abstract].
- Constraints on $\mathcal P_\zeta$ from PS and peak theory "remain largely similar for the monochromatic case" but "differ in the case of a broad primordial power spectrum" (arXiv:2603.23025) [src: abstract]; for PBHs the equality of the two contributions that justifies the PS factor 2 for haloes "no longer holds" (arXiv:2509.25871) [src: abstract].
- $\beta(M)\approx 7.06\times 10^{-18}\,\gamma^{-1/2}\,\left(\frac{h}{0.67}\right)^{2}\,\left(\frac{g_{*\mathrm{i}}}{106.75}\right)^{1/4}\,\Omega_{\mathrm{PBH}}(M)\,\left(\frac{M}{10^{15}\,\mathrm{g}}\right)^{1/2}$ (arXiv:2002.12778) [src: Eq. 6], for radiation-era formation with adiabatic expansion afterwards [src: Sect. I.3].
- Semiclassical lifetime $\tau\approx 407\,\left(\frac{f(M)}{15.35}\right)^{-1}\,M_{10}^{3}\,\mathrm{s}$ (arXiv:2002.12778) [src: Eq. 14]; $M_*=5.00\times 10^{14}$ g from MacGibbon's calculations as quoted there [src: Sect. I.4.1, last paragraph]; from "a prototype model", memory burden "Applied to black holes" predicts "a drastic deviation from Hawking evaporation, at the latest after losing half of the mass" (arXiv:2006.00011) [src: abstract].
- Initial clustering of PBHs formed from the collapse of large Gaussian density fluctuations: "we do not expect clustering on very small scales beyond what is expected from a random, Poisson distribution" (arXiv:1805.05912) [src: abstract]; local non-Gaussianity can "substantially modify" constraints (arXiv:2609.11306) [src: abstract].
- Defects follow from the vacuum manifold $\mathcal{M}=G/H,$ (arXiv:0911.1345) [src: Eq. 8]: walls for $\pi_0$, strings for $\pi_1$, monopoles for $\pi_2$ non-trivial [src: Sect. 2, text after Eq. 8]; deficit angle "$\delta=8\pi G\mu$" [src: Sect. 10.1, inline, paragraph beginning "The deficit angle"]. <!-- num: not a value -->
- String networks scale with $\gamma=\xi/t$ "typically of order 0.3 and 0.55" in radiation and matter (arXiv:0911.1345) [src: Sect. 4, inline, second paragraph]; network loops in Abelian-Higgs simulations decay fast, and "one can estimate that $f_\text{NG}<0.1$ at $95$% confidence level" (arXiv:2103.16248) [src: abstract, inline].
- Metastable strings decay at $\Gamma_{d}=\frac{\mu}{2\pi}\exp\left(-\pi\kappa\right)\qquad\text{with}\qquad\kappa=\frac{m_{M}^{2}}{\mu}$ (arXiv:2307.04691) [src: Eq. 1]; stable GUT-scale strings are "firmly excluded" by PTA results [src: Sect. 1, first paragraph].
- Walls scale as $\rho_{\rm wall}(t)=\mathcal{A}\frac{\sigma}{t},$ (arXiv:1703.02576) [src: Eq. 2.17] with $\mathcal{A}\simeq 0.8\pm 0.1,$ [src: Eq. 2.18] for $Z_2$ walls in the simulations of its Ref. [46] [src: Sect. 2.2, text after Eq. 2.18], or "$\xi_{max} \approx 1.2$" with IR modes maximally suppressed, proposed as universal "Assuming that physically the memory of initial conditions is erased" (arXiv:2509.25367) [src: abstract, inline]; walls with a tension above the bound $\sigma^{1/3}\lesssim\mathcal{O}(\mathrm{MeV}).$ (arXiv:1703.02576) [src: Eq. 2.22] "must not exist in the universe at the present time" [src: Sect. 2.2, text after Eq. 2.22].

## Checks a referee makes
<!-- key: checks-a-referee-makes -->

- Threshold variable, profile family, $q$ and $w$ stated; averaged-compaction formulae used only inside their validated range of $w$ (`references/formalism.md`, analytical threshold formulae).
- Nonlinear $\delta$–$\zeta$ relation and non-perturbative non-Gaussianity included; statistical formalism and window function stated.
- Critical scaling only near threshold; monochromatic or extended mass function; thermal-history assumptions behind $\beta\leftrightarrow f$.
- Semiclassical or memory-burdened evaporation, with the onset model.
- Nambu–Goto or field-theory strings, loop model, $f_{\rm NG}$, $P$ for superstrings, $\sqrt\kappa$ for metastable strings; wall area parameter, bias mechanism and $C_{\rm ann}$. Details: `references/approximations.md`, last section.

## Errors that recur
<!-- key: errors-that-recur -->

- Quoting a threshold without its variable or profile, or mixing the compaction peak with $\mu_{\mathrm c}$ of $\zeta$ (for one monochromatic profile $\delta_{\mathrm{c}}\approx 0.588$ against $\mu_{\mathrm{c}}\approx 0.628$, arXiv:2211.05767) [src: Sect. II.7.2, inline, Example B.1].
- Thresholding $\mathcal R_c$ or $\zeta$ directly (arXiv:1405.7023; arXiv:1805.03946) [src: abstract].
- Applying the critical-scaling law or the PS factor 2 outside their ranges (arXiv:2211.05767) [src: Sect. III.1, text after Eq. III.6]; (arXiv:2509.25871) [src: abstract].
- Using $M=\gamma M_{\rm H}$ for matter-era or critical-collapse PBHs, or normalising to the particle horizon after inflation (arXiv:2002.12778) [src: Sect. I.3, text after Eq. 4].
- Confusing Carr et al.'s two $f(M)$ (dark-matter fraction, emitted species) and the several $\gamma$ of the domain (`references/approximations.md`).
- Treating all PBHs below $M_*$ as evaporated without saying semiclassical evaporation is assumed (arXiv:2211.05767) [src: Sect. V.2].
- Using Nambu–Goto bounds on $G\mu$ for Abelian-Higgs strings (arXiv:2103.16248) [src: abstract]; quoting stable GUT-scale strings as a PTA explanation (arXiv:2307.04691) [src: Sect. 1].
- Copying printed slips: Eqs. III.6 (last row) and III.7 of arXiv:2211.05767 v5, Eq. 4 of arXiv:2002.12778 v2 (see `references/approximations.md`). <!-- num: not a value -->

## Related skills
<!-- key: related-skills -->

- `thcosmo-cosmological-gravitational-waves`: scalar-induced backgrounds (`deep/scalar-induced-kernels.md`), cosmic-string spectra with the VOS model, loop densities and emission per loop (`deep/cosmic-string-spectra.md`), domain-wall spectra; here only formation and network dynamics.
- `thcosmo-dark-matter-models`: PBHs as dark matter and their observational status; axion strings and walls as sources of axion dark matter.
- `thcosmo-inflation`: models producing a peak in $\mathcal P_\zeta$ and the stochastic tail of $\zeta$ (`deep/stochastic-delta-n-tails.md`); `thcosmo-primordial-correlators`: loop corrections from PBH-scale modes (`deep/loop-corrections.md`).
- `thcosmo-baryogenesis-phase-transitions`: the first-order transition itself (nucleation, $\beta/H$, supercooling, walls) behind PT-PBHs and strings from $B-L$ breaking.
- cosmoskill: `cosmo-early-universe-exotica` (measured PBH, string and wall limits, PTA and LVK backgrounds), `cosmo-neutrinos-dark-matter` (PBH dark-matter limits), `cosmo-cmb` (CMB limits on $G\mu$).

<!-- thcosmoskill:block:start — generated by tools/sync_blocks.py, do not edit by hand -->
## Levels and layers
<!-- key: levels-and-layers -->

Answer at the lowest level that answers the question, then stop.

| Level | Read | Holds |
|---|---|---|
| L1 | this file only | the headline equations and values, the state of the domain, the checks a referee makes, the errors that recur |
| L2 | one file of `references/` | what this file does not hold: the formalism and its conventions, the model landscape, other results and their history, the validity of each approximation, open questions |
| L3 | one dossier of `deep/` | none in this skill yet: say so and answer at L2 |
| L4 | the cited paper itself | what L1 to L3 quote; required before an equation or a number goes into a manuscript, a proposal or a referee report, and when two statements of the skills disagree |

Sizes, in thousands of tokens: L1 5k; approximations 5k; formalism 14k; models 5k; open 3k; results 10k.

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
`python3 "${CLAUDE_SKILL_DIR}"/../*theoretical-cosmology/scripts/layers.py thcosmo-pbh-defects`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. An
override replaces its base section for this researcher: use it, and quote
the base value beside it, both labelled. A suppressed section is left out
and named as suppressed; use it only when the question asks for that
section's own content, and then say that the layer hides it. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[thcosmoskill L<level> · <base, personal, project, or several joined by +> · thcosmo-pbh-defects/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- thcosmoskill:block:end -->
