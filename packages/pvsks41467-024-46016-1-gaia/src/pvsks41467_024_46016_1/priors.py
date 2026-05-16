"""Priors for independent claims in the R2R perovskite solar cell package."""

from .motivation import (
    commercial_tce_cost,
    cost_prediction,
    lab_scale_limitation,
    vacuum_electrode_cost,
)

from .s2_pfsd import (
    pfsd_technique_description,
)

from .s3_automated import (
    high_throughput_capability,
)

from .s3_automated import (
    htab_passivation,
    p3ht_heating_requirement,
)

# Prior ranges:
# - 0.85 to 0.95: well-established fact or strong experimental observation
# - 0.65 to 0.85: supported by evidence but imperfect
# - 0.40 to 0.65: tentative, single-source, method-dependent, or uncertain
# - 0.20 to 0.40: speculative or weak assumption

PRIORS = {
    lab_scale_limitation: (
        0.85,
        "Lab-scale PeSC limitations are well-documented in literature, with solution-based methods not economically viable for scale-up.",
    ),
    vacuum_electrode_cost: (
        0.90,
        "Vacuum-processed Au electrodes are widely recognized as the highest-cost PeSC component; this is a well-established fact in the field.",
    ),
    commercial_tce_cost: (
        0.85,
        "TCE cost structure is well-documented; commercial TCEs with ~8 Ω sq⁻¹ sheet resistance represent a significant cost component.",
    ),
    pfsd_technique_description: (
        0.80,
        "PFSD technique using sub-stoichiometric organic cations (<50 mol% of PbI₂) is a reported method with demonstrated success.",
    ),
    cost_prediction: (
        0.70,
        "Manufacturing cost projection of ~0.7 USD/W_p is based on demonstrated devices and established cost models, but represents a prediction for future production scale.",
    ),
    high_throughput_capability: (
        0.85,
        "High-throughput R2R platform capability is demonstrated in the paper with production and testing of thousands of cells per day.",
    ),
    htab_passivation: (
        0.80,
        "HTAB passivation mechanism is well-established in the literature; surface trap passivation and molecular anchoring for P3HT are commonly reported effects.",
    ),
    p3ht_heating_requirement: (
        0.75,
        "The substrate heating requirement (45°C) for uniform P3HT coating is a specific technical parameter demonstrated in the paper.",
    ),
}