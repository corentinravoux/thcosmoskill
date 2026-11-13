# Open questions in baryogenesis, phase transitions and primordial magnetic fields

Scope: live debates with both sides cited, unresolved calculations, what the next data or calculation will decide, forecasts (labelled), and misconceptions and stale claims with the paper that corrects each.

Snapshot: 2026-11-13

## Debates
<!-- key: debates -->

### Is perturbative electroweak baryogenesis still viable?
<!-- key: is-perturbative-electroweak-baryogenesis-still -->
- Against: the electron-EDM bounds "have become so strong that they essentially exclude all models of electroweak baryogenesis that can be treated perturbatively", "it appears" (Bodeker & Buchmuller 2020, arXiv:2009.07294) [src: Sect. III.3, paragraph beginning "Studies of electroweak baryogenesis with two Higgs doublets"]; the washout criterion has tightened to $v/T_c\gtrsim 1.33$ in the minimal 3d EFT, "slightly stronger than previously anticipated" (arXiv:2506.04939) [src: abstract].
- For: the EDM bounds "led to the construction of models, where CP violation in baryogenesis and low-energy CP violation are decoupled", and "in strongly coupled composite Higgs models electroweak baryogenesis is still possible" (arXiv:2009.07294) [src: Sect. III.5]; van de Vis, de Vries & Postma call EWBG "increasingly challenged" and stress that "it is essential to make precise predictions for the baryon asymmetry and the corresponding experimental signatures within specific scenarios" (arXiv:2508.09989) [src: abstract].

### Vev-insertion against semiclassical sources
<!-- key: vev-insertion-against-semiclassical-sources -->
- The vev-insertion source vanishes at leading order in the gradient expansion when the thermal self-energies are included consistently in the kinetic equation, as shown in the work followed by arXiv:2508.09989 (their Refs. [255, 256]) [src: Sect. 3.4.1]; the semiclassical (WKB) force of Eq. 49 of arXiv:2009.07294 is the method implemented in BARYONET (arXiv:2510.21915) [src: abstract]. No paper in this run defends the leading-order VIA source after that result.

### 4d daisy resummation against the 3d EFT
<!-- key: daisy-resummation-against-the-3d-eft -->
- Daisy resummation carries renormalisation-scale uncertainties of "two to three orders-of-magnitude" in the GW peak amplitude, which dimensional reduction "drastically reduces", "pushing it to higher orders" (arXiv:2009.10080) [src: abstract].
- But higher-dimensional operators of the 3d EFT "can substantially modify the predicted transition strength and GW signals", which "indicates a potential breakdown of the high-temperature expansion precisely in the region with the lowest transition temperatures, where the strongest GW signals are expected" (arXiv:2511.14831) [src: abstract].

### Can primordial magnetic fields relieve the Hubble tension?
<!-- key: can-primordial-magnetic-fields-relieve-the -->
- For: with MHD simulations and Lyman-α transfer, non-helical Batchelor-spectrum fields of "approximately 5-10 pico-Gauss" are preferred, "from mild ($\sim 1.8\sigma$ with Planck + DESI) to moderate ($\sim 3\sigma$ with Planck + DESI + SH0ES-calibrated SN) significance" (Jedamzik, Pogosian & Abel 2025, arXiv:2503.09599) [src: abstract, inline].
- Against: in a linearised treatment "for fields with red-tilted spectra", "The clumping factors we find are too small to alleviate outstanding cosmological tensions" (Schiff & Venumadhav 2025, arXiv:2506.16517) [src: abstract]. `[der]` The two analyses assume different spectra (Batchelor against red-tilted), so they do not contradict each other directly. The status of the tension itself belongs to cosmoskill `cosmo-tensions-anomalies` and `thcosmo-tensions-model-building`.

### Non-helical decay of primordial fields
<!-- key: non-helical-decay-of-primordial-fields -->
- Standard decay models make non-helical electroweak relics "too low" for the blazar observations; under the proposed reconnection-controlled decay conserving the helicity fluctuation level they would be "stronger by several orders of magnitude" (arXiv:2203.03573) [src: abstract]; for non-helical fields "there currently exists no definitive theory" (arXiv:2012.01393) [src: abstract].

### Friction on ultra-relativistic walls: $\gamma^1$ or $\gamma^2$
<!-- key: friction-on-ultra-relativistic-walls-gamma-1-or -->
- Bodeker & Moore 2017: transition radiation limits "wall velocities to $\gamma\sim 1/\alpha$" (arXiv:1703.08215) [src: abstract, inline].
- Höche et al. 2020: after leading-log resummation of multiple soft emissions, $P\sim \gamma^2T^4$, "independent of the particle masses, implying a significantly slower terminal velocity than previously suggested" (arXiv:2007.10343) [src: abstract, inline].
- Gouttenoire et al. 2021: pressure "linear both in the Lorentz boost and in the order parameter, up to a log" (arXiv:2112.07686) [src: abstract]. Athron et al. report that this study "recovered the $\gamma^{1}$ scaling", "arguing that the computation in ref. [517] satisfies the Ward identity erroneously, because the presence of the bubble wall breaks four-momentum conservation", and that another study (their Ref. [525]) "noted that the $\gamma^{2}$ friction found in ref. [517] does not vanish in the limit where the heavy particles remain massless"; Athron et al. introduce the $\gamma^{2}$ result with "Controversially" (arXiv:2305.02357) [src: Sect. 5.5.3, paragraph before Eq. 5.68]. No reply by the authors of arXiv:2007.10343 was found in this run.
- `[der]` What decides: a calculation of the soft-emission pressure that both sides accept; the phenomenological friction models are built to accommodate either scaling, $\mathcal{K}\propto h(\gamma)$ with $h=\gamma$ or $\gamma^{2}$ (arXiv:2305.02357) [src: Sect. 5.5.3, text after Eq. 5.69].

## Unresolved calculations
<!-- key: unresolved-calculations -->

- **Wall velocity.** State-of-the-art calculations carry "several $O(1)$ uncertainties" (arXiv:2510.27691) [src: abstract]; the ultra-relativistic friction scaling is disputed (debate above).
- **Percolation in an expanding universe.** "To our knowledge, a percolation study has not been performed in expanding spacetime" (arXiv:2305.02357) [src: Sect. 4.7.2, text after Eq. 4.66].
- **Sound-wave lifetime and length scale.** The timescales "are only approximately estimated, they may contribute significantly to the uncertainty in GW predictions"; "we currently lack a reasonable estimate of the splitting between longitudinal and rotational components for use in non-lattice studies" (arXiv:2305.02357) [src: Sect. 5.4, text after Eq. 5.40]. The resulting spectra and the suppression factor are in `thcosmo-cosmological-gravitational-waves` (`deep/phase-transition-spectra.md`).
- **Sphaleron conversion across the crossover** (computed in 2026). Equilibrium conversion factors at fixed temperature neglect the variation of the Higgs value and of the rate across the crossover (arXiv:2609.07467) [src: abstract].
- **Leptogenesis beyond Boltzmann.** The RIS subtraction was historically wrong (arXiv:2009.07294) [src: Sect. IV.2, footnote 18]; quantum kinetic equations for ARS come from two approaches, the Hamiltonian time evolution and the closed-time-path technique, whose relations that review discusses (arXiv:1711.02862) [src: abstract].

## What the next data and calculations decide
<!-- key: what-the-next-data-and-calculations-decide -->

- **EDMs and the LHC.** Bodeker & Buchmuller underline "the importance of searching for new heavy resonances and deviations from SM predictions for Higgs couplings in the next run of the LHC" (arXiv:2009.07294) [src: Sect. III.5]; "The developing experimental programs will play a crucial role in either falsifying or detecting the new physics responsible for electroweak baryogenesis" (arXiv:2508.09989) [src: abstract].
- **Gravitational waves** from a first-order transition (LISA band for the electroweak scale) test the transition; forecasts and templates are in `thcosmo-cosmological-gravitational-waves`.
- **CMB and magnetic fields. Forecast:** "Future high-resolution CMB temperature and polarization measurements will be crucial for confirming or further constraining PMFs at recombination" (arXiv:2503.09599) [src: abstract].
- **Baryon isocurvature** constrains Affleck–Dine (arXiv:2602.08781) [src: abstract].
- **Birefringence:** "The minimal setup predicts a positive birefringence angle, consistent with the CMB hint" (arXiv:2609.25202) [src: abstract]; `[der]` a confirmed isotropic rotation of either sign would test this axiogenesis model. **Forecast.**
- **IGMF detection:** an analysis is quoted as "recent $3.8\sigma$ evidence for a non-zero intergalactic magnetic field from anisotropic pair-halo searches using Fermi-LAT data" in arXiv:2604.20768 [src: abstract]; the primary analysis was not read in this run.

## Stale claims and misconceptions
<!-- key: stale-claims-and-misconceptions -->

- "The Standard-Model electroweak transition is first order": it is a crossover for Higgs masses above an endpoint "most likely $m_{H,c} \approx 80$ GeV" (arXiv:hep-ph/9605288) [src: abstract, inline], with $T_c=(159\pm1)$ GeV (arXiv:1404.3565) [src: abstract, inline].
- "Magnetic fields from bubbles of a first-order QCD transition": the transition is "an analytic crossover" (arXiv:hep-lat/0611014) [src: abstract], so these scenarios "need to be re-examined" (arXiv:2010.10525) [src: Sect. III.2].
- "Friction vanishes in local thermal equilibrium": the LTE friction $p_{\text{fr}}=\vert\Delta\{(\gamma^2-1)Ts\}\vert$ is "contrary to the long-held expectation of vanishing friction in local thermal equilibrium" (arXiv:2305.02357) [src: Sect. 5.5.3, text after Eq. 5.63]; an earlier "$\gamma^{2}$ scaling" of LTE friction is called "(misleading)" [src: Sect. 5.5.3, text after Eq. 5.63].
- "$v_w$ can be set to the Chapman–Jouguet speed": "fixing $v_{w}=v_{\text{CJ}}$ is an arbitrary choice" (arXiv:2305.02357) [src: Sect. 5.5.2, text after Eq. 5.52].
- "EWBG needs subsonic walls": quoted from its Ref. [111], "It was found, contrary to common lore, that baryogenesis with $v_{\rm w}$ larger than the speed of sound is possible" (arXiv:2009.07294) [src: Sect. III.2, paragraph after Fig. 5].
- "$v_c/T_c\gtrsim 1$ guarantees no washout": the criterion is gauge-dependent and rough (arXiv:2508.09989) [src: Sect. 5.4]; the lattice-based criterion in the minimal 3d EFT is $v/T_c\gtrsim 1.33$ (arXiv:2506.04939) [src: abstract].
- "Nucleation when $S(T(t_{n}))\sim 140,$" (arXiv:2305.02357) [src: Eq. 4.61]: valid "only at the electroweak scale and during the radiation dominated era" (arXiv:2305.02357) [src: Sect. 4.7.1, inline, text after Eq. 4.61].
- "Leading-log collision integrals are conservative for $v_w$": they "underestimate the friction" (arXiv:2305.02357) [src: Sect. 5.5.3, text after Eq. 5.65].

## Not verified
<!-- key: not-verified -->

- No reply to the Ward-identity critique of arXiv:2007.10343 was searched for beyond the citing literature surfaced by date-sorted searches.
- The primary paper of the $3.8\sigma$ IGMF claim and the JILA electron-EDM paper were not read. <!-- num: not a value -->
