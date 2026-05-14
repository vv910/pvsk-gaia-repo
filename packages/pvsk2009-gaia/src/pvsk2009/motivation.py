"""
Motivation and Introduction for pvsk2009.

This module covers the background context and main findings reported in
Kojima et al. (2009) - the first report of organometal halide perovskites
as visible-light sensitizers for photovoltaic cells.
"""

from gaia.lang import (
    claim,
    setting,
    question,
)

# Background: Dye-sensitized solar cell technology
dye_sensitized_tiO2_established = setting(
    "Dye-sensitized mesoscopic TiO2 films have been established as high-efficiency "
    "photoanodes for solar cells, suitable for vacuum-free printing processes and "
    "low-temperature TiO2 coating technology enabling thin, flexible plastic cells [@pvsk2009].",
    title="Dye-sensitized TiO2 as established photoanode technology",
)

# Limitation of organic sensitizers
organic_sensitizer_limitations = claim(
    "Organic sensitizers limit light-harvesting ability due to their low absorption "
    "coefficients and narrow absorption bands, restricting the efficiency of "
    "dye-sensitized photovoltaic cells [@pvsk2009].",
    title="Organic sensitizer limitations",
)

# Quantum dot approach and its limitations
quantum_dot_approach = claim(
    "Researchers have examined quantum dots (CdS, CdSe, PbS, InP, InAs) for photovoltaic "
    "cells in electrochemical and solid-state structures, but intense bandgap light "
    "absorption has not resulted in high performance due to significant losses in light "
    "utilization and/or charge separation at the semiconductor-sensitizer interface [@pvsk2009].",
    title="Quantum dot sensitizer limitations",
)

# Perovskite material properties
perovskite_optical_properties = setting(
    "The organometal halide perovskite compounds CH3NH3PbX3 (X = Br, I) have unique "
    "optical properties, excitonic properties, and electrical conductivity, and can be "
    "synthesized from abundant sources (Pb, C, N, and halogen) [@pvsk2009].",
    title="Perovskite material properties",
)

# Main finding: Perovskite sensitization of TiO2
perovskite_sensitization_demonstrated = claim(
    "Nanocrystalline perovskite particles (CH3NH3PbX3, X = Br, I) self-organized on TiO2 "
    "function as n-type semiconductors and efficiently sensitize TiO2 for visible-light "
    "conversion in photovoltaic cells [@pvsk2009].",
    title="Perovskite sensitization of TiO2 for visible-light conversion",
)

# Efficiency result for iodide cell
iodide_cell_efficiency = claim(
    "A CH3NH3PbI3-based photovoltaic cell achieved a power conversion efficiency of 3.81% "
    "under 100 mW/cm2 AM 1.5 simulated sunlight irradiation [@pvsk2009].",
    title="CH3NH3PbI3 cell efficiency 3.81%",
)

# High photovoltage result for bromide cell
bromide_cell_high_voltage = claim(
    "A CH3NH3PbBr3-based photovoltaic cell achieved a high open-circuit voltage (Voc) of "
    "0.96 V under 100 mW/cm2 AM 1.5 simulated sunlight irradiation [@pvsk2009].",
    title="CH3NH3PbBr3 cell Voc 0.96 V",
)

# Research question
research_question = question(
    "Can organometal halide perovskite compounds serve as effective visible-light "
    "sensitizers for photovoltaic cells, overcoming the limitations of organic sensitizers "
    "and quantum dots?"
)