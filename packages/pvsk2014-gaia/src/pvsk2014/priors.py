"""
Priors for pvsk2014-gaia package.

All independent (leaf) claims that are not derived from any strategy
need priors assigned here.
"""

from .motivation import (
    sequential_deposition_benchmark,
    vacuum_deposition_benchmark,
    spin_coating_problem,
    uniformity_limitation,
    mixed_solvent_solution,
    perovskite_composition,
)

from .s2_methods import (
    crystallinity_preserved,
    dense_grained_morphology,
    dmso_retards_reaction,
    elemental_analysis_confirms,
    ftir_confirmation,
    intermediate_phase_formation,
    intermediate_phase_rms_roughness,
    low_angle_xrd_peaks,
    mixed_solvent_outcome,
    perovskite_conversion_temperature,
    perovskite_film_rms_roughness,
    pure_gbl_outcome,
    solvent_engineering_process,
    without_toluene_outcome,
)

from .s3_results import (
    average_bilayer_efficiency,
    bilayer_forward_scan,
    bilayer_reverse_scan,
    certified_efficiency_162,
    hysteresis_origin,
    ipce_plateau,
    jsc_from_ipce,
    large_hysteresis_without_mp,
    negligible_hysteresis_bilayer,
    no_mp_tio2_forward_scan,
    no_mp_tio2_reverse_scan,
    reproducibility_histogram,
    thickness_vs_efficiency,
    delay_time_effect,
)

from .s4_discussion import (
    formation_mechanism,
    mp_tio2_necessity,
    role_of_dmso,
    role_of_toluene,
)

PRIORS = {
    # motivation - prior art benchmarks (well-established in literature)
    sequential_deposition_benchmark: (
        0.85,
        "Directly reported experimental measurement from Burschka2013 paper, widely cited benchmark."
    ),
    vacuum_deposition_benchmark: (
        0.85,
        "Directly reported experimental measurement from Liu2013 paper, widely cited benchmark."
    ),
    # motivation - problem statement (directly reported observations)
    spin_coating_problem: (
        0.85,
        "Directly reported experimental observation with clear Eperon2014 reference."
    ),
    uniformity_limitation: (
        0.85,
        "Directly reported experimental observation with clear Eperon2014 reference."
    ),
    mixed_solvent_solution: (
        0.85,
        "Core method described in this paper - key contribution claim."
    ),
    # s2_methods - experimental observations
    crystallinity_preserved: (
        0.85,
        "Directly measured XRD data reported in paper."
    ),
    dense_grained_morphology: (
        0.85,
        "Directly observed via SEM reported in paper."
    ),
    dmso_retards_reaction: (
        0.80,
        "Mechanistic interpretation supported by intermediate phase observations."
    ),
    elemental_analysis_confirms: (
        0.85,
        "Directly measured elemental analysis data reported in paper."
    ),
    ftir_confirmation: (
        0.85,
        "Directly measured FTIR spectrum reported in paper."
    ),
    intermediate_phase_formation: (
        0.85,
        "Directly observed via XRD when toluene is introduced onto wet film."
    ),
    intermediate_phase_rms_roughness: (
        0.85,
        "Directly measured AFM data reported in paper."
    ),
    low_angle_xrd_peaks: (
        0.85,
        "Directly measured XRD data reported in paper."
    ),
    mixed_solvent_outcome: (
        0.85,
        "Directly observed experimental outcome reported in paper."
    ),
    perovskite_conversion_temperature: (
        0.85,
        "Directly measured in situ high-temperature XRD data reported in paper."
    ),
    perovskite_film_rms_roughness: (
        0.85,
        "Directly measured AFM data reported in paper."
    ),
    # s3_results - J-V measurements (directly reported experimental data)
    average_bilayer_efficiency: (
        0.85,
        "Directly measured J-V characteristics from 12 devices averaged in paper."
    ),
    bilayer_forward_scan: (
        0.85,
        "Directly measured J-V curve data reported in paper Table 1."
    ),
    bilayer_reverse_scan: (
        0.85,
        "Directly measured J-V curve data reported in paper Table 1."
    ),
    certified_efficiency_162: (
        0.90,
        "Certified by independent photovoltaics calibration laboratory - highest confidence."
    ),
    hysteresis_origin: (
        0.75,
        "Proposed explanation for hysteresis consistent with observations, not directly proven."
    ),
    ipce_plateau: (
        0.85,
        "Directly measured IPCE spectrum reported in paper."
    ),
    jsc_from_ipce: (
        0.85,
        "Derived from IPCE integration - standard measurement technique."
    ),
    large_hysteresis_without_mp: (
        0.85,
        "Directly measured J-V curves showing 9.1% efficiency discrepancy."
    ),
    negligible_hysteresis_bilayer: (
        0.85,
        "Directly measured J-V curves from bilayer cells showing coincident forward/reverse scans."
    ),
    no_mp_tio2_forward_scan: (
        0.85,
        "Directly measured J-V curve data reported in paper Table 1."
    ),
    no_mp_tio2_reverse_scan: (
        0.85,
        "Directly measured J-V curve data reported in paper Table 1."
    ),
    reproducibility_histogram: (
        0.85,
        "Statistical data from 108 independently fabricated devices."
    ),
    thickness_vs_efficiency: (
        0.85,
        "Directly measured data from 12 cells per thickness point."
    ),
    delay_time_effect: (
        0.85,
        "Directly measured J-V characteristics at multiple delay times."
    ),
    perovskite_composition: (
        0.85,
        "Material composition used in this study as described in paper."
    ),
    pure_gbl_outcome: (
        0.85,
        "Directly observed experimental outcome reported in paper Supplementary Fig. 1."
    ),
    solvent_engineering_process: (
        0.85,
        "Five-step process described in paper - core methodological contribution."
    ),
    without_toluene_outcome: (
        0.85,
        "Directly observed experimental outcome reported in paper Supplementary Fig. 1."
    ),
    # s4_discussion - mechanistic interpretations
    formation_mechanism: (
        0.80,
        "Proposed mechanism consistent with all observations but not directly proven."
    ),
    mp_tio2_necessity: (
        0.80,
        "Conclusion drawn from thickness optimization experiment data."
    ),
    role_of_dmso: (
        0.80,
        "Mechanistic interpretation consistent with experimental observations."
    ),
    role_of_toluene: (
        0.85,
        "Role confirmed by contrast between with/without toluene drip experiments."
    ),
}