"""
S2: Directed cross-package support.

These are non-equivalence relationships where one paper's exported claim makes
another paper's claim more plausible or better motivated.
"""

from gaia.lang import support

from ._imports import (
    pvsk2012_1_solid_stability,
    pvsk2012_2_al2o3_best,
    pvsk2013_sequential_deposition,
    pvsk2013_reproducibility,
    pvsk2014_bilayer_architecture,
    pvsk2014_certified_efficiency,
    pvsk2014_full_coverage,
    pvsk2015_phase_stabilization,
    pvsk2015_synergetic_effect,
    pvsk_triple_cation_strategy,
    pvsk_triple_cation_best_pce,
    pvsk2017_2d3d_composite,
    pvsk2017_cb_upshift,
    pvsk2017_one_year_stability,
    pvsk_mda_alpha_stabilization,
    pvsk_damp_heat_dual_passivation,
    pvsk_damp_heat_t95,
    pvsk_damp_heat_iec,
    pvsk_all_inorganic_ion_migration,
    pvsk_formate_interfaces,
    pvsk_formate_recombination_reduction,
    pvsk_all_tandem_passivation_route,
    pvsk_all_tandem_certified,
    pvsk_all_tandem_diffusion_length,
    pvsk_3d3d_phj_solution,
    pvsk_3d3d_type2_alignment,
    pvsk_3d3d_tandem_champion,
    pvsk_persik_2024_bilateral_passivation,
    pvsk_persik_2024_nrel_certified,
    pvsk_persik_2024_sq_limit,
    pvsk_htl201_binding,
    pvsk_htl201_certified,
    pvsk_htl201_pb_passivation,
    pvsk_dipolar_strategy,
    pvsk_dipolar_diffusion_length,
    pvsk_dipolar_jet_certified,
    pvsk_dipolar_type_ii_alignment,
    pvsk_r2r_pfsd,
    pvsk_r2r_best_cell,
    pvsk_bifacial_6000h,
    pvsk_bifacial_damp_heat,
    pvsk_homogeneous_2d_fabr,
)


support_solid_state_to_meso_superstructure = support(
    [pvsk2012_1_solid_stability],
    pvsk2012_2_al2o3_best,
    reason=(
        "The solid-state replacement of liquid electrolyte makes Lee 2012's "
        "meso-superstructured high-efficiency device more plausible as a general "
        "architecture, not an isolated result."
    ),
    prior=0.82,
)


support_sequential_control_to_bilayer_uniformity = support(
    [pvsk2013_sequential_deposition, pvsk2013_reproducibility],
    pvsk2014_full_coverage,
    reason=(
        "The 2013 sequential-deposition package establishes conversion and "
        "reproducibility control that supports the 2014 full-coverage bilayer "
        "film result."
    ),
    prior=0.78,
)


support_bilayer_architecture_to_certified_efficiency = support(
    [pvsk2014_bilayer_architecture],
    pvsk2014_certified_efficiency,
    reason=(
        "The bilayer architecture claim is the architectural premise behind the "
        "2014 certified-efficiency improvement."
    ),
    prior=0.84,
)


support_mixed_cation_to_triple_cation = support(
    [pvsk2015_phase_stabilization, pvsk2015_synergetic_effect],
    pvsk_triple_cation_strategy,
    reason=(
        "The 2015 mixed-cation stabilization evidence directly motivates the later "
        "triple-cation strategy."
    ),
    prior=0.86,
)


support_triple_cation_to_2d3d_stability = support(
    [pvsk_triple_cation_best_pce, pvsk_triple_cation_strategy],
    pvsk2017_2d3d_composite,
    reason=(
        "The triple-cation result supports the feasibility of combining phase-stable "
        "bulk composition with 2D/3D interface engineering."
    ),
    prior=0.76,
)


support_2d3d_to_damp_heat = support(
    [pvsk2017_2d3d_composite, pvsk2017_one_year_stability],
    pvsk_damp_heat_t95,
    reason=(
        "The 2017 2D/3D stability result supports the later tailored-dimensionality "
        "claim that similar dimensional control can survive damp-heat testing."
    ),
    prior=0.82,
)


support_mda_to_stable_alpha_phase = support(
    [pvsk_mda_alpha_stabilization],
    pvsk_damp_heat_dual_passivation,
    reason=(
        "MDA-based alpha-phase stabilization supports the broader idea that local "
        "chemical stabilization can be paired with interface protection."
    ),
    prior=0.73,
)


support_capping_to_ion_migration_suppression = support(
    [pvsk_damp_heat_dual_passivation],
    pvsk_all_inorganic_ion_migration,
    reason=(
        "The 2D/3D damp-heat package supports the all-inorganic capping claim by "
        "showing that dimensional interfaces can function as stability barriers."
    ),
    prior=0.77,
)


support_formate_to_grain_passivation = support(
    [pvsk_formate_interfaces, pvsk_formate_recombination_reduction],
    pvsk_all_tandem_passivation_route,
    reason=(
        "Formate interface passivation supplies a chemical precedent for the "
        "wide-bandgap grain-surface passivation route."
    ),
    prior=0.80,
)


support_grain_passivation_to_diffusion_length = support(
    [pvsk_all_tandem_passivation_route],
    pvsk_all_tandem_diffusion_length,
    reason=(
        "The grain-surface passivation route supports the observed diffusion-length "
        "increase by suppressing recombination-active defects."
    ),
    prior=0.86,
)


support_2d3d_band_shift_to_dipolar_alignment = support(
    [pvsk2017_cb_upshift],
    pvsk_dipolar_type_ii_alignment,
    reason=(
        "The 2017 conduction-band upshift from 2D/3D grading supports the later "
        "dipolar-passivation claim that interfacial electrostatics can tune band "
        "alignment."
    ),
    prior=0.74,
)


support_3d3d_to_persik_bilateral_passivation = support(
    [pvsk_3d3d_type2_alignment, pvsk_3d3d_phj_solution],
    pvsk_persik_2024_bilateral_passivation,
    reason=(
        "The 3D/3D bilayer heterojunction supplies a band-alignment precedent for "
        "the bilateral passivation strategy used in perovskite/silicon tandems."
    ),
    prior=0.81,
)


support_all_perovskite_to_3d3d_tandem = support(
    [pvsk_all_tandem_certified],
    pvsk_3d3d_tandem_champion,
    reason=(
        "The certified all-perovskite tandem result supports the viability of later "
        "3D/3D tandem optimization."
    ),
    prior=0.79,
)


support_3d3d_to_persik_record = support(
    [pvsk_3d3d_type2_alignment],
    pvsk_persik_2024_sq_limit,
    reason=(
        "The type-II 3D/3D alignment result supports the 2024 claim that bilayer "
        "interface design can help perovskite/silicon tandems exceed the "
        "single-junction limit."
    ),
    prior=0.80,
)


support_persik_to_htl201_record = support(
    [pvsk_persik_2024_nrel_certified],
    pvsk_htl201_certified,
    reason=(
        "The 2024 certified perovskite/silicon record supports the 2025 HTL201 "
        "record as an incremental continuation of the same tandem pathway."
    ),
    prior=0.87,
)


support_htl201_to_dipolar_buried_interface = support(
    [pvsk_htl201_binding, pvsk_htl201_pb_passivation],
    pvsk_dipolar_strategy,
    reason=(
        "HTL201's strong binding and Pb-defect passivation support the later buried "
        "interface dipolar-passivation design rule."
    ),
    prior=0.78,
)


support_dipolar_to_tandem_certification = support(
    [pvsk_dipolar_strategy, pvsk_dipolar_diffusion_length],
    pvsk_dipolar_jet_certified,
    reason=(
        "Dipolar buried-interface passivation and diffusion-length enhancement "
        "jointly support the certified tandem performance."
    ),
    prior=0.86,
)


support_damp_heat_to_bifacial_stability = support(
    [pvsk_damp_heat_iec],
    pvsk_bifacial_damp_heat,
    reason=(
        "The 2022 damp-heat package supports the later bifacial module damp-heat "
        "stability result as a related environmental-stability target."
    ),
    prior=0.76,
)


support_bifacial_stability_to_long_operation = support(
    [pvsk_bifacial_damp_heat],
    pvsk_bifacial_6000h,
    reason=(
        "Damp-heat retention supports the broader claim that bifacial modules can "
        "maintain performance during long operational tests."
    ),
    prior=0.80,
)


support_r2r_process_to_cell_performance = support(
    [pvsk_r2r_pfsd],
    pvsk_r2r_best_cell,
    reason=(
        "The PFSD process claim supports the roll-to-roll best-cell performance by "
        "linking scalable coating to device quality."
    ),
    prior=0.82,
)


support_homogeneous_2d_to_scale = support(
    [pvsk_homogeneous_2d_fabr],
    pvsk_r2r_pfsd,
    reason=(
        "Homogeneous 2D passivation at large area supports the broader feasibility "
        "of scalable coating processes that must preserve interface quality."
    ),
    prior=0.70,
)
