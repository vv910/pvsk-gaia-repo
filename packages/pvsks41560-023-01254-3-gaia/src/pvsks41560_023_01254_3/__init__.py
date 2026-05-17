"""
pvsks41560-023-01254-3: Gu2023 bifacial perovskite minimodules.

Package for formalizing: Gu et al., "Design optimization of bifacial perovskite
minimodules for improved efficiency and stability," Nature Energy (2023).
"""

from gaia.lang import (
    claim,
    setting,
    question,
    support,
    compare,
    deduction,
    abduction,
    induction,
    analogy,
    extrapolation,
    elimination,
    case_analysis,
    mathematical_induction,
    composite,
    infer,
    contradiction,
    equivalence,
    complement,
    disjunction,
)

from .motivation import (
    bifacial_gain_background,
    perovskite_bifacial_challenge,
    research_objective,
    front_efficiency_record,
    stability_demonstrated,
    power_generation_density_measurement,
    bifaciality_measurement,
    initial_efficiency_retention,
)

from .s2_module_structure import (
    module_structure_p_i_n,
    ito_sheet_resistance,
    ag_grid_design,
    optimal_ag_grid_spacing,
    relative_pce_loss_reduction,
    ff_improvement_with_ag_grid,
    bifacial_gain_percentage,
    simulated_pgds_by_albedo,
)

from .s3_hydrophobic_additive import (
    ald_damage_to_perovskite,
    tpfb_in_htl_protection,
    tpfb_spread_to_perovskite,
    hydrophobic_surface_confirmation,
    tpfb_passivation_effect,
    tpfb_reduced_trap_density,
    tpfb_frei_level_ptaa,
    ff_improvement_tpfb,
    tpfb_enhanced_stability,
)

from .s4_light_scattering import (
    jsc_reduction_without_reflective_electrode,
    sio2_np_light_scattering,
    optimal_np_size_range,
    optimal_np_spacing_range,
    absorption_enhancement_simulation,
    np_synthesis_and_embedding,
    no_extra_recombination_from_np,
    jsc_increase_with_optimal_np,
    front_pce_improvement_with_np,
)

from .s5_performance import (
    small_cell_front_pce,
    small_cell_rear_pce,
    bifaciality_small_cell,
    power_generation_density_albedo_02,
    minimodule_front_aperture_efficiency,
    minimodule_rear_aperture_efficiency,
    nrel_certified_front_efficiency,
    nrel_certified_rear_efficiency,
    average_front_efficiency_8_modules,
    average_rear_efficiency_8_modules,
    pgd_by_albedo,
)

from .s6_stability import (
    initial_pce_retention_6000h,
    damp_heat_retention,
    ald_sno2_stabilization_benefit,
    stability_benefits_composition,
)

from .strategies import (
    strat_ag_grid_balances_tradeoffs,
    strat_bifacial_gain_from_albedo,
    strat_simulated_pgds_support_objective,
    strat_tpfb_spreading_mechanism,
    strat_tpfb_passivation,
    strat_tpfb_stability,
    strat_ff_improvement_from_tpfb,
    strat_np_size_optimization,
    strat_np_spacing_optimization,
    strat_pce_improvement_from_np,
    strat_small_cell_bifaciality,
    strat_minimodule_record,
    strat_pgd_advantage,
    strat_nrel_certification,
    strat_module_reproducibility,
    strat_stability_6000h,
    strat_damp_heat_stability,
    strat_overall_conclusion,
    strat_combined_performance,
)

__all__ = [
    # motivation
    "bifacial_gain_background",
    "perovskite_bifacial_challenge",
    "research_objective",
    "front_efficiency_record",
    "stability_demonstrated",
    "power_generation_density_measurement",
    "bifaciality_measurement",
    "initial_efficiency_retention",
    # s2
    "module_structure_p_i_n",
    "ito_sheet_resistance",
    "ag_grid_design",
    "optimal_ag_grid_spacing",
    "relative_pce_loss_reduction",
    "ff_improvement_with_ag_grid",
    "bifacial_gain_percentage",
    "simulated_pgds_by_albedo",
    # s3
    "ald_damage_to_perovskite",
    "tpfb_in_htl_protection",
    "tpfb_spread_to_perovskite",
    "hydrophobic_surface_confirmation",
    "tpfb_passivation_effect",
    "tpfb_reduced_trap_density",
    "tpfb_frei_level_ptaa",
    "ff_improvement_tpfb",
    "tpfb_enhanced_stability",
    # s4
    "jsc_reduction_without_reflective_electrode",
    "sio2_np_light_scattering",
    "optimal_np_size_range",
    "optimal_np_spacing_range",
    "absorption_enhancement_simulation",
    "np_synthesis_and_embedding",
    "no_extra_recombination_from_np",
    "jsc_increase_with_optimal_np",
    "front_pce_improvement_with_np",
    # s5
    "small_cell_front_pce",
    "small_cell_rear_pce",
    "bifaciality_small_cell",
    "power_generation_density_albedo_02",
    "minimodule_front_aperture_efficiency",
    "minimodule_rear_aperture_efficiency",
    "nrel_certified_front_efficiency",
    "nrel_certified_rear_efficiency",
    "average_front_efficiency_8_modules",
    "average_rear_efficiency_8_modules",
    "pgd_by_albedo",
    # s6
    "initial_pce_retention_6000h",
    "damp_heat_retention",
    "ald_sno2_stabilization_benefit",
    "stability_benefits_composition",
    # strategies
    "strat_ag_grid_balances_tradeoffs",
    "strat_bifacial_gain_from_albedo",
    "strat_simulated_pgds_support_objective",
    "strat_tpfb_spreading_mechanism",
    "strat_tpfb_passivation",
    "strat_tpfb_stability",
    "strat_ff_improvement_from_tpfb",
    "strat_np_size_optimization",
    "strat_np_spacing_optimization",
    "strat_pce_improvement_from_np",
    "strat_small_cell_bifaciality",
    "strat_minimodule_record",
    "strat_pgd_advantage",
    "strat_nrel_certification",
    "strat_module_reproducibility",
    "strat_stability_6000h",
    "strat_damp_heat_stability",
    "strat_overall_conclusion",
    "strat_combined_performance",
]