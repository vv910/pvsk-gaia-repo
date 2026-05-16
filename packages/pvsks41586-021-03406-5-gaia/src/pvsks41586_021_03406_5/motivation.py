"""
motivation.py - Introduction and motivation for pseudo-halide anion engineering.

This module covers the background on perovskite solar cells (PSCs),
the challenges with FAPbI3, and the motivation for using formate (HCOO-) engineering.
"""

from gaia.lang import (
    claim, setting, question, support, infer,
    contradiction, complement, equivalence, disjunction,
)

# =============================================================================
# Perovskite Solar Cell Background
# =============================================================================

perovskite_general_formula = setting(
    "Metal halide perovskites have the general formula ABX3, where A is a monovalent "
    "cation (e.g., caesium, methylammonium, or formamidinium), B is a divalent metal "
    "(e.g., lead, tin, or germanium), and X is a halide anion [@Jeong2021].",
    title="Perovskite general formula ABX3",
)

fapbi3_emergence = claim(
    "Among many perovskite compositions, cubic α-phase formamidinium lead triiodide "
    "(FAPbI3) has emerged as the most promising semiconductor for highly efficient "
    "and stable perovskite solar cells, due to its optimal bandgap and thermal stability [@Jeong2021].",
    title="FAPbI3 as most promising perovskite",
)

psc_research_drivers = claim(
    "PSCs have attracted much attention since 2009, driven by low-cost solution processing "
    "and attractive optoelectronic properties including tunable bandgap, high absorption "
    "coefficient, low recombination rate, and high charge carrier mobility [@Jeong2021].",
    title="PSC research drivers",
)

pce_progress = claim(
    "Within a decade, the power conversion efficiency (PCE) of single-junction PSCs progressed "
    "from 3% to a certified value of 25.5%, the highest value obtained for thin-film photovoltaics [@Jeong2021].",
    title="PSC efficiency progression to 25.5%",
)

operational_stability_progress = claim(
    "Through additive and interface engineering strategies, the long-term operational stability "
    "of PSCs now exceeds 1,000 hours in full sunlight, making them promising for deployment [@Jeong2021].",
    title="PSC operational stability exceeds 1000h",
)

# =============================================================================
# Challenges with FAPbI3
# =============================================================================

compositional_engineering_importance = claim(
    "Compositional engineering plays a key role in achieving highly efficient and stable PSCs. "
    "Mixtures of MAPbI3 with FAPbI3 have been extensively studied because FAPbI3 is thermally "
    "more stable and has a bandgap closer to the Shockley-Queisser limit [@Jeong2021].",
    title="Compositional engineering importance",
)

fapbi3_phase_transition_problem = claim(
    "Thin FAPbI3 films undergo a phase transition from the black α-phase to a photoinactive "
    "yellow δ-phase below 150°C, which is a major problem for device stability [@Jeong2021].",
    title="FAPbI3 phase transition problem",
)

previous_mixture_approaches = claim(
    "Previous approaches to stabilize α-FAPbI3 used mixtures of MA+, Cs+, and Br- ions, "
    "but this comes at the cost of blue-shifted absorbance and phase segregation under "
    "operational conditions [@Jeong2021].",
    title="Previous mixture approaches cause issues",
)

alpha_fapbi3_candidate = claim(
    "Pure α-FAPbI3 has emerged as the candidate of choice for highly efficient and stable PSCs, "
    "addressing the issues of previous mixed-cation approaches [@Jeong2021].",
    title="Pure α-FAPbI3 as optimal candidate",
)

prior_efficiency_record = claim(
    "Using MACl additive in FAPbI3 precursor solution, a certified efficiency of 23.48% was "
    "achieved for mesoporous FAPbI3 PSCs, with further optimization reaching 23.73% - approaching "
    "the theoretical maximum [@Jeong2021].",
    title="Prior FAPbI3 efficiency record 23.73%",
)

voc_lag = claim(
    "The open-circuit voltage (Voc) of around 1.15 V for FAPbI3 PSCs still lags behind the "
    "radiative limit, suggesting that more work is needed to reduce defect density and suppress "
    "non-radiative recombination of charge carriers [@Jeong2021].",
    title="Voc lags behind radiative limit",
)

# =============================================================================
# Formate Engineering Introduction
# =============================================================================

previous_anion_engineering = claim(
    "Bromide, chloride (Cl-), and thiocyanate (SCN-) anions have commonly been used to improve "
    "crystallinity and stability of perovskite films [@Jeong2021].",
    title="Previous anion engineering with Br, Cl, SCN",
)

formate_previous_studies = claim(
    "Formate (HCOO-) has been investigated in MAPbI3 PSCs, where previous studies showed that "
    "MAHCOO improves film quality by controlling crystal growth, and formic acid accelerates "
    "crystallization. However, these studies focused mainly on morphology and nucleation [@Jeong2021].",
    title="Previous formate studies on MAPbI3",
)

# =============================================================================
# Key Hypothesis and Results
# =============================================================================

key_role_of_formate = claim(
    "HCOO- anions play a key role in removing halide vacancies, which are the predominant "
    "lattice defects in FAPbI3 perovskite films, enabling PCE to exceed 25% with high "
    "operational stability and EQE_EL exceeding 10% [@Jeong2021].",
    title="HCOO- removes halide vacancies",
)

formate_size_fits_vacancy = claim(
    "Formate is small enough to fit into iodide vacancies, thereby eliminating this prevalent "
    "and notorious defect that accelerates non-radiative recombination, decreasing both "
    "fill factor and Voc of solar cells [@Jeong2021].",
    title="Formate fits iodide vacancy size",
)

defect_passivation_crystallinity = claim(
    "The combination of defect passivation and improved crystallinity from 2% FAHCOO addition "
    "is essential to attain the high efficiency and stability demonstrated by the target PSCs [@Jeong2021].",
    title="Defect passivation + improved crystallinity",
)

# =============================================================================
# Research Questions
# =============================================================================

research_question_mechanism = question(
    "What is the fundamental mechanism by which HCOO- anions passivate iodide vacancies "
    "in FAPbI3 perovskite films?"
)

research_question_performance = question(
    "Can pseudo-halide anion engineering with formate enable FAPbI3 PSCs to exceed 25% PCE "
    "while maintaining high operational stability?"
)

# =============================================================================
# Strategies
# =============================================================================

strat_background_supports_problem = support(
    [fapbi3_emergence, pce_progress, voc_lag],
    formate_size_fits_vacancy,
    reason="The emergence of FAPbI3 as the most promising perovskite, combined with the progress "
    "in efficiency to 25.5% but persistent Voc lag behind radiative limits, motivates the search "
    "for defect passivation strategies. The key insight is that formate is small enough to fit "
    "into iodide vacancies - a structural fact that enables the passivation mechanism proposed "
    "in this work [@Jeong2021].",
    prior=0.5,
)

strat_previous_work_supports_formate = support(
    [previous_anion_engineering, formate_previous_studies],
    key_role_of_formate,
    reason="Previous anion engineering with Br, Cl, SCN established that anion passivation "
    "improves perovskite films. Prior formate studies on MAPbI3 showed effects on morphology "
    "and crystallization, but this paper extends understanding to show formate specifically "
    "removes halide vacancies - the predominant lattice defects in FAPbI3 - enabling PCE "
    "exceeding 25% with high stability [@Jeong2021].",
    prior=0.5,
)

strat_phase_problem_motivates_solution = support(
    [fapbi3_phase_transition_problem, previous_mixture_approaches, alpha_fapbi3_candidate],
    defect_passivation_crystallinity,
    reason="The phase transition problem (α to δ below 150°C) and the issues with previous "
    "mixture approaches (phase segregation) drove the search for a different solution. "
    "The emergence of pure α-FAPbI3 as the optimal candidate motivated exploring formate "
    "engineering as a way to both passivate defects and improve crystallinity without "
    "introducing phase segregation problems [@Jeong2021].",
    prior=0.5,
)

__all__ = [
    "perovskite_general_formula",
    "fapbi3_emergence",
    "psc_research_drivers",
    "pce_progress",
    "operational_stability_progress",
    "compositional_engineering_importance",
    "fapbi3_phase_transition_problem",
    "previous_mixture_approaches",
    "alpha_fapbi3_candidate",
    "prior_efficiency_record",
    "voc_lag",
    "previous_anion_engineering",
    "formate_previous_studies",
    "key_role_of_formate",
    "formate_size_fits_vacancy",
    "defect_passivation_crystallinity",
    "research_question_mechanism",
    "research_question_performance",
    "strat_background_supports_problem",
    "strat_previous_work_supports_formate",
    "strat_phase_problem_motivates_solution",
]