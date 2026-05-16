"""
Priors for independent claims in the pvskscience.adk1633 package.

These priors are assigned to leaf claims (independent premises) that are not
derived from any other claim through reasoning strategies.
"""

from .motivation import (
    diammonium_field_effect,
    methylthio_chemical_passivation,
)
from .s2_methods import (
    dianmmonium_pce_improvement,
    dianmmonium_field_effect_mechanism,
)
from .s3_results import (
    pred_dmdp,
    pred_single,
    qss_pce_certification,
    photovoltaic_params,
    thermal_stability,
    operating_stability,
)
from .s4_discussion import (
    plqy_loss_reduction,
)

PRIORS = {
    dianmmonium_pce_improvement: (
        0.85,
        "Directly measured experimental improvement from control to treated devices."
    ),
    dianmmonium_field_effect_mechanism: (
        0.70,
        "Field-effect mechanism supported by UPS measurements and literature."
    ),
    diammonium_field_effect: (
        0.75,
        "Mechanism supported by DFT calculations and literature on diammonium passivation."
    ),
    methylthio_chemical_passivation: (
        0.75,
        "Mechanism supported by DFT, NMR, SIMS, and XPS characterization data."
    ),
    pred_dmdp: (
        0.65,
        "Theoretical prediction based on bimolecular passivation model."
    ),
    pred_single: (
        0.50,
        "Alternative prediction based on single-molecule passivation literature."
    ),
    qss_pce_certification: (
        0.90,
        "NREL-certified quasi-steady-state measurement under standard protocol."
    ),
    photovoltaic_params: (
        0.85,
        "Directly reported experimental measurement with clear protocol."
    ),
    thermal_stability: (
        0.85,
        "Directly measured experimental stability under ISOS-D-2 protocol."
    ),
    operating_stability: (
        0.85,
        "Directly measured experimental stability under ISOS-L-3 protocol."
    ),
    plqy_loss_reduction: (
        0.80,
        "Experimental measurement of PLQY loss reduction after C60 deposition."
    ),
}