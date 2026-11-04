---
name: thcosmo-inflation
description: Use when deriving, checking or reviewing inflationary dynamics and models — slow roll, Hubble-flow and potential parameters, n_s and r predictions, Lyth bound, Starobinsky, Higgs, monomial, natural, hilltop, alpha- and xi-attractors, hybrid, curvaton, turning trajectories, ultra-slow and constant roll, reheating and N_*, preheating, initial conditions, stochastic and eternal inflation, curvature tails, ACT DR6 n_s and model status.
---

# Inflation — expert reference

Snapshot 2026-11-02. Every equation and number names its paper and
the place it was read; no equation or number is derived by an agent.
Conventions: reduced Planck mass in Baumann (arXiv:0907.5424) and Martin, Ringeval & Vennin (arXiv:1303.3787); Baumann counts e-folds forward in his Eq. 70 and backward from the end of inflation in his Eq. 82, Martin et al. forward from an initial time; pivot 0.05 Mpc⁻¹ except in Planck 2018 X model comparisons (0.002 Mpc⁻¹). <!-- num: not a value --> Re-read the cited paper before
an equation or a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Conventions; slow-roll background, Hubble-flow and potential parameters, first- and second-order spectra, $n_s$, $r$, Lyth bound; α- and ξ-attractor formalism; ultra-slow and constant roll; multi-field covariant formalism and turn rate; reheating and $N_*$; preheating; stochastic inflation and eternal inflation | `references/formalism.md` |
| One card per model: Starobinsky, Higgs, monomial, natural, hilltop, other Planck-table classes, α-attractors, ξ-attractors, polynomial attractors, hybrid, curvaton, curved field spaces; their status after ACT DR6 | `references/models.md` |
| Bounds on $n_s$ and $r$ by dataset, reheating constraints, initial conditions in numerical relativity, stochastic tails, history of key results | `references/results.md` |
| Validity of slow roll and horizon crossing, the $N_*$ window, EFT and frames, separate universe; convention traps (N, η, α, pivot); numerical tools; referee checklist | `references/approximations.md` |
| Debates (the high $n_s$ of ACT with DESI; the initial-conditions problem), unresolved calculations, next data, stale claims | `references/open-questions.md` |
| How $n_s$, $r$ and the running follow from the Hubble-flow parameters to second order, and how Hubble-flow and potential parameters convert | `deep/slow-roll-predictions.md` |
| How $N_*$ follows from the reheating history, and how $w_{\rm reh}$, $T_{\rm reh}$ and the reheating parameter move $n_s$ and $r$ for a given model | `deep/reheating-and-efolds.md` |
| How multi-field perturbations are computed (adiabatic and entropic split, turns, isocurvature transfer, δN), and when a model reduces to single field | `deep/multi-field-perturbations.md` |
| Bibliography with versions read; subtopics and where they come from | `references/sources.tsv`, `references/subtopics.tsv` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- Leading order: $n_{\rm s}-1=2\eta_{\rm v}^{\star}-6\epsilon_{\rm v}^{\star}$, $r=16\epsilon_{\rm v}^{\star}$ and the single-field consistency relation $r=-8n_{\rm t}$ (arXiv:0907.5424) [src: Eqs. 236, 238, 239]; in Hubble-flow form $n_{\scriptscriptstyle{\mathrm{S}}}=1-2\epsilon_{1}-\epsilon_{2},\quad n_{\scriptscriptstyle{\mathrm{T}}}=-2\epsilon_{1}.$ (arXiv:1303.3787) [src: Eq. 31].
- Baumann's η = −φ̈/(Hφ̇) is not the Hubble-flow $\epsilon_2$; in slow roll $\varepsilon\approx\epsilon_{\rm v}\,,\hskip 18.49988pt\eta\approx\eta_{\rm v}-\epsilon_{\rm v}\,.$ (arXiv:0907.5424) [src: Eq. 80].
- The energy scale follows from r: $V^{1/4}\sim\left(\frac{r}{0.01}\right)^{1/4}\,10^{16}\,{\rm GeV}$ (arXiv:0907.5424) [src: Eq. 218]; the Lyth bound $\frac{\Delta\phi}{M_{\rm pl}}\simeq{\cal O}(1)\left(\frac{r}{0.01}\right)^{1/2}\,,$ carries an order-one coefficient [src: Eq. 356].
- $N_*$ is set by reheating: $\Delta N_{*}=\ln R_{\mathrm{rad}}-N_{{}_{0}}-\dfrac{1}{4}\ln\left[\dfrac{9}{\epsilon_{1*}(3-\epsilon_{1\mathrm{end}})}\dfrac{V_{\mathrm{end}}}{V_{*}}\right]+\dfrac{1}{4}\ln(8\pi^{2}P_{*}),$ (arXiv:1303.3787) [src: Eq. 48]; Planck 2018 X writes the same with $w_{\rm int}$ (arXiv:1807.06211, Eq. 47).
- $R^{2}$ predicts $n_{\mathrm{s}}-1\simeq-\frac{2}{N}\thinspace,\quad r\simeq\frac{12}{N^{2}},$ (arXiv:1807.06211) [src: Eq. 48]; α-attractors at small α give n_s = 1 − 2/N, r = 12α/N² (arXiv:1311.0472) [src: abstract].
- Planck 2018 + BK15: $\phi^{2}$ at ln B = −11.5, natural inflation $-6.6$, relative to $R^{2}$ (arXiv:1807.06211) [src: Table 5]; BK18 gives $r_{0.05}<0.036$ (arXiv:2110.00483) [src: abstract].
- ACT DR6 + Planck + lensing + DESI DR1: $n_s=0.974\pm0.003$ (arXiv:2503.14452) [src: abstract]; Starobinsky on the 2σ boundary of P-ACT-LB (arXiv:2503.14454) [src: Sect. IV.4]; with SPT and DESI DR2, Higgs, Starobinsky and exponential α-attractors disfavoured at more than 2σ (arXiv:2512.05108) [src: abstract].
- The high $n_s$ tracks the CMB–DESI BAO tension and τ (arXiv:2512.05108) [src: abstract], and drops to n_s = 0.9692 ± 0.0035 with a small negative curvature (arXiv:2607.28445) [src: abstract], whose authors conclude that the tension with these models holds only for ΛCDM.
- Ultra-slow roll (η = 3) invalidates the horizon-crossing formula: the curvature perturbation evolves outside the horizon (arXiv:gr-qc/0503017) [src: abstract].
- Stochastic inflation: $\frac{\mathrm{d}\varphi}{\mathrm{d}N}=-\frac{V^{\prime}}{3H^{2}}+\frac{H}{2\pi}\xi\left(N\right)\,.$ in e-folds (arXiv:1506.04732) [src: Eq. 1]; quantum diffusion makes the tails exponential, beyond any perturbative non-Gaussian expansion (arXiv:1912.05399) [src: abstract].
- Eternal inflation sets in at the critical speed φ̇²/H⁴ = 3/(2π²) (arXiv:0802.1067) [src: abstract].
- Turn rate $\eta_{\bot}\equiv\frac{V_{N}}{\dot{\phi}_{0}H}\,,$ measured against field-space geodesics (arXiv:1010.3693) [src: Eq. 2.18]; field-space curvature can destabilise heavy fields (arXiv:1510.01281) [src: abstract].
- Numerical relativity: inflation starts from gradient-dominated data if the field begins on a flat part of the potential (arXiv:1511.05143) [src: abstract]; small-field and, per a 2026 study, plateau models are less robust (arXiv:1608.04408; arXiv:2608.24997) [src: abstracts].

## Checks a referee makes
<!-- key: checks-a-referee-makes -->

- Planck-mass convention, direction of N, and the meaning of η and α stated.
- Slow-roll order stated; numerical integration where slow roll fails or the background is off the attractor.
- $N_*$ from a stated reheating history when the verdict depends on $n_s$.
- Bounds with dataset and pivot; the ΛCDM and DESI dependence of the high $n_s$ acknowledged.
- EFT cutoff and frame of reheating for non-minimal and $R^{2}$ models; field-space geometry and isocurvature for multi-field models.
- Tails from stochastic δN, not perturbative expansions. Details: `references/approximations.md`, last section.

## Errors that recur
<!-- key: errors-that-recur -->

- Comparing r at 0.002 Mpc⁻¹ (Planck 2018 X, arXiv:1807.06211) [src: abstract] with r at 0.05 Mpc⁻¹ (BICEP/Keck, arXiv:2110.00483) [src: abstract] without the pivot.
- Mixing Baumann's η with Martin's $\epsilon_2$, or the forward and backward e-fold conventions, and flipping the sign of $d\varepsilon/dN$ (arXiv:0907.5424, Eqs. 70, 73, 82).
- Using the α of α-attractors, of constant roll (arXiv:1411.5021, Eq. 7) and the running $\alpha_{\rm S}$ interchangeably.
- Declaring Starobinsky inflation excluded from ACT DR6 alone: its status depends on DESI BAO, τ, reheating and the cosmological model (arXiv:2512.05108; arXiv:2510.18656; arXiv:2607.28445) [src: abstracts].
- Quoting n_s = 1 − 2/N, r = 12α/N² for large α (arXiv:1311.0472) [src: abstract].
- Applying horizon-crossing or slow-roll formulas through an ultra-slow-roll phase, or trusting a smooth Hubble-flow parametrisation of it (arXiv:gr-qc/0503017; arXiv:2606.28005) [src: abstracts].
- Treating $\phi^{2}$ or natural inflation as viable benchmarks (arXiv:1807.06211) [src: Table 5].
- Copying the Planck 2018 X hilltop limit without noting that the quartic-case limit is printed with $\mu_{2}$ (arXiv:1807.06211) [src: Sect. 4.2].

## Related skills
<!-- key: related-skills -->

- `thcosmo-primordial-correlators`: quantisation of the modes, in-in formalism, EFT of inflation, sound speed, non-Gaussianity shapes, loop corrections from ultra-slow roll and their debate, QFT in de Sitter. Here only the power spectra and the stochastic formalism.
- `thcosmo-fundamental-theory`: string embeddings (monodromy, D-brane, Kähler moduli), swampland and trans-Planckian censorship, alternatives to inflation.
- `thcosmo-pbh-defects`: PBH formation and abundance from the tails computed here.
- `thcosmo-cosmological-gravitational-waves`: tensor backgrounds beyond r, preheating and scalar-induced gravitational waves.
- `thcosmo-cosmological-perturbations`: gauge-invariant variables, δN and separate universe, adiabatic and isocurvature initial conditions.
- cosmoskill `cosmo-inflation-primordial` (measured $n_s$, r, running, isocurvature), `cosmo-cmb` (likelihoods, τ), `cosmo-tensions-anomalies` (CMB–BAO tension).

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

Sizes, in thousands of tokens: L1 4k; approximations 3k; formalism 9k; models 6k; open 2k; results 4k; deep/multi-field-perturbations 8k; deep/reheating-and-efolds 9k; deep/slow-roll-predictions 11k.

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
`python3 "${CLAUDE_SKILL_DIR}"/../*theoretical-cosmology/scripts/layers.py thcosmo-inflation`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. An
override replaces its base section for this researcher: use it, and quote
the base value beside it, both labelled. A suppressed section is left out
and named as suppressed; use it only when the question asks for that
section's own content, and then say that the layer hides it. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[thcosmoskill L<level> · <base, personal, project, or several joined by +> · thcosmo-inflation/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- thcosmoskill:block:end -->
