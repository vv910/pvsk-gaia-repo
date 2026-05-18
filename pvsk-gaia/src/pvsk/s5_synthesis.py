"""
S5: Final scientific synthesis conclusions.

The warrants here avoid broad multi-premise conjunctions and also avoid many
duplicative independent supports.  Each conclusion receives a small number of
non-overlapping warrants so BP can raise belief without saturating it.
"""

from gaia.lang import claim, support

from . import s2_support as _directed_support_edges
from ._imports import (
    pvsk2009_bromide_voc,
    pvsk2009_iodide_ipce,
    pvsk2015_bandgap_tradeoff,
    pvsk_htl201_certified,
)
from .s1_agreement import (
    agreement_dimensional_interfaces_improve_stability,
    agreement_hysteresis_can_be_suppressed_by_architecture,
    agreement_passivation_reduces_recombination,
    agreement_perovskite_absorber_validated,
    agreement_phase_and_composition_control_matter,
    agreement_solid_state_architectures_raise_efficiency,
    agreement_tandems_raise_efficiency_ceiling,
)
from .s3_contradictions import (
    tension_conventional_vs_dipolar_buried_passivation,
    tension_hysteresis_has_multiple_sources,
    tension_liquid_vs_solid_stability,
    tension_passivation_mechanisms_are_complementary,
    tension_passivation_transport_tradeoff_is_conditional,
    tension_stability_routes_are_condition_specific,
)
from .s4_induction import (
    law_band_alignment_controls_charge_selectivity,
    law_interface_passivation_reduces_nonradiative_loss,
    law_perovskite_absorbers_scale_across_architectures,
    law_stability_needs_phase_and_interface_control,
    law_tandems_raise_perovskite_efficiency_ceiling,
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
    ],
    synthesis_perovskites_are_validated_pv_platform,
    reason=(
        "The platform conclusion requires both cross-paper absorber agreement and "
        "the induction law that the absorber works across architectures."
    ),
    prior=0.82,
)

strat_synthesis_platform_from_architecture = support(
    [agreement_solid_state_architectures_raise_efficiency],
    synthesis_perovskites_are_validated_pv_platform,
    reason="Solid-state architecture progress independently supports platform validity.",
    prior=0.68,
)


synthesis_efficiency_progression_is_interface_driven = claim(
    "The long-run efficiency progression is best explained by interface, architecture, "
    "composition, and contact engineering rather than by a change in the basic "
    "absorber concept.",
    title="Efficiency progression is interface and architecture driven",
)

strat_synthesis_efficiency_from_composition_and_passivation = support(
    [
        agreement_phase_and_composition_control_matter,
        agreement_passivation_reduces_recombination,
    ],
    synthesis_efficiency_progression_is_interface_driven,
    reason="Composition control and passivation convergence jointly support the efficiency-growth mechanism.",
    prior=0.78,
)

strat_synthesis_efficiency_from_record_contact = support(
    [pvsk_htl201_certified],
    synthesis_efficiency_progression_is_interface_driven,
    reason="The HTL201 record supplies a later contact-engineering check on the synthesis.",
    prior=0.68,
)


synthesis_passivation_is_general_design_rule = claim(
    "Passivation is a general PVSK design rule: chemically bound passivators, "
    "field-effect molecules, dimensional barriers, and dipolar interfaces all work "
    "when they reduce recombination without blocking extraction.",
    title="Passivation is a general design rule",
)

strat_synthesis_passivation_from_agreement_and_law = support(
    [
        agreement_passivation_reduces_recombination,
        law_interface_passivation_reduces_nonradiative_loss,
    ],
    synthesis_passivation_is_general_design_rule,
    reason="Agreement and induction jointly support passivation as a general design rule.",
    prior=0.82,
)

strat_synthesis_passivation_from_tension_resolution = support(
    [
        tension_passivation_mechanisms_are_complementary,
        tension_passivation_transport_tradeoff_is_conditional,
    ],
    synthesis_passivation_is_general_design_rule,
    reason="Mechanistic complementarity and conditional transport penalties define the rule's scope.",
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
        law_stability_needs_phase_and_interface_control,
        agreement_dimensional_interfaces_improve_stability,
    ],
    synthesis_stability_requires_integrated_control,
    reason="The stability law and dimensional-interface agreement jointly support integrated control.",
    prior=0.84,
)

strat_synthesis_stability_from_conditional_routes = support(
    [tension_stability_routes_are_condition_specific],
    synthesis_stability_requires_integrated_control,
    reason="Condition-specific stability routes show why no single mechanism is sufficient.",
    prior=0.72,
)


synthesis_hysteresis_is_practically_suppressed = claim(
    "Current-density hysteresis is not a single solved microscopic mechanism, but it "
    "has become practically suppressible through architecture, dimensional interface "
    "design, and buried-interface passivation.",
    title="Hysteresis is practically suppressible",
)

strat_synthesis_hysteresis_from_architecture = support(
    [agreement_hysteresis_can_be_suppressed_by_architecture],
    synthesis_hysteresis_is_practically_suppressed,
    reason="Architecture-level agreement supports practical suppression.",
    prior=0.76,
)

strat_synthesis_hysteresis_from_multisource_tension = support(
    [tension_hysteresis_has_multiple_sources],
    synthesis_hysteresis_is_practically_suppressed,
    reason="A multi-source mechanism explains why practical suppression need not solve one universal microscopic cause.",
    prior=0.62,
)


synthesis_bandgap_and_contact_engineering_define_tradeoff_space = claim(
    "PVSK optimization is governed by a bandgap-contact trade-off space: iodide, "
    "bromide, mixed cations, and selective contacts tune current, voltage, and "
    "extraction rather than optimizing all metrics independently.",
    title="Bandgap and contact engineering define the trade-off space",
)

strat_synthesis_bandgap_from_material_tradeoff = support(
    [pvsk2009_bromide_voc, pvsk2009_iodide_ipce, pvsk2015_bandgap_tradeoff],
    synthesis_bandgap_and_contact_engineering_define_tradeoff_space,
    reason="Early halide contrast and later composition tuning define the material side of the trade-off space.",
    prior=0.72,
)

strat_synthesis_bandgap_from_contact_law = support(
    [law_band_alignment_controls_charge_selectivity],
    synthesis_bandgap_and_contact_engineering_define_tradeoff_space,
    reason="The band-alignment law supplies the contact-selectivity side of the trade-off space.",
    prior=0.74,
)


synthesis_tandems_are_primary_high_efficiency_path = claim(
    "Tandem architectures are the primary high-efficiency path for PVSK: their "
    "advantage depends on bandgap tunability, interfacial selectivity, and low-loss "
    "contacts rather than on tandem stacking alone.",
    title="Tandems are the primary high-efficiency path",
)

strat_synthesis_tandem_from_agreement_and_law = support(
    [
        agreement_tandems_raise_efficiency_ceiling,
        law_tandems_raise_perovskite_efficiency_ceiling,
    ],
    synthesis_tandems_are_primary_high_efficiency_path,
    reason="Tandem agreement and tandem induction jointly support the high-efficiency path.",
    prior=0.84,
)

strat_synthesis_tandem_from_buried_interface_scope = support(
    [tension_conventional_vs_dipolar_buried_passivation],
    synthesis_tandems_are_primary_high_efficiency_path,
    reason="Buried-interface passivation tension explains why tandem records depend on contact design.",
    prior=0.58,
)


synthesis_mechanistic_tensions_are_conditionally_resolved = claim(
    "The major apparent conflicts across PVSK papers are conditionally resolved: "
    "they usually reflect different architectures, stress tests, interfaces, or "
    "optimization targets rather than mutually exclusive physical laws.",
    title="Mechanistic tensions are conditionally resolved",
)

strat_synthesis_tensions_from_architecture_and_stability = support(
    [
        tension_liquid_vs_solid_stability,
        tension_stability_routes_are_condition_specific,
    ],
    synthesis_mechanistic_tensions_are_conditionally_resolved,
    reason="Architecture-dependent stability and condition-specific stability routes support conditional resolution.",
    prior=0.76,
)

strat_synthesis_tensions_from_interface_mechanisms = support(
    [
        tension_hysteresis_has_multiple_sources,
        tension_passivation_mechanisms_are_complementary,
        tension_passivation_transport_tradeoff_is_conditional,
    ],
    synthesis_mechanistic_tensions_are_conditionally_resolved,
    reason="Interface-related mechanism tensions are resolved by scope conditions rather than exclusive mechanisms.",
    prior=0.68,
)
