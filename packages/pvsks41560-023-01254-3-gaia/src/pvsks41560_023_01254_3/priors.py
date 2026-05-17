"""
Priors for independent claims in the Gu2023 bifacial perovskite minimodules package.

Each entry is: ClaimVariable: (prior, justification_string)
"""

from .motivation import (
    bifacial_gain_background,
    average_albedo_recorded,
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


PRIORS = {
    # Well-established facts or strong experimental observations
    bifacial_gain_background: (
        0.85,
        "Well-established knowledge about bifacial silicon solar cell advantage, supported by extensive literature.",
    ),
    small_cell_front_pce: (
        0.90,
        "Directly measured experimental result from champion small cell with clear protocol.",
    ),
    small_cell_rear_pce: (
        0.90,
        "Directly measured experimental result from champion small cell with clear protocol.",
    ),
    nrel_certified_front_efficiency: (
        0.95,
        "NREL-certified measurement - highest confidence due to independent third-party verification.",
    ),
    nrel_certified_rear_efficiency: (
        0.95,
        "NREL-certified measurement - highest confidence due to independent third-party verification.",
    ),
    initial_pce_retention_6000h: (
        0.90,
        "Directly measured stability data with clear protocol and long duration.",
    ),
    optimal_ag_grid_spacing: (
        0.85,
        "Simulation result validated by experimental measurement of resistance and FF.",
    ),
    relative_pce_loss_reduction: (
        0.85,
        "Modeling result with experimental validation through FF improvement.",
    ),
    ff_improvement_with_ag_grid: (
        0.90,
        "Directly measured fill factor values with clear before-after comparison.",
    ),
    ff_improvement_tpfb: (
        0.90,
        "Directly measured fill factor improvement with statistical validation across 14 samples.",
    ),
    tpfb_spread_to_perovskite: (
        0.85,
        "XPS measurement providing direct compositional evidence of TPFB spreading.",
    ),
    hydrophobic_surface_confirmation: (
        0.85,
        "Direct contact angle measurement providing physical evidence of hydrophobicity change.",
    ),
    tpfb_reduced_trap_density: (
        0.85,
        "Direct measurement of trap density via dark injection Current-Voltage analysis.",
    ),
    jsc_increase_with_optimal_np: (
        0.90,
        "Direct Jsc measurement across 14 samples with clear statistical improvement.",
    ),
    front_pce_improvement_with_np: (
        0.90,
        "Direct efficiency measurement from I-V curves with champion cell reporting.",
    ),
    average_front_efficiency_8_modules: (
        0.85,
        "Statistical data from 8 independently fabricated modules showing good reproducibility.",
    ),
    average_rear_efficiency_8_modules: (
        0.85,
        "Statistical data from 8 independently fabricated modules showing good reproducibility.",
    ),
    # Supported by evidence but imperfect or single-source
    optimal_np_size_range: (
        0.80,
        "FDTD simulation result requiring correct material optical constants.",
    ),
    optimal_np_spacing_range: (
        0.80,
        "Simulation result with experimental validation but narrow parameter space studied.",
    ),
    simulated_pgds_by_albedo: (
        0.80,
        "Simulation based on validated device model but depends on albedo assumptions.",
    ),
    sio2_np_light_scattering: (
        0.85,
        "Mie scattering is well-established physics, application to this system is novel.",
    ),
    np_synthesis_and_embedding: (
        0.85,
        "Direct SEM imaging confirms embedding and spacing, but concentration optimization is empirical.",
    ),
    no_extra_recombination_from_np: (
        0.85,
        "PL intensity and lifetime measurements support no additional recombination, but indirect evidence.",
    ),
    power_generation_density_albedo_02: (
        0.85,
        "Calculated from direct Jsc and efficiency measurements with known albedo.",
    ),
    tpfb_frei_level_ptaa: (
        0.85,
        "Direct UPS measurement of Fermi level shift with clear methodology.",
    ),
    tpfb_in_htl_protection: (
        0.85,
        "Accelerated moisture test shows clear protective effect, reproducibility demonstrated.",
    ),
    minimodule_front_aperture_efficiency: (
        0.90,
        "Directly measured aperture efficiency with clear area definition and I-V characterization.",
    ),
    minimodule_rear_aperture_efficiency: (
        0.90,
        "Directly measured aperture efficiency with clear area definition and I-V characterization.",
    ),
    ald_sno2_stabilization_benefit: (
        0.80,
        "Reasoned explanation based on multiple observations including PL imaging and BCP recrystallization.",
    ),
    stability_benefits_composition: (
        0.80,
        "Reasoned conclusion based on comparison with previous literature on FA-Cs composition stability.",
    ),
    ag_grid_design: (
        0.85,
        "Well-established engineering principle validated by extensive modeling and experimental FF data.",
    ),
    pgd_by_albedo: (
        0.85,
        "Calculated from direct efficiency measurements at multiple albedos with controlled LED calibration.",
    ),
    damp_heat_retention: (
        0.80,
        "Direct measured data from damp-heat test chamber with controlled temperature and humidity.",
    ),
    tpfb_passivation_effect: (
        0.85,
        "Direct PL measurement showing increased intensity and lifetime, supported by trap density data.",
    ),
    tpfb_enhanced_stability: (
        0.80,
        "Accelerated stability test under light soaking with comparison to control samples.",
    ),
    jsc_reduction_without_reflective_electrode: (
        0.85,
        "Calculated estimate based on optical absorption differences, consistent with observed Jsc values.",
    ),
    module_structure_p_i_n: (
        0.90,
        "Device structure clearly described with layer-by-layer composition and thickness.",
    ),
    ito_sheet_resistance: (
        0.85,
        "Direct four-point probe measurement providing sheet resistance and transmittance.",
    ),
    ald_damage_to_perovskite: (
        0.85,
        "Direct SEM imaging and XRD evidence of perovskite degradation after ALD process.",
    ),
    absorption_enhancement_simulation: (
        0.80,
        "FDTD simulation validated by experimental absorption measurements.",
    ),
    # Additional motivation claims
    perovskite_bifacial_challenge: (
        0.90,
        "Literature-supported description of challenges common to bifacial perovskite development.",
    ),
    research_objective: (
        0.90,
        "Clear statement of research intent with quantitative targets and achieved outcomes.",
    ),
    bifaciality_measurement: (
        0.85,
        "Bifaciality calculated from independently measured front and rear efficiencies.",
    ),
    initial_efficiency_retention: (
        0.90,
        "Direct measurement of efficiency retention over extended light soaking duration.",
    ),
    average_albedo_recorded: (
        0.85,
        "Literature-supported albedo values from multiple geographic locations.",
    ),
    bifaciality_small_cell: (
        0.90,
        "Calculated from directly measured front and rear efficiencies with clear method.",
    ),
}