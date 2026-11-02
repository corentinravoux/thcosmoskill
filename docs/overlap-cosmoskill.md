# Overlap with cosmoskill

Plan v2, stage 3, step P6 (decisions D9 and D29). Equations and definitions
that the pilot `thcosmo-lss-perturbation-theory` shares with cosmoskill
1.0.3, and which suite is their home. Written 2026-10-31 from the section
lists of both skills; refreshed each time a theory domain that overlaps
cosmoskill is built.

**Rule (D9).** The theory suite holds the formalism: derivations, kernels,
counterterms, bias bases and their relations, RSD models as theory.
cosmoskill holds what each survey analysis adopts and how it is fitted to
data. cosmoskill 1.0.3 is a released, standalone package: its existing
sections stay as they are, so that it still answers without thcosmoskill;
they gain a pointer to the home section here. A statement present in both
is checked for agreement when either side is refreshed.

## `cosmo-theory-foundations`

| cosmoskill section (key) | Shared with the pilot | Home | Action |
|---|---|---|---|
| `physics-and-methods#redshift-space-distortions-kaiser-fingers-of` (§8: Kaiser, dispersion models, TNS, streaming) | `formalism#redshift-space-distortions`; `models#tns-model` | thcosmoskill for the models as theory; cosmoskill for the survey use | pointer added in cosmoskill 1.0.4 |
| `physics-and-methods#perturbation-theory-and-eftoflss-ingredients` (§9: one-loop structure, counterterms, IR resummation, AP mapping, code differences) | `formalism#standard-perturbation-theory-equations-and`, `#effective-field-theory-stress-tensor`, `#infrared-resummation` | thcosmoskill for the derivations; cosmoskill for the AP mapping and the code-level choices of survey analyses | pointer added in cosmoskill 1.0.4 |
| `physics-and-methods#bias-expansions` (§10: Eulerian basis, equivalent bases, co-evolution conversions between codes) | `formalism#bias-expansion`; `models#eulerian-bias-expansion-in-the-galileon-basis` | thcosmoskill for the bases and their relations; cosmoskill for the conversions used between survey codes | pointer added in cosmoskill 1.0.4 |
| `physics-and-methods#halo-model` (§11) | none in the pilot | `thcosmo-nonlinear-structure` (planned) | revisit when built |
| `deep/eft-perturbation-theory` (derivation of F_n, one-loop, counterterm, Lagrangian route, two loops) | the pilot's formalism and models | thcosmoskill once the pilot's dossiers exist (stage 3, P7) | pointer added in cosmoskill 1.0.4 |

## `cosmo-galaxy-clustering`

| cosmoskill section | Shared with the pilot | Home | Action |
|---|---|---|---|
| `deep/full-shape-modelling` (what is fitted, nuisance priors, ShapeFit, codes, scale cuts) | the one-loop model and bias parametrisation it uses | cosmoskill: this is analysis practice | none; the pilot points to it for fits to data |

## Known shared slips

Both suites record, as printed slips with no published correction, the
redshift-space kernel slip of arXiv:1909.05277 Eq. A.1 (cosmoskill,
`cosmo-theory-foundations` errors that recur) and the slips of
arXiv:2212.08488 Eqs. 28, 32 and 39 (thcosmoskill, hub
`references/stale-claims.md`).
