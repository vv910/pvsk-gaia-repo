"""
Reasoning strategies connecting claims.

This module adds reasoning strategies to connect the claims from Pass 1.
"""

from gaia.lang import (
    support,
)

# Import claims from motivation
from .motivation import (
    tandem_configuration,
    performance_potential,
    two_d_three_d_problem,
    surface_passivation_tradeoff,
    phj_solution,
    ion_immiscibility,
    hybrid_deposition_method,
    bilateral_improvement,
    nbg_champion_pce,
    nbg_average_improvement,
    type_two_band_alignment,
    previous_limitation,
)

# Import claims from s2_methods
from .s2_methods import (
    work_functions,
    bandgaps,
    heterojunction_verification,
    phj_layer_thickness,
    ion_distribution_stability,
)

# Import claims from s3_results
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

# Import claims from s4_discussion
from .s4_discussion import (
    type_ii_mechanism,
    depletion_region,
    electron_extraction_acceleration,
    two_d_layer_limitation,
    three_d_advantage,
    remaining_voc_ff_loss,
    optical_losses,
    future_improvement_path,
    long_term_stability,
    bromide_migration,
    thermal_stability_note,
    record_efficiency,
    bilateral_voc_ff,
    solution_processadvantage,
    charge_separation,
)

#------------------------------------------------------------------------------
# Motivation: Tandem configuration supports efficiency potential
#------------------------------------------------------------------------------

strat_tandem_efficiency = support(
    [tandem_configuration, performance_potential],
    previous_limitation,
    reason="Tandem cells should outperform single junctions due to broader solar spectrum utilization and reduced thermalization losses. However, previous record tandems had high Voc deficit and low FF due to non-radiative recombination at the Pb-Sn/C60 interface.",
    prior=0.85,
)

#------------------------------------------------------------------------------
# Problem statement: 2D/3D problem and surface passivation trade-off
#------------------------------------------------------------------------------

strat_two_d_limitations = support(
    [two_d_three_d_problem, surface_passivation_tradeoff],
    phj_solution,
    reason="The fundamental trade-off between surface passivation and conductivity in 2D/3D heterojunctions requires a new solution approach. 2D layers hinder charge transport.",
    prior=0.88,
)

#------------------------------------------------------------------------------
# PHJ solution connects to the problem it solves
#------------------------------------------------------------------------------

strat_phj_addresses_problem = support(
    [two_d_three_d_problem, surface_passivation_tradeoff],
    bilateral_improvement,
    reason="The 3D/3D bilayer PHJ addresses both surface passivation (reducing non-radiative recombination) and maintains high conductivity for charge transport.",
    prior=0.85,
)

#------------------------------------------------------------------------------
# Type II band alignment mechanism
#------------------------------------------------------------------------------

strat_type_ii_from_measurements = support(
    [work_functions, bandgaps],
    type_two_band_alignment,
    reason="Type II band alignment is directly supported by UPS measurements (work functions: 4.68 eV for Pb-Sn, 4.55 eV for FL-WBG) and optical bandgaps (1.25 eV vs 1.62 eV).",
    prior=0.92,
)

strat_type_ii_enables_charge_extraction = support(
    [type_two_band_alignment],
    type_ii_mechanism,
    reason="Type II alignment at the heterojunction interface facilitates electron extraction into C60 while reducing hole concentration in the defective interface layer.",
    prior=0.88,
)

#------------------------------------------------------------------------------
# PHJ formation: Hybrid deposition enables ion immiscibility
#------------------------------------------------------------------------------

strat_ion_immiscibility_enables_phj = support(
    [ion_immiscibility, hybrid_deposition_method],
    phj_solution,
    reason="Limited Pb2+/Sn2+ ion intermixing combined with the non-destructive hybrid evaporation-solution method preserves a stable 3D/3D bilayer structure that would otherwise homogenize.",
    prior=0.88,
)

#------------------------------------------------------------------------------
# PHJ verification supports ion distribution stability
#------------------------------------------------------------------------------

strat_stability_from_edx = support(
    [heterojunction_verification, phj_layer_thickness, ion_distribution_stability],
    phj_solution,
    reason="HR-STEM, EDX, and ToF-SIMS measurements confirm the ~50 nm FL-WBG layer on Pb-Sn persists after 60 days with no Sn2+ diffusion, validating the PHJ structure.",
    prior=0.88,
)

#------------------------------------------------------------------------------
# NBG PSC performance: Control vs PHJ comparison supports bilateral improvement
#------------------------------------------------------------------------------

strat_control_vs_phj = support(
    [control_vs_phj_comparison, device_statistics, champion_device],
    bilateral_improvement,
    reason="Direct experimental comparison (26 devices each, 148 PHJ total) shows PHJ improves both Voc (0.824V to 0.869V) and FF (78.5% to 80.8%) simultaneously.",
    prior=0.9,
)

strat_eqe_validates = support(
    [eqe_validation],
    champion_device,
    reason="EQE integrated photocurrent (32.5 mA/cm2) matches J-V measurement (33.0 mA/cm2), confirming measurement accuracy.",
    prior=0.9,
)

#------------------------------------------------------------------------------
# Champion device connects to record efficiency
#------------------------------------------------------------------------------

strat_nbg_champion = support(
    [nbg_champion_pce, eqe_validation],
    champion_device,
    reason="Champion NBG PSC achieves 23.8% PCE (stabilized 23.5%) with Voc=0.873V, Jsc=33.0 mA/cm2, FF=82.6%, validated by EQE.",
    prior=0.9,
)

strat_average_improvement = support(
    [nbg_average_improvement],
    bilateral_improvement,
    reason="Average PCE improves from 21.0% (control) to 22.8% (PHJ) across 26 devices per type, showing consistent improvement in Voc and FF.",
    prior=0.88,
)

#------------------------------------------------------------------------------
# PL and charge dynamics support non-radiative recombination suppression
#------------------------------------------------------------------------------

strat_pl_confirms_recombination = support(
    [pl_intensity_increase, trapped_reduction, built_in_potential],
    type_ii_mechanism,
    reason="Increased steady-state PL intensity, reduced trap density (SCLC), lower dark saturation current, and 50 mV higher built-in potential all confirm suppressed non-radiative recombination.",
    prior=0.88,
)

strat_el_qy = support(
    [el_qy_comparison, voc_loss_reduction],
    type_ii_mechanism,
    reason="EL quantum yield increases from 0.47% to 3.09%, corresponding to Voc loss reduction from 147 mV to 97 mV, confirming recombination suppression.",
    prior=0.88,
)

#------------------------------------------------------------------------------
# TRPL supports charge separation mechanism
#------------------------------------------------------------------------------

strat_trpl_separation = support(
    [trpl_phj_film, electron_transfer_rate],
    charge_separation,
    reason="Fast 7 ns decay component in PHJ films (vs none in control) and faster ETL transfer (70 ns vs 110 ns) indicate efficient charge separation at the type II interface.",
    prior=0.88,
)

strat_control_recombination = support(
    [trpl_control_film],
    type_ii_mechanism,
    reason="Control film shows slower bimolecular recombination (283 ns, 1073 ns) indicating more severe non-radiative recombination than PHJ films.",
    prior=0.88,
)

#------------------------------------------------------------------------------
# TA spectroscopy supports charge transfer mechanism
#------------------------------------------------------------------------------

strat_ta_transfer = support(
    [phj_ta_nbg_pumped, control_ta_spectrum],
    type_ii_mechanism,
    reason="New 780 nm TA peak in PHJ (when pumped from NBG side) that rises after 300 ps indicates electron injection from Pb-Sn into FL-WBG perovskite.",
    prior=0.88,
)

strat_no_back_transfer = support(
    [phj_ta_fl_wbg_pumped],
    type_ii_mechanism,
    reason="When pumping FL-WBG side, only 780 nm peak appears with no charge transfer signature, confirming no back-transfer - consistent with type II band alignment.",
    prior=0.88,
)

#------------------------------------------------------------------------------
# Simulation supports mechanism explanation
#------------------------------------------------------------------------------

strat_simulation = support(
    [simulation_model, dil_trap_density_effect, dil_thickness_effect, simulated_improvement],
    type_ii_mechanism,
    reason="SCAPS-1D simulation shows PHJ devices maintain performance at high DIL trap densities where control devices degrade, and are insensitive to DIL thickness, explaining the >40mV Voc and 5% FF improvement.",
    prior=0.82,
)

#------------------------------------------------------------------------------
# Type II mechanism discussion
#------------------------------------------------------------------------------

strat_type_ii_mechanism = support(
    [type_two_band_alignment, depletion_region, electron_extraction_acceleration],
    type_ii_mechanism,
    reason="Type II alignment reduces hole concentration in DIL and accelerates electron extraction into C60, suppressing non-radiative recombination at the interface.",
    prior=0.88,
)

#------------------------------------------------------------------------------
# Tandem performance
#------------------------------------------------------------------------------

strat_wbg_subcell = support(
    [wbg_subcell_performance],
    record_efficiency,
    reason="WBG subcell with FA0.8Cs0.2Pb(I0.62Br0.38)3 (1.78 eV bandgap) achieves 18.6% PCE with Voc=1.274V, Jsc=17.7 mA/cm2, FF=82.6%.",
    prior=0.9,
)

strat_tandem_comparison = support(
    [nbg_subcell_in_tandem, tandem_ff_improvement],
    record_efficiency,
    reason="PHJ in NBG subcell improves tandem FF from 78.0% to 81.4% and PCE from 26.0% to 27.7% under current-matching conditions.",
    prior=0.88,
)

strat_champion_tandem = support(
    [tandem_champion, certified_efficiency, eqe_tandem],
    record_efficiency,
    reason="Champion tandem achieves 28.5% PCE (certified 28.0% by JET) with Voc=2.112V, Jsc=16.5 mA/cm2, FF=81.9%, validated by EQE current matching.",
    prior=0.95,
)

strat_large_area = support(
    [large_area_tandem],
    record_efficiency,
    reason="Large-area 1.05 cm2 tandem achieves 26.9% PCE with Voc=2.149V, Jsc=15.7 mA/cm2, FF=79.8%.",
    prior=0.85,
)

#------------------------------------------------------------------------------
# Stability
#------------------------------------------------------------------------------

strat_operational_stability = support(
    [operational_stability],
    long_term_stability,
    reason="Tandem with PHJ retains 93% of initial PCE after 600h MPP tracking under AM 1.5G illumination in ambient air, demonstrating good operational stability.",
    prior=0.88,
)

strat_degradation = support(
    [degradation_mechanism, reverse_bias_stability],
    long_term_stability,
    reason="Performance degradation after 688h is mainly FF drop from Au migration into perovskite. Reverse-bias stability of tandem is superior to single-junction PSCs.",
    prior=0.82,
)

#------------------------------------------------------------------------------
# Long-term stability of PHJ structure
#------------------------------------------------------------------------------

strat_phj_stability = support(
    [long_term_stability, bromide_migration, thermal_stability_note],
    solution_processadvantage,
    reason="PHJ structure shows no Sn2+ diffusion after 60 days and no PCE degradation after 3000h dark storage. Br- diffusion occurs but does not affect bandgap. Thermal stability can be improved with better electrodes and tunnel junction.",
    prior=0.85,
)

#------------------------------------------------------------------------------
# Discussion: 3D/3D vs 2D/3D advantages
#------------------------------------------------------------------------------

strat_three_d_advantage = support(
    [two_d_layer_limitation, bilateral_voc_ff],
    three_d_advantage,
    reason="Unlike 2D/3D heterojunctions which hinder charge transport due to low conductivity, 3D/3D PHJ achieves both surface passivation (high Voc) and high conductivity (high FF).",
    prior=0.88,
)

#------------------------------------------------------------------------------
# Future improvements
#------------------------------------------------------------------------------

strat_remaining_losses = support(
    [remaining_voc_ff_loss, optical_losses],
    future_improvement_path,
    reason="Voc and FF remain below Shockley-Queisser limits due to non-radiative recombination and optical losses. Reducing bulk defects, passivating interfaces, and improving light management can enable >30% PCE.",
    prior=0.82,
)

strat_solution_advantage = support(
    [hybrid_deposition_method, ion_immiscibility, solution_processadvantage],
    phj_solution,
    reason="The non-destructive hybrid evaporation-solution method enables 3D/3D bilayer PHJ fabrication that was previously unachievable with conventional solution processing, which damages Pb-Sn perovskites.",
    prior=0.88,
)

__all__ = [
    "strat_tandem_efficiency",
    "strat_two_d_limitations",
    "strat_phj_addresses_problem",
    "strat_type_ii_from_measurements",
    "strat_type_ii_enables_charge_extraction",
    "strat_ion_immiscibility_enables_phj",
    "strat_stability_from_edx",
    "strat_control_vs_phj",
    "strat_eqe_validates",
    "strat_nbg_champion",
    "strat_average_improvement",
    "strat_pl_confirms_recombination",
    "strat_el_qy",
    "strat_trpl_separation",
    "strat_control_recombination",
    "strat_ta_transfer",
    "strat_no_back_transfer",
    "strat_simulation",
    "strat_type_ii_mechanism",
    "strat_wbg_subcell",
    "strat_tandem_comparison",
    "strat_champion_tandem",
    "strat_large_area",
    "strat_operational_stability",
    "strat_degradation",
    "strat_phj_stability",
    "strat_three_d_advantage",
    "strat_remaining_losses",
    "strat_solution_advantage",
]