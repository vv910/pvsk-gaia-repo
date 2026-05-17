"""
Gaia knowledge package for Lin2025: All-perovskite tandem solar cells with dipolar passivation.
Methods - Mixed Pb-Sn PSC with dipolar passivation.
"""

from gaia.lang import claim, setting
from .motivation import (
    dipolar_passivation_strategy,
    sa_dipole_moment,
)

# Device structure
device_structure = claim(
    "The mixed Pb-Sn perovskite solar cells have a p-i-n configuration consisting of "
    "ITO/PEDOT:PSS/SA/NBG perovskites/C60/ALD-SnO2 (or C60/BCP/Cu) [@Lin2025]."
)

# Dipolar passivation design principles
dipolar_passivation_design = claim(
    "The dipolar passivation for the HTL/Pb-Sn perovskite interface is designed with passivating groups and positively oriented dipoles, "
    "with the net dipole directed towards the Pb-Sn perovskite surface. Sulfanilic acid (SA) is used as the dipolar molecule, featuring "
    "an -NH3+ passivating group and a -SO3- dipole group [@Lin2025]."
)

# ToF-SIMS confirmation of SA at buried interface
tof_simms_analysis = claim(
    "Time-of-flight secondary ion mass spectrometry (ToF-SIMS) analysis confirms that SA molecules accumulate at the "
    "perovskite/HTL buried interface, with stronger signal detected near the bottom surface compared to the top surface [@Lin2025]."
)

# XPS evidence
xps_evidence = claim(
    "X-ray photoelectron spectroscopy (XPS) measurements detect S 2p signals at the buried perovskite interface, confirming "
    "the presence of SA molecules at the bottom surface after perovskite film deposition [@Lin2025]."
)

# Molecular orientation from AIMD
aimd_molecular_orientation = claim(
    "Ab initio molecular dynamics (AIMD) simulations suggest a favoured molecular orientation in which the -NH3+ group anchors "
    "to the perovskite bottom surface, whereas the -SO3- group is directed towards the HTL (PEDOT:PSS) [@Lin2025]."
)

# KPFM measurements
kpfm_potential_change = claim(
    "Kelvin probe force microscopy (KPFM) measurements show that the surface potential of the dipolar-passivation-treated Pb-Sn perovskite "
    "decreases from -80 mV (control) to -162 mV, accompanied by a 76 mV increase in PEDOT:PSS surface potential [@Lin2025]."
)

# Energy level alignment with dipolar passivation
energy_level_alignment = claim(
    "With dipolar passivation, the work function and valence-band maximum of the Pb-Sn perovskite are approximately -4.74 eV and "
    "-5.26 eV, respectively, compared with -4.68 eV and -5.27 eV for the control. The work function of PEDOT:PSS increases from "
    "-4.90 eV to -4.81 eV with dipolar passivation [@Lin2025]."
)

# Type-II energy alignment
type_ii_energy_alignment = claim(
    "A type-II energy-level alignment forms between the dipolar-passivation-treated Pb-Sn perovskites and PEDOT:PSS, creating an "
    "electric field directed from the perovskite surface towards PEDOT:PSS, effectively driving carriers away from the defective "
    "interface layer (DIL) and facilitating holes drifting into PEDOT:PSS while repelling electrons from the HTL/Pb-Sn perovskite "
    "interface [@Lin2025]."
)

__all__ = [
    "device_structure",
    "dipolar_passivation_design",
    "tof_simms_analysis",
    "xps_evidence",
    "aimd_molecular_orientation",
    "kpfm_potential_change",
    "energy_level_alignment",
    "type_ii_energy_alignment",
]