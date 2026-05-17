"""
Gaia knowledge package for Jia2025: Efficient perovskite/silicon tandem with asymmetric self-assembly molecule.
"""

from gaia.lang import claim, setting

from .motivation import (
    perovskite_silicon_tscs_introduced,
    single_junction_plateau,
    voc_loss_problem,
    sam_advantages,
    existing_sams_limitation,
    research_objective,
    htl201_introduced,
    htl201_design_features,
    htl201_outcome,
    certified_pce_result,
)

from .s2_molecular_design import (
    asymmetric_design,
    htl201_chemical_verification,
    reference_sams,
    thermal_stability,
    homo_energy_levels,
)

from .s3_interface_interactions import (
    izo_htl201_strong_interaction,
    htl201_stronger_affinity,
    htl201_higher_fractional_coverage,
    coverage_factors_before_wash,
    coverage_factors_stable,
    htl201_higher_coverage_factor,
    sam_thickness_comparable_to_molecule_length,
    htl201_strong_binding_perovskite,
    htl201_passivates_pb_defects,
)

from .s4_photovoltaic_performance import (
    device_configuration,
    htl201_average_pce,
    htl201_champion_pce,
    me4pacz_average_pce,
    htl201_enhanced_voc_ff,
    eqe_integrated_current,
    certified_pce_34_58,
    htl201_derivatives_also_good,
)

from .s5_morphology_crystallinity import (
    water_contact_angles,
    perovskite_precursor_contact,
    htl201_smooth_uniform,
    htl201_perovskite_dense_uniform,
    perovskite_thickness,
    htl201_enhanced_crystallinity,
    htl201_delayed_nucleation,
)

from .s6_charge_dynamics import (
    htl201_brighter_pl_mapping,
    pl_peak_at_733nm,
    htl201_higher_carrier_lifetime,
    htl201_most_significant_pb_shift,
    plqry_values,
    qfls_values,
    ups_valence_band,
    homo_levels_by_ups,
    htl201_minimal_energy_difference,
    htl201_highest_conducting_current,
    htl201_smaller_pff_ff_difference,
    htl201_lower_reverse_saturation,
)

from .s7_stability import (
    htl201_shelf_life_98_9_percent,
    htl201_operational_25c_98_percent,
    htl201_operational_45c_91_3_percent,
    meo4pacz_operational_stability,
    me4pacz_significant_decline,
    htl201_better_electrochemical_stability,
    all_sams_good_photostability,
    htl201_impeded_leakage_reduced_recombination,
)

from .s8_strategies import (
    strat_asymmetric_supports_coverage,
    strat_coverage_supports_morphology,
    strat_binding_supports_passivation,
    strat_energy_supports_voc_ff,
    strat_charge_supports_pce,
    strat_stability_supports_longevity,
    strat_htl201_outperforms,
    strat_qfls_supports_voc,
)

__all__ = [
    # motivation
    "perovskite_silicon_tscs_introduced",
    "single_junction_plateau",
    "voc_loss_problem",
    "sam_advantages",
    "existing_sams_limitation",
    "research_objective",
    "htl201_introduced",
    "htl201_design_features",
    "htl201_outcome",
    "certified_pce_result",
    # s2_molecular_design
    "asymmetric_design",
    "htl201_chemical_verification",
    "reference_sams",
    "thermal_stability",
    "homo_energy_levels",
    # s3_interface_interactions
    "izo_htl201_strong_interaction",
    "htl201_stronger_affinity",
    "htl201_higher_fractional_coverage",
    "coverage_factors_before_wash",
    "coverage_factors_stable",
    "htl201_higher_coverage_factor",
    "sam_thickness_comparable_to_molecule_length",
    "htl201_strong_binding_perovskite",
    "htl201_passivates_pb_defects",
    # s4_photovoltaic_performance
    "device_configuration",
    "htl201_average_pce",
    "htl201_champion_pce",
    "me4pacz_average_pce",
    "htl201_enhanced_voc_ff",
    "eqe_integrated_current",
    "certified_pce_34_58",
    "htl201_derivatives_also_good",
    # s5_morphology_crystallinity
    "water_contact_angles",
    "perovskite_precursor_contact",
    "htl201_smooth_uniform",
    "htl201_perovskite_dense_uniform",
    "perovskite_thickness",
    "htl201_enhanced_crystallinity",
    "htl201_delayed_nucleation",
    # s6_charge_dynamics
    "htl201_brighter_pl_mapping",
    "pl_peak_at_733nm",
    "htl201_higher_carrier_lifetime",
    "htl201_most_significant_pb_shift",
    "plqry_values",
    "qfls_values",
    "ups_valence_band",
    "homo_levels_by_ups",
    "htl201_minimal_energy_difference",
    "htl201_highest_conducting_current",
    "htl201_smaller_pff_ff_difference",
    "htl201_lower_reverse_saturation",
    # s7_stability
    "htl201_shelf_life_98_9_percent",
    "htl201_operational_25c_98_percent",
    "htl201_operational_45c_91_3_percent",
    "meo4pacz_operational_stability",
    "me4pacz_significant_decline",
    "htl201_better_electrochemical_stability",
    "all_sams_good_photostability",
    "htl201_impeded_leakage_reduced_recombination",
    # s8_strategies
    "strat_asymmetric_supports_coverage",
    "strat_coverage_supports_morphology",
    "strat_binding_supports_passivation",
    "strat_energy_supports_voc_ff",
    "strat_charge_supports_pce",
    "strat_stability_supports_longevity",
    "strat_htl201_outperforms",
    "strat_qfls_supports_voc",
]