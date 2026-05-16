"""
Priors for independent claims in the pvskscience_abn5679 package.

Independent claims are those that are not the conclusion of any strategy.
Their priors represent the reviewer's initial belief before considering reasoning chains.
"""
from .motivation import (
    psc_efficiency_exceeds_25,
    t80_lifetime_thousand_hours,
    commercial_requirement_20_years,
    accelerated_aging_enables_rapid_screening,
    psc_sensitivity_challenge,
    research_objective,
    inorganic_cs_pbi3_chosen,
    capped_vs_uncapped_device_structure,
    all_inorganic_stack_designed,
)
from .s2_methods import (
    device_structure_diagram,
    champion_pce_uncapped,
    champion_pce_capped,
    capped_improved_ff_and_voc,
    highest_efficiency_all_inorganic,
    giwaxs_new_reflections,
    giwaxs_surface_preferential,
    giwaxs_interfacial_nature_confirmed,
    capping_layer_thickness,
    trpl_lifetime_uncapped,
    trpl_lifetime_capped,
    stability_test_conditions,
    no_degradation_capped_35c,
    fitting_r_squared,
    two_transport_regimes,
    high_temperature_ion_dominated,
    xrd_uncapped_degradation,
    xrd_capped_no_change,
    sem_uncapped_pinholes,
    sem_capped_no_change,
    xps_iodine_increase_uncapped,
    xps_no_iodine_capped,
)
from .s3_results import (
    giwaxs_angle_dependence,
    trpl_observation,
    degradation_rate_follows_arrhenius,
    activation_energy_comparable_fast_slow,
    activation_energy_capped_higher,
    ion_migration_speculated,
    af_110c_value,
    t80_110c_capped,
    ea_ion_uncapped,
    ea_ion_capped_twice_uncapped,
    key_results_summary,
)
from .s4_discussion import (
    ion_migration_degradation_mechanism,
    capping_stabilizes_interface,
    passivation_effect,
    single_mechanism_arrhenius,
    data_collapse_universal_curve,
    stability_comparison,
    cation_exchange_challenge,
    thermal_photostability_design,
)

PRIOR_JUSTIFICATION = (
    "Well-established background fact reported across multiple sources in the PSC literature."
)

EXPERIMENTAL_OBSERVATION_JUSTIFICATION = (
    "Directly reported experimental measurement with clear protocol."
)

THEORETICAL_FRAMEWORK_JUSTIFICATION = (
    "Standard theoretical framework in PSC stability literature."
)

PRIORS = {
    # Motivation - background context
    psc_efficiency_exceeds_25: (
        0.90,
        "Well-established benchmark result widely reported in the PSC literature."
    ),
    t80_lifetime_thousand_hours: (
        0.90,
        "Widely acknowledged limitation in PSC stability literature."
    ),
    commercial_requirement_20_years: (
        0.95,
        "Industry standard lifetime requirement for commercial PV deployment."
    ),
    accelerated_aging_enables_rapid_screening: (
        0.85,
        "Standard practice in PV stability assessment."
    ),
    psc_sensitivity_challenge: (
        0.85,
        "Widely recognized challenge in PSC stability research."
    ),
    research_objective: (
        0.90,
        "Direct statement of research intent from the authors."
    ),
    inorganic_cs_pbi3_chosen: (
        0.90,
        "Explicitly stated design choice by the authors."
    ),
    capped_vs_uncapped_device_structure: (
        0.90,
        "Explicitly stated device configuration."
    ),
    all_inorganic_stack_designed: (
        0.90,
        "Explicit statement about device stack design."
    ),
    # Methods - device structure and characterization
    device_structure_diagram: (
        0.90,
        "Description of the explicitly fabricated device structure."
    ),
    champion_pce_uncapped: (
        0.88,
        "Direct experimental measurement from device characterization."
    ),
    champion_pce_capped: (
        0.88,
        "Direct experimental measurement from device characterization."
    ),
    capped_improved_ff_and_voc: (
        0.88,
        "Direct experimental measurement from device characterization."
    ),
    highest_efficiency_all_inorganic: (
        0.80,
        "Claim about relative ranking; depends on literature survey."
    ),
    giwaxs_new_reflections: (
        0.90,
        "Direct observation from GIWAXS measurement."
    ),
    giwaxs_surface_preferential: (
        0.85,
        "Inference from angle-dependent GIWAXS data."
    ),
    giwaxs_interfacial_nature_confirmed: (
        0.85,
        "Direct observation from cross-sectional SEM imaging."
    ),
    capping_layer_thickness: (
        0.85,
        "Estimated from XPS depth profiling with defined protocol."
    ),
    trpl_lifetime_uncapped: (
        0.90,
        "Direct TRPL measurement."
    ),
    trpl_lifetime_capped: (
        0.90,
        "Direct TRPL measurement."
    ),
    stability_test_conditions: (
        0.90,
        "Explicitly defined experimental conditions."
    ),
    no_degradation_capped_35c: (
        0.90,
        "Direct experimental observation over 3531 hours."
    ),
    fitting_r_squared: (
        0.85,
        "Directly computed from experimental data fitting."
    ),
    two_transport_regimes: (
        0.85,
        "Direct observation from conductivity measurements."
    ),
    high_temperature_ion_dominated: (
        0.80,
        "Standard interpretation of high-temperature transport regime in ion-conducting films."
    ),
    xrd_uncapped_degradation: (
        0.90,
        "Direct XRD measurement of aged devices."
    ),
    xrd_capped_no_change: (
        0.90,
        "Direct XRD measurement of aged devices."
    ),
    sem_uncapped_pinholes: (
        0.90,
        "Direct SEM observation of aged devices."
    ),
    sem_capped_no_change: (
        0.90,
        "Direct SEM observation of aged devices."
    ),
    xps_iodine_increase_uncapped: (
        0.90,
        "Direct XPS measurement of aged HTL surface."
    ),
    xps_no_iodine_capped: (
        0.90,
        "Direct XPS measurement of aged HTL surface."
    ),
    # Results - experimental data analysis
    giwaxs_angle_dependence: (
        0.85,
        "Direct observation from GIWAXS measurements at different angles."
    ),
    trpl_observation: (
        0.85,
        "Direct comparison of TRPL lifetimes."
    ),
    degradation_rate_follows_arrhenius: (
        0.85,
        "Direct observation from Arrhenius plot fitting."
    ),
    activation_energy_comparable_fast_slow: (
        0.80,
        "Direct result from Arrhenius analysis of k_fast and k_slow."
    ),
    activation_energy_capped_higher: (
        0.85,
        "Direct result from Arrhenius analysis comparing capped vs uncapped."
    ),
    ion_migration_speculated: (
        0.65,
        "Speculative interpretation by the authors, not direct proof."
    ),
    af_110c_value: (
        0.85,
        "Calculated from Arrhenius parameters with error bars from propagation."
    ),
    t80_110c_capped: (
        0.85,
        "Direct measurement from stability curves at 110°C."
    ),
    ea_ion_uncapped: (
        0.85,
        "Derived from temperature-dependent conductivity analysis."
    ),
    ea_ion_capped_twice_uncapped: (
        0.80,
        "Comparison of derived Ea_ion values."
    ),
    key_results_summary: (
        0.85,
        "Summary of directly measured and derived quantities."
    ),
    # Discussion - interpretations
    ion_migration_degradation_mechanism: (
        0.70,
        "Inferential claim based on multiple indirect observations (XRD, SEM, XPS)."
    ),
    capping_stabilizes_interface: (
        0.80,
        "Inferential claim based on structural characterization comparison."
    ),
    passivation_effect: (
        0.75,
        "Inference from TRPL and VOC observations."
    ),
    single_mechanism_arrhenius: (
        0.85,
        "Direct conclusion from Arrhenius linearity analysis."
    ),
    data_collapse_universal_curve: (
        0.85,
        "Direct observation from AF-corrected time plots."
    ),
    stability_comparison: (
        0.80,
        "Comparison with literature values; requires survey accuracy."
    ),
    cation_exchange_challenge: (
        0.85,
        "Well-understood limitation in the PSC capping literature."
    ),
    thermal_photostability_design: (
        0.90,
        "Explicit design rationale stated by the authors."
    ),
}