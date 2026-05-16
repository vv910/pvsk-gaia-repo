"""
Priors for pvskscience.aay7044 (Min2019, Science 366, 749).

Assigns priors to independent leaf claims: experimental observations,
theoretical predictions, method descriptions, and background facts.
"""

from .motivation import (
    perovskite_structure,
    fapbi3_bandgap,
    alpha_delta_transition,
    mixed_cation_problem,
    mda_properties,
    research_question,
    mapbbr3_control_efficiency,
    fapbi3_stabilization_history,
)
from .s2_methods import (
    deposition_method,
    surface_passivation,
    device_structure,
    uvvis_absorption,
    pl_spectra,
    ftir_confirms_mda,
    xrd_phase_analysis,
    giwaxs_analysis,
    xps_cl_content,
    tofsims_cl_mapping,
    defect_density_sclc,
    pl_lifetime,
    j_v_measurement,
    eqe_spectral_response,
    stability_test_protocols,
    dft_bandgap_calculation,
    xrd_peak_shift,
)
from .s3_results import (
    uvvis_blue_shift,
    pl_peak_shifts,
    bandgap_values,
    dft_bandgap_fa_vacancy,
    dft_bandgap_cl_interstitial,
    pl_quality_enhancement,
    humidity_phase_stability,
    alpha_phase_retention_38,
    alpha_phase_retention_57,
    crystallinity_improvement,
    giwaxs_no_impurity,
    xrd_peak_lower_angle,
    pce_distributions,
    target_best_jv,
    certified_pce,
    highest_jsc,
    eqe_expanded_range,
    morphology_unchanged,
    electron_trap_density,
    hole_trap_reduction,
    carrier_lifetime_target,
    cl_enriched_interface,
    humidity_stability,
    thermal_stability,
    photostability,
    optimal_composition,
    mda_superior_to_mapbbr3,
)
from .s4_discussion import (
    stabilization_mechanism_h_bonding,
    stabilization_mechanism_entropic,
    stabilization_mechanism_tolerance_factor,
    stabilization_mechanism_cl_interstitial,
    v_fa_defects_shallow,
    phase_stability_summary,
    cl_interface_photostability,
    photostability_mechanism,
    literature_comparison,
    aberration_free_stability,
    conclusion_alpha_stabilization,
    conclusion_no_tradeoff,
)

# Settings: no priors needed (they are mathematical/background facts)
# research_question: no prior (it is a question, not a claim)

PRIORS: dict = {
    # ── Motivation / background claims ──────────────────────────────────────────
    mapbbr3_control_efficiency: (
        0.90,
        "Directly reported certified result from an accredited laboratory (Newport, USA), "
        "representing the prior best-in-class mp-TiO2 PSC efficiency at time of publication."
    ),
    fapbi3_stabilization_history: (
        0.85,
        "Literature review of prior stabilization approaches with multiple supporting references; "
        "accurate summary of the state of the field before this work."
    ),

    # ── Methods claims ─────────────────────────────────────────────────────────
    deposition_method: (
        0.90,
        "Standard perovskite film deposition protocol described in detail with reference to "
        "prior art; process is reproducible and well-characterized."
    ),
    surface_passivation: (
        0.85,
        "Surface passivation methods are well-established in the literature and directly "
        "reported by the authors with appropriate references."
    ),
    device_structure: (
        0.90,
        "Standard device architecture (FTO/SnO2/mp-TiO2/perovskite/HTM/Au) is a well-known "
        "regular PSC structure; CuPC HTM choice for thermal tests is explicitly justified."
    ),
    uvvis_absorption: (
        0.92,
        "UV-vis absorption is a standard spectroscopic measurement with clear protocol; "
        "quantitative peak positions are directly reported."
    ),
    pl_spectra: (
        0.92,
        "PL emission peaks are directly measured spectroscopic values with high precision; "
        "consistent trend across compositions confirms reliability."
    ),
    ftir_confirms_mda: (
        0.80,
        "FT-IR and NMR are standard analytical methods confirming MDA presence; direct "
        "measurement with clear interpretation of organic incorporation."
    ),
    xrd_phase_analysis: (
        0.93,
        "XRD is a standard phase identification technique; characteristic peak positions "
        "(14.3, 28.6, 11.6 degrees) directly reveal alpha vs delta phase content."
    ),
    giwaxs_analysis: (
        0.85,
        "GIWAXS is a quantitative structural technique; ring patterns and fitted 1D spectra "
        "confirm phase purity with no secondary phases detected."
    ),
    xps_cl_content: (
        0.82,
        "XPS is a standard surface-sensitive technique for elemental analysis; Cl enrichment "
        "at TiO2 interface is a semiquantitative but reliable finding."
    ),
    tofsims_cl_mapping: (
        0.80,
        "ToF-SIMS is a standard depth profiling technique; qualitative Cl distribution is "
        "reliable, though quantification has known limitations."
    ),
    defect_density_sclc: (
        0.82,
        "SCLC is a standard method for trap density; the trap-filled limit voltage is "
        "directly measurable; N_defects calculation follows standard equations with "
        "known material parameters."
    ),
    pl_lifetime: (
        0.88,
        "TRPL with time-correlated single-photon counting is a standard technique; "
        "biexponential fit is physically motivated; lifetime values are directly reported."
    ),
    j_v_measurement: (
        0.93,
        "J-V characterization under AM 1.5 is the standard PSC measurement protocol; "
        "certification by Newport using QSS method adds further confidence."
    ),
    eqe_spectral_response: (
        0.85,
        "EQE is a standard spectral response measurement; wavelength-dependent current "
        "generation is directly measured and consistent with absorption data."
    ),
    stability_test_protocols: (
        0.88,
        "Three stability protocols (humidity, thermal, MPP tracking) are standard "
        "accelerated aging tests for PSCs; conditions are explicitly defined."
    ),
    dft_bandgap_calculation: (
        0.75,
        "DFT is a well-established computational method; however, bandgap prediction "
        "has known systematic errors (underestimation); relative trends are more "
        "reliable than absolute values."
    ),
    xrd_peak_shift: (
        0.88,
        "XRD peak positions are directly measurable with high precision; the observed "
        "lower-angle shift with increasing MDACl2 is a clear systematic trend."
    ),

    # ── Results: optical and bandgap ───────────────────────────────────────────
    uvvis_blue_shift: (
        0.92,
        "Direct UV-vis measurement showing progressive blue-shift; trend is consistent "
        "across all compositions and reproducible."
    ),
    pl_peak_shifts: (
        0.92,
        "Direct PL emission measurements with consistent 2-nm step shifts; internally "
        "consistent with UV-vis data; confirmed by multiple runs."
    ),
    bandgap_values: (
        0.90,
        "Bandgap derived from UV-vis absorption edge (Tauc plot method); values are "
        "self-consistent with PL peak positions and DFT predictions."
    ),
    dft_bandgap_fa_vacancy: (
        0.70,
        "DFT-computed bandgap for FA vacancy model; absolute value subject to DFT "
        "systematic error but relative comparison (1.47 vs 1.45 eV) is qualitatively "
        "consistent with experiment."
    ),
    dft_bandgap_cl_interstitial: (
        0.70,
        "DFT-computed bandgap for Cl interstitial model; predicts 1.69 eV, substantially "
        "higher than experiment (1.49 eV), indicating this mechanism is not dominant."
    ),
    pl_quality_enhancement: (
        0.82,
        "PL quantum yield measured with integrated sphere; the non-monotonic behavior "
        "(increase at 3.8 mol%, decrease at 5.7 mol%) is a directly observed trend."
    ),

    # ── Results: phase stability ──────────────────────────────────────────────
    humidity_phase_stability: (
        0.93,
        "Direct XRD measurement of phase content after 80% RH exposure for 24h; "
        "complete conversion of pure FAPbI3 to delta-phase is unambiguously detected."
    ),
    alpha_phase_retention_38: (
        0.93,
        "XRD shows pure alpha-phase retention at 3.8 mol% after humidity stress; "
        "this is the key stability finding of the paper."
    ),
    alpha_phase_retention_57: (
        0.92,
        "XRD confirms alpha-phase retention at 5.7 mol% as well; broad composition "
        "range confirms robust stabilization window."
    ),
    crystallinity_improvement: (
        0.85,
        "XRD signal intensity increase is a direct measurement; the trend up to "
        "3.8 mol% is clear; absence of impurity peaks confirms clean incorporation."
    ),
    giwaxs_no_impurity: (
        0.88,
        "GIWAXS provides comprehensive crystal structure information; absence of "
        "secondary phase peaks (FACl, MDACl2) is a clear negative result."
    ),
    xrd_peak_lower_angle: (
        0.87,
        "XRD peak shift to lower angle is a precise, directly measured shift; "
        "consistent with lattice expansion from interstitial Cl-."
    ),

    # ── Results: device performance ─────────────────────────────────────────────
    pce_distributions: (
        0.88,
        "Statistics from 20+ devices per composition; average PCE and standard "
        "deviation are directly reported; clear compositional trend observed."
    ),
    target_best_jv: (
        0.92,
        "Best-performing device J-V parameters are directly measured under standard "
        "AM 1.5 conditions; internally consistent with EQE integration."
    ),
    certified_pce: (
        0.95,
        "Independently certified by Newport, USA using the quasi-steady-state (QSS) "
        "method — the most reliable PCE certification available."
    ),
    highest_jsc: (
        0.95,
        "Certified JSC value (26.70 mA/cm2) is an official measurement from Newport "
        "accredited laboratory; highest reported for FA-based PSCs is a verifiable claim."
    ),
    eqe_expanded_range: (
        0.85,
        "EQE spectral response is a direct measurement; expanded wavelength range "
        "is visually clear in the figure and consistent with narrower bandgap."
    ),
    morphology_unchanged: (
        0.85,
        "SEM is a standard imaging technique; no notable differences between target "
        "and control is a reliable negative result."
    ),

    # ── Results: defect and carrier dynamics ───────────────────────────────────
    electron_trap_density: (
        0.82,
        "SCLC-derived trap densities are directly computed from measured V_TFL; "
        "values are self-consistent across compositions (5.4-8.0e15 cm-3 range)."
    ),
    hole_trap_reduction: (
        0.75,
        "Hole-only device SCLC measurements are less commonly reported; the reduction "
        "trend with MDACl2 is a positive result though fewer details are given."
    ),
    carrier_lifetime_target: (
        0.88,
        "TRPL lifetime of 1562 ns (target) vs 715 ns (control) is a directly "
        "measured difference; >2x increase is a clear, reproducible trend."
    ),
    cl_enriched_interface: (
        0.83,
        "XPS and ToF-SIMS both independently confirm Cl enrichment at TiO2 interface; "
        "two-technique corroboration strengthens confidence."
    ),

    # ── Results: stability ─────────────────────────────────────────────────────
    humidity_stability: (
        0.90,
        "Humidity test at 85% RH is a standard accelerated aging test; >90% retention "
        "for target vs 40% for control at 70h is a large, unambiguous difference."
    ),
    thermal_stability: (
        0.90,
        "Thermal aging at 150C in air is an aggressive accelerated test; >90% retention "
        "after 20h for target vs <20% for control is a definitive result."
    ),
    photostability: (
        0.88,
        "600-hour MPP tracking under full AM 1.5G is the most demanding operational "
        "stability test; ~90% PCE retention is a directly measured, impressive result."
    ),

    # ── Results: key conclusions ──────────────────────────────────────────────
    optimal_composition: (
        0.88,
        "Optimal composition conclusion is supported by multiple independent measurements: "
        "phase stability, bandgap preservation, PCE, JSC, and stability all peak or "
        "plateau at 3.8 mol%."
    ),
    mda_superior_to_mapbbr3: (
        0.88,
        "Head-to-head comparison with MAPbBr3-stabilized control on the same device "
        "architecture; all metrics (PCE, JSC, stability) favor MDACl2; comparison "
        "is directly supported by the experimental data."
    ),

    # ── Discussion: mechanisms ─────────────────────────────────────────────────
    stabilization_mechanism_h_bonding: (
        0.78,
        "H-bonding mechanism is a well-established explanation for MA stabilization "
        "(supported by refs 33-35); extension to MDA is a plausible analogical "
        "argument based on MDA's higher H-bonding capacity."
    ),
    stabilization_mechanism_entropic: (
        0.72,
        "Entropic stabilization from cation mixing is a known mechanism (ref 32); "
        "applies generally to solid solutions; MDA substitution is one instance."
    ),
    stabilization_mechanism_tolerance_factor: (
        0.70,
        "Goldschmidt tolerance factor adjustment is a standard crystallographic "
        "explanation for phase stability; quantitative t values are estimates."
    ),
    stabilization_mechanism_cl_interstitial: (
        0.75,
        "Interstitial Cl- is supported by XRD peak shift (lower angle = expanded "
        "lattice) and DFT (Cl_i bandgap prediction); indirect but consistent evidence."
    ),
    v_fa_defects_shallow: (
        0.72,
        "Shallow trap nature of V_FA is a prior literature report (ref 37); the "
        "experimental evidence (no JSC loss, PL enhancement) is consistent with this."
    ),
    phase_stability_summary: (
        0.80,
        "Multi-mechanism explanation is logically coherent and covers all major "
        "stabilization factors; the mechanisms are individually plausible and mutually "
        "consistent."
    ),
    cl_interface_photostability: (
        0.78,
        "Interface Cl suppressing TiO2 photocatalysis is a prior literature report "
        "(refs 41-42); the observation of Cl enrichment at the interface is direct "
        "experimental evidence supporting this mechanism."
    ),
    photostability_mechanism: (
        0.78,
        "Dual mechanism (interface Cl + alpha-phase stabilization) is well-supported "
        "by the data: both factors are present and both are known to improve "
        "photostability per literature."
    ),
    literature_comparison: (
        0.88,
        "Direct comparison with prior art (MAPbBr3 control and previous literature) "
        "is factually stated based on reported values; the efficiency gap is real "
        "and verifiable."
    ),
    aberration_free_stability: (
        0.80,
        "The claim of no efficiency-stability trade-off is directly supported by "
        "the data: the target outperforms the control on both efficiency AND all "
        "three stability metrics simultaneously."
    ),

    # ── Discussion: main conclusions ──────────────────────────────────────────
    conclusion_alpha_stabilization: (
        0.88,
        "Core conclusion of the paper: 3.8 mol% MDACl2 stabilizes alpha-FAPbI3 "
        "while preserving bandgap, achieving record efficiency (23.73% certified) "
        "and record stability (600h MPP). Supported by all experimental results."
    ),
    conclusion_no_tradeoff: (
        0.85,
        "The key scientific contribution: demonstrating that the efficiency-stability "
        "trade-off can be avoided by using MDACl2 instead of MA/Br/Cs. Directly "
        "supported by head-to-head comparison data showing MDACl2 beats MAPbBr3 "
        "on both efficiency and all stability metrics."
    ),
}