"""
Motivation module for Azmi et al. 2022 paper on damp heat-stable PSCs.

This module covers the Introduction section, establishing the motivation,
problem statement, and key research gap addressed by the paper.
"""

from gaia.lang import claim, setting, question

# -----------------------------------------------------------------------------
# Research context and motivation
# -----------------------------------------------------------------------------

commercial_lifetime_requirement = claim(
    "Commercial photovoltaic technology requires a guaranteed product lifetime "
    "of at least 25 to 30 years, as is common for conventional crystalline silicon "
    "(c-Si) PV modules [@Azmi2022].",
    title="Commercial PV lifetime requirement",
)

damp_heat_test_standard = claim(
    "The IEC 61215:2016 damp-heat test at 85 degrees Celsius and 85% relative "
    "humidity is the standard for verifying stability of commercial PV modules. "
    "A stabilized PCE performing like a commercial c-Si solar cell (PCE ~20%) would "
    "need to pass this test for >1000 hours with <5% relative loss in PCE [@Azmi2022].",
    title="IEC damp-heat test standard",
)

pscs_main_challenge = claim(
    "After the demonstration of excellent power conversion efficiencies (PCEs) "
    "of perovskite solar cells (PSCs), the main challenge toward market entry is "
    "successfully passing standard industrial lifetime assessment tests, particularly "
    "the damp-heat test [@Azmi2022].",
    title="PSCs main challenge is stability",
)

perovskite_instability_mechanism = claim(
    "The instability of 3D perovskite films used as the photoactive absorber layer "
    "in PSCs is mainly attributed to high defect densities as well as ion migration "
    "at grain boundaries and interfaces, which is exacerbated at higher operational "
    "temperatures [@Azmi2022].",
    title="Perovskite instability mechanisms",
)

defect_passivation_strategy = claim(
    "Growing 2D perovskite layers on the top surface of 3D perovskites creates a "
    "2D/3D perovskite heterojunction that can effectively passivate surface defects "
    "and suppress ion migration, thereby enhancing PCE and lifetime [@Azmi2022].",
    title="2D/3D heterojunction passivation strategy",
)

# -----------------------------------------------------------------------------
# The persistent challenge
# -----------------------------------------------------------------------------

inverted_pscs_passivation_challenge = claim(
    "For 'inverted' PSCs, top-contact passivation at the electron-selective side "
    "has consistently failed in both PCE and lifetime -- this represents a persistent "
    "challenge in the perovskite community, despite inverted PSCs being easier to "
    "fabricate and scale up [@Azmi2022].",
    title="Inverted PSCs passivation challenge",
)

c60_weak_bonding = claim(
    "C60 is only weakly bonded to perovskite layers, which induces high energetic "
    "disorder between perovskite and C60 layers that limits device performance at "
    "elevated operating temperatures. A thin C60 layer is also insufficient to "
    "protect the 3D perovskite film from moisture or oxygen ingress [@Azmi2022].",
    title="C60 limitations at electron-selective interface",
)

# -----------------------------------------------------------------------------
# Research gap and solution approach
# -----------------------------------------------------------------------------

research_gap = claim(
    "The electron-selective interface of inverted PSCs has been frequently ignored "
    "because it was assumed that C60 provides sufficient passivation. Attention "
    "has predominantly focused on the hole-selective interface at the transparent "
    "bottom contact, leaving the electron-selective interface understudied "
    "[@Azmi2022].",
    title="Electron-selective interface understudied",
)

proposed_solution = claim(
    "Implementing 2D perovskite passivation layers formed with oleylammonium iodide "
    "(OLAI) molecules at the electron-selective interface can solve the issues of "
    "weak C60 bonding, energetic disorder, and insufficient protection against "
    "moisture/oxygen ingress [@Azmi2022].",
    title="OLAI 2D perovskite passivation solution",
)

dimensionality_tailoring_key = claim(
    "Tailoring the dimensionality (n) of the 2D perovskite fragments at the "
    "electron-selective interface of inverted PSCs is essential to enable efficient "
    "top-contact passivation. Higher-n layers have lower formation energy and better "
    "electronic properties [@Azmi2022].",
    title="Dimensionality tailoring is key",
)

room_temp_vs_thermal_annealing = claim(
    "2D perovskite passivation layers prepared through thermal annealing (2D-TA) "
    "show dominant n=1 emission, while room-temperature treatment (2D-RT) with OLAI "
    "produces higher-dimensionality layers (n >= 2) more effectively [@Azmi2022].",
    title="Room-temperature processing enables higher n",
)