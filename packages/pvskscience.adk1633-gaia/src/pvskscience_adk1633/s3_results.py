"""
Section 3: PDAI2/3MTPA characteristics and photovoltaic performance.

This module covers DFT analysis of ligand binding, characterization of passivation effects,
photovoltaic performance metrics, and longevity studies.
"""

from gaia.lang import (
    claim, setting, support, infer, compare, deduction, abduction,
    induction, analogy, extrapolation, elimination, case_analysis,
    mathematical_induction, composite, contradiction, equivalence,
    complement, disjunction, infer
)

# Import from motivation for use within this module
from .motivation import diammonium_field_effect, methylthio_chemical_passivation, dual_passivation_concept, single_molecule_insufficient

# DFT binding energy for 3MTPA vs AA
binding_energy_3mtpa = claim(
    "Density functional theory (DFT) calculations showed a binding energy difference (delta-E_clean) of -0.22 eV for 3MTPA between parallel and vertical configurations, indicating stronger preference for parallel orientation compared with -0.13 eV for AA (amylammonium) [@Liu2024].",
    title="3MTPA has stronger binding preference",
)

# 3MTPA binding leads to greater occupation on vacancy defects
vacancy_defect_occupation = claim(
    "The larger delta-E_clean value for 3MTPA corresponds to greater occupation on the iodide vacancy defect position on the perovskite surface [@Liu2024].",
    title="3MTPA shows greater vacancy occupation",
)

# Electrostatic potential - lower phi_min for 3MTPA
phi_min_3mtpa = claim(
    "3MTPA has a lower minimum electrostatic potential (phi_min) than AA due to its electron-rich center surrounding the sulfur atom, which facilitates binding with the positively charged iodide vacancy [@Liu2024].",
    title="3MTPA has lower phi_min",
)

# Electrostatic potential - higher phi_max for 3MTPA
phi_max_3mtpa = claim(
    "3MTPA has a higher maximum electrostatic potential (phi_max) at the -NH3+ side compared with AA, which adds increased binding strength between the ligand and the surface cation vacancy site of the perovskite [@Liu2024].",
    title="3MTPA has higher phi_max",
)

# Relative binding energy with iodide vacancy
binding_vacancy_interaction = claim(
    "The binding energy difference (delta-E_relative) between defective surface and clean surface for 3MTPA is -0.38 eV, indicating favorable interaction with iodide vacancy defects. In contrast, AA binding energy remains nearly unchanged regardless of iodide vacancy presence [@Liu2024].",
    title="3MTPA binds favorably to iodide vacancies",
)

# Charge redistribution - S-Pb coordination bonding
spb_coordination = claim(
    "3MTPA induces notable charge redistribution that accumulates charges at the iodide vacancy, assigned to S-Pb coordination bonding, whereas AA does not show this coordination interaction [@Liu2024].",
    title="S-Pb coordination bonding with 3MTPA",
)

# Hydrogen bond formation with FA
hydrogen_bond_3mtpa = claim(
    "Charge transfer between 3MTPA and formamidinium (FA) was observed, accompanied by a shorter distance of 2.72 angstrom between the sulfur atom in 3MTPA and the hydrogen atom in FA, indicating hydrogen bond formation. In contrast, the distance between carbon in AA and hydrogen in FA was 3.33 angstrom [@Liu2024].",
    title="3MTPA forms hydrogen bond with FA",
)

# FA vacancy formation energy change
fa_vacancy_energy = claim(
    "The formation energy of the FA vacancy increased from -0.79 eV to -0.71 eV upon 3MTPA treatment, indicating reduced propensity for FA vacancy formation [@Liu2024].",
    title="FA vacancy formation energy increases with 3MTPA",
)

# NMR evidence for hydrogen bonding
nmr_hydrogen_bonding = claim(
    "Proton NMR spectra showed that the amino proton peak of FAI at delta = 8.82 ppm exhibited increased broadening and shifted to a lower field after mixing with 3MTPAI compared with AAI, indicating stronger hydrogen bonding interactions between 3MTPA and FA than between AA and FA [@Liu2024].",
    title="NMR evidence for stronger hydrogen bonding",
)

# XPS - Pb 4f peak shift
xps_pb_shift = claim(
    "X-ray photoelectron spectroscopy (XPS) showed that the Pb 4f peaks of the passivated perovskite film shifted toward a lower binding energy of 0.23 eV compared with the control film, attributed to increased electron density at Pb2+ from DMDP treatment [@Liu2024].",
    title="XPS Pb 4f peak shift confirms passivation",
)

# SIMS signal ratio analysis
sims_signal_ratio = claim(
    "Time-of-flight secondary ion mass spectrometry (ToF-SIMS) analysis showed a signal ratio of 1:2.7 for PDA:3MTPA, lower than the ratio of 1:1.1 for PDA:AA under identical conditions, suggesting that 3MTPA has stronger binding affinity to the perovskite surface and a better passivation effect on defects [@Liu2024].",
    title="SIMS confirms stronger 3MTPA binding",
)

# PL mapping - PDAI2/3MTPA shows higher PL
pl_intensity_mapping = claim(
    "Centimeter-scale photoluminescence (PL) intensity distribution showed that the region surrounding the PDAI2/3MTPA center exhibited higher PL emission than the corresponding region for PDAI2/AAI, with the lowest PL contour region skewed toward the PDAI2/AAI center [@Liu2024].",
    title="PL mapping shows higher emission with PDAI2/3MTPA",
)

# Morphology unchanged after DMDP
morphology_unchanged = claim(
    "Scanning electron microscopy (SEM) images revealed dense polygonal grains with sizes of approximately 500 nm for the control perovskite film, and morphologies were unchanged after DMDP passivation [@Liu2024].",
    title="Morphology unchanged after DMDP",
)

# No low-dimensional perovskite formed
no_low_dim_perovskite = claim(
    "Grazing-incidence wide-angle x-ray scattering (GIWAXS) did not reveal any peaks at low scattering vectors q in the DMDP-based film, indicating that no low-dimensional perovskite formed. The peak at approximately 0.84 angstrom^-1 in the control sample was assigned to delta-FAPbI3 formed in ambient humid air during measurement, and its suppression in the DMDP-based film indicates improved ambient stability [@Liu2024].",
    title="No low-dimensional perovskite; improved stability",
)

# TA spectra - single bleach feature
ta_single_bleach = claim(
    "Transient absorption (TA) spectra showed that the passivated film displayed a single bleach spectral feature from the three-dimensional perovskite, further corroborating that no low-dimensional perovskite formed [@Liu2024].",
    title="TA confirms 3D perovskite structure",
)

# TRPL - control lifetime
trpl_control_lifetime = claim(
    "Time-resolved photoluminescence (TRPL) measurements showed that control perovskite films had a sharp decrease in emission characteristic of high levels of nonradiative carrier recombination on the bare perovskite surface [@Liu2024].",
    title="Control film shows short carrier lifetime",
)

# TRPL - PDAI2 limited improvement
trpl_pda_limited = claim(
    "Treatment with PDAI2 showed little improvement in TRPL lifetime, reflecting its limited suppression of defect-induced surface recombination, consistent with its field-effect passivation role rather than chemical passivation [@Liu2024].",
    title="PDAI2 shows limited TRPL improvement",
)

# TRPL - 3MTPAI sustained plateau
trpl_3mtpai_plateau = claim(
    "The perovskite film treated with 3MTPAI displayed a sustained plateau in the TRPL decay curve, reflecting increased carrier lifetime, likely due to combined effect of reduced nonradiative traps and enhanced photon recycling [@Liu2024].",
    title="3MTPAI shows sustained TRPL plateau",
)

# UPS - energy level difference
ups_cbm_fermi = claim(
    "Ultraviolet photoelectron spectroscopy (UPS) characterization showed that PDAI2 treatment reduced the energy level difference between the conduction band minimum (E_CBM) and the Fermi level (E_F) of the perovskite surface to 0.10 eV, compared with 0.20 eV for control and 0.17 eV for 3MTPAI treatments [@Liu2024].",
    title="PDAI2 reduces CBM-Fermi level difference",
)

# Field-effect passivation from n-type doping
ntype_doping_field_effect = claim(
    "The stronger n-type doping effect of PDAI2, attributed to the additional -NH3+ group extending away from the perovskite matrix, induces a surface dipole that repels minority carriers at the interface, enabling field-effect passivation and reducing interface recombination [@Liu2024].",
    title="PDAI2 enables field-effect passivation via n-type doping",
)

# DMDP improves PLQY
plqy_improvement = claim(
    "The DMDP strategy improved photoluminescence quantum yield (PLQY) of the perovskite/C60 samples and increased PCE to >26% even at 12 mM concentration of 3MTPAI, without interference between 3MTPAI and PDAI2 [@Liu2024].",
    title="DMDP improves PLQY and PCE",
)

# 3MTPAI and PDAI2 do not interfere
no_interference = claim(
    "3MTPAI and PDAI2 could increase passivation and decrease carrier recombination without interfering with one another: PDAI2 does not enhance PLQY before C60 deposition but limits PLQY loss after C60 coating, whereas 3MTPAI increases PLQY before C60 but shows losses after C60, and DMDP combines both advantages [@Liu2024].",
    title="3MTPAI and PDAI2 do not interfere",
)

# Photovoltaic parameters summary
photovoltaic_params = claim(
    "DMDP-based devices showed improved PCE from 22.8 +/- 0.4% to 25.5 +/- 0.3% compared with control devices, with enhancements in open-circuit voltage (V_OC) from 1.12 +/- 0.01 V to 1.16 +/- 0.01 V and fill factor (FF) from 78.5 +/- 1.3% to 83.8 +/- 1.3% [@Liu2024].",
    title="DMDP improves PCE to 25.5 +/- 0.3%",
)

# Dark saturation current reduction
dark_saturation_current = claim(
    "Diode characteristics in the absence of light showed that DMDP-based devices presented an average dark saturation current (J0) reduction by two orders of magnitude compared with control devices, demonstrating effective inhibition of carrier recombination [@Liu2024].",
    title="DMDP reduces dark saturation current by 2 orders",
)

# Champion device J-V
champion_device_jv = claim(
    "The champion DMDP device exhibited a PCE of 26.4% with short-circuit current (J_SC) of 26.2 mA/cm^2, V_OC of 1.17 V, and FF of 85.8% [@Liu2024].",
    title="Champion device PCE 26.4%",
)

# QSS PCE certification
qss_pce_certification = claim(
    "NREL certification using the asymptotic maximum power scan protocol reported a quasi-steady-state (QSS) PCE of 25.1% for an illuminated area of 0.05 cm^2, along with a fast-scan PCE of 25.9%, surpassing other reported certified QSS PCEs that did not exceed 25% [@Liu2024].",
    title="NREL certified QSS PCE 25.1%",
)

# Larger area device
large_area_device = claim(
    "1.5 cm^2 devices using DMDP treatment delivered a PCE of 24.0%, consistent with increased film homogeneity and reduced localized nonradiative recombination [@Liu2024].",
    title="1.5 cm^2 device PCE 24.0%",
)

# Thermal stability - 1600 hours at 85C
thermal_stability = claim(
    "After 1600 hours of thermal aging at 85 degrees C in nitrogen (ISOS-D-2 protocol), DMDP-based devices retained 95% of initial PCE, surpassing the retention of 84% for control devices [@Liu2024].",
    title="Thermal stability: 95% retention after 1600h at 85C",
)

# Operating stability - 2000 hours at 65C
operating_stability = claim(
    "After 2000 hours of continuous operation under 1 sun illumination at 65 degrees C in ambient air (ISOS-L-3 protocol), the DMDP-based device maintained 96% of original PCE, whereas the control device was reduced to 70% of initial PCE [@Liu2024].",
    title="Operating stability: 96% retention after 2000h at 65C",
)

# DMDP works on other perovskite compositions
universality_wbg = claim(
    "The DMDP strategy improved the average PCE of wide bandgap (WBG) PSCs by 13%, demonstrating applicability to other perovskite compositions [@Liu2024].",
    title="DMDP improves WBG PSC PCE by 13%",
)

# DMDP works on NBG perovskite
universality_nbg = claim(
    "The DMDP strategy improved the average PCE of narrow bandgap (NBG) PSCs by 14%, demonstrating applicability to other perovskite compositions [@Liu2024].",
    title="DMDP improves NBG PSC PCE by 14%",
)

# Tandem device architecture
tandem_architecture = claim(
    "Monolithic all-perovskite tandem solar cells were fabricated with the structure FTO/NiOx/Me-4PACz/WBG perovskite/C60/SnOx/Au/PEDOT:PSS/NBG perovskite/C60/SnOx/Ag [@Liu2024].",
    title="Tandem device architecture",
)

# Tandem device performance
tandem_pce = claim(
    "The champion tandem device with illuminated area of 0.05 cm^2 exhibited a PCE of 28.1% with V_OC of 2.14 V, J_SC of 15.6 mA/cm^2, and FF of 84.0%, with a stabilized PCE of 27.1% under maximum power point tracking [@Liu2024].",
    title="Tandem device PCE 28.1%",
)

# DMDP working principle - combined effect
strat_dmdp_combined_effect = support(
    [diammonium_field_effect, methylthio_chemical_passivation],
    plqy_improvement,
    reason="PDAI2 provides field-effect passivation by repelling minority carriers through n-type doping, while 3MTPAI provides chemical passivation by binding to defects through S-Pb coordination and hydrogen bonding. Together they achieve improved PLQY and PCE without interfering with one another [@Liu2024].",
    prior=0.5,
)

# DMDP enables high PCE
strat_dmdp_enables_high_pce = support(
    [photovoltaic_params, qss_pce_certification],
    champion_device_jv,
    reason="The certified QSS PCE of 25.1% and the improved photovoltaic parameters (V_OC, FF) jointly support the champion device PCE of 26.4% [@Liu2024].",
    prior=0.5,
)

# DMDP enables stability
strat_dmdp_enables_stability = support(
    [thermal_stability, operating_stability],
    dual_passivation_concept,
    reason="Thermal stability (95% retention after 1600h at 85C) and operating stability (96% retention after 2000h at 65C) demonstrate that the combined chemical and field-effect passivation effectively addresses both surface and interface recombination for long-term device stability [@Liu2024].",
    prior=0.5,
)

# Abduction: DMDP vs control for efficiency
obs_quasi_steady_state_pce = claim(
    "The observed quasi-steady-state PCE for DMDP devices is 25.1% certified by NREL, whereas control devices are limited to approximately 22.8% PCE under the same QSS protocol [@Liu2024].",
    title="Observed QSS PCE advantage",
)

alt_control_single_molecule = claim(
    "Single-molecule passivation (using only chemical or only field-effect passivation) limits inverted PSCs to approximately 24.5% PCE under QSS protocol, as previously reported in literature [@Liu2024].",
    title="Alternative: single-molecule passivation",
)

pred_dmdp = claim(
    "DMDP (bimolecular passivation with both chemical and field-effect mechanisms) predicts PCE >25% QSS for inverted PSCs [@Liu2024].",
    title="DMDP prediction: >25% QSS PCE",
)

pred_single = claim(
    "Single-molecule passivation predicts PCE approximately 24.5% QSS for inverted PSCs [@Liu2024].",
    title="Single-molecule prediction: ~24.5% QSS",
)

s_dmdp = support(
    [pred_dmdp],
    obs_quasi_steady_state_pce,
    reason="Bimolecular passivation with both chemical and field-effect mechanisms addresses both surface and interface recombination, predicting PCE >25% QSS, which would explain the observed 25.1% certified PCE",
    prior=0.85,
)

s_alt = support(
    [pred_single],
    obs_quasi_steady_state_pce,
    reason="Single-molecule passivation cannot address both recombination processes simultaneously, limiting inverted PSCs to approximately 24.5% PCE, which would explain the observation",
    prior=0.4,
)

comp = compare(
    pred_dmdp,
    pred_single,
    obs_quasi_steady_state_pce,
    reason="NREL-certified QSS PCE of 25.1% for DMDP devices versus approximately 24.5% for single-molecule passivation confirms DMDP's superior efficiency",
    prior=0.9,
)

abd_dmdp_vs_single = abduction(s_dmdp, s_alt, comp,
    reason="Both DMDP and single-molecule passivation attempt to explain the observed QSS PCE; DMDP better explains the observed 25.1% certified efficiency")

__all__ = [
    "binding_energy_3mtpa",
    "vacancy_defect_occupation",
    "phi_min_3mtpa",
    "phi_max_3mtpa",
    "binding_vacancy_interaction",
    "spb_coordination",
    "hydrogen_bond_3mtpa",
    "fa_vacancy_energy",
    "nmr_hydrogen_bonding",
    "xps_pb_shift",
    "sims_signal_ratio",
    "pl_intensity_mapping",
    "morphology_unchanged",
    "no_low_dim_perovskite",
    "ta_single_bleach",
    "trpl_control_lifetime",
    "trpl_pda_limited",
    "trpl_3mtpai_plateau",
    "ups_cbm_fermi",
    "ntype_doping_field_effect",
    "plqy_improvement",
    "no_interference",
    "photovoltaic_params",
    "dark_saturation_current",
    "champion_device_jv",
    "qss_pce_certification",
    "large_area_device",
    "thermal_stability",
    "operating_stability",
    "universality_wbg",
    "universality_nbg",
    "tandem_architecture",
    "tandem_pce",
    "strat_dmdp_combined_effect",
    "strat_dmdp_enables_high_pce",
    "strat_dmdp_enables_stability",
    "obs_quasi_steady_state_pce",
    "alt_control_single_molecule",
    "pred_dmdp",
    "pred_single",
    "s_dmdp",
    "s_alt",
    "comp",
    "abd_dmdp_vs_single",
]