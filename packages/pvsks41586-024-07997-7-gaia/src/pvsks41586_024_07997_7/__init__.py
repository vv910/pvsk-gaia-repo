"""
pvsks41586-024-07997-7-gaia - Perovskite/silicon tandem solar cells with bilayer interface passivation

This package formalizes the knowledge from the paper:
- Title: Perovskite/silicon tandem solar cells with bilayer interface passivation
- DOI: 10.1038/s41586-024-07997-7
- Authors: Jiang Liu et al.
- Published: 5 September 2024

Main conclusion: A bilayer interface passivation strategy (LiF/EDAI) achieving 33.89% certified PCE,
first double-junction tandem to exceed the Shockley-Queisser limit.
"""

from gaia.lang import (
    claim,
    setting,
    question,
    support,
    infer,
)

from .motivation import (
    csi_solar_cell_dominance,
    auger_recombination_limit,
    tandem_strategy,
    pin_interface_recombination,
    passivation_tradeoff,
    research_question,
    bilateral_passivation_strategy,
    lif_limited_effectiveness,
    edai_chemical_passivation,
    nanoscale_contact_requirement,
    double_textured_silicon,
    champion_device_performance,
    strat_bilayer_strategy,
    strat_nanoscale_requirement,
    strat_double_texture,
)

from .s3_results import (
    pl_intensity_ranking,
    plqy_increase_with_c60,
    plqy_with_complete_top_contact,
    trpl_lifetime_results,
    passivation_targets_perovskite_c60,
    single_junction_device_results,
    pseudo_ff_values,
    power_loss_analysis,
    tof_sims_lif_distribution,
    tof_sims_edai_distribution,
    lif_discontinuity_confirmation,
    kpfm_surface_potential,
    electric_field_enhancement,
    xps_pb4f_shift,
    metallic_pb_suppression,
    xps_n1s_results,
    work_function_reduction,
    fermi_level_to_valence_band,
    ionization_potential_slight_increase,
    c60_interface_ie_variation,
    dft_slab_structures,
    pa_vs_eda_orientation,
    binding_energy_comparison,
    trap_state_elimination,
    textured_substrate_optimization,
    minority_carrier_lifetime,
    eqe_spectral_response,
    voc_statistical_improvement,
    fill_factor_improvement,
    champion_device_jv,
    stabilized_power_output,
    nrel_certified_pce,
    storage_stability,
    operational_stability,
    theoretical_prediction_lif_only,
    theoretical_prediction_edai_only,
    theoretical_prediction_bilayer,
    s_lif,
    s_edai,
    s_bilayer,
    comp_passivation,
    comp_voc,
    abduction_bilayer,
    abduction_voc,
    edai_ff_tradeoff,
    bilayer_no_tradeoff,
    contradiction_passivation_transport,
)

from .s4_discussion import (
    bilayer_mechanism_synthesis,
    nanoscale_contact_design,
    asymmetric_texture_benefits,
    first_to_exceed_sq_limit,
    stability_implications,
    strat_bilayer_mechanism,
    strat_nanoscale,
    strat_texture,
    strat_certified,
    strat_stability,
)

__all__ = [
    # Background settings
    "csi_solar_cell_dominance",
    "auger_recombination_limit",
    "tandem_strategy",
    "pin_interface_recombination",
    "passivation_tradeoff",
    # Research question
    "research_question",
    # Core claims
    "bilateral_passivation_strategy",
    "lif_limited_effectiveness",
    "edai_chemical_passivation",
    "nanoscale_contact_requirement",
    "double_textured_silicon",
    "champion_device_performance",
    # Strategies
    "strat_bilayer_strategy",
    "strat_nanoscale_requirement",
    "strat_double_texture",
    # Results claims (key ones)
    "pl_intensity_ranking",
    "plqy_increase_with_c60",
    "plqy_with_complete_top_contact",
    "trpl_lifetime_results",
    "single_junction_device_results",
    "power_loss_analysis",
    "lif_discontinuity_confirmation",
    "electric_field_enhancement",
    "metallic_pb_suppression",
    "pa_vs_eda_orientation",
    "binding_energy_comparison",
    "trap_state_elimination",
    "minority_carrier_lifetime",
    "eqe_spectral_response",
    "voc_statistical_improvement",
    "champion_device_jv",
    "nrel_certified_pce",
    "storage_stability",
    "operational_stability",
    # Abduction/Comparison strategies
    "theoretical_prediction_bilayer",
    "s_bilayer",
    "comp_passivation",
    "comp_voc",
    "abduction_bilayer",
    "abduction_voc",
    # Contradiction
    "edai_ff_tradeoff",
    "bilayer_no_tradeoff",
    "contradiction_passivation_transport",
    # Discussion synthesis
    "bilayer_mechanism_synthesis",
    "nanoscale_contact_design",
    "asymmetric_texture_benefits",
    "first_to_exceed_sq_limit",
    "stability_implications",
    "strat_bilayer_mechanism",
    "strat_nanoscale",
    "strat_texture",
    "strat_certified",
    "strat_stability",
]