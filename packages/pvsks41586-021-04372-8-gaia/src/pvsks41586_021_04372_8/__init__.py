"""
All-perovskite tandem solar cells with improved grain surface passivation.

Lin et al., Nature 2022 (https://doi.org/10.1038/s41586-021-04372-8)

A Gaia knowledge package formalizing the key findings on grain surface passivation
using CF3-PA to enable thick Pb-Sn perovskite absorbers and achieve 26.4% certified
efficiency in all-perovskite tandem solar cells.
"""

from gaia.lang import claim, setting

# Import all module exports
from .motivation import (
    perovskite_tunable_bandgap,
    tandem_structure,
    low_photocurrent_limitation,
    thick_absorber_needed,
    short_diffusion_length,
    grain_surface_passivation_route,
    thickness_limited_by_passivation,
    cf3_pa_hypothesis,
    research_question,
    certified_26_4_percent,
    stability_600h,
)

from .s2_dft_methods import (
    three_ammonium_cations,
    electrostatic_potential_ordering,
    cf3_pa_complete_adsorption,
    pea_pa_incomplete_adsorption,
    cf3_pa_suppresses_iodine_vacancies,
    cf3_pa_strongest_binding,
    deep_in_gap_states_eliminated,
    sn_vacancy_formation_increased,
    donor_defect_reduction,
)

from .s3_results import (
    optimal_concentrations,
    cf3_pa_best_pv_parameters,
    jsc_increases_with_thickness_cf3,
    control_jsc_saturates,
    best_cf3_pa_device,
    average_pc3_pa_200_devices,
    eqe_integrated_jsc,
)

from .s4_characterization import (
    passivator_no_morphology_change,
    cf3_pa_at_surfaces_and_boundaries,
    single_3d_perovskite_phase,
    no_2d_peaks_high_concentration,
    sn4_plus_at_surface_control,
    sn2_plus_oxidation_suppressed,
    pl_intensity_enhanced_cf3,
    carrier_lifetimes,
    similar_dc_mobility,
    diffusion_length_increased_threefold,
    limiting_carrier_mobility,
)

from .s5_tandem_results import (
    wbg_cell_pce,
    thicknesses_optimized,
    jsc_increases_with_nbg_thickness,
    pce_increases_with_thickness,
    best_tandem_reverse,
    eqe_matched_currents,
    average_tandem_96_devices,
    certified_pce_264_percent,
    large_area_tandem,
    shelf_stability_2400h,
    operational_stability_600h,
)

# Exported conclusions - the paper's core contributions
__all__ = [
    # Background
    "perovskite_tunable_bandgap",
    "tandem_structure",
    "low_photocurrent_limitation",
    "thick_absorber_needed",
    "short_diffusion_length",
    "grain_surface_passivation_route",
    "thickness_limited_by_passivation",
    "cf3_pa_hypothesis",
    "research_question",
    # DFT predictions
    "three_ammonium_cations",
    "electrostatic_potential_ordering",
    "cf3_pa_complete_adsorption",
    "pea_pa_incomplete_adsorption",
    "cf3_pa_suppresses_iodine_vacancies",
    "cf3_pa_strongest_binding",
    "deep_in_gap_states_eliminated",
    "sn_vacancy_formation_increased",
    "donor_defect_reduction",
    # Pb-Sn PSC results
    "optimal_concentrations",
    "cf3_pa_best_pv_parameters",
    "jsc_increases_with_thickness_cf3",
    "control_jsc_saturates",
    "best_cf3_pa_device",
    "average_pc3_pa_200_devices",
    "eqe_integrated_jsc",
    # Characterization
    "passivator_no_morphology_change",
    "cf3_pa_at_surfaces_and_boundaries",
    "single_3d_perovskite_phase",
    "no_2d_peaks_high_concentration",
    "sn4_plus_at_surface_control",
    "sn2_plus_oxidation_suppressed",
    "pl_intensity_enhanced_cf3",
    "carrier_lifetimes",
    "similar_dc_mobility",
    "diffusion_length_increased_threefold",
    "limiting_carrier_mobility",
    # Tandem results
    "wbg_cell_pce",
    "thicknesses_optimized",
    "jsc_increases_with_nbg_thickness",
    "pce_increases_with_thickness",
    "best_tandem_reverse",
    "eqe_matched_currents",
    "average_tandem_96_devices",
    "certified_pce_264_percent",
    "large_area_tandem",
    "shelf_stability_2400h",
    "operational_stability_600h",
    # Exported key conclusions
    "certified_26_4_percent",
    "stability_600h",
]