"""
Priors for independent claims in the Saliba 2016 triple cation perovskite package.

Each entry is (prior, "justification") where the justification explains
why this prior is appropriate for the claim.
"""

from .motivation import (
    efficiency_progression,
    mapbi3_never_exceeded_20percent,
    mapbi3_phase_transition,
    mapbi3_halide_segregation,
    fapi3_instability,
    cspbi3_bandgap,
    ma_crystallizer,
    yellow_phase_impurities,
    cs_ionic_radius,
    cs_effectively_promotes_black_phase,
    ma_induces_slowly,
)

from .s2_methods import (
    xrd_measurement,
    cs_addition_eliminates_impurities,
    cs_integrated_into_lattice,
    black_phase_entropically_stabilized,
    thermal_stability_test,
    cs_increases_thermal_stability,
    film_formation_no_annealing,
    film_formation_with_cs,
    processing_temperature_sensitivity,
    cs5m_monomorphic_grains,
    seed_assisted_crystal_growth,
    device_statistics,
    cs_benefits_reproducibility,
    best_stabilized_pce,
    long_term_stability,
    fill_factor_degradation,
    high_performer_stability,
    cs_ma_ratio_optimization,
)


PRIORS = {
    # Well-established background from literature (0.85-0.95)
    efficiency_progression: (
        0.90,
        "Historical efficiency progression from 3.8% to 22.1% is a well-documented fact confirmed by NREL tracking and multiple publications."
    ),
    mapbi3_never_exceeded_20percent: (
        0.92,
        "This is a well-established empirical fact confirmed across many research groups since 2009."
    ),
    mapbi3_phase_transition: (
        0.90,
        "The 55C phase transition in MAPbI3 is widely documented in the literature and can be directly measured."
    ),
    ma_crystallizer: (
        0.88,
        "The role of MA as crystallizer for FA perovskite is established in prior literature (Lee et al., Jeon et al.) and well-supported by experimental evidence."
    ),
    yellow_phase_impurities: (
        0.88,
        "Yellow phase impurities in FA perovskite are widely reported and their impact on performance is an established concern in the field."
    ),
    cs_ionic_radius: (
        0.95,
        "Ionic radii are well-established crystallographic values that can be precisely measured."
    ),
    cs_effectively_promotes_black_phase: (
        0.82,
        "Cs effectiveness in promoting black phase is supported by multiple independent reports (Li et al., Yi et al., Lee et al.) though the mechanism has some uncertainty."
    ),
    ma_induces_slowly: (
        0.80,
        "The slower crystallization rate of MA relative to Cs is supported by experimental observations of yellow phase persistence with MA-only compositions."
    ),

    # Direct experimental observations and measurements (0.65-0.85)
    fapi3_instability: (
        0.85,
        "FAPbI3 room temperature instability is well-documented, with yellow phase formation confirmed by XRD in multiple studies."
    ),
    cspbi3_bandgap: (
        0.88,
        "Band gap of 1.73 eV for CsPbI3 is a directly measurable optical property."
    ),
    xrd_measurement: (
        0.90,
        "XRD measurements are direct experimental observations with clear peaks that can be unambiguously identified."
    ),
    cs_addition_eliminates_impurities: (
        0.88,
        "Direct XRD observation showing disappearance of yellow phase and PbI2 peaks upon Cs addition - clear experimental evidence."
    ),
    cs_integrated_into_lattice: (
        0.75,
        "Lattice integration inference is well-supported by XRD shift and blue-shift in optical spectra, though the exact mechanism has some modeling uncertainty."
    ),
    black_phase_entropically_stabilized: (
        0.78,
        "Entropic stabilization explanation is theoretically sound and consistent with observed phenomena, though direct measurement is challenging."
    ),
    thermal_stability_test: (
        0.90,
        "Thermal stress test at 130C for 3 hours is a direct experimental observation with clear visual and spectroscopic evidence."
    ),
    cs_increases_thermal_stability: (
        0.82,
        "Direct comparison of Cs10M vs Cs0M under thermal stress shows clear difference; Br content contribution is well-established."
    ),
    film_formation_no_annealing: (
        0.90,
        "Direct observation of film color, absorption spectra, and XRD of as-deposited films without annealing - clear experimental evidence."
    ),
    film_formation_with_cs: (
        0.90,
        "Direct observation of black perovskite formation at room temperature with XRD confirmation - clear experimental evidence."
    ),
    processing_temperature_sensitivity: (
        0.88,
        "Direct experimental comparison at 18C vs 25C with absorption and XRD confirmation - clear temperature dependence observed."
    ),
    cs5m_monomorphic_grains: (
        0.85,
        "SEM imaging provides direct visual evidence of grain structure differences between Cs5M and Cs0M devices."
    ),
    seed_assisted_crystal_growth: (
        0.68,
        "Seed-assisted mechanism is a plausible hypothesis supported by the observation of room-temperature perovskite formation, but the precise crystallization mechanism requires more characterization."
    ),
    device_statistics: (
        0.90,
        "Statistical data from 40 control and 98 Cs-based devices across 18 batches prepared by 3 people provides robust statistical evidence."
    ),
    cs_benefits_reproducibility: (
        0.82,
        "The correlation between temperature sensitivity and batch variation is strongly supported by the 'bad batch' experiment and the large-scale statistical data."
    ),
    best_stabilized_pce: (
        0.88,
        "Maximum power point tracking measurement at 960 mV giving 21.1% is a direct experimental measurement with good agreement with JV scans."
    ),
    long_term_stability: (
        0.85,
        "250-hour aging test under operational conditions with slow half-life component of ~5000 hours provides strong stability evidence."
    ),
    fill_factor_degradation: (
        0.82,
        "Observation that current and voltage do not decrease significantly while fill factor degrades is supported by periodic JV scans during aging."
    ),
    high_performer_stability: (
        0.80,
        "Direct comparison of stability between high-performing Cs0M (16-18%) and best Cs devices shows clear difference; this is first such test on 20% devices."
    ),
    cs_ma_ratio_optimization: (
        0.78,
        "Device performance optimum with both Cs and MA present is supported by systematic variation experiments reported in ESI."
    ),

    # Tentative or method-dependent claims (0.40-0.65)
    mapbi3_halide_segregation: (
        0.65,
        "Light-induced halide segregation in MAPbBrxI(3-x) is reported in the literature but the precise conditions and mechanisms have some uncertainty."
    ),
}