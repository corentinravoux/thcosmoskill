---
name: thcosmo-neutrinos-light-relics
description: Use when deriving, checking or reviewing the theory of cosmic neutrinos and light relics — neutrino decoupling, Standard-Model N_eff and its QED corrections, Delta N_eff of thermal relics, massive-neutrino Boltzmann hierarchy, free streaming, -8 f_nu suppression, phase shift, dark radiation (free-streaming or fluid), LiMRs, light sterile neutrinos, self-interacting neutrinos (G_eff), majorons, invisible neutrino decay, negative neutrino mass parameters.
---

# Neutrinos and light relics — expert reference

Snapshot 2026-11-03. Every equation and number names its paper and
the place it was read; no equation or number is derived by an agent.
Conventions: natural units; Lesgourgues & Pastor (arXiv:astro-ph/0603494) use signature (+,−,−,−) with φ in $g_{00}$, Ma & Bertschinger (arXiv:astro-ph/9506072) use (−,+,+,+) with ψ in $g_{00}$; $N_{\rm eff}$ defined through ρ_ν/ρ_γ (arXiv:2012.02726, Eq. 1, limit T/m_e → 0); see `references/formalism.md` and the hub's `references/conventions.md`. <!-- num: not a value --> Re-read the cited paper before
an equation or a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Conventions; decoupling and the definition of $N_{\rm eff}$; $\Delta N_{\rm eff}$ of a thermal relic; massive-neutrino background, orderings; Vlasov equation and Legendre hierarchy; free-streaming scales; phase-shift formalism; interaction and decay formalism; LiMR scales; sterile thermalisation | `references/formalism.md` |
| One card per model: free-streaming and fluid-like dark radiation, self-interacting neutrinos, invisible decay, LiMRs, light sterile neutrinos, majorons; their status | `references/models.md` |
| Standard-Model $N_{\rm eff}$ and its error budget; minimal thermal $\Delta N_{\rm eff}$; power suppression; phase-shift detections; LiMR bounds; history of key results | `references/results.md` |
| Instantaneous decoupling; BBN with negative $\Delta N_{\rm eff}$; contact limit and collision kernels; fluid approximations in Boltzmann codes; convention traps; referee checklist | `references/approximations.md` |
| The debate on NLO QED corrections to $N_{\rm eff}^{\rm SM}$; the neutrino-mass tension seen from theory; forecasts; stale claims | `references/open-questions.md` |
| Bibliography with versions read; subtopics and where they come from | `references/sources.tsv`, `references/subtopics.tsv` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- $N_{\rm eff}$ is defined by $\left.\frac{\rho_{\nu}}{\rho_{\gamma}}\right|_{T/m_{e}\to 0}\equiv\frac{7}{8}\Big(\frac{4}{11}\Big)^{4/3}N_{\rm eff}^{\rm SM},$ (arXiv:2012.02726) [src: Eq. 1]; the benchmark is $N_{\rm eff}^{\rm SM} = 3.0440 \pm 0.0002$, its error dominated by numerics and $\sin^2\theta_{12}$ (arXiv:2012.02726) [src: abstract].
- The deviation from 3 is mostly the $m_e/T_d$ correction (+0.04) and the ${\cal O}(e^2)$ QED equation of state (+0.01); non-instantaneous decoupling gives −0.005 (arXiv:2012.02726) [src: Table 5].
- 3.046 is stale: it misses the ${\cal O}(e^3)$ correction (arXiv:2012.02726) [src: Sect. 6]. The claim of 3.043 (arXiv:2306.05460) [src: abstract] is disputed: the NLO rate effect is "about a factor of 30 smaller" (arXiv:2402.18481) [src: abstract].
- A light thermal relic adds $\Delta N_{\rm eff}=\frac{4}{7}g_{X,\star}\left(\frac{T_{X}}{T_{\nu}}\right)^{4}=\frac{4}{7}g_{X,\star}\left(\frac{43}{4g_{\star}(T_{F})}\right)^{4/3}\ ,$ (arXiv:2203.07943) [src: Eq. 2]; any species once in equilibrium gives $\Delta N_{\rm eff}\geq 0.027$ unless the thermal history changes [src: Sect. 2.1]; a reheating temperature below $T_F$ evades it (arXiv:1604.08614) [src: Sect. 1].
- $\Omega_{\nu}=\frac{\rho_{\nu}}{\rho_{\rm c}}=\frac{\sum_{i}m_{i}}{93.14\,h^{2}~{\rm eV}}~,$ (arXiv:astro-ph/0603494) [src: Eq. 12]; minimal sums $\sum m_{\nu}\gtrsim 0.06$ eV (normal) and $\gtrsim 0.10$ eV (inverted) (arXiv:2404.19322) [src: Sect. III].
- Free streaming leaves modes with $k<k_{\rm nr}$, $k_{\rm nr}\simeq 0.018\,\,\Omega_{\rm m}^{1/2}\left(\frac{m}{1\,\mathrm{eV}}\right)^{1/2}h\,\mathrm{Mpc}^{-1}~.$, untouched (arXiv:astro-ph/0603494) [src: Eq. 97]; above it $\delta_{\rm cdm}\propto a^{p_{+}}\simeq a^{1-\frac{3}{5}f_{\nu}}~,$ [src: Eq. 134].
- The small-scale suppression rule, printed $\frac{P(k)^{f_{\nu}}}{P(k)^{f_{\nu}=0}}\simeq-8\,f_{\nu}~.$ (arXiv:astro-ph/0603494) [src: Eq. 144], is called "a reasonable first-order approximation for $0<f_{\nu}<0.07$" at fixed $(\omega_{\rm m},\Omega_\Lambda)$ [src: Sect. 4.5.7], and is introduced as an approximation to Eq. 143 "for plausible values of $(\omega_{\rm m},N_{\nu},\Omega_{\Lambda})$" [src: Sect. 4.5.6, text before Eq. 144].
- The current CMB mass bound is "mostly a background measurement"; the free-streaming mass is bounded only at $\sum m_\nu^\mathrm{Pert.} < 0.8\,\mathrm{eV}$ (arXiv:2411.14524) [src: abstract].
- A phase shift needs a "mode traveling faster than $c_{\gamma}$" or "non-adiabatic fluctuations" (arXiv:1508.06342) [src: Sect. 2.2]; for adiabatic fluctuations the first "is realized by free-streaming relativistic particles, such as neutrinos or other forms of dark radiation", and "Alternatively, a phase shift can arise from isocurvature fluctuations" [src: abstract]. At leading order $\theta\approx 0.191\pi\,\epsilon_{X}+\mathcal{O}(\epsilon_{X}^{2})\,,$ [src: Eq. 2.67].
- The neutrino phase shift is detected "at about 10σ" with Planck and "roughly 14σ" with ACT and SPT (arXiv:2501.13788) [src: abstract].
- Fluid-like relics give no phase shift and are allowed in larger amounts: $\Delta N_{\rm eff,fld}<0.38$ against $\Delta N_{\rm eff,fs}<0.28$ (Planck 2018 + BAO, 95% C.L., as compiled in arXiv:2203.07943) [src: Table 1].
- The strongly interacting neutrino mode is disfavoured with odds of 5:100000 by DESI DR1 FS + BAO + CMB-SPA (arXiv:2610.26654) [src: abstract].
- Neutrino-decay limits from the $(m/E)^3$ damping rate are superseded: the rate scales as $(m/E)^5$ (arXiv:2011.01502) [src: abstract], with a daughter-mass factor that makes limits "remarkably independent of the parent mass" (arXiv:2203.09075) [src: abstract].
- Cosmology presses on fully thermalised light sterile neutrinos, not on partially populated ones (arXiv:2606.21518) [src: abstract].

## Checks a referee makes
<!-- key: checks-a-referee-makes -->

- The $N_{\rm eff}^{\rm SM}$ baseline of every $\Delta N_{\rm eff}$; instantaneous or full decoupling.
- Spin, $T_F$, $g_\star$ table and reheating assumption for a thermal relic.
- Gauge and potential names; ordering or degenerate masses; fixed parameters in any "effect of the mass"; fluid-approximation accuracy at the scales used.
- Contact limit, flavour structure and posterior multimodality for interactions; the $(m/E)^5$ rate and daughter mass for decays.
- Thermalisation degree and effective versus physical mass for sterile neutrinos. Details: `references/approximations.md`, last section.

## Errors that recur
<!-- key: errors-that-recur -->

- Quoting N_eff^SM = 3.046 as current, or 3.043 as settled (arXiv:2012.02726; arXiv:2402.18481) [src: Sect. 6; abstract].
- Reading $-8f_\nu$ as the ratio of power spectra, as Eq. 144 of arXiv:astro-ph/0603494 prints it, rather than as a fractional change, or using it beyond $f_\nu<0.07$ [src: Sect. 4.5.7].
- Copying a hierarchy between Lesgourgues & Pastor and Ma & Bertschinger without swapping φ and ψ (arXiv:astro-ph/0603494, Eq. 25; arXiv:astro-ph/9506072, Eq. 5). <!-- num: not a value -->
- Treating the phase shift as unbreakable evidence of free streaming in a fit where other parameters move (arXiv:1902.00534) [src: abstract].
- Extrapolating dark-radiation BBN fits to $\Delta N_{\rm eff}<0$ (arXiv:2507.23354) [src: abstract].
- Using pre-2020 invisible-decay limits (arXiv:1907.05425) built on the $(m/E)^3$ rate (arXiv:2011.01502) [src: abstract].
- Assuming a lower neutrino abundance relaxes the mass bound: $T_\nu$ and $\sum m_\nu$ are positively correlated (arXiv:2609.15970) [src: abstract].

## Related skills
<!-- key: related-skills -->

- `thcosmo-lss-perturbation-theory`: massive neutrinos in perturbation theory beyond linear order and in the EFTofLSS (two-home rule).
- `thcosmo-thermal-history`: equilibrium thermodynamics, $g_\star$, Boltzmann equation and BBN networks; here only neutrino decoupling and $N_{\rm eff}$.
- `thcosmo-dark-matter-models`: keV sterile neutrinos and other dark-matter candidates; here only light sterile neutrinos and LiMRs.
- `thcosmo-cmb-physics` and `thcosmo-cosmological-perturbations`: CMB physics and gauge-invariant perturbations in general.
- `thcosmo-tensions-model-building` (planned): the neutrino-mass tension and $H_0$ responses (self-interacting neutrinos, majorons, dark radiation) as model-building questions.
- cosmoskill `cosmo-neutrinos-dark-matter` (measured $\sum m_\nu$ and $N_{\rm eff}$), `cosmo-cmb`, `cosmo-bbn`, `cosmo-tensions-anomalies`.

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

Sizes, in thousands of tokens: L1 4k; approximations 3k; formalism 7k; models 5k; open 2k; results 4k; deep/interacting-neutrino-perturbations 11k; deep/neff-standard-model-calculation 10k; deep/neutrino-mass-below-the-floor 9k.

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
`python3 "${CLAUDE_SKILL_DIR}"/../*theoretical-cosmology/scripts/layers.py thcosmo-neutrinos-light-relics`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. An
override replaces its base section for this researcher: use it, and quote
the base value beside it, both labelled. A suppressed section is left out
and named as suppressed; use it only when the question asks for that
section's own content, and then say that the layer hides it. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[thcosmoskill L<level> · <base, personal, project, or several joined by +> · thcosmo-neutrinos-light-relics/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- thcosmoskill:block:end -->
