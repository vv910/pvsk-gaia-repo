"""
Pb-Sn PSCs with 3D/3D bilayer PHJ - Methods and Device Architecture.

This module contains the device structure, fabrication methods, and
characterization techniques for mixed Pb-Sn PSCs with 3D/3D bilayer PHJ.
"""

from gaia.lang import (
    claim,
    setting,
)

#------------------------------------------------------------------------------
# Device structure
#------------------------------------------------------------------------------

device_architecture = setting(
    "The mixed Pb-Sn PSC with 3D/3D bilayer PHJ has a device structure of "
    "glass/ITO/PEDOT:PSS/perovskite/C60/BCP/Cu, where ITO is indium tin oxide, "
    "PEDOT:PSS is poly(3,4-ethylenedioxythiophene) polystyrene sulfonate, "
    "C60 is fullerene, and BCP is bathocuproine.",
    title="Device architecture of Pb-Sn PSC with PHJ",
)

fl_wbg_composition = setting(
    "The optimal FL-WBG perovskite composition is FA0.7Cs0.3Pb(I0.85Br0.14)3 with a "
    "thickness of 50 nm for the FL-WBG perovskite layer.",
    title="FL-WBG perovskite composition and thickness",
)

nbg_composition = setting(
    "The NBG perovskite has composition FA0.7MA0.3Pb0.5Sn0.5I3, where MA is methylammonium, "
    "with SnF2 (10 mol% relative to SnI2) added to the precursor solution to reduce Sn4+.",
    title="NBG perovskite composition",
)

#------------------------------------------------------------------------------
# Hybrid deposition process
#------------------------------------------------------------------------------

inorganic_layer_deposition = claim(
    "PbI2/CsBr is deposited on NBG perovskite films by dual-source co-evaporation at "
    "rates of 0.25 A/s and 0.1 A/s respectively (PbI2:CsBr rate ratio of 5:2), until the "
    "inorganic framework layer reaches approximately 30 nm thickness.",
    title="Inorganic PbI2/CsBr layer evaporation",
)

organic_salt_deposition = claim(
    "Organic salt (FAI:FABr = 1:1, 0.1 M in IPA) is deposited on the inorganic layer "
    "by two-step spin-coating (1000 rpm for 10 s, then 4000 rpm for 30 s), followed by "
    "heating at 100 C for 2 min and washing with IPA to remove excess organic salts.",
    title="Organic salt spin-coating and conversion",
)

peai_post_treatment = claim(
    "PEAI (1 mg/ml in IPA) is dynamically spin-coated on the FL-WBG layer and heated "
    "at 100 C for 30 s as a post-treatment, which slightly improves FF and PCE of PHJ devices.",
    title="PEAI post-treatment on FL-WBG layer",
)

#------------------------------------------------------------------------------
# Characterization methods
#------------------------------------------------------------------------------

morphology_method = claim(
    "The morphology and crystalline structure of PHJ-incorporated Pb-Sn perovskite films "
    "were investigated using scanning electron microscopy (SEM) and X-ray diffraction (XRD).",
    title="Morphology and structure characterization",
)

heterojunction_verification = claim(
    "The vertical structure of the PHJ was investigated using cross-sectional high-resolution "
    "scanning transmission electron microscopy (HR-STEM), energy-dispersive X-ray (EDX) mapping, "
    "and time-of-flight secondary-ion mass spectrometry (ToF-SIMS).",
    title="Heterojunction structure verification",
)

phj_layer_thickness = claim(
    "EDX mapping and ToF-SIMS results indicate a FL-WBG perovskite layer thickness "
    "of approximately 50 nm on top of the Pb-Sn perovskite, with stronger Pb2+ signal "
    "near the heterojunction surface and no noticeable Sn2+ signal in the FL-WBG layer.",
    title="PHJ layer thickness verification",
)

ion_distribution_stability = claim(
    "EDX and ToF-SIMS measurements show that the PHJ sample retains its distinct "
    "heterostructure after 60 days of storage in N2-filled glovebox, with no evidence "
    "of Sn2+ diffusion into the FL-WBG layer, although Br- easily diffuses into Pb-Sn perovskites.",
    title="PHJ structural stability over time",
)

#------------------------------------------------------------------------------
# Energy level characterization
#------------------------------------------------------------------------------

work_functions = claim(
    "UV photoemission spectroscopy measurements show work functions of 4.68 eV for Pb-Sn "
    "perovskite and 4.55 eV for FL-WBG perovskite, with valence band maxima of 5.27 eV "
    "and 5.79 eV respectively.",
    title="Work function and valence band measurements",
)

bandgaps = claim(
    "The optical bandgaps are 1.25 eV for Pb-Sn perovskite and 1.62 eV for FL-WBG perovskite, "
    "giving conduction band minima of 4.02 eV and 4.17 eV respectively (calculated from "
    "work function and valence band maximum).",
    title="Bandgap values for both perovskite layers",
)

#------------------------------------------------------------------------------
# Performance characterization
#------------------------------------------------------------------------------

jv_measurement = claim(
    "J-V characteristics were measured using a Keithley 2400 SourceMeter under AM 1.5G "
    "illumination at 100 mW cm^-2, with a scanning rate of 100 mV/s (voltage steps of 20 mV "
    "and delay time of 100 ms) in a nitrogen-filled glovebox.",
    title="J-V measurement conditions",
)

eqe_measurement = claim(
    "External quantum efficiency (EQE) measurements were performed in ambient air using "
    "a QE system with monochromatic light, and the integrated photocurrent was compared "
    "with J-V measurements.",
    title="EQE measurement method",
)

__all__ = [
    "device_architecture",
    "fl_wbg_composition",
    "nbg_composition",
    "inorganic_layer_deposition",
    "organic_salt_deposition",
    "peai_post_treatment",
    "morphology_method",
    "heterojunction_verification",
    "phj_layer_thickness",
    "ion_distribution_stability",
    "work_functions",
    "bandgaps",
    "jv_measurement",
    "eqe_measurement",
]