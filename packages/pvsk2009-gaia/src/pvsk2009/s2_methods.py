"""
Methods for pvsk2009 - Experimental procedures and characterization.

This module covers the photoelectrode preparation, perovskite deposition,
cell construction, and measurement techniques reported in Kojima et al. (2009).
"""

from gaia.lang import (
    claim,
    setting,
)

# Substrate and TiO2 buffer layer preparation
fto_substrate_preparation = setting(
    "Fluorine-doped SnO2 transparent conductive glass (FTO, 10 ohm/sq) was used as "
    "substrate, pretreated by soaking in 40 mM TiCl4 aqueous solution at 70C for 30 min "
    "to form a thin TiO2 buffer layer [@pvsk2009].",
    title="FTO substrate and TiO2 buffer layer preparation",
)

# TiO2 mesoporous film preparation
tiO2_mesoporous_film = setting(
    "A mesoporous TiO2 film (n-type semiconductor) was prepared on the above-treated FTO "
    "by coating with a commercial nanocrystalline TiO2 paste using a screen printer and "
    "sintering at 480C for 1 h in air, resulting in a film thickness of 8-12 um [@pvsk2009].",
    title="TiO2 mesoporous film preparation",
)

# Optimal TiO2 thickness for short-circuit photocurrent
tiO2_thickness_optimization = claim(
    "Maximum short-circuit photocurrent density (Jsc) occurred with 8 um TiO2 thickness "
    "for CH3NH3PbI3/TiO2 and 12 um for CH3NH3PbBr3/TiO2 [@pvsk2009].",
    title="Optimal TiO2 thickness for Jsc",
)

# Perovskite precursor synthesis - bromide
bromide_precursor_synthesis = setting(
    "CH3NH3Br was synthesized from HBr and 40% methylamine in methanol solution followed "
    "by recrystallization. For CH3NH3PbBr3, a 20 wt% precursor solution of CH3NH3Br and "
    "PbBr2 in N,N-dimethylformamide was used [@pvsk2009].",
    title="Bromide perovskite precursor synthesis",
)

# Perovskite precursor synthesis - iodide
iodide_precursor_synthesis = setting(
    "CH3NH3I was synthesized from HI and 40% methylamine in methanol solution followed by "
    "recrystallization. For CH3NH3PbI3, an 8 wt% precursor solution of CH3NH3I and PbI2 "
    "in gamma-butyrolactone was employed [@pvsk2009].",
    title="Iodide perovskite precursor synthesis",
)

# Perovskite deposition method
perovskite_self_organization = setting(
    "Nanocrystalline particles of CH3NH3PbX3 (X = Br, I) were deposited on the TiO2 "
    "surface by a self-organization process: precursor solution coating followed by "
    "spin-coating and drying, during which the liquid precursor film changed color "
    "indicating perovskite formation in the solid state. CH3NH3PbBr3 changed from "
    "colorless to yellow; CH3NH3PbI3 changed from yellowish to black [@pvsk2009].",
    title="Perovskite self-organization deposition process",
)

# Crystal structure characterization - cubic perovskite for bromide
bromide_cubic_structure = claim(
    "CH3NH3PbBr3 has a cubic perovskite structure with lattice constant a = 5.9 Angstrom, "
    "exhibiting X-ray diffraction peaks at 14.77, 20.97, 29.95, 42.9, and 45.74 degrees "
    "assigned as the (100), (110), (200), (220), and (300) planes respectively [@pvsk2009].",
    title="CH3NH3PbBr3 cubic perovskite structure",
)

# Crystal structure characterization - tetragonal perovskite for iodide
iodide_tetragonal_structure = claim(
    "CH3NH3PbI3 has a tetragonal perovskite structure with lattice parameters a = 8.855 "
    "Angstrom and c = 12.659 Angstrom, exhibiting X-ray diffraction peaks at 14.00 and "
    "28.36 degrees for the (110) and (220) planes respectively [@pvsk2009].",
    title="CH3NH3PbI3 tetragonal perovskite structure",
)

# SEM observation of bromide particles
bromide_particle_size = claim(
    "Scanning electron microscopy observation of CH3NH3PbBr3-deposited TiO2 showed "
    "nanosized particles (2-3 nm) existing on the TiO2 surface, as indicated by the "
    "arrow in Figure 1b with a scale bar of 10 nm [@pvsk2009].",
    title="CH3NH3PbBr3 nanoparticle size 2-3 nm",
    metadata={"figure": "artifacts/images/4f7634ba7feab2e29c785a996f9a09ff5696940ffb186832ca44cbdd52526f3b.jpg",
             "caption": "Fig. 1b | SEM image of CH3NH3PbBr3 nanoparticles on TiO2"},
)

# Cell construction
cell_construction = setting(
    "The photovoltaic cell was constructed by combining the CH3NH3PbX3/TiO2 electrode "
    "(photoelectrode/anode) and a Pt-coated FTO glass counter electrode (cathode) with "
    "insertion of a 50 um thick separator film. The electrode gap was filled with an "
    "organic electrolyte solution containing lithium halide and halogen as a redox couple "
    "[@pvsk2009].",
    title="Photovoltaic cell construction",
)

# Bromide cell electrolyte
bromide_electrolyte = setting(
    "The CH3NH3PbBr3/TiO2-based cell employed an electrolyte consisting of 0.4 M LiBr "
    "and 0.04 M Br2 dissolved in acetonitrile [@pvsk2009].",
    title="Bromide cell electrolyte composition",
)

# Iodide cell electrolyte
iodide_electrolyte = setting(
    "The CH3NH3PbI3/TiO2-based cell employed an electrolyte consisting of 0.15 M LiI "
    "and 0.075 M I2 dissolved in methoxyacetonitrile [@pvsk2009].",
    title="Iodide cell electrolyte composition",
)

# Measurement setup
measurement_setup = setting(
    "The sandwich-type open cell had an effective light-exposure area of 0.238 cm2 with "
    "a black mask. Incident photon-to-current quantum conversion efficiency (IPCE) was "
    "measured on an action spectrum measurement setup (PEC-S20), and photocurrent "
    "voltage (I-V) performance was measured using a solar simulator (PEC-L10) "
    "irradiating simulated sunlight of AM 1.5 and 100 mW/cm2 intensity [@pvsk2009].",
    title="Photovoltaic measurement setup",
)