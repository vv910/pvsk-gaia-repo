"""
Priors for independent claims in Jia2025 package.

These priors are assigned to leaf claims that are not derived from other claims.
"""

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


PRIORS = {
    perovskite_silicon_tscs_introduced: (
        0.90,
        "Well-established background in photovoltaic research [@Jia2025]."
    ),
    sam_advantages: (
        0.90,
        "Well-known advantages of SAMs widely reported in literature [@Jia2025]."
    ),
    single_junction_plateau: (
        0.85,
        "Common knowledge in photovoltaic field based on NREL efficiency chart [@Jia2025]."
    ),
    reference_sams: (
        0.90,
        "Directly reported synthesis and characterization in the paper [@Jia2025]."
    ),
    thermal_stability: (
        0.85,
        "Direct measurement from thermal gravimetric analysis reported in paper [@Jia2025]."
    ),
    device_configuration: (
        0.90,
        "Standard device stack described in paper [@Jia2025]."
    ),
    pl_peak_at_733nm: (
        0.85,
        "Direct spectroscopic measurement consistent with 1.69 eV bandgap [@Jia2025]."
    ),
    ups_valence_band: (
        0.85,
        "Direct UPS measurement reported in paper [@Jia2025]."
    ),
    all_sams_good_photostability: (
        0.85,
        "Direct NMR measurement after 24h illumination reported in paper [@Jia2025]."
    ),
    htl201_chemical_verification: (
        0.85,
        "Verified by multiple spectroscopic methods (NMR, MS, FTIR) in paper [@Jia2025]."
    ),
    water_contact_angles: (
        0.85,
        "Direct contact angle measurement reported in paper [@Jia2025]."
    ),
    perovskite_precursor_contact: (
        0.85,
        "Direct contact angle measurement with perovskite precursor reported [@Jia2025]."
    ),
    htl201_smooth_uniform: (
        0.85,
        "AFM measurement directly showing smooth uniform surface [@Jia2025]."
    ),
    perovskite_thickness: (
        0.85,
        "Direct SEM measurement of perovskite film thickness [@Jia2025]."
    ),
    htl201_enhanced_crystallinity: (
        0.80,
        "XRD measurement showing increased diffraction intensity and preferred orientation [@Jia2025]."
    ),
    htl201_delayed_nucleation: (
        0.80,
        "In-situ observation of nucleation timing via optical microscopy and PL [@Jia2025]."
    ),
    htl201_brighter_pl_mapping: (
        0.85,
        "Direct PL mapping imaging measurement [@Jia2025]."
    ),
    htl201_most_significant_pb_shift: (
        0.80,
        "Direct XPS measurement of Pb 4f core level shifts [@Jia2025]."
    ),
    htl201_highest_conducting_current: (
        0.80,
        "Direct C-AFM measurement of conducting current [@Jia2025]."
    ),
    asymmetric_design: (
        0.85,
        "Molecular structure confirmed by NMR and described in paper [@Jia2025]."
    ),
    htl201_stronger_affinity: (
        0.80,
        "Molecular dynamics simulation result, supported by experimental data [@Jia2025]."
    ),
    htl201_higher_fractional_coverage: (
        0.80,
        "Simulation result validated by experimental coverage factors [@Jia2025]."
    ),
    coverage_factors_before_wash: (
        0.80,
        "Quantitative XPS analysis reported in paper [@Jia2025]."
    ),
    coverage_factors_stable: (
        0.80,
        "XPS measurements across multiple washing cycles reported [@Jia2025]."
    ),
    htl201_higher_coverage_factor: (
        0.80,
        "Consistent experimental result across all conditions in paper [@Jia2025]."
    ),
    sam_thickness_comparable_to_molecule_length: (
        0.80,
        "Spectroscopic ellipsometry measurement consistent with monolayer formation [@Jia2025]."
    ),
    htl201_strong_binding_perovskite: (
        0.80,
        "DFT calculation validated by binding energy measurements [@Jia2025]."
    ),
    htl201_passivates_pb_defects: (
        0.75,
        "DFT calculation showing shorter N-Pb distance and higher binding energy [@Jia2025]."
    ),
    htl201_average_pce: (
        0.85,
        "Statistical average from 20 independent devices with clear protocol [@Jia2025]."
    ),
    htl201_champion_pce: (
        0.90,
        "Best device performance from 20 devices, with detailed J-V parameters [@Jia2025]."
    ),
    me4pacz_average_pce: (
        0.85,
        "Statistical average from 20 independent devices [@Jia2025]."
    ),
    eqe_integrated_current: (
        0.80,
        "Integrated from EQE measurement reported in paper [@Jia2025]."
    ),
    htl201_enhanced_crystallinity: (
        0.80,
        "XRD and GIWAXS measurements showing enhanced crystallinity [@Jia2025]."
    ),
    htl201_higher_carrier_lifetime: (
        0.85,
        "Time-resolved PL measurement with clear protocol [@Jia2025]."
    ),
    plqry_values: (
        0.85,
        "PLQY measurement using integrated sphere at 1-sun equivalent intensity [@Jia2025]."
    ),
    qfls_values: (
        0.80,
        "Calculated from PLQY results using standard method [@Jia2025]."
    ),
    homo_levels_by_ups: (
        0.85,
        "Direct UPS measurement reported in paper [@Jia2025]."
    ),
    htl201_minimal_energy_difference: (
        0.80,
        "Calculated from UPS-measured HOMO levels and perovskite valence band [@Jia2025]."
    ),
    htl201_smaller_pff_ff_difference: (
        0.80,
        "Suns-Voc measurement for single-junction inverted devices [@Jia2025]."
    ),
    htl201_lower_reverse_saturation: (
        0.80,
        "Dark J-V measurement showing lower reverse saturation current [@Jia2025]."
    ),
    htl201_shelf_life_98_9_percent: (
        0.85,
        "Shelf-life test over 1080h with clear experimental protocol [@Jia2025]."
    ),
    htl201_operational_25c_98_percent: (
        0.85,
        "MPPT measurement at 25C for 1020h under 1-sun illumination [@Jia2025]."
    ),
    htl201_operational_45c_91_3_percent: (
        0.85,
        "MPPT measurement at 45C for 1020h under 1-sun illumination [@Jia2025]."
    ),
    meo4pacz_operational_stability: (
        0.85,
        "MPPT measurement with same protocol as HTL201 devices [@Jia2025]."
    ),
    me4pacz_significant_decline: (
        0.80,
        "Clear operational stability decline observed after 500h [@Jia2025]."
    ),
    htl201_better_electrochemical_stability: (
        0.80,
        "Cyclic voltammetry measurement showing stable redox peaks for HTL201 [@Jia2025]."
    ),
    izo_htl201_strong_interaction: (
        0.85,
        "XPS measurement showing 0.7 eV and 0.5 eV shifts for Zn 2p and In 3d [@Jia2025]."
    ),
    htl201_impeded_leakage_reduced_recombination: (
        0.80,
        "Explains observed stability improvement based on device physics [@Jia2025]."
    ),
    certified_pce_34_58: (
        0.90,
        "Certified by European Solar Test Installation (ESTI) [@Jia2025]."
    ),
    htl201_derivatives_also_good: (
        0.80,
        "Device performance data for HTL203 and HTL207 reported in paper [@Jia2025]."
    ),
    htl201_perovskite_dense_uniform: (
        0.80,
        "SEM observation of dense uniform morphology with larger grain size [@Jia2025]."
    ),
}