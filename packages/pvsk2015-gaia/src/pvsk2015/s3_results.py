"""
Results module for Jeon2015 (Nature 2015).

This module covers the experimental results including:
- J-V characteristics for different compositions
- Phase stability and transition behavior
- XRD analysis
- Morphology results (SEM)
- EQE spectra
- Best device performance data

Key quantitative findings:
- Optimal composition: x=0.15 with PCE = 18.4% (best), 17.3% (average)
- Certified PCE: 17.9% by Newport
- Maximum Jsc: 22.0 mA/cm^2 at x=0.15
- Maximum Voc: 1.12 V at x=0.30
- Maximum FF: 73% at x=0.15
"""

from gaia.lang import (
    claim,
    setting,
    support,
    infer,
)

# =============================================================================
# PHOTOVOLTAIC PARAMETERS TABLE (KEY RESULTS)
# =============================================================================

table1_pce_trend = claim(
    "The power conversion efficiency (PCE) of (FAPbI3)1-x(MAPbBr3)x solar cells "
    "shows a maximum value of 17.3% at x=0.15, increasing from 0.5% at x=0 (annealed "
    "at 100 degrees C) to the maximum, then decreasing to 15.4% at x=0.30. The PCE "
    "trend follows the simultaneous enhancement of Jsc and FF, while Voc continues "
    "to increase with x due to bandgap widening [@Jeon2015].",
    title="PCE trend with composition x",
    metadata={
        "source_table": "artifacts/full.md, Table 1",
    },
)

table1_photovoltaic_parameters = claim(
    "Photovoltaic parameters for (FAPbI3)1-x(MAPbBr3)x solar cells:\n\n"
    "| x | Jsc (mA/cm^2) | Voc (V) | FF | PCE (%) | Series resistance (Ohm cm^2) |\n"
    "|---|---|---|---|---|---|\n"
    "| 0 (150 C anneal) | 22.0 | 0.88 | 0.70 | 13.5 | 5.7 |\n"
    "| 0 (100 C anneal) | 1.10 | 0.88 | 0.51 | 0.5 | 345 |\n"
    "| 0.05 | 17.1 | 1.02 | 0.65 | 11.3 | 6.0 |\n"
    "| 0.10 | 21.0 | 1.04 | 0.66 | 14.5 | 4.8 |\n"
    "| 0.15 | 22.0 | 1.08 | 0.73 | 17.3 | 3.9 |\n"
    "| 0.20 | 21.5 | 1.09 | 0.71 | 16.7 | 4.3 |\n"
    "| 0.25 | 21.0 | 1.10 | 0.69 | 15.9 | 4.9 |\n"
    "| 0.30 | 20.0 | 1.12 | 0.69 | 15.4 | 5.7 |\n\n"
    "All cells annealed at 100 C except x=0 which also had a 150 C condition. "
    "PCE values are averaged from reverse and forward J-V sweeps [@Jeon2015].",
    title="Complete photovoltaic parameters table",
    metadata={
        "source_table": "artifacts/full.md, Table 1",
    },
)

jsc_maximum = claim(
    "Jsc increases from 19.0 mA/cm^2 at x=0.05 to a maximum value of 22.0 mA/cm^2 "
    "at x=0.15, then decreases to 20.0 mA/cm^2 at x=0.30. The trend reflects the "
    "trade-off between charge-collection efficiency (higher at low x due to better "
    "phase stability) and light-harvesting efficiency (reduced at high x due to "
    "bandgap widening causing blue-shift of absorption onset) [@Jeon2015].",
    title="Jsc trend with composition",
)

voc_increases_with_x = claim(
    "Voc increases from 1.00 V at x=0.05 to 1.12 V at x=0.30 across the entire "
    "composition range. This increase is attributed to the widening of the bandgap "
    "as MAPbBr3 content increases (Br substituting I increases bandgap) [@Jeon2015].",
    title="Voc trend with composition",
)

ff_maximum = claim(
    "Fill factor (FF) shows exactly the same trend as Jsc, with a maximum value "
    "of 73% at x=0.15. The similarity in behavior supports the interpretation that "
    "FF is limited by charge-collection efficiency, which is reflected in the series "
    "resistance values: 345 Ohm cm^2 at x=0 (100 C anneal), decreasing to 3.9 Ohm cm^2 "
    "at x=0.15, then increasing again at higher x [@Jeon2015].",
    title="FF trend with composition",
)

series_resistance = claim(
    "Series resistance shows a strong inverse correlation with device performance. "
    "At x=0 with 100 C annealing, series resistance is 345 Ohm cm^2 (very high), "
    "which corresponds to very low Jsc (1.10 mA/cm^2) and low FF (0.51). At x=0.15, "
    "series resistance reaches its minimum of 3.9 Ohm cm^2, coinciding with maximum "
    "PCE (17.3%) and FF (73%). At x=0.30, series resistance increases to 5.7 Ohm cm^2 "
    "[@Jeon2015].",
    title="Series resistance trend with composition",
)

# =============================================================================
# HYSTERESIS BEHAVIOR
# =============================================================================

fapbi3_hysteresis = claim(
    "FAPbI3-based cells with x=0 and x=0.15 show negligible hysteresis even with "
    "a short scanning delay time of 40 ms, in contrast to MAPbI3 which exhibits "
    "large hysteresis. The small discrepancies related to scan direction for "
    "FAPbI3/MAPbBr3 systems disappear at longer delay times above 100 ms. This "
    "may be related to the balance between electron and hole transport within the "
    "perovskite layer [@Jeon2015].",
    title="Hysteresis behavior comparison",
)

# =============================================================================
# ABSORPTION SPECTRA
# =============================================================================

absorption_blue_shift = claim(
    "The ultraviolet-visible absorption spectra show a systematic shift of the "
    "absorption band edge to shorter wavelengths (blue-shift) when MAPbBr3 content "
    "increases. This is because Br has a larger electronegativity than I, which "
    "widens the bandgap of the mixed halide perovskite. The reduction of Jsc "
    "observed at x greater than 0.15 is directly related to this blue-shift of "
    "absorption onset and resulting reduced light-harvesting efficiency [@Jeon2015].",
    title="Absorption spectra blue-shift with increasing x",
)

# =============================================================================
# EQE SPECTRA
# =============================================================================

eqe_blue_shift = claim(
    "The external quantum efficiency (EQE) spectrum is blue-shifted when x "
    "increases, resulting in reduced Jsc at high x values. However, a relatively "
    "lower Jsc at x below 0.15 indicates that charge-collection efficiency is also "
    "low, because Jsc is proportional to the product of charge-collection efficiency "
    "and light-harvesting efficiency [@Jeon2015].",
    title="EQE spectra behavior",
)

eqe_plateau = claim(
    "For the best-performing device with x=0.15, the EQE spectrum shows a very "
    "broad plateau of over 80% between 400 nm and 750 nm. The Jsc value integrated "
    "from the EQE spectrum is in good agreement with that measured by J-V curve "
    "[@Jeon2015].",
    title="EQE plateau for best device",
)

# =============================================================================
# PHASE TRANSITION BEHAVIOR
# =============================================================================

dsc_phase_transition = claim(
    "Differential scanning calorimetry (DSC) of yellow FAPbI3 powder shows an "
    "endothermic peak around 160 degrees Celsius, which corresponds to the phase "
    "transition from yellow non-perovskite to black perovskite. This peak appears "
    "without any weight loss up to 250 degrees Celsius in thermogravimetric analysis, "
    "confirming it is a structural phase transition rather than decomposition. The "
    "XRD spectra measured in situ confirm this assignment of the endothermic peak "
    "[@Jeon2015].",
    title="DSC phase transition temperature",
)

phase_reversibility = claim(
    "The phase transition in FAPbI3 is reversible in air: the yellow non-perovskite "
    "phase changes to black perovskite when annealed at 170 degrees Celsius, and the "
    "black powder turns yellow again after being stored in air for 10 days. This "
    "reversibility indicates the yellow phase is thermodynamically stable at room "
    "temperature in ambient conditions [@Jeon2015].",
    title="FAPbI3 phase transition reversibility",
)

perovskite_polymorphs = claim(
    "FAPbI3 exists in two polymorphs: a black perovskite phase with trigonal symmetry "
    "(space group P3m1) and a yellow non-perovskite phase with hexagonal symmetry "
    "(space group P6_3mc). The black phase consists of a three-dimensional network "
    "of corner-sharing octahedra, while the yellow phase contains linear chains of "
    "[PbI6] octahedra with face-sharing. Only the black perovskite phase is "
    "photovoltaically active [@Jeon2015].",
    title="FAPbI3 polymorph structures",
)

# =============================================================================
# XRD RESULTS
# =============================================================================

xrd_nonperovskite_x0 = claim(
    "The XRD spectrum of pure FAPbI3 thin film (x=0) annealed at 100 degrees Celsius "
    "shows the typical diffraction pattern of hexagonal non-perovskite polymorph "
    "(P6_3mc), because 100 degrees Celsius is much lower than the 160 degrees Celsius "
    "phase transition temperature. This explains the poor photovoltaic performance "
    "[@Jeon2015].",
    title="Pure FAPbI3 XRD shows non-perovskite phase",
)

xrd_perovskite_x15 = claim(
    "When FA+ cations in FAPbI3 are substituted by 15 mol% of MA+ cations, a strong "
    "(111) diffraction peak at 13.9 degrees for the trigonal perovskite phase (P3m1) "
    "appears despite annealing at only 100 degrees Celsius. The same diffraction peaks "
    "are observed in systems containing Br- ions (15 mol%), although a secondary "
    "phase coexists in the film [@Jeon2015].",
    title="15 mol% MA substitution stabilizes perovskite phase",
)

synergetic_effect = claim(
    "A simultaneous introduction of 15 mol% of both MA+ cations and Br- anions in "
    "FAPbI3 to obtain (FAPbI3)0.85(MAPbBr3)0.15 leads to a synergetic effect that "
    "stabilizes the perovskite phase at 100 degrees Celsius. This combination is "
    "sufficient to form a FAPbI3 perovskite phase even at 5 mol% addition, although "
    "single MA+ or Br- substitution can only partially form the perovskite phase "
    "[@Jeon2015].",
    title="Synergetic effect of MA+ and Br- co-substitution",
)

fwhm_crystallinity = claim(
    "The full width at half maximum (FWHM) of the (-111) diffraction peak decreases "
    "for x greater than 0.15, indicating that a highly crystalline perovskite layer "
    "is formed at these compositions. The enhancement of phase stability and "
    "crystallinity results in improvement of PCE in the x range of 0 to 0.15 "
    "[@Jeon2015].",
    title="FWHM indicates improved crystallinity at x>0.15",
)

black_powder_only = claim(
    "Photographs of as-prepared powders show that black powder (perovskite phase) "
    "is obtained only for (FAPbI3)0.85(MAPbBr3)0.15 among all FAPbI3-based materials "
    "tested. XRD spectra of these powders confirm that only (FAPbI3)0.85(MAPbBr3)0.15 "
    "shows a pure perovskite phase with no endothermic DSC peaks [@Jeon2015].",
    title="Only mixed cation-anion composition yields pure perovskite powder",
)

# =============================================================================
# MORPHOLOGY RESULTS
# =============================================================================

sem_morphology_x0 = claim(
    "The surface of pure FAPbI3 (x=0) exhibits an irregular morphology with bumpy "
    "roughness when annealed at 150 degrees Celsius. This rough surface is due to "
    "the phase transition from non-perovskite to perovskite and the high temperature "
    "required for perovskite formation [@Jeon2015].",
    title="Pure FAPbI3 morphology is rough",
)

sem_morphology_x15 = claim(
    "Incorporating MAPbBr3 into FAPbI3 (x=0.15) considerably smooths the surface "
    "morphology, producing a uniform and dense morphology with well-developed "
    "crystallites. However, at x=0.05, large voids between crystal boundaries are "
    "still present. The improved morphology is responsible for the highly improved "
    "cell performance [@Jeon2015].",
    title="15 mol% MAPbBr3 produces smooth morphology",
)

# =============================================================================
# BEST DEVICE PERFORMANCE
# =============================================================================

best_device_jv = claim(
    "For the best-performing device with x=0.15 in the architecture "
    "FTO/blocking-TiO2 (70 nm)/mesoporous-TiO2 (200 nm)/perovskite (300 nm)/PTAA/Au, "
    "the J-V curves measured via reverse and forward bias sweep give averaged values: "
    "Jsc = 22.5 mA/cm^2, Voc = 1,105 mV, FF = 73.2%, corresponding to a PCE of "
    "18.4% under standard AM1.5G conditions. The PCE value is in agreement with that "
    "obtained from stabilized power output near the maximum power point "
    "(0.89 V) [@Jeon2015].",
    title="Best device J-V characteristics",
    metadata={
        "source_figure": "artifacts/full.md, Figure 3a",
    },
)

certified_pce = claim(
    "Devices exhibiting PCEs of 18.0% with very small hysteresis were certified by "
    "the standardized method in the photovoltaic calibration laboratory at Newport "
    "Corporation, confirming a PCE of 17.9% under AM1.5G full sun. This is the "
    "highest reported PCE for perovskite-based solar cells, excluding values "
    "overestimated by reverse bias scan [@Jeon2015].",
    title="Certified PCE by Newport",
    metadata={
        "source_figure": "artifacts/full.md, Extended Data Figure 8",
    },
)

hysteresis_80nm = claim(
    "For cells using a thinner mesoporous-TiO2 layer (80 nm), an unprecedented PCE "
    "of 20.3% was measured via reverse bias scan. However, the PCE of approximately "
    "17.3% obtained from average J-V curve and steady-state current measurement is far "
    "lower than the reverse-bias value, owing to a low PCE of 15.5% with forward bias "
    "scan. This result demonstrates that PCE should be obtained from J-V curves "
    "averaged with reverse and forward bias sweep, not from reverse-bias alone "
    "[@Jeon2015].",
    title="Thin mesoporous layer shows hysteresis issues",
    metadata={
        "source_figure": "artifacts/full.md, Extended Data Figure 7",
    },
)

__all__ = [
    "table1_pce_trend",
    "table1_photovoltaic_parameters",
    "jsc_maximum",
    "voc_increases_with_x",
    "ff_maximum",
    "series_resistance",
    "fapbi3_hysteresis",
    "absorption_blue_shift",
    "eqe_blue_shift",
    "eqe_plateau",
    "dsc_phase_transition",
    "phase_reversibility",
    "perovskite_polymorphs",
    "xrd_nonperovskite_x0",
    "xrd_perovskite_x15",
    "synergetic_effect",
    "fwhm_crystallinity",
    "black_powder_only",
    "sem_morphology_x0",
    "sem_morphology_x15",
    "best_device_jv",
    "certified_pce",
    "hysteresis_80nm",
]