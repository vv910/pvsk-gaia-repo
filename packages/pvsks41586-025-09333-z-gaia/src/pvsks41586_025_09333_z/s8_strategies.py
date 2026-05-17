"""
Strategies connecting claims for Jia2025 paper.

This module adds reasoning strategies that connect claims together.
"""

from gaia.lang import (
    claim,
    support,
    infer,
    contradiction,
)

# Import all claims for use in strategies
from .motivation import (
    perovskite_silicon_tscs_introduced,
    single_junction_plateau,
    voc_loss_problem,
    sam_advantages,
    existing_sams_limitation,
    research_objective,
    htl201_introduced,
    htl201_design_features,
    htl201_outcome,
    certified_pce_result,
)

from .s2_molecular_design import (
    asymmetric_design,
    htl201_chemical_verification,
    reference_sams,
    thermal_stability,
    homo_energy_levels,
)

from .s3_interface_interactions import (
    izo_htl201_strong_interaction,
    htl201_stronger_affinity,
    htl201_higher_fractional_coverage,
    coverage_factors_before_wash,
    coverage_factors_stable,
    htl201_higher_coverage_factor,
    sam_thickness_comparable_to_molecule_length,
    htl201_strong_binding_perovskite,
    htl201_passivates_pb_defects,
)

from .s4_photovoltaic_performance import (
    device_configuration,
    htl201_average_pce,
    htl201_champion_pce,
    me4pacz_average_pce,
    htl201_enhanced_voc_ff,
    eqe_integrated_current,
    certified_pce_34_58,
    htl201_derivatives_also_good,
)

from .s5_morphology_crystallinity import (
    water_contact_angles,
    perovskite_precursor_contact,
    htl201_smooth_uniform,
    htl201_perovskite_dense_uniform,
    perovskite_thickness,
    htl201_enhanced_crystallinity,
    htl201_delayed_nucleation,
)

from .s6_charge_dynamics import (
    htl201_brighter_pl_mapping,
    pl_peak_at_733nm,
    htl201_higher_carrier_lifetime,
    htl201_most_significant_pb_shift,
    plqry_values,
    qfls_values,
    ups_valence_band,
    homo_levels_by_ups,
    htl201_minimal_energy_difference,
    htl201_highest_conducting_current,
    htl201_smaller_pff_ff_difference,
    htl201_lower_reverse_saturation,
)

from .s7_stability import (
    htl201_shelf_life_98_9_percent,
    htl201_operational_25c_98_percent,
    htl201_operational_45c_91_3_percent,
    meo4pacz_operational_stability,
    me4pacz_significant_decline,
    htl201_better_electrochemical_stability,
    all_sams_good_photostability,
    htl201_impeded_leakage_reduced_recombination,
)


# Strategy: HTL201's asymmetric design supports its stronger interaction with IZO
strat_asymmetric_supports_coverage = support(
    [asymmetric_design, izo_htl201_strong_interaction],
    htl201_higher_coverage_factor,
    reason="The asymmetric molecular design of HTL201 (with spacers and anchoring groups flanking the carbazole core) creates stronger coordination interactions with IZO, leading to higher fractional coverage on the IZO surface compared to symmetric SAMs Me-4PACz and MeO-4PACz [@Jia2025].",
    prior=0.5,
)

# Strategy: HTL201 higher coverage supports better perovskite morphology
strat_coverage_supports_morphology = support(
    [htl201_higher_coverage_factor, htl201_smooth_uniform],
    htl201_perovskite_dense_uniform,
    reason="Higher SAM coverage on IZO creates a more uniform surface that promotes dense and uniform perovskite film morphology with larger grain size, as observed for HTL201 compared to Me-4PACz and MeO-4PACz.",
    prior=0.5,
)

# Strategy: HTL201's stronger binding supports defect passivation
strat_binding_supports_passivation = support(
    [htl201_strong_binding_perovskite, htl201_passivates_pb_defects],
    htl201_outcome,
    reason="The strong binding energy between HTL201 and perovskite, driven by the enhanced dipole moment from asymmetric design, enables effective coordination with Pb2+ defects at the SAM/perovskite surface, providing defect passivation that enhances QFLS and enables Voc near 2V [@Jia2025].",
    prior=0.5,
)

# Strategy: Energy level alignment supports Voc and FF enhancement
strat_energy_supports_voc_ff = support(
    [htl201_minimal_energy_difference, htl201_higher_coverage_factor],
    htl201_enhanced_voc_ff,
    reason="The minimal energy difference (0.09 eV) between HTL201 and perovskite reduces Voc loss and facilitates hole extraction, while the higher coverage reduces interfacial recombination. Together, these enable the significantly enhanced Voc and FF observed for HTL201-based devices compared to Me-4PACz and MeO-4PACz [@Jia2025].",
    prior=0.5,
)

# Strategy: Charge dynamics improvements support high PCE
strat_charge_supports_pce = support(
    [htl201_higher_carrier_lifetime, plqry_values, htl201_smaller_pff_ff_difference],
    certified_pce_34_58,
    reason="The combination of higher carrier lifetime (5860 ns), highest PLQY (0.399%), and suppressed transport losses (smaller pFF-FF difference) in HTL201 devices collectively demonstrate reduced non-radiative recombination and efficient charge extraction, which underpin the certified 34.58% PCE [@Jia2025].",
    prior=0.5,
)

# Strategy: Stability mechanisms support operational stability
strat_stability_supports_longevity = support(
    [htl201_impeded_leakage_reduced_recombination, htl201_better_electrochemical_stability],
    htl201_operational_25c_98_percent,
    reason="HTL201's impeded leakage current and reduced non-radiative recombination at the buried interface, combined with its superior electrochemical stability compared to Me-4PACz and MeO-4PACz, ensure that the device maintains high performance during extended operation. This explains the retention of 98.0% PCE after 1020h at 25C.",
    prior=0.5,
)

# Strategy: HTL201 outperforms reference SAMs
strat_htl201_outperforms = support(
    [htl201_enhanced_voc_ff, certified_pce_34_58, htl201_shelf_life_98_9_percent],
    htl201_introduced,
    reason="Multiple independent measurements confirm HTL201's superior performance: certified 34.58% PCE (vs 32.18% for Me-4PACz and 33.34% for MeO-4PACz), enhanced Voc and FF, and 98.9% retention after 1080h storage. This validates the research objective that an asymmetric SAM design can achieve full coverage and favorable energy levels for high-efficiency TSCs [@Jia2025].",
    prior=0.5,
)

# Strategy: QFLS values support high Voc
strat_qfls_supports_voc = support(
    [qfls_values, htl201_minimal_energy_difference],
    htl201_outcome,
    reason="The QFLS values of 1.270V for HTL201 and 1.267V for Me-4PACz are both high, explaining their high Voc. HTL201 achieves slightly higher QFLS due to better energy level alignment and defect passivation, contributing to its near-2V Voc.",
    prior=0.5,
)

__all__ = [
    "strat_asymmetric_supports_coverage",
    "strat_coverage_supports_morphology",
    "strat_binding_supports_passivation",
    "strat_energy_supports_voc_ff",
    "strat_charge_supports_pce",
    "strat_stability_supports_longevity",
    "strat_htl201_outperforms",
    "strat_qfls_supports_voc",
]