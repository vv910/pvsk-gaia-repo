"""
Discussion module for Jeon2015 (Nature 2015).

This module covers the discussion, conclusions, and key implications
from the paper, including the synergetic effect mechanism and future directions.

Key conclusions:
- Co-substitution of MA+ and Br- stabilizes FAPbI3 perovskite at low temperature
- Optimal composition x=0.15 achieves PCE > 18%
- Certified 17.9% PCE (highest for perovskite solar cells at publication)
"""

from gaia.lang import (
    claim,
    setting,
    support,
    infer,
    contradiction,
)

# Import source claims for reasoning connections FIRST
from .s2_methods import (
    xrd_method,
    uvvis_method,
    sem_method,
    dsc_tga_method,
    eqe_method,
    jv_measurement,
    composition_system,
    device_architecture,
)

from .s3_results import (
    table1_photovoltaic_parameters,
    best_device_jv,
    certified_pce,
    jsc_maximum,
    voc_increases_with_x,
    ff_maximum,
    series_resistance,
    eqe_plateau,
    fapbi3_hysteresis,
    absorption_blue_shift,
    eqe_blue_shift,
    dsc_phase_transition,
    phase_reversibility,
    perovskite_polymorphs,
    xrd_nonperovskite_x0,
    xrd_perovskite_x15,
    synergetic_effect,
    fwhm_crystallinity,
    black_powder_only,
    sem_morphology_x0,
    sem_morphology_x15,
    hysteresis_80nm,
)

from .motivation import (
    mapbi3_transport,
    fapbi3_transport,
    conductivity_type,
    perovskite_structure,
    mapbi3_properties,
    fapbi3_properties,
    fapbi3_phase_instability,
    fapbi3_lower_performance,
    mixed_cation_pellet,
    prior_work_seok,
)

# =============================================================================
# KEY CONCLUSIONS FROM PAPER
# =============================================================================

main_conclusion = claim(
    "Incorporation of MAPbBr3 into FAPbI3 stabilizes the perovskite phase of FAPbI3 "
    "and improves the power conversion efficiency of the solar cell to more than 18% "
    "under standard illumination of 100 mW/cm^2 (AM1.5G). The optimal composition is "
    "(FAPbI3)0.85(MAPbBr3)0.15 with certified PCE of 17.9% [@Jeon2015].",
    title="Main conclusion: MAPbBr3 stabilizes FAPbI3 and improves PCE",
)

synergy_mechanism = claim(
    "The synergetic effect of simultaneous MA+ cation and Br- anion co-substitution "
    "into FAPbI3 at 15 mol% stabilizes the perovskite phase at 100 degrees Celsius. "
    "This is because the ionic radius of FA (1.9-2.2 Angstrom) is at the upper limit "
    "of what fits in the AMX3 structure, making it borderline unstable. The combined "
    "substitution at both A-site (FA to MA, smaller) and X-site (I to Br, smaller) "
    "relieves the structural strain and enables the perovskite phase to form at "
    "lower temperature. Neither MA+ nor Br- substitution alone achieves the same "
    "stabilization effect [@Jeon2015].",
    title="Mechanism of synergetic effect",
)

phase_stabilization_evidence = claim(
    "The perovskite phase stabilization caused by MAPbBr3 introduction was confirmed "
    "by: (1) XRD showing pure perovskite phase at room temperature for x=0.15, (2) DSC "
    "showing no endothermic peak (no phase transition) for x=0.15 powder, (3) black "
    "powder color at room temperature for x=0.15 (all other compositions remain yellow), "
    "and (4) smooth morphology with well-developed crystallites at x=0.15 vs rough "
    "surface at x=0 [@Jeon2015].",
    title="Evidence for perovskite phase stabilization",
)

morphology_improvement = claim(
    "Manipulating the composition of FAPbI3 by adding MAPbBr3 leads to stabilization "
    "of the perovskite phase with a uniform and dense morphology as well as well-developed "
    "crystallites. These morphological improvements are responsible for the highly improved "
    "cell performance, alongside the electrical benefits of balanced charge transport "
    "[@Jeon2015].",
    title="Morphology improvement with MAPbBr3",
)

bandgap_tuning_tradeoff = claim(
    "The composition (FAPbI3)1-x(MAPbBr3)x allows bandgap tuning across the range. "
    "As x increases: Voc increases due to bandgap widening (from 1.00 V at x=0.05 to "
    "1.12 V at x=0.30), but Jsc decreases above x=0.15 due to blue-shifted absorption "
    "onset reducing light harvesting. The optimal balance is achieved at x=0.15, "
    "maximizing overall PCE to 17.3% (average) and 18.4% (best cell) [@Jeon2015].",
    title="Bandgap tuning creates performance tradeoff",
)

hysteresis_benefit = claim(
    "FAPbI3/MAPbBr3 cells exhibit negligible hysteresis even at short scan times "
    "(40 ms), unlike MAPbI3 cells. This advantage is attributed to the better balance "
    "between electron and hole transport in the mixed-cation system: FAPbI3 has "
    "p-type character with long hole-diffusion length (813 nm), while MAPbI3 has "
    "n-type character with shorter electron-diffusion length. In the bilayer "
    "architecture with light entering through FTO/TiO2, this transport balance "
    "reduces hysteresis [@Jeon2015].",
    title="Mixed system has reduced hysteresis",
)

# =============================================================================
# COMPARISON WITH PRIOR WORK
# =============================================================================

comparison_mapbi3 = claim(
    "(FAPbI3)0.85(MAPbBr3)0.15 has advantages over pure MAPbI3 including: (1) narrower "
    "bandgap (broader absorption, higher potential Jsc), (2) higher Voc due to "
    "bandgap tunability, (3) negligible hysteresis vs large hysteresis for MAPbI3, "
    "(4) certified 17.9% PCE vs previous best of 16-17% for MAPbI3. Pure FAPbI3 alone "
    "cannot achieve high performance due to phase instability requiring high-temperature "
    "processing [@Jeon2015].",
    title="Comparison with MAPbI3 performance",
)

comparison_fapbi3 = claim(
    "Pure FAPbI3 shows poor performance (PCE 0.5% at 100 C annealing) because it "
    "forms the yellow non-perovskite phase at low temperatures, requiring 150 C "
    "annealing to achieve 13.5% PCE. The co-substitution approach enables 18.4% PCE "
    "at only 100 C annealing, demonstrating the critical importance of phase "
    "stabilization for high performance [@Jeon2015].",
    title="Comparison with pure FAPbI3 performance",
)

comparison_prior_mixed = claim(
    "The (FAPbI3)0.85(MAPbBr3)0.15 composition differs from prior mixed-cation work "
    "(e.g., Pellet et al.) by simultaneously substituting both the A-site (FA to MA) "
    "and X-site (I to Br), whereas prior work only substituted A-site. The dual "
    "substitution creates the synergetic stabilization effect that enables high "
    "performance at low processing temperature [@Jeon2015].",
    title="Comparison with prior mixed-cation approaches",
)

# =============================================================================
# FUTURE IMPLICATIONS
# =============================================================================

future_potential = claim(
    "The strategy of compositional engineering through simultaneous cation and anion "
    "co-substitution may lead to more efficient and cost-effective inorganic-organic "
    "hybrid perovskite solar cells. The approach demonstrates that fine-tuning "
    "composition can simultaneously optimize multiple device parameters including "
    "phase stability, morphology, bandgap, and charge transport balance [@Jeon2015].",
    title="Future potential of compositional engineering",
)

understanding_phase_stability = claim(
    "The finding that AMX3 materials exist as either two polymorphs (perovskite and "
    "non-perovskite) or only one depending on the atomic size of components suggests "
    "a general design principle: combining multiple size-tuning substituents at "
    "different crystallographic sites can stabilize the desired perovskite phase. "
    "This understanding applies to other perovskite systems beyond FAPbI3 [@Jeon2015].",
    title="General principle for perovskite phase stability",
)

need_further_study = claim(
    "Further investigation is required to determine the energetics of perovskite and "
    "non-perovskite formation and to establish the composition of the stable form in "
    "perovskite halide materials. Understanding the fundamental thermodynamic and "
    "kinetic factors will enable rational design of even better compositions "
    "[@Jeon2015].",
    title="Areas requiring further investigation",
)

# =============================================================================
# REASONING CONNECTIONS (Pass 2: Connect)
# =============================================================================

# Main conclusion supported by multiple evidence streams
strat_main_conclusion = support(
    [phase_stabilization_evidence, morphology_improvement, bandgap_tuning_tradeoff],
    main_conclusion,
    reason="The phase stabilization evidence (XRD, DSC, powder color), morphology improvement (SEM), and photovoltaic performance data (PCE trend with x) all jointly support that MAPbBr3 incorporation stabilizes FAPbI3 and improves efficiency.",
    prior=0.5,
)

# Phase stabilization from multiple experimental observations
strat_phase_evidence = support(
    [xrd_perovskite_x15, dsc_phase_transition, black_powder_only],
    phase_stabilization_evidence,
    reason="XRD shows perovskite phase at 100C for x=0.15, DSC shows no phase transition, and black powder forms at room temperature for x=0.15 - all confirm phase stabilization.",
    prior=0.5,
)

# Morphology improvement from SEM evidence
strat_morphology_evidence = support(
    [sem_morphology_x15, sem_morphology_x0],
    morphology_improvement,
    reason="SEM shows smooth uniform morphology at x=0.15 vs rough irregular morphology at x=0, confirming improved surface coverage.",
    prior=0.5,
)

# PCE trend from photovoltaic data
strat_pce_trend = support(
    [table1_photovoltaic_parameters, best_device_jv, certified_pce],
    bandgap_tuning_tradeoff,
    reason="Table 1 shows PCE peaks at x=0.15 (17.3% average, 18.4% best), certified 17.9%, and performance declines at higher x due to blue-shifted absorption.",
    prior=0.5,
)

# Synergy mechanism explains dual substitution effect
strat_synergy = support(
    [synergetic_effect],
    synergy_mechanism,
    reason="The experimental observation that only co-substitution (MA+ and Br-) produces pure perovskite phase at low temperature supports the synergy mechanism explanation.",
    prior=0.5,
)

# Hysteresis benefit from transport properties
strat_hysteresis = support(
    [fapbi3_hysteresis, mapbi3_transport, fapbi3_transport, conductivity_type],
    hysteresis_benefit,
    reason="Transport properties (electron/hole diffusion lengths) and conductivity type explain why FAPbI3/MAPbBr3 has less hysteresis than MAPbI3.",
    prior=0.5,
)

# J-V measurement consistency
strat_jv_consistency = support(
    [best_device_jv, eqe_plateau],
    certified_pce,
    reason="The best device's J-V curves and EQE-integrated Jsc agree, supporting the certified PCE validity.",
    prior=0.5,
)

# Phase polymorph evidence supports instability claim
strat_polymorph_evidence = support(
    [perovskite_polymorphs, phase_reversibility],
    fapbi3_phase_instability,
    reason="The two polymorph structures (perovskite vs non-perovskite) and reversible phase transition under ambient conditions explain FAPbI3 instability.",
    prior=0.5,
)

# Comparison with MAPbI3
strat_compare_mapbi3 = support(
    [main_conclusion, hysteresis_benefit],
    comparison_mapbi3,
    reason="The mixed cation system's certified 17.9% PCE and negligible hysteresis directly compare favorably to MAPbI3 performance limitations.",
    prior=0.5,
)

# Comparison with pure FAPbI3
strat_compare_fapbi3 = support(
    [fapbi3_phase_instability, main_conclusion],
    comparison_fapbi3,
    reason="The phase instability of pure FAPbI3 at low temperature vs the stabilized performance at x=0.15 demonstrates the critical importance of the co-substitution approach.",
    prior=0.5,
)

__all__ = [
    "main_conclusion",
    "synergy_mechanism",
    "phase_stabilization_evidence",
    "morphology_improvement",
    "bandgap_tuning_tradeoff",
    "hysteresis_benefit",
    "comparison_mapbi3",
    "comparison_fapbi3",
    "comparison_prior_mixed",
    "future_potential",
    "understanding_phase_stability",
    "need_further_study",
    # reasoning strategies
    "strat_main_conclusion",
    "strat_phase_evidence",
    "strat_morphology_evidence",
    "strat_pce_trend",
    "strat_synergy",
    "strat_hysteresis",
    "strat_jv_consistency",
    "strat_polymorph_evidence",
    "strat_compare_mapbi3",
    "strat_compare_fapbi3",
]