---
name: thcosmo-dark-matter-models
description: Use when deriving, checking or reviewing dark-matter model building — relic abundance, freeze-out, thermal cross-section, coannihilation, Sommerfeld and bound states, unitarity bound, freeze-in and FIMPs, non-standard expansion histories, axion misalignment and strings, ultralight or fuzzy dark matter, sterile neutrinos, warm dark matter transfer functions, SIDM, atomic and dissipative dark matter, SIMPs, asymmetric dark matter, gravitational production, PBHs as dark matter.
---

# Dark-matter models — expert reference

Snapshot 2026-11-03. Every equation and number names its paper and <!-- eq: notation -->
the place it was read; no equation or number is derived by an agent.
Conventions: natural units; $m_{\rm pl}$ is the reduced Planck mass and R the scale factor in Safdi's lectures (arXiv:2303.02169), $x\equiv m_{\chi}/T$ for freeze-out, $Y\equiv n_{\chi}/s$ for freeze-in (arXiv:1706.07442); see `references/formalism.md`, Conventions. Re-read the cited paper before
an equation or a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Conventions; freeze-out Boltzmann equation and estimates; freeze-in equations and yields; non-standard histories; misalignment and axion strings; ultralight-field linear theory; warm cut-off fits; dark matter–baryon and dark-radiation interactions; gravitational production | `references/formalism.md` |
| One card per candidate: thermal WIMP, FIMP, QCD axion, ultralight dark matter, thermal warm relic, sterile neutrino, SIDM, atomic and dissipative, SIMP and hidden-sector relics, asymmetric, interacting, PBHs (status) | `references/models.md` |
| Phase-space, quantum-pressure and Planck-scale mass bounds; unitarity bound; thermal cross-section benchmarks; bounds on non-cold dark matter; history of key results; not verified | `references/results.md` |
| Instantaneous freeze-out and its exceptions; standard history; freeze-in and misalignment assumptions; transfer-function fits; convention traps; referee checklist | `references/approximations.md` |
| Post-inflationary axion mass; the unidentified X-ray line and sterile neutrinos; SIDM core collapse; fuzzy-dark-matter heating bounds; PBH window and fine-tuning; unresolved calculations; stale claims | `references/open-questions.md` |
| How the thermal relic abundance is computed when the textbook calculation fails (coannihilation, forbidden channels and resonances, coscattering, Sommerfeld enhancement and bound states, early kinetic decoupling), which code implements which treatment, and the precision each reaches | `deep/relic-abundance-beyond-freeze-out.md` |
| How the QCD-axion abundance is computed from misalignment with a lattice temperature-dependent mass, pre- against post-inflationary cases (isocurvature, strings and domain walls), and why the post-inflationary mass prediction is disputed | `deep/axion-relic-abundance.md` |
| How a thermal-relic warm-dark-matter mass bound is translated to other non-cold models (sterile neutrinos, freeze-in, decay products), which matching criterion each translation uses, and when one mass cannot carry the bound | `deep/noncold-dm-mass-mappings.md` |
| Bibliography with versions read; subtopics and where they come from | `references/sources.tsv`, `references/subtopics.tsv` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- Freeze-out: $\begin{split}{dn_{\chi}\over dt}+3Hn_{\chi}=-\langle\sigma v\rangle(n_{\chi}^{2}-n_{\rm eq}^{2})\,,\end{split}$ (arXiv:2303.02169) [src: Eq. 16], freezing out at $x_{\rm fo}\sim 10$ [src: Sect. 4.1].
- The thermal cross-section is 2.2*10^-26 cm^3s^-1 above 10 GeV, reaching 5.2*10^-26 cm^3s^-1 near 0.3 GeV, not the "canonical" 3*10^-26 (arXiv:1204.3622) [src: abstract]; in a decoupled sector it can differ by "orders of magnitude" (arXiv:2007.03696) [src: abstract].
- Unitarity caps point-like thermal relics at 140 TeV (self-conjugate) and below 100 TeV (non-self-conjugate) with bound states and Sommerfeld enhancement (arXiv:1904.11503) [src: abstract]; other freeze-out processes evade it (arXiv:2207.01635) [src: abstract].
- Freeze-in is IR-dominated and reheating-independent for renormalisable couplings (arXiv:0911.1120) [src: abstract], with $y\simeq 10^{-12}\left(\frac{\Omega_{\rm\chi}h^{2}}{0.12}\right)^{1/2}\left(\frac{g_{*}}{100}\right)^{3/4}\left(\frac{m_{\sigma}}{m_{\rm\chi}}\right)^{1/2}.$ (arXiv:1706.07442) [src: Eq. 10]; non-renormalisable portals make it ultraviolet (arXiv:1410.6157) [src: abstract].
- Relic-density limits assume a standard history; in a pMSSM example, an early quintessence (kination) phase raises a higgsino relic density by "two orders of magnitude" without disrupting BBN (arXiv:2104.11488) [src: Sect. 8.1].
- QCD axion with pre-inflationary breaking: $\begin{split}\Omega_{a}h^{2}\sim 0.1\theta_{i}^{2}\left({f_{a}\over 3\times 10^{11}\,\,{\rm GeV}}\right)^{1+{1\over n+2}}\sim 0.1\theta_{i}^{2}\left({f_{a}\over 3\times 10^{11}\,\,{\rm GeV}}\right)^{1.1}\,.\end{split}$, a mass "around 10 to 20 μeV" for θ_i of order one (arXiv:2303.02169) [src: Eq. 72 and text after].
- Post-inflationary axion mass is disputed: (40,180) μeV (arXiv:2108.05368) [src: abstract], 95–450 μeV (arXiv:2401.17253) [src: abstract], 17.46(84) μeV "in this minimal model" (arXiv:2609.20801) [src: abstract].
- Fuzzy cut-off: $T_{\rm F}(k)\approx{\cos x^{3}\over 1+x^{8}}$ (arXiv:astro-ph/0003365) [src: Eq. 8], with $x=1.61\,m_{22}^{1/18}k/k_{J{\rm eq}}$ (arXiv:astro-ph/0003365) [src: inline, text after Eq. 8]; the canonical $10^{-22}$–$10^{-21}$ eV range is disfavoured by Lyman-α (arXiv:2007.12705) [src: abstract].
- Warm cut-off: $T(k)=[1+(\alpha k)^{2\nu}]^{-5/\nu}$ with ν = 1.12 (arXiv:astro-ph/0501562) [src: Eq. 6 and text after]; thermal relic above 5.7 keV at 95% C.L. from high-z Lyman-α (arXiv:2309.04533) [src: abstract].
- Sterile neutrinos' "conventional production through active-sterile mixing is tightly constrained by X-ray searches and structure-formation observations" (arXiv:2609.04650) [src: abstract]; Shi–Fuller production with $L \gtrsim 0.5$ reopens $m_s \gtrsim 10$ keV (arXiv:2507.18752) [src: abstract].
- SIDM needs $\sigma/m\sim 1\;{\rm cm^{2}/g}\approx 2\times 10^{-24}\;{\rm cm^{2}/GeV}$ to affect halos and leaves large-scale structure as in ΛCDM (arXiv:1705.02358) [src: Eq. 2; Sect. I.3].
- Gravitational production is a background for every non-thermal model, diluted by low reheating (arXiv:2306.13061) [src: abstract] and sensitive to the reheating equation of state (arXiv:2602.10215) [src: abstract].
- PBH windows are quoted with different edges, $10^{17}$–$10^{22}$ g (arXiv:2606.12775) [src: abstract] and $10^{17}$–$10^{21}$ g (arXiv:2510.00246) [src: abstract]: quote the paper.

## Checks a referee makes
<!-- key: checks-a-referee-makes -->

- Boltzmann equation solved with $g_{*}(T)$ and $g_{*s}(T)$; coannihilation, resonances, Sommerfeld and bound states included where relevant.
- Self-conjugate or not stated; expansion history and reheating temperature stated.
- Gravitational-production background estimated for non-thermal models.
- Non-thermal momentum distributions propagated to a transfer function, not mapped by mass alone.
- Axions: pre- or post-inflationary breaking, isocurvature or strings and domain-wall number.
- Status with dataset, confidence level and date. Details: `references/approximations.md`, last section.

## Errors that recur
<!-- key: errors-that-recur -->

- Quoting 3×10⁻²⁶ cm³ s⁻¹ as mass-independent (arXiv:1204.3622) [src: abstract, inline], or 340 TeV as the unitarity bound, which "assumes $Ω_{DM} h^2 = 1$" (arXiv:1904.11503) [src: abstract, inline].
- Copying the fuzzy-dark-matter fit from Eberhardt & Ferreira (arXiv:2507.00705, Eq. 78), printed with $T^{2}$ and $m_{22}^{-1/18}$, instead of Hu et al. (arXiv:astro-ph/0003365, Eq. 8).
- Comparing thermal-relic and sterile-neutrino keV masses without the map of arXiv:astro-ph/0501562, Eq. 5.
- Using Safdi's order-of-magnitude Eqs. 19 or 72 (arXiv:2303.02169) as precise relic abundances.
- Applying relic-density limits outside a standard radiation-dominated history (arXiv:2104.11488, Sect. 8.1).
- Treating fuzzy dark matter at $10^{-22}$ eV or the 3.5 keV sterile neutrino as settled candidates (arXiv:2007.12705) [src: abstract]; (arXiv:1812.06976) [src: abstract], with the reply arXiv:2004.06601 [src: abstract].

## Related skills
<!-- key: related-skills -->

- `thcosmo-thermal-history`: equilibrium thermodynamics, $g_{*}$, the Boltzmann equation as a method; here freeze-out as a production mechanism.
- `thcosmo-nonlinear-structure`: wave dark-matter dynamics (solitons, granules), halo cores, SIDM halo evolution; here only the linear cut-offs.
- `thcosmo-pbh-defects`: PBH formation, abundance, evaporation and axion-string network theory; here PBHs only as a dark-matter candidate.
- `thcosmo-dark-energy`: dark matter–dark energy interactions. `thcosmo-neutrinos-light-relics`: dark radiation and $N_{\rm eff}$.
- `thcosmo-inflation`: the inflationary background that sets isocurvature and gravitational production.
- cosmoskill `cosmo-neutrinos-dark-matter` (measured limits: direct, indirect, X-ray, Lyman-α, PBH), `cosmo-lyman-alpha` (forest systematics), `cosmo-early-universe-exotica`.

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

Sizes, in thousands of tokens: L1 4k; approximations 3k; formalism 8k; models 7k; open 3k; results 3k; deep/axion-relic-abundance 9k; deep/noncold-dm-mass-mappings 10k; deep/relic-abundance-beyond-freeze-out 10k.

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
`python3 "${CLAUDE_SKILL_DIR}"/../*theoretical-cosmology/scripts/layers.py thcosmo-dark-matter-models`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. An
override replaces its base section for this researcher: use it, and quote
the base value beside it, both labelled. A suppressed section is left out
and named as suppressed; use it only when the question asks for that
section's own content, and then say that the layer hides it. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[thcosmoskill L<level> · <base, personal, project, or several joined by +> · thcosmo-dark-matter-models/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- thcosmoskill:block:end -->
