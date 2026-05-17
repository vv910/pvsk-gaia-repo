"""
pvskscience_abm5784 - Gaia knowledge package for Azmi et al. 2022:
Damp heat-stable perovskite solar cells with tailored-dimensionality 2D/3D heterojunctions.

This package formalizes the knowledge from the Science paper on 2D/3D perovskite
heterojunction solar cells achieving 24.3% PCE with >1000h damp-heat stability.
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

# Import strategies to register reasoning chains
from . import strategies

__all__ = [
    # Core exported conclusions
    "main_achievement",
    "key_innovation",
    "champion_pce_24_3_percent",
    "t95_after_1200_hours",
    "iecs_standard_met",
    "dual_function_passivation",
    "trap_state_passivation",
    "moisture_oxygen_barrier",
    "energy_level_match_critical",
    "rt_vs_ta_comparison",
    "universality_of_method",
    "commercial_relevance",
]