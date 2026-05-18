"""
S1: Cross-paper agreement claims.

These local claims represent convergent conclusions across paper packages.  The
paper-level claims are not restated as observations; they are imported from each
package's public API and used directly as evidence.
"""

from gaia.lang import claim, support

from ._imports import (
    pvsk2009_sensitization,
    pvsk2012_1_panchromatic,
    pvsk2012_1_solid_stability,
    pvsk2012_2_al2o3_best,
    pvsk2012_2_semiconductor,
    pvsk2013_certified,
    pvsk2014_certified_efficiency,
    pvsk2014_negligible_hysteresis,
    pvsk2015_phase_stabilization,
    pvsk_triple_cation_best_pce,
    pvsk_triple_cation_strategy,
    pvsk2017_one_year_stability,
    pvsk2017_2d3d_composite,
    pvsk_mda_alpha_stabilization,
    pvsk_damp_heat_dual_passivation,
    pvsk_damp_heat_t95,
    pvsk_all_inorganic_ion_migration,
    pvsk_formate_recombination_reduction,
    pvsk_all_tandem_deep_states,
    pvsk_all_tandem_certified,
    pvsk_3d3d_type2_alignment,
    pvsk_persik_2024_nrel_certified,
    pvsk_htl201_certified,
    pvsk_dipolar_strategy,
    pvsk_dipolar_jet_certified,
    pvsk_r2r_cells,
    pvsk_r2r_modules,
    pvsk_bifacial_nrel_front,
    pvsk_homogeneous_2d_large_module,
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
