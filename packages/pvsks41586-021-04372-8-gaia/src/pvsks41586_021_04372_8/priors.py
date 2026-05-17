"""
Prioirs for pvsks41586-021-04372-8-gaia package.

Assigns priors to independent leaf claims that are not derived from other claims.
Derived conclusions should not get priors - they get their beliefs from BP propagation.
"""

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


PRIORS = {
    # Background on perovskite and tandem structure
    perovskite_tunable_bandgap: (
        0.9,
        "Well-established property of metal-halide perovskites, widely reported in literature."
    ),
    tandem_structure: (
        0.9,
        "Standard architecture for all-perovskite tandem cells, established in literature."
    ),
    low_photocurrent_limitation: (
        0.85,
        "Reported limitation based on certified efficiency records (Green et al., Prog. Photovoltaics 2021)."
    ),
    thick_absorber_needed: (
        0.9,
        "Physical requirement from current-matching condition in tandem solar cells."
    ),
    short_diffusion_length: (
        0.85,
        "Widely reported property of polycrystalline Pb-Sn perovskite thin films."
    ),
    grain_surface_passivation_route: (
        0.85,
        "Established approach with evidence from multiple prior works."
    ),
    thickness_limited_by_passivation: (
        0.8,
        "Reported limitation supported by experimental evidence in prior works."
    ),
    cf3_pa_hypothesis: (
        0.7,
        "Rational hypothesis based on molecular design considerations."
    ),

    # DFT methods results
    three_ammonium_cations: (
        0.95,
        "Direct statement of experimental design, not a derived claim."
    ),
    electrostatic_potential_ordering: (
        0.9,
        "Computational result from Gaussian calculations with established methods."
    ),
    cf3_pa_complete_adsorption: (
        0.8,
        "Simulation result at 400K showing complete adsorption of 16/16 CF3-PA molecules."
    ),
    pea_pa_incomplete_adsorption: (
        0.8,
        "Simulation result showing incomplete adsorption for PA (15/16) and PEA (13/16)."
    ),
    cf3_pa_suppresses_iodine_vacancies: (
        0.75,
        "Prediction from MD simulations, partially supported by experimental observations."
    ),
    cf3_pa_strongest_binding: (
        0.85,
        "DFT-calculated binding energies with established methodology."
    ),
    deep_in_gap_states_eliminated: (
        0.8,
        "Electronic structure calculation result from DFT."
    ),
    sn_vacancy_formation_increased: (
        0.75,
        "Defect formation energy calculation from DFT."
    ),
    donor_defect_reduction: (
        0.7,
        "Prediction from DFT calculations in Supplementary Note 1."
    ),

    # Device performance results
    optimal_concentrations: (
        0.9,
        "Experimental optimization result from systematic concentration studies."
    ),
    cf3_pa_best_pv_parameters: (
        0.85,
        "Direct experimental measurement across 15 devices for each type."
    ),
    jsc_increases_with_thickness_cf3: (
        0.85,
        "Direct measurement showing Jsc increasing from 750nm to 1200nm device."
    ),
    control_jsc_saturates: (
        0.85,
        "Direct measurement showing Jsc saturation and Voc/FF degradation in control devices."
    ),
    best_cf3_pa_device: (
        0.85,
        "Best device measurement with stabilized efficiency confirmation."
    ),
    average_pc3_pa_200_devices: (
        0.85,
        "Statistical result from over 200 devices, showing narrow distribution."
    ),
    eqe_integrated_jsc: (
        0.85,
        "EQE integration result consistent with J-V measurement."
    ),

    # Characterization results
    passivator_no_morphology_change: (
        0.85,
        "Direct observation from SEM imaging."
    ),
    cf3_pa_at_surfaces_and_boundaries: (
        0.85,
        "ToF-SIMS measurement showing passivator distribution."
    ),
    single_3d_perovskite_phase: (
        0.9,
        "XRD measurement showing single phase."
    ),
    no_2d_peaks_high_concentration: (
        0.85,
        "XRD measurement even at 20 mol% CF3-PA showing no 2D peaks."
    ),
    sn4_plus_at_surface_control: (
        0.85,
        "Angle-dependent XPS measurement showing Sn4+ at surface."
    ),
    sn2_plus_oxidation_suppressed: (
        0.8,
        "XPS measurement comparing control and CF3-PA films."
    ),
    pl_intensity_enhanced_cf3: (
        0.85,
        "Direct steady-state PL measurement."
    ),
    carrier_lifetimes: (
        0.85,
        "Time-resolved PL measurement with biexponential fitting."
    ),
    similar_dc_mobility: (
        0.8,
        "Terahertz spectroscopy measurement showing similar mobility."
    ),
    diffusion_length_increased_threefold: (
        0.8,
        "Calculated from mobility and lifetime measurements (Ld = sqrt(mu*tau))."
    ),
    limiting_carrier_mobility: (
        0.8,
        "Terahertz spectroscopy measurement with error bars reported."
    ),

    # Tandem results
    wbg_cell_pce: (
        0.85,
        "Direct device measurement of WBG subcell."
    ),
    thicknesses_optimized: (
        0.9,
        "Optimization result for current-matching between subcells."
    ),
    jsc_increases_with_nbg_thickness: (
        0.85,
        "Direct J-V measurement across multiple thickness values."
    ),
    pce_increases_with_thickness: (
        0.85,
        "Direct device measurement showing PCE improvement with thickness."
    ),
    best_tandem_reverse: (
        0.85,
        "Best device measurement with stabilized efficiency confirmation."
    ),
    eqe_matched_currents: (
        0.85,
        "EQE integration showing well-matched subcell currents."
    ),
    average_tandem_96_devices: (
        0.85,
        "Statistical result from 96 devices."
    ),
    certified_pce_264_percent: (
        0.9,
        "Independent JET certification, included in official efficiency tables."
    ),
    large_area_tandem: (
        0.85,
        "Direct measurement of large-area device with 1.05 cm^2 aperture."
    ),
    shelf_stability_2400h: (
        0.8,
        "Aging test measurement under controlled conditions."
    ),
    operational_stability_600h: (
        0.8,
        "MPP tracking measurement under simulated 1 Sun illumination."
    ),

    # Exported conclusions
    certified_26_4_percent: (
        0.95,
        "Independently certified PCE by JET laboratory."
    ),
    stability_600h: (
        0.85,
        "Operational stability measurement showing 90% retained after 600h."
    ),
}