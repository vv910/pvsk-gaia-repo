"""
Motivation and background for the Min2019 perovskite solar cell paper.

This module covers the introduction content: the motivation for stabilizing
alpha-phase FAPbI3 while maintaining its inherent narrow bandgap.
"""

from gaia.lang import (
    claim,
    setting,
    question,
    support,
    deduction,
    composite,
    compare,
    abduction,
    infer,
)

# -----------------------------------------------------------------------------
# Background settings (mathematical definitions, established principles)
# -----------------------------------------------------------------------------

perovskite_structure = setting(
    "Lead halide perovskites (LHPs) have the general formula ABX3, where A is a "
    "cation (e.g., FA+, MA+), B is a divalent metal (Pb2+), and X is a halide (I-). "
    "The Goldschmidt tolerance factor t predicts phase stability: t ~ 0.9 is optimal "
    "for the cubic black alpha-phase, with t > 1 favoring hexagonal delta-phase.",
    title="LHP structure and Goldschmidt tolerance factor",
)

fapbi3_bandgap = setting(
    "FAPbI3 (formamidinium lead triiodide, FA+ = H2N=CH-NH2+) has the narrowest "
    "bandgap among lead halide perovskites, ranging from 1.45 to 1.51 eV in thin films, "
    "broader solar-light absorption, and improved thermal stability compared to MAPbI3 "
    "because of its higher decomposition temperature.",
    title="FAPbI3 bandgap and thermal stability",
)

alpha_delta_transition = setting(
    "FAPbI3 readily transforms from the desired trigonal black alpha-phase into the "
    "undesired wide-bandgap delta-phase with hexagonal symmetry under ambient conditions "
    "at room temperature. The alpha-phase is metastable below 120C and converts to "
    "the thermodynamically stable delta-phase.",
    title="Alpha-delta phase transition in FAPbI3",
)

mixed_cation_problem = setting(
    "Mixed cation-anion approaches (FAxMA1-x, FA1-x-yMAxCry) stabilize alpha-FAPbI3 "
    "but introduce MA (reducing thermal stability), Br- (causing phase separation and "
    "bandgap widening), and Cs+ (requiring complex synthesis). These additions increase "
    "bandgap and reduce photon absorption, lowering current density.",
    title="Problems with mixed cation-anion stabilization",
)

mda_properties = setting(
    "Methylenediammonium (MDA2+, +H3N-CH2-NH3+) has an ionic radius of 262 pm, "
    "comparable to FA+ (256 pm), but differs in valence state (divalent vs monovalent). "
    "MDA has more hydrogen atoms than FA or MA, enabling more H-bonds with I- ions, "
    "which could provide structural stabilization at even smaller amounts than MA.",
    title="MDACl2 properties and ionic radius",
)

# -----------------------------------------------------------------------------
# Question
# -----------------------------------------------------------------------------

research_question = question(
    "Can the alpha-phase of FAPbI3 be stabilized using MDACl2 doping (without MA, Cs, "
    "or Br) while maintaining the inherent narrow bandgap of pristine FAPbI3, thereby "
    "achieving higher power conversion efficiency and improved stability compared to "
    "mixed-cation-anion stabilized control devices?"
)

# -----------------------------------------------------------------------------
# Independent background claims
# -----------------------------------------------------------------------------

mapbbr3_control_efficiency = claim(
    "A control device using FAPbI3 stabilized by MAPbBr3 (with 5 mol% MAPbBr3) "
    "achieves a PCE of approximately 23%, representing the highest efficiency among "
    "mp-TiO2-based PSCs reported at the time of this study [@Min2019].",
    title="MAPbBr3-stabilized control device efficiency",
)

fapbi3_stabilization_history = claim(
    "Prior approaches to alpha-FAPbI3 stabilization include: (1) mixing with MAPbBr3 "
    "(reaching >18% PCE in FAPbI3:MAPbBr3 0.85:0.15), (2) surface functionalization "
    "with phenylethylammonium lead iodide (PEAI), and (3) incorporating both Rb+ and "
    "Cs+. However, these methods still underperform compared to mixed cation approaches "
    "and face limitations in stability or efficiency.",
    title="Prior alpha-FAPbI3 stabilization approaches",
)

__all__ = [
    "perovskite_structure",
    "fapbi3_bandgap",
    "alpha_delta_transition",
    "mixed_cation_problem",
    "mda_properties",
    "research_question",
    "mapbbr3_control_efficiency",
    "fapbi3_stabilization_history",
]