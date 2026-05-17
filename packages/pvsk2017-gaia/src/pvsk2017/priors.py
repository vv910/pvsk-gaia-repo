"""
Priors for PVSK 2017 paper formalization.

Independent claims need priors in this file. Derived conclusions get BP-computed beliefs.
Settings do not need priors.
"""

from .motivation import (
    perovskite_pce_record,
    perovskite_degradation_mechanisms,
    stability_limiting_factors,
    two_d_perovskite_stability,
)

from .s2_methods import (
    avai_synthesis,
    two_d_three_d_composite_preparation,
    interface_model,
    pl_excitation_selectivity,
)

from .s4_discussion import (
    module_gff,
)

from .strategies import (
    dft_2d3d_pred,
    dft_standard_pred,
)

PRIOR = {
    perovskite_pce_record: (0.92, "NREL-certified record."),
    perovskite_degradation_mechanisms: (0.90, "Well-documented mechanism."),
    stability_limiting_factors: (0.88, "Widely reported."),
    two_d_perovskite_stability: (0.85, "Multiple studies support."),
    avai_synthesis: (0.90, "Clear characterization."),
    two_d_three_d_composite_preparation: (0.88, "Precise method."),
    interface_model: (0.85, "Experimental data."),
    pl_excitation_selectivity: (0.80, "Physics established."),
    module_gff: (0.92, "Direct calculation."),
    dft_2d3d_pred: (0.75, "DFT method."),
    dft_standard_pred: (0.75, "DFT method."),
}

# Alias for compatibility
PRIORS = PRIOR