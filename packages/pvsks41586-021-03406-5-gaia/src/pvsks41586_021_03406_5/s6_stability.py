"""
s6_stability.py - Stability test results.

This module covers the shelf-life, thermal, and operational stability
of reference and target (2% Fo-FAPbI3) PSC devices.
"""

from gaia.lang import (
    claim, setting, question, support, infer,
    contradiction, complement, equivalence, disjunction,
)

# =============================================================================
# Shelf-Life Stability Results
# =============================================================================

shelf_life_stability = claim(
    "Unencapsulated reference PSCs stored in dark at 25°C and 20% relative humidity showed "
    "a PCE decrease of about 35% after 1,000 hours of aging. In contrast, the target PSCs "
    "(2% Fo-FAPbI3) showed only about 10% degradation over the same period, demonstrating "
    "significantly improved shelf-life stability with formate addition [@Jeong2021].",
    title="Shelf-life stability results",
    metadata={"figure": "artifacts/images/2a0fa091b79d266fd962153db49416b6e7c753da39ba17017be5e5681d88b88f.jpg",
               "caption": "Fig. 4a | Shelf-life stability of reference and target PSCs"},
)

target_shelf_life_retains_90 = claim(
    "The target PSC retains approximately 90% of its initial PCE after 1,000 hours of "
    "shelf-life aging under ambient conditions (dark, 25°C, 20% RH), while the reference "
    "cell retains only about 65% of its initial PCE [@Jeong2021].",
    title="Target retains 90% vs reference 65% after 1000h",
)

# =============================================================================
# Thermal Stability Results
# =============================================================================

thermal_stability = claim(
    "Heat stability test performed by annealing unencapsulated PSC devices at 60°C under "
    "20% relative humidity shows that the target cell retained around 80% of its initial "
    "efficiency after 1,000 hours, whereas the reference cell retained only about 40% "
    "of its initial efficiency. This demonstrates substantially improved thermal stability "
    "with formate addition [@Jeong2021].",
    title="Thermal stability at 60°C results",
    metadata={"figure": "artifacts/images/a6d503fcb86065d4d35e71ffaa61096f8b8a508e1f1c8280591c883c3a28721c.jpg",
               "caption": "Fig. 4b | Heat stability of reference and target PSCs"},
)

target_heat_stability_80_percent = claim(
    "The target PSC maintains 80% of initial efficiency after 1,000 hours at 60°C and 20% RH, "
    "compared to only 40% for the reference PSC, representing a 2x improvement in thermal "
    "stability [@Jeong2021].",
    title="Target retains 80% vs reference 40% after heat aging",
)

# =============================================================================
# Operational Stability Results
# =============================================================================

operational_stability_short_term = claim(
    "Under continuous light soaking using a xenon lamp with MPP tracking in nitrogen "
    "atmosphere, the target PSC maintained PCE above 24% after 10 hours of operation, "
    "while the reference PSC decreased to 22.8%. This demonstrates improved short-term "
    "operational stability with formate treatment [@Jeong2021].",
    title="Short-term operational stability (10 hours)",
    metadata={"figure": "artifacts/images/60c7071eaf6553b45195f24875b5beb6a6ca2014cd1169b36ffd1210087dd60f.jpg",
               "caption": "Fig. 4c | Operational stability over 10 hours"},
)

long_term_operational_stability = claim(
    "Long-term operational stability test over 450 hours of MPP tracking shows that the "
    "PCE of the reference cell decreased by about 30%, while the target cell only lost "
    "around 15% of its initial efficiency. During this test the PSC temperature was around "
    "35°C due to illumination without cooling [@Jeong2021].",
    title="Long-term operational stability (450 hours)",
    metadata={"figure": "artifacts/images/7699c5d4b9c2da4ef7eb6b3291a5977e7c873de2c44d964781e0305eed7efc4a.jpg",
               "caption": "Fig. 4d | Long-term operational stability over 450 hours"},
)

reference_degradation_mechanism = claim(
    "During the 450-hour MPP tracking test, the reference perovskite layer showed "
    "considerable decrease in Jsc and fill factor, suggesting that the reference perovskite "
    "layer is less stable. The decline in fill factor is attributed to de-doping of the hole "
    "conductor due to Li+ ion migration under illumination [@Jeong2021].",
    title="Reference cell degradation mechanism",
)

# =============================================================================
# Stability Mechanism Interpretation
# =============================================================================

stability_from_crystallinity = claim(
    "The improvement in thermal and operational stability of the target cell compared to "
    "the reference cell is attributed to the better crystallinity of the perovskite film "
    "and reduced concentration of halide defects. NMR experiments confirm that formate "
    "is not incorporated into the bulk of the perovskite, but rather passivates surfaces "
    "and grain boundaries [@Jeong2021].",
    title="Stability improvement from crystallinity and reduced defects",
)

crystallinity_importance_stability = claim(
    "Crystallinity is crucial for perovskite stability because the main degradation process "
    "starts from defects near the grain boundaries. The high crystallinity and large grain "
    "size of formate-containing perovskite films (as validated by SEM and XRD measurements) "
    "contribute to greater stability and performance [@Jeong2021].",
    title="Crystallinity crucial for perovskite stability",
)

formate_binding_stability = claim(
    "MD simulations and DFT calculations show that formate anions have the highest binding "
    "affinity among all halides and pseudo-halides for iodide vacancy sites, making them the "
    "best candidates to eliminate the most abundant and deleterious lattice defects. This "
    "results in marked reduction of trap-mediated non-radiative recombination, which is "
    "validated by EQE_EL, time-resolved PL, ideality factor, and SCLC measurements [@Jeong2021].",
    title="Formate binding affinity eliminates defects for stability",
)

low_halide_vacancy_stability = claim(
    "A low level of halide vacancies is beneficial for the stability of solar cells because "
    "halide vacancies can lead to degradation as a result of photoinduced iodine loss, "
    "especially under light illumination. Formate passivation reduces halide vacancies, "
    "thereby improving operational stability under illumination [@Jeong2021].",
    title="Low halide vacancies prevent photoinduced iodine loss",
)

# =============================================================================
# Strategies
# =============================================================================

strat_formate_improves_shelf_life = support(
    [shelf_life_stability, target_shelf_life_retains_90],
    claim("Formate addition improves shelf-life stability 3.5x"),
    reason="Reference degrades 35% after 1000h while target only degrades 10%, representing "
    "a 3.5x improvement in shelf-life stability. This improvement is attributed to the "
    "combination of better crystallinity and reduced halide defects with formate passivation "
    "[@Jeong2021].",
    prior=0.5,
)

strat_formate_improves_thermal_stability = support(
    [thermal_stability, target_heat_stability_80_percent],
    claim("Formate addition improves thermal stability 2x"),
    reason="At 60°C and 20% RH for 1000 hours, target retains 80% vs reference 40% of initial "
    "PCE. The 2x improvement in thermal stability is attributed to improved crystallinity and "
    "reduced halide defect concentration from formate passivation [@Jeong2021].",
    prior=0.5,
)

strat_formate_improves_operational_stability = support(
    [long_term_operational_stability, reference_degradation_mechanism],
    claim("Formate addition improves operational stability 2x"),
    reason="Over 450 hours MPP tracking, target loses only 15% vs reference 30% of initial "
    "PCE. Reference degradation is linked to Jsc and FF decrease from perovskite instability "
    "(defects) and Li+ migration. Target's better crystallinity and reduced defects provide "
    "improved operational stability [@Jeong2021].",
    prior=0.5,
)

strat_stability_mechanism = support(
    [stability_from_crystallinity, crystallinity_importance_stability,
     formate_binding_stability, low_halide_vacancy_stability],
    claim("Stability improvements from formate passivation mechanism"),
    reason="Stability improvements (shelf-life 3.5x, thermal 2x, operational 2x) are explained "
    "by the combined effects of: (1) better crystallinity from slower crystal growth due to "
    "HCOO- coordination with Pb2+ in solution, (2) larger grain size reducing grain boundary "
    "defects, (3) reduced halide vacancy concentration from formate's highest binding affinity "
    "for I- vacancies, and (4) prevention of photoinduced iodine loss through defect elimination "
    "[@Jeong2021].",
    prior=0.5,
)

__all__ = [
    "shelf_life_stability",
    "target_shelf_life_retains_90",
    "thermal_stability",
    "target_heat_stability_80_percent",
    "operational_stability_short_term",
    "long_term_operational_stability",
    "reference_degradation_mechanism",
    "stability_from_crystallinity",
    "crystallinity_importance_stability",
    "formate_binding_stability",
    "low_halide_vacancy_stability",
    "strat_formate_improves_shelf_life",
    "strat_formate_improves_thermal_stability",
    "strat_formate_improves_operational_stability",
    "strat_stability_mechanism",
]