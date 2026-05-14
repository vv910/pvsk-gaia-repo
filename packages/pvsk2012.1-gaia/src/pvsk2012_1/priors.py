from .motivation import (
    solid_state_sensitized_solar_cells_background,
    perovskite_nanocrystals_as_light_harvesters,
    pce_9_7_percent,
    jsc_17_6_ma_cm2,
    voc_0_888_v,
    ff_0_62,
    ipce_over_50_percent,
    bandgap_1_5_ev,
    tiO2_bandgap_3_1_ev,
    evb_minus_5_43_ev,
    ecb_minus_3_93_ev,
    stability_improvement,
    charge_separation_mechanism,
    device_structure,
    absorption_coefficient,
)

from .s2_methods import (
    perovskite_synthesis,
    tiO2_nanoparticle_synthesis,
    device_fabrication,
)

from .s3_results import (
    jsc_vs_tio2_thickness,
    voc_vs_tio2_thickness,
    ff_vs_tio2_thickness,
    pce_vs_tio2_thickness,
    dark_current_scaled_linearly,
    recombination_resistance_decreased,
    electron_lifetime_decreased,
    band_edge_emission_780nm,
    exciton_decay_multiexponential,
    reductive_quenching_observed,
    hole_injection_mechanism,
    delta_voc_reduction,
)

from .s4_discussion import (
    stability_observation_1,
    stability_observation_2,
    stability_observation_3,
    panchromatic_absorption_leads_to_high_jsc,
    pce_prediction_from_individual_params,
)


# Priors for independent claims (leaf nodes that need prior values)
# Evidence quality guidelines:
#   0.65-0.85: supported by evidence but imperfect / single source / method-dependent
#   0.85-0.95: well-established fact or strong experimental observation

PRIORS = {
    # Independent premises - adjusted to 0.65-0.85 range per review requirement
    # Direct experimental measurements
    pce_9_7_percent: (0.82, "Direct power conversion efficiency measurement under standard illumination"),
    jsc_17_6_ma_cm2: (0.82, "Direct current density measurement with calibrated source meter"),
    voc_0_888_v: (0.82, "Direct voltage measurement under illumination"),
    ff_0_62: (0.80, "Fill factor calculated from J-V curve with established formula"),

    # Spectroscopic measurements
    bandgap_1_5_ev: (0.80, "Determined from Kubelka-Munk analysis of reflectance data"),
    tiO2_bandgap_3_1_ev: (0.80, "Determined from Kubelka-Munk analysis, consistent with literature"),
    evb_minus_5_43_ev: (0.75, "UPS measurement with known photon energy calibration"),
    ecb_minus_3_93_ev: (0.75, "Calculated from bandgap and EVB, consistent energy level alignment"),

    # Stability observations - single source, method-dependent
    stability_improvement: (0.78, "500+ hour stability test with multiple parameters tracked"),
    stability_observation_1: (0.78, "Direct current measurement over 500 hours"),
    stability_observation_2: (0.78, "Direct voltage measurement over 500 hours"),
    stability_observation_3: (0.75, "Fill factor calculated from J-V curves at multiple time points"),

    # Spectroscopic observations
    ipce_over_50_percent: (0.75, "Direct IPCE measurement with calibrated system"),
    band_edge_emission_780nm: (0.75, "Steady-state emission measurement"),
    exciton_decay_multiexponential: (0.72, "Time-resolved single photon counting, multiexponential fit"),
    reductive_quenching_observed: (0.75, "TAS measurements on multiple samples"),
    hole_injection_mechanism: (0.75, "TAS comparison between samples with/without HTM"),

    # Device structure and properties
    device_structure: (0.78, "Cross-sectional SEM imaging confirms structure"),
    absorption_coefficient: (0.75, "Calculated from reflectance data using established method"),
    charge_separation_mechanism: (0.72, "Combined PIA and TAS results, consistent with literature"),

    # TiO2 thickness dependence - single study
    jsc_vs_tio2_thickness: (0.72, "Multiple samples measured across thickness range"),
    voc_vs_tio2_thickness: (0.72, "Multiple samples measured, clear trend observed"),
    ff_vs_tio2_thickness: (0.72, "Multiple samples measured, consistent with theory"),
    pce_vs_tio2_thickness: (0.72, "Multiple samples measured, efficiency calculated from J-V curves"),
    dark_current_scaled_linearly: (0.70, "Impedance spectroscopy measurements, clear linear relationship"),
    recombination_resistance_decreased: (0.70, "Impedance analysis with consistent fitting"),
    electron_lifetime_decreased: (0.70, "Calculated from C_A and R_CT, consistent with physical understanding"),
    delta_voc_reduction: (0.70, "Consistent with impedance spectroscopy analysis"),

    # Synthesis and fabrication
    perovskite_synthesis: (0.78, "Well-established synthesis method, characterized"),
    tiO2_nanoparticle_synthesis: (0.78, "Standard synthesis with acetic acid hydrolysis and autoclaving"),
    device_fabrication: (0.75, "Detailed protocol with multiple processing steps, characterized by SEM"),

    # Background knowledge - well-established
    solid_state_sensitized_solar_cells_background: (0.85, "Established background knowledge in the field"),
    perovskite_nanocrystals_as_light_harvesters: (0.75, "Literature values cited, consistent with observations"),

    # Derived/background claims needing priors
    panchromatic_absorption_leads_to_high_jsc: (0.75, "Conclusion supported by multiple measurements"),
    pce_prediction_from_individual_params: (0.78, "Calculated from independently measured JSC, VOC, FF"),
}