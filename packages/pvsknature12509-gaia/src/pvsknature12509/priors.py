"""
Priors for Liu et al. 2013 Nature paper.

Paper: Efficient planar heterojunction perovskite solar cells by vapour deposition
Citation: [@Liu2013]

Independent premises from experimental measurements and observations need priors.
Derived conclusions get their beliefs from BP propagation, not from priors.
"""

from .motivation import (
    meso_superstructured_improvement,
    solution_planarHeterojunction,
    high_efficiency_planar_demonstrated,
    vapour_deposition_enables_uniform_films,
    device_architecture_description,
    study_rationale,
    perovskite_material_introduction,
    photovoltaic_generations,
)

from .s3_results import (
    xrd_peak_positions,
    vapour_deposited_morphology,
    solution_processed_morphology,
    vapour_deposited_cross_section,
    solution_processed_cross_section,
    vapour_best_Jsc,
    vapour_best_Voc,
    vapour_best_FF,
    solution_best_Jsc,
    solution_best_Voc,
    solution_best_FF,
    vapour_batch_Jsc_avg,
    vapour_batch_Voc_avg,
    vapour_batch_FF_avg,
)

from .s4_discussion import (
    vapour_deposition_maturity,
    oled_vapour_deposition_compatibility,
)

# PRIORS dictionary - required export for Gaia
PRIORS = {
    meso_superstructured_improvement: (
        0.85,
        "Directly reported experimental result from prior work (Lee et al. 2012) with established methodology."
    ),
    solution_planarHeterojunction: (
        0.80,
        "Prior experimental result with moderate sample size, established baseline for this work."
    ),
    high_efficiency_planar_demonstrated: (
        0.90,
        "Key new finding with direct J-V measurement under standard test conditions (AM1.5, 101 mW/cm²)."
    ),
    vapour_deposition_enables_uniform_films: (
        0.85,
        "Direct observation from SEM imaging, clear visual evidence of uniform morphology."
    ),
    xrd_peak_positions: (
        0.90,
        "Direct instrumental measurement (X-ray diffraction), precise 2θ values reported."
    ),
    vapour_deposited_morphology: (
        0.85,
        "Direct SEM observation with clear qualitative difference from solution processing."
    ),
    solution_processed_morphology: (
        0.85,
        "Direct SEM observation showing incomplete coverage and platelet formation."
    ),
    vapour_deposited_cross_section: (
        0.85,
        "Direct SEM cross-sectional measurement, uniform 330 nm thickness clearly observable."
    ),
    solution_processed_cross_section: (
        0.80,
        "Direct SEM observation with reported thickness range (50-410 nm) and pinhole regions."
    ),
    vapour_best_Jsc: (
        0.90,
        "Direct J-V measurement, key figure of merit for solar cell performance."
    ),
    vapour_best_Voc: (
        0.90,
        "Direct J-V measurement, key figure of merit for solar cell performance."
    ),
    vapour_best_FF: (
        0.90,
        "Direct J-V measurement, key figure of merit for solar cell performance."
    ),
    solution_best_Jsc: (
        0.90,
        "Direct J-V measurement for baseline comparison device."
    ),
    solution_best_Voc: (
        0.90,
        "Direct J-V measurement for baseline comparison device."
    ),
    solution_best_FF: (
        0.90,
        "Direct J-V measurement for baseline comparison device."
    ),
    vapour_batch_Jsc_avg: (
        0.85,
        "Statistical average from 12-device batch with reported standard deviation."
    ),
    vapour_batch_Voc_avg: (
        0.85,
        "Statistical average from 12-device batch with reported standard deviation."
    ),
    vapour_batch_FF_avg: (
        0.85,
        "Statistical average from 12-device batch with reported standard deviation."
    ),
    vapour_deposition_maturity: (
        0.80,
        "Established industrial fact about vapour deposition technology maturity."
    ),
    oled_vapour_deposition_compatibility: (
        0.80,
        "Well-known commercial success of OLED vapour deposition validates this claim."
    ),
    device_architecture_description: (
        0.85,
        "Device architecture description from the paper's figure and text, well-established configuration."
    ),
    study_rationale: (
        0.80,
        "Author's stated purpose for the study, reasonable framing of research objectives."
    ),
    perovskite_material_introduction: (
        0.80,
        "Background context about perovskite material properties from literature."
    ),
    photovoltaic_generations: (
        0.80,
        "General background knowledge on PV technology generations from literature."
    ),
}

# Alias for backwards compatibility
PRIOR_MAP = PRIORS
PRIOR = PRIORS