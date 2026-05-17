"""
Molecular structure design and characterization of HTL201 and reference SAMs.

This module covers the molecular design section and basic characterization.
"""

from gaia.lang import (
    claim,
    setting,
)

# Molecular structure design
asymmetric_design = claim(
    "Different from most reported carbazole-based SAMs, which feature a symmetric molecular "
    "structure with nitrogen atoms bonded to phosphonic acid anchoring groups, HTL201 has an "
    "asymmetric carbazole-based structure incorporating spacers and anchoring phosphonic acid "
    "groups flanking the phenyl ring of the carbazole core.",
    title="HTL201 asymmetric molecular design",
)

htl201_chemical_verification = claim(
    "The chemical structure of HTL201 was verified through 1H nuclear magnetic resonance (NMR) "
    "spectroscopy, 13C NMR spectroscopy, mass spectrometry and Fourier transform infrared "
    "spectroscopy.",
    title="HTL201 chemical structure verification",
)

reference_sams = claim(
    "Two symmetric SAMs, Me-4PACz and MeO-4PACz, were examined for comparison with HTL201 "
    "to demonstrate the positive impact of the side-chain phosphonic acid group on performance enhancement.",
    title="Reference SAMs Me-4PACz and MeO-4PACz",
)

thermal_stability = claim(
    "All three SAM molecules (Me-4PACz, MeO-4PACz, HTL201) show thermal decomposition "
    "temperatures above 200 degrees C, indicating capability to withstand the high temperatures "
    "(100 degrees C) used for device fabrication.",
    title="SAM thermal stability above 200C",
)

homo_energy_levels = claim(
    "The highest occupied molecular orbital (HOMO) energy levels of Me-4PACz, MeO-4PACz and "
    "HTL201 were measured at -5.32 eV, -5.08 eV and -5.11 eV, respectively, by cyclic voltammetry.",
    title="HOMO energy levels of SAMs",
)

__all__ = [
    "asymmetric_design",
    "htl201_chemical_verification",
    "reference_sams",
    "thermal_stability",
    "homo_energy_levels",
]