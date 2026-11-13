# Models of baryogenesis, first-order transitions and magnetogenesis

Scope: the model landscape, one card per model or class, chosen by literature weight in the reviews of Bodeker & Buchmuller (arXiv:2009.07294), Athron et al. (arXiv:2305.02357), Elor et al. (arXiv:2203.05010), Vachaspati (arXiv:2010.10525) and Durrer & Neronov (arXiv:1303.7121) and in the 2025–2026 literature. Formalism in `formalism.md`; model-independent results in `results.md`; gravitational-wave spectra in `thcosmo-cosmological-gravitational-waves`.

Snapshot: 2026-11-13

## Electroweak baryogenesis and first-order electroweak transitions
<!-- key: electroweak-baryogenesis-and-first-order -->

### Electroweak baryogenesis (class)
<!-- key: electroweak-baryogenesis-class -->
- **Defining equations:** the semiclassical CP-violating force $F_{z}=-\frac{\left(|m|^{2}\right)^{\prime}}{2E}+s\left[\frac{\left(|m|^{2}\theta^{\prime}\right)^{\prime}}{2EE_{z}}-\frac{|m|^{2}\left(|m|^{2}\right)^{\prime}\theta^{\prime}}{4E^{3}E_{z}}\right]\ ,$ (Bodeker & Buchmuller 2020, arXiv:2009.07294) [src: Eq. 49], transport equations and the weak sphaleron rate; formalism in `formalism.md`. The idea goes back to Kuzmin, Rubakov & Shaposhnikov 1985 (doi:10.1016/0370-2693(85)91028-7), not read here.
- **Parameters:** strength of the transition $v_n/T_n$ (or $x(T_c)$ in the 3d EFT), wall velocity $v_w$ and width $\ell_w$, CP-violating phase in the wall.
- **Predictions:** an asymmetry "directly proportional to the weak-sphaleron rate in the symmetric phase", a lepton asymmetry "of the same order of magnitude as the baryon asymmetry" (arXiv:2009.07294) [src: Sect. III.2]; supersonic walls are not excluded: "contrary to common lore, that baryogenesis with $v_{\rm w}$ larger than the speed of sound is possible, and that the generated asymmetry smoothly decreases with increasing $v_{\rm w}$", quoted from its Ref. [111] [src: Sect. III.2, paragraph after Fig. 5]. A gravitational-wave background from the same transition: `thcosmo-cosmological-gravitational-waves`.
- **Consistency:** in the Standard Model the transition is a crossover, so "Sakharov's third condition is not satisfied" (arXiv:2009.07294) [src: Sect. III.1, text after Eq. 47]. The vev-insertion source used in part of the literature vanishes "at leading order in the gradient expansion (but to all orders in the VIA expansion)", as shown in the references followed by van de Vis, de Vries & Postma (their Refs. [255, 256]) (arXiv:2508.09989) [src: Sect. 3.4.1]; reply: none found in this run (see `open-questions.md`).
- **Observational status:** the electron EDM bounds "essentially exclude all models of electroweak baryogenesis that can be treated perturbatively", "it appears" (arXiv:2009.07294) [src: Sect. III.3, paragraph beginning "Studies of electroweak baryogenesis with two Higgs doublets"]; "scenarios of electroweak baryogenesis are increasingly challenged by results from contemporary experiments" (arXiv:2508.09989) [src: abstract]; "The current best limit on the electron EDM comes from the HfF+ JILA experiment", their Ref. [363] [src: Sect. 6.1.1]. Ways out named by Bodeker & Buchmuller: models in which "CP violation in baryogenesis and low-energy CP violation are decoupled, and the electroweak phase transition takes place at temperatures well above a TeV", and "strongly coupled composite Higgs models" [src: Sect. III.5].
- **Status date:** 2026-11-13

### SMEFT with a $(\varphi^\dagger\varphi)^3$ operator
<!-- key: smeft-with-a-varphi-dagger-varphi-3-operator -->
- **Defining equations:** ${\cal L}_{\rm SMEFT}={\cal L}_{\rm SM}+\sum_{i}\frac{c_{i}\mathcal{O}_{i}}{\Lambda^{d_{i}-4}}\,.$ (arXiv:2508.09989) [src: Eq. 2.24]; with only $\mathcal{O}_{\varphi}=(\varphi^{\dagger}\varphi)^{3}/\Lambda^{2}$, $V_{\rm SMEFT}=\frac{1}{2}a_{2}\phi^{2}+\frac{1}{4}a_{4}\phi^{4}+\frac{1}{6}a_{6}\phi^{6}=-\frac{1}{4}(m_{h}^{2}-2a_{6}v^{4})\phi^{2}+\frac{1}{4}\left(\frac{m_{h}^{2}}{2v^{2}}-2a_{6}v^{2}\right)\phi^{4}+\frac{1}{8}a_{6}\phi^{6}\,,$ [src: Eq. 2.25], $a_{6}=3/(4\Lambda^{2})$; the text after it prints "$m_{h}^{2}=125$ GeV" for the Higgs mass, as printed [src: Sect. 2.3.5, text after Eq. 2.25].
- **Parameters:** the cutoff $\Lambda$ only.
- **Predictions:** "a FOPT is possible for cutoffs in the 600 - 1000 GeV range", as found in their Ref. [210] (arXiv:2508.09989) [src: Sect. 2.3.5, text after Eq. 2.25].
- **Consistency:** "despite appearances, there is no hierarchy of scales", as pointed out in their Refs. [28, 209, 213, 214] (arXiv:2508.09989) [src: Sect. 2.3.5]; truncation effects of the high-temperature EFT are discussed in arXiv:2511.14831 [src: abstract]. <!-- num: not a value -->
- **Observational status:** not assessed in the sources read.
- **Status date:** 2026-11-13

## Leptogenesis
<!-- key: leptogenesis -->

### Thermal leptogenesis in the type-I seesaw (hierarchical $N_i$)
<!-- key: thermal-leptogenesis-in-the-type-i-seesaw -->
- **Defining equations:** kinetic equations $\begin{split}\frac{dN_{N}}{dz}&=-D(N_{N}-N_{N}^{\text{eq}})\ ,\\ \frac{dN_{B-L}}{dz}&=-\varepsilon D(N_{N}-N^{\text{eq}})-WN_{B-L}\ .\end{split}$ (Bodeker & Buchmuller 2020, arXiv:2009.07294) [src: Eq. 102]; proposed by Fukugita & Yanagida 1986 (doi:10.1016/0370-2693(86)91126-3), not read here.
- **Parameters:** $M_1$, $\varepsilon_1$, $\widetilde m_1$, $\overline m$; initial $N_1$ abundance.
- **Predictions:** $\eta_{B}\sim 10^{-2}\ \varepsilon_{1}\kappa_{f}\sim 10^{-10}\cdots 10^{-8}\ ,$ (arXiv:2009.07294) [src: Eq. 113], introduced for "GUTs with hierarchical heavy right-handed neutrinos" by "a simple estimate yields the right order of magnitude for the baryon-to-photon ratio [88, 91]", for "$M_{1}/M_{3}\sim 10^{-5}\cdots 10^{-4}$" and "$\kappa_{f}\sim 10^{-2}\cdots 10^{-1}$" [src: Sect. IV.3.1, text before Eq. 113]; light-neutrino mass window and $M_1$ bounds in `results.md`. "The generated $B-L$ asymmetry strongly depends on neutrino parameters, and it is noteworthy that for masses and mixings consistent with neutrino oscillations the observed baryon-to-photon ratio is naturally obtained" [src: Sect. IV.3.1, text after Fig. 15].
- **Consistency:** with the reheating temperature it implies, $T_{reh} > 10^{10}$ GeV, "Implications for the gravitino problem are also discussed" (arXiv:hep-ph/0202239) [src: abstract, inline].
- **Observational status:** not directly testable at the seesaw scale `[der]`; the cosmological bound on $\sum m_\nu$ "is consistent with this mass window" (arXiv:2009.07294) [src: Sect. IV.3.1, text after Eq. 111]; the measured bound is in cosmoskill `cosmo-neutrinos-dark-matter`.
- **Status date:** 2026-11-13

### Flavoured leptogenesis
<!-- key: flavoured-leptogenesis -->
- **Defining equations:** the two-flavour equations of Eq. 117 of arXiv:2009.07294 [src: Eq. 117], valid below $T_\tau\sim 10^{12}$ GeV [src: Sect. IV.3.2, text after Eq. 115]; density-matrix equations far below $T_\tau$. <!-- num: not a value -->
- **Parameters:** projections $p_{\tau}=|C_{1\tau}|^{2}\ ,\quad p_{\tau^{\perp}}=1-|C_{1\tau}|^{2}\ ,\quad\langle\tau|\tau^{\perp}\rangle=0\ ,$ (arXiv:2009.07294) [src: Eq. 116] and flavoured CP asymmetries.
- **Predictions:** a $B-L$ asymmetry with the flavour structure $N_{B-L}\propto\left(\frac{\varepsilon_{\tau\tau}}{p_{\tau\tau}}+\frac{\varepsilon_{\tau^{\perp}\tau^{\perp}}}{p_{\tau^{\perp}\tau^{\perp}}}\right)\propto\varepsilon_{\tau\tau}\left(\frac{1}{p_{\tau\tau}}-\frac{1}{1-p_{\tau\tau}}\right)\ .$ (arXiv:2009.07294) [src: Eq. 118]; a lower leptogenesis scale with tuning (`results.md`).
- **Consistency:** none found among the sources read.
- **Observational status:** not assessed in the sources read.
- **Status date:** 2026-11-13

### Resonant leptogenesis
<!-- key: resonant-leptogenesis -->
- **Defining equations:** nearly degenerate heavy Majorana neutrinos "that have mass differences comparable to their decay widths" (Pilaftsis & Underwood 2003, arXiv:hep-ph/0309342) [src: abstract]; equations not transcribed here.
- **Parameters:** heavy masses and their splitting, Yukawa couplings.
- **Predictions:** viable "with heavy Majorana neutrinos even as light as about 1 TeV" [src: abstract].
- **Consistency:** the subtraction of real intermediate states is addressed in the same paper [src: abstract]; the widely used prescription of Kolb–Wolfram and Harvey et al. "turned out to be incorrect, as observed by Giudice et al." (arXiv:2009.07294) [src: Sect. IV.2, footnote 18].
- **Observational status:** "In principle, searches for CP asymmetries in rare $W$-boson decays can test low-scale leptogenesis in the GeV-scale type-I seesaw with three quasi-degenerate-in-mass heavy right-handed neutrinos" (Fortin et al. 2026, arXiv:2610.24063) [src: abstract, first sentence]; the rest of that paper was not read. **Forecast.**
- **Status date:** 2026-11-13

### Leptogenesis from sterile-neutrino oscillations (ARS)
<!-- key: leptogenesis-from-sterile-neutrino-oscillations -->
- **Defining equations:** lepton asymmetries "produced through the CP-violating oscillations of 'sterile' (electroweak singlet) neutrinos", communicated to ordinary leptons through Yukawa couplings and reprocessed by sphalerons (Akhmedov, Rubakov & Smirnov 1998, arXiv:hep-ph/9803255) [src: abstract]; quantum kinetic equations from Hamiltonian evolution or the closed-time-path formalism (Drewes et al. 2017, arXiv:1711.02862) [src: abstract].
- **Parameters:** right-handed neutrinos "at the electroweak scale or below" (arXiv:1711.02862) [src: abstract], mixings, initial conditions.
- **Predictions:** "the observed value of baryon asymmetry can be generated in this way" with no physics beyond the singlet neutrinos (arXiv:hep-ph/9803255) [src: abstract]. In the $\nu$MSM, "The observed baryon asymmetry requires lepton chemical potentials $\mu_{\alpha}/T\sim 10^{-10}$ at $T\sim T_{\rm EW}$", the lightest sterile neutrino being dark matter "in the range $1<M_{1}\lesssim 50$ keV" and "the scenario predicts that the lightest neutrino mass effectively vanishes ($m_{1}\simeq 0$)" (arXiv:2009.07294) [src: Sect. IV.4, inline].
- **Consistency:** none found among the sources read.
- **Observational status:** parameter space charted for two right-handed neutrinos in arXiv:1711.02862 [src: abstract]; laboratory searches are out of scope.
- **Status date:** 2026-11-13

## Affleck–Dine and other mechanisms
<!-- key: affleck-dine-and-other-mechanisms -->

### Affleck–Dine baryogenesis
<!-- key: affleck-dine-baryogenesis -->
- **Defining equations:** a complex scalar carrying baryon number with $B$-violating interactions, CP-violating "For general complex $\epsilon$ and $\delta$", ${\cal L}_{I}=\lambda|\phi|^{4}+\epsilon\phi^{3}\phi^{*}+\delta\phi^{4}+c.c.$ (Dine & Kusenko 2003, arXiv:hep-ph/0303065) [src: Eq. 65]; in supersymmetry, the condensate is made of "linear combinations of the squark and slepton fields" [src: Sect. III.5]; original proposal Affleck & Dine 1985 (doi:10.1016/0550-3213(85)90021-5).
- **Parameters:** initial amplitude $\phi_o$, mass $m$ ("With supersymmetry in mind, we will think of $m$ as of order $M_{W}$" in the toy model of Sect. III.2), the operator lifting the flat direction, reheating temperature.
- **Predictions:** $n_B$ of Eq. 73 of arXiv:hep-ph/0303065; in the inflationary picture the review adopts in Sect. III.5, the baryon number "develops classically" and "is frozen once $H\sim m_{3/2}$" [src: Sect. III.5, inline]; the review treats the fragmentation of the condensate into Q-balls and B-balls as dark matter in its Sects. III.6.2–III.6.5 (section titles only were read). Without supersymmetry, "by means of a complex Nambu-Goldstone boson carrying baryon number", or with "a charged Peccei-Quinn field containing the QCD axion as a phase" in the role of the AD field (Bodeker & Buchmuller 2020, arXiv:2009.07294) [src: Sect. V]. <!-- num: not a value -->
- **Consistency:** `[der]` a condensate present during inflation carries quantum fluctuations that become baryon isocurvature.
  - Wu et al. 2026 "update the viable parameter space for baryogenesis using recent Cosmic Microwave Background constraints on baryon-density isocurvature perturbations, taking the quantum fluctuations of the scalar condensate generated during inflation as initial conditions" (arXiv:2602.08781) [src: abstract]. In the Affleck–Dine curvaton scenario "correlated baryon isocurvature perturbations are inevitably generated, resulting in excessively large correlated matter isocurvature perturbations"; reply, a proposed mechanism: cancellation "by anti-correlated dark matter isocurvature perturbations, thereby realizing compensated isocurvature perturbations" (Kawasaki & Neda 2026, arXiv:2607.21008) [src: abstract].
- **Observational status:** constrained through baryon isocurvature by the CMB (arXiv:2602.08781) [src: abstract]; the isocurvature bounds are in cosmoskill `cosmo-inflation-primordial`.
- **Status date:** 2026-11-13

### GUT baryogenesis
<!-- key: gut-baryogenesis -->
- **Defining equations:** CP-violating decays of "scalar and vector leptoquarks, whose decays violate baryon and lepton number" (Bodeker & Buchmuller 2020, arXiv:2009.07294) [src: Sect. II.1]; equations not transcribed here.
- **Parameters:** leptoquark masses and CP phases.
- **Predictions:** in SU(5), which conserves $B-L$, "leptoquark decays can create only a $B+L$ asymmetry, with a vanishing asymmetry for $B-L$" [src: Sect. II.1].
- **Consistency:** "at temperatures above the electroweak phase transition ($B+L$)-violating sphaleron processes are in thermal equilibrium. Hence, any nonzero ($B+L$)-asymmetry is washed out", as emphasised by Kuzmin, Rubakov & Shaposhnikov (arXiv:2009.07294) [src: Sect. II.1]; the abstract says these GUT models "were excluded by the discovery of $B+L$ violating sphaleron processes at high temperatures" [src: abstract]. In SO(10), "With $B-L$ broken at the GUT scale, right-handed neutrinos with masses below the GUT scale are ideal agents for generating a $B-L$ asymmetry" [src: Sect. II.1].
- **Observational status:** excluded in its SU(5) form by the argument above. `[der]`
- **Status date:** 2026-11-13

### Spontaneous baryogenesis and axiogenesis
<!-- key: spontaneous-baryogenesis-and-axiogenesis -->
- **Defining equations:** the arrow of time is set "by the motion of a light pseudo Goldstone boson of a spontaneously broken approximate global $\text{U(1)}_{B}$ baryon symmetry", where "Baryon-number-violating interactions can be in thermal equilibrium, and the observed baryon asymmetry can be generated for a sufficiently large $\text{U(1)}_{B}$ breaking scale" (Bodeker & Buchmuller 2020, arXiv:2009.07294) [src: Sect. V]; equations not transcribed here.
- **Parameters:** the $\text{U(1)}_{B}$ breaking scale, the coupling of the (pseudo)scalar to the baryon or lepton current. <!-- num: not a value -->
- **Predictions:** "spontaneous baryogenesis is a rather general phenomenon in the presence of axionlike particles", and "their coupling to gluons is already enough to generate a baryon asymmetry", quoted from its Ref. [142] (arXiv:2009.07294) [src: Sect. V]. In axiogenesis with a rotating axion-like field, Co et al. 2026 claim that "both the hint of cosmic birefringence and the observed baryon asymmetry can be simultaneously explained", with "matter and kination domination ending around a temperature of $\mathcal O(3\text{-}50)$ MeV" (arXiv:2609.25202) [src: abstract]. Gravitational variants: the Ricci scalar in the role of the axion ("gravitational baryogenesis"), and leptogenesis from inflationary gravitational waves "via the gravitational anomaly of the lepton current" (arXiv:2009.07294) [src: Sect. V].
- **Consistency:** none found among the sources read.
- **Observational status:** the birefringence hint is "$2\text{-}4\sigma$" in "Recent analyses of Planck and ACT CMB data", as quoted in arXiv:2609.25202 [src: abstract]; the measurement is in cosmoskill `cosmo-inflation-primordial`.
- **Status date:** 2026-11-13

### Low-scale and late-time baryogenesis (class)
<!-- key: other-low-scale-mechanisms-pointers -->
- **Defining equations:** cold electroweak transition with tachyonic preheating generating Chern–Simons number; decays of a singlet scalar "coupled to higher-dimensional $B$-violating operators" below the electroweak transition; $B$-meson oscillations "in an extension of the standard model with exotic $B$-meson decays" (Bodeker & Buchmuller 2020, arXiv:2009.07294) [src: Sect. V]; equations not transcribed here. <!-- eq: notation -->
- **Parameters:** model-dependent.
- **Predictions:** the singlet-decay mechanism "can be probed by neutron-antineutron oscillations and the neutron EDM"; the $B$-meson mechanism operates "At even lower temperatures of around 10 MeV" (arXiv:2009.07294) [src: Sect. V]. The Snowmass white paper of Elor et al. 2022 surveys such ideas "with an emphasis on experimental testability" (arXiv:2203.05010) [src: abstract].
- **Consistency:** none found among the sources read.
- **Observational status:** not assessed in the sources read.
- **Status date:** 2026-11-13

## Magnetogenesis
<!-- key: magnetogenesis -->

### Magnetogenesis at the electroweak transition
<!-- key: magnetogenesis-at-the-electroweak-transition -->
- **Defining equations:** field from Higgs gradients, $({\bf B}_{V})_{i}\sim-i\frac{2\sin\theta_{w}}{g\eta^{2}}\frac{1}{V}\int_{V}d^{3}x\,\epsilon_{ijk}\partial_{j}\Phi^{\dagger}\partial_{k}\Phi\sim-i\frac{2\sin\theta_{w}}{g\eta^{2}}\frac{1}{V}\int_{\partial V}dS^{j}\,\epsilon_{ijk}\Phi^{\dagger}\partial_{k}\Phi$ (Vachaspati 2020, arXiv:2010.10525) [src: Eq. 43].
- **Parameters:** domain size $\xi$ at the transition, helicity from CP violation.
- **Predictions:** $E_{M}(k)\sim\frac{1}{k}B^{2}_{V,\lambda}\sim k^{3}.$ (arXiv:2010.10525) [src: Eq. 45]; "The generation of magnetic helicity requires new CP violating interactions that can be tested by accelerator experiments" [src: abstract]. A 2026 review notes that "Near the electroweak scale, these phenomena are not necessarily independent" and that "The electroweak anomaly allows hypermagnetic helicity to exchange charge with chiral fermions" (Abu-Ajamieh 2026, arXiv:2611.02007) [src: abstract].
- **Consistency:** an earlier estimate of its Ref. [129] "used a different definition of the 'average magnetic field' that has been criticized in Refs. [26, 27]" (arXiv:2010.10525) [src: Sect. III.1.2, text after Eq. 45]. The Standard-Model electroweak transition is a crossover (`results.md`), so the domain picture applies to a first-order transition beyond the Standard Model or to the crossover as an estimate `[der]`.
- **Observational status:** relic strength depends on the decay law; under reconnection-controlled decay the electroweak relic is consistent with the blazar constraints (arXiv:2203.03573) [src: abstract]; under earlier decay models it was "too low" [src: abstract].
- **Status date:** 2026-11-13

### Inflationary magnetogenesis with a kinetic coupling $f(\varphi)^2F^2$
<!-- key: inflationary-magnetogenesis-with-a-kinetic -->
- **Defining equations:** $\ddot{A}_{i}+2\frac{\dot{f}}{f}\dot{A}_{i}-\Delta A_{i}=0~,$ (Durrer & Neronov 2013, arXiv:1303.7121) [src: Eq. 34] with $f(t)=f_{1}\left(\frac{t}{t_{1}}\right)^{\gamma}\;.$ [src: Eq. 35], following Martin & Yokoyama 2008 and Subramanian 2010 as cited there.
- **Parameters:** $\gamma$ (spectral slope), $f_1$, $t_1$, $H_{\rm inf}$.
- **Predictions:** scale invariance for $\gamma=-2$; "Normalizing $e^{2}$ such that $f=f_{1}=1$ after inflation", $\frac{\rho_{B}}{\rho_{\rm rad}}\simeq\frac{1}{(t_{1}a_{1}M_{P})^{2}}\simeq\left(\frac{H_{\rm inf}}{M_{P}}\right)^{2}\,.$ (arXiv:1303.7121) [src: Eq. 50]; "it is then easy to obtain magnetic fields of the order of e.g. $10^{-9}$ Gauss $/a^{2}$ on all cosmologically relevant scales in the scale invariant case" "With a suitable choice of $f_{1}^{2}t_{1}^{4}$", "while maintaining the condition $f_{1}t_{1}a<M_{P}^{-1}$ during all of inflation, in order to prevent back reaction" [src: Sect. 3.1.1, inline, text after Eq. 50]; for $\gamma>0$ a "very blue" spectrum [src: Sect. 3.1.1, text before Eq. 51].
- **Consistency:** strong-coupling problem for $\gamma\sim-2$: "To arrive at $e^{2}=1/137$ at the end of inflation, $e^{2}/f$ must have been much larger than 1 during most of inflation" (arXiv:1303.7121) [src: Sect. 3.1.1, text after Eq. 50]; backreaction bound of arXiv:0907.1030 [src: abstract] (`results.md`). The same review adds: "This is actually the only way to save this model, to violate gauge invariance", whose consequences "have not yet been studied", and "This problem is avoided if $\gamma>0$", at the price of a "very blue" spectrum (arXiv:1303.7121) [src: Sect. 3.1.1, inline, text after Eq. 50]. No reply restoring the $\gamma\sim-2$ case was read.
- **Observational status:** not assessed in the sources read beyond the bounds above.
- **Status date:** 2026-11-13

### Magnetogenesis at a first-order transition beyond the Standard Model
<!-- key: magnetogenesis-at-a-first-order-transition -->
- **Defining equations:** "Sufficiently strong first-order phase transitions (FOPTs) in the early Universe can simultaneously produce an observable stochastic gravitational wave background (SGWB) and a large-scale primordial magnetic field (PMF)"; example: an ALP sector with a radiatively broken global $U(1)$ coupled through a Higgs portal (Borah, Dev & Ghoshal 2026, arXiv:2604.20768) [src: abstract].
- **Parameters:** transition parameters ($\alpha$, $\beta/H$, $T_*$), helicity fraction; ALP decay constant $f_a$ in the example.
- **Predictions:** "For maximally helical configurations, we find peak field strengths up to $B_0 \sim 10^{-9}$ G at coherence length $\lambda_0 \sim 10^{-3}-10^{-1}$ Mpc", computed "accounting for inverse cascade effects", with correlated GW signals for "$10^3$ GeV $\lesssim f_a \lesssim 10^5$ GeV" (arXiv:2604.20768) [src: abstract, inline]. The GW spectrum belongs to `thcosmo-cosmological-gravitational-waves`.
- **Consistency:** none found among the sources read.
- **Observational status:** "consistent with lower bounds on the IGMF inferred from blazar observations", assuming maximally helical fields (arXiv:2604.20768) [src: abstract].
- **Status date:** 2026-11-13

### QCD-epoch magnetogenesis
<!-- key: qcd-epoch-magnetogenesis -->
- **Defining equations:** charge separation at bubble walls of a first-order QCD transition, ferromagnetic domain walls, or axion interactions during hadronisation (Vachaspati 2020, arXiv:2010.10525) [src: Sect. III.2]; equations not transcribed here.
- **Parameters:** model-dependent.
- **Predictions:** one estimate "$10^{-20}$ G on a coherence scale $\sim 1$ kpc", quoted from its Ref. [157] (arXiv:2010.10525) [src: Sect. III.2, inline].
- **Consistency:** bubble-based scenarios "need to be re-examined" because the QCD transition is a crossover [src: Sect. III.2]; see arXiv:hep-lat/0611014 [src: abstract].
- **Observational status:** not assessed in the sources read.
- **Status date:** 2026-11-13

## Not verified
<!-- key: not-verified -->
