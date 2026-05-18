"""
S1: Cross-paper agreement claims.

These local claims represent convergent conclusions across paper packages.  The
paper-level claims are not restated as observations; they are imported from each
package's public API and used directly as evidence.
"""

from gaia.lang import claim, support

from ._imports import (
    pvsk2013_reproducibility,
    pvsk2009_sensitization,
    pvsk2012_1_panchromatic,
    pvsk2012_1_solid_stability,
    pvsk2012_2_al2o3_best,
    pvsk2012_2_semiconductor,
    pvsk2013_certified,
    pvsk2014_full_coverage,
    pvsk2014_certified_efficiency,
    pvsk2014_negligible_hysteresis,
    pvsk2015_phase_stabilization,
    pvsk_triple_cation_best_pce,
    pvsk_triple_cation_tunable_bandgap,
    pvsk_triple_cation_strategy,
    pvsk2017_one_year_stability,
    pvsk2017_2d3d_composite,
    pvsk_mda_alpha_stabilization,
    pvsk_damp_heat_iec,
    pvsk_damp_heat_barrier,
    pvsk_damp_heat_dual_passivation,
    pvsk_damp_heat_t95,
    pvsk_bifacial_damp_heat,
    pvsk_all_inorganic_activation_energy,
    pvsk_all_inorganic_ion_migration,
    pvsk_all_inorganic_t80,
    pvsk_all_inorganic_capped_improvement,
    pvsk_formate_recombination_reduction,
    pvsk_formate_ideality,
    pvsk_formate_long_term_stability,
    pvsk_all_tandem_deep_states,
    pvsk_all_tandem_large_area,
    pvsk_all_tandem_operational_600h,
    pvsk_all_tandem_certified,
    pvsk_3d3d_type2_alignment,
    pvsk_3d3d_certified,
    pvsk_persik_2024_nrel_certified,
    pvsk_htl201_certified,
    pvsk_htl201_operational_25c,
    pvsk_htl201_voc_ff,
    pvsk_dipolar_strategy,
    pvsk_dipolar_tandem_stability,
    pvsk_dipolar_jet_certified,
    pvsk_dmdp_qss_certification,
    pvsk_r2r_cells,
    pvsk_r2r_modules,
    pvsk_r2r_module_record,
    pvsk_r2r_pfsd,
    pvsk_r2r_carbon_electrode,
    pvsk_r2r_cost_prediction,
    pvsk_r2r_production_cost_power,
    pvsk_r2r_throughput,
    pvsk_bifacial_nrel_front,
    pvsk_bifacial_6000h,
    pvsk_bifacial_module_record,
    pvsk_homogeneous_2d_large_module,
    pvsk_homogeneous_2d_large_device,
    pvsk_homogeneous_2d_stability,
    pvsk_homogeneous_2d_triple_halide,
)


agreement_perovskite_absorber_validated = claim(
    "Independent packages agree that organometal halide perovskites are effective "
    "photovoltaic absorbers rather than merely experimental dye replacements.",
    title="Perovskite absorbers are validated across early architectures",
)

strat_agreement_perovskite_absorber_validated = support(
    [
        pvsk2009_sensitization,
        pvsk2012_1_panchromatic,
        pvsk2012_2_semiconductor,
        pvsk2014_certified_efficiency,
    ],
    agreement_perovskite_absorber_validated,
    reason=(
        "The 2009 sensitizer result, 2012 solid-state panchromatic response, "
        "2012 meso-superstructured semiconductor behavior, and 2014 certified "
        "bilayer efficiency all point to the same absorber-level conclusion."
    ),
    prior=0.94,
)


agreement_solid_state_architectures_raise_efficiency = claim(
    "The early efficiency jump is consistently associated with solid-state and "
    "architecturally controlled devices, not with liquid-electrolyte sensitization.",
    title="Solid-state architectures raise efficiency",
)

strat_agreement_solid_state_architectures_raise_efficiency = support(
    [
        pvsk2012_1_solid_stability,
        pvsk2012_2_al2o3_best,
        pvsk2013_certified,
        pvsk2014_certified_efficiency,
    ],
    agreement_solid_state_architectures_raise_efficiency,
    reason=(
        "Kim 2012, Lee 2012, Burschka 2013, and Jeon 2014 all connect solid-state "
        "device design or controlled architecture with much higher performance."
    ),
    prior=0.91,
)


agreement_phase_and_composition_control_matter = claim(
    "Composition and phase control are repeated enabling themes for high-efficiency "
    "and stable perovskite devices.",
    title="Composition and phase control are repeated enablers",
)

strat_agreement_phase_and_composition_control_matter = support(
    [
        pvsk2015_phase_stabilization,
        pvsk_triple_cation_strategy,
        pvsk_triple_cation_best_pce,
        pvsk_mda_alpha_stabilization,
    ],
    agreement_phase_and_composition_control_matter,
    reason=(
        "Mixed-cation stabilization, triple-cation stabilization, and MDA-based "
        "alpha-FAPbI3 stabilization independently support a composition-control "
        "design principle."
    ),
    prior=0.89,
)


agreement_passivation_reduces_recombination = claim(
    "Surface, grain-boundary, and buried-interface passivation repeatedly reduce "
    "non-radiative recombination or its device-level signatures.",
    title="Passivation reduces recombination across interfaces",
)

strat_agreement_passivation_reduces_recombination = support(
    [
        pvsk_formate_recombination_reduction,
        pvsk_all_tandem_deep_states,
        pvsk_damp_heat_dual_passivation,
        pvsk_dipolar_strategy,
    ],
    agreement_passivation_reduces_recombination,
    reason=(
        "Formate, CF3-PA, tailored-dimensionality 2D/3D, and dipolar strategies "
        "all target recombination-active defects at interfaces or grain surfaces."
    ),
    prior=0.90,
)


agreement_dimensional_interfaces_improve_stability = claim(
    "Dimensional interface engineering, including 2D/3D interfaces and capping "
    "layers, repeatedly improves moisture, thermal, or operational stability.",
    title="Dimensional interfaces improve stability",
)

strat_agreement_dimensional_interfaces_improve_stability = support(
    [
        pvsk2017_one_year_stability,
        pvsk2017_2d3d_composite,
        pvsk_damp_heat_t95,
        pvsk_all_inorganic_ion_migration,
    ],
    agreement_dimensional_interfaces_improve_stability,
    reason=(
        "The 2017 2D/3D result, 2022 damp-heat-stable 2D/3D devices, and "
        "all-inorganic 2D capping all connect dimensional interface control with "
        "stability gains."
    ),
    prior=0.88,
)


agreement_hysteresis_can_be_suppressed_by_architecture = claim(
    "Device architecture and interface design can suppress current-density "
    "hysteresis to a practical level.",
    title="Architecture can suppress hysteresis",
)

strat_agreement_hysteresis_can_be_suppressed_by_architecture = support(
    [
        pvsk2014_negligible_hysteresis,
        pvsk2017_2d3d_composite,
        pvsk_dipolar_strategy,
    ],
    agreement_hysteresis_can_be_suppressed_by_architecture,
    reason=(
        "Bilayer engineering, 2D/3D interface engineering, and buried-interface "
        "dipolar passivation all address interface-controlled loss pathways linked "
        "to hysteresis."
    ),
    prior=0.84,
)


agreement_tandems_raise_efficiency_ceiling = claim(
    "Perovskite-based tandem architectures repeatedly raise the efficiency ceiling "
    "beyond single-junction perovskite cells.",
    title="Tandems raise the efficiency ceiling",
)

strat_agreement_tandems_raise_efficiency_ceiling = support(
    [
        pvsk_all_tandem_certified,
        pvsk_3d3d_type2_alignment,
        pvsk_persik_2024_nrel_certified,
        pvsk_htl201_certified,
        pvsk_dipolar_jet_certified,
    ],
    agreement_tandems_raise_efficiency_ceiling,
    reason=(
        "All-perovskite tandem, 3D/3D bilayer, perovskite/silicon, HTL201, and "
        "dipolar passivation packages independently support tandem-level efficiency "
        "growth."
    ),
    prior=0.95,
)


agreement_scalability_has_multiple_routes = claim(
    "Scalable perovskite manufacturing is supported by multiple routes rather than "
    "a single deposition platform.",
    title="Scalability has multiple manufacturing routes",
)

strat_agreement_scalability_has_multiple_routes = support(
    [
        pvsk_r2r_cells,
        pvsk_r2r_modules,
        pvsk_bifacial_nrel_front,
        pvsk_homogeneous_2d_large_module,
    ],
    agreement_scalability_has_multiple_routes,
    reason=(
        "Roll-to-roll cells and modules, bifacial minimodules, and homogeneous 2D "
        "large modules show that scale-up can be pursued through distinct process "
        "families."
    ),
    prior=0.86,
)


phase_stability_axis = claim(
    "Phase-stability evidence forms a distinct synthesis axis: mixed-cation, "
    "triple-cation, MDA, and triple-halide controls all suppress phase instability "
    "without being interchangeable with interface protection.",
    title="Phase-stability evidence axis",
)

strat_phase_stability_axis = support(
    [
        pvsk2015_phase_stabilization,
        pvsk_triple_cation_strategy,
        pvsk_mda_alpha_stabilization,
        pvsk_homogeneous_2d_triple_halide,
    ],
    phase_stability_axis,
    reason=(
        "Composition-level phase control recurs in 2015 mixed-cation, later "
        "triple-cation, MDA-stabilized FAPbI3, and triple-halide module work."
    ),
    prior=0.86,
)


interface_stability_axis = claim(
    "Interface-stability evidence is a separate axis because 2D/3D interfaces, "
    "formate treatment, tailored-dimensionality passivation, and dipolar buried "
    "interfaces protect device stacks through local interfacial chemistry.",
    title="Interface-stability evidence axis",
)

strat_interface_stability_axis = support(
    [
        pvsk2017_2d3d_composite,
        pvsk_damp_heat_dual_passivation,
        pvsk_formate_long_term_stability,
        pvsk_dipolar_tandem_stability,
    ],
    interface_stability_axis,
    reason=(
        "The stability gains are reported at interfaces or heterointerfaces rather "
        "than only through bulk absorber composition."
    ),
    prior=0.82,
)


ion_migration_axis = claim(
    "Ion migration is a shared stability axis: vacancy passivation, higher "
    "activation energy, capped-device retention, and hysteresis-linked transport "
    "all indicate that mobile ions couple device operation to degradation.",
    title="Ion-migration evidence axis",
)

strat_ion_migration_axis = support(
    [
        pvsk_all_inorganic_ion_migration,
        pvsk_all_inorganic_activation_energy,
        pvsk_all_inorganic_t80,
        pvsk2014_negligible_hysteresis,
    ],
    ion_migration_axis,
    reason=(
        "All-inorganic capping directly targets ion migration, while hysteresis "
        "suppression supplies a device-level symptom of the same transport issue."
    ),
    prior=0.78,
)


humidity_thermal_stress_axis = claim(
    "Humidity and thermal stress form a separate evidence axis because damp heat, "
    "thermal-photostability, and bifacial-module stress tests probe environmental "
    "drivers beyond room-temperature efficiency.",
    title="Humidity-thermal stress evidence axis",
)

strat_humidity_thermal_stress_axis = support(
    [
        pvsk_damp_heat_t95,
        pvsk_damp_heat_iec,
        pvsk_bifacial_damp_heat,
        pvsk_all_inorganic_t80,
    ],
    humidity_thermal_stress_axis,
    reason=(
        "The damp-heat, IEC, bifacial, and thermal extrapolation claims normalize "
        "stability evidence by stress mode rather than treating all retention tests "
        "as equivalent."
    ),
    prior=0.80,
)


operational_stability_axis = claim(
    "Operational stability is an evidence axis separate from accelerated stress: "
    "long operation, operational PCE retention, and tandem stability establish "
    "whether design rules survive realistic device bias and illumination.",
    title="Operational-stability evidence axis",
)

strat_operational_stability_axis = support(
    [
        pvsk2017_one_year_stability,
        pvsk_formate_long_term_stability,
        pvsk_htl201_operational_25c,
        pvsk_all_tandem_operational_600h,
        pvsk_bifacial_6000h,
    ],
    operational_stability_axis,
    reason=(
        "These claims report operational or long-duration retention, which is not "
        "identical to a single accelerated stress result."
    ),
    prior=0.78,
)


encapsulated_module_stability_axis = claim(
    "Encapsulated module stability is a scale-relevant evidence axis because it "
    "combines packaging, area, interconnection, and environmental retention rather "
    "than only small-cell material stability.",
    title="Encapsulated-module stability evidence axis",
)

strat_encapsulated_module_stability_axis = support(
    [
        pvsk_damp_heat_iec,
        pvsk_bifacial_6000h,
        pvsk_homogeneous_2d_stability,
        pvsk_dipolar_tandem_stability,
    ],
    encapsulated_module_stability_axis,
    reason=(
        "IEC damp-heat, 6000 h bifacial operation, homogeneous 2D module stability, "
        "and tandem operational stability expose package-level reliability demands."
    ),
    prior=0.76,
)


passivation_reduces_recombination_and_improves_voltage = claim(
    "Passivation often improves voltage by reducing recombination, as shown by "
    "formate, all-inorganic capping, and HTL/contact passivation; this positive "
    "effect is distinct from the transport penalty modeled in the tension layer.",
    title="Passivation reduces recombination and improves voltage",
)

strat_passivation_reduces_recombination_and_improves_voltage = support(
    [
        agreement_passivation_reduces_recombination,
        pvsk_formate_ideality,
        pvsk_all_inorganic_capped_improvement,
        pvsk_htl201_voc_ff,
    ],
    passivation_reduces_recombination_and_improves_voltage,
    reason=(
        "Recombination signatures, ideality-factor improvement, capped-device "
        "Voc/FF improvement, and HTL201 voltage/fill-factor gains all point to the "
        "same beneficial side of passivation."
    ),
    prior=0.84,
)


area_normalized_performance = claim(
    "Area-normalized performance evidence distinguishes small record cells from "
    "large-area tandems, minimodules, roll-to-roll modules, and homogeneous 2D "
    "large devices.",
    title="Area-normalized performance evidence",
)

strat_area_normalized_performance = support(
    [
        pvsk_all_tandem_large_area,
        pvsk_r2r_module_record,
        pvsk_bifacial_module_record,
        pvsk_homogeneous_2d_large_device,
    ],
    area_normalized_performance,
    reason=(
        "These package claims report area- or module-relevant performance rather "
        "than relying on single small-area champion cells."
    ),
    prior=0.72,
)


certification_status_normalized = claim(
    "Certification-normalized evidence separates independently certified or "
    "externally verified efficiencies from internal champion scans.",
    title="Certification-normalized performance evidence",
)

strat_certification_status_normalized = support(
    [
        pvsk2013_certified,
        pvsk2014_certified_efficiency,
        pvsk_all_tandem_certified,
        pvsk_persik_2024_nrel_certified,
        pvsk_htl201_certified,
        pvsk_bifacial_nrel_front,
    ],
    certification_status_normalized,
    reason=(
        "The synthesis treats third-party certification as a normalizing layer "
        "across early cells, tandem records, and bifacial minimodules."
    ),
    prior=0.82,
)


stabilized_output_vs_scan_pce = claim(
    "Stabilized output and quasi-steady-state certification are normalized apart "
    "from scan-only PCE so that hysteresis-prone or transient records are not "
    "treated as identical evidence.",
    title="Stabilized-output versus scan-PCE evidence",
)

strat_stabilized_output_vs_scan_pce = support(
    [
        pvsk_triple_cation_best_pce,
        pvsk_dmdp_qss_certification,
        pvsk_persik_2024_nrel_certified,
        pvsk_htl201_certified,
        pvsk_bifacial_nrel_front,
    ],
    stabilized_output_vs_scan_pce,
    reason=(
        "Stabilized PCE, quasi-steady-state certification, and NREL/ESTI-style "
        "records reduce the risk of treating scan artifacts as deployment evidence."
    ),
    prior=0.78,
)


module_yield_and_reproducibility = claim(
    "Module yield and reproducibility are normalized manufacturing evidence: "
    "sequential-film reproducibility, full coverage, roll-to-roll modules, and "
    "large homogeneous modules address repeatability rather than isolated peaks.",
    title="Module yield and reproducibility evidence",
)

strat_module_yield_and_reproducibility = support(
    [
        pvsk2013_reproducibility,
        pvsk2014_full_coverage,
        pvsk_r2r_modules,
        pvsk_homogeneous_2d_large_module,
    ],
    module_yield_and_reproducibility,
    reason=(
        "The evidence layer groups claims about reproducible formation, film "
        "coverage, and module-scale output before they support manufacturing "
        "conclusions."
    ),
    prior=0.70,
)


encapsulation_and_lifetime_requirements = claim(
    "Encapsulation and lifetime requirements remain explicit manufacturing "
    "constraints because module-scale value depends on retained output under "
    "packaging, damp heat, and long-operation tests.",
    title="Encapsulation and lifetime requirements",
)

strat_encapsulation_and_lifetime_requirements = support(
    [
        encapsulated_module_stability_axis,
        pvsk_damp_heat_barrier,
        pvsk_bifacial_6000h,
        pvsk_all_tandem_operational_600h,
    ],
    encapsulation_and_lifetime_requirements,
    reason=(
        "Packaging barriers, module retention, and tandem operational tests make "
        "lifetime a separate bottleneck from whether coating can make a cell."
    ),
    prior=0.74,
)


throughput_and_material_utilization = claim(
    "Throughput and material utilization are normalized cost evidence because "
    "roll-to-roll coating, printable carbon contacts, and cost-per-watt models "
    "speak to capital intensity and material waste, not directly to lifetime.",
    title="Throughput and material-utilization evidence",
)

strat_throughput_and_material_utilization = support(
    [
        pvsk_r2r_pfsd,
        pvsk_r2r_carbon_electrode,
        pvsk_r2r_production_cost_power,
        pvsk_r2r_throughput,
    ],
    throughput_and_material_utilization,
    reason=(
        "PFSD, printable carbon, production-cost estimates, and high-throughput "
        "testing are grouped as process-economics evidence before cost conclusions."
    ),
    prior=0.68,
)


printable_contacts_reduce_capex_but_require_lifetime_validation = claim(
    "Printable carbon contacts plausibly reduce capital and material cost, but the "
    "low-cost inference remains conditional until lifetime and yield are validated "
    "at module scale.",
    title="Printable contacts reduce capex but require lifetime validation",
)

strat_printable_contacts_reduce_capex_but_require_lifetime_validation = support(
    [
        pvsk_r2r_carbon_electrode,
        pvsk_r2r_cost_prediction,
        throughput_and_material_utilization,
        encapsulation_and_lifetime_requirements,
    ],
    printable_contacts_reduce_capex_but_require_lifetime_validation,
    reason=(
        "The carbon-contact route lowers process burden, but the normalized "
        "lifetime layer keeps the cost claim from becoming deployment-ready proof."
    ),
    prior=0.66,
)
