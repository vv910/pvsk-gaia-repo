"""
Priors for pvsk2009 package.
"""

from .motivation import (
    perovskite_sensitization_demonstrated,
    organic_sensitizer_limitations,
    quantum_dot_approach,
)

from .s2_methods import (
    bromide_cubic_structure,
    iodide_tetragonal_structure,
    tiO2_thickness_optimization,
    bromide_particle_size,
)

from .s3_results import (
    photocurrent_generation,
    bromide_ipce_spectrum,
    iodide_ipce_spectrum,
    bromide_iv_characteristics,
    iodide_iv_characteristics,
)

from .s4_discussion import (
    valence_band_levels,
)

PRIORS = {
    # XRD structural characterization
    bromide_cubic_structure: (
        0.88,
        "X-ray diffraction is a well-established technique. "
        "The cubic perovskite structure (a=5.9A) with peaks at 14.77, 20.97, 29.95, 42.9, "
        "45.74 degrees is a direct structural measurement [@pvsk2009]."
    ),

    iodide_tetragonal_structure: (
        0.88,
        "X-ray diffraction measurement of tetragonal perovskite structure (a=8.855A, c=12.659A) "
        "is a well-established analytical result with peaks at 14.00 and 28.36 degrees [@pvsk2009]."
    ),

    # IPCE spectroscopic measurements
    bromide_ipce_spectrum: (
        0.90,
        "IPCE is a direct spectral response measurement. "
        "The maximum of 65% with sharp band-edge rise at 570 nm reflects directly measured "
        "photon-to-current conversion efficiency [@pvsk2009]."
    ),

    iodide_ipce_spectrum: (
        0.88,
        "IPCE is a direct spectral response measurement. "
        "The 45% maximum with extended responsivity to 800 nm reflects directly measured "
        "spectral response under controlled conditions [@pvsk2009]."
    ),

    # I-V electrical measurements
    bromide_iv_characteristics: (
        0.90,
        "I-V characteristics under 100 mW/cm2 AM 1.5 are standard photovoltaic measurements. "
        "Values Jsc=5.57 mA/cm2, Voc=0.96 V, FF=0.59, eta=3.13% are directly measured [@pvsk2009]."
    ),

    iodide_iv_characteristics: (
        0.90,
        "I-V characteristics under 100 mW/cm2 AM 1.5 are standard photovoltaic measurements. "
        "Values Jsc=11.0 mA/cm2, Voc=0.61 V, FF=0.57, eta=3.81% are directly measured [@pvsk2009]."
    ),

    # Photoelectron spectroscopy
    valence_band_levels: (
        0.87,
        "Photoelectron spectroscopy provides direct measurement of valence band levels. "
        "Values 5.38 eV (bromide) and 5.44 eV (iodide) versus vacuum are directly measured [@pvsk2009]."
    ),

    # Core experimental observations
    photocurrent_generation: (
        0.88,
        "Photocurrent generation under light irradiation is a direct experimental observation. "
        "The 5-11 mA/cm2 anodic photocurrent amplitudes are directly measured [@pvsk2009]."
    ),

    # Main finding
    perovskite_sensitization_demonstrated: (
        0.85,
        "The demonstration of perovskite sensitization of TiO2 is supported by multiple "
        "independent lines of evidence: IPCE spectra, photovoltaic efficiency, crystal "
        "structure XRD confirmation, and first demonstration in literature [@pvsk2009]."
    ),

    # Background claims
    organic_sensitizer_limitations: (
        0.82,
        "The limitation of organic sensitizers due to low absorption coefficients and narrow "
        "absorption bands is well-established in the dye-sensitized solar cell literature [@pvsk2009]."
    ),

    quantum_dot_approach: (
        0.80,
        "The limitations of quantum dot sensitizers due to light utilization and charge "
        "separation losses is supported by multiple prior studies [@pvsk2009]."
    ),

    # Methods-related observations
    tiO2_thickness_optimization: (
        0.85,
        "The optimal TiO2 thickness (8 um for iodide, 12 um for bromide) was determined "
        "through systematic experimental optimization [@pvsk2009]."
    ),

    bromide_particle_size: (
        0.82,
        "SEM observation of 2-3 nm CH3NH3PbBr3 particles on TiO2 is a direct microscopic "
        "observation. Figure 1b scale bar (10 nm) provides calibration [@pvsk2009]."
    ),
}