"""
S6: Manufacturing, cost, and deployment synthesis.

Manufacturing conclusions use a small number of scoped warrants to avoid
overcounting closely related roll-to-roll evidence.
"""

from gaia.lang import claim, support

from ._imports import (
    pvsk_bifacial_6000h,
    pvsk_bifacial_gain,
    pvsk_bifacial_nrel_front,
    pvsk_bifacial_power_density,
    pvsk_damp_heat_iec,
    pvsk_homogeneous_2d_large_module,
    pvsk_htl201_certified,
    pvsk_r2r_best_cell,
    pvsk_r2r_carbon_electrode,
    pvsk_r2r_cells,
    pvsk_r2r_cost_prediction,
    pvsk_r2r_modules,
    pvsk_r2r_production_cost_power,
    pvsk_r2r_throughput,
)
from .s1_agreement import agreement_scalability_has_multiple_routes
from .s4_induction import (
    law_scalable_deposition_can_preserve_device_quality,
    law_stability_needs_phase_and_interface_control,
    law_tandems_raise_perovskite_efficiency_ceiling,
)


synthesis_scalable_manufacturing_is_demonstrated = claim(
    "PVSK scale-up is demonstrated at the synthesis level: roll-to-roll cells and "
    "modules, bifacial minimodules, and homogeneous 2D large modules show that "
    "device quality can survive multiple manufacturing routes.",
    title="Scalable manufacturing is demonstrated across routes",
)

strat_synthesis_scale_from_law_and_agreement = support(
    [
        law_scalable_deposition_can_preserve_device_quality,
        agreement_scalability_has_multiple_routes,
    ],
    synthesis_scalable_manufacturing_is_demonstrated,
    reason="A scalable-deposition law plus cross-route agreement support manufacturing scale-up.",
    prior=0.78,
)

strat_synthesis_scale_from_module_examples = support(
    [pvsk_r2r_cells, pvsk_r2r_modules, pvsk_homogeneous_2d_large_module],
    synthesis_scalable_manufacturing_is_demonstrated,
    reason="Roll-to-roll cells/modules and homogeneous 2D large modules provide concrete examples.",
    prior=0.70,
)


synthesis_low_cost_path_depends_on_printable_contacts = claim(
    "The low-cost PVSK path depends on printable high-throughput processing and "
    "low-cost contacts, especially carbon-based electrodes that reduce dependence "
    "on noble-metal evaporation.",
    title="Low-cost path depends on printable contacts",
)

strat_synthesis_low_cost_from_printable_contact = support(
    [pvsk_r2r_carbon_electrode, pvsk_r2r_best_cell],
    synthesis_low_cost_path_depends_on_printable_contacts,
    reason="Carbon-electrode replacement and retained device quality support printable low-cost contacts.",
    prior=0.68,
)

strat_synthesis_low_cost_from_cost_and_throughput = support(
    [pvsk_r2r_cost_prediction, pvsk_r2r_production_cost_power, pvsk_r2r_throughput],
    synthesis_low_cost_path_depends_on_printable_contacts,
    reason="Cost modeling and throughput support the economic plausibility, with model uncertainty retained.",
    prior=0.56,
)


synthesis_bifacial_modules_add_system_value = claim(
    "Bifacial perovskite modules add system-level value because rear-side collection "
    "and reflected-light power density can improve deployment economics beyond "
    "front-side cell efficiency alone.",
    title="Bifacial modules add system-level value",
)

strat_synthesis_bifacial_from_gain_and_density = support(
    [pvsk_bifacial_gain, pvsk_bifacial_power_density],
    synthesis_bifacial_modules_add_system_value,
    reason="Bifacial gain and power-density evidence support system-level value.",
    prior=0.72,
)

strat_synthesis_bifacial_from_certified_stability = support(
    [pvsk_bifacial_nrel_front, pvsk_bifacial_6000h],
    synthesis_bifacial_modules_add_system_value,
    reason="Certification and long operation support practical module relevance.",
    prior=0.68,
)


synthesis_industrialization_requires_three_way_alignment = claim(
    "PVSK industrialization requires simultaneous alignment of record efficiency, "
    "stress-tested stability, and scalable manufacturing; progress in only one of "
    "these axes is insufficient for deployment.",
    title="Industrialization requires efficiency-stability-scale alignment",
)

strat_synthesis_industrialization_three_axes = support(
    [
        law_tandems_raise_perovskite_efficiency_ceiling,
        pvsk_htl201_certified,
        law_stability_needs_phase_and_interface_control,
        pvsk_damp_heat_iec,
        law_scalable_deposition_can_preserve_device_quality,
        pvsk_r2r_cells,
    ],
    synthesis_industrialization_requires_three_way_alignment,
    reason=(
        "Industrialization requires all three axes together: certified high-efficiency "
        "tandems, stress-tested stability, and scalable roll-to-roll-compatible manufacturing."
    ),
    prior=0.78,
)
