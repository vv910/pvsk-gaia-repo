"""
Results for pvsk2009 - Photovoltaic performance data.

This module covers the IPCE action spectra, I-V characteristics,
and photovoltaic performance metrics reported in Kojima et al. (2009).
"""

from gaia.lang import (
    claim,
    setting,
    support,
)

# IPCE action spectrum for bromide cell
bromide_ipce_spectrum = claim(
    "With CH3NH3PbBr3/TiO2, photocurrent occurred in the visible wavelength region "
    "(lambda < 600 nm), exhibiting a sharp rise at approximately 570 nm with saturation "
    "at less than 520 nm, characteristic of band-gap absorption. The IPCE reached a maximum "
    "of 65% with a plateau indicating strong absorption by the 8 um thin film of "
    "CH3NH3PbBr3/TiO2 [@pvsk2009].",
    title="CH3NH3PbBr3 IPCE spectrum 65% max",
    metadata={"figure": "artifacts/images/82473e6d0fe888b823d0ade917066070e4ea568beb54f5aa585977a399b62870.jpg",
             "caption": "Fig. 2a | IPCE action spectra for CH3NH3PbBr3/TiO2 (solid) and CH3NH3PbI3/TiO2 (dashed)"},
)

# IPCE action spectrum for iodide cell
iodide_ipce_spectrum = claim(
    "The CH3NH3PbI3/TiO2 cell showed a low IPCE of 45% but an extended spectral "
    "responsivity to lambda = 800 nm, reflecting the black color of the electrode. "
    "This bathochromic shift by halogen substitution is analogous to that for silver "
    "halide ionic crystals [@pvsk2009].",
    title="CH3NH3PbI3 IPCE 45% with extended spectral range to 800 nm",
    metadata={"figure": "artifacts/images/82473e6d0fe888b823d0ade917066070e4ea568beb54f5aa585977a399b62870.jpg",
             "caption": "Fig. 2a | IPCE action spectra comparison"},
)

# Photocurrent generation under light irradiation
photocurrent_generation = claim(
    "Light irradiation of the photovoltaic cells caused generation of anodic photocurrents "
    "with amplitudes of 5-11 mA/cm2 [@pvsk2009].",
    title="Anodic photocurrent generation 5-11 mA/cm2",
)

# I-V characteristics for bromide cell
bromide_iv_characteristics = claim(
    "Under 100 mW/cm2 AM 1.5 irradiation, the CH3NH3PbBr3-sensitized cell yielded "
    "Jsc = 5.57 mA/cm2, Voc = 0.96 V, fill factor (FF) = 0.59, and power conversion "
    "efficiency (eta) = 3.13% [@pvsk2009].",
    title="CH3NH3PbBr3 cell I-V performance",
    metadata={"figure": "artifacts/images/9dc3b0b5468ffcca6d463a8dca5c7d683f770a86759f61752c1a91c9cdce8b07.jpg",
             "caption": "Fig. 2b | Photocurrent voltage characteristics"},
)

# I-V characteristics for iodide cell
iodide_iv_characteristics = claim(
    "Under 100 mW/cm2 AM 1.5 irradiation, the CH3NH3PbI3-sensitized cell yielded "
    "Jsc = 11.0 mA/cm2 (twice that of the bromide cell), Voc = 0.61 V, fill factor (FF) = 0.57, "
    "and power conversion efficiency (eta) = 3.81% [@pvsk2009].",
    title="CH3NH3PbI3 cell I-V performance",
    metadata={"figure": "artifacts/images/9dc3b0b5468ffcca6d463a8dca5c7d683f770a86759f61752c1a91c9cdce8b07.jpg",
             "caption": "Fig. 2b | Photocurrent voltage characteristics"},
)

# Jsc comparison between cells
jsc_comparison = claim(
    "The short-circuit current density (Jsc) for the CH3NH3PbI3-sensitized cell "
    "(11.0 mA/cm2) was twice that of the CH3NH3PbBr3-sensitized cell (5.57 mA/cm2), "
    "reflecting the integrated area of the IPCE spectra [@pvsk2009].",
    title="Jsc for iodide cell twice that of bromide cell",
)

# Voc comparison between cells
voc_comparison = claim(
    "The CH3NH3PbI3-sensitized cell showed a low open-circuit voltage (Voc) of 0.61 V, "
    "while the CH3NH3PbBr3-sensitized cell yielded a notably high Voc of 0.96 V. "
    "The high Voc of the bromide cell is associated with its higher conduction band "
    "relative to that of the iodide, allowing electronic interaction with the surface "
    "conduction-band levels of TiO2 [@pvsk2009].",
    title="Bromide cell Voc 0.96 V vs iodide cell Voc 0.61 V",
)

# Ru complex comparison
ru_complex_voc_comparison = claim(
    "With Ru complex sensitizers and TiO2, the maximal Voc ever reported is in the range "
    "of 0.86-0.93 V. The 0.96 V achieved with CH3NH3PbBr3 exceeds this range [@pvsk2009].",
    title="CH3NH3PbBr3 Voc exceeds Ru complex maximal Voc",
)

# Efficiency comparison with prior work
efficiency_comparison = claim(
    "The highest power conversion efficiency of 3.81% obtained with CH3NH3PbI3 is "
    "significantly higher than those obtained to date with nonorganic sensitizers and "
    "quantum dots [@pvsk2009].",
    title="Perovskite efficiency exceeds prior quantum dot sensitizers",
)

# Photovoltaic performance table
pv_performance_table = claim(
    "Photovoltaic characteristics of perovskite-based cells under 100 mW/cm2 AM 1.5 "
    "simulated sunlight irradiation with an effective incident area of 0.24 cm2:\n\n"
    "| Perovskite Sensitizer on TiO2 | Jsc (mA/cm2) | Voc (V) | FF | eta (%) |\n"
    "|-------------------------------|--------------|---------|-----|--------|\n"
    "| CH3NH3PbBr3                   | 5.57         | 0.96    | 0.59| 3.13   |\n"
    "| CH3NH3PbI3                   | 11.0         | 0.61    | 0.57| 3.81   |",
    title="Photovoltaic performance summary table",
)

# High IPCE confirms efficient sensitization
efficient_sensitization_confirmation = claim(
    "The anodic photocurrent with high IPCE values (65% for bromide, 45% for iodide) "
    "corroborates that TiO2 was efficiently sensitized by the nanocrystalline perovskite "
    "under visible light irradiation [@pvsk2009].",
    title="High IPCE confirms efficient TiO2 sensitization by perovskite",
)

# Durability observation
durability_observation = claim(
    "Continuous irradiation caused photocurrent decay for an open cell exposed to air, "
    "indicating a durability issue that requires further study to improve cell lifetime "
    "[@pvsk2009].",
    title="Photocurrent decay observed under continuous irradiation",
)