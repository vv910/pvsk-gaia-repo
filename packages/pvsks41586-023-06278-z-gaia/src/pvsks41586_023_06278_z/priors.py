"""
Prior probability assignments for independent claims.

This module assigns priors to leaf claims (independent premises) based on
evidence strength and source reliability.
"""

from .motivation import (
    tandem_configuration,
    performance_potential,
    previous_limitation,
    two_d_three_d_problem,
    surface_passivation_tradeoff,
    phj_solution,
    type_two_band_alignment,
    bilateral_improvement,
    hybrid_deposition_method,
    ion_immiscibility,
    nbg_champion_pce,
    nbg_average_improvement,
)

from .s2_methods import (
    device_architecture,
    fl_wbg_composition,
    nbg_composition,
    inorganic_layer_deposition,
    organic_salt_deposition,
    peai_post_treatment,
    morphology_method,
    heterojunction_verification,
    phj_layer_thickness,
    ion_distribution_stability,
    work_functions,
    bandgaps,
    jv_measurement,
    eqe_measurement,
)

from .s3_results import (
    control_vs_phj_comparison,
    device_statistics,
    champion_device,
    eqe_validation,
    pl_intensity_increase,
    trapped_reduction,
    built_in_potential,
    el_qy_comparison,
    voc_loss_reduction,
    trpl_phj_film,
    trpl_control_film,
    electron_transfer_rate,
    control_ta_spectrum,
    phj_ta_nbg_pumped,
    phj_ta_fl_wbg_pumped,
    wbg_subcell_performance,
    nbg_subcell_in_tandem,
    tandem_ff_improvement,
    tandem_champion,
    eqe_tandem,
    certified_efficiency,
    large_area_tandem,
    operational_stability,
    degradation_mechanism,
    reverse_bias_stability,
    simulation_model,
    dil_trap_density_effect,
    dil_thickness_effect,
    simulated_improvement,
)

from .s4_discussion import (
    type_ii_mechanism,
    depletion_region,
    charge_separation,
    electron_extraction_acceleration,
    two_d_layer_limitation,
    three_d_advantage,
    remaining_voc_ff_loss,
    optical_losses,
    future_improvement_path,
    long_term_stability,
    thermal_stability_note,
    bromide_migration,
    record_efficiency,
    bilateral_voc_ff,
    solution_processadvantage,
)

PRIORS = {
    tandem_configuration: (
        0.9,
        "Established device configuration for all-perovskite tandem solar cells."
    ),
    performance_potential: (
        0.9,
        "Well-understood photovoltaic principle for tandem cells."
    ),
    previous_limitation: (
        0.9,
        "Directly reported performance limitations from previous record devices."
    ),
    two_d_three_d_problem: (
        0.9,
        "Directly reported transport limitation of 2D layers in PSCs."
    ),
    surface_passivation_tradeoff: (
        0.85,
        "Reported trade-off between passivation and conductivity in heterojunctions."
    ),
    phj_solution: (
        0.85,
        "Proposed solution that was experimentally validated."
    ),
    type_two_band_alignment: (
        0.9,
        "Directly measured by UV photoemission spectroscopy and calculated from bandgaps."
    ),
    bilateral_improvement: (
        0.9,
        "Direct experimental measurement showing simultaneous Voc and FF improvement."
    ),
    hybrid_deposition_method: (
        0.88,
        "Reported non-destructive deposition method with experimental verification."
    ),
    ion_immiscibility: (
        0.88,
        "Supported by ToF-SIMS and EDX observations showing no Sn2+ diffusion."
    ),
    nbg_champion_pce: (
        0.9,
        "Direct J-V measurement of champion device with detailed parameters."
    ),
    nbg_average_improvement: (
        0.88,
        "Statistical comparison from 26 control and 26 PHJ devices."
    ),
    device_architecture: (
        0.95,
        "Standard PSC architecture with well-defined layers."
    ),
    fl_wbg_composition: (
        0.92,
        "Optimized composition based on systematic variation studies."
    ),
    nbg_composition: (
        0.92,
        "Standard mixed Pb-Sn perovskite composition with SnF2 addition."
    ),
    inorganic_layer_deposition: (
        0.88,
        "Reported evaporation parameters with thickness calibration."
    ),
    organic_salt_deposition: (
        0.88,
        "Standard spin-coating process with washing step."
    ),
    peai_post_treatment: (
        0.85,
        "Slightly improves performance but effect is minor."
    ),
    morphology_method: (
        0.9,
        "Standard SEM and XRD characterization."
    ),
    heterojunction_verification: (
        0.9,
        "Multiple complementary techniques (HR-STEM, EDX, ToF-SIMS)."
    ),
    phj_layer_thickness: (
        0.88,
        "Direct EDX and ToF-SIMS measurement of layer thickness."
    ),
    ion_distribution_stability: (
        0.88,
        "60-day stability study with EDX and ToF-SIMS verification."
    ),
    work_functions: (
        0.92,
        "Direct UPS measurement with reported precision."
    ),
    bandgaps: (
        0.92,
        "Direct optical measurement with standard technique."
    ),
    jv_measurement: (
        0.92,
        "Standard J-V measurement with proper calibration."
    ),
    eqe_measurement: (
        0.92,
        "Standard EQE measurement with spectral mismatch consideration."
    ),
    control_vs_phj_comparison: (
        0.88,
        "Direct comparison from 26 devices per type over identical runs."
    ),
    device_statistics: (
        0.88,
        "148 devices, good reproducibility shown."
    ),
    champion_device: (
        0.9,
        "Direct J-V measurement of champion device."
    ),
    eqe_validation: (
        0.9,
        "EQE integrated Jsc matches J-V measurement within tolerance."
    ),
    pl_intensity_increase: (
        0.88,
        "Direct PL measurement showing increased intensity."
    ),
    trapped_reduction: (
        0.85,
        "Multiple measurements (SCLC, dark current, ideality factor) confirm reduction."
    ),
    built_in_potential: (
        0.88,
        "Direct Mott-Schottky analysis."
    ),
    el_qy_comparison: (
        0.88,
        "Direct EL measurement with calculated Voc loss."
    ),
    voc_loss_reduction: (
        0.88,
        "Directly measured from EL quantum yield comparison."
    ),
    trpl_phj_film: (
        0.88,
        "Direct TRPL measurement with biexponential fit."
    ),
    trpl_control_film: (
        0.88,
        "Direct TRPL measurement with biexponential fit."
    ),
    electron_transfer_rate: (
        0.85,
        "Derived from differential lifetime analysis."
    ),
    control_ta_spectrum: (
        0.88,
        "Direct TA measurement showing single peak."
    ),
    phj_ta_nbg_pumped: (
        0.88,
        "Direct TA measurement with time-resolved observation."
    ),
    phj_ta_fl_wbg_pumped: (
        0.88,
        "Direct TA measurement confirming no back-transfer."
    ),
    wbg_subcell_performance: (
        0.9,
        "Direct J-V measurement of WBG subcell."
    ),
    nbg_subcell_in_tandem: (
        0.88,
        "Subcell performance in tandem configuration."
    ),
    tandem_ff_improvement: (
        0.88,
        "Direct comparison from 26 devices per type."
    ),
    tandem_champion: (
        0.9,
        "Direct J-V measurement of champion tandem device."
    ),
    eqe_tandem: (
        0.9,
        "EQE confirms current matching between subcells."
    ),
    certified_efficiency: (
        0.95,
        "Certified by JET, an accredited independent PV calibration laboratory."
    ),
    large_area_tandem: (
        0.85,
        "1.05 cm^2 large-area device measured."
    ),
    operational_stability: (
        0.88,
        "600-hour MPP tracking with encapsulation."
    ),
    degradation_mechanism: (
        0.8,
        "Attributed to Au migration based on Supplementary Fig. 46."
    ),
    reverse_bias_stability: (
        0.85,
        "Compared with single-junction PSCs under reverse bias."
    ),
    simulation_model: (
        0.82,
        "SCAPS-1D simulation with reasonable parameters."
    ),
    dil_trap_density_effect: (
        0.85,
        "Simulation shows differential sensitivity between control and PHJ."
    ),
    dil_thickness_effect: (
        0.85,
        "Simulation shows PHJ is insensitive to DIL thickness."
    ),
    simulated_improvement: (
        0.82,
        "Simulation prediction with DIL parameters from experimental conditions."
    ),
    type_ii_mechanism: (
        0.88,
        "Mechanism explanation consistent with energy band diagrams."
    ),
    depletion_region: (
        0.85,
        "Derived from Mott-Schottky analysis."
    ),
    charge_separation: (
        0.88,
        "Consistent with TRPL fast decay component assignment."
    ),
    electron_extraction_acceleration: (
        0.85,
        "Consistent with differential lifetime measurements."
    ),
    two_d_layer_limitation: (
        0.9,
        "Known limitation of 2D/3D heterojunctions in literature."
    ),
    three_d_advantage: (
        0.88,
        "PHJ achieves both passivation and transport as demonstrated."
    ),
    remaining_voc_ff_loss: (
        0.85,
        "Comparison with Shockley-Queisser limit shows remaining losses."
    ),
    optical_losses: (
        0.85,
        "Analysis of reflection, parasitic absorption, and insufficient absorption."
    ),
    future_improvement_path: (
        0.8,
        "Proposed pathway to 30% with reasonable estimates."
    ),
    long_term_stability: (
        0.88,
        "3000-hour aging study with no degradation observed."
    ),
    thermal_stability_note: (
        0.82,
        "Literature-supported methods for improvement."
    ),
    bromide_migration: (
        0.88,
        "Direct ToF-SIMS observation of Br- diffusion."
    ),
    record_efficiency: (
        0.95,
        "Certified record efficiency of 28.0% by JET."
    ),
    bilateral_voc_ff: (
        0.9,
        "Direct experimental demonstration."
    ),
    solution_processadvantage: (
        0.88,
        "Demonstrated non-destructive hybrid method."
    ),
}