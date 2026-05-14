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
# These are set based on evidence quality and source reliability

PRIORS = {
    # Very high confidence: direct experimental measurements with clear protocols
    pce_9_7_percent: (0.92, "Direct measurement with calibrated solar simulator, NREL-calibrated reference cell"),
    jsc_17_6_ma_cm2: (0.92, "Direct measurement with Keithley source meter under standard conditions"),
    voc_0_888_v: (0.92, "Direct voltage measurement under illumination"),
    ff_0_62: (0.90, "Calculated from J-V curve with established formula"),

    # High confidence: spectroscopic measurements
    bandgap_1_5_ev: (0.88, "Determined from Kubelka-Munk analysis of reflectance data, consistent with literature"),
    tiO2_bandgap_3_1_ev: (0.88, "Determined from Kubelka-Munk analysis, consistent with known TiO2 value"),
    evb_minus_5_43_ev: (0.85, "UPS measurement with known photon energy calibration"),
    ecb_minus_3_93_ev: (0.85, "Calculated from bandgap and EVB, consistent energy level alignment"),

    # Moderate confidence: stability observations
    stability_improvement: (0.85, "500+ hour stability test with multiple parameters tracked"),
    stability_observation_1: (0.88, "Direct current measurement over 500 hours"),
    stability_observation_2: (0.88, "Direct voltage measurement over 500 hours"),
    stability_observation_3: (0.85, "Fill factor calculated from J-V curves at multiple time points"),

    # Moderate confidence: spectroscopic observations
    ipce_over_50_percent: (0.85, "Direct IPCE measurement with calibrated system"),
    band_edge_emission_780nm: (0.85, "Steady-state emission measurement"),
    exciton_decay_multiexponential: (0.82, "Time-resolved single photon counting, clear multiexponential fit"),
    reductive_quenching_observed: (0.85, "TAS measurements on multiple samples with consistent results"),
    hole_injection_mechanism: (0.85, "TAS comparison between samples with/without HTM"),

    # Device structure and properties
    device_structure: (0.90, "Cross-sectional SEM imaging confirms structure"),
    absorption_coefficient: (0.85, "Calculated from reflectance data using established method"),
    charge_separation_mechanism: (0.82, "Combined PIA and TAS results, consistent with literature"),

    # TiO2 thickness dependence
    jsc_vs_tio2_thickness: (0.85, "Multiple samples measured across thickness range"),
    voc_vs_tio2_thickness: (0.85, "Multiple samples measured, clear trend observed"),
    ff_vs_tio2_thickness: (0.85, "Multiple samples measured, consistent with theory"),
    pce_vs_tio2_thickness: (0.85, "Multiple samples measured, efficiency calculated from J-V curves"),
    dark_current_scaled_linearly: (0.82, "Impedance spectroscopy measurements, clear linear relationship"),
    recombination_resistance_decreased: (0.82, "Impedance analysis with consistent fitting"),
    electron_lifetime_decreased: (0.82, "Calculated from C_A and R_CT, consistent with physical understanding"),
    delta_voc_reduction: (0.82, "Consistent with impedance spectroscopy analysis"),

    # Synthesis and fabrication
    perovskite_synthesis: (0.88, "Well-established synthesis method, washed and characterized"),
    tiO2_nanoparticle_synthesis: (0.88, "Standard synthesis with acetic acid hydrolysis and autoclaving"),
    device_fabrication: (0.85, "Detailed protocol with multiple processing steps, characterized by SEM"),

    # Background knowledge
    solid_state_sensitized_solar_cells_background: (0.95, "Established background knowledge in the field"),
    perovskite_nanocrystals_as_light_harvesters: (0.82, "Literature values cited, consistent with observations"),

    # Additional missing priors (from orphaned list)
    pce_9_7_percent: (0.92, "Direct measurement with calibrated solar simulator, NREL-calibrated reference cell"),
    absorption_coefficient: (0.85, "Calculated from reflectance data using established method"),
    band_edge_emission_780nm: (0.85, "Steady-state emission measurement"),
    dark_current_scaled_linearly: (0.82, "Impedance spectroscopy measurements, clear linear relationship"),
    delta_voc_reduction: (0.82, "Consistent with impedance spectroscopy analysis"),
    ecb_minus_3_93_ev: (0.85, "Calculated from bandgap and EVB, consistent energy level alignment"),
    electron_lifetime_decreased: (0.82, "Calculated from C_A and R_CT, consistent with physical understanding"),
    evb_minus_5_43_ev: (0.85, "UPS measurement with known photon energy calibration"),
    exciton_decay_multiexponential: (0.82, "Time-resolved single photon counting, clear multiexponential fit"),
    ff_vs_tio2_thickness: (0.85, "Multiple samples measured, consistent with theory"),
    ipce_over_50_percent: (0.85, "Direct IPCE measurement with calibrated system"),
    jsc_vs_tio2_thickness: (0.85, "Multiple samples measured across thickness range"),
    pce_vs_tio2_thickness: (0.85, "Multiple samples measured, efficiency calculated from J-V curves"),
    recombination_resistance_decreased: (0.82, "Impedance analysis with consistent fitting"),
    reductive_quenching_observed: (0.85, "TAS measurements on multiple samples with consistent results"),
    voc_vs_tio2_thickness: (0.85, "Multiple samples measured, clear trend observed"),
    device_structure: (0.90, "Cross-sectional SEM imaging confirms structure"),

    # Strategy conclusions needing priors
    panchromatic_absorption_leads_to_high_jsc: (0.85, "Conclusion supported by multiple measurements"),
    pce_prediction_from_individual_params: (0.88, "Calculated from independently measured JSC, VOC, FF"),
}