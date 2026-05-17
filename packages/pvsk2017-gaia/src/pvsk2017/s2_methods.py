"""
Structural and Optoelectronic Characterization Methods.

This module covers the experimental methods for synthesizing 2D perovskite,
creating 2D/3D composites, and characterizing their structural and optical properties.
Paper lines 32-52 discuss the Results - Structural and Optoelectronic characterization.
"""

from gaia.lang import claim, setting

# Material synthesis
avai_synthesis = claim(
    "The 2D perovskite was synthesized using protonated salt of aminovaleric acid iodide "
    "(HOOC(CH2)4NH3I, AVAI) as organic precursor mixed with PbI2, resulting in "
    "(HOOC(CH2)4NH3)2PbI4 low-dimensional perovskite structure with yellowish film "
    "containing needle-like crystallites [@Grancini2017].",
    title="AVAI-based 2D perovskite synthesis",
)

two_d_three_d_composite_preparation = claim(
    "2D/3D composites were engineered by mixing (AVAI:PbI2) and (CH3NH3I:PbI2) precursors "
    "at different molar ratios (0-3-5-10-20-50%), infiltrated into mesoporous oxide scaffold "
    "by single-step deposition followed by slow drying, allowing reorganization before solidification [@Grancini2017].",
    title="2D/3D composite preparation method",
)

# Structural characterization methods
absorption_spectroscopy = setting(
    "UV-vis spectroscopy was used to measure absorption spectra of perovskite films, "
    "with excitation at specific wavelengths for photoluminescence measurements.",
    title="Absorption spectroscopy setup",
)

raman_spectroscopy = setting(
    "Raman spectra were collected using a micro-Raman system (Renishaw) with 532 nm laser excitation, "
    "50-250 cm-1 range, calibrated against silicon wafer. Measurements conducted at room temperature "
    "on encapsulated samples with laser power below 50 μW to prevent degradation [@Grancini2017].",
    title="Raman spectroscopy parameters",
)

xrd_method = setting(
    "X-ray diffraction measurements used a D8 Advance diffractometer (Bruker) in Bragg-Brentano geometry "
    "on perovskite layers grown on mesoporous titania/zirconia substrates [@Grancini2017].",
    title="XRD measurement setup",
)

# Photoluminescence characterization
steady_state_pl = setting(
    "Steady-state PL measurements used a spectrophotometer (Gilden Photonics) with excitation at 400 nm "
    "and 600 nm to selectively probe different perovskite phases. Time-resolved PL used "
    "pulsed laser (460 nm, <100 ps pulse width, 20 MHz repetition rate) with Time Correlated "
    "Single Photon Counting detection (1 ns time resolution) [@Grancini2017].",
    title="Photoluminescence characterization setup",
)

pl_excitation_selectivity = claim(
    "By varying the excitation side, the system selectively interrogates perovskite crystals "
    "within the oxide scaffold (penetration depth <100 nm at 600 nm) versus the top bulk "
    "perovskite layer, enabling phase-specific analysis [@Grancini2017].",
    title="Excitation side PL selectivity",
)

# DFT simulation method
dft_methodology = setting(
    "First principles DFT calculations used periodic boundary conditions with plane-wave/pseudopotential "
    "formalism (PWSCF/Quantum-ESPRESSO). PBE functional with ultrasoft scalar-relativistic "
    "pseudopotentials. Cutoffs: 25 Ry (wave function) and 200 Ry (electronic density). "
    "SOC included for DOS calculations [@Grancini2017].",
    title="DFT calculation parameters",
)

interface_model = claim(
    "The 2D/3D interface model used I-terminated MAPbI3 2x2x3 tetragonal slab (001 surfaces) combined "
    "with (HOOC(CH2)3NH3)PbI4 experimental structure. Lattice mismatch <1%. One MA+ layer replaced "
    "with AVA layer at interface. Cell parameters a=b=17.7112 with 10 Å vacuum along z [@Grancini2017].",
    title="2D/3D interface computational model",
)