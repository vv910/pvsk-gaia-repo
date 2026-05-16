"""
Burschka2013: Sequential deposition as a route to high-performance perovskite-sensitized solar cells.

This Gaia knowledge package formalizes the 2013 Nature paper by Burschka et al.
demonstrating a sequential deposition method for high-performance perovskite solar cells.
"""

from gaia.lang import claim, setting, support, infer

# Import all module exports
from .motivation import (
    perovskite_definition,
    prior_work_limitation,
    sequential_deposition_introduced,
    control_improvement,
    efficiency_achieved,
    reproducibility_improvement,
)

from .s2_methods import (
    device_structure,
    mesoporous_tio2_deposition,
    pbi2_infiltration,
    mai_conversion,
    htm_deposition,
    best_device_modification,
    j_v_measurement,
    ipce_measurement,
    stability_testing,
    optical_spectroscopy,
    xrd_measurement,
)

from .s3_results import (
    pbi2_complete_infiltration,
    pbi2_crystal_size,
    color_change_observed,
    absorption_increase,
    pl_quenching_pbi2,
    perovskite_pl_increase,
    pbi2_tio2_orientation,
    perovskite_xrd_confirmed,
    flat_substrate_incomplete_conversion,
    conversion_rate_enhancement,
    nanomorphology_enforced,
    typical_device_performance,
    device_batch_statistics,
    performance_table,
    ipce_onset,
    ipce_peak_value,
    integrated_current_match,
    lhe_data,
    apce_exceeds_90_percent,
    best_device_performance,
    certified_efficiency,
    best_device_improvement_attributed,
    stability_result,
    no_photodegradation,
    pce_decrease_mechanism,
)

from .s4_discussion import (
    conversion_facilitation,
    nanomorphology_enforcement,
    layered_pbi2_structure,
    thermodynamic_driving_force,
    reaction_kinetics_enhancement,
    two_step_method_applicability,
    record_efficiency,
    reproducibility_demonstrated,
    future_potential,
)

# ============================================================================
# REASONING STRATEGIES
# ============================================================================

# Support strategy: sequential deposition method enables better morphology control
strat_seq_deposition_supports_control = support(
    [sequential_deposition_introduced, pbi2_complete_infiltration],
    control_improvement,
    reason="The sequential method infiltrates PbI2 into TiO2 nanopores first, then converts "
          "in place. This prevents uncontrolled precipitation that causes morphological "
          "variations in single-step deposition (@prior_work_limitation). The complete "
          "infiltration shown by SEM confirms uniform loading within the porous structure.",
    prior=0.85,
)

# Support strategy: nanoporous confinement enables rapid complete conversion
strat_confinement_supports_conversion = support(
    [pbi2_crystal_size, perovskite_xrd_confirmed, flat_substrate_incomplete_conversion],
    conversion_rate_enhancement,
    reason="The 22 nm crystal size confined in TiO2 pores converts completely within seconds "
          "(@perovskite_xrd_confirmed), while flat substrates with 50-200 nm crystallites "
          "show incomplete conversion even after 45 min (@flat_substrate_incomplete_conversion). "
          "This demonstrates that nanoscopic confinement drastically accelerates conversion.",
    prior=0.9,
)

# Support strategy: improved morphology leads to higher efficiency
strat_morphology_supports_efficiency = support(
    [control_improvement, conversion_rate_enhancement],
    efficiency_achieved,
    reason="Better morphology control (@control_improvement) and rapid complete conversion "
          "(@conversion_rate_enhancement) produce uniform perovskite films with optimal "
          "light harvesting and charge collection, enabling the reported 15% PCE. "
          "The certified 14.14% (@certified_efficiency) confirms this performance.",
    prior=0.85,
)

# Support strategy: reproducibility from controlled morphology
strat_reproducibility = support(
    [device_batch_statistics, control_improvement],
    reproducibility_improvement,
    reason="The batch average of 12.0% with standard deviation of only 0.5% (@device_batch_statistics) "
          "demonstrates excellent reproducibility. This stems from the controlled morphology "
          "(@control_improvement) that eliminates the wide performance spread seen in "
          "single-step deposition.",
    prior=0.9,
)

# Support strategy: explanation for high photocurrent in best devices
strat_loading_supports_current = support(
    [best_device_modification, best_device_improvement_attributed],
    best_device_performance,
    reason="The modified conditions (shorter spin-cast time and pre-wetting) increase perovskite "
          "loading in the TiO2 pores and enhance light scattering (@best_device_improvement_attributed). "
          "This produces the higher Jsc of 20.0 mA/cm^2 and 15.0% PCE (@best_device_performance).",
    prior=0.8,
)

# Support strategy: stability without photodegradation
strat_stability = support(
    [stability_result, no_photodegradation],
    pce_decrease_mechanism,
    reason="After 500 hours of light soaking, the device retains >80% PCE (@stability_result) "
          "with no change in Jsc (@no_photodegradation), confirming the perovskite is stable. "
          "The PCE decrease is attributed to shunt resistance loss affecting Voc and FF, "
          "not to light harvester degradation.",
    prior=0.85,
)

# Support strategy: mechanism of fast conversion
strat_mechanism_supports_rate = support(
    [layered_pbi2_structure, thermodynamic_driving_force, reaction_kinetics_enhancement],
    conversion_facilitation,
    reason="The layered I-Pb-I structure of PbI2 (@layered_pbi2_structure) allows easy cation "
          "insertion between layers. The large lattice energy difference (@thermodynamic_driving_force) "
          "provides the driving force, and the 22 nm crystal size (@reaction_kinetics_enhancement) "
          "greatly enhances kinetics, together explaining the rapid complete conversion.",
    prior=0.85,
)

# Support strategy: high IPCE and APCE demonstrate quality
strat_quantum_yield = support(
    [ipce_peak_value, apce_exceeds_90_percent],
    integrated_current_match,
    reason="Peak IPCE >90% (@ipce_peak_value) and APCE >90% across visible range "
          "(@apce_exceeds_90_percent) demonstrate near-unity quantum yield for carrier "
          "generation and collection. This explains why the integrated current (18.4 mA/cm^2) "
          "matches the measured Jsc.",
    prior=0.9,
)

__all__ = [
    # From motivation
    "perovskite_definition",
    "prior_work_limitation",
    "sequential_deposition_introduced",
    "control_improvement",
    "efficiency_achieved",
    "reproducibility_improvement",
    # From s2_methods
    "device_structure",
    "mesoporous_tio2_deposition",
    "pbi2_infiltration",
    "mai_conversion",
    "htm_deposition",
    "best_device_modification",
    "j_v_measurement",
    "ipce_measurement",
    "stability_testing",
    "optical_spectroscopy",
    "xrd_measurement",
    # From s3_results
    "pbi2_complete_infiltration",
    "pbi2_crystal_size",
    "color_change_observed",
    "absorption_increase",
    "pl_quenching_pbi2",
    "perovskite_pl_increase",
    "pbi2_tio2_orientation",
    "perovskite_xrd_confirmed",
    "flat_substrate_incomplete_conversion",
    "conversion_rate_enhancement",
    "nanomorphology_enforced",
    "typical_device_performance",
    "device_batch_statistics",
    "performance_table",
    "ipce_onset",
    "ipce_peak_value",
    "integrated_current_match",
    "lhe_data",
    "apce_exceeds_90_percent",
    "best_device_performance",
    "certified_efficiency",
    "best_device_improvement_attributed",
    "stability_result",
    "no_photodegradation",
    "pce_decrease_mechanism",
    # From s4_discussion
    "conversion_facilitation",
    "nanomorphology_enforcement",
    "layered_pbi2_structure",
    "thermodynamic_driving_force",
    "reaction_kinetics_enhancement",
    "two_step_method_applicability",
    "record_efficiency",
    "reproducibility_demonstrated",
    "future_potential",
    # Strategies
    "strat_seq_deposition_supports_control",
    "strat_confinement_supports_conversion",
    "strat_morphology_supports_efficiency",
    "strat_reproducibility",
    "strat_loading_supports_current",
    "strat_stability",
    "strat_mechanism_supports_rate",
    "strat_quantum_yield",
]