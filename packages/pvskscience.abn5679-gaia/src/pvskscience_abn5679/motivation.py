"""
Motivation and Introduction

This module contains background context and research motivation for studying
perovskite solar cell stability and accelerated aging methods.
"""
from gaia.lang import claim, setting, question

# Background on PSC efficiency and stability challenges
psc_efficiency_exceeds_25 = claim(
    "Modern perovskite solar cells (PSCs) achieve power conversion efficiencies exceeding 25%, "
    "approaching commercial viability requirements.",
    title="PSC efficiencies exceed 25%"
)

t80_lifetime_thousand_hours = claim(
    "The most stable and efficient PSCs have reported T80 lifetimes of just a few hundred or "
    "thousand hours under continuous illumination, far below the >20-year lifetimes required "
    "for most commercial applications.",
    title="T80 lifetimes are insufficient for commercialization"
)

commercial_requirement_20_years = claim(
    "Most commercial PV applications require >20-year operational lifetimes.",
    title="Commercial lifetime requirement exceeds 20 years"
)

accelerated_aging_enables_rapid_screening = claim(
    "Accelerated aging tests can facilitate rapid PSC stability screening by quantifying "
    "lifetime acceleration factors that relate lifetimes under standard and elevated stress conditions.",
    title="Accelerated aging enables rapid stability screening"
)

psc_sensitivity_challenge = claim(
    "Developing robust acceleration factors for PSCs is challenging due to their complex "
    "sensitivities to temperature, light, and electrical bias.",
    title="PSC sensitivity to multiple stressors complicates AF development"
)

# Research objective
research_objective = claim(
    "This work uses elevated temperatures (up to 110°C) to quantify accelerated degradation of "
    "encapsulated CsPbI3 PSCs under constant illumination, and demonstrates that a 2D Cs2PbI2Cl2 "
    "capping layer stabilizes the interface while improving efficiency.",
    title="Research objective: quantify accelerated degradation and demonstrate interface stabilization"
)

# Device configuration choices
inorganic_cs_pbi3_chosen = claim(
    "Inorganic CsPbI3 was chosen as the photoabsorber to maximize thermal and photostability, "
    "despite slightly lower efficiencies compared to organic-inorganic hybrid perovskites.",
    title="Inorganic CsPbI3 chosen for stability"
)

capped_vs_uncapped_device_structure = claim(
    "Inorganic CsPbI3 PSCs were fabricated both with (capped) and without (uncapped) a 2D "
    "Cs2PbI2Cl2 layer between the CsPbI3 absorber and the CuSCN hole transport layer (HTL).",
    title="Capped and uncapped device configurations"
)

all_inorganic_stack_designed = setting(
    "The all-inorganic device stack includes TiO2, Al2O3, and CuSCN transport layers, "
    "as well as fluorinated tin oxide (FTO) and Cr/Au electrodes, designed to maximize "
    "thermal and photostability."
)

# Research questions
how_does_2d_capping_affect_stability = question(
    "How does the 2D Cs2PbI2Cl2 capping layer affect the operational stability of CsPbI3 PSCs "
    "under elevated temperature and constant illumination?"
)

what_is_intrinsic_lifetime = question(
    "What is the intrinsic operational lifetime of capped CsPbI3 PSCs under standard conditions "
    "(1 sun, 35°C)?"
)