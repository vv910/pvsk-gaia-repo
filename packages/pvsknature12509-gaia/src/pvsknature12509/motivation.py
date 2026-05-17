"""
Motivation module for Liu et al. 2013 Nature paper.

Paper: Efficient planar heterojunction perovskite solar cells by vapour deposition
Citation: [@Liu2013]

This module covers the introduction and motivation sections.
"""

from gaia.lang import (
    claim,
    setting,
    question,
    support,
    infer,
)

# Background on photovoltaic technologies
photovoltaic_generations = claim(
    "The photovoltaic technology landscape comprises: (1) wafer-based first-generation devices, "
    "(2) thin-film solid semiconductor absorber layers sandwiched between charge-selective contacts, "
    "and (3) nanostructured/mesostructured solar cells relying on distributed heterojunctions [@Liu2013].",
    title="Photovoltaic technology generations",
)

# Organometal halide perovskites as promising materials
perovskite_material_introduction = claim(
    "Organometal trihalide perovskites with general formula (RNH3)BX3 (R = CnH2n+1, X = I, Br, or Cl, B = Pb or Sn) "
    "have recently emerged as promising materials for high-efficiency nanostructured devices [@Liu2013].",
    title="Organometal halide perovskite introduction",
)

# Previous meso-superstructured solar cell work
meso_superstructured_improvement = claim(
    "Replacing mesoporous TiO2 with mesoporous Al2O3 in perovskite solar cells resulted in significant "
    "efficiency improvement, delivering open-circuit voltage exceeding 1.1 V in a 'meso-superstructured solar cell' [@Liu2013].",
    title="Meso-superstructured solar cell improvement",
)

meso_superstructured_mechanism = claim(
    "The observed enhancement in open-circuit voltage in meso-superstructured cells is due to confinement "
    "of photo-excited electrons within the perovskite phase, thereby increasing the splitting of quasi-Fermi "
    "levels for electrons and holes under illumination [@Liu2013].",
    title="Meso-superstructured open-circuit voltage mechanism",
)

# Efficiency progress leading to this work
meso_efficiency_progress = claim(
    "Further removal of thermal sintering of mesoporous Al2O3 layer and better optimization of processing "
    "led to meso-superstructured solar cells exceeding 12% efficiency [@Liu2013].",
    title="Meso-superstructured efficiency progress",
)

# Solution-processed planar heterojunction as precursor
solution_planarHeterojunction = claim(
    "CH3NH3PbI3-xClx can operate relatively efficiently as a thin-film absorber in a solution-processed "
    "planar heterojunction solar cell configuration, delivering approximately 5% efficiency when no mesostructure is involved [@Liu2013].",
    title="Solution-processed planar heterojunction efficiency",
)

# Research question
planar_vs_meso_question = question(
    "Is mesostructure essential for the highest efficiencies with perovskite absorbers, "
    "or can a simplified thin-film planar heterojunction lead to superior technology? [@Liu2013]",
    title="Planar vs mesostructure efficiency question",
)

# Key finding from this work
high_efficiency_planar_demonstrated = claim(
    "A simple planar heterojunction solar cell incorporating vapour-deposited perovskite as the absorbing layer "
    "can achieve solar-to-electrical power conversion efficiencies exceeding 15% under simulated full sunlight [@Liu2013].",
    title="High-efficiency planar heterojunction demonstration",
)

# Device architecture description
device_architecture_description = claim(
    "The planar heterojunction p-i-n solar cell is constructed from the light-incident side: "
    "FTO-coated glass / compact n-type TiO2 (electron-selective contact) / perovskite layer / "
    "p-type spiro-OMeTAD (hole conductor) / silver cathode [@Liu2013].",
    title="Planar heterojunction device architecture",
)

# Vapour deposition advantage
vapour_deposition_enables_uniform_films = claim(
    "Dual-source vapour deposition creates uniform flat films of the mixed halide perovskite CH3NH3PbI3-xClx "
    "with superior uniformity over multiple length scales compared to solution processing [@Liu2013].",
    title="Vapour deposition creates uniform films",
)

# Rationale for this study
study_rationale = claim(
    "The purpose of this study was to understand and optimize the properties of the vapour-deposited perovskite "
    "absorber layer, while using solution-processed compact TiO2 and spiro-OMeTAD hole transporter (as is usual "
    "in meso-superstructured solar cells) to isolate the variable of interest [@Liu2013].",
    title="Study rationale for focusing on vapour-deposited absorber",
)