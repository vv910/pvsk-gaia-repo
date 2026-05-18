"""
S3: Mechanistic tensions and their synthesis-level resolutions.

Most cross-paper differences here are conditional tensions rather than strict
logical contradictions.  They are therefore modeled as claims supported by the
conflicting-looking evidence, not with contradiction() or complement().
"""

from gaia.lang import claim, support

from ._imports import (
    pvsk2009_durability,
    pvsk2012_1_stability,
    pvsk2012_2_planar,
    pvsknature12509_planar_efficiency,
    pvsknature12509_uniformity,
    pvsk2013_sequential_deposition,
    pvsk2014_hysteresis_origin,
    pvsk2014_negligible_hysteresis,
    pvsk2015_phase_stabilization,
    pvsk_triple_cation_strategy,
    pvsk2017_hysteresis,
    pvsk2017_2d3d_composite,
    pvsk_mda_alpha_stabilization,
    pvsk_damp_heat_dual_passivation,
    pvsk_all_inorganic_ion_migration,
    pvsk_formate_interfaces,
    pvsk_formate_recombination_reduction,
    pvsk_persik_2024_edai_tradeoff,
    pvsk_persik_2024_no_tradeoff,
    pvsk_persik_2024_passivation_tradeoff,
    pvsk_dmdp_dual_concept,
    pvsk_dmdp_field_effect,
    pvsk_dmdp_chemical_passivation,
    pvsk_dmdp_single_molecule_limit,
    pvsk_dipolar_conventional_limit,
    pvsk_dipolar_strategy,
)


tension_liquid_vs_solid_stability = claim(
    "Early liquid-electrolyte instability and later solid-state stability are a "
    "device-architecture tension rather than a contradiction about the absorber.",
    title="Liquid and solid-state stability claims are architecture-dependent",
)

strat_tension_liquid_vs_solid_stability = support(
    [pvsk2009_durability, pvsk2012_1_stability],
    tension_liquid_vs_solid_stability,
    reason=(
        "The 2009 decay observation and the 2012 stability improvement can both be "
        "true because the electrolyte and solid-state device stacks impose different "
        "chemical environments."
    ),
    prior=0.89,
)


tension_hysteresis_has_multiple_sources = claim(
    "Hysteresis evidence is best read as a multi-source mechanism involving ion "
    "migration, delayed polarization, and interface recombination rather than a "
    "single universal cause.",
    title="Hysteresis has multiple context-dependent sources",
)

strat_tension_hysteresis_has_multiple_sources = support(
    [
        pvsk2014_hysteresis_origin,
        pvsk2014_negligible_hysteresis,
        pvsk2017_hysteresis,
        pvsk2017_2d3d_composite,
    ],
    tension_hysteresis_has_multiple_sources,
    reason=(
        "Jeon 2014 and Grancini 2017 emphasize different control levers, but both "
        "link hysteresis suppression to architecture and interface conditions."
    ),
    prior=0.82,
)


tension_planar_vs_meso_is_process_dependent = claim(
    "Planar and mesoporous architectures are not globally ranked; their relative "
    "performance depends on deposition route, film coverage, and transport design.",
    title="Planar versus mesoporous preference is process-dependent",
)

strat_tension_planar_vs_meso_is_process_dependent = support(
    [pvsk2012_2_planar, pvsknature12509_planar_efficiency, pvsknature12509_uniformity],
    tension_planar_vs_meso_is_process_dependent,
    reason=(
        "Lee 2012's meso-superstructured result and Liu 2013's planar vapour result "
        "can coexist because vapour deposition changes the film-uniformity constraint."
    ),
    prior=0.80,
)


tension_solution_vs_vapour_control = claim(
    "Sequential solution processing and vapour deposition emphasize different film "
    "quality controls: conversion chemistry versus uniform physical deposition.",
    title="Solution and vapour deposition optimize different controls",
)

strat_tension_solution_vs_vapour_control = support(
    [pvsk2013_sequential_deposition, pvsknature12509_uniformity],
    tension_solution_vs_vapour_control,
    reason=(
        "Sequential deposition and vapour deposition both improve film quality, but "
        "through distinct control variables."
    ),
    prior=0.78,
)


tension_passivation_mechanisms_are_complementary = claim(
    "Chemical bonding, field-effect passivation, dimensional barriers, and dipolar "
    "alignment are complementary interface mechanisms rather than mutually exclusive "
    "explanations.",
    title="Passivation mechanisms are complementary",
)

strat_tension_passivation_mechanisms_are_complementary = support(
    [
        pvsk_formate_interfaces,
        pvsk_formate_recombination_reduction,
        pvsk_dmdp_field_effect,
        pvsk_dmdp_chemical_passivation,
        pvsk_damp_heat_dual_passivation,
        pvsk_dipolar_strategy,
    ],
    tension_passivation_mechanisms_are_complementary,
    reason=(
        "Formate, DMDP, tailored-dimensionality, and dipolar packages act on "
        "different interface degrees of freedom, so their mechanisms can reinforce "
        "rather than exclude each other."
    ),
    prior=0.86,
)


tension_passivation_transport_tradeoff_is_conditional = claim(
    "The passivation-versus-transport trade-off is conditional: some passivators "
    "raise voltage while hurting fill factor, whereas bilayer or dual-function "
    "strategies can reduce recombination without the same transport penalty.",
    title="Passivation-transport trade-off is conditional",
)

strat_tension_passivation_transport_tradeoff_is_conditional = support(
    [
        pvsk_persik_2024_passivation_tradeoff,
        pvsk_persik_2024_edai_tradeoff,
        pvsk_persik_2024_no_tradeoff,
        pvsk_dmdp_single_molecule_limit,
        pvsk_dmdp_dual_concept,
    ],
    tension_passivation_transport_tradeoff_is_conditional,
    reason=(
        "The EDAI-only trade-off and the later no-trade-off or dual-passivation "
        "results are compatible when passivator geometry and transport contact are "
        "treated as conditions."
    ),
    prior=0.84,
)


tension_stability_routes_are_condition_specific = claim(
    "Stability strategies are condition-specific: mixed cations, 2D/3D barriers, "
    "all-inorganic capping, and MDA stabilization target different degradation "
    "drivers.",
    title="Stability routes are condition-specific",
)

strat_tension_stability_routes_are_condition_specific = support(
    [
        pvsk2015_phase_stabilization,
        pvsk_triple_cation_strategy,
        pvsk_mda_alpha_stabilization,
        pvsk_damp_heat_dual_passivation,
        pvsk_all_inorganic_ion_migration,
    ],
    tension_stability_routes_are_condition_specific,
    reason=(
        "The stability packages do not identify one exhaustive route; they target "
        "phase instability, moisture/oxygen ingress, and ion migration under "
        "different test conditions."
    ),
    prior=0.85,
)


tension_conventional_vs_dipolar_buried_passivation = claim(
    "Conventional buried-interface passivation is insufficient for some tandem "
    "conditions, while dipolar passivation addresses electrostatic alignment and "
    "charge extraction more directly.",
    title="Conventional and dipolar buried passivation differ by target mechanism",
)

strat_tension_conventional_vs_dipolar_buried_passivation = support(
    [pvsk_dipolar_conventional_limit, pvsk_dipolar_strategy],
    tension_conventional_vs_dipolar_buried_passivation,
    reason=(
        "The dipolar package frames the conflict as a limitation of conventional "
        "passivation under buried-interface tandem constraints, not a universal "
        "contradiction between all passivation approaches."
    ),
    prior=0.82,
)
