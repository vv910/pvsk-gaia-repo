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
    pvsknature12509_vapour_deposition,
    pvsk2013_sequential_deposition,
    pvsk2013_reproducibility,
    pvsk2014_hysteresis_origin,
    pvsk2014_negligible_hysteresis,
    pvsk2015_hysteresis_benefit,
    pvsk2015_phase_stabilization,
    pvsk_triple_cation_strategy,
    pvsk2017_hysteresis,
    pvsk2017_2d3d_composite,
    pvsk_mda_alpha_stabilization,
    pvsk_formate_long_term_stability,
    pvsk_damp_heat_dual_passivation,
    pvsk_damp_heat_iec,
    pvsk_all_inorganic_ion_migration,
    pvsk_all_inorganic_t80,
    pvsk_formate_interfaces,
    pvsk_formate_recombination_reduction,
    pvsk_all_tandem_large_area,
    pvsk_all_tandem_operational_600h,
    pvsk_3d3d_passivation_tradeoff,
    pvsk_persik_2024_edai_tradeoff,
    pvsk_persik_2024_no_tradeoff,
    pvsk_persik_2024_nrel_certified,
    pvsk_persik_2024_passivation_tradeoff,
    pvsk_dmdp_dual_concept,
    pvsk_dmdp_field_effect,
    pvsk_dmdp_chemical_passivation,
    pvsk_dmdp_single_molecule_limit,
    pvsk_dipolar_conventional_limit,
    pvsk_dipolar_buried_recombination,
    pvsk_dipolar_charge_extraction,
    pvsk_dipolar_strategy,
    pvsk_htl201_certified,
    pvsk_htl201_operational_25c,
    pvsk_r2r_cells,
    pvsk_r2r_modules,
    pvsk_r2r_cost_prediction,
    pvsk_r2r_production_cost_power,
    pvsk_r2r_throughput,
    pvsk_bifacial_gain,
    pvsk_bifacial_power_density,
    pvsk_bifacial_nrel_front,
    pvsk_bifacial_6000h,
    pvsk_homogeneous_2d_large_module,
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


planar_vs_mesoporous_is_process_conditioned = claim(
    "Planar and mesoporous device comparisons are process-conditioned: film "
    "coverage, vapor uniformity, and transport-layer design determine which "
    "architecture performs better in a given package.",
    title="Planar versus mesoporous is process-conditioned",
)

strat_planar_vs_mesoporous_is_process_conditioned = support(
    [
        tension_planar_vs_meso_is_process_dependent,
        pvsk2012_2_planar,
        pvsknature12509_uniformity,
    ],
    planar_vs_mesoporous_is_process_conditioned,
    reason=(
        "The older architecture tension becomes a mechanism condition once planar "
        "success is separated from film uniformity and charge-transport constraints."
    ),
    prior=0.84,
)


solution_vs_vapor_deposition_is_scale_quality_tradeoff = claim(
    "Solution and vapor deposition represent a scale-quality trade-off rather "
    "than a universal ranking: solution routes emphasize conversion chemistry and "
    "throughput, while vapor routes emphasize uniform physical coverage.",
    title="Solution versus vapor deposition is a scale-quality trade-off",
)

strat_solution_vs_vapor_deposition_is_scale_quality_tradeoff = support(
    [
        tension_solution_vs_vapour_control,
        pvsk2013_reproducibility,
        pvsknature12509_vapour_deposition,
        pvsk_r2r_cells,
    ],
    solution_vs_vapor_deposition_is_scale_quality_tradeoff,
    reason=(
        "Sequential solution deposition, vapor uniformity, and later roll-to-roll "
        "processing expose different process bottlenecks rather than one dominant "
        "deposition method."
    ),
    prior=0.78,
)


passivation_may_hurt_ff_if_it_blocks_extraction = claim(
    "Passivation can hurt fill factor when the passivating layer or molecule "
    "blocks extraction, thickens the tunneling barrier, or disrupts contact "
    "selectivity.",
    title="Passivation may hurt FF if it blocks extraction",
)

strat_passivation_may_hurt_ff_if_it_blocks_extraction = support(
    [
        pvsk_persik_2024_edai_tradeoff,
        pvsk_persik_2024_passivation_tradeoff,
        pvsk_3d3d_passivation_tradeoff,
        pvsk_dmdp_single_molecule_limit,
    ],
    passivation_may_hurt_ff_if_it_blocks_extraction,
    reason=(
        "Multiple packages report that passivation chemistry alone can introduce "
        "transport penalties or fail without a complementary extraction pathway."
    ),
    prior=0.80,
)


effective_passivation_requires_defect_reduction_without_transport_penalty = claim(
    "Effective passivation requires defect reduction without a transport penalty; "
    "the useful design rule is therefore conditional rather than simply "
    "'add more passivation'.",
    title="Effective passivation avoids a transport penalty",
)

strat_effective_passivation_requires_defect_reduction_without_transport_penalty = support(
    [
        passivation_may_hurt_ff_if_it_blocks_extraction,
        pvsk_persik_2024_no_tradeoff,
        pvsk_dmdp_dual_concept,
        pvsk_dipolar_charge_extraction,
    ],
    effective_passivation_requires_defect_reduction_without_transport_penalty,
    reason=(
        "No-trade-off bilayers, bimolecular passivation, and dipolar charge "
        "extraction show how the transport condition can be satisfied."
    ),
    prior=0.76,
)


passivation_vs_transport_is_conditional = claim(
    "The passivation-versus-transport tension is conditional: the same class of "
    "interfacial interventions can either reduce recombination or impede "
    "extraction depending on molecular geometry and contact energetics.",
    title="Passivation versus transport is conditional",
)

strat_passivation_vs_transport_is_conditional = support(
    [
        tension_passivation_transport_tradeoff_is_conditional,
        passivation_may_hurt_ff_if_it_blocks_extraction,
        effective_passivation_requires_defect_reduction_without_transport_penalty,
    ],
    passivation_vs_transport_is_conditional,
    reason=(
        "The earlier tension node is refined into an explicit condition: preserved "
        "charge extraction determines whether passivation helps the device."
    ),
    prior=0.84,
)


ion_migration_contributes_to_hysteresis = claim(
    "Ion migration contributes to hysteresis by producing delayed internal fields "
    "or polarization responses that depend on scan history and device stack.",
    title="Ion migration contributes to hysteresis",
)

strat_ion_migration_contributes_to_hysteresis = support(
    [
        pvsk2014_hysteresis_origin,
        pvsk2017_hysteresis,
        pvsk_all_inorganic_ion_migration,
    ],
    ion_migration_contributes_to_hysteresis,
    reason=(
        "Hysteresis observations and later ion-migration suppression claims align "
        "on mobile ionic defects as one contributor, not the sole mechanism."
    ),
    prior=0.75,
)


interface_recombination_amplifies_hysteresis = claim(
    "Interface recombination can amplify hysteresis because scan-dependent charge "
    "accumulation and defective contacts change recombination losses during the "
    "measurement.",
    title="Interface recombination amplifies hysteresis",
)

strat_interface_recombination_amplifies_hysteresis = support(
    [
        pvsk2014_hysteresis_origin,
        pvsk_formate_recombination_reduction,
        pvsk_dipolar_buried_recombination,
    ],
    interface_recombination_amplifies_hysteresis,
    reason=(
        "The hysteresis-origin claim is connected to later packages where reducing "
        "buried-interface or grain-boundary recombination improves device behavior."
    ),
    prior=0.72,
)


dimensional_interface_engineering_suppresses_hysteresis_in_practice = claim(
    "Dimensional interface engineering suppresses hysteresis in practice by "
    "combining better coverage, barrier protection, and interfacial recombination "
    "control.",
    title="Dimensional interfaces suppress hysteresis in practice",
)

strat_dimensional_interface_engineering_suppresses_hysteresis_in_practice = support(
    [
        pvsk2014_negligible_hysteresis,
        pvsk2015_hysteresis_benefit,
        pvsk2017_2d3d_composite,
        pvsk_dipolar_strategy,
    ],
    dimensional_interface_engineering_suppresses_hysteresis_in_practice,
    reason=(
        "Bilayer, mixed-composition, 2D/3D, and buried-interface strategies "
        "converge on practical hysteresis suppression even when microscopic causes "
        "remain plural."
    ),
    prior=0.80,
)


hysteresis_suppression_does_not_identify_single_microscopic_cause = claim(
    "Practical hysteresis suppression does not identify one microscopic cause; it "
    "only shows that the combined ion-migration, recombination, and polarization "
    "effects can be controlled under specific architectures.",
    title="Hysteresis suppression does not identify a single cause",
)

strat_hysteresis_suppression_does_not_identify_single_microscopic_cause = support(
    [
        tension_hysteresis_has_multiple_sources,
        ion_migration_contributes_to_hysteresis,
        interface_recombination_amplifies_hysteresis,
        dimensional_interface_engineering_suppresses_hysteresis_in_practice,
    ],
    hysteresis_suppression_does_not_identify_single_microscopic_cause,
    reason=(
        "The evidence supports practical suppression while preserving uncertainty "
        "about which microscopic channel dominates in each stack."
    ),
    prior=0.78,
)


record_efficiency_vs_module_scaling_is_not_automatic = claim(
    "Record efficiency does not automatically scale to modules because champion "
    "cells, large-area tandems, roll-to-roll modules, and homogeneous 2D modules "
    "stress different uniformity and interconnection constraints.",
    title="Record efficiency versus module scaling is not automatic",
)

strat_record_efficiency_vs_module_scaling_is_not_automatic = support(
    [
        pvsk_htl201_certified,
        pvsk_persik_2024_nrel_certified,
        pvsk_all_tandem_large_area,
        pvsk_r2r_modules,
        pvsk_homogeneous_2d_large_module,
    ],
    record_efficiency_vs_module_scaling_is_not_automatic,
    reason=(
        "The highest certified cell/tandem records and the module-scale claims are "
        "both credible, but they do not measure the same manufacturing bottleneck."
    ),
    prior=0.70,
)


stability_under_single_stressor_does_not_guarantee_field_stability = claim(
    "Stability under one stressor does not guarantee field stability because damp "
    "heat, thermal ion migration, long illumination, and tandem operation impose "
    "different coupled degradation paths.",
    title="Single-stressor stability does not guarantee field stability",
)

strat_stability_under_single_stressor_does_not_guarantee_field_stability = support(
    [
        tension_stability_routes_are_condition_specific,
        pvsk_damp_heat_iec,
        pvsk_formate_long_term_stability,
        pvsk_htl201_operational_25c,
        pvsk_all_tandem_operational_600h,
        pvsk_all_inorganic_t80,
    ],
    stability_under_single_stressor_does_not_guarantee_field_stability,
    reason=(
        "The stress conditions are not interchangeable, so the graph keeps "
        "accelerated and operational stability evidence as conditional support."
    ),
    prior=0.76,
)


bifacial_gain_depends_on_albedo_and_installation_context = claim(
    "Bifacial power gain depends on albedo and installation context; rear-side "
    "collection improves system value only when reflected irradiance and module "
    "layout support it.",
    title="Bifacial gain depends on albedo and installation context",
)

strat_bifacial_gain_depends_on_albedo_and_installation_context = support(
    [
        pvsk_bifacial_gain,
        pvsk_bifacial_power_density,
        pvsk_bifacial_nrel_front,
        pvsk_bifacial_6000h,
    ],
    bifacial_gain_depends_on_albedo_and_installation_context,
    reason=(
        "The bifacial package reports gain under a specified albedo and combines it "
        "with certification and long operation, making context a condition rather "
        "than a refutation."
    ),
    prior=0.74,
)


cost_projection_depends_on_yield_lifetime_and_throughput = claim(
    "Cost projections depend on yield, lifetime, and throughput: printable "
    "contacts and roll-to-roll processing lower plausible cost only if module "
    "reproducibility and retained output hold at scale.",
    title="Cost projection depends on yield, lifetime, and throughput",
)

strat_cost_projection_depends_on_yield_lifetime_and_throughput = support(
    [
        pvsk_r2r_cost_prediction,
        pvsk_r2r_production_cost_power,
        pvsk_r2r_throughput,
        pvsk_r2r_modules,
        pvsk_bifacial_6000h,
    ],
    cost_projection_depends_on_yield_lifetime_and_throughput,
    reason=(
        "The cost model, throughput claim, module demonstration, and lifetime "
        "evidence are distinct conditions for a cautious low-cost conclusion."
    ),
    prior=0.70,
)
