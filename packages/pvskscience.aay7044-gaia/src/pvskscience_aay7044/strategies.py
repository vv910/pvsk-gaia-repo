"""
Strategies for pvskscience.aay7044 (Min2019, Science 366, 749).

All cross-module and complex reasoning strategies are defined here so that
each module's claims and settings are fully loaded before strategy arguments
are resolved.
"""

from gaia.lang import (
    support,
    composite,
    compare,
    abduction,
    induction,
    infer,
    contradiction,
)

# Import all claims from all modules
from .motivation import (
    mapbbr3_control_efficiency,
)

from .s2_methods import (
    deposition_method,
    surface_passivation,
    device_structure,
    uvvis_absorption,
    pl_spectra,
    ftir_confirms_mda,
    xrd_phase_analysis,
    giwaxs_analysis,
    xps_cl_content,
    tofsims_cl_mapping,
    defect_density_sclc,
    pl_lifetime,
    j_v_measurement,
    eqe_spectral_response,
    stability_test_protocols,
    dft_bandgap_calculation,
    xrd_peak_shift,
)

from .s3_results import (
    uvvis_blue_shift,
    pl_peak_shifts,
    bandgap_values,
    dft_bandgap_fa_vacancy,
    dft_bandgap_cl_interstitial,
    pl_quality_enhancement,
    humidity_phase_stability,
    alpha_phase_retention_38,
    alpha_phase_retention_57,
    crystallinity_improvement,
    giwaxs_no_impurity,
    xrd_peak_lower_angle,
    pce_distributions,
    target_best_jv,
    certified_pce,
    highest_jsc,
    eqe_expanded_range,
    morphology_unchanged,
    electron_trap_density,
    hole_trap_reduction,
    carrier_lifetime_target,
    cl_enriched_interface,
    humidity_stability,
    thermal_stability,
    photostability,
    optimal_composition,
    mda_superior_to_mapbbr3,
)

from .s4_discussion import (
    stabilization_mechanism_h_bonding,
    stabilization_mechanism_entropic,
    stabilization_mechanism_tolerance_factor,
    stabilization_mechanism_cl_interstitial,
    v_fa_defects_shallow,
    phase_stability_summary,
    cl_interface_photostability,
    photostability_mechanism,
    literature_comparison,
    aberration_free_stability,
    conclusion_alpha_stabilization,
    conclusion_no_tradeoff,
)

# Import settings for use as background only
from .motivation import (
    perovskite_structure,
    fapbi3_bandgap,
    alpha_delta_transition,
    mixed_cation_problem,
    mda_properties,
)

# -----------------------------------------------------------------------------
# Methods + Results: DFT theory vs experiment abduction
# FA vacancy model (H) vs Cl interstitial model (Alt)
# -----------------------------------------------------------------------------

s_h_fa_vacancy = support(
    [dft_bandgap_fa_vacancy],
    bandgap_values,
    reason="FA vacancy model (FA1-2xMDAx)Pb(I1-xClx)3 at x=0.037 predicts bandgap "
    "of 1.47 eV, which is close to the experimentally observed 1.49 eV for x=3.8 mol% "
    "MDACl2; this computational result supports the FA vacancy mechanism as the "
    "dominant structural effect of MDACl2 incorporation [@Min2019].",
    prior=0.70,
)

s_alt_cl_interstitial = support(
    [dft_bandgap_cl_interstitial],
    bandgap_values,
    reason="Cl interstitial model (FA1-xMDAx)PbI3Clx at x=0.037 predicts bandgap "
    "of 1.69 eV, substantially higher than the experimental observation of 1.49 eV; "
    "this large deviation indicates that Cl interstitial incorporation is NOT the "
    "dominant mechanism in the actual samples; the calculation itself is correct "
    "but the mechanism does not match the observed bandgap [@Min2019].",
    prior=0.20,
)

comp_bandgap = compare(
    dft_bandgap_fa_vacancy,
    dft_bandgap_cl_interstitial,
    bandgap_values,
    reason="FA vacancy model predicts 1.47 eV (deviation +0.02 eV from experiment), "
    "while Cl interstitial predicts 1.69 eV (deviation +0.20 eV from experiment); "
    "the FA vacancy prediction is much closer to the measured bandgap of 1.49 eV, "
    "indicating this mechanism is dominant and Cl interstitial is a minor contributor "
    "[@Min2019].",
    prior=0.88,
)

abd_fa_vacancy_vs_cl_interstitial = abduction(
    s_h_fa_vacancy,
    s_alt_cl_interstitial,
    comp_bandgap,
    reason="Two competing DFT models for MDACl2 incorporation: FA vacancy vs Cl interstitial. "
    "The FA vacancy model prediction (1.47 eV) closely matches experiment (1.49 eV), "
    "while the Cl interstitial model (1.69 eV) significantly overestimates bandgap widening. "
    "This abduction supports the FA vacancy mechanism as the dominant structural effect, "
    "with Cl interstitials present but not dominating the bandgap behavior [@Min2019].",
)

# -----------------------------------------------------------------------------
# Methods: structural characterization confirmation
# -----------------------------------------------------------------------------

strat_mda_incorporation = support(
    [xrd_phase_analysis, giwaxs_analysis],
    ftir_confirms_mda,
    reason="XRD shows no impurity peaks and phase retention under humidity; "
    "GIWAXS confirms no secondary phases (FACl, MDACl2) and identical crystal "
    "structure between target and control; together these structural techniques "
    "independently corroborate successful MDA incorporation into the FAPbI3 lattice "
    "without forming secondary phases [@Min2019].",
    prior=0.88,
)

strat_cl_interface_confirmation = support(
    [xps_cl_content, tofsims_cl_mapping],
    cl_enriched_interface,
    reason="XPS shows higher residual Cl content in target vs control, enriched at "
    "the TiO2 interface; ToF-SIMS independently confirms higher Cl anion concentration "
    "in the target and its spatial distribution at the perovskite/TiO2 interface; "
    "the two techniques are complementary (XPS is surface-sensitive, ToF-SIMS provides "
    "depth profiling), and their agreement strongly confirms Cl enrichment at the "
    "critical TiO2/perovskite interface [@Min2019].",
    prior=0.85,
)

strat_xrd_expansion_interpretation = support(
    [xrd_peak_shift, xrd_phase_analysis],
    stabilization_mechanism_cl_interstitial,
    reason="The XRD (001) peak shifting to lower angle with increasing MDACl2 content "
    "indicates lattice expansion; this is consistent with interstitial Cl- ions "
    "(radius 181 pm, much smaller than I- at 220 pm) occupying interstitial sites "
    "rather than lattice contraction from H-bonding; this structural evidence supports "
    "the mechanism of interstitial Cl- contributing to phase stabilization through "
    "lattice strain relief and the observed small bandgap increase [@Min2019].",
    prior=0.82,
)

# -----------------------------------------------------------------------------
# Results: bandgap preservation
# -----------------------------------------------------------------------------

strat_bandgap_preservation = support(
    [uvvis_blue_shift, pl_peak_shifts, bandgap_values],
    optimal_composition,
    reason="UV-vis shows absorption edge for x=3.8 mol% nearly identical to pure FAPbI3 "
    "(no MACl mediator); PL peaks shift from 826 nm (x=0) to 822 nm (x=3.8 mol%), "
    "a small 4 nm shift; bandgap values show 1.49 eV for x=3.8 vs 1.45 eV for pristine "
    "FAPbI3; the control (MAPbBr3) shows a larger shift to 1.53 eV, confirming that "
    "MDACl2 causes much less bandgap widening than MAPbBr3 for equivalent stabilization; "
    "this bandgap preservation is a key component of the optimal composition claim "
    "[@Min2019].",
    prior=0.92,
)

# -----------------------------------------------------------------------------
# Results: electronic quality
# -----------------------------------------------------------------------------

strat_trap_density_measurement = support(
    [j_v_measurement, defect_density_sclc],
    electron_trap_density,
    reason="The space-charge-limited current (SCLC) method uses the trap-filled limit "
    "voltage (V_TFL) from dark J-V curves of electron-only devices; the measurement "
    "protocol (J-V measurement) provides the voltage data, while the SCLC analysis "
    "(defect_density_sclc) provides the calculation method using N_defects equation; "
    "the direct measurement of V_TFL combined with the standard SCLC equation yields "
    "the electron trap densities (5.4e15 to 8.0e15 cm-3) for all compositions [@Min2019].",
    prior=0.82,
)

strat_pl_lifetime_measurement = support(
    [pl_lifetime, j_v_measurement],
    carrier_lifetime_target,
    reason="TRPL measurements on quartz substrates yield non-radiative recombination "
    "lifetimes using a biexponential fit; the target (3.8 mol% MDACl2) shows 1562 ns "
    "vs control 715 ns, more than double; this is a direct measurement reported in "
    "the J-V measurement context (pl_lifetime module), and the J-V context confirms "
    "the reproducibility of the films used for both PL and device measurements [@Min2019].",
    prior=0.88,
)

strat_electronic_quality = support(
    [electron_trap_density, carrier_lifetime_target, pl_quality_enhancement],
    cl_enriched_interface,
    reason="Electron trap densities remain low (5.7e15 cm-3 at x=3.8) and lower than "
    "control (1.0e16 cm-3); carrier lifetime is more than doubled (1562 ns vs 715 ns); "
    "PL quantum yield is enhanced at 3.8 mol%; these three independent electronic "
    "measurements collectively demonstrate that MDACl2 incorporation at optimal content "
    "improves film electronic quality and passivates traps rather than introducing "
    "deep traps; this is consistent with the observed JSC improvement [@Min2019].",
    prior=0.85,
)

# -----------------------------------------------------------------------------
# Results: phase stabilization
# -----------------------------------------------------------------------------

strat_alpha_phase_stabilization = support(
    [humidity_phase_stability, alpha_phase_retention_38, alpha_phase_retention_57],
    phase_stability_summary,
    reason="XRD shows that pure FAPbI3 (x=0) completely converts to delta-phase after "
    "24h at 80% humidity; 1.9 mol% shows strong delta transition; 3.8 and 5.7 mol% "
    "retain pure alpha-phase; this establishes 3.8 mol% as the minimum threshold for "
    "effective humidity-induced phase stabilization; the broad composition window "
    "(3.8 to 5.7 mol%) indicates robust stabilization under humidity stress [@Min2019].",
    prior=0.93,
)

# -----------------------------------------------------------------------------
# Results: device performance
# -----------------------------------------------------------------------------

strat_jsc_from_bandgap = support(
    [target_best_jv, eqe_expanded_range, bandgap_values, certified_pce],
    highest_jsc,
    reason="The target device achieves JSC = 26.50 mA/cm2 (best) and certified 26.70 mA/cm2, "
    "the highest for FA-based PSCs; EQE shows expanded absorption wavelength range "
    "compared to control; this directly results from maintaining narrower bandgap "
    "of FAPbI3 (1.49 eV vs 1.53 eV for MAPbBr3 control); the narrower bandgap extends "
    "photon absorption in the near-infrared region, yielding higher photocurrent; "
    "certified values from Newport confirm these results [@Min2019].",
    prior=0.93,
)

comp_pce_improvement = compare(
    target_best_jv,
    mapbbr3_control_efficiency,
    mda_superior_to_mapbbr3,
    reason="Target device (3.8 mol% MDACl2): PCE = 24.66%, JSC = 26.50 mA/cm2, "
    "VOC = 1.14 V, FF = 81.77%. Control (MAPbBr3): PCE = 23.05%, JSC = 25.14 mA/cm2, "
    "VOC = 1.14 V, FF = 80.55%. Target improves PCE by +1.61 absolute percent, "
    "driven primarily by higher JSC (+1.36 mA/cm2) while VOC is identical and FF is "
    "slightly higher. The JSC improvement comes from narrower bandgap (1.49 vs 1.53 eV) "
    "enabling better near-infrared absorption, confirmed by EQE expansion. This directly "
    "supports the conclusion that MDACl2 is superior to MAPbBr3 for stabilization "
    "[@Min2019].",
    prior=0.93,
)

# -----------------------------------------------------------------------------
# Results: stability
# -----------------------------------------------------------------------------

strat_humidity_stability = support(
    [humidity_stability, alpha_phase_retention_38],
    mda_superior_to_mapbbr3,
    reason="Under 85% RH at 25C (unencapsulated), target retains >90% initial PCE "
    "after 70h while control drops to 40%; this 50+ percentage point difference is a "
    "large, unambiguous performance gap; the humidity stability directly correlates "
    "with alpha-phase retention under humidity stress (alpha_phase_retention_38), "
    "confirming that MDACl2's phase stabilization translates to device-level humidity "
    "resistance superior to MAPbBr3-stabilized control [@Min2019].",
    prior=0.90,
)

strat_thermal_stability = support(
    [thermal_stability],
    mda_superior_to_mapbbr3,
    background=[mixed_cation_problem],
    reason="At 150C in air (unencapsulated), target retains >90% PCE after 20h while "
    "control degrades to <20% after 17h due to MA evaporation from MAPbBr3; this "
    "directly demonstrates the thermal advantage of being MA-free; the mixed cation "
    "problem explains why MA causes low thermal stability, and the target avoids this "
    "entirely; MDACl2 provides structural stabilization without the thermal instability "
    "inherent to MA-containing compositions [@Min2019].",
    prior=0.90,
)

strat_photostability = support(
    [photostability, cl_enriched_interface, alpha_phase_retention_38],
    mda_superior_to_mapbbr3,
    reason="Target maintains ~90% PCE (>23.0%) after 600 hours MPP tracking under "
    "full AM 1.5G illumination without UV filter; two mechanisms contribute: "
    "(1) Cl enrichment at TiO2 interface suppresses TiO2 photocatalytic degradation "
    "(cl_enriched_interface), and (2) alpha-phase stabilization by MDA prevents "
    "photo-induced phase transition (alpha_phase_retention_38); both factors are "
    "necessary — neither alone explains the exceptional 600-hour operational "
    "stability under harsh illumination conditions [@Min2019].",
    prior=0.88,
)

strat_optimal_composition = support(
    [alpha_phase_retention_38, bandgap_values, pce_distributions, humidity_stability,
     thermal_stability, photostability],
    optimal_composition,
    reason="Multiple independent measurements all point to 3.8 mol% as optimal: "
    "(1) Phase stability — 3.8 mol% is the minimum threshold for alpha retention under "
    "humidity (alpha_phase_retention_38); "
    "(2) Bandgap — 1.49 eV at 3.8 mol% is close to pristine FAPbI3 (1.45 eV), while "
    "5.7 mol% increases to 1.51 eV (bandgap_values); "
    "(3) PCE — 3.8 mol% shows highest average PCE (22.46%) and best device (24.66%), "
    "while 5.7 mol% shows slight decline (pce_distributions); "
    "(4) Stability — 3.8 mol% provides excellent humidity, thermal, and photostability "
    "all meeting >90% retention criteria; "
    "5.7 mol% also stabilizes but with slightly degraded PCE and PL quantum yield, "
    "making 3.8 mol% the true optimum across all metrics [@Min2019].",
    prior=0.88,
)

strat_cl_interstitial_evidence = support(
    [xrd_peak_lower_angle, dft_bandgap_cl_interstitial],
    stabilization_mechanism_cl_interstitial,
    reason="Two independent lines of evidence support interstitial Cl- ions: "
    "(1) XRD (001) peak shifts to lower angle with increasing MDACl2 content, "
    "indicating lattice expansion — consistent with small Cl- ions (181 pm) occupying "
    "interstitial sites rather than contracting the lattice; "
    "(2) DFT predicts Cl interstitial composition yields 1.69 eV, substantially "
    "higher than observed 1.49 eV, confirming Cl interstitials are present but not "
    "dominant; together these indicate interstitial Cl- contributes to lattice "
    "expansion and phase stabilization but does not cause the main bandgap effect "
    "[@Min2019].",
    prior=0.78,
)

# -----------------------------------------------------------------------------
# Discussion: phase stabilization mechanisms
# -----------------------------------------------------------------------------

strat_h_bonding_support = support(
    [stabilization_mechanism_h_bonding],
    phase_stability_summary,
    background=[mda_properties],
    reason="MDA has more hydrogen atoms than FA or MA, enabling more H-bonds with I- "
    "in the lattice; this is the same mechanism by which MA stabilizes alpha-FAPbI3 "
    "(supported by refs 33-35 in the paper); MDA's divalent state and comparable ionic "
    "radius to FA means it can substitute at FA sites and provide structural "
    "stabilization at smaller amounts than MA (3.8 mol% MDACl2 vs 5 mol% MAPbBr3); "
    "this H-bonding is one of four mechanisms contributing to alpha-phase stabilization "
    "[@Min2019, refs 33-35].",
    prior=0.78,
)

strat_entropic_support = support(
    [stabilization_mechanism_entropic],
    phase_stability_summary,
    background=[mda_properties],
    reason="MDA2+ substituting for FA+ at 3.8 mol% creates cation mixing at FA sites; "
    "this mixing affords entropic stabilization through entropy gain and small internal "
    "energy input, forming a solid solution that stabilizes the black alpha-phase; "
    "this entropic contribution (ref 32) complements the enthalpic H-bonding "
    "stabilization from MDA, making the overall stabilization more robust than either "
    "mechanism alone; combined, these thermodynamic factors kinetically trap the "
    "metastable alpha-phase at room temperature [@Min2019, ref 32].",
    prior=0.75,
)

strat_tolerance_factor_support = support(
    [stabilization_mechanism_tolerance_factor],
    phase_stability_summary,
    background=[perovskite_structure],
    reason="Goldschmidt tolerance factor t for FAPbI3 is approximately 1.0, above the "
    "optimal t ~ 0.9 for cubic alpha-phase stability; MDA2+ (ionic radius 262 pm) "
    "substituting for FA+ (256 pm) at 3.8 mol% brings t slightly closer to 0.9, "
    "improving thermodynamic stability of the cubic alpha-phase; the divalent state "
    "of MDA2+ introduces charge-compensating defects (FA vacancies or Cl interstitials) "
    "that provide additional lattice strain relaxation; this tolerance factor "
    "optimization is a known mechanism for phase stabilization in mixed-cation "
    "perovskites (ref 31) [@Min2019].",
    prior=0.72,
)

strat_v_fa_shallow_support = support(
    [v_fa_defects_shallow, electron_trap_density, pl_quality_enhancement],
    phase_stability_summary,
    reason="FA vacancy (V_FA) defects from MDA2+ substitution are shallow traps near "
    "the conduction band (ref 37); they do not act as deep electron traps, as confirmed "
    "by: (1) electron trap density remains low (5.7e15 cm-3 at x=3.8, lower than "
    "control's 1.0e16 cm-3), (2) JSC is not reduced by MDACl2 incorporation, and "
    "(3) PL quantum yield is enhanced at optimal 3.8 mol%; these electronic quality "
    "metrics collectively confirm that V_FA defects are shallow and non-trapping, "
    "meaning MDACl2 incorporation does not introduce detrimental non-radiative "
    "recombination pathways that would otherwise limit device performance [@Min2019, ref 37].",
    prior=0.80,
)

composite_phase_stabilization = composite(
    premises=[stabilization_mechanism_h_bonding,
              stabilization_mechanism_entropic,
              stabilization_mechanism_tolerance_factor,
              v_fa_defects_shallow,
              electron_trap_density, pl_quality_enhancement],
    conclusion=phase_stability_summary,
    sub_strategies=[strat_h_bonding_support, strat_entropic_support,
                    strat_tolerance_factor_support, strat_v_fa_shallow_support],
    background=[mda_properties, perovskite_structure],
    reason="Four mechanisms collectively explain alpha-phase stabilization by MDACl2: "
    "(1) H-bonding between MDA's H-N groups and I- in the lattice provides enthalpic "
    "stabilization; (2) entropic stabilization from cation mixing at FA sites provides "
    "thermodynamic stabilization; (3) tolerance factor adjustment brings t closer to "
    "the optimal 0.9 for cubic phase; (4) interstitial Cl- ions expand the lattice "
    "and reduce strain. Together these mechanisms kinetically trap the metastable "
    "alpha-phase at room temperature, preventing conversion to the thermodynamically "
    "favored delta-phase under humidity, thermal, and optical stress conditions. "
    "No single mechanism alone is sufficient; all four contribute and are mutually "
    "consistent [@Min2019].",
)

# -----------------------------------------------------------------------------
# Discussion: photostability mechanisms
# -----------------------------------------------------------------------------

strat_cl_interface_photostability = support(
    [cl_enriched_interface, photostability],
    photostability_mechanism,
    reason="Cl enrichment at TiO2/perovskite interface (confirmed by XPS and ToF-SIMS) "
    "contributes to photostability by suppressing TiO2 photocatalytic activity that would "
    "otherwise degrade perovskite under UV illumination (refs 41-42); the target device "
    "maintains ~90% PCE after 600 hours MPP tracking under full AM 1.5G with no UV filter, "
    "a demanding test that includes significant UV content; this exceptional "
    "photostability demonstrates that interfacial Cl enrichment is a critical factor "
    "in protecting the perovskite layer from UV-induced degradation [@Min2019, refs 41-42].",
    prior=0.82,
)

strat_dual_photostability = support(
    [cl_interface_photostability, alpha_phase_retention_38, photostability],
    photostability_mechanism,
    reason="The exceptional photostability (90% PCE retention after 600 hours MPP under "
    "full sunlight) results from two synergistic factors: (1) interfacial Cl enrichment "
    "suppressing TiO2 photocatalysis (cl_interface_photostability), and (2) alpha-phase "
    "stabilization by MDA preventing photo-induced phase transition "
    "(alpha_phase_retention_38); neither factor alone can explain the 600-hour "
    "operational stability under full AM 1.5G illumination without UV filtering; "
    "both are necessary and together provide robust protection against UV-induced, "
    "heat-induced, and phase-transition-induced degradation pathways [@Min2019].",
    prior=0.82,
)

# -----------------------------------------------------------------------------
# Discussion: final conclusions
# -----------------------------------------------------------------------------

record_jsc_support = support(
    [certified_pce, highest_jsc, eqe_expanded_range],
    conclusion_alpha_stabilization,
    reason="The certified JSC of 26.70 mA/cm2 (Newport, USA) represents the highest "
    "short-circuit current density reported for PSCs fabricated from FA-based lead "
    "halide perovskites. This was achieved by maintaining the inherent narrow bandgap "
    "of FAPbI3 (1.49 eV vs 1.53 eV for MAPbBr3 control) while stabilizing the "
    "alpha-phase with MDACl2, enabling enhanced photon absorption in the near-infrared "
    "region. EQE confirms expanded absorption range. Both JSC values (26.10 and "
    "26.70 mA/cm2) were independently certified by Newport using the QSS method, "
    "making these the most reliable values in the field [@Min2019].",
    prior=0.95,
)

strat_record_jsc_support = support(
    [literature_comparison, certified_pce, highest_jsc],
    conclusion_alpha_stabilization,
    reason="Prior to this work, the highest efficiency for mp-TiO2-based PSCs was "
    "MAPbBr3-stabilized FAPbI3 at ~23% PCE with certified JSC ~25 mA/cm2; this work "
    "achieves 24.66% PCE (certified 23.73%) with certified JSC = 26.70 mA/cm2, "
    "a 1.6 mA/cm2 improvement that directly results from maintaining the inherent "
    "narrower bandgap of FAPbI3; the certified values from Newport (certified_pce, "
    "highest_jsc) confirm these are the highest reported values for FA-based PSCs "
    "and mp-TiO2-based PSCs, validating the literature comparison claim [@Min2019].",
    prior=0.90,
)

strat_aberration_free = support(
    [aberration_free_stability, humidity_stability, thermal_stability, optimal_composition],
    conclusion_no_tradeoff,
    reason="Unlike mixed-cation-anion approaches that sacrifice thermal stability (MA), "
    "introduce phase segregation (Br), or require complex synthesis (Cs/Rb), the MDACl2 "
    "approach achieves both high efficiency and robust stability without trade-offs; "
    "the data directly support this: target retains >90% PCE after 20h at 150C in air "
    "(vs <20% for MA-containing control) and after 70h at 85% RH (vs 40% for control), "
    "while achieving the highest PCE (24.66%) and JSC (26.70 mA/cm2) for this class "
    "of devices; no other stabilization approach simultaneously delivers all four "
    "metrics (efficiency, humidity stability, thermal stability, photostability) "
    "without compromise [@Min2019].",
    prior=0.85,
)

strat_main_conclusion = support(
    [phase_stability_summary, optimal_composition, mda_superior_to_mapbbr3,
     certified_pce, highest_jsc],
    conclusion_alpha_stabilization,
    reason="The core conclusion of the paper is that MDACl2 stabilizes alpha-FAPbI3 "
    "while preserving the inherent narrow bandgap, enabling record efficiency and "
    "stability. The evidence chain: (1) phase_stability_summary establishes the "
    "multi-mechanism stabilization, (2) optimal_composition identifies 3.8 mol% as "
    "the sweet spot across all metrics, (3) mda_superior_to_mapbbr3 provides direct "
    "head-to-head comparison showing MDACl2 outperforms MAPbBr3 on all metrics, "
    "and (4) certified PCE (23.73%) and record JSC (26.70 mA/cm2) from Newport confirm "
    "these are the highest reported values. Together these support the conclusion "
    "that MDACl2 is a superior stabilization approach for alpha-FAPbI3 PSCs "
    "[@Min2019].",
    prior=0.90,
)

strat_final_conclusion = support(
    [conclusion_alpha_stabilization, aberration_free_stability, literature_comparison],
    conclusion_no_tradeoff,
    reason="The key scientific contribution is demonstrating that the efficiency-stability "
    "trade-off can be eliminated by using MDACl2 instead of MA/Br/Cs. The evidence: "
    "(1) conclusion_alpha_stabilization establishes that MDACl2 achieves both high "
    "efficiency (23.73% certified PCE, 26.70 mA/cm2 JSC) and robust stability (>90% "
    "retention after 600h MPP, 20h at 150C, 70h at 85% RH), "
    "(2) aberration_free_stability shows no efficiency-stability trade-offs exist "
    "with MDACl2, and "
    "(3) literature_comparison confirms prior approaches required trade-offs between "
    "bandgap (MA, Br), thermal stability (MA), or synthesis complexity (Cs/Rb). "
    "This work demonstrates that the inherent bandgap of alpha-FAPbI3 can be fully "
    "utilized in stable, high-efficiency PSCs [@Min2019].",
    prior=0.88,
)

__all__ = [
    # DFT theory vs experiment
    "s_h_fa_vacancy",
    "s_alt_cl_interstitial",
    "comp_bandgap",
    "abd_fa_vacancy_vs_cl_interstitial",
    # Methods structural
    "strat_mda_incorporation",
    "strat_cl_interface_confirmation",
    "strat_xrd_expansion_interpretation",
    # Results bandgap
    "strat_bandgap_preservation",
    # Results electronic quality
    "strat_trap_density_measurement",
    "strat_pl_lifetime_measurement",
    "strat_electronic_quality",
    # Results phase
    "strat_alpha_phase_stabilization",
    # Results performance
    "strat_jsc_from_bandgap",
    "comp_pce_improvement",
    # Results stability
    "strat_humidity_stability",
    "strat_thermal_stability",
    "strat_photostability",
    "strat_optimal_composition",
    "strat_cl_interstitial_evidence",
    # Discussion mechanisms
    "strat_h_bonding_support",
    "strat_entropic_support",
    "strat_tolerance_factor_support",
    "strat_v_fa_shallow_support",
    "composite_phase_stabilization",
    # Discussion photostability
    "strat_cl_interface_photostability",
    "strat_dual_photostability",
    # Discussion conclusions
    "record_jsc_support",
    "strat_record_jsc_support",
    "strat_aberration_free",
    "strat_main_conclusion",
    "strat_final_conclusion",
]
