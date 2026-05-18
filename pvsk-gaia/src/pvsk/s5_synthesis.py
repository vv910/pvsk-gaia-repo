"""
S5: Final scientific synthesis conclusions.

The warrants here avoid broad multi-premise conjunctions and also avoid many
duplicative independent supports.  Each conclusion receives a small number of
non-overlapping warrants so BP can raise belief without saturating it.
"""

from gaia.lang import claim, support

from . import s2_support as _directed_support_edges
from .s1_agreement import (
    agreement_dimensional_interfaces_improve_stability,
    agreement_hysteresis_can_be_suppressed_by_architecture,
    agreement_passivation_reduces_recombination,
    agreement_perovskite_absorber_validated,
    agreement_phase_and_composition_control_matter,
    agreement_solid_state_architectures_raise_efficiency,
    agreement_tandems_raise_efficiency_ceiling,
    encapsulated_module_stability_axis,
    humidity_thermal_stress_axis,
    interface_stability_axis,
    ion_migration_axis,
    operational_stability_axis,
    phase_stability_axis,
)
from .s3_contradictions import (
    bifacial_gain_depends_on_albedo_and_installation_context,
    effective_passivation_requires_defect_reduction_without_transport_penalty,
    hysteresis_suppression_does_not_identify_single_microscopic_cause,
    interface_recombination_amplifies_hysteresis,
    ion_migration_contributes_to_hysteresis,
    passivation_vs_transport_is_conditional,
    planar_vs_mesoporous_is_process_conditioned,
    record_efficiency_vs_module_scaling_is_not_automatic,
    solution_vs_vapor_deposition_is_scale_quality_tradeoff,
    stability_under_single_stressor_does_not_guarantee_field_stability,
    tension_conventional_vs_dipolar_buried_passivation,
    tension_hysteresis_has_multiple_sources,
    tension_liquid_vs_solid_stability,
    tension_passivation_mechanisms_are_complementary,
    tension_passivation_transport_tradeoff_is_conditional,
    tension_stability_routes_are_condition_specific,
    cost_projection_depends_on_yield_lifetime_and_throughput,
    dimensional_interface_engineering_suppresses_hysteresis_in_practice,
)
from .s4_induction import (
    bandgap_contact_coupling_controls_voc_jsc_ff_tradeoff,
    deployment_value_requires_efficiency_stability_and_area_scaling,
    dimensional_interfaces_combine_defect_passivation_and_barrier_protection,
    interface_control_improves_charge_selectivity,
    interface_control_reduces_recombination,
    ion_migration_links_hysteresis_and_stability,
    law_band_alignment_controls_charge_selectivity,
    law_interface_passivation_reduces_nonradiative_loss,
    law_perovskite_absorbers_scale_across_architectures,
    law_stability_needs_phase_and_interface_control,
    law_tandems_raise_perovskite_efficiency_ceiling,
    low_loss_recombination_or_contact_layers_are_required,
    passivation_benefit_is_conditioned_on_preserved_charge_extraction,
    passivation_improves_tandem_voltage_retention,
    passivation_reduces_nonradiative_loss,
    tandem_deployment_still_depends_on_scalable_stability,
    tandem_performance_requires_bandgap_matching_and_low_loss_contacts,
    tandem_record_efficiency_depends_on_interface_contact_engineering,
)


synthesis_perovskites_are_validated_pv_platform = claim(
    "The 22-package evidence base supports perovskite photovoltaics as a validated "
    "photovoltaic platform: the absorber works across architectures, and the later "
    "performance gains come from controlling interfaces, composition, and contacts.",
    title="Perovskites are a validated photovoltaic platform",
)

strat_synthesis_platform_from_absorber_and_law = support(
    [
        agreement_perovskite_absorber_validated,
        law_perovskite_absorbers_scale_across_architectures,
        deployment_value_requires_efficiency_stability_and_area_scaling,
    ],
    synthesis_perovskites_are_validated_pv_platform,
    reason=(
        "The platform conclusion requires both cross-paper absorber agreement and "
        "the induction law that the absorber works across architectures, with "
        "deployment value routed through efficiency, stability, and area scaling."
    ),
    prior=0.80,
)

strat_synthesis_platform_from_architecture = support(
    [
        agreement_solid_state_architectures_raise_efficiency,
        dimensional_interfaces_combine_defect_passivation_and_barrier_protection,
    ],
    synthesis_perovskites_are_validated_pv_platform,
    reason=(
        "Solid-state architecture progress and reusable dimensional-interface "
        "control independently support platform validity."
    ),
    prior=0.66,
)


synthesis_efficiency_progression_is_interface_driven = claim(
    "The long-run efficiency progression is best explained by interface, architecture, "
    "composition, and contact engineering rather than by a change in the basic "
    "absorber concept.",
    title="Efficiency progression is interface and architecture driven",
)

strat_synthesis_efficiency_from_composition_and_passivation = support(
    [
        interface_control_reduces_recombination,
        interface_control_improves_charge_selectivity,
        bandgap_contact_coupling_controls_voc_jsc_ff_tradeoff,
    ],
    synthesis_efficiency_progression_is_interface_driven,
    reason=(
        "Efficiency growth is routed through shared interface and contact "
        "mechanisms rather than through a list of champion paper claims."
    ),
    prior=0.80,
)

strat_synthesis_efficiency_from_record_contact = support(
    [tandem_record_efficiency_depends_on_interface_contact_engineering],
    synthesis_efficiency_progression_is_interface_driven,
    reason=(
        "The tandem-record mechanism supplies a later contact-engineering check on "
        "the interface-driven efficiency synthesis."
    ),
    prior=0.66,
)


synthesis_passivation_is_general_design_rule = claim(
    "Passivation is a general PVSK design rule: chemically bound passivators, "
    "field-effect molecules, dimensional barriers, and dipolar interfaces all work "
    "when they reduce recombination without blocking extraction.",
    title="Passivation is a general design rule",
)

strat_synthesis_passivation_from_agreement_and_law = support(
    [
        passivation_reduces_nonradiative_loss,
        passivation_benefit_is_conditioned_on_preserved_charge_extraction,
        effective_passivation_requires_defect_reduction_without_transport_penalty,
    ],
    synthesis_passivation_is_general_design_rule,
    reason=(
        "The design rule is supported by nonradiative-loss reduction only when "
        "charge extraction is preserved."
    ),
    prior=0.82,
)

strat_synthesis_passivation_from_tension_resolution = support(
    [
        tension_passivation_mechanisms_are_complementary,
        passivation_vs_transport_is_conditional,
    ],
    synthesis_passivation_is_general_design_rule,
    reason=(
        "Mechanistic complementarity and conditional transport penalties define "
        "the passivation rule's scope."
    ),
    prior=0.62,
)


synthesis_stability_requires_integrated_control = claim(
    "Durable PVSK devices require integrated control of phase stability, dimensional "
    "interface protection, ion migration, and device-stack chemistry; no single "
    "stability mechanism explains all successful packages.",
    title="Stability requires integrated control",
)

strat_synthesis_stability_from_law_and_agreement = support(
    [
        phase_stability_axis,
        interface_stability_axis,
        ion_migration_axis,
        humidity_thermal_stress_axis,
        operational_stability_axis,
        encapsulated_module_stability_axis,
    ],
    synthesis_stability_requires_integrated_control,
    reason=(
        "Integrated stability is decomposed into phase, interface, ion-migration, "
        "humidity/thermal, operational, and encapsulated-module evidence axes."
    ),
    prior=0.78,
)

strat_synthesis_stability_from_conditional_routes = support(
    [
        law_stability_needs_phase_and_interface_control,
        ion_migration_links_hysteresis_and_stability,
        dimensional_interfaces_combine_defect_passivation_and_barrier_protection,
        stability_under_single_stressor_does_not_guarantee_field_stability,
    ],
    synthesis_stability_requires_integrated_control,
    reason=(
        "The stability law is narrowed by ion-migration, dimensional-interface, and "
        "single-stressor limitation nodes."
    ),
    prior=0.72,
)


synthesis_hysteresis_is_practically_suppressed = claim(
    "Current-density hysteresis is not a single solved microscopic mechanism, but it "
    "has become practically suppressible through architecture, dimensional interface "
    "design, and buried-interface passivation.",
    title="Hysteresis is practically suppressible",
)

strat_synthesis_hysteresis_from_architecture = support(
    [
        ion_migration_contributes_to_hysteresis,
        interface_recombination_amplifies_hysteresis,
        dimensional_interface_engineering_suppresses_hysteresis_in_practice,
    ],
    synthesis_hysteresis_is_practically_suppressed,
    reason=(
        "Practical hysteresis suppression is now tied to ion migration, interface "
        "recombination, and dimensional-interface control."
    ),
    prior=0.78,
)

strat_synthesis_hysteresis_from_multisource_tension = support(
    [
        hysteresis_suppression_does_not_identify_single_microscopic_cause,
        agreement_hysteresis_can_be_suppressed_by_architecture,
    ],
    synthesis_hysteresis_is_practically_suppressed,
    reason=(
        "A multi-source mechanism explains why practical suppression need not "
        "solve one universal microscopic cause."
    ),
    prior=0.62,
)


synthesis_bandgap_and_contact_engineering_define_tradeoff_space = claim(
    "PVSK optimization is governed by a bandgap-contact trade-off space: iodide, "
    "bromide, mixed cations, and selective contacts tune current, voltage, and "
    "extraction rather than optimizing all metrics independently.",
    title="Bandgap and contact engineering define the trade-off space",
)

strat_synthesis_bandgap_from_material_tradeoff = support(
    [
        bandgap_contact_coupling_controls_voc_jsc_ff_tradeoff,
        passivation_benefit_is_conditioned_on_preserved_charge_extraction,
    ],
    synthesis_bandgap_and_contact_engineering_define_tradeoff_space,
    reason=(
        "The trade-off conclusion is routed through the shared bandgap-contact "
        "mechanism and the passivation/transport condition."
    ),
    prior=0.78,
)

strat_synthesis_bandgap_from_contact_law = support(
    [
        law_band_alignment_controls_charge_selectivity,
        low_loss_recombination_or_contact_layers_are_required,
    ],
    synthesis_bandgap_and_contact_engineering_define_tradeoff_space,
    reason=(
        "The band-alignment law supplies the contact-selectivity side of the "
        "trade-off space, while tandem low-loss contacts expose the same bottleneck."
    ),
    prior=0.72,
)


synthesis_tandems_are_primary_high_efficiency_path = claim(
    "Tandem architectures are the primary high-efficiency path for PVSK: their "
    "advantage depends on bandgap tunability, interfacial selectivity, and low-loss "
    "contacts rather than on tandem stacking alone.",
    title="Tandems are the primary high-efficiency path",
)

strat_synthesis_tandem_from_agreement_and_law = support(
    [
        tandem_performance_requires_bandgap_matching_and_low_loss_contacts,
        tandem_record_efficiency_depends_on_interface_contact_engineering,
        passivation_improves_tandem_voltage_retention,
    ],
    synthesis_tandems_are_primary_high_efficiency_path,
    reason=(
        "The tandem conclusion is decomposed into bandgap matching, low-loss "
        "contacts, passivation-enabled voltage retention, and record-efficiency "
        "interface/contact engineering."
    ),
    prior=0.84,
)

strat_synthesis_tandem_from_buried_interface_scope = support(
    [
        agreement_tandems_raise_efficiency_ceiling,
        law_tandems_raise_perovskite_efficiency_ceiling,
        tension_conventional_vs_dipolar_buried_passivation,
        tandem_deployment_still_depends_on_scalable_stability,
    ],
    synthesis_tandems_are_primary_high_efficiency_path,
    reason=(
        "Tandem records remain a high-efficiency path, but buried-interface and "
        "scalable-stability conditions define the path's deployment scope."
    ),
    prior=0.60,
)


synthesis_mechanistic_tensions_are_conditionally_resolved = claim(
    "The major apparent conflicts across PVSK papers are conditionally resolved: "
    "they usually reflect different architectures, stress tests, interfaces, or "
    "optimization targets rather than mutually exclusive physical laws.",
    title="Mechanistic tensions are conditionally resolved",
)

strat_synthesis_tensions_from_architecture_and_stability = support(
    [
        planar_vs_mesoporous_is_process_conditioned,
        solution_vs_vapor_deposition_is_scale_quality_tradeoff,
        record_efficiency_vs_module_scaling_is_not_automatic,
        stability_under_single_stressor_does_not_guarantee_field_stability,
        cost_projection_depends_on_yield_lifetime_and_throughput,
    ],
    synthesis_mechanistic_tensions_are_conditionally_resolved,
    reason=(
        "Process, scale, stability, and cost tensions are resolved by explicit "
        "scope conditions rather than by treating one paper as refuting another."
    ),
    prior=0.72,
)

strat_synthesis_tensions_from_interface_mechanisms = support(
    [
        tension_liquid_vs_solid_stability,
        tension_hysteresis_has_multiple_sources,
        tension_passivation_mechanisms_are_complementary,
        passivation_vs_transport_is_conditional,
        bifacial_gain_depends_on_albedo_and_installation_context,
    ],
    synthesis_mechanistic_tensions_are_conditionally_resolved,
    reason=(
        "Interface-related and deployment-context tensions are conditionally "
        "resolved by architecture, passivation, stress, and installation context."
    ),
    prior=0.66,
)
