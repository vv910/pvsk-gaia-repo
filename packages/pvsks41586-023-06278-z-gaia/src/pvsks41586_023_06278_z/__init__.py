"""
All-perovskite tandem solar cells with 3D/3D bilayer perovskite heterojunction.

Lin et al., Nature (2023) - https://doi.org/10.1038/s41586-023-06278-z

This package formalizes the knowledge from this paper about 3D/3D bilayer
perovskite heterojunctions for high-efficiency all-perovskite tandem solar cells.
"""

from gaia.lang import (
    claim,
    setting,
    question,
)

# Import all modules
from . import motivation
from . import s2_methods
from . import s3_results
from . import s4_discussion
from . import strategies

# Re-export for convenience
from .motivation import (
    tandem_configuration,
    performance_potential,
    previous_limitation,
    two_d_three_d_problem,
    surface_passivation_tradeoff,
    phj_solution,
    type_two_band_alignment,
    bilateral_improvement,
    hybrid_deposition_method,
    ion_immiscibility,
    nbg_champion_pce,
    nbg_average_improvement,
    mechanism_question,
    tandem_question,
)

from .s2_methods import (
    device_architecture,
    fl_wbg_composition,
    nbg_composition,
    inorganic_layer_deposition,
    organic_salt_deposition,
    peai_post_treatment,
    morphology_method,
    heterojunction_verification,
    phj_layer_thickness,
    ion_distribution_stability,
    work_functions,
    bandgaps,
    jv_measurement,
    eqe_measurement,
)

from .s3_results import (
    control_vs_phj_comparison,
    device_statistics,
    champion_device,
    eqe_validation,
    pl_intensity_increase,
    trapped_reduction,
    built_in_potential,
    el_qy_comparison,
    voc_loss_reduction,
    trpl_phj_film,
    trpl_control_film,
    electron_transfer_rate,
    control_ta_spectrum,
    phj_ta_nbg_pumped,
    phj_ta_fl_wbg_pumped,
    wbg_subcell_performance,
    nbg_subcell_in_tandem,
    tandem_ff_improvement,
    tandem_champion,
    eqe_tandem,
    certified_efficiency,
    large_area_tandem,
    operational_stability,
    degradation_mechanism,
    reverse_bias_stability,
    simulation_model,
    dil_trap_density_effect,
    dil_thickness_effect,
    simulated_improvement,
)

from .s4_discussion import (
    type_ii_mechanism,
    depletion_region,
    charge_separation,
    electron_extraction_acceleration,
    two_d_layer_limitation,
    three_d_advantage,
    remaining_voc_ff_loss,
    optical_losses,
    future_improvement_path,
    long_term_stability,
    thermal_stability_note,
    bromide_migration,
    record_efficiency,
    bilateral_voc_ff,
    solution_processadvantage,
)

__all__ = [
    # From motivation
    "tandem_configuration",
    "performance_potential",
    "previous_limitation",
    "two_d_three_d_problem",
    "surface_passivation_tradeoff",
    "phj_solution",
    "type_two_band_alignment",
    "bilateral_improvement",
    "hybrid_deposition_method",
    "ion_immiscibility",
    "nbg_champion_pce",
    "nbg_average_improvement",
    "mechanism_question",
    "tandem_question",
    # From s2_methods
    "device_architecture",
    "fl_wbg_composition",
    "nbg_composition",
    "inorganic_layer_deposition",
    "organic_salt_deposition",
    "peai_post_treatment",
    "morphology_method",
    "heterojunction_verification",
    "phj_layer_thickness",
    "ion_distribution_stability",
    "work_functions",
    "bandgaps",
    "jv_measurement",
    "eqe_measurement",
    # From s3_results
    "control_vs_phj_comparison",
    "device_statistics",
    "champion_device",
    "eqe_validation",
    "pl_intensity_increase",
    "trapped_reduction",
    "built_in_potential",
    "el_qy_comparison",
    "voc_loss_reduction",
    "trpl_phj_film",
    "trpl_control_film",
    "electron_transfer_rate",
    "control_ta_spectrum",
    "phj_ta_nbg_pumped",
    "phj_ta_fl_wbg_pumped",
    "wbg_subcell_performance",
    "nbg_subcell_in_tandem",
    "tandem_ff_improvement",
    "tandem_champion",
    "eqe_tandem",
    "certified_efficiency",
    "large_area_tandem",
    "operational_stability",
    "degradation_mechanism",
    "reverse_bias_stability",
    "simulation_model",
    "dil_trap_density_effect",
    "dil_thickness_effect",
    "simulated_improvement",
    # From s4_discussion
    "type_ii_mechanism",
    "depletion_region",
    "charge_separation",
    "electron_extraction_acceleration",
    "two_d_layer_limitation",
    "three_d_advantage",
    "remaining_voc_ff_loss",
    "optical_losses",
    "future_improvement_path",
    "long_term_stability",
    "thermal_stability_note",
    "bromide_migration",
    "record_efficiency",
    "bilateral_voc_ff",
    "solution_processadvantage",
]