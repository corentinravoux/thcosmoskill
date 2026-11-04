---
name: thcosmo-primordial-correlators
description: Use when deriving, checking or reviewing inflationary correlators — in-in and Schwinger–Keldysh calculations, Maldacena bispectrum, EFT of inflation and sound speed, f_NL shapes and templates (local, equilateral, orthogonal, folded), squeezed-limit and soft theorems, cosmological collider, cosmological bootstrap and optical theorem, resonant and sharp features, inflationary loops and PBH loop debate, decoherence, QFT in de Sitter, stochastic inflation and SdSET.
---

# Primordial correlators — expert reference

Snapshot 2026-11-02. Every equation and number names its paper and
the place it was read; no equation or number is derived by an agent.
Conventions: Chen's review (arXiv:1002.1416) uses signature $(-,+,+,+)$ and sets the reduced Planck mass to one [src: Sect. 4, text after Eq. 4.1], and comoving gauge $h_{ij}=a^{2}e^{2\zeta}\delta_{ij}~$ (arXiv:1002.1416) [src: Eq. 4.7]; Planck templates use $\Phi\equiv(3/5)\zeta$ (arXiv:1905.05697) [src: Sect. 2.1, inline, text after Eq. 2]; power-spectrum normalisations differ between sources (`references/formalism.md`, Conventions). <!-- num: not a value --> Re-read the cited paper before
an equation or a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Conventions; in-in formalism and the cubic action; EFT of inflation; shape templates; consistency relations; collider building blocks; bootstrap singularities and cutting rules; feature templates; loops; decoherence; QFT in de Sitter and stochastic inflation | `references/formalism.md` |
| One card per model class: canonical slow roll, small sound speed (EFT, DBI), excited initial states, curvaton and local multi-field, quasi-single-field and collider, sharp features, resonant features (axion monodromy); their status | `references/models.md` |
| Consistency-relation theorems, Suyama–Yamaguchi inequality, sound-speed bounds, collider and bootstrap results, loop and decoherence results, de Sitter representations, history of key results | `references/results.md` |
| Slow-roll order, decoupling limit, perturbativity at small $c_s$, Bunch–Davies, weak mixing, templates, stochastic and Lindblad approximations, convention traps, printing slips, numerical issues, referee checklist | `references/approximations.md` |
| Debates (one-loop PBH back-reaction, scalar decoherence, collider mixing, feature hints), unresolved calculations, forecasts, stale claims | `references/open-questions.md` |
| How the single-field scalar bispectrum follows from the cubic action with the in-in formalism, up to the Maldacena result | `deep/in-in-bispectrum.md` |
| How the Goldstone action is built from the unitary-gauge EFT, when the decoupling limit holds, and how $f_{\rm NL}$ follows from $c_s$ and $M_3$ | `deep/eft-of-inflation.md` |
| How the squeezed-limit consistency relations are derived, what violates them, and why the single-field squeezed signal is not observable | `deep/soft-limits-and-consistency.md` |
| Bibliography with versions read; subtopics and where they come from | `references/sources.tsv`, `references/subtopics.tsv` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- The slow-roll shape function is $S=\frac{\epsilon}{8}\left[-\left(\frac{k_{1}^{2}}{k_{2}k_{3}}+{\rm 2~perm.}\right)+\left(\frac{k_{1}}{k_{2}}+{\rm 5~perm.}\right)+\frac{8}{K}\left(\frac{k_{1}k_{2}}{k_{3}}+{\rm 2~perm.}\right)\right]$ $+\frac{\eta}{8}\left(\frac{k_{1}^{2}}{k_{2}k_{3}}+{\rm 2~perm.}\right)~$ with Hubble-flow η (Chen 2010, arXiv:1002.1416) [src: Eq. 4.23]; the η term comes from the field redefinition, and $f_{NL}\sim{\cal O}(0.01)$ [src: Sect. 4, text after Eq. 4.23].
- Single-field squeezed limit: $\lim_{k_{1}\rightarrow 0}\langle\zeta_{\vec{\kappa}_{1}}\zeta_{\vec{\kappa}_{2}}\zeta_{\vec{\kappa}_{3}}\rangle=-(2\pi)^{3}\delta^{3}(\sum_{i}\vec{k}_{i})(n_{s}-1)P_{k_{1}}P_{k_{3}}\;$ (arXiv:astro-ph/0407059) [src: Eq. 1]; it is a projection effect with no primordial signal in the CMB or halo bias (arXiv:1305.0824) [src: abstract].
- Soft limits form an infinite tower of Ward identities, fixed completely at orders n = 0, 1 (arXiv:1304.5527) [src: abstract]; they fail when the growing mode is not constant, as in non-attractor phases (arXiv:1210.3692) [src: abstract]. <!-- num: not a value -->
- EFT of inflation: $c_{s}^{-2}=1-\frac{2M_{2}^{4}}{M_{\rm Pl}^{2}\dot{H}}\;$ [src: Eq. 38] and $f_{\rm NL}^{\rm equil.}=\frac{85}{324}\cdot\frac{1}{c_{s}^{2}}\;$ (arXiv:0709.0293) [src: Eq. 45]; Planck 2018 gives $c_{\mathrm{s}}^{\rm DBI}\geq\ 0.086$ at 95% (arXiv:1905.05697) [src: Eq. 59].
- Superhorizon non-Gaussianity obeys $\tau_{NL}\geq\frac{36}{25}f_{NL}^{2}.$ (arXiv:0709.2545) [src: Eq. 19].
- Collider mass parameter $\mu=\sqrt{m^{2}/H^{2}-9/4}$ (arXiv:2203.08128) [src: Sect. 3.1, inline, text after Eq. 3.7].
- Collider squeezed scaling $S\sim q^{\frac{1}{2}+\mathrm{i}\mu}P_{s}(\cos\theta)$ and, for bulk particle production in a weakly coupled background, $f_{\mathrm{NL}}^{\mathrm{ex}}\sim\varepsilon\mu^{n}\mathrm{e}^{-\pi\mu}$ (arXiv:2203.08128) [src: Sect. 3.1, inline, text after Eq. 3.8]; strong mixing halves the Boltzmann suppression (arXiv:2608.23243) [src: abstract].
- No collider detection: $2.35σ$ maximum for spin-0 in Planck after look-elsewhere (arXiv:2512.22085) [src: abstract]; maximal $χ^2$ improvement of $5.3$ over the multi-field landscape (arXiv:2607.18369) [src: abstract].
- Bootstrap: the total-energy pole has the flat-space amplitude as residue, $\lim_{E\to 0}\psi_{n}=\frac{iA_{n}}{E^{\alpha}}\,$ (arXiv:2203.08121) [src: Eq. 2.9]; unitarity gives the cosmological optical theorem (arXiv:2009.02898) [src: abstract].
- Features: sharp features oscillate linearly in k, resonant ones in $\log k$ (arXiv:2203.08128) [src: Sect. 4.1]; Planck hints reach at most $2.6σ$ global significance (arXiv:2605.30236) [src: abstract].
- Loops grow at most as logarithms of the scale factor (arXiv:hep-th/0605244) [src: abstract]; the one-loop running is in $H/\mu$ (arXiv:0912.2734) [src: abstract]. <!-- num: not a value --> <!-- eq: notation -->
- The claim that enhanced small-scale modes spoil CMB-scale correlators at one loop (arXiv:2211.03395) is disputed by boundary-term, separate-universe and Ward-identity analyses (arXiv:2408.08296, arXiv:2605.04815, arXiv:2605.13325) [src: abstracts].
- Scalar decoherence in single-clock inflation is not slow-roll suppressed once scalar and tensor environments act together (Burgess et al. 2026, arXiv:2607.22914) [src: abstract].
- Light fields in de Sitter: $P_{\rm eq}(\phi)=Ce^{-8\pi^{2}V(\phi)/3H^{4}}\,$ at leading order (arXiv:2106.09728) [src: Eq. 2.4]; SdSET derives stochastic inflation as RG resummation (arXiv:2007.03693) [src: abstract].

## Checks a referee makes
<!-- key: checks-a-referee-makes -->

- Power-spectrum normalisation and the variable and sign of $f_{\rm NL}$ stated.
- Slow-roll parameters defined (Hubble-flow or potential) and the order kept.
- Vacuum stated; folded enhancement from excited states discussed.
- Decoupling limit and strong-coupling scale checked for small $c_s$.
- Weak or strong mixing justified for collider signals; Boltzmann suppression not assumed blindly.
- Squeezed-limit claims separated from projection effects.
- Loops: regularisation, counterterms, tadpoles, boundary terms; replies to the PBH loop claim cited.
- Template searches: orthogonalisation and look-elsewhere correction. Details: `references/approximations.md`, last section.

## Errors that recur
<!-- key: errors-that-recur -->

- Moving a coefficient between Chen's $\frac{P_{\zeta}}{2k_{1}^{3}}(2\pi)^{5}$ normalisation (arXiv:1002.1416, Eq. 4.17) and the $(2\pi)^{3}P_{k}$ of Creminelli & Zaldarriaga (arXiv:astro-ph/0407059, Eq. 3) without the relation. <!-- num: not a value --> <!-- eq: notation -->
- Quoting an $f_{\rm NL}$ without its variable: Planck templates use $\Phi\equiv(3/5)\zeta$ (arXiv:1905.05697) [src: Sect. 2.1, inline, text after Eq. 2].
- Treating Cheung et al.'s Eq. 41, labelled $n_{s}$, as $n_{s}-1$ (arXiv:0709.0293). <!-- num: not a value -->
- Copying the action of Chen's Eq. 4.1, printed without the square of the Planck mass (arXiv:1002.1416).
- Citing $c_{s}>0.028$ (arXiv:0709.0293, Eq. 47, WMAP era) as the current bound.
- Calling the single-field squeezed limit an observable primordial signal (arXiv:1305.0824).
- Saying one-loop effects rule out PBHs from single-field inflation; the paper itself now says "constraining" (arXiv:2211.03395, v3).
- Assuming $\mathrm{e}^{-\pi\mu}$ suppression at strong mixing or with oscillating masses (arXiv:2608.23243, arXiv:2511.00152). <!-- num: not a value -->
- Translating equilateral constraints to other shapes through the equilateral normalisation (arXiv:astro-ph/0405356).

## Related skills
<!-- key: related-skills -->

- `thcosmo-inflation`: background dynamics, slow-roll parameters, model landscape, $n_s$ and $r$, stochastic and eternal inflation and the tails of the curvature distribution; here only the correlators and the QFT justification of the stochastic equation.
- `thcosmo-lss-perturbation-theory`: late-time consistency relations, scale-dependent bias from local PNG and $b_\phi$; here the primordial shapes and soft theorems.
- `thcosmo-cosmological-perturbations`: gauge choices, conserved ζ, separate universe and δN used for local-type predictions.
- `thcosmo-cmb-physics`: transfer of the primordial bispectrum to the CMB; `thcosmo-cosmological-gravitational-waves`: tensor spectra and scalar-induced waves; `thcosmo-pbh-defects`: PBH formation from enhanced spectra; `thcosmo-fundamental-theory`: string embeddings such as axion monodromy and de Sitter constructions.
- `theoretical-cosmology` hub: conventions atlas for slow-roll parameters, ζ versus ℛ and the sign of $f_{\rm NL}$.
- cosmoskill `cosmo-inflation-primordial` (measured $n_s$, $r$, $f_{\rm NL}$), `cosmo-cmb` (bispectrum likelihoods), `cosmo-galaxy-clustering` (LSS searches for PNG and features).

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

Sizes, in thousands of tokens: L1 4k; approximations 4k; formalism 14k; models 4k; open 3k; results 6k; deep/eft-of-inflation 9k; deep/in-in-bispectrum 9k; deep/soft-limits-and-consistency 10k.

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
`python3 "${CLAUDE_SKILL_DIR}"/../*theoretical-cosmology/scripts/layers.py thcosmo-primordial-correlators`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. An
override replaces its base section for this researcher: use it, and quote
the base value beside it, both labelled. A suppressed section is left out
and named as suppressed; use it only when the question asks for that
section's own content, and then say that the layer hides it. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[thcosmoskill L<level> · <base, personal, project, or several joined by +> · thcosmo-primordial-correlators/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- thcosmoskill:block:end -->
