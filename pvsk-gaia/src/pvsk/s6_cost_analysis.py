"""
S6: Manufacturing, cost, and deployment synthesis.

Manufacturing conclusions use a small number of scoped warrants to avoid
overcounting closely related roll-to-roll evidence.
"""

from gaia.lang import claim, support

from ._imports import (
    pvsk_bifacial_6000h,
    pvsk_bifacial_nrel_front,
)
from .s1_agreement import (
    agreement_scalability_has_multiple_routes,
    area_normalized_performance,
    certification_status_normalized,
    encapsulated_module_stability_axis,
    encapsulation_and_lifetime_requirements,
    module_yield_and_reproducibility,
    printable_contacts_reduce_capex_but_require_lifetime_validation,
    stabilized_output_vs_scan_pce,
    throughput_and_material_utilization,
)
from .s3_contradictions import (
    bifacial_gain_depends_on_albedo_and_installation_context,
    cost_projection_depends_on_yield_lifetime_and_throughput,
    record_efficiency_vs_module_scaling_is_not_automatic,
    stability_under_single_stressor_does_not_guarantee_field_stability,
)
from .s4_induction import (
    deployment_value_requires_efficiency_stability_and_area_scaling,
    law_scalable_deposition_can_preserve_device_quality,
    scalable_manufacturing_requires_uniformity_yield_and_encapsulation,
    sustained_improvement_comes_from_reusable_design_axes,
    tandem_deployment_still_depends_on_scalable_stability,
)
from .s5_synthesis import (
    synthesis_bandgap_and_contact_engineering_define_tradeoff_space,
    synthesis_efficiency_progression_is_interface_driven,
    synthesis_hysteresis_is_practically_suppressed,
    synthesis_passivation_is_general_design_rule,
    synthesis_stability_requires_integrated_control,
    synthesis_tandems_are_primary_high_efficiency_path,
)


synthesis_scalable_manufacturing_is_demonstrated = claim(
    "PVSK scale-up is demonstrated at the synthesis level: roll-to-roll cells and "
    "modules, bifacial minimodules, and homogeneous 2D large modules show that "
    "device quality can survive multiple manufacturing routes.",
    title="Scalable manufacturing is demonstrated across routes",
)

strat_synthesis_scale_from_law_and_agreement = support(
    [
        scalable_manufacturing_requires_uniformity_yield_and_encapsulation,
        agreement_scalability_has_multiple_routes,
        area_normalized_performance,
        certification_status_normalized,
    ],
    synthesis_scalable_manufacturing_is_demonstrated,
    reason=(
        "Manufacturing scale-up is routed through uniformity, yield, "
        "encapsulation, area-normalized performance, and certification evidence."
    ),
    prior=0.76,
)

strat_synthesis_scale_from_module_examples = support(
    [
        law_scalable_deposition_can_preserve_device_quality,
        module_yield_and_reproducibility,
        stabilized_output_vs_scan_pce,
        encapsulation_and_lifetime_requirements,
        record_efficiency_vs_module_scaling_is_not_automatic,
    ],
    synthesis_scalable_manufacturing_is_demonstrated,
    reason=(
        "Concrete scale examples support manufacturability only after normalized "
        "yield, stabilized-output, lifetime, and record-to-module limitations are "
        "kept explicit."
    ),
    prior=0.64,
)


synthesis_low_cost_path_depends_on_printable_contacts = claim(
    "The low-cost PVSK path depends on printable high-throughput processing and "
    "low-cost contacts, especially carbon-based electrodes that reduce dependence "
    "on noble-metal evaporation.",
    title="Low-cost path depends on printable contacts",
)

strat_synthesis_low_cost_from_printable_contact = support(
    [
        printable_contacts_reduce_capex_but_require_lifetime_validation,
        throughput_and_material_utilization,
    ],
    synthesis_low_cost_path_depends_on_printable_contacts,
    reason=(
        "Printable contacts support a low-cost path as a capex and material-use "
        "mechanism, while lifetime validation remains part of the premise."
    ),
    prior=0.64,
)

strat_synthesis_low_cost_from_cost_and_throughput = support(
    [
        cost_projection_depends_on_yield_lifetime_and_throughput,
        module_yield_and_reproducibility,
        encapsulation_and_lifetime_requirements,
    ],
    synthesis_low_cost_path_depends_on_printable_contacts,
    reason=(
        "Cost modeling remains a cautious inference because yield, lifetime, and "
        "throughput are explicit conditions rather than established deployment facts."
    ),
    prior=0.54,
)


synthesis_bifacial_modules_add_system_value = claim(
    "Bifacial perovskite modules add system-level value because rear-side collection "
    "and reflected-light power density can improve deployment economics beyond "
    "front-side cell efficiency alone.",
    title="Bifacial modules add system-level value",
)

strat_synthesis_bifacial_from_gain_and_density = support(
    [
        deployment_value_requires_efficiency_stability_and_area_scaling,
        bifacial_gain_depends_on_albedo_and_installation_context,
        area_normalized_performance,
    ],
    synthesis_bifacial_modules_add_system_value,
    reason=(
        "Bifacial value is routed through deployment value and installation-context "
        "conditions instead of treating rear-side gain as universally portable."
    ),
    prior=0.72,
)

strat_synthesis_bifacial_from_certified_stability = support(
    [
        pvsk_bifacial_nrel_front,
        pvsk_bifacial_6000h,
        encapsulated_module_stability_axis,
    ],
    synthesis_bifacial_modules_add_system_value,
    reason="Certification and long operation support practical module relevance.",
    prior=0.68,
)


synthesis_perovskites_have_sustained_improvement_pathways = claim(
    "PVSK performance has sustained improvement pathways because efficiency, "
    "stability, hysteresis suppression, module value, and manufacturability can "
    "be repeatedly improved through reusable design axes: composition control, "
    "interface passivation, bandgap-contact engineering, dimensional/interface "
    "design, and scalable processing. This is a technical-iteration claim, not "
    "an environmental lifecycle-sustainability claim.",
    title="Perovskites have sustained technical improvement pathways",
)

strat_synthesis_sustained_pathways_from_efficiency_axes = support(
    [
        sustained_improvement_comes_from_reusable_design_axes,
        synthesis_efficiency_progression_is_interface_driven,
        synthesis_passivation_is_general_design_rule,
        synthesis_bandgap_and_contact_engineering_define_tradeoff_space,
    ],
    synthesis_perovskites_have_sustained_improvement_pathways,
    reason=(
        "Efficiency, passivation, and bandgap-contact conclusions share reusable "
        "technical design axes rather than isolated record claims."
    ),
    prior=0.72,
)

strat_synthesis_sustained_pathways_from_stability_axes = support(
    [
        sustained_improvement_comes_from_reusable_design_axes,
        synthesis_stability_requires_integrated_control,
        synthesis_hysteresis_is_practically_suppressed,
    ],
    synthesis_perovskites_have_sustained_improvement_pathways,
    reason=(
        "Stability and hysteresis suppression support sustained improvement when "
        "ion migration, passivation, and dimensional-interface mechanisms are "
        "treated as reusable controls."
    ),
    prior=0.66,
)

strat_synthesis_sustained_pathways_from_manufacturing_axes = support(
    [
        sustained_improvement_comes_from_reusable_design_axes,
        synthesis_scalable_manufacturing_is_demonstrated,
        scalable_manufacturing_requires_uniformity_yield_and_encapsulation,
    ],
    synthesis_perovskites_have_sustained_improvement_pathways,
    reason=(
        "The scalable-manufacturing connection keeps sustained improvement tied "
        "to process iteration while preserving uniformity, yield, and lifetime "
        "conditions."
    ),
    prior=0.62,
)


synthesis_industrialization_requires_three_way_alignment = claim(
    "PVSK industrialization requires simultaneous alignment of record efficiency, "
    "stress-tested stability, and scalable manufacturing; progress in only one of "
    "these axes is insufficient for deployment.",
    title="Industrialization requires efficiency-stability-scale alignment",
)

strat_synthesis_industrialization_three_axes = support(
    [
        synthesis_efficiency_progression_is_interface_driven,
        synthesis_stability_requires_integrated_control,
        synthesis_scalable_manufacturing_is_demonstrated,
    ],
    synthesis_industrialization_requires_three_way_alignment,
    reason=(
        "The core industrialization claim requires efficiency, stability, and "
        "scale axes to hold together rather than as isolated successes."
    ),
    prior=0.72,
)

strat_synthesis_industrialization_from_tandem_cost_deployment_axes = support(
    [
        synthesis_tandems_are_primary_high_efficiency_path,
        synthesis_low_cost_path_depends_on_printable_contacts,
        deployment_value_requires_efficiency_stability_and_area_scaling,
    ],
    synthesis_industrialization_requires_three_way_alignment,
    reason=(
        "Tandem upside and printable-contact cost plausibility become industrial "
        "only when deployment value also survives area and stability constraints."
    ),
    prior=0.66,
)

strat_synthesis_industrialization_from_limitation_nodes = support(
    [
        tandem_deployment_still_depends_on_scalable_stability,
        record_efficiency_vs_module_scaling_is_not_automatic,
        stability_under_single_stressor_does_not_guarantee_field_stability,
        cost_projection_depends_on_yield_lifetime_and_throughput,
        synthesis_perovskites_have_sustained_improvement_pathways,
    ],
    synthesis_industrialization_requires_three_way_alignment,
    reason=(
        "The industrialization conclusion stays cautious because the main "
        "limitation nodes remain active: tandem deployment, record-to-module "
        "transfer, field stability, and cost-model conditions."
    ),
    prior=0.58,
)
