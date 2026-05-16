"""
s3_results.py - Experimental Results for perovskite solar cells

This module covers the key experimental results including device performance,
spectroscopic characterization, and charge transport measurements.
"""
from gaia.lang import claim, setting

# ============ Device Performance Results ============

# Al2O3 best device performance
al2o3_best_device = claim(
    "The most efficient Al2O3-based device exhibited short-circuit photocurrent "
    "(Jsc) = 17.8 mA cm^-2, open-circuit voltage (Voc) = 0.98 V, fill factor of 0.63, "
    "yielding overall power conversion efficiency (eta) = 10.9% under simulated AM1.5 "
    "full solar illumination [@Lee2012].",
    title="Best Al2O3 MSSC device performance"
)

# TiO2 sensitized device
tio2_device = claim(
    "The sensitized TiO2 solar cell exhibited Jsc = 17.8 mA cm^-2, Voc = 0.80 V, "
    "fill factor of 0.53, yielding overall power conversion efficiency of 7.6% under "
    "simulated AM1.5 illumination [@Lee2012].",
    title="TiO2 sensitized device performance"
)

# High Voc Al2O3 device
al2o3_high_voc_device = claim(
    "An Al2O3-based device exhibited Jsc = 15.4 mA cm^-2 and Voc = 1.13 V but with "
    "a low fill factor of 0.45, yielding eta = 7.8% [@Lee2012].",
    title="Al2O3 device with high Voc"
)

# Planar junction diode
planar_junction = claim(
    "A planar-junction diode with structure FTO/compact TiO2/CH3NH3PbI2Cl/spiro-OMeTAD/Ag "
    "(perovskite film ~150 nm thick) exhibited Jsc = 7.13 mA cm^-2, Voc = 0.64 V, "
    "fill factor of 0.4, and eta = 1.8% [@Lee2012].",
    title="Planar junction diode performance"
)

# Voc improvement trend
voc_improvement = claim(
    "The Al2O3 cells generated open-circuit voltages more than 200 mV higher than "
    "sensitized TiO2 solar cells, with comparable short-circuit currents and slightly "
    "lower fill factors [@Lee2012].",
    title="Voc improvement with Al2O3 scaffold"
)

# IPCE results
ipce_spectral_range = claim(
    "Both TiO2- and Al2O3-based devices exhibited spectral sensitivity spanning from "
    "visible to near-IR (400 to 800 nm) with peak IPCE > 80% for both oxides [@Lee2012].",
    title="IPCE spectral response"
)

# Optical band gap
optical_bandgap = claim(
    "The optical band gap of CH3NH3PbI2Cl is 1.55 eV, determined from IPCE onset "
    "at 800 nm [@Lee2012].",
    title="Perovskite optical band gap"
)

# Voltage deficit
voltage_deficit = claim(
    "With optical band gap of 1.55 eV and open-circuit voltage of 1.1 V, the "
    "difference in energy is only 0.45 eV, competitive with the best thin-film "
    "technologies [@Lee2012].",
    title="Small voltage deficit"
)

# ============ Spectroscopic Results ============

# UV-Vis absorbance
absorbance_capability = claim(
    "Absorption spectra demonstrated good light-harvesting capabilities over the "
    "visible to near-IR spectrum, with the film at 500 nm having absorbance around "
    "1.8 (98.4% absorption) [@Lee2012].",
    title="Absorbance spectrum"
)

# Photostability
photostability = claim(
    "The perovskite absorber was stable to prolonged light exposure, demonstrated "
    "by 1000 hours of constant illumination under simulated full sunlight with "
    "absorbance at 500 nm remaining around 1.8 throughout [@Lee2012].",
    title="Long-term photostability"
)

# PIA results - TiO2 sensitization
tio2_sensitization = claim(
    "PIA spectrum for mesoporous TiO2 film coated with perovskite revealed features "
    "in the near-IR assigned to free electrons in titania, confirming effective "
    "sensitization of titania by the perovskite [@Lee2012].",
    title="Effective TiO2 sensitization"
)

# PIA results - Al2O3 insulation
al2o3_insulating = claim(
    "Films of Al2O3 coated with perovskite exhibited no PIA signal, confirming the "
    "insulating role of alumina - electrons remain in the perovskite phase "
    "[@Lee2012].",
    title="Al2O3 acts as insulator"
)

# PIA - hole transfer efficiency
hole_transfer_effective = claim(
    "After addition of spiro-OMeTAD, absorption features at 525, 750, and 1200 nm "
    "assigned to hole on triarylamine moieties dominated the spectra for both TiO2 "
    "and Al2O3 samples, indicating hole transfer is highly effective from "
    "photoexcited perovskite to spiro-OMeTAD [@Lee2012].",
    title="Hole transfer to spiro-OMeTAD"
)

# PIA - hole conductor requirement
hole_conductor_required = claim(
    "A hole conductor is required to enable long-lived charge species within the "
    "perovskite coated on Al2O3 [@Lee2012].",
    title="Hole conductor requirement for MSSC"
)

# ============ Charge Transport Results ============

# Charge collection comparison
charge_collection_speed = claim(
    "Charge collection in Al2O3-based devices was faster than in TiO2-based "
    "sensitized devices by a factor > 10, indicating faster electron diffusion "
    "through the perovskite phase than through n-type TiO2 [@Lee2012].",
    title="Faster charge collection with Al2O3"
)

# Planar junction planarjunction_semiconducting
perovskite_semicondo = claim(
    "The construction of a planar-junction diode demonstrates the 'semiconducting' "
    "nature of the perovskite, which can function as both absorber and n-type "
    "component transporting electronic charge out of the device [@Lee2012].",
    title="Perovskite as semiconductor"
)

# Chemical capacitance difference
chemical_capacitance = claim(
    "For mesoporous TiO2, sites in the tail of density of states extend into the "
    "band gap, causing the quasi-Fermi level for electrons (EFn*) to be farther from "
    "conduction band than in highly crystalline semiconductor. This 'chemical "
    "capacitance' allows more charge storage. In Al2O3-based MSSCs, all electronic "
    "charge resides in the perovskite, moving EFn* nearer to conduction band for "
    "same charge density [@Lee2012].",
    title="Chemical capacitance mechanism for Voc improvement"
)

# TiO2 chemical capacitance explanation
tio2_chemical_capacitance = claim(
    "The increased voltage in TiO2 devices arises from chemical capacitance of "
    "sub-band gap states in the disordered TiO2, while Al2O3 has essentially no "
    "chemical capacitance [@Lee2012].",
    title="TiO2 sub-band gap states cause voltage loss"
)

# Compact TiO2 layer
compact_tio2 = setting(
    "A compact layer of TiO2 (50-100 nm thick) deposited via spray pyrolysis serves "
    "as electron-selective anode with donor density of approximately 10^18 cm^-3 "
    "[@Lee2012]."
)

# MSSC definition
mssc_definition = claim(
    "Because there is no n-type oxide in Al2O3-based cells, these devices are "
    "not 'sensitized' solar cells but rather two-component hybrid solar cells called "
    "'meso-superstructured solar cells' (MSSC) where Al2O3 acts as a mesoscale "
    "scaffold [@Lee2012].",
    title="MSSC definition and principle"
)

__all__ = [
    # Device performance
    "al2o3_best_device",
    "tio2_device",
    "al2o3_high_voc_device",
    "planar_junction",
    "voc_improvement",
    "ipce_spectral_range",
    "optical_bandgap",
    "voltage_deficit",
    # Spectroscopic
    "absorbance_capability",
    "photostability",
    "tio2_sensitization",
    "al2o3_insulating",
    "hole_transfer_effective",
    "hole_conductor_required",
    # Charge transport
    "charge_collection_speed",
    "perovskite_semicondo",
    "chemical_capacitance",
    "tio2_chemical_capacitance",
    "compact_tio2",
    "mssc_definition",
]