"""
s2_methods.py - Materials and Methods for perovskite solar cell fabrication

This module covers the device architecture, materials, fabrication protocols,
and characterization methods used in this study.
"""
from gaia.lang import claim, setting

# Perovskite composition
perovskite_composition = setting(
    "The perovskite used is mixed-halide methylammonium lead iodide chloride "
    "(CH3NH3PbI2Cl), processed from precursor solution in N,N-dimethylformamide (DMF) "
    "via spin-coating in ambient conditions [@Lee2012]."
)

# Crystal structure parameters
crystal_structure = claim(
    "X-ray diffraction analysis for CH3NH3PbI2Cl showed diffraction peaks at 14.20 deg, "
    "28.58 deg, and 43.27 deg, assigned as (110), (220), and (330) planes of a "
    "tetragonal perovskite structure with lattice parameters a = 8.825 A, b = 8.835 A, "
    "c = 11.24 A, similar to CH3NH3PbI3 previously reported [@Lee2012].",
    title="Perovskite crystal structure"
)

# Film quality
film_crystallinity = claim(
    "Extremely narrow diffraction peaks suggest films have long-range crystalline "
    "domains (>200 nm, peak width limited by instrument broadening) and are highly "
    "oriented with the a axis [@Lee2012].",
    title="Perovskite film crystallinity"
)

# Film stability
film_stability = claim(
    "The iodide-chloride mixed-halide perovskite was remarkably stable to processing "
    "in air, in contrast to methylammonium trihalogen plumbates previously reported "
    "in solar cells [@Lee2012].",
    title="Perovskite air stability"
)

# Device architecture - general
device_architecture = setting(
    "The solar cell structure uses FTO-coated glass with compact TiO2 layer as anode, "
    "porous oxide film (either TiO2 or Al2O3), perovskite absorber, spiro-OMeTAD "
    "hole conductor, and silver electrode [@Lee2012]."
)

# n-type scaffold
n_type_scaffold = setting(
    "Mesoporous TiO2 (anatase) serves as the n-type transparent component in "
    "sensitized devices [@Lee2012]."
)

# insulator scaffold
insulator_scaffold = setting(
    "Mesoporous Al2O3 (insulator with wide band gap 7-9 eV) serves as an inert "
    "scaffold that structures the absorber and forces electrons to reside in and be "
    "transported through the perovskite in meso-superstructured solar cells (MSSC) "
    "[@Lee2012]."
)

# Hole conductor
hole_conductor = setting(
    "2,2',7,7'-tetrakis-(N,N-di-p-methoxyphenylamine)9,9'-spirobifluorene "
    "(spiro-OMeTAD) is used as the transparent p-type hole conductor [@Lee2012]."
)

# Fabrication process
fabrication_process = claim(
    "Porous oxide films were fabricated from sol-gel-processed sintered nanoparticles; "
    "the perovskite precursor solution was infiltrated via spin-coating and dried at "
    "100 deg C, enabling perovskite formation via self-assembly of constituent ions "
    "[@Lee2012].",
    title="Device fabrication process"
)

# Pore filling
pore_filling = claim(
    "At optimum perovskite precursor concentrations, no capping layer appeared, "
    "indicating perovskite was predominantly formed within the mesoporous film and "
    "uniformly distributed throughout [@Lee2012].",
    title="Perovskite pore filling"
)

# Perovskite conductivity
perovskite_conductivity = claim(
    "The perovskite absorber is reasonably conductive, measured to be on the order of "
    "10^-3 S cm^-1 [@Lee2012].",
    title="Perovskite conductivity"
)

# Spiro-OMeTAD conductivity
spiro_conductivity = claim(
    "Spiro-OMeTAD has conductivity of approximately 10^-5 S cm^-1, lower than the "
    "perovskite, so a thick capping layer results in high series resistance [@Lee2012].",
    title="Spiro-OMeTAD conductivity"
)

# IPCE measurement
ipce_method = setting(
    "Incident photon-to-electron conversion efficiency (IPCE) action spectrum measures "
    "spectral sensitivity of devices [@Lee2012]."
)

# J-V measurement
jv_method = setting(
    "Current density-voltage (J-V) curves were measured under simulated AM1.5 "
    "illumination of 100 mW cm^-2 [@Lee2012]."
)

# PIA spectroscopy
pia_method = setting(
    "Photoinduced absorption (PIA) spectroscopy was used to examine charge generation "
    "in oxide films coated with perovskite [@Lee2012]."
)

# Transient photocurrent
transient_photocurrent_method = setting(
    "Small-perturbation transient photocurrent decay measurements were performed to "
    "probe charge transport effectiveness, where decay rate is approximately proportional "
    "to charge transport rate out of the photoactive layer [@Lee2012]."
)

# SEM/EDX characterization
sem_edx_method = setting(
    "Cross-sectional scanning electron microscopy (SEM) with elemental mapping via "
    "energy-dispersive x-ray (EDX) analysis verified perovskite distribution "
    "[@Lee2012]."
)

__all__ = [
    "perovskite_composition",
    "crystal_structure",
    "film_crystallinity",
    "film_stability",
    "device_architecture",
    "n_type_scaffold",
    "insulator_scaffold",
    "hole_conductor",
    "fabrication_process",
    "pore_filling",
    "perovskite_conductivity",
    "spiro_conductivity",
    "ipce_method",
    "jv_method",
    "pia_method",
    "transient_photocurrent_method",
    "sem_edx_method",
]