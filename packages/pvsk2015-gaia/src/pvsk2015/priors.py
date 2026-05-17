"""
Priors for Jeon2015 (Nature 2015) knowledge package.

This file assigns prior probabilities to independent claims based on
their evidential strength and source reliability.

Prior ranges:
- 0.85 to 0.95: well-established fact or strong experimental observation
- 0.65 to 0.85: supported by evidence but imperfect
- 0.40 to 0.65: tentative, single-source, method-dependent, or uncertain
- 0.20 to 0.40: speculative or weak assumption
"""

from .s3_results import (
    best_device_jv,
    black_powder_only,
    eqe_plateau,
    fapbi3_hysteresis,
    dsc_phase_transition,
    phase_reversibility,
    perovskite_polymorphs,
    synergetic_effect,
    sem_morphology_x0,
    sem_morphology_x15,
    table1_photovoltaic_parameters,
    xrd_perovskite_x15,
)

from .motivation import (
    mapbi3_transport,
    fapbi3_transport,
    conductivity_type,
)

# =============================================================================
# PRIORS DICTIONARY
# =============================================================================

PRIORS = {
    best_device_jv: (
        0.9,
        "Direct experimental measurement from best-performing device with "
        "verified J-V curves and EQE integration, reported in a peer-reviewed "
        "Nature paper with standardized certification.",
    ),
    table1_photovoltaic_parameters: (
        0.9,
        "Systematic photovoltaic parameter measurements across composition range "
        "with averaged forward/reverse sweeps, minimizing hysteresis effects. "
        "Tabulated data from a controlled experimental study.",
    ),
    eqe_plateau: (
        0.9,
        "Direct external quantum efficiency measurement showing >80% plateau "
        "between 400-750nm, with Jsc integrated from EQE matching J-V measurement. "
        "Strong experimental verification.",
    ),
    black_powder_only: (
        0.85,
        "Visual observation of powder color (black = perovskite) at room "
        "temperature for x=0.15 composition. Clear qualitative result with "
        "photographs as documentation.",
    ),
    dsc_phase_transition: (
        0.85,
        "Direct DSC measurement showing endothermic peak at 160C for pure FAPbI3 "
        "and no peak for x=0.15 composition. Thermal analysis with clear "
        "experimental protocol.",
    ),
    synergetic_effect: (
        0.85,
        "Key experimental finding that co-substitution achieves what single "
        "substitution cannot. XRD confirms pure perovskite phase only for the "
        "dual-substituted composition.",
    ),
    xrd_perovskite_x15: (
        0.85,
        "X-ray diffraction measurement showing strong (111) perovskite peak "
        "at 13.9 degrees for x=0.15 at only 100C annealing, while x=0 shows "
        "non-perovskite phase. Direct structural evidence.",
    ),
    mapbi3_transport: (
        0.8,
        "Electron and hole diffusion length measurements reported in the "
        "literature (referenced as ref 20). Well-established characterization "
        "technique for perovskite materials.",
    ),
    fapbi3_transport: (
        0.8,
        "Electron and hole diffusion length measurements for FAPbI3 from "
        "referenced literature (ref 16). Consistent with established characterization.",
    ),
    conductivity_type: (
        0.8,
        "Seebeck coefficient measurements showing n-type (MAPbI3) and p-type "
        "(FAPbI3) character. Established thermoelectric characterization method.",
    ),
    sem_morphology_x15: (
        0.85,
        "Direct SEM observation of smooth, uniform, dense morphology at x=0.15. "
        "Clear visual evidence from well-controlled sample preparation.",
    ),
    sem_morphology_x0: (
        0.85,
        "Direct SEM observation of rough, irregular, bumpy surface for x=0 "
        "at 150C annealing. Clear experimental observation of phase transition effects.",
    ),
    perovskite_polymorphs: (
        0.85,
        "Established crystallographic knowledge about FAPbI3 polymorphism. "
        "Black perovskite (P3m1) vs yellow non-perovskite (P6_3mc) well-documented "
        "in cited literature (refs 17-18).",
    ),
    phase_reversibility: (
        0.8,
        "Direct experimental observation of reversible phase transition: yellow "
        "non-perovskite at room temperature converts to black perovskite at 170C, "
        "and reverts after 10 days in air. Clear documented behavior.",
    ),
    fapbi3_hysteresis: (
        0.85,
        "Direct J-V hysteresis measurement comparing FAPbI3/MAPbBr3 to MAPbI3. "
        "Measured with 40ms scanning delay showing negligible hysteresis for "
        "mixed system vs large hysteresis for MAPbI3.",
    ),
}