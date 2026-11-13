---
name: thcosmo-baryogenesis-phase-transitions
description: Use when deriving, checking or reviewing theory of the baryon asymmetry or early-universe phase transitions — Sakharov conditions, sphaleron rate and B-L conversion, electroweak baryogenesis (CP sources, washout v/T, EDM status), leptogenesis (Davidson-Ibarra, flavour, resonant, ARS), Affleck-Dine, electroweak and QCD crossovers, effective potential and 3d EFT, bounce and nucleation, beta/H, percolation, wall velocity and friction, primordial magnetogenesis and MHD decay.
---

# Baryogenesis, phase transitions and primordial magnetic fields — expert reference

Snapshot 2026-11-13. Every equation and number names its paper and
the place it was read; no equation or number is derived by an agent.
Conventions: natural units; each source keeps its own signature and Planck-mass symbol (table in `references/formalism.md`, and the hub's `references/conventions.md`). Re-read the cited paper before
an equation or a number enters a manuscript.

## File map
<!-- key: file-map -->

| Question | Load |
|---|---|
| Conventions of the main sources; anomaly, sphaleron rate and $B$–$(B-L)$ conversion; effective potential, thermal functions, daisy and 3d EFT; bounce, rate prefactor, $P_f$, nucleation, percolation and completion, $\beta_*$ and $R_{\rm sep}$; wall pressure, LTE and ultra-relativistic friction; EWBG force and washout; leptogenesis kinetic equations; Affleck–Dine toy model; magnetic-field statistics, generation and MHD decay | `references/formalism.md` |
| One card per mechanism: EWBG, SMEFT $\phi^6$, thermal, flavoured, resonant and ARS leptogenesis, Affleck–Dine, GUT, spontaneous baryogenesis and axiogenesis, magnetogenesis at the electroweak, QCD and BSM transitions and during inflation; their status | `references/models.md` |
| Observed $\eta_B$ as quoted; Standard-Model crossover, sphaleron rate, freeze-out and conversion factor; QCD crossover; washout criterion; wall velocities and friction results; Davidson–Ibarra and neutrino-mass bounds; magnetic-field bounds and decay; history of key results | `references/results.md` |
| Validity of the perturbative potential, nucleation milestones, LTE and fluid ansatz, transport (WKB, VIA), leptogenesis kinetic equations, MHD decay laws; convention traps and printed slips; referee checklist | `references/approximations.md` |
| Viability of EWBG, VIA against WKB, 4d against 3d EFT, $\gamma$ against $\gamma^2$ friction, magnetic fields and the Hubble tension, non-helical decay; unresolved calculations; what next data decide; stale claims | `references/open-questions.md` |
| Bibliography with versions read; subtopics and where they come from | `references/sources.tsv`, `references/subtopics.tsv` |

## What an expert holds in mind
<!-- key: what-an-expert-holds-in-mind -->

- Sakharov's three conditions, and "after an inflationary phase one cannot have $B\neq 0$ as an initial condition of the hot early Universe" (arXiv:2009.07294) [src: Sect. II.1].
- Anomaly $\partial_{\mu}J_{B}^{\mu}=\frac{n_{f}}{32\pi^{2}}g^{2}F^{a}_{\mu\nu}\widetilde{F}^{a\mu\nu},$ (arXiv:2009.07294) [src: Eq. 3], so $B-L$ is conserved; with all Yukawas in equilibrium above the electroweak transition and, "For simplicity", family-independent lepton chemical potentials, $B=c_{s}(B-L)\ ,\quad L=(c_{s}-1)(B-L)\ ,$ [src: Eq. 39], $c_{s}=(8n_{f}+4)/(22n_{f}+13)$ [src: Sect. II.3, text after Eq. 39]; across the crossover "$C_\text{sph} = 0.3328(5)$ for $B-L$" (arXiv:2609.07467) [src: abstract].
- Standard Model: no electroweak phase transition but a crossover "sharply defined at $T_c = (159\pm 1)$ GeV", symmetric-phase rate $\Gamma/T^4 = (18\pm 3)\alpha_W^5$, sphaleron freeze-out $T_* = (131.7\pm 2.3)$ GeV (arXiv:1404.3565) [src: abstract, inline]; the QCD transition is "an analytic crossover" (arXiv:hep-lat/0611014) [src: abstract].
- Washout: the rough $\frac{v_{n}}{T}\gtrsim 1.$ (arXiv:2508.09989) [src: Eq. 5.17] is gauge-dependent; the lattice criterion is $x(T_c) \lesssim 0.025$, i.e. "$v/T_c \gtrsim 1.33$" in the minimal SU(2)+Higgs 3d EFT (arXiv:2506.04939) [src: abstract].
- Daisy-resummed 4d potentials carry "two to three orders-of-magnitude uncertainty in the peak gravitational wave amplitude"; the 3d EFT "drastically reduces this scale dependence" (arXiv:2009.10080) [src: abstract], but its higher-dimensional operators indicate "a potential breakdown of the high-temperature expansion precisely in the region with the lowest transition temperatures" (arXiv:2511.14831) [src: abstract].
- Milestones: nucleation $N(t_{n})=\frac{4\pi}{3}\int_{t_{c}}^{t_{n}}dt\,\frac{\Gamma(T(t))P_{f}(t)}{H^{3}(t)}=1,$ (arXiv:2305.02357) [src: Eq. 4.58]; percolation $P_{f}(t_{p})\approx 0.71.$ [src: Eq. 4.62]; the action criterion $S(T(t_{n}))\sim 140,$ [src: Eq. 4.61] holds only "at the electroweak scale and during the radiation dominated era" [src: Sect. 4.7.1, inline, text after Eq. 4.61].
- $\beta_{*}=-\left.\derivative{S}{t}\right|_{t_{*}}.$ (arXiv:2305.02357) [src: Eq. 5.47] assumes a fast transition; for an exponential rate, neglecting the expansion of space, $R_{\text{sep}}\approx(8\pi)^{\frac{1}{3}}\frac{v_{w}}{\beta_{*}},$ [src: Eq. 5.49], "Strictly speaking" obtained where "$P_{f}=1/e$" [src: Sect. 5.4, text after Eq. 5.49], modified to $R_{\text{sep}}\approx(8\pi)^{\frac{1}{3}}\frac{\max(v_{w},c_{s,f})}{\beta_{*}}.$ [src: Eq. 5.50] in its Ref. [10]; the review recommends $L_*=R_{\rm sep}$ "because the hydrodynamic simulations that provide GW fits calculate $R_{\text{sep}}$" [src: Sect. 5.4, inline, text before Eq. 5.46], with $R_{\text{sep}}(t)=n(t)^{-\frac{1}{3}}.$ [src: Eq. 5.41].
- Wall velocity: "near the speed of sound or are ultra-relativistic with $\gamma\gtrsim 10$" in the real scalar singlet model, as quoted by Athron et al. from their Ref. [514] (arXiv:2305.02357) [src: Sect. 5.5.3]; state-of-the-art calculations carry "several $O(1)$ uncertainties" (arXiv:2510.27691) [src: abstract]; the LTE fit gives "a rough upper bound" (arXiv:2305.02357) [src: Sect. 5.5.3, paragraph beginning "The predicted value of $v_{w}$ from (5.64)"].
- Ultra-relativistic friction at leading order $p_{\text{fr}}^{\text{LO}}(t)=\sum_{j}c_{j}g_{j}\frac{\Delta m_{j}^{2}T^{2}}{24},$ (arXiv:2305.02357) [src: Eq. 5.67]; in extensions with extra scalars, transition radiation limits walls to "$\gamma\sim 1/\alpha$" (arXiv:1703.08215) [src: abstract, inline]; the $\gamma^1$ against $\gamma^2$ scaling at higher order is disputed (arXiv:2007.10343; arXiv:2112.07686) [src: abstract].
- EWBG: perturbative models are "essentially" excluded by electron-EDM bounds, "it appears" (arXiv:2009.07294) [src: Sect. III.3]; the leading-order vev-insertion source vanishes when thermal self-energies are included consistently, as shown in the work that review follows (arXiv:2508.09989) [src: Sect. 3.4.1].
- Leptogenesis: $\eta_{B}=\frac{n_{B}}{n_{\gamma}}=\frac{3}{4}\frac{c_{s}}{f}\varepsilon\kappa_{\text{f}}\simeq\eta_{B}\simeq 0.96\times 10^{-2}\varepsilon\kappa_{\text{f}}\ .$ (arXiv:2009.07294) [src: Eq. 104] (as printed); Davidson–Ibarra, "For a hierarchical spectrum of right-handed neutrinos", with $m_{\nu_3}=\sqrt{\Delta m^2_{\rm atm}}$ and thermal $\nu_R$ production, find $T_{\rm reh}>M_{\nu_R}>10^8$ GeV; "Reasonable estimates of nu_R production and the subsequent washout of the asymmetry, as made by Buchmuller and Plumacher, imply" $M_{\nu_R} > 10^9$ GeV (arXiv:hep-ph/0202239) [src: abstract]; light-neutrino window, "Assuming" m̃₁ = O(m_i) (arXiv:2009.07294) [src: Sect. IV.3.1, text before Eq. 111], $10^{-3}\lesssim m_{i}\lesssim 0.1~\text{eV}\ .$ [src: Eq. 111], type-I seesaw only.
- Flavour matters below $T_{\tau}\sim 10^{12}$ GeV (arXiv:2009.07294) [src: Sect. IV.3.2, text after Eq. 115]; resonant leptogenesis works "even as light as about 1 TeV" (arXiv:hep-ph/0309342) [src: abstract].
- Inflationary magnetogenesis with $f^2F^2$: strong coupling for the scale-invariant case (arXiv:1303.7121) [src: Sect. 3.1.1, text after Eq. 50] and, "Assuming that back reaction does not spoil inflation", seeds that "recalculated to the present epoch cannot exceed $10^{-32}G$ in $Mpc$ scales" (arXiv:0907.1030) [src: abstract].
- MHD decay (freely decaying, "vanishing velocity field at the initial time" [src: Sect. IV.1]): the peak wavenumber, "determined by simulations" in the helical case [src: text before Eq. 77], falls as $k_{\rm in}(\eta)\sim k_{\rm in}(\eta_{0})\left(\frac{\eta_{0}}{\eta}\right)^{2/3},\ \ {\rm helical\ case}$ (arXiv:2010.10525) [src: Eq. 77], against $k_{\rm in}(\eta)\propto\eta^{-1/2},\ \ {\rm nonhelical\ case}.$ [src: Eq. 72]; under the proposed reconnection-controlled decay, non-helical electroweak relics "would be stronger by several orders of magnitude" (arXiv:2203.03573) [src: abstract].

## Checks a referee makes
<!-- key: checks-a-referee-makes -->

- Non-perturbative or 3d-EFT evidence for a first-order transition; scale and gauge dependence shown.
- Which temperature ($T_n$, $T_p$, $T_f$); percolation in supercooled cases; validity of the linear $\beta$.
- How $v_w$ was obtained; no $v_w=v_{\rm CJ}$ by default. <!-- eq: notation -->
- EWBG: lattice washout criterion, semiclassical source, EDM constraints. Leptogenesis: flavour regime, initial abundance, $\Delta L=2$ washout, seesaw type. <!-- num: not a value --> <!-- eq: notation -->
- Affleck–Dine: baryon isocurvature. Magnetogenesis: backreaction, strong coupling, helicity, decay law, field-strength definition. Details: `references/approximations.md`, last section.

## Errors that recur
<!-- key: errors-that-recur -->

- Treating the Standard-Model electroweak or QCD transition as first order (arXiv:hep-ph/9605288; arXiv:hep-lat/0611014) [src: abstract].
- Using $v_c/T_c\gtrsim 1$ as gauge-independent and sufficient; the 3d-EFT lattice value is $1.33$ for the discontinuity of the condensate (arXiv:2506.04939) [src: abstract].
- Using the action criterion $S(T(t_{n}))\sim 140,$ (arXiv:2305.02357) [src: Eq. 4.61] outside the electroweak scale and the radiation era, or where the action minimum lies above it [src: Sect. 4.7.1, text after Eq. 4.61].
- Dropping the $\int dz\,(dT/dz)\,\partial V/\partial T$ term of the friction by assuming $\text{d}T/\text{d}z=0$ (arXiv:2305.02357) [src: Sect. 5.5.3, inline, text after Eq. 5.61]; quoting zero friction in LTE (arXiv:2305.02357) [src: Sect. 5.5.3, text after Eq. 5.63].
- Applying the LTE wall velocity to ultra-relativistic walls, where LTE "is not reasonable when $\gamma\gg 1$" (arXiv:2305.02357) [src: Sect. 5.5.3].
- Applying the neutrino-mass bound from leptogenesis outside the type-I seesaw (arXiv:2009.07294) [src: Sect. IV.3.1, text after Eq. 111]; using the old RIS subtraction (arXiv:2009.07294) [src: Sect. IV.2, footnote 18].
- Opposite $R_\xi$ conventions for the Landau gauge (arXiv:2305.02357) [src: Sect. 2.2.2, footnote 7].
- Copying printed slips: Eq. 104 of arXiv:2009.07294, Eq. 5.61 of arXiv:2305.02357, the text after Eq. 2.25 of arXiv:2508.09989, the text after Eq. 69 of arXiv:hep-ph/0303065 (see `approximations.md`). <!-- num: not a value -->

## Related skills
<!-- key: related-skills -->

- `thcosmo-cosmological-gravitational-waves`: GW spectra from transitions, the parameters $\alpha$, $\kappa$, $K$ as they enter the templates, and how the sound-wave spectrum is derived (`deep/phase-transition-spectra.md`); here only the transition dynamics.
- `thcosmo-pbh-defects` (planned): PBHs from false-vacuum remnants and supercooled transitions, cosmic strings from $B-L$ breaking.
- `thcosmo-neutrinos-light-relics`: light-neutrino physics; `thcosmo-dark-matter-models`: asymmetric dark matter and sterile-neutrino dark matter; `thcosmo-inflation`: the inflationary background of Affleck–Dine and inflationary magnetogenesis.
- `thcosmo-thermal-history` (planned): equilibrium thermodynamics and $g_*$; `thcosmo-tensions-model-building` (planned): magnetic fields and the Hubble tension.
- cosmoskill: `cosmo-cmb` and `cosmo-bbn` (measured $\eta_B$, CMB limits on magnetic fields), `cosmo-neutrinos-dark-matter` ($\sum m_\nu$), `cosmo-inflation-primordial` (isocurvature, birefringence), `cosmo-early-universe-exotica` (measured GW backgrounds).

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

Sizes, in thousands of tokens: L1 5k; approximations 6k; formalism 14k; models 7k; open 3k; results 6k.

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
`python3 "${CLAUDE_SKILL_DIR}"/../*theoretical-cosmology/scripts/layers.py thcosmo-baryogenesis-phase-transitions`
and read what it prints before answering. A note applies when its subject is
the question's; you need not open the section it is attached to. An
override replaces its base section for this researcher: use it, and quote
the base value beside it, both labelled. A suppressed section is left out
and named as suppressed; use it only when the question asks for that
section's own content, and then say that the layer hides it. Say which
statements come from a local layer.

End the answer with one line, `<file>` being `skill` for this file or the
name of the reference file without extension:
`[thcosmoskill L<level> · <base, personal, project, or several joined by +> · thcosmo-baryogenesis-phase-transitions/<file>#<key>]`
The key is the comment under the heading of the section used; leave `#<key>`
out if you did not read that heading. At L4, put the paper and the place
read instead: `arXiv:<id>, <abstract or section>`.
<!-- thcosmoskill:block:end -->
