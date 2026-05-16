"""
Priors for independent claims in the pvsk2013-gaia package.
"""

from .motivation import sequential_deposition_introduced
from .s2_methods import best_device_modification
from .s3_results import (
    pbi2_complete_infiltration,
    pbi2_crystal_size,
    flat_substrate_incomplete_conversion,
    perovskite_xrd_confirmed,
    device_batch_statistics,
    ipce_peak_value,
    best_device_improvement_attributed,
    stability_result,
    no_photodegradation,
    apce_exceeds_90_percent,
)
from .s4_discussion import (
    layered_pbi2_structure,
    thermodynamic_driving_force,
    reaction_kinetics_enhancement,
)

PRIORS = {
    pbi2_complete_infiltration: (
        0.9,
        "Direct SEM observation showing complete PbI2 infiltration into TiO2 nanopores."
    ),
    pbi2_crystal_size: (
        0.88,
        "Crystal size (~22 nm) measured from pore size constraint."
    ),
    perovskite_xrd_confirmed: (
        0.9,
        "Direct XRD measurement showing tetragonal perovskite peaks after conversion."
    ),
    flat_substrate_incomplete_conversion: (
        0.85,
        "Direct XRD observation of unreacted PbI2 after 45 min on flat glass."
    ),
    device_batch_statistics: (
        0.9,
        "Direct experimental measurement from 10 devices: average PCE 12.0% +/- 0.5%."
    ),
    ipce_peak_value: (
        0.9,
        "Direct IPCE measurement showing peak values exceeding 90%."
    ),
    best_device_improvement_attributed: (
        0.78,
        "Attribution supported by pre-wetting modification and spectral response changes."
    ),
    stability_result: (
        0.88,
        "Direct 500-hour stability test: device retains >80% of initial PCE."
    ),
    no_photodegradation: (
        0.85,
        "Direct observation of unchanged Jsc during stability test."
    ),
    sequential_deposition_introduced: (
        0.92,
        "Core method clearly described in paper."
    ),
    best_device_modification: (
        0.88,
        "Direct description of modified conditions: shorter spin-cast and pre-wetting."
    ),
    layered_pbi2_structure: (
        0.9,
        "Well-established in literature on polytypism and intercalation."
    ),
    thermodynamic_driving_force: (
        0.82,
        "Established principle from semiconductor nanocrystal ion exchange literature."
    ),
    reaction_kinetics_enhancement: (
        0.85,
        "Reasonable mechanistic interpretation combining formation energy and nanoscale morphology."
    ),
    apce_exceeds_90_percent: (
        0.9,
        "Direct measurement showing APCE >90% across visible range without correction for reflective losses."
    ),
}