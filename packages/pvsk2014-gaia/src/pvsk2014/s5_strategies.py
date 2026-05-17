"""
Pass 2: Connect reasoning with draft strategies.

This module adds strategies connecting claims to form the paper's reasoning chain.
Uses `infer` as draft strategy type (to be refined in Pass 4).
"""

from gaia.lang import (
    support,
    claim,
)

from .motivation import (
    perovskite_optical_properties,
    perovskite_ambipolar_transport,
    perovskite_long_diffusion_lengths,
    sequential_deposition_benchmark,
    vacuum_deposition_benchmark,
    spin_coating_problem,
    uniformity_limitation,
    bilayer_architecture,
    perovskite_composition,
    mixed_solvent_solution,
    certified_efficiency,
)

from .s2_methods import (
    intermediate_phase_formation,
    dmso_retards_reaction,
    mixed_solvent_outcome,
    without_toluene_outcome,
    pure_gbl_outcome,
    crystallinity_preserved,
    intermediate_phase_identity,
    elemental_analysis_confirms,
    low_angle_xrd_peaks,
    ftir_confirmation,
    perovskite_conversion_temperature,
    full_surface_coverage,
    dense_grained_morphology,
    intermediate_phase_rms_roughness,
    perovskite_film_rms_roughness,
)

from .s3_results import (
    no_mp_tio2_forward_scan,
    no_mp_tio2_reverse_scan,
    large_hysteresis_without_mp,
    bilayer_forward_scan,
    bilayer_reverse_scan,
    negligible_hysteresis_bilayer,
    average_bilayer_efficiency,
    best_cell_average,
    ipce_plateau,
    jsc_from_ipce,
    reproducibility_histogram,
    certified_efficiency_162,
    thickness_vs_efficiency,
    hysteresis_origin,
    balanced_thickness_concept,
)

from .s4_discussion import (
    formation_mechanism,
    intermediate_phase_critical,
    role_of_dmso,
    role_of_toluene,
    solid_state_conversion,
    bilayer_advantages,
    mp_tio2_necessity,
    solvent_engineering_contribution,
    intercalation_strategy,
    key_achievement,
)

# --- Strategy: intermediate phase explains uniformity ---

strat_intermediate_phase_uniformity = support(
    [mixed_solvent_outcome, intermediate_phase_formation, dmso_retards_reaction],
    full_surface_coverage,
    reason=(
        "The mixed solvent with toluene drip leads to intermediate phase formation (@intermediate_phase_formation), "
        "which enables uniform film formation (@mixed_solvent_outcome). "
        "The DMSO coordination with Pb2+ retards rapid reaction (@dmso_retards_reaction), preventing premature crystallization "
        "and enabling 100% surface coverage (@full_surface_coverage)."
    ),
    prior=0.5,
)

# --- Strategy: intermediate phase identity confirmed ---

strat_xrd_identity = support(
    [low_angle_xrd_peaks, elemental_analysis_confirms, ftir_confirmation],
    intermediate_phase_identity,
    reason=(
        "Low-angle XRD peaks confirm intercalation of MAI and DMSO into PbI2 layers (@low_angle_xrd_peaks), "
        "elemental analysis matches the MAI-PbI2-DMSO formula (@elemental_analysis_confirms), "
        "and FTIR confirms N-H and S-O functional groups from both MAI and DMSO (@ftir_confirmation). "
        "Together these confirm the intermediate phase is a new MAI-PbI2-DMSO compound distinct from known phases."
    ),
    prior=0.5,
)

# --- Strategy: crystallinity preserved ---

strat_crystallinity = support(
    [crystallinity_preserved, perovskite_conversion_temperature],
    solid_state_conversion,
    reason=(
        "Crystallinity of perovskite films is preserved regardless of toluene drip (@crystallinity_preserved), "
        "and the conversion from intermediate phase to perovskite occurs via solid-state transformation at 100 degrees C (@perovskite_conversion_temperature). "
        "This solid-state conversion from the uniform intermediate phase preserves the flat morphology (@solid_state_conversion)."
    ),
    prior=0.5,
)

# --- Strategy: morphology characterization supports mechanism ---

strat_morphology = support(
    [intermediate_phase_rms_roughness, perovskite_film_rms_roughness, dense_grained_morphology],
    full_surface_coverage,
    reason=(
        "AFM shows the intermediate phase has RMS roughness of 6.0 nm (@intermediate_phase_rms_roughness), "
        "which increases only slightly to 8.3 nm after conversion to perovskite (@perovskite_film_rms_roughness). "
        "The dense-grained uniform morphology with 100-500 nm grains (@dense_grained_morphology) confirms "
        "100% surface coverage (@full_surface_coverage) is achieved through the solvent engineering process."
    ),
    prior=0.5,
)

# --- Strategy: hysteresis comparison supports bilayer advantage ---

strat_bilayer_eliminates_hysteresis = support(
    [large_hysteresis_without_mp, no_mp_tio2_forward_scan, no_mp_tio2_reverse_scan,
     negligible_hysteresis_bilayer, bilayer_forward_scan, bilayer_reverse_scan],
    bilayer_advantages,
    reason=(
        "Cells without mp-TiO2 exhibit large hysteresis with 9.1% efficiency discrepancy between forward (9.1%) and reverse (14.4%) scans (@large_hysteresis_without_mp, @no_mp_tio2_forward_scan, @no_mp_tio2_reverse_scan). "
        "In contrast, bilayer cells with 200-nm-thick mp-TiO2 show negligible hysteresis with nearly identical forward (15.8%) and reverse (15.9%) scan results (@negligible_hysteresis_bilayer, @bilayer_forward_scan, @bilayer_reverse_scan). "
        "This demonstrates the bilayer architecture effectively addresses hysteresis issues (@bilayer_advantages)."
    ),
    prior=0.5,
)

# --- Strategy: bilayer efficiency supports key achievement ---

strat_bilayer_efficiency = support(
    [average_bilayer_efficiency, best_cell_average, certified_efficiency_162],
    key_achievement,
    reason=(
        "The bilayer architecture achieves average PCE of 15.85% with negligible hysteresis (@average_bilayer_efficiency), "
        "the best cell shows PCE of 16.5% (@best_cell_average), "
        "and certification confirms 16.2% PCE under standard AM 1.5 G full sun conditions (@certified_efficiency_162). "
        "These results demonstrate the key achievement of certified 16.2% efficiency via fully solution-based process (@key_achievement)."
    ),
    prior=0.5,
)

# --- Strategy: mechanism explains intermediate phase formation ---

strat_mechanism_explains = support(
    [role_of_dmso, role_of_toluene, formation_mechanism],
    intermediate_phase_critical,
    reason=(
        "The DMSO coordinates with Pb2+ forming MAI-PbI2-DMSO intermediate phase while retarding rapid reaction (@role_of_dmso), "
        "toluene removes excess DMSO and freezes constituents into a uniform layer (@role_of_toluene), "
        "and the detailed mechanism shows how these steps produce the uniform intermediate phase (@formation_mechanism). "
        "This confirms the intermediate phase formation is decisive for achieving uniform perovskite layers (@intermediate_phase_critical)."
    ),
    prior=0.5,
)

# --- Strategy: balanced thickness explains hysteresis elimination ---

strat_thickness_optimization = support(
    [thickness_vs_efficiency, hysteresis_origin, mp_tio2_necessity],
    balanced_thickness_concept,
    reason=(
        "As mp-TiO2 thickness increases to approximately 200 nm, hysteresis reaches minimum (@thickness_vs_efficiency), "
        "which correlates with efficient charge collection reducing the large diffusion capacitance effect (@hysteresis_origin). "
        "An optimally thick mp-TiO2 layer is necessary for efficient charge collection (@mp_tio2_necessity), "
        "confirming the balanced thickness concept is critical for coincident J-V scans (@balanced_thickness_concept)."
    ),
    prior=0.5,
)

# --- Strategy: reproducibility supports process validity ---

strat_reproducibility = support(
    [reproducibility_histogram, average_bilayer_efficiency],
    solvent_engineering_contribution,
    reason=(
        "Approximately 80% of 108 independently fabricated devices exceed 15% PCE (@reproducibility_histogram), "
        "with average bilayer efficiency of 15.85% (@average_bilayer_efficiency). "
        "This high reproducibility demonstrates that solvent engineering provides a reliable process (@solvent_engineering_contribution)."
    ),
    prior=0.5,
)

# --- Strategy: intercalation enables uniform layers ---

strat_intercalation = support(
    [intermediate_phase_identity, full_surface_coverage, solid_state_conversion],
    intercalation_strategy,
    reason=(
        "The MAI-PbI2-DMSO intermediate phase forms via intercalation of MAI and DMSO into PbI2 layers (@intermediate_phase_identity), "
        "enabling 100% surface coverage (@full_surface_coverage), "
        "and the solid-state conversion preserves this uniformity (@solid_state_conversion). "
        "This intercalation strategy is effective for forming uniform PbI2-based perovskite layers (@intercalation_strategy)."
    ),
    prior=0.5,
)

# --- Strategy: problem statement leads to solution approach ---

strat_solution_approach = support(
    [spin_coating_problem, uniformity_limitation, mixed_solvent_solution],
    bilayer_architecture,
    reason=(
        "Simple spin-coating cannot produce homogeneous perovskite layers with 100% surface coverage (@spin_coating_problem, @uniformity_limitation), "
        "motivating the development of solvent engineering with GBL/DMSO mixed solvent and toluene drip (@mixed_solvent_solution). "
        "This solution approach enables the bilayer architecture that achieves both uniform morphology and high efficiency (@bilayer_architecture)."
    ),
    prior=0.5,
)

# --- Strategy: prior benchmarks contextualize achievement ---

strat_benchmark_comparison = support(
    [sequential_deposition_benchmark, vacuum_deposition_benchmark, key_achievement],
    certified_efficiency,
    reason=(
        "Prior work achieved 15.0% PCE via sequential deposition (@sequential_deposition_benchmark) and 15.4% via vacuum deposition (@vacuum_deposition_benchmark). "
        "The solvent engineering approach achieves certified 16.2% PCE (@key_achievement, @certified_efficiency), "
        "exceeding both prior benchmarks through a fully solution-based process without vacuum or high-temperature steps."
    ),
    prior=0.5,
)

# --- Strategy: IPCE validates performance ---

strat_ipce_validation = support(
    [ipce_plateau, jsc_from_ipce],
    best_cell_average,
    reason=(
        "The best cell shows IPCE plateau over 80% between 420-700 nm (@ipce_plateau), "
        "and the Jsc integrated from IPCE matches the J-V measurement (@jsc_from_ipce), "
        "validating the measured Jsc of 19.58 mA cm^-2 and PCE of 16.5% (@best_cell_average)."
    ),
    prior=0.5,
)