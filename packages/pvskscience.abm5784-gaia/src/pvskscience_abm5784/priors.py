"""
Priors for independent claims in the Azmi et al. 2022 paper package.

Independent claims (leaf nodes in the knowledge graph) need priors assigned here.
These priors reflect the initial confidence level before reasoning propagation.
"""

from .motivation import (
    commercial_lifetime_requirement,
    damp_heat_test_standard,
    pscs_main_challenge,
    perovskite_instability_mechanism,
    defect_passivation_strategy,
    inverted_pscs_passivation_challenge,
    c60_weak_bonding,
    research_gap,
    proposed_solution,
    dimensionality_tailoring_key,
    room_temp_vs_thermal_annealing,
)

from .s2_methods import (
    device_structure,
    olai_post_treatment,
    two_d_rt_processing,
    giwaxs_characterization,
    hr_stem_elemental_mapping,
    pl_characterization,
    ups_energy_levels,
    contact_angle_moisture_resistance,
    sem_morphology,
    j_v_characteristics,
    pce_gain_absolute,
    energy_loss_reduction,
    trap_assisted_recombination,
    damp_heat_test_protocol,
    mppt_measurement,
    university_for_various_compositions,
    reproducibility,
)

from .s3_results import (
    giwaxs_n1_n2_peaks,
    hr_stem_n1_n2_confirmation,
    pl_n2_uniform_capping,
    ef_vbm_wider_gap_2d_rt,
    cbm_closer_to_c60_2d_rt,
    champion_pce_24_3_percent,
    pce_gain_2_percent_absolute,
    voc_1_20_v,
    ff_82_percent,
    energy_loss_0_34_ev,
    ta_lower_ff,
    narrow_statistical_distribution,
    universality_across_compositions,
    longer_recombination_lifetime,
    t95_after_1200_hours,
    pce_after_damp_heat_19_3_percent,
    structural_optical_robustness,
    mppt_95_percent_retention,
    enhanced_moisture_resistance,
    industry_standard_achieved,
    rt_vs_ta_comparison,
    passivation_vs_control,
)

from .s4_discussion import (
    main_achievement,
    key_innovation,
    dual_function_passivation,
    trap_state_passivation,
    moisture_oxygen_barrier,
    energy_level_match_critical,
    n_type_enhancement,
    regular_vs_inverted_pscs,
    c60_passivation_insufficient,
    scalability_advantage,
    universality_of_method,
    reproducibility_practical,
    thermal_stability_at_elevated_temps,
    robustness_after_thermal_aging,
    commercial_relevance,
    iecs_standard_met,
)

# Independent claim priors for the Azmi 2022 PSC stability paper
# Ranges:
#   0.85-0.95: well-established fact or strong experimental observation
#   0.65-0.85: supported by evidence but imperfect
#   0.40-0.65: tentative, single-source, method-dependent, or uncertain
#   0.20-0.40: speculative or weak assumption

PRIORS = {
    commercial_lifetime_requirement: (
        0.92,
        "Well-established industry standard for commercial PV modules per IEC 61215:2016."
    ),
    damp_heat_test_standard: (
        0.92,
        "Standard IEC test condition definition; widely reported in literature."
    ),
    pscs_main_challenge: (
        0.88,
        "Consistently reported challenge in PSC commercialization literature."
    ),
    perovskite_instability_mechanism: (
        0.85,
        "Well-documented mechanism in PSC degradation literature with multiple supporting studies."
    ),
    defect_passivation_strategy: (
        0.82,
        "Demonstrated strategy with multiple publications showing effectiveness."
    ),
    inverted_pscs_passivation_challenge: (
        0.85,
        "Persistent challenge widely acknowledged in perovskite community literature."
    ),
    c60_weak_bonding: (
        0.80,
        "Reported in recent literature with experimental UPS evidence."
    ),
    research_gap: (
        0.80,
        "Literature review claim supported by cited references on interface focus."
    ),
    proposed_solution: (
        0.75,
        "Proposed but not yet demonstrated at time of publication -- requires experimental validation."
    ),
    dimensionality_tailoring_key: (
        0.82,
        "Key finding supported by systematic experimental comparison of annealing conditions."
    ),
    room_temp_vs_thermal_annealing: (
        0.85,
        "Directly observed experimental difference between processing conditions with GIWAXS evidence."
    ),
    device_structure: (
        0.90,
        "Standard inverted PSC architecture clearly described in methods and confirmed by cross-sectional SEM."
    ),
    olai_post_treatment: (
        0.88,
        "Clearly described synthesis method with established chemistry."
    ),
    two_d_rt_processing: (
        0.85,
        "Directly comparative experimental observation between 2D-RT and 2D-TA conditions."
    ),
    giwaxs_characterization: (
        0.88,
        "Standard X-ray characterization technique with quantitative diffraction analysis."
    ),
    hr_stem_elemental_mapping: (
        0.88,
        "High-resolution imaging with elemental analysis; direct measurement of interlayer distances."
    ),
    pl_characterization: (
        0.85,
        "Standard optical characterization providing emission wavelength and lifetime data."
    ),
    ups_energy_levels: (
        0.85,
        "Direct UPS measurement of energy levels with clear shift observation."
    ),
    contact_angle_moisture_resistance: (
        0.82,
        "Measured contact angles directly demonstrating enhanced moisture resistance."
    ),
    sem_morphology: (
        0.85,
        "Direct SEM observation of surface morphology."
    ),
    j_v_characteristics: (
        0.90,
        "Standard electrical characterization of solar cells with measured current-voltage curves."
    ),
    pce_gain_absolute: (
        0.88,
        "Directly measured comparison between control and 2D-RT devices with clear PCE values."
    ),
    energy_loss_reduction: (
        0.82,
        "Calculated from measured VOC and known bandgap; thermodynamic limit comparison."
    ),
    trap_assisted_recombination: (
        0.82,
        "Transient photovoltage and light intensity measurements provide direct evidence."
    ),
    damp_heat_test_protocol: (
        0.88,
        "Standard IEC test conditions with clear protocol description."
    ),
    mppt_measurement: (
        0.88,
        "Standard MPPT measurement under 1-sun illumination with clear duration."
    ),
    university_for_various_compositions: (
        0.82,
        "Systematic experimental demonstration across multiple compositions and techniques."
    ),
    reproducibility: (
        0.85,
        "Statistical analysis across 7 researchers with quantified deviation."
    ),
    giwaxs_n1_n2_peaks: (
        0.88,
        "Direct GIWAXS quantitative diffraction data showing n=1 and n=2 peaks."
    ),
    hr_stem_n1_n2_confirmation: (
        0.88,
        "Direct HR-STEM imaging with measured interlayer distances of 1.2nm and 1.5nm."
    ),
    pl_n2_uniform_capping: (
        0.85,
        "Direct PL imaging at wavelength corresponding to n=2 showing uniform coverage."
    ),
    ef_vbm_wider_gap_2d_rt: (
        0.82,
        "Direct UPS measurement of Fermi level and VBM with quantified gap difference."
    ),
    cbm_closer_to_c60_2d_rt: (
        0.82,
        "Derived from UPS measurements comparing CBM positions relative to C60."
    ),
    champion_pce_24_3_percent: (
        0.88,
        "Direct J-V measurement of champion device with stabilized output confirmation."
    ),
    pce_gain_2_percent_absolute: (
        0.85,
        "Direct comparison between control and 2D-RT device performance."
    ),
    voc_1_20_v: (
        0.88,
        "Directly measured from J-V curves; compares well to thermodynamic limit."
    ),
    ff_82_percent: (
        0.88,
        "Directly measured fill factor from J-V curves."
    ),
    energy_loss_0_34_ev: (
        0.82,
        "Calculated from measured VOC (1.20V) and bandgap (1.55eV) using standard formula."
    ),
    ta_lower_ff: (
        0.85,
        "Direct J-V measurements showing FF < 79% for 2D-TA devices."
    ),
    narrow_statistical_distribution: (
        0.85,
        "Statistical data with quantified distributions shown in figures S8 and S11."
    ),
    universality_across_compositions: (
        0.82,
        "Systematic demonstration across different bandgaps and deposition techniques."
    ),
    longer_recombination_lifetime: (
        0.82,
        "Direct transient photovoltage decay measurement showing longer lifetime."
    ),
    t95_after_1200_hours: (
        0.88,
        "Direct stability measurement under damp-heat conditions showing >95% retention."
    ),
    pce_after_damp_heat_19_3_percent: (
        0.85,
        "Direct measurement of three devices after damp-heat test with statistical spread."
    ),
    structural_optical_robustness: (
        0.82,
        "Structural and optical characterization after thermal aging at 85C for 500+ hours."
    ),
    mppt_95_percent_retention: (
        0.85,
        "Direct MPPT tracking for >500 hours showing ~95% retention."
    ),
    enhanced_moisture_resistance: (
        0.80,
        "Testing under extreme conditions (>50% RH) demonstrating enhanced resistance."
    ),
    industry_standard_achieved: (
        0.88,
        "Direct result of passing IEC 61215:2016 damp-heat protocol."
    ),
    rt_vs_ta_comparison: (
        0.85,
        "Direct comparison of device performance between 2D-RT and 2D-TA processing."
    ),
    passivation_vs_control: (
        0.88,
        "Direct comparison between passivated and control devices with clear performance gap."
    ),
    main_achievement: (
        0.90,
        "Core result of the paper: >95% retention after >1000h damp-heat + 24.3% PCE."
    ),
    key_innovation: (
        0.85,
        "Key insight supported by systematic comparison of RT vs TA processing and resulting n values."
    ),
    dual_function_passivation: (
        0.80,
        "Inferred mechanism from multiple experimental observations (stability + PL + recombination)."
    ),
    trap_state_passivation: (
        0.82,
        "Supported by PL emission increase, lifetime extension, and ideality factor reduction."
    ),
    moisture_oxygen_barrier: (
        0.80,
        "Supported by contact angle measurements and damp-heat test results."
    ),
    energy_level_match_critical: (
        0.82,
        "Supported by UPS data showing CBM positions and correlation with FF values."
    ),
    n_type_enhancement: (
        0.78,
        "Inferred from Fermi level position relative to VBM; consistent with better charge extraction."
    ),
    regular_vs_inverted_pscs: (
        0.82,
        "Literature comparison supported by cited references on regular vs inverted device performance."
    ),
    c60_passivation_insufficient: (
        0.82,
        "Supported by control device degradation despite encapsulation and UPS evidence."
    ),
    scalability_advantage: (
        0.80,
        "General property of inverted architecture widely reported in literature."
    ),
    universality_of_method: (
        0.82,
        "Demonstrated across multiple compositions and deposition techniques with systematic enhancement."
    ),
    reproducibility_practical: (
        0.82,
        "Quantified reproducibility data across 7 researchers supports practical viability."
    ),
    thermal_stability_at_elevated_temps: (
        0.80,
        "Mechanistic inference supported by damp-heat test results at 85C."
    ),
    robustness_after_thermal_aging: (
        0.82,
        "Direct structural/optical characterization after thermal aging confirms robustness."
    ),
    commercial_relevance: (
        0.85,
        "Synthesis of both high efficiency (>24%) and long-term stability meeting IEC standard."
    ),
    iecs_standard_met: (
        0.88,
        "Direct outcome of passing the IEC 61215:2016 damp-heat test protocol."
    ),
}