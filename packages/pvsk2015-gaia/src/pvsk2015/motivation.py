"""
Motivation module for Jeon2015 (Nature 2015).

This module covers the introduction and motivation sections of the paper:
"Compositional engineering of perovskite materials for high-performance solar cells"

Key topics:
- Perovskite material background (AMX3 structure)
- MAPbI3 vs FAPbI3 comparison
- Motivation for combining FAPbI3 (narrow bandgap) with MAPbBr3 (stability)
"""

from gaia.lang import (
    claim,
    setting,
    question,
)

# =============================================================================
# PEROVSKITE MATERIAL BACKGROUND (SETTING)
# =============================================================================

perovskite_structure = setting(
    "An inorganic-organic lead halide perovskite has the general formula AMX3, "
    "where A is an organic ammonium cation (such as MA or FA), M is Pb or Sn, "
    "and X is a halide anion. The size of cation A is critical for forming a "
    "close-packed perovskite structure; A must fit into the space composed of "
    "four adjacent corner-sharing MX6 octahedra.",
    title="AMX3 perovskite structure definition",
)

mapbi3_properties = claim(
    "Methylammonium lead iodide (MAPbI3) has a bandgap of approximately 1.5-1.6 eV "
    "and an absorption spectrum extending up to a wavelength of 800 nm. It has been "
    "extensively used as a light harvester in solar cells. The highest reported PCE "
    "for solution-processed MAPbI3 has been 16-17%, though 19.3% was reported in a "
    "planar device architecture from a reverse-bias current-voltage (I-V) curve "
    "[@Jeon2015].",
    title="MAPbI3 optoelectronic properties",
)

fapbi3_properties = claim(
    "Formamidinium lead iodide (FAPbI3), which contains FA cations instead of MA "
    "cations at the A-site of the AMX3 perovskite structure, has a bandgap of "
    "1.48 eV with an absorption edge at 840 nm. The structural and opto-electrical "
    "differences between MAPbI3 and FAPbI3 originate from the difference in ionic "
    "radius: MA is approximately 1.8 Angstrom, while FA is 1.9-2.2 Angstrom "
    "[@Jeon2015].",
    title="FAPbI3 optoelectronic properties",
)

# =============================================================================
# PROBLEM STATEMENT
# =============================================================================

fapbi3_phase_instability = claim(
    "The black perovskite-type polymorph (alpha-phase) of FAPbI3, which is stable "
    "at temperatures above 160 degrees Celsius, transforms into the yellow non-perovskite "
    "polymorph (delta-phase) in ambient humid atmosphere. This phase transition is "
    "reversible and degrades photovoltaic performance because the yellow phase has a "
    "larger optical bandgap and inferior charge-transporting ability due to its linear "
    "chain-like [PbI6] octahedron structure with face-sharing [@Jeon2015].",
    title="FAPbI3 phase instability problem",
)

fapbi3_lower_performance = claim(
    "The photovoltaic performance of FAPbI3 has been reported to be lower than that "
    "of MAPbI3, despite FAPbI3 having a more suitable bandgap for photovoltaic "
    "applications. The performance limitation is attributed to the phase instability "
    "and the need for high-temperature annealing to achieve the perovskite phase "
    "[@Jeon2015].",
    title="FAPbI3 performance limitation",
)

# =============================================================================
# RESEARCH QUESTION
# =============================================================================

research_question = question(
    "Can incorporating MAPbBr3 into FAPbI3 stabilize the perovskite phase at lower "
    "temperatures while improving the overall power conversion efficiency beyond "
    "the best reported values for MAPbI3 or FAPbI3 alone?"
)

# =============================================================================
# PRIOR WORK (EXTERNAL CONTEXT)
# =============================================================================

mixed_cation_pellet = claim(
    "Pellet et al. demonstrated improved PCE using mixed cation lead iodide perovskites "
    "by gradually substituting MA with FA cations, which increases the absorption range "
    "by shifting it redwards. However, the performance was still dominated by MAPbI3 "
    "rather than FAPbI3 [@Jeon2015].",
    title="Prior mixed cation work (Pellet)",
)

prior_work_seok = claim(
    "Jeon et al. previously reported a 16.2% certified PCE using a combination of "
    "MAPbI3 and MAPbBr3 with a bilayer architecture consisting of perovskite-infiltrated "
    "mesoporous-TiO2 electrodes and an extremely uniform and dense upper perovskite layer "
    "obtained by solvent engineering techniques, with absorption edge below 770 nm "
    "[@Jeon2015].",
    title="Prior work from same group (Seok)",
)

# =============================================================================
# TRANSPORT PROPERTIES (MOTIVATION)
# =============================================================================

mapbi3_transport = claim(
    "In MAPbI3, the electron-diffusion length is approximately 130 nm, which is 1.4 "
    "times larger than the hole-diffusion length of approximately 90 nm. This imbalance "
    "affects the photocurrent collection efficiency [@Jeon2015].",
    title="MAPbI3 charge transport properties",
)

fapbi3_transport = claim(
    "In FAPbI3, the hole-diffusion length is approximately 813 nm, which is 4.6 times "
    "longer than the electron-diffusion length of approximately 177 nm. This is the "
    "opposite transport imbalance compared to MAPbI3 [@Jeon2015].",
    title="FAPbI3 charge transport properties",
)

conductivity_type = claim(
    "Kanatzidis et al. showed by measuring the Seebeck coefficient that MAPbI3 and FAPbI3 "
    "display n-type and p-type character, respectively. This difference in majority "
    "carrier type influences the device behavior in different cell architectures "
    "[@Jeon2015].",
    title="MAPbI3 and FAPbI3 conductivity types",
)

__all__ = [
    "perovskite_structure",
    "mapbi3_properties",
    "fapbi3_properties",
    "fapbi3_phase_instability",
    "fapbi3_lower_performance",
    "research_question",
    "mixed_cation_pellet",
    "prior_work_seok",
    "mapbi3_transport",
    "fapbi3_transport",
    "conductivity_type",
]