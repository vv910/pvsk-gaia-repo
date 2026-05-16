"""
Results section: Connecting reasoning with strategies.

This module connects knowledge nodes with reasoning strategies.
"""

from gaia.lang import (
    claim,
    setting,
    support,
    infer,
    contradiction,
    compare,
    abduction,
)

from .motivation import (
    efficiency_progression,
    abx3_structure,
    exceptional_absorption,
    low_exciton_binding,
    long_diffusion_lengths,
    tuneable_bandgap,
    mapbi3_never_exceeded_20percent,
    mapbi3_phase_transition,
    mapbi3_halide_segregation,
    fapi3_instability,
    cspbi3_bandgap,
    cspbi3_thermal_stability,
    mixed_cations_design_principle,
    ma_crystallizer,
    yellow_phase_impurities,
    cs_ionic_radius,
    cs_effectively_promotes_black_phase,
    ma_induces_slowly,
    triple_cation_strategy,
    triple_cation_versatility,
    triple_cation_robustness,
    cs_suppresses_yellow_phase,
    industrialization_relevance,
)

from .s2_methods import (
    triple_cation_composition,
    xrd_measurement,
    cs_addition_eliminates_impurities,
    absorption_pl_spectra,
    cs_integrated_into_lattice,
    black_phase_entropically_stabilized,
    thermal_stability_test,
    cs_increases_thermal_stability,
    film_formation_no_annealing,
    film_formation_with_cs,
    processing_temperature_sensitivity,
    cs_benefits_summary,
    device_architecture,
    baseline_efficiency,
    fill_factor_improvement,
    cs_ma_ratio_optimization,
    cs5m_monomorphic_grains,
    seed_assisted_crystal_growth,
    device_statistics,
    cs_benefits_reproducibility,
    best_stabilized_pce,
    long_term_stability,
    fill_factor_degradation,
    high_performer_stability,
)

# Strategy: Triple cation strategy enables high efficiency and stability
strat_triple_cation_supports_high_efficiency = support(
    [triple_cation_strategy],
    triple_cation_versatility,
    reason="The triple cation Cs/MA/FA strategy allows fine-tuning of perovskite films to achieve stabilized PCE exceeding 21% and maintaining ~18% after 250 hours under operational conditions [@Saliba2016].",
    prior=0.5,
)

# Strategy: Cs suppresses yellow phase - evidence from XRD
strat_xrd_supports_cs_eliminates_impurities = support(
    [xrd_measurement, cs_addition_eliminates_impurities],
    cs_suppresses_yellow_phase,
    reason="XRD data for CsxM series shows that Cs0M has yellow phase peaks at 11.6 and 12.7 degrees, but upon Cs addition these peaks disappear completely, indicating Cs suppresses yellow phase impurities [@Saliba2016].",
    prior=0.5,
)

# Strategy: Cs integrates into lattice and stabilizes black phase
strat_cs_lattice_integration = support(
    [cs_integrated_into_lattice, black_phase_entropically_stabilized],
    triple_cation_robustness,
    reason="Cs integration into the perovskite lattice lowers effective cation radius, shifting tolerance factor toward cubic structure. The black phase is entropically stabilized at room temperature, making films less sensitive to temperature, solvent vapors, and heating protocols [@Saliba2016].",
    prior=0.5,
)

# Strategy: Thermal stability improved by Cs
strat_cs_improves_thermal_stability = support(
    [thermal_stability_test, cs_increases_thermal_stability],
    triple_cation_robustness,
    reason="Thermal stability tests at 130C for 3 hours show Cs10M retains black color while Cs0M bleaches. Cs increases thermal stability for fixed halide ratio, contributing to operational stability [@Saliba2016].",
    prior=0.5,
)

# Strategy: Cs enables film formation at room temperature
strat_cs_enables_room_temp_formation = support(
    [film_formation_no_annealing, film_formation_with_cs],
    cs_suppresses_yellow_phase,
    reason="Cs0M does not form perovskite without annealing, remaining red with no perovskite XRD peak. Cs10M forms black perovskite at room temperature, showing Cs induces black phase directly during deposition [@Saliba2016].",
    prior=0.5,
)

# Strategy: Processing temperature sensitivity reduced by Cs
strat_cs_reduces_temp_sensitivity = support(
    [processing_temperature_sensitivity],
    cs_benefits_summary,
    reason="Cs0M requires 25C to form perovskite but Cs10M forms at 18C. Cs10M is more robust to temperature variations during processing, which is critical for reproducibility and industrialization [@Saliba2016].",
    prior=0.5,
)

# Strategy: Device performance improvement
strat_cs_improves_device_performance = support(
    [fill_factor_improvement, cs_ma_ratio_optimization, device_statistics],
    triple_cation_versatility,
    reason="Fill factor improves to 0.77 at 10% Cs. Both Cs and MA are required for optimal performance. Statistics from 98 Cs5M devices show PCE of 19.20 plus or minus 0.91% vs 16.37 plus or minus 1.49% for Cs0M, with 20 devices exceeding 20% [@Saliba2016].",
    prior=0.5,
)

# Strategy: Cs leads to monolithic grains
strat_cs_leads_to_monomorphic_grains = support(
    [cs5m_monomorphic_grains, seed_assisted_crystal_growth],
    fill_factor_improvement,
    reason="Cs5M devices have monolithic grains extending from bottom to top, enabling better charge transport and higher fill factor. Cs acts as seed for crystal growth at room temperature, promoting uniform grain formation [@Saliba2016].",
    prior=0.5,
)

# Strategy: Reproducibility improved
strat_cs_improves_reproducibility = support(
    [cs_benefits_reproducibility, device_statistics],
    industrialization_relevance,
    reason="MA/FA alone is sensitive to processing temperature causing batch variations. Cs addition stabilizes the black phase regardless of initial temperature, enabling 98 devices across 18 batches to achieve consistent 19.2% efficiency with reduced standard deviation. This is key for industrial manufacturing [@Saliba2016].",
    prior=0.5,
)

# Strategy: Long-term stability demonstrated
strat_long_term_stability = support(
    [long_term_stability, high_performer_stability],
    triple_cation_versatility,
    reason="Cs5M maintains ~18% efficiency after 250 hours under operational conditions with a half-life of ~5000 hours, one of the highest for high-efficiency PSCs. This demonstrates industrial viability of triple cation perovskites [@Saliba2016].",
    prior=0.5,
)

# Strategy: Best device achieves 21.1%
strat_best_device = support(
    [best_stabilized_pce, fill_factor_degradation],
    triple_cation_versatility,
    reason="The best Cs5M device achieves 21.1% stabilized PCE under maximum power point tracking. Fill factors reach approximately 0.8, values rarely achieved. Most degradation comes from fill factor, not current or voltage [@Saliba2016].",
    prior=0.5,
)

# Strategy: Why pure compounds fail - structural instability
strat_pure_compounds_fail = support(
    [mapbi3_never_exceeded_20percent, mapbi3_phase_transition, fapi3_instability, cspbi3_bandgap],
    mixed_cations_design_principle,
    reason="Pure MAPbI3 never exceeds 20% due to phase transition at 55C, moisture degradation, and halide segregation. Pure FAPbI3 is unstable at room temperature, forming yellow phase. CsPbI3 black phase only stable above 300C. These limitations necessitate mixed cation approaches [@Saliba2016].",
    prior=0.5,
)

# Strategy: MA as partial crystallizer - but Cs is more effective
strat_ma_crystallizer_limitation = support(
    [ma_crystallizer, ma_induces_slowly, yellow_phase_impurities],
    triple_cation_strategy,
    reason="MA acts as crystallizer for FA perovskite but slowly, permitting yellow phase to persist. Cs has larger size difference from FA, inducing crystallization more effectively and suppressing yellow phase with small amounts [@Saliba2016].",
    prior=0.5,
)

# Strategy: Cs ionic radius enables effective tolerance factor tuning
strat_cs_tolerance_factor = support(
    [cs_ionic_radius, cs_effectively_promotes_black_phase],
    triple_cation_strategy,
    reason="Cs ionic radius (1.81A) is considerably smaller than MA (2.70A) or FA (2.79A). This large size difference allows Cs to effectively tune the Goldschmidt tolerance factor, pushing FA into the beneficial black perovskite phase [@Saliba2016].",
    prior=0.5,
)

# Strategy: Triple cation enables industrialization
strat_industrialization = support(
    [triple_cation_robustness, cs_benefits_summary, cs_benefits_reproducibility],
    industrialization_relevance,
    reason="Triple cation perovskites are thermally stable, less sensitive to processing variations, and enable reproducible high efficiency devices exceeding 20% on a regular basis. This robustness is essential for cost-efficient large-scale manufacturing of perovskite solar cells [@Saliba2016].",
    prior=0.5,
)

__all__ = [
    "strat_triple_cation_supports_high_efficiency",
    "strat_xrd_supports_cs_eliminates_impurities",
    "strat_cs_lattice_integration",
    "strat_cs_improves_thermal_stability",
    "strat_cs_enables_room_temp_formation",
    "strat_cs_reduces_temp_sensitivity",
    "strat_cs_improves_device_performance",
    "strat_cs_leads_to_monomorphic_grains",
    "strat_cs_improves_reproducibility",
    "strat_long_term_stability",
    "strat_best_device",
    "strat_pure_compounds_fail",
    "strat_ma_crystallizer_limitation",
    "strat_cs_tolerance_factor",
    "strat_industrialization",
]