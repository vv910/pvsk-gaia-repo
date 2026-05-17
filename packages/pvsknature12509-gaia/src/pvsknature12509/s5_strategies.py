"""
Strategies module for Liu et al. 2013 Nature paper.

Paper: Efficient planar heterojunction perovskite solar cells by vapour deposition
Citation: [@Liu2013]

This module connects claims with reasoning strategies.
Only claims that are DERIVED from other claims in the paper need strategies.
Independent background facts (stated but not derived) are claims without strategies.
"""

from gaia.lang import (
    support,
    compare,
    contradiction,
)

# Import named claims from modules
from .motivation import (
    meso_superstructured_improvement,
    meso_superstructured_mechanism,
    meso_efficiency_progress,
    solution_planarHeterojunction,
    planar_vs_meso_question,
    vapour_deposition_enables_uniform_films,
    high_efficiency_planar_demonstrated,
    device_architecture_description,
)

from .s3_results import (
    xrd_peak_positions,
    xrd_phase_purity,
    xrd_c_axis_contraction,
    crystal_structure_description,
    crystal_size_limited,
    vapour_deposited_morphology,
    solution_processed_morphology,
    vapour_deposited_cross_section,
    solution_processed_cross_section,
    vapour_best_Jsc,
    vapour_best_Voc,
    vapour_best_FF,
    vapour_best_PCE,
    solution_best_Jsc,
    solution_best_Voc,
    solution_best_FF,
    solution_best_PCE,
    vapour_batch_Jsc_avg,
    vapour_batch_Voc_avg,
    vapour_batch_FF_avg,
    vapour_batch_PCE_avg,
    diffusion_length_lower_bound,
    uniformity_advantage,
    pinhole_shunting,
    solution_efficiency_surprise,
)

from .s4_discussion import (
    perovskite_versatility,
    tandem_top_cell_potential,
    all_perovskite_multijunction,
    infra_compatibility,
    manufacturing_route_question,
    diffusion_length_needs_work,
    wider_bandgap_top_cell_target,
    threshold_15_percent,
    planar_architecture_sufficiency,
    future_directions,
    vapour_deposition_maturity,
    oled_vapour_deposition_compatibility,
    vapour_vs_solution_fom_comparison,
)

# ========================
# Motivation section - derived claims
# ========================

strat_meso_mechanism = support(
    [meso_superstructured_improvement],
    meso_superstructured_mechanism,
    reason="The mechanism explaining the Voc enhancement is based on electron confinement increasing quasi-Fermi level splitting under illumination [@Liu2013].",
    prior=0.5,
)

strat_meso_efficiency = support(
    [meso_superstructured_mechanism],
    meso_efficiency_progress,
    reason="Building on the Voc enhancement mechanism, further optimization of the meso-superstructured design led to >12% efficiency [@Liu2013].",
    prior=0.5,
)

strat_high_efficiency_planar = support(
    [vapour_deposition_enables_uniform_films, high_efficiency_planar_demonstrated],
    planar_architecture_sufficiency,
    reason="The key finding that vapour-deposited planar heterojunction achieves >15% efficiency demonstrates that mesostructure is not necessary for highest efficiencies, directly answering the research question [@Liu2013].",
    prior=0.5,
)

# ========================
# Results section - derived claims
# ========================

strat_xrd_purity = support(
    [xrd_peak_positions],
    xrd_phase_purity,
    reason="Close inspection of the (110) region shows minimal PbI2 and no CH3NH3PbCl3 peaks, indicating high phase purity of the mixed-halide perovskite [@Liu2013].",
    prior=0.5,
)

strat_c_axis = support(
    [xrd_phase_purity],
    xrd_c_axis_contraction,
    reason="The c-axis contraction observed in XRD is consistent with theoretical predictions of Cl occupying apical positions out of the PbI4 plane [@Liu2013].",
    prior=0.5,
)

strat_crystal_structure = support(
    [xrd_peak_positions],
    crystal_structure_description,
    reason="Based on the XRD analysis, the crystal structure is identified as orthorhombic ABX3 perovskite as illustrated in Fig. 1d [@Liu2013].",
    prior=0.5,
)

strat_crystal_size = support(
    [xrd_peak_positions],
    crystal_size_limited,
    reason="XRD peak width analysis indicates crystal sizes exceed 400 nm (the resolution limit due to machine broadening) for both deposition methods [@Liu2013].",
    prior=0.5,
)

strat_vapour_PCE = support(
    [vapour_best_Jsc, vapour_best_Voc, vapour_best_FF],
    vapour_best_PCE,
    reason="PCE calculated from Jsc (21.5 mA/cm²), Voc (1.07 V), and FF (0.68) = 15.4% under AM1.5 101 mW/cm² simulated sunlight [@Liu2013].",
    prior=0.5,
)

strat_solution_PCE = support(
    [solution_best_Jsc, solution_best_Voc, solution_best_FF],
    solution_best_PCE,
    reason="PCE calculated from Jsc (17.6 mA/cm²), Voc (0.84 V), and FF (0.58) = 8.6% under AM1.5 simulated sunlight [@Liu2013].",
    prior=0.5,
)

strat_vapour_batch_PCE = support(
    [vapour_batch_Jsc_avg, vapour_batch_Voc_avg, vapour_batch_FF_avg],
    vapour_batch_PCE_avg,
    reason="PCE calculated from average Jsc (18.9 mA/cm²), Voc (1.05 V), and FF (0.62) = 12.3% for the 12-device batch [@Liu2013].",
    prior=0.5,
)

strat_diffusion_length = support(
    [vapour_deposited_cross_section],
    diffusion_length_lower_bound,
    reason="Since charges are successfully collected at both p-type and n-type heterojunctions across the 330 nm film, the diffusion length must be at least this value [@Liu2013].",
    prior=0.5,
)

strat_uniformity_advantage = support(
    [vapour_deposited_morphology, solution_processed_morphology],
    uniformity_advantage,
    reason="The contrast in film uniformity (uniform nanometer-scale features for vapour vs. inhomogeneous micrometer-scale platelets for solution) directly correlates with the performance difference between the two deposition methods [@Liu2013].",
    prior=0.5,
)

strat_pinhole_shunting = support(
    [solution_processed_morphology, solution_processed_cross_section],
    pinhole_shunting,
    reason="The voids and pinholes in solution-processed films expose the TiO2 layer directly to spiro-OMeTAD, creating shunting paths that reduce FF and Voc compared to the uniform vapour-deposited films [@Liu2013].",
    prior=0.5,
)

strat_solution_efficiency_surprise = support(
    [pinhole_shunting, solution_best_PCE],
    solution_efficiency_surprise,
    reason="Despite pinholes causing shunting, the solution-processed devices still achieve >8% efficiency, demonstrating the inherent capability of the perovskite absorber material independent of film quality issues [@Liu2013].",
    prior=0.5,
)

# ========================
# Discussion section - derived claims
# ========================

strat_perovskite_versatility = support(
    [high_efficiency_planar_demonstrated, crystal_structure_description],
    perovskite_versatility,
    reason="The demonstration of >15% efficiency in a simple planar architecture using versatile vapour deposition, combined with the known flexibility of the ABX3 perovskite family, establishes perovskite versatility for highly efficient solar cells [@Liu2013].",
    prior=0.5,
)

strat_tandem_potential = support(
    [high_efficiency_planar_demonstrated, vapour_deposition_maturity],
    tandem_top_cell_potential,
    reason="The >15% efficiency achieved by vapour-deposited perovskite, combined with the mature vapour deposition technique, makes it suitable as a top cell in tandem configurations with established PV technologies [@Liu2013].",
    prior=0.5,
)

strat_all_perovskite = support(
    [tandem_top_cell_potential, perovskite_versatility],
    all_perovskite_multijunction,
    reason="The demonstrated versatility of perovskites in composition (for bandgap tuning) and processing methods supports the long-term vision of all-perovskite multi-junction cells [@Liu2013].",
    prior=0.5,
)

strat_infra_compatibility = support(
    [vapour_deposition_maturity, oled_vapour_deposition_compatibility],
    infra_compatibility,
    reason="The mature industrial status of vapour deposition technology and its compatibility with existing PV manufacturing infrastructure enables rapid technology transfer [@Liu2013].",
    prior=0.5,
)

strat_manufacturing_question = support(
    [infra_compatibility, solution_planarHeterojunction],
    manufacturing_route_question,
    reason="While vapour deposition currently produces better films, the question of whether solution processing can eventually match this quality remains open [@Liu2013].",
    prior=0.5,
)

strat_diffusion_length_work = support(
    [diffusion_length_lower_bound],
    diffusion_length_needs_work,
    reason="While 330 nm sets a lower bound, precise values and charge generation mechanisms require further investigation [@Liu2013].",
    prior=0.5,
)

strat_wider_bandgap_target = support(
    [tandem_top_cell_potential, infra_compatibility],
    wider_bandgap_top_cell_target,
    reason="The perovskite technology achieves >15% efficiency as a wide-bandgap absorber and is compatible with existing PV infrastructure, fulfilling the long-standing community goal of an efficient top cell for tandem configurations [@Liu2013].",
    prior=0.5,
)

strat_threshold_15_percent = support(
    [vapour_best_PCE, vapour_batch_PCE_avg],
    threshold_15_percent,
    reason="The best device at 15.4% and batch average at 12.3% demonstrate that the 15% threshold has been crossed with planar architecture, proving mesostructure is not essential for high perovskite efficiencies [@Liu2013].",
    prior=0.5,
)

strat_planar_architecture_sufficiency = support(
    [threshold_15_percent, uniformity_advantage],
    planar_architecture_sufficiency,
    reason="The achievement of >15% PCE in a simple planar heterojunction without any mesostructure demonstrates that complex nanostructures are unnecessary for peak perovskite performance [@Liu2013].",
    prior=0.5,
)

strat_future_directions = support(
    [diffusion_length_needs_work],
    future_directions,
    reason="Based on the remaining knowledge gaps identified in this work, future research directions are outlined [@Liu2013].",
    prior=0.5,
)

strat_fom_comparison = support(
    [vapour_best_Jsc, vapour_best_Voc, vapour_best_FF, solution_best_Jsc, solution_best_Voc, solution_best_FF],
    vapour_vs_solution_fom_comparison,
    reason="Direct comparison of best-performing devices shows vapour deposition outperforms solution processing across all four key metrics (Jsc, Voc, FF, PCE) [@Liu2013].",
    prior=0.5,
)