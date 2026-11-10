---
name: thcosmo-cosmological-gravitational-waves
description: Use when deriving, checking or reviewing theory of cosmological gravitational-wave backgrounds — Omega_GW, h_c and S_h normalisations, primordial tensors and transfer functions, n_T = -r/8, axion-gauge chiral tensors, preheating, first-order phase-transition templates (alpha, beta/H, v_w, K, sound waves, turbulence), cosmic strings and domain walls, scalar-induced waves and their gauge issue, GW friction and d_L^GW, PTA cosmological interpretations.
---

# Cosmological gravitational waves — expert reference

Snapshot 2026-11-05. Every equation and number names its paper and
the place it was read; no equation or number is derived by an agent.
Conventions: signature (−,+,+,+), conformal time, $ds^{2}=a^{2}(\eta)\,\left[-d\eta^{2}+(\delta_{ij}+h_{ij})\,dx^{i}dx^{j}\right]\,.$ (arXiv:1801.04268) [src: Eq. 66], Fourier kernel $e^{-i\mathbf{k}\cdot\mathbf{x}}$ with $d^3k/(2\pi)^3$, polarisation tensors normalised to 2; see `references/formalism.md` and the hub's `references/conventions.md`. <!-- num: not a value --> Re-read the cited paper before
an equation or a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Conventions; tensor equation of motion; $h_c$, $S_h$, $\Omega_{\rm GW}$ and redshifting; inflationary tensor spectrum and transfer function; axion–gauge-field production; preheating; phase-transition parameters and templates; string loops and domain walls; scalar-induced kernels; friction and $d_L^{\rm GW}$ | `references/formalism.md` |
| One card per source: slow-roll inflation, axion inflation, preheating, sound-wave and supercooled transitions, cosmic strings, biased domain walls, scalar-induced waves; their status | `references/models.md` |
| Radiation bound; amplitude of the irreducible background; neutrino damping; PT, defect and SIGW results; propagation; history of key results | `references/results.md` |
| Averaging and sub-horizon conditions; transfer-function approximations; homogeneous backreaction; PT template validity; Nambu–Goto versus field theory; SIGW gauge and order; normalisation traps; referee checklist | `references/approximations.md` |
| PTA interpretation, string-loop and backreaction debates, SIGW gauge; forecasts; stale claims | `references/open-questions.md` |
| Bibliography with versions read; subtopics and where they come from | `references/sources.tsv`, `references/subtopics.tsv` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- $\Omega_{\rm GW}^{(0)}(f)=\frac{4\pi^{2}}{3H_{0}^{2}}\,f^{3}\,S_{h}(f)\,.$ (arXiv:1801.04268) [src: Eq. 94] holds with $h_c$ normalised by $\langle h_{ij}(\mathbf{x},\eta)\,h_{ij}(\mathbf{x},\eta)\rangle=2\,\int_{0}^{+\infty}\frac{dk}{k}\,h_{c}^{2}(k,\eta)\,,$ [src: Eq. 85]; the review flags "the factor two difference with respect to e.g. [54]" [src: Sect. 3.2, text before Eq. 94].
- A background produced in radiation domination today has $h^{2}\,\Omega_{\rm GW}=1.6\times 10^{-5}\,\left(\frac{100}{g_{*}(T_{p})}\right)^{1/3}\,\left(\frac{1}{\rho}\,\frac{d\rho_{\rm GW}}{d\mathrm{log}k}\right)_{p}$ (arXiv:1801.04268) [src: Eq. 104] at $f=2.6\times 10^{-8}\,\mathrm{Hz}\,\,\,x_{k}\,\left(\frac{g_{*}(T_{p})}{100}\right)^{1/6}\,\frac{T_{p}}{\mathrm{GeV}}$ [src: Eq. 105], with $x_{k}\geq 1$ by causality [src: Sect. 3.3, inline, text after Eq. 103].
- The integrated density obeys $\left(\frac{h^{2}\rho_{\rm GW}}{\rho_{c}}\right)_{0}\leq h^{2}\Omega_{\gamma}^{0}~\frac{7}{8}\,\left(\frac{4}{11}\right)^{4/3}\Delta N_{\rm eff}=5.6\times 10^{-6}\,\Delta N_{\rm eff}\,,$ (arXiv:1801.04268) [src: Eq. 129], for sub-horizon backgrounds produced before BBN or decoupling [src: Sect. 4.1, text after Eq. 130].
- Slow-roll inflation gives $n_{T}(k)=-\frac{r_{k}}{8}\,.$ (arXiv:1801.04268) [src: Eq. 203] and $\Omega_{\rm GW}\simeq 5\cdot 10^{-16}\left({H_{k}\over H_{\rm max}}\right)^{2}\,,$ [src: Eq. 204]; a stiff epoch lasting "until just before BBN" can raise this by $\sim 10^{7}$ at LISA frequencies for "a super stiff phase with $w\simeq+1$" [src: Sect. 5.2, inline, text after Eq. 230].
- Neutrino free streaming cuts the squared tensor amplitude "by 35.6 % for wavelengths that enter the horizon during the radiation-dominated phase" (arXiv:astro-ph/0306304) [src: abstract].
- Axion–gauge-field production gives a chiral, non-Gaussian, blue background, $h^{2}\Omega_{\rm GW}^{\rm(pp)}\simeq 1.5\cdot 10^{-13}(H/m_{\rm Pl})^{4}(e^{4\pi\xi}/{\xi^{6}})$ for $\xi>1$ (arXiv:1801.04268) [src: Sect. 6.1.2, inline, text after Eq. 241]; a detectable signal needs "significant backreaction" (arXiv:2510.17207) [src: abstract], where lattice and homogeneous treatments disagree (arXiv:2411.16368; arXiv:2510.17207) [src: abstract].
- The 2024 LISA sound-wave template is a double broken power law with slopes 3, 1, −3 and amplitude $h^{2}\Omega_{\mathrm{int}}=h^{2}F_{\mathrm{GW},0}\,A_{\text{sw}}\,K^{2}\left(H_{*}\tau_{\rm sw}\right)\left(H_{*}R_{*}\right),$ (arXiv:2403.03723) [src: Eq. 10; Table 1], with $H_{*}\tau_{\rm sw}={\rm min}\left[H_{*}\tau_{\rm sh},1\right]$ [src: Sect. 2.2.1, inline, text after Eq. 11].
- Strong deflagrations: current modelling "substantially overestimates the gravitational wave signal", "in the most extreme case by a factor of $10^{3}$" (arXiv:1906.00480) [src: abstract]; the daisy-resummed potential carries "two to three orders-of-magnitude uncertainty in the peak gravitational wave amplitude" (arXiv:2009.10080) [src: abstract].
- String bounds depend on the loop picture: field-theory loops decaying within a Hubble time give "much weaker gravitational wave constraints on their tension" than Nambu–Goto loops (arXiv:1703.06696) [src: abstract].
- NANOGrav 15-year: all tested cosmological sources "with the exception of stable cosmic strings of field theory origin" can reproduce the signal, with Bayes factors "in the range from 10 to 100" that "should not be regarded as evidence for new physics" (arXiv:2306.16219) [src: abstract].
- Scalar-induced waves have an infrared tail $\frac{d\ln\Omega_{\rm GW}^{\rm induced}}{d\ln k}(k\ll k_{\rm rh})\approx 3\,,$ (arXiv:2109.01398) [src: Eq. 2.23], and $3-2\vert b\vert$ in an intermediate range of a constant-$w$ era [src: Eq. 2.22]; the scaling survives higher orders and non-Gaussianity (arXiv:2609.17928) [src: abstract].
- The gauge issue of induced waves is not solved by gauge-invariant variables: "There are infinitely many ways to define gauge invariant variables" (arXiv:2109.01398) [src: Sect. 7.2].
- Modified friction: $\frac{d_{L}^{\,\rm gw}(z)}{d_{L}^{\,\rm em}(z)}=\Xi_{0}+\frac{1-\Xi_{0}}{(1+z)^{n}}\,.$ (arXiv:1805.08731) [src: Eq. 22]; it matters "even in theories where the speed of gravity is equal to $c$" [src: abstract].

## Checks a referee makes
<!-- key: checks-a-referee-makes -->

- Normalisation of $h_c$, $\mathcal{P}_h$ and polarisation tensors, the Planck mass, $\Omega_{\rm GW}$ or $h^2\Omega_{\rm GW}$, and the $g_*$, $g_S$ at production.
- Sub-horizon production, causal $f^3$ tail, radiation bound applied to the integrated density.
- PT: template and its validity (Chapman–Jouguet speed, shock time, turbulence, the 0.6 factor in K, expanding versus Minkowski simulations, thermal-potential method). <!-- num: not a value -->
- Strings: loop picture, loop distribution, harmonic or burst formalism; walls: bias mechanism.
- Axion inflation: backreaction treatment and $\Delta N_{\rm eff}$. SIGW: gauge, Gaussianity, constant-w and reheating assumptions, order in a matter era. Details: `references/approximations.md`, last section.

## Errors that recur
<!-- key: errors-that-recur -->

- Mixing the $h_c$ convention of Caprini & Figueroa with one that "differs by a factor 2" (arXiv:1801.04268) [src: Sect. 3.2, text after Eq. 85]. <!-- num: not a value -->
- Using the 2019 Eq. 29 when shocks form within a Hubble time; the review says Eq. 32 is "often the relevant expression" for LISA models (arXiv:1910.13125) [src: Sect. 3.3, inline, text after Eq. 32]. <!-- num: not a value -->
- Taking $K=\kappa\alpha/(1+\alpha)$ of one bubble for the bulk flow; the 2024 template uses $K\simeq 0.6\,\kappa\,\alpha/(1+\alpha)$ (arXiv:2403.03723) [src: Sect. 2.2.1, inline, text after Eq. 11].
- Using the envelope approximation for strong transitions, where collided walls are "essential" (arXiv:2403.03723) [src: Sect. 2.1, text after Eq. 6].
- Quoting a $G\mu$ bound without its loop model; or quoting a PTA fit as evidence for new physics (arXiv:2306.16219) [src: abstract].
- Applying the radiation bound to a narrow peak or to super-horizon modes (arXiv:1801.04268) [src: Sect. 4.1, text after Eq. 130].
- Copying printed slips: the exponent after Eq. 230 of arXiv:1801.04268 is printed as a product, $\dot l$ before its Eq. 380 lacks μ, Eq. 116 of arXiv:2401.04388 has limits from ∞ to ∞, and Eq. 61 of arXiv:1807.09241 squares $(1+\cos\iota)$ (see `formalism.md`, `approximations.md`). <!-- num: not a value -->
- Treating the speed of tensors here: its constraints on theories are in `thcosmo-modified-gravity`.

## Related skills
<!-- key: related-skills -->

- `thcosmo-modified-gravity`: the speed of tensors after GW170817, graviton decay and the Horndeski and DHOST conditions (`deep/speed-of-tensors-constraints.md`); here only the propagation equations.
- `thcosmo-inflation`: inflationary dynamics, $r$ and $n_s$ of each model; `thcosmo-primordial-correlators`: tensor non-Gaussianity and loops.
- `thcosmo-baryogenesis-phase-transitions` (planned): nucleation, wall velocity, effective potential; here only the GW spectra.
- `thcosmo-pbh-defects` (planned): defect networks and PBH abundance; here only their GW signals.
- `thcosmo-cosmological-perturbations` (planned): the gauge question of second-order tensors.
- `thcosmo-neutrinos-light-relics`: the Standard-Model $N_{\rm eff}$ behind the radiation bound.
- cosmoskill `cosmo-early-universe-exotica` (measured backgrounds, PTA fits), `cosmo-multimessenger` (standard sirens), `cosmo-cmb` and `cosmo-inflation-primordial` (r bounds).

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

Sizes, in thousands of tokens: L1 4k; approximations 4k; formalism 12k; models 5k; open 2k; results 4k; deep/cosmic-string-spectra 9k; deep/phase-transition-spectra 10k; deep/scalar-induced-kernels 8k.

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
`python3 "${CLAUDE_SKILL_DIR}"/../*theoretical-cosmology/scripts/layers.py thcosmo-cosmological-gravitational-waves`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. An
override replaces its base section for this researcher: use it, and quote
the base value beside it, both labelled. A suppressed section is left out
and named as suppressed; use it only when the question asks for that
section's own content, and then say that the layer hides it. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[thcosmoskill L<level> · <base, personal, project, or several joined by +> · thcosmo-cosmological-gravitational-waves/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- thcosmoskill:block:end -->
