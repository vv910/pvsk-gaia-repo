from gaia.lang import (
    claim,
    setting,
    support,
    compare,
    deduction,
    abduction,
    induction,
)

__all__ = [
    "jsc_vs_tio2_thickness",
    "voc_vs_tio2_thickness",
    "ff_vs_tio2_thickness",
    "pce_vs_tio2_thickness",
    "dark_current_scaled_linearly",
    "electron_lifetime_decreased",
    "band_edge_emission_780nm",
    "exciton_decay_multiexponential",
    "reductive_quenching_observed",
    "hole_injection_mechanism",
    "recombination_resistance_decreased",
]


# ===== PHOTOVOLTAIC PERFORMANCE VS TIO2 THICKNESS =====

jsc_vs_tio2_thickness = claim(
    "The short-circuit current density (JSC) is not strongly dependent on TiO2 film thickness, with JSC values of 16-17 mA/cm^2 obtainable within the film thickness range of 0.6-1.4 micrometers.",
    title="JSC largely independent of TiO2 thickness"
)

voc_vs_tio2_thickness = claim(
    "The open-circuit voltage (VOC) decreases from approximately 0.9 V to approximately 0.85 V as the TiO2 film thickness increases to 0.8 micrometers, and further decreases to around 0.8 V when the film thickness exceeds 1.2 micrometers. VOC starts to decline significantly from 1.5 micrometers.",
    title="VOC decreases with increasing TiO2 thickness"
)

ff_vs_tio2_thickness = claim(
    "The fill factor (FF) gradually decreases with increasing TiO2 film thickness, as a consequence of the lower VOC and an increase in electron transport resistance.",
    title="FF decreases with increasing TiO2 thickness"
)

pce_vs_tio2_thickness = claim(
    "Due to diminishing VOC and FF, the power conversion efficiency (PCE) clearly decreases with increasing TiO2 film thickness. The thinnest film of 0.6 micrometers delivers a PCE of over 9%, and more than 8% can be achieved from thicknesses less than 1 micrometer.",
    title="PCE decreases with increasing TiO2 thickness"
)


# ===== IMPEDANCE SPECTROSCOPY RESULTS =====

dark_current_scaled_linearly = claim(
    "The dark current scaled nearly linearly with the thickness of the mesoporous TiO2 layer.",
    title="Dark current scales linearly with TiO2 thickness"
)

recombination_resistance_decreased = claim(
    "The charge transfer resistance (RCT) near short circuit is dominated by the interface between the hole conductor and the under-layer. Under forward bias (V_applied > 500 mV), RCT drops steeply with increasing forward bias because dark current is now dominated by electron flow across the photo-anode interface to the hole conductor.",
    title="Recombination resistance behavior"
)

electron_lifetime_decreased = claim(
    "The calculated electron lifetime (tau_n = C_A x R_CT) shows a faster decline at higher forward bias with increasing TiO2 thickness, leading to the observed overall reduction in delta_VOC.",
    title="Electron lifetime decreases with TiO2 thickness"
)


# ===== SPECTROSCOPY RESULTS =====

band_edge_emission_780nm = claim(
    "A powder of CH3NH3PbI3 shows a band edge emission centered at 780 nm.",
    title="Band edge emission at 780 nm"
)

exciton_decay_multiexponential = claim(
    "The emission decay of CH3NH3PbI3 examined by single photon counting technique showed multiexponential decay with lifetimes of 78 ns and 350 ns, assigned to radiative decay of excitons in CH3NH3PbI3.",
    title="Multiexponential exciton decay with 78 ns and 350 ns lifetimes"
)

reductive_quenching_observed = claim(
    "On Al2O3 samples, the amplitude of the bleaching signal at 483 nm was smaller than on samples deprived of HTM. The positive absorption signal in the 630-700 nm region completely disappeared, with strong quenching of stimulated emission above 700 nm. These results suggest a rapid reductive quenching of the excited state of the perovskite by the hole-transporting material.",
    title="Rapid reductive quenching by HTM observed"
)

hole_injection_mechanism = claim(
    "The transient spectrum of the HTM/CH3NH3PbI3/TiO2 sample exhibits the same features as the sample without HTM, but with the bleaching peak in the 480 nm region being less pronounced and the stimulated emission peak clearly attenuated in the presence of HTM, pointing toward the reductive quenching of the perovskite.",
    title="Hole injection from perovskite to HTM confirmed"
)


# ===== TiO2 THICKNESS STUDY =====

# These are used to build the impedance understanding
delta_voc_reduction = claim(
    "The decrease in VOC with increasing TiO2 thickness is attributed to the increase in dark current augmenting linearly with film thickness, which lowers the electron concentration under illumination and hence their quasi-Fermi level.",
    title="VOC decrease explained by dark current"
)