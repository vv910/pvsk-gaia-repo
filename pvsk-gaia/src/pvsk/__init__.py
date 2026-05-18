"""
PVSK synthesis package.

This package builds a cross-package reasoning graph over the exported public
claims of 22 perovskite solar-cell Gaia packages.  It does not re-formalize the
source papers; it imports their top-level public claims and adds synthesis-layer
agreement, support, tension, induction, and final conclusion nodes.
"""

from .s5_synthesis import (
    synthesis_bandgap_and_contact_engineering_define_tradeoff_space,
    synthesis_efficiency_progression_is_interface_driven,
    synthesis_hysteresis_is_practically_suppressed,
    synthesis_mechanistic_tensions_are_conditionally_resolved,
    synthesis_passivation_is_general_design_rule,
    synthesis_perovskites_are_validated_pv_platform,
    synthesis_stability_requires_integrated_control,
    synthesis_tandems_are_primary_high_efficiency_path,
)
from .s6_cost_analysis import (
    synthesis_bifacial_modules_add_system_value,
    synthesis_industrialization_requires_three_way_alignment,
    synthesis_low_cost_path_depends_on_printable_contacts,
    synthesis_perovskites_have_sustained_improvement_pathways,
    synthesis_scalable_manufacturing_is_demonstrated,
)


__all__ = [
    "synthesis_perovskites_are_validated_pv_platform",
    "synthesis_efficiency_progression_is_interface_driven",
    "synthesis_passivation_is_general_design_rule",
    "synthesis_stability_requires_integrated_control",
    "synthesis_hysteresis_is_practically_suppressed",
    "synthesis_bandgap_and_contact_engineering_define_tradeoff_space",
    "synthesis_tandems_are_primary_high_efficiency_path",
    "synthesis_mechanistic_tensions_are_conditionally_resolved",
    "synthesis_scalable_manufacturing_is_demonstrated",
    "synthesis_low_cost_path_depends_on_printable_contacts",
    "synthesis_bifacial_modules_add_system_value",
    "synthesis_perovskites_have_sustained_improvement_pathways",
    "synthesis_industrialization_requires_three_way_alignment",
]
