"""
Burschka2013: Methods and experimental section.

This module captures the device fabrication, characterization methods, and stability testing.
"""

from gaia.lang import claim, setting

# === Device Fabrication Setup ===

device_structure = setting(
    "The photovoltaic device structure consists of: FTO-coated glass substrate (front contact), "
    "30-40 nm TiO2 compact layer (aerosol spray pyrolysis), 350 nm mesoporous TiO2 layer "
    "(20-nm-sized anatase particles), perovskite infiltrant, spiro-MeOTAD hole-transporting "
    "material (HTM), and 80 nm Au back contact [@Burschka2013].",
    title="Device structure configuration",
)

mesoporous_tio2_deposition = setting(
    "Mesoporous TiO2 films composed of 20-nm-sized particles are deposited by spin coating "
    "at 5,000 rpm for 30 s using TiO2 paste (Dyesol 18NRT) diluted in ethanol (2:7 weight ratio), "
    "followed by drying at 125 C and annealing at 500 C for 15 min [@Burschka2013].",
    title="Mesoporous TiO2 deposition protocol",
)

pbi2_infiltration = setting(
    "PbI2 is dissolved in N,N-dimethylformamide (DMF) at a concentration of 462 mg/ml (~1 M) "
    "under stirring at 70 C. The mesoporous TiO2 films are infiltrated by spin coating at "
    "6,500 rpm for 90 s, then dried at 70 C for 30 min [@Burschka2013].",
    title="PbI2 infiltration protocol",
)

mai_conversion = setting(
    "After PbI2 infiltration, films are dipped in a solution of CH3NH3I in 2-propanol (10 mg/ml) "
    "for 20 s, rinsed with 2-propanol, and dried at 70 C for 30 min to convert PbI2 to "
    "CH3NH3PbI3 perovskite [@Burschka2013].",
    title="Methylammonium iodide conversion protocol",
)

htm_deposition = setting(
    "The HTM is deposited by spin coating at 4,000 rpm for 30 s using a solution of "
    "spiro-MeOTAD (72.3 mg), 4-tert-butylpyridine (28.8 ul), lithium bis(trifluoromethylsulphonyl)"
    "imide (17.5 ul of 520 mg/ml in acetonitrile), and Co(III) dopant (29 ul of 300 mg/ml in "
    "acetonitrile) in 1 ml chlorobenzene [@Burschka2013].",
    title="HTM spin-coating formulation",
)

best_device_modification = claim(
    "For the best-performing devices (15% PCE), the PbI2 is spin-cast at 6,500 rpm for 5 s "
    "(instead of 90 s), and samples are pre-wetted by dipping in 2-propanol for 1-2 s before "
    "the CH3NH3I conversion step [@Burschka2013].",
    title="Modified conditions for best-performing devices",
)

# === Characterization Methods ===

j_v_measurement = setting(
    "Current-voltage characteristics are measured under simulated AM1.5G solar irradiation "
    "using a 450 W xenon lamp with Schott K113 Tempax sunlight filter. Light intensity is "
    "calibrated using a calibrated Si reference diode with KG-3 infrared cut-off filter. "
    "Devices are measured using a 0.285 cm^2 metal aperture [@Burschka2013].",
    title="J-V characterization method",
)

ipce_measurement = setting(
    "IPCE spectra are recorded as functions of wavelength under constant white light bias "
    "(approximately 5 mW/cm^2) from an array of white LEDs. The excitation beam from a "
    "300 W xenon lamp is focused through a Gemini-180 double monochromator and chopped "
    "at approximately 2 Hz, detected with an SR830 DSP Lock-In Amplifier [@Burschka2013].",
    title="IPCE measurement method",
)

stability_testing = setting(
    "For long-term stability tests, devices are sealed in argon using a 50-mm-thick hot-melting "
    "polymer and microscope coverslip. Devices are subjected to constant light soaking at "
    "approximately 100 mW/cm^2 using white LED array (Philips LXM3-PW51 4000K), maintained at "
    "maximum power point, at approximately 45 C. J-V measurements at different light "
    "intensities are recorded automatically every 2 h [@Burschka2013].",
    title="Long-term stability test protocol",
)

optical_spectroscopy = setting(
    "Optical absorption measurements are carried out using a Varian Cary 5 spectrophotometer. "
    "Photoluminescence is measured on a Horiba Jobin Yvon Fluorolog spectrofluorometer. "
    "Samples are placed vertically in a 10 mm path length cuvette [@Burschka2013].",
    title="Optical spectroscopy methods",
)

xrd_measurement = setting(
    "X-ray powder diagrams are recorded on an X'Pert MPD PRO (PANalytical) with Cu anode "
    "(lambda = 1.54060 A), graphite (002) monochromator, and RTMS X'Celerator detector in "
    "BRAGG-BRENTANO geometry. Step size is 0.008 deg with acquisition time up to 7.5 min/deg "
    "[@Burschka2013].",
    title="XRD measurement parameters",
)

__all__ = [
    "device_structure",
    "mesoporous_tio2_deposition",
    "pbi2_infiltration",
    "mai_conversion",
    "htm_deposition",
    "best_device_modification",
    "j_v_measurement",
    "ipce_measurement",
    "stability_testing",
    "optical_spectroscopy",
    "xrd_measurement",
]