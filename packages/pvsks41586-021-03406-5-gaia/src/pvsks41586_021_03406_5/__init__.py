"""
pvsks41586_021_03406_5 - Pseudo-halide anion engineering for α-FAPbI3 PSCs.

A Gaia knowledge package formalizing the paper:
Jeong et al., "Pseudo-halide anion engineering for α-FAPbI3 perovskite solar cells"
Nature 592, 627-632 (2021). DOI: 10.1038/s41586-021-03406-5
"""

from gaia.lang import claim, setting

# Re-export all public symbols from modules
from .motivation import (
    perovskite_general_formula,
    fapbi3_emergence,
    psc_research_drivers,
    pce_progress,
    operational_stability_progress,
    compositional_engineering_importance,
    fapbi3_phase_transition_problem,
    previous_mixture_approaches,
    alpha_fapbi3_candidate,
    prior_efficiency_record,
    voc_lag,
    previous_anion_engineering,
    formate_previous_studies,
    key_role_of_formate,
    formate_size_fits_vacancy,
    defect_passivation_crystallinity,
    research_question_mechanism,
    research_question_performance,
    strat_background_supports_problem,
    strat_previous_work_supports_formate,
    strat_phase_problem_motivates_solution,
)

from .s2_methods import (
    reference_film_preparation,
    fo_fapbi3_film_preparation,
    film_preparation_reproducibility,
    uv_vis_absorption_method,
    photoluminescence_method,
    sem_morphology_method,
    xrd_crystallinity_method,
    solid_state_nmr_method,
    tofsims_composition_method,
    afm_roughness_method,
    device_configuration,
    spiro_ometad_composition,
    j_v_measurement_method,
    eqe_measurement_method,
    eqe_el_measurement_method,
    stability_test_methods,
    md_simulation_method,
    dft_binding_energy_method,
    strat_methods_characterize_films,
    strat_methods_validate_device,
    strat_simulation_explains_mechanism,
)

from .s3_results import (
    absorption_spectra_results,
    bandgap_identical,
    pl_decay_results,
    reduced_trap_density,
    sem_morphology_results,
    larger_grain_size,
    monolithic_grain_structure,
    surface_roughness_results,
    xrd_phase_results,
    alpha_phase_confirmation,
    improved_crystallinity_2percent,
    gi_xrd_stabilization_results,
    alpha_stabilization_humidity,
    pb207_nmr_results,
    formate_not_in_bulk,
    c13_nmr_formate_environment,
    formate_at_interfaces,
    quantitative_c13_nmr,
    tofsims_confirmation,
    strat_optical_supports_passivation,
    strat_morphology_supports_crystallinity,
    strat_nmr_supports_surface_passivation,
    strat_gi_xrd_supports_stability,
)

from .s4_simulation import (
    md_solution_coordination,
    in_situ_crystal_growth,
    md_surface_passivation,
    md_passivation_structure,
    binding_affinity_comparison,
    formate_highest_affinity,
    fa_cation_binding,
    defect_elimination_mechanism,
    strat_md_solution_supports_slower_growth,
    strat_md_surface_supports_passivation,
    strat_binding_affinity_validates_formate,
)

from .s5_performance import (
    reference_device_performance,
    target_device_performance,
    performance_improvement,
    pcertified_performance,
    performance_distribution,
    eqe_results,
    jsc_verification,
    eqe_el_results,
    non_radiative_recombination_reduction,
    voc_shadowqueisser,
    jsc_light_intensity_linearity,
    voc_light_intensity_ideality,
    reduced_ideality_factor,
    fill_factor_improvement_mechanism,
    formamidinium_acetate_control,
    formate_without_macl,
    strat_formate_improves_voc,
    strat_formate_improves_ff,
    strat_formate_improves_jsc,
    strat_abduction_performance,
    strat_control_validates_formate,
    strat_overall_improvement,
)

from .s6_stability import (
    shelf_life_stability,
    target_shelf_life_retains_90,
    thermal_stability,
    target_heat_stability_80_percent,
    operational_stability_short_term,
    long_term_operational_stability,
    reference_degradation_mechanism,
    stability_from_crystallinity,
    crystallinity_importance_stability,
    formate_binding_stability,
    low_halide_vacancy_stability,
    strat_formate_improves_shelf_life,
    strat_formate_improves_thermal_stability,
    strat_formate_improves_operational_stability,
    strat_stability_mechanism,
)

# Define the exported conclusions for this knowledge package
__all__ = [
    # Core results
    "key_role_of_formate",
    "formate_size_fits_vacancy",
    "defect_passivation_crystallinity",
    "formate_not_in_bulk",
    "formate_at_interfaces",
    "formate_highest_affinity",
    "target_device_performance",
    "pcertified_performance",
    "non_radiative_recombination_reduction",
    "voc_shadowqueisser",
    "reduced_ideality_factor",
    "alpha_stabilization_humidity",
    "target_shelf_life_retains_90",
    "target_heat_stability_80_percent",
    "long_term_operational_stability",
]