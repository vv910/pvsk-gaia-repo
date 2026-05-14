"""
Discussion and Conclusions for pvsk2009 - Energy levels and mechanism.

This module covers the energy band analysis, charge injection mechanism,
and concluding remarks from Kojima et al. (2009).
"""

from gaia.lang import (
    claim,
    setting,
    support,
)

# Valence band levels from photoelectron spectroscopy
valence_band_levels = claim(
    "Photoelectron spectroscopy of spin-coated polycrystalline films showed valence-band "
    "levels of CH3NH3PbBr3 and CH3NH3PbI3 at approximately 5.38 and 5.44 eV versus the "
    "vacuum level, respectively [@pvsk2009].",
    title="Perovskite valence band levels",
)

# Oxidation potentials of halides in electrolyte
halide_oxidation_potentials = setting(
    "The valence-band levels of the perovskites are considered to be more positive than "
    "the oxidation potentials of the corresponding halides in the electrolyte, which are "
    "estimated to be 5.1-5.6 eV for Br2/Br- and 4.5-5.0 eV for I2/I- (depending on halide "
    "concentration) [@pvsk2009].",
    title="Halide redox couple oxidation potentials",
)

# Conduction band levels from optical absorption edges
conduction_band_levels = claim(
    "The conduction-band levels calculated from the wavelengths of the optical absorption "
    "edges are at approximately 3.36 and 4.0 eV for CH3NH3PbBr3 and CH3NH3PbI3, "
    "respectively. These values allow electron injection to the TiO2 conduction band "
    "(approximately 4.0 eV) [@pvsk2009].",
    title="Perovskite conduction band levels enabling electron injection to TiO2",
)

# Bromide conduction band relative to TiO2
bromide_conduction_band_higher = claim(
    "The conduction band of CH3NH3PbBr3 (approximately 3.36 eV) is higher than that of "
    "CH3NH3PbI3 (approximately 4.0 eV), and the higher conduction band of the bromide "
    "relative to the iodide is associated with its higher open-circuit voltage (Voc = 0.96 V) "
    "through electronic interaction with the surface conduction-band levels of TiO2 [@pvsk2009].",
    title="Higher bromide conduction band explains higher Voc",
)

# Bromide redox coupling enables high Voc
bromide_redox_coupling = claim(
    "The origin of the high Voc (0.96 V) with CH3NH3PbBr3 is the bromide employed as a "
    "redox partner to couple with the perovskite bromide; the electrochemically more "
    "positive potential of bromide compared with iodide expands the range of photovoltage "
    "[@pvsk2009].",
    title="Bromide redox coupling expands photovoltage range",
)

# Quantum confinement effect assessment
quantum_confinement_assessment = claim(
    "The IPCE spectra suggest that quantum confinement effect may not dominate the "
    "present perovskite system if it partially exists by sensitizing TiO2 at shorter "
    "wavelengths [@pvsk2009].",
    title="Quantum confinement effect not dominant",
)

# Bathochromic shift explanation
bathochromic_shift_explanation = claim(
    "The bathochromic shift (red-shift) of the IPCE spectrum from bromide to iodide "
    "perovskite, extending spectral responsivity to 800 nm for CH3NH3PbI3, is analogous "
    "to the shift observed in silver halide ionic crystals and reflects the narrower "
    "bandgap of the iodide compound [@pvsk2009].",
    title="Bathochromic shift from bromide to iodide analogous to silver halides",
)

# Charge separation mechanism
charge_separation_mechanism = claim(
    "The efficient sensitization is enabled by: (1) favorable energy band alignment "
    "allowing electron injection from perovskite conduction band to TiO2, (2) the valence "
    "band being more positive than halide oxidation potentials enabling hole transfer to "
    "the electrolyte, and (3) strong light absorption by the perovskite film enabling "
    "high IPCE values [@pvsk2009].",
    title="Charge separation mechanism in perovskite-sensitized TiO2",
)

# Conclusion: Perovskite sensitization demonstrated
conclusion_perovskite_sensitization = claim(
    "The organolead halide perovskite compounds efficiently sensitize TiO2 for visible-light "
    "conversion in photovoltaic cells, representing a significant advance over nonorganic "
    "sensitizers and quantum dots that had not achieved comparable performance [@pvsk2009].",
    title="Perovskite efficiently sensitizes TiO2 for visible-light conversion",
)

# Conclusion: High photovoltage potential
conclusion_high_voltage = claim(
    "The perovskite materials are especially promising for realizing high photovoltages "
    "close to 1.0 V, as demonstrated by the 0.96 V achieved with CH3NH3PbBr3, which "
    "exceeds the maximal Voc previously achieved with Ru complex sensitizers (0.86-0.93 V) "
    "[@pvsk2009].",
    title="Perovskite enables high photovoltages close to 1.0 V",
)

# Future directions
future_directions = setting(
    "A series of organic-inorganic perovskite materials CH3NH3MX3 (M = Pb, Sn; X = halogen) "
    "exhibiting different energy gaps are targets for optimizing cell performance [@pvsk2009].",
    title="Future perovskite materials for cell optimization",
)

# Efficiency milestone
efficiency_milestone = claim(
    "The demonstration of 3.81% power conversion efficiency with CH3NH3PbI3 represents "
    "a milestone: the first application of organometal halide perovskites as visible-light "
    "sensitizers in photovoltaic cells, establishing a new class of materials for solar "
    "energy conversion [@pvsk2009].",
    title="3.81% efficiency marks first perovskite-sensitized solar cell",
)