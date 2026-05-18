"""
Methods module for pvsks41586-024-07997-7-gaia.

This module covers the experimental methods used in this study, including
materials, device fabrication, and characterization techniques.

Paper: Perovskite/silicon tandem solar cells with bilayer interface passivation
DOI: 10.1038/s41586-024-07997-7
"""

from gaia.lang import (
    claim,
    setting,
    support,
    infer,
)

# =============================================================================
# Materials and Fabrication Settings
# =============================================================================

silicon_bottom_cell_material = setting(
    "An n-doped <100> CZ Si wafer with resistivity of 1-4 Ohm-cm was used for Si bottom cell "
    "fabrication. The rear surface was textured using standard texture procedure (pyramid size "
    "3-5 micrometers). The front surface was mildly textured using relatively low alkaline "
    "concentration to ensure compatibility with perovskite deposition.",
    title="Silicon bottom cell substrate preparation",
)

silicon_heterojunction_layers = setting(
    "Hydrogenated intrinsic amorphous silicon (i-a-Si:H) layers with thickness approximately 5 nm "
    "were grown on both sides of the CZ wafers. N-type nanocrystalline silicon oxide (nc-SiOx:H) and "
    "p-type nc-Si:H layers with thicknesses of approximately 15 nm and 20 nm were deposited on "
    "the front and back, respectively. A 100-nm-thick In2O3-based transparent conductive oxide was "
    "deposited on the rear side, followed by silver deposition, and a 10-nm-thick TCO film was "
    "deposited on the front side.",
    title="Silicon heterojunction layer stack",
)

perovskite_precursor = setting(
    "The perovskite precursor solution (1.6 M wide-bandgap) had composition "
    "FA0.8MA0.15Cs0.05Pb(I0.76Br0.24)3 with 5% excess PbX2 (X=I, Br). The solution was prepared by "
    "dissolving caesium iodide, methylammonium bromide, FAI, PbBr2, and PbI2 in mixed solvent of "
    "dimethylformamide:dimethyl sulfoxide (v:v=4:1).",
    title="Perovskite precursor composition",
)

perovskite_deposition = setting(
    "A two-step spin-coating procedure (1000 rpm for 40 s and 3000 rpm for 20 s) was used. "
    "Ethyl acetate (200 microliters) was dropped in the center of substrates 10 s before the end "
    "of spin coating. Substrates were then annealed at 100 degrees C for 30 min.",
    title="Perovskite film deposition procedure",
)

lif_deposition = setting(
    "Approximately 1 nm LiF was deposited on the perovskite layer by thermal evaporation.",
    title="LiF interlayer deposition",
)

edai_deposition = setting(
    "The organic salt EDAI was ultrasonically dissolved in isopropanol with optimal concentration "
    "of 0.3 mg/ml. The EDAI solution was spin coated on LiF-coated perovskite surface at 3000 rpm "
    "for 30 s and annealed at 100 degrees C for 2 min. After cooling, isopropanol solvent was "
    "dropped at 5000 rpm to wash residual EDAI material.",
    title="EDAI bilayer deposition procedure",
)

bilateral_passivation_stack = setting(
    "The complete bilayer passivation stack consists of: perovskite / LiF (~1nm, discontinuous) / "
    "EDAI (nanoscale localized contacts) / C60 (10nm) / SnO2 (15nm, ALD) / IZO / Ag / MgF2 (110nm).",
    title="Complete bilayer passivation device stack",
)

# =============================================================================
# Characterization Methods
# =============================================================================

pl_measurement = setting(
    "PL images were acquired at room temperature using a Visiontec luminescence analyzer. Samples "
    "were illuminated with two 530 nm blue lasers. A Si CCD camera with band-pass filter (730 plus/minus "
    "30 nm) was used to image luminescence from the perovskite layer. TRPL measurements were carried "
    "out with a fluorescence spectrometer (FluoTime 250, PicoQuant) using a picosecond laser diode "
    "with wavelength of 405 nm.",
    title="Photoluminescence characterization",
)

plqy_measurement = setting(
    "For PLQY measurements, a 532 nm laser with 1-sun equivalent intensity was used for excitation. "
    "The excitation light was coupled into a fiber directed into an integrating sphere on which "
    "the sample was illuminated. Emission was coupled into another fiber connected to a spectrometer.",
    title="PLQY measurement setup",
)

tof_sims_measurement = setting(
    "TOF-SIMS was conducted with an IONTOF TOF.SIMS 5-100 device. A Bi3+ beam (30 kV, 45 degree incidence) "
    "was used as the primary beam, and sputter etching was performed using a Cs+ beam (1 kV, 8 nA, "
    "45 degree incidence) to obtain depth profiles. Analysis area was 100 x 100 micrometers squared "
    "and sputtering area was 300 x 300 micrometers squared.",
    title="TOF-SIMS measurement configuration",
)

xps_measurement = setting(
    "XPS measurements were conducted using a Thermo Fisher ESCALAB Xi+ system with monochromated "
    "Al K-alpha X-ray source (1487.6 eV). Samples were in electrical contact with the analyzer "
    "at ground potential.",
    title="XPS measurement configuration",
)

ups_measurement = setting(
    "UPS measurements were conducted using a Thermo Fisher ESCALAB Xi+ system. Surface work function "
    "and valence region were studied by UPS with vacuum ultraviolet unfiltered He(I) (21.22 eV) source. "
    "Samples were biased to -10 V to observe secondary electron cut-off.",
    title="UPS measurement configuration",
)

kpfm_measurement = setting(
    "KPFM was performed on a custom-built system inside an argon-filled glovebox measuring "
    "contact-potential difference between the probe (NANOSENSORS PPP-EFM, Pt-Ir coated) and sample. "
    "Devices were cleaved to expose a sufficiently flat cross section.",
    title="KPFM measurement configuration",
)

jv_measurement = setting(
    "Current-voltage measurements were performed in air using a Keithley 2400 device with controlled "
    "stage temperature of 25 degrees C under AM 1.5G illumination from LED-based solar simulator "
    "(WaveLabs SINUS-230). Spectral irradiance was measured using external spectrometer and adjusted "
    "to ensure mismatch factor around 1.00 plus/minus 0.01. Light intensity was calibrated to 1000 W/m^2 "
    "using Fraunhofer ISE CalLab-certified c-Si solar cells. J-V curves were obtained with step size "
    "of 10 mV and delay time of 10 ms. A black mask with aperture area of 1.0 cm^2 was used for each test.",
    title="J-V measurement configuration",
)

SunsVoc_measurement = setting(
    "Suns-Voc measurements were conducted using the WaveLabs SINUS-230 system. Suns-Voc directly "
    "measures Voc as a function of light intensity varying from approximately 0.01 to 1.1 suns. "
    "Final pseudo-J-V curves were obtained by shifting data at 1 sun to the Voc point.",
    title="Suns-Voc measurement configuration",
)

eqe_measurement = setting(
    "For EQE measurements of Si bottom subcell in tandem, green LED light with peak wavelength of "
    "525 nm was illuminated on the cell and 0.5 V bias voltage was applied. For perovskite top subcell, "
    "near-infrared LED with peak wavelength of 845 nm was illuminated on the cell with 0.5 V bias voltage.",
    title="EQE measurement configuration",
)

dft_calculation = setting(
    "DFT calculations were performed using projector-augmented wave method as implemented in Vienna "
    "ab initio simulation package code. Generalized gradient approximation with Perdew-Burke-Ernzerhof "
    "exchange-correlation functional and van der Waals interactions (DFT-D3 method) were used. "
    "K-meshes were 6x6x6 for bulk, 4x4x1 for slabs, and 2x2x1 for interfaces. Energy cut-offs were "
    "500 eV for bulk and 450 eV for slabs and interfaces.",
    title="DFT calculation parameters",
)
