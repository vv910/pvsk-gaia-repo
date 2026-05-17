"""
s2_methods.py - Experimental methods and characterization techniques.

This module covers the methods used in the paper including:
- Perovskite film preparation
- Post-treatment procedures
- Characterization techniques (PL, GIWAXS, SEM, AFM, etc.)
- DFT calculations
"""

from gaia.lang import claim, setting

# Perovskite composition
perovskite_composition = setting(
    "FA-dominated perovskite (FA0.93Cs0.07PbI3) featuring slightly narrow bandgap "
    "is used, with 5% reduction in Cs concentration compared to prior report. "
    "Crystallization dynamics are optimized by solvent modulation, resulting in "
    "high-quality pinhole-free morphology without antisolvent [@Li2024].",
    title="FA0.93Cs0.07PbI3 perovskite composition",
)

# 2D ligands tested
ligands_tested = claim(
    "Commonly used ammonium halides are selected as post-treatment agents: "
    "BA (n-butylammonium), OA (n-octylammonium), DA (n-dodecylammonium), "
    "HDA (hexadecylammonium), PMA (phenmethylammonium), PEA (phenylethylammonium), "
    "NMA (1-naphthylmethylammonium), PRMA (1-pyrenemethylammonium). RX represents "
    "ammonium halides where R is organic ammonium and X is halide [@Li2024].",
    title="2D ligands used in post-treatment study",
)

# Device configuration
device_configuration = setting(
    "PSM structure: glass/FTO/SnO2/perovskite/passivator/spiro-OMeTAD/Au. "
    "Perovskite precursor solution uses DMF/2-Me mixed solvent (300 microliter/250 microliter) "
    "with equal molar NMP and excess 7 mol% PbI2 and 35 mol% MACl [@Li2024].",
    title="PSM device configuration",
)

# Post-treatment solutions
post_treatment_preparation = setting(
    "Post-treatment solutions prepared by dissolving 15 mmol of different organic "
    "halide salts in 1 ml IPA solution. For DABr/FABr treatment, mixed solutions "
    "are dynamically spun onto perovskite surface at ~18 C, 4000 rpm for 30 s, "
    "followed by annealing at 100 C for 5 min [@Li2024].",
    title="Post-treatment solution preparation",
)

# Antisolvent-free spin coating
antisolvent_free_process = claim(
    "Perovskite precursor is antisolvent-free spin-coated on glass/FTO/SnO2 substrates "
    "in N2 glovebox (T < 18 C, 5000 rpm for 60 s). After annealing at 70 C in N2 for 1 min, "
    "film is annealed at 100 C for 2 h in ambient with relative humidity ~30% [@Li2024].",
    title="Antisolvent-free spin coating process",
)

# PL spectroscopy method
pl_characterization = claim(
    "Steady-state PL spectra obtained using PL microscopic spectrometer with LED light "
    "source emitting at 405 nm in ambient environment (~20 C, low humidity). Ocean Optical "
    "spectrometer (QE65Pro) used to collect PL emission. In situ PL measurements performed "
    "during spin-coating process at 1 s intervals for total of 2 min [@Li2024].",
    title="Photoluminescence characterization method",
)

# GIWAXS characterization
giwaxs_method = claim(
    "GIWAXS performed using GANESHA 300 XL SAXS SYSTEM with X-ray photon energy of 8.05 keV "
    "(wavelength = 1.54 A). Incidence light angle 0.8 degrees, Pilatus 300k detector used "
    "to collect scattering signal. Out-of-plane scattering vectors qz used for analysis [@Li2024].",
    title="GIWAXS characterization method",
)

# SEM characterization
sem_method = claim(
    "Field-emission scanning electron microscopy (SEM, JSM-7500F, Zeiss Ultra Plus) used "
    "for surface and cross-sectional morphology characterization of perovskite films [@Li2024].",
    title="SEM characterization method",
)

# AFM and KPFM method
afm_kpfm_method = claim(
    "Atomic force microscopy and Kelvin probe force microscopy (AFM and KPFM, SPM-9700, "
    "Asylum Research) used to characterize surface morphology and surface potential "
    "distribution of perovskite films [@Li2024].",
    title="AFM and KPFM characterization method",
)

# SCLC method for trap density
sclc_method = claim(
    "Space-charge-limited current (SCLC) measurements performed by constructing "
    "electron-only and hole-only devices to quantify electron and hole trap density (Nt) "
    "and mobility values. Measurements enable calculation of Nt from I-V curves [@Li2024].",
    title="SCLC method for trap density",
)

# J-V characterization
jv_characterization = claim(
    "J-V curves measured using Keithley 2400 source meter with solar simulator (Oriel "
    "94023A, 300 W) calibrated to AM 1.5G at 100 mW/cm2 using reference silicon solar cell. "
    "Black metal aperture masks used: 0.14 cm2 for small devices, 1.04 cm2 for large devices [@Li2024].",
    title="J-V characterization method",
)

# EQE measurement
eqe_method = claim(
    "External quantum efficiency (EQE) spectra measured using commercial EQE system "
    "(QE-R, Enlitech). Integrated current density from EQE used to validate J-V "
    "characterization results [@Li2024].",
    title="EQE measurement method",
)

# MPPT stability testing
mppt_method = claim(
    "Maximum power point tracking (MPPT) tested using multi-channel solar cell stability "
    "test system with LED light source (6500 K, white-light LED array) calibrated to "
    "equivalent one sun illumination. Encapsulated mini-modules tested in ambient air "
    "with ~50% RH [@Li2024].",
    title="MPPT stability testing method",
)

# DFT computational method
dft_method = claim(
    "First-principles calculations performed using density functional theory (DFT) with "
    "Vienna ab initio simulation package. Projector augmented wave method used for "
    "core-valence electron interactions. PBE functional within GGA used for exchange-correlation. "
    "van der Waals corrected by Grimme potential (D2). Plane-wave cutoff energy 400 eV, "
    "k-point mesh 0.01 A^-1, geometry fully relaxed to convergence criteria of "
    "energy < 1e-5 eV and force < 0.01 eV/A [@Li2024].",
    title="DFT computational method",
)

# ToF-SIMS method
tofsims_method = claim(
    "Time-of-flight secondary-ion mass spectrometry (PHI nano TOFII Time-of-Flight SIMS) "
    "used to perform ToF-SIMS depth profiles and images of perovskite films, confirming "
    "distribution of DA cations and Br ions on 3D perovskite surface [@Li2024].",
    title="ToF-SIMS characterization method",
)

# Time-resolved PL method
trpl_method = claim(
    "Time-resolved photoluminescence spectra measured at 800 nm using 485 nm picosecond "
    "pulsed diode laser with ~200 ps pulse width and impulse energy of 14 pJ per pulse "
    "(Nano LED-C2 N-485L, HORIBA Scientific). Confocal PL mappings performed using "
    "fluorescence spectrometer with 404 nm laser, 1 MHz repetition rate (Micro Time 200, "
    "Pico-Quant GmbH) [@Li2024].",
    title="Time-resolved PL characterization method",
)

# Slot-die printing method
slot_die_method = claim(
    "Perovskite precursor ink diluted by 2-Me to 1 M, slot-die printed on 20cmx20cm and "
    "30cmx30cm substrates in ambient air (T ~ 20 C, ~20% RH). Syringe pump set to 0.2 ml/s, "
    "stainless steel slot-die head with 10 micrometer internal shim, gap height 110 micrometer, "
    "coating speed 2 mm/s, air knife with N2 pressure 0.35 MPa. Printed film annealed at "
    "100 C for 1 h then 120 C for 1.5 h in ambient air [@Li2024].",
    title="Slot-die printing method for large-area modules",
)

# Laser patterning method
laser_pattering_method = claim(
    "Picosecond laser (Suzhou Microtreat Intelligent Technology) used to process P1, P2, P3 "
    "patterns for series connection of subcells in large modules. P1 etching: power 12 W, "
    "speed 4000 mm/s. P2 etching: power 9.3 W, speed 2000 mm/s. P3: 0.5 mm wide tape, "
    "power 8.4 W, speed 3000 mm/s for 5cmx5cm mini-module with GFF ~96% [@Li2024].",
    title="Laser patterning for module interconnection",
)