"""
Gaia knowledge package for Lin2025: All-perovskite tandem solar cells with dipolar passivation.
Nature, 2025. https://doi.org/10.1038/s41586-025-09773-7

Exported conclusions from this paper's knowledge formalization.
"""

from gaia.lang import claim, setting, question

# Motivation - core problem and solution
from .motivation import (
    all_perovskite_tandem_description,
    buried_interface_recombination,
    conventional_passivation_limitation,
    optimal_buried_passivation_requirement,
    dipolar_passivation_strategy,
    sa_dipole_moment,
    diffusion_length_enhancement,
    pb_sn_psc_performance,
    tandem_performance,
)

# Methods - device structure and dipolar passivation design
from .s2_methods import (
    device_structure,
    dipolar_passivation_design,
    tof_simms_analysis,
    xps_evidence,
    aimd_molecular_orientation,
    kpfm_potential_change,
    energy_level_alignment,
    type_ii_energy_alignment,
)

# Results - charge-carrier dynamics and performance
from .s3_results import (
    steady_state_pl,
    trpl_decay_components,
    enhanced_charge_extraction,
    terahertz_mobility,
    limiting_carrier_mobility,
    diffusion_length,
    electroluminescence_qy,
    average_voc_improvement,
    qfis_values,
    single_junction_metrics,
    pcce_histogram,
    operational_stability,
)

# Discussion - tandem cells and stability
from .s4_discussion import (
    tandem_device_configuration,
    tandem_buried_interface_challenge,
    tandem_sensitivity_reduction,
    tandem_pv_parameters,
    champion_tandem_device,
    jet_certified_pce,
    large_area_tandem,
    wbg_subcell_performance,
    thickness_optimization,
    contact_loss_mitigation,
    tandem_operational_stability,
    tandem_thermal_stability,
    future_direction,
)

# Strategies - reasoning connections
from .strategies import (
    strat_problem_supports_solution,
    strat_aimd_supports_orientation,
    strat_kpfm_confirms_orientation,
    strat_tof_simms_confirms_sa,
    strat_xps_confirms_sa,
    strat_energy_align_supports_pl,
    strat_energy_align_supports_trpl,
    strat_trpl_supports_extraction,
    strat_terahertz_mobility,
    strat_mobility_supports_diffusion_length,
    strat_pl_supports_el,
    strat_el_supports_voc,
    strat_diffusion_length_supports_qfils,
    strat_diffusion_supports_metrics,
    strat_statistics,
    strat_stability,
    strat_nbg_tandem_challenge,
    strat_contact_loss_mitigation,
    strat_tandem_champion,
    strat_jet_certification,
    strat_large_area,
    strat_operational_stability,
    strat_thermal_stability,
    strat_wbg_performance,
    strat_thickness_balance,
    strat_diff_length_enhancement_supports_main_claim,
    conv_vs_dipolar_contradiction,
)

# Priors
from .priors import PRIORS

__all__ = [
    # Motivation
    "all_perovskite_tandem_description",
    "buried_interface_recombination",
    "conventional_passivation_limitation",
    "optimal_buried_passivation_requirement",
    "dipolar_passivation_strategy",
    "sa_dipole_moment",
    "diffusion_length_enhancement",
    "pb_sn_psc_performance",
    "tandem_performance",
    # Methods
    "device_structure",
    "dipolar_passivation_design",
    "tof_simms_analysis",
    "xps_evidence",
    "aimd_molecular_orientation",
    "kpfm_potential_change",
    "energy_level_alignment",
    "type_ii_energy_alignment",
    # Results
    "steady_state_pl",
    "trpl_decay_components",
    "enhanced_charge_extraction",
    "terahertz_mobility",
    "limiting_carrier_mobility",
    "diffusion_length",
    "electroluminescence_qy",
    "average_voc_improvement",
    "qfis_values",
    "single_junction_metrics",
    "pcce_histogram",
    "operational_stability",
    # Discussion
    "tandem_device_configuration",
    "tandem_buried_interface_challenge",
    "tandem_sensitivity_reduction",
    "tandem_pv_parameters",
    "champion_tandem_device",
    "jet_certified_pce",
    "large_area_tandem",
    "wbg_subcell_performance",
    "thickness_optimization",
    "contact_loss_mitigation",
    "tandem_operational_stability",
    "tandem_thermal_stability",
    "future_direction",
    # Strategies
    "strat_problem_supports_solution",
    "strat_aimd_supports_orientation",
    "strat_kpfm_confirms_orientation",
    "strat_tof_simms_confirms_sa",
    "strat_xps_confirms_sa",
    "strat_energy_align_supports_pl",
    "strat_energy_align_supports_trpl",
    "strat_trpl_supports_extraction",
    "strat_terahertz_mobility",
    "strat_mobility_supports_diffusion_length",
    "strat_pl_supports_el",
    "strat_el_supports_voc",
    "strat_diffusion_length_supports_qfils",
    "strat_diffusion_supports_metrics",
    "strat_statistics",
    "strat_stability",
    "strat_nbg_tandem_challenge",
    "strat_contact_loss_mitigation",
    "strat_tandem_champion",
    "strat_jet_certification",
    "strat_large_area",
    "strat_operational_stability",
    "strat_thermal_stability",
    "strat_wbg_performance",
    "strat_thickness_balance",
    "strat_diff_length_enhancement_supports_main_claim",
    "conv_vs_dipolar_contradiction",
]