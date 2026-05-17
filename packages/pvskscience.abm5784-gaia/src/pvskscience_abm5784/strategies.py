"""
Reasoning strategies for Azmi et al. 2022 paper package.

This module contains the infer strategies connecting claims with reasoning chains.
"""

from gaia.lang import (
    claim,
    setting,
    support,
    infer,
    contradiction,
)

# =============================================================================
# Claim references for use in strategies
# =============================================================================

from .motivation import (
    commercial_lifetime_requirement,
    damp_heat_test_standard,
    pscs_main_challenge,
    perovskite_instability_mechanism,
    defect_passivation_strategy,
    inverted_pscs_passivation_challenge,
    c60_weak_bonding,
    research_gap,
    proposed_solution,
    dimensionality_tailoring_key,
    room_temp_vs_thermal_annealing,
)

from .s2_methods import (
    device_structure,
    olai_post_treatment,
    two_d_rt_processing,
    giwaxs_characterization,
    hr_stem_elemental_mapping,
    pl_characterization,
    ups_energy_levels,
    contact_angle_moisture_resistance,
    sem_morphology,
    j_v_characteristics,
    pce_gain_absolute,
    energy_loss_reduction,
    trap_assisted_recombination,
    damp_heat_test_protocol,
    mppt_measurement,
    university_for_various_compositions,
    reproducibility,
)

from .s3_results import (
    giwaxs_n1_n2_peaks,
    hr_stem_n1_n2_confirmation,
    pl_n2_uniform_capping,
    ef_vbm_wider_gap_2d_rt,
    cbm_closer_to_c60_2d_rt,
    champion_pce_24_3_percent,
    pce_gain_2_percent_absolute,
    voc_1_20_v,
    ff_82_percent,
    energy_loss_0_34_ev,
    ta_lower_ff,
    narrow_statistical_distribution,
    universality_across_compositions,
    longer_recombination_lifetime,
    t95_after_1200_hours,
    pce_after_damp_heat_19_3_percent,
    structural_optical_robustness,
    mppt_95_percent_retention,
    enhanced_moisture_resistance,
    industry_standard_achieved,
    rt_vs_ta_comparison,
    passivation_vs_control,
)

from .s4_discussion import (
    main_achievement,
    key_innovation,
    dual_function_passivation,
    trap_state_passivation,
    moisture_oxygen_barrier,
    energy_level_match_critical,
    n_type_enhancement,
    regular_vs_inverted_pscs,
    c60_passivation_insufficient,
    scalability_advantage,
    universality_of_method,
    reproducibility_practical,
    thermal_stability_at_elevated_temps,
    robustness_after_thermal_aging,
    commercial_relevance,
    iecs_standard_met,
)

# =============================================================================
# Strategies connecting motivation to the problem
# =============================================================================

strat_psc_instability = support(
    [perovskite_instability_mechanism, defect_passivation_strategy],
    inverted_pscs_passivation_challenge,
    reason=(
        "The instability mechanisms in 3D perovskites (high defect densities and ion migration) "
        "are well-documented, and growing 2D perovskite layers on 3D surfaces creates heterojunctions "
        "that can passivate defects and suppress ion migration. However, despite this knowledge, "
        "top-contact passivation at the electron-selective interface of inverted PSCs has consistently "
        "failed, indicating a persistent unsolved challenge in the field (@perovskite_instability_mechanism, "
        "@defect_passivation_strategy, @inverted_pscs_passivation_challenge)."
    ),
    prior=0.5,
)

strat_c60_limitation = support(
    [c60_weak_bonding, research_gap],
    proposed_solution,
    reason=(
        "C60 is only weakly bonded to perovskite layers, causing high energetic disorder and insufficient "
        "protection against moisture/oxygen ingress. The electron-selective interface has been understudied "
        "because C60 was assumed to provide sufficient passivation. These limitations of C60 create a clear "
        "motivation for implementing 2D perovskite passivation layers formed with OLAI molecules, which can "
        "address all these issues simultaneously (@c60_weak_bonding, @research_gap)."
    ),
    prior=0.5,
)

strat_rt_produces_higher_n = support(
    [dimensionality_tailoring_key, room_temp_vs_thermal_annealing],
    proposed_solution,
    reason=(
        "The dimensionality of 2D perovskite fragments is key to enabling efficient passivation, "
        "with higher-n layers having lower formation energy. Room-temperature processing with OLAI "
        "produces higher-dimensionality layers (n >= 2) more effectively than thermal annealing which "
        "yields only n=1. This tailoring approach directly supports the proposed solution of using "
        "2D-RT processing for better passivation performance (@dimensionality_tailoring_key, "
        "@room_temp_vs_thermal_annealing)."
    ),
    prior=0.5,
)

# =============================================================================
# Strategies connecting characterization to results
# =============================================================================

strat_giwaxs_confirms_n2 = support(
    [giwaxs_characterization],
    giwaxs_n1_n2_peaks,
    reason=(
        "GIWAXS characterization showed diffraction peaks at qz approximately 0.2 to 0.5 Angstrom^-1 "
        "corresponding to (001) and (002) planes of 2D perovskite crystals. 2D-TA films were dominated "
        "by n=1 (peak at qz approximately 0.35 Angstrom^-1), while 2D-RT films showed both n=1 and n=2 "
        "peaks with substantial n=2 at lower qz. These quantitative diffraction results directly confirm "
        "the presence of both n=1 and n=2 layers in 2D-RT samples (@giwaxs_characterization)."
    ),
    prior=0.5,
)

strat_stem_confirms_n2 = support(
    [hr_stem_elemental_mapping],
    hr_stem_n1_n2_confirmation,
    reason=(
        "Cross-sectional HR-STEM images and HAADF/EDS elemental mapping differentiated between n=1 "
        "and n=2 layers in 2D-RT samples (vs only n=1 in 2D-TA). Elemental mapping showed reduction "
        "in C, Pb, and I densities corresponding to both n=1 and n=2 layers. Interlayer distances "
        "measured as approximately 1.2 nm for n=1 and approximately 1.5 nm for n=2 directly confirm "
        "the existence of n=2 layers in 2D-RT samples (@hr_stem_elemental_mapping)."
    ),
    prior=0.5,
)

strat_pl_confirms_uniform_n2 = support(
    [pl_characterization],
    pl_n2_uniform_capping,
    reason=(
        "PL imaging at approximately 570 nm corresponding to n=2 showed uniform capping layer "
        "formation on 3D perovskite surfaces for 2D-RT samples. PL spectra confirmed n=1 dominance "
        "in 2D-TA and more pronounced n=2 emission in 2D-RT, consistent with GIWAXS and TEM results. "
        "This optical characterization confirms uniform n=2 formation in 2D-RT samples "
        "(@pl_characterization)."
    ),
    prior=0.5,
)

# =============================================================================
# Strategies connecting energy levels to device performance
# =============================================================================

strat_energy_levels_support_performance = support(
    [ups_energy_levels, ef_vbm_wider_gap_2d_rt, cbm_closer_to_c60_2d_rt],
    champion_pce_24_3_percent,
    reason=(
        "UPS measurements showed that OLAI post-treatment widened the energetic gap between EF and VBM, "
        "indicating enhanced n-type character. The CBM of 2D-RT films was closer to CBM of C60, enabling "
        "more efficient charge transfer at the 2D/3D perovskite interface. These favorable energy level "
        "alignments directly support the high device performance (24.3% PCE, 1.20V VOC, 82% FF) observed "
        "in 2D-RT devices (@ups_energy_levels, @ef_vbm_wider_gap_2d_rt, @cbm_closer_to_c60_2d_rt)."
    ),
    prior=0.5,
)

strat_2d_ta_energy_mismatch = support(
    [ups_energy_levels, cbm_closer_to_c60_2d_rt],
    ta_lower_ff,
    reason=(
        "UPS results showed that C60 bonding is weak and 2D-TA films have CBM much higher than C60 "
        "with less n-type character. This energy level mismatch at the electron-selective contact "
        "directly explains the lower FF values (<79%) observed in 2D-TA devices compared to 2D-RT "
        "devices. The correlation between energy level alignment and FF provides clear evidence for "
        "this mechanism (@ups_energy_levels, @cbm_closer_to_c60_2d_rt)."
    ),
    prior=0.5,
)

# =============================================================================
# Strategies for device performance results
# =============================================================================

strat_pce_improvement = support(
    [j_v_characteristics, pce_gain_absolute, voc_1_20_v, ff_82_percent],
    champion_pce_24_3_percent,
    reason=(
        "J-V characteristics directly measured the 2D-RT device performance: maximum PCE of 24.3%, "
        "stabilized PCE approximately 24%, VOC approximately 1.20V, and FF approximately 82%. These "
        "specific values from direct electrical measurements establish the champion device performance "
        "(@j_v_characteristics, @pce_gain_absolute, @voc_1_20_v, @ff_82_percent)."
    ),
    prior=0.5,
)

strat_absolute_pce_gain = support(
    [champion_pce_24_3_percent, passivation_vs_control],
    pce_gain_2_percent_absolute,
    reason=(
        "The 2D-RT devices achieved maximum PCE of 24.3% compared to control devices at approximately "
        "22%, representing an absolute approximately 2% PCE gain. This gain was confirmed across "
        "measurements and compares favorably with PCEs for other inverted PSCs reported in literature "
        "(@champion_pce_24_3_percent, @passivation_vs_control)."
    ),
    prior=0.5,
)

strat_energy_loss_optimization = support(
    [voc_1_20_v, energy_loss_reduction],
    energy_loss_0_34_ev,
    reason=(
        "With VOC of approximately 1.20V and optical bandgap (Eg) of 1.55 eV, the device energy loss "
        "Eloss = Eg - qVOC = 1.55 eV - 1.20 eV = 0.35 eV (reported as 0.34 eV). This represents "
        "approximately 96% of the thermodynamic limit of VOC (1.262 V), comparable to GaAs solar "
        "cells achieving approximately 98% of thermodynamic limit. The calculated energy loss directly "
        "supports this high-efficiency achievement (@voc_1_20_v, @energy_loss_reduction)."
    ),
    prior=0.5,
)

strat_trap_recombination_reduced = support(
    [trap_assisted_recombination, longer_recombination_lifetime],
    trap_state_passivation,
    reason=(
        "Transient photovoltage decay and light intensity-dependent measurements showed that 2D-passivated "
        "devices exhibited longer charge recombination lifetime and lower ideality factor than control "
        "devices. This directly confirms reduced trap-assisted recombination at 3D/C60 interfaces, "
        "which is a key mechanism of the 2D perovskite passivation effect (@trap_assisted_recombination, "
        "@longer_recombination_lifetime)."
    ),
    prior=0.5,
)

# =============================================================================
# Strategies connecting processing conditions to n-dimensionality
# =============================================================================

strat_rt_vs_ta_comparison = support(
    [two_d_rt_processing, giwaxs_n1_n2_peaks, hr_stem_n1_n2_confirmation, pl_n2_uniform_capping],
    rt_vs_ta_comparison,
    reason=(
        "2D-RT processing with OLAI molecules produces higher-dimensionality layers (n >= 2) more "
        "effectively than 2D-TA at 100C which is dominated by n=1. Multiple characterization techniques "
        "confirm this: GIWAXS shows n=2 peaks in 2D-RT but not 2D-TA; HR-STEM shows interlayer distances "
        "of 1.5nm (n=2) and 1.2nm (n=1) in 2D-RT but only 1.2nm in 2D-TA; PL shows uniform n=2 emission "
        "at 570nm for 2D-RT. This leads to better energy level alignment with C60 and higher device "
        "performance in 2D-RT vs poor alignment and lower FF in 2D-TA (@two_d_rt_processing, "
        "@giwaxs_n1_n2_peaks, @hr_stem_n1_n2_confirmation, @pl_n2_uniform_capping)."
    ),
    prior=0.5,
)

# =============================================================================
# Strategies for stability results
# =============================================================================

strat_damp_heat_stability = support(
    [damp_heat_test_protocol, t95_after_1200_hours, pce_after_damp_heat_19_3_percent],
    industry_standard_achieved,
    reason=(
        "The damp-heat test protocol followed IEC 61215:2016 at 85C and 85% RH. Champion stability "
        "cells retained more than 95% of initial PCE (T95) after more than 1200 hours, and three "
        "devices showed average PCE of 19.3 +/- 0.69% after the test. These direct measurements under "
        "standardized conditions demonstrate that the encapsulated PSCs successfully pass the industry-"
        "relevant damp-heat test per IEC protocols (@damp_heat_test_protocol, @t95_after_1200_hours, "
        "@pce_after_damp_heat_19_3_percent)."
    ),
    prior=0.5,
)

strat_mppt_stability = support(
    [mppt_measurement, mppt_95_percent_retention],
    thermal_stability_at_elevated_temps,
    reason=(
        "MPPT measurements under simulated 1-sun illumination (AM 1.5) in ambient air for more than "
        "500 hours showed that 2D-RT-based devices retained approximately 95% of initial PCE, while "
        "control devices retained less than 90% for only approximately 100 hours. This sustained "
        "performance under continuous illumination confirms the thermal stability of 2D-passivated "
        "devices at elevated temperatures (@mppt_measurement, @mppt_95_percent_retention)."
    ),
    prior=0.5,
)

strat_robustness_after_aging = support(
    [structural_optical_robustness, mppt_95_percent_retention],
    robustness_after_thermal_aging,
    reason=(
        "There was no substantial change in structural and optical properties of 2D perovskite "
        "passivation films after more than 500 hours at 85C under dark conditions, and MPPT testing "
        "showed approximately 95% retention after more than 500 hours under illumination. Together, "
        "these results confirm the thermal robustness of the 2D perovskite structure and its "
        "suitability for long-term stability applications (@structural_optical_robustness, "
        "@mppt_95_percent_retention)."
    ),
    prior=0.5,
)

# =============================================================================
# Strategies for mechanism discussion
# =============================================================================

strat_dual_passivation_mechanism = support(
    [trap_state_passivation, moisture_oxygen_barrier, enhanced_moisture_resistance],
    dual_function_passivation,
    reason=(
        "The 2D perovskite passivation serves dual functions based on multiple experimental "
        "observations: (1) trap state passivation evidenced by stronger PL emission, longer PL "
        "lifetime, reduced trap-assisted recombination, and lower ideality factor; (2) moisture/"
        "oxygen barrier function evidenced by contact angle measurements showing enhanced resilience "
        "and successful damp-heat test performance at 85C/85% RH. These simultaneous mechanisms "
        "enable the excellent stability observed in 2D-RT devices (@trap_state_passivation, "
        "@moisture_oxygen_barrier, @enhanced_moisture_resistance)."
    ),
    prior=0.5,
)

strat_energy_level_match = support(
    [cbm_closer_to_c60_2d_rt, ff_82_percent, ta_lower_ff],
    energy_level_match_critical,
    reason=(
        "The CBM of 2D-RT films is closer to the CBM of C60, enabling more efficient charge "
        "transfer at the 2D/3D interface. This favorable alignment yields high FF of 82% in "
        "2D-RT devices. In contrast, 2D-TA films have CBM much higher than C60, causing energy "
        "level mismatch and lower FF (<79%). The correlation between energy level positions and "
        "FF values directly supports that energy level alignment is critical for device performance "
        "(@cbm_closer_to_c60_2d_rt, @ff_82_percent, @ta_lower_ff)."
    ),
    prior=0.5,
)

strat_n_type_enhancement = support(
    [ef_vbm_wider_gap_2d_rt, voc_1_20_v],
    n_type_enhancement,
    reason=(
        "The wider energetic gap between Fermi level (EF) and VBM in 2D-RT samples indicates "
        "enhanced n-type character of post-treated 3D perovskite films. This enhanced n-type "
        "character contributes to better charge extraction, as evidenced by the high VOC of "
        "1.20V representing approximately 96% of thermodynamic limit. The correlation between "
        "n-type enhancement and VOC supports this mechanism (@ef_vbm_wider_gap_2d_rt, @voc_1_20_v)."
    ),
    prior=0.5,
)

# =============================================================================
# Strategies for broader implications
# =============================================================================

strat_universality = support(
    [universality_across_compositions],
    universality_of_method,
    reason=(
        "The 2D-RT passivation approach was demonstrated to be universal across various perovskite "
        "compositions (different bandgaps) and deposition techniques (one-step, two-step, blade-"
        "coating), with systematic absolute PCE enhancement of 1.5 to 2.0% across all conditions. "
        "This broad applicability supports the universality claim for the passivation method "
        "(@universality_across_compositions)."
    ),
    prior=0.5,
)

strat_reproducibility_validates = support(
    [narrow_statistical_distribution, reproducibility],
    reproducibility_practical,
    reason=(
        "The narrow statistical distribution of PCE, VOC, FF, and JSC values confirmed high "
        "reproducibility, with less than 0.5% deviation for person-to-person variations among "
        "seven different researchers. This quantified reproducibility data across many devices "
        "and researchers demonstrates the practical viability of the approach for scalable "
        "manufacturing (@narrow_statistical_distribution, @reproducibility)."
    ),
    prior=0.5,
)

strat_commercial_relevance = support(
    [champion_pce_24_3_percent, t95_after_1200_hours, industry_standard_achieved, pce_after_damp_heat_19_3_percent],
    commercial_relevance,
    reason=(
        "The commercial relevance of this work combines three key achievements: (1) high efficiency "
        "with 24.3% PCE and approximately 2% absolute gain over control; (2) excellent long-term "
        "stability with >95% retention after >1200 hours under damp-heat conditions; (3) meeting "
        " IEC 61215:2016 industrial stability standard with 19.3% PCE retained after >1000 hours. "
        "These results directly address the two main hurdles (efficiency and lifetime) preventing "
        "PSCs from entering the commercial PV market (@champion_pce_24_3_percent, @t95_after_1200_hours, "
        "@industry_standard_achieved, @pce_after_damp_heat_19_3_percent)."
    ),
    prior=0.5,
)

strat_iec_standard = support(
    [damp_heat_test_protocol, t95_after_1200_hours, pce_after_damp_heat_19_3_percent],
    iecs_standard_met,
    reason=(
        "The encapsulated 2D-RT PSCs successfully passed the IEC 61215:2016 damp-heat test protocol "
        "at 85C and 85% RH, which is the standard for commercial PV module stability. The devices "
        "retained more than 95% of initial PCE (T95) after more than 1200 hours, with an average PCE "
        "of 19.3 +/- 0.69% after the test. This represents a very high retained PCE meeting one of the "
        "critical industrial stability standards for PV modules (@damp_heat_test_protocol, "
        "@t95_after_1200_hours, @pce_after_damp_heat_19_3_percent)."
    ),
    prior=0.5,
)

# =============================================================================
# Key innovation strategy
# =============================================================================

strat_key_innovation = support(
    [dimensionality_tailoring_key, room_temp_vs_thermal_annealing, rt_vs_ta_comparison,
     energy_level_match_critical, champion_pce_24_3_percent],
    key_innovation,
    reason=(
        "The key innovation is tailoring the dimensionality (n) of 2D perovskite fragments at the "
        "electron-selective interface using room-temperature (2D-RT) processing, which produces "
        "higher n layers (n >= 2) with lower formation energy. This contrasts with thermal annealing "
        "(2D-TA) which yields only n=1 layers. Higher n in 2D-RT enables better energy level alignment "
        "with C60 (CBM closer to C60), resulting in higher device performance (24.3% PCE, 82% FF) "
        "compared to 2D-TA (lower FF <79%). The systematic comparison between RT and TA processing, "
        "combined with GIWAXS and HR-STEM confirmation of n values, demonstrates that dimensionality "
        "tailoring at the electron-selective interface is the essential enabling factor for successful "
        "passivation in inverted PSCs (@dimensionality_tailoring_key, @room_temp_vs_thermal_annealing, "
        "@rt_vs_ta_comparison, @energy_level_match_critical, @champion_pce_24_3_percent)."
    ),
    prior=0.5,
)

# =============================================================================
# Main achievement strategy
# =============================================================================

strat_main_achievement = support(
    [key_innovation, champion_pce_24_3_percent, pce_gain_2_percent_absolute,
     t95_after_1200_hours, iecs_standard_met, dual_function_passivation],
    main_achievement,
    reason=(
        "The main achievement combines multiple key results from the paper: (1) high PCE of 24.3% "
        "with approximately 2% absolute gain via 2D-RT passivation; (2) excellent damp-heat stability "
        "with >95% retention after >1200 hours, meeting IEC 61215:2016 standard; (3) key innovation "
        "of tailoring dimensionality (n) at electron-selective interface with room-temperature "
        "processing to produce higher n layers (n >= 2); (4) dual-function passivation mechanism "
        "providing both defect passivation and moisture/oxygen barrier protection. These results "
        "represent a significant advance toward PSC commercialization by simultaneously achieving "
        "high efficiency and long-term operational stability under industry-standard test conditions "
        "(@key_innovation, @champion_pce_24_3_percent, @pce_gain_2_percent_absolute, "
        "@t95_after_1200_hours, @iecs_standard_met, @dual_function_passivation)."
    ),
    prior=0.5,
)