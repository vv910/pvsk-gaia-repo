"""
Reasoning strategies connecting claims in the Gu2023 bifacial perovskite package.

This module contains the infer strategies linking premises to conclusions,
organizing the reasoning structure for the bifacial perovskite minimodules work.
"""

from gaia.lang import (
    claim,
    setting,
    support,
    compare,
    deduction,
    abduction,
    induction,
    analogy,
    extrapolation,
    elimination,
    case_analysis,
    mathematical_induction,
    composite,
    infer,
    contradiction,
    equivalence,
    complement,
    disjunction,
)

from .motivation import (
    bifacial_gain_background,
    average_albedo_recorded,
    perovskite_bifacial_challenge,
    research_objective,
    front_efficiency_record,
    stability_demonstrated,
    power_generation_density_measurement,
    bifaciality_measurement,
    initial_efficiency_retention,
)

from .s2_module_structure import (
    module_structure_p_i_n,
    ito_sheet_resistance,
    ag_grid_design,
    optimal_ag_grid_spacing,
    relative_pce_loss_reduction,
    ff_improvement_with_ag_grid,
    bifacial_gain_percentage,
    simulated_pgds_by_albedo,
)

from .s3_hydrophobic_additive import (
    ald_damage_to_perovskite,
    tpfb_in_htl_protection,
    tpfb_spread_to_perovskite,
    hydrophobic_surface_confirmation,
    tpfb_passivation_effect,
    tpfb_reduced_trap_density,
    tpfb_frei_level_ptaa,
    ff_improvement_tpfb,
    tpfb_enhanced_stability,
)

from .s4_light_scattering import (
    jsc_reduction_without_reflective_electrode,
    sio2_np_light_scattering,
    optimal_np_size_range,
    optimal_np_spacing_range,
    absorption_enhancement_simulation,
    np_synthesis_and_embedding,
    no_extra_recombination_from_np,
    jsc_increase_with_optimal_np,
    front_pce_improvement_with_np,
)

from .s5_performance import (
    small_cell_front_pce,
    small_cell_rear_pce,
    bifaciality_small_cell,
    power_generation_density_albedo_02,
    minimodule_front_aperture_efficiency,
    minimodule_rear_aperture_efficiency,
    nrel_certified_front_efficiency,
    nrel_certified_rear_efficiency,
    average_front_efficiency_8_modules,
    average_rear_efficiency_8_modules,
    pgd_by_albedo,
)

from .s6_stability import (
    initial_pce_retention_6000h,
    damp_heat_retention,
    ald_sno2_stabilization_benefit,
    stability_benefits_composition,
)


# ============================================================================
# REASONING STRATEGIES: Module Structure
# ============================================================================

# Ag grid design enables balanced performance
strat_ag_grid_balances_tradeoffs = support(
    [ag_grid_design, optimal_ag_grid_spacing, relative_pce_loss_reduction],
    ff_improvement_with_ag_grid,
    reason="The Ag grid design rationale (@ag_grid_design) and optimal spacing of approximately 2mm (@optimal_ag_grid_spacing) together explain the FF improvement from 0.70 to 0.77 and PCE loss reduction from 8.6% to less than 0.9% (@relative_pce_loss_reduction). The modeling shows that this spacing minimizes the bifacial gain loss while maximizing resistance reduction.",
    prior=0.85,
)

# Bifacial gain follows from albedo harvesting
strat_bifacial_gain_from_albedo = support(
    [bifacial_gain_background, ff_improvement_with_ag_grid, optimal_ag_grid_spacing],
    bifacial_gain_percentage,
    reason="The 15% bifacial power gain (@bifacial_gain_percentage) follows from the combination of background bifacial gain in silicon modules (@bifacial_gain_background), the improved fill factor with optimal Ag grid (@ff_improvement_with_ag_grid), and the optimized grid spacing (@optimal_ag_grid_spacing) that maximizes rear light harvesting while minimizing shading.",
    prior=0.85,
)

# Simulated PGDs align with performance targets
strat_simulated_pgds_support_objective = support(
    [simulated_pgds_by_albedo, research_objective],
    power_generation_density_measurement,
    reason="The simulated PGDs of 21.5-26.4 mW/cm2 for albedos 0.1-0.4 (@simulated_pgds_by_albedo) provide the theoretical basis for the research objective (@research_objective), showing that bifacial perovskite modules can exceed monofacial performance at typical albedos.",
    prior=0.80,
)


# ============================================================================
# REASONING STRATEGIES: Hydrophobic Additive
# ============================================================================

# TPFB spreads and enhances hydrophobicity
strat_tpfb_spreading_mechanism = support(
    [tpfb_in_htl_protection, tpfb_spread_to_perovskite],
    hydrophobic_surface_confirmation,
    reason="The observation that mixing 5 wt% TPFB in PTAA (@tpfb_in_htl_protection) protects perovskite during ALD is explained by the measured spreading of approximately 35% of TPFB from HTL to perovskite surface (@tpfb_spread_to_perovskite), which directly increases surface hydrophobicity (@hydrophobic_surface_confirmation).",
    prior=0.90,
)

# TPFB passivation reduces defects
strat_tpfb_passivation = support(
    [tpfb_spread_to_perovskite, hydrophobic_surface_confirmation],
    tpfb_passivation_effect,
    reason="TPFB passivation of perovskite (@tpfb_passivation_effect) is supported by the spreading behavior (@tpfb_spread_to_perovskite) that brings TPFB to the perovskite surface and the enhanced hydrophobicity (@hydrophobic_surface_confirmation), which together create a protective and passivating interface.",
    prior=0.85,
)

# TPFB reduces trap density and enhances stability
strat_tpfb_stability = support(
    [tpfb_passivation_effect, tpfb_reduced_trap_density],
    tpfb_enhanced_stability,
    reason="The enhanced stability from TPFB (@tpfb_enhanced_stability) is supported by the passivation effect (@tpfb_passivation_effect) and reduced trap density (@tpfb_reduced_trap_density), which together indicate fewer point defects that could catalyze degradation pathways under light soaking.",
    prior=0.80,
)

# FF improvement from TPFB has multiple causes
strat_ff_improvement_from_tpfb = support(
    [tpfb_in_htl_protection, tpfb_passivation_effect, tpfb_frei_level_ptaa],
    ff_improvement_tpfb,
    reason="The FF improvement from 0.68 to 0.76 with TPFB in HTL (@ff_improvement_tpfb) is supported by three mechanisms: moisture protection during ALD processing (@tpfb_in_htl_protection), passivation reducing recombination (@tpfb_passivation_effect), and p-doping of PTAA for better energy alignment (@tpfb_frei_level_ptaa). These mechanisms act synergistically to improve charge extraction and reduce losses.",
    prior=0.85,
)


# ============================================================================
# REASONING STRATEGIES: Light Scattering NPs
# ============================================================================

# NP size optimization follows from scattering simulation
strat_np_size_optimization = support(
    [sio2_np_light_scattering, optimal_np_size_range],
    absorption_enhancement_simulation,
    reason="The FDTD simulation showing 5.4-19.8% enhanced 800nm absorption (@absorption_enhancement_simulation) is based on the Mie scattering principle (@sio2_np_light_scattering) and the optimal size range of 400-600nm (@optimal_np_size_range) that balances efficient red/NIR scattering with minimal UV-vis absorption loss.",
    prior=0.85,
)

# Optimal NP spacing maximizes absorption without defects
strat_np_spacing_optimization = support(
    [optimal_np_spacing_range, np_synthesis_and_embedding, no_extra_recombination_from_np],
    jsc_increase_with_optimal_np,
    reason="The Jsc increase from 23.1 to 23.9 mA/cm2 (@jsc_increase_with_optimal_np) with optimal NP spacing is supported by the simulated optimal spacing of 1-1.5 um (@optimal_np_spacing_range), successful embedding of 500nm SiO2 NPs (@np_synthesis_and_embedding), and the confirmation that NPs do not introduce extra recombination (@no_extra_recombination_from_np).",
    prior=0.85,
)

# PCE improvement from NPs follows from Jsc and absorption
strat_pce_improvement_from_np = support(
    [jsc_increase_with_optimal_np, absorption_enhancement_simulation, no_extra_recombination_from_np],
    front_pce_improvement_with_np,
    reason="The PCE increase from 22.1% to 23.2% (@front_pce_improvement_with_np) directly follows from the Jsc increase (@jsc_increase_with_optimal_np) due to enhanced red/NIR absorption (@absorption_enhancement_simulation), while the absence of extra recombination (@no_extra_recombination_from_np) ensures fill factor is not compromised.",
    prior=0.85,
)


# ============================================================================
# REASONING STRATEGIES: Performance
# ============================================================================

# Small cell performance demonstrates bifaciality advantage
strat_small_cell_bifaciality = support(
    [small_cell_front_pce, small_cell_rear_pce],
    bifaciality_small_cell,
    reason="The high bifaciality of approximately 80% (@bifaciality_small_cell) follows from the combination of 20.2% front efficiency (@small_cell_front_pce) and 18.5% rear efficiency (@small_cell_rear_pce), demonstrating effective rear-side light harvesting in bifacial configuration.",
    prior=0.90,
)

# Minimodule efficiency comparable to best monofacial
strat_minimodule_record = support(
    [minimodule_front_aperture_efficiency, minimodule_rear_aperture_efficiency],
    front_efficiency_record,
    reason="The front efficiency record comparable to best monofacial minimodules (@front_efficiency_record) is supported by the champion minimodule front efficiency of 20.2% (@minimodule_front_aperture_efficiency) and rear efficiency of 15.0% (@minimodule_rear_aperture_efficiency), with certified NREL values of 19.2% and 14.1% respectively.",
    prior=0.90,
)

# PGD measurement confirms advantage over single-junction cells
strat_pgd_advantage = support(
    [power_generation_density_albedo_02, pgd_by_albedo],
    power_generation_density_measurement,
    reason="The power-generation density of 26.4 mW/cm2 at albedo 0.2 (@power_generation_density_measurement) exceeding any reported single-junction perovskite solar cell is supported by the small cell PGD of 26.4 mW/cm2 (@power_generation_density_albedo_02) and the average module PGDs of 22.4-25.3 mW/cm2 for albedos 0.2-0.4 (@pgd_by_albedo).",
    prior=0.85,
)

# NREL certification validates performance claims
strat_nrel_certification = support(
    [minimodule_front_aperture_efficiency, minimodule_rear_aperture_efficiency],
    nrel_certified_front_efficiency,
    reason="The NREL certified front efficiency of 19.2% (@nrel_certified_front_efficiency) is credible because it was measured on a champion minimodule with front aperture efficiency of 20.2% (@minimodule_front_aperture_efficiency), and the rear certified efficiency of 14.1% (@nrel_certified_rear_efficiency) matches the measured rear efficiency of 15.0% (@minimodule_rear_aperture_efficiency).",
    prior=0.90,
)

# Reproducibility across 8 modules demonstrated
strat_module_reproducibility = support(
    [average_front_efficiency_8_modules, average_rear_efficiency_8_modules],
    pgd_by_albedo,
    reason="The average PGD values of 22.4-25.3 mW/cm2 at albedos 0.2-0.4 (@pgd_by_albedo) are credible because they come from measurements across eight bifacial minimodules showing good reproducibility with average front efficiency 19.5% (@average_front_efficiency_8_modules) and rear efficiency 14.5% (@average_rear_efficiency_8_modules).",
    prior=0.85,
)


# ============================================================================
# REASONING STRATEGIES: Stability
# ============================================================================

# 6000h stability confirmed and explained
strat_stability_6000h = support(
    [initial_pce_retention_6000h, ald_sno2_stabilization_benefit, stability_benefits_composition],
    stability_demonstrated,
    reason="The demonstrated stability of 97% retention after 6000h (@stability_demonstrated) is supported by the measured 97% retention after over 6,000 hours light soaking (@initial_pce_retention_6000h), explained by ALD SnO2 stabilization benefits (@ald_sno2_stabilization_benefit) and the stable FA-Cs composition (@stability_benefits_composition).",
    prior=0.90,
)

# Damp-heat stability additional confirmation
strat_damp_heat_stability = support(
    [ald_sno2_stabilization_benefit, stability_benefits_composition],
    damp_heat_retention,
    reason="The damp-heat retention of approximately 84% after 1,000 hours (@damp_heat_retention) is supported by the same stabilization mechanisms: ALD SnO2 prevents interface degradation (@ald_sno2_stabilization_benefit) and the FA-Cs composition provides intrinsic stability (@stability_benefits_composition).",
    prior=0.80,
)


# ============================================================================
# REASONING STRATEGIES: Overall Conclusions
# ============================================================================

# Research objective achieved through combined strategies
strat_overall_conclusion = support(
    [
        ff_improvement_with_ag_grid,
        ff_improvement_tpfb,
        front_pce_improvement_with_np,
        bifacial_gain_percentage,
        pgd_by_albedo,
        initial_pce_retention_6000h,
    ],
    research_objective,
    reason="The research objective of record high efficiency and stability (@research_objective) is supported by: (1) Ag grid achieving FF 0.77 and 15% bifacial gain (@ff_improvement_with_ag_grid), (2) TPFB in HTL achieving FF 0.76 and moisture protection (@ff_improvement_tpfb), (3) SiO2 NPs recovering absorption to achieve 23.2% PCE (@front_pce_improvement_with_np), (4) bifacial gain of 15% at albedo 0.2 (@bifacial_gain_percentage), (5) average PGD of 23.9 mW/cm2 at albedo 0.3 (@pgd_by_albedo), and (6) 97% retention after 6000h light soaking (@initial_pce_retention_6000h).",
    prior=0.85,
)

# Combined techniques yield optimal bifacial minimodule performance
strat_combined_performance = support(
    [
        bifaciality_small_cell,
        minimodule_front_aperture_efficiency,
        nrel_certified_front_efficiency,
        pgd_by_albedo,
        initial_pce_retention_6000h,
    ],
    front_efficiency_record,
    reason="The bifacial minimodule front efficiency comparable to best monofacial modules (@front_efficiency_record) is supported by the small cell bifaciality of 80% (@bifaciality_small_cell), champion minimodule front efficiency of 20.2% (@minimodule_front_aperture_efficiency), NREL certification of 19.2% stabilized (@nrel_certified_front_efficiency), average PGD of 25.3 mW/cm2 at albedo 0.4 (@pgd_by_albedo), and 97% efficiency retention after 6000h (@initial_pce_retention_6000h).",
    prior=0.85,
)