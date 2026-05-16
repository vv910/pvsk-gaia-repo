"""
Priors for pvsks41586-024-07997-7-gaia.

This module assigns priors to independent (leaf) claims.
Prior ranges:
- 0.85-0.95: well-established fact or strong experimental observation
- 0.65-0.85: supported by evidence but imperfect
- 0.40-0.65: tentative, single-source, method-dependent, or uncertain
- 0.20-0.40: speculative or weak assumption
"""

from .motivation import (
    lif_limited_effectiveness,
    edai_chemical_passivation,
    nanoscale_contact_requirement,
    double_textured_silicon,
    passivation_tradeoff,
)

from .s3_results import (
    lif_discontinuity_confirmation,
    metallic_pb_suppression,
    xps_pb4f_shift,
    pa_vs_eda_orientation,
    tof_sims_edai_distribution,
    eqe_spectral_response,
    minority_carrier_lifetime,
    voc_statistical_improvement,
    nrel_certified_pce,
    champion_device_jv,
    storage_stability,
    operational_stability,
    theoretical_prediction_bilayer,
    theoretical_prediction_edai_only,
    theoretical_prediction_lif_only,
    edai_ff_tradeoff,
    bilayer_no_tradeoff,
)

# =============================================================================
# Well-established facts and strong experimental observations (0.85-0.95)
# =============================================================================

PRIORS = {
    nrel_certified_pce: (
        0.90,
        "NREL certification provides third-party verification of the 33.89% stabilized PCE."
    ),
    champion_device_jv: (
        0.90,
        "Directly measured J-V data from champion device with clear scan conditions."
    ),
    double_textured_silicon: (
        0.85,
        "Device fabrication description confirming the asymmetric texture design."
    ),
    storage_stability: (
        0.85,
        "Directly observed experimental data with clear protocol (53 days air storage)."
    ),
    operational_stability: (
        0.85,
        "Directly observed experimental data with clear protocol (1200 hours MPP tracking)."
    ),
}

# =============================================================================
# Supported by evidence but imperfect (0.65-0.85)
# =============================================================================

PRIORS.update({
    lif_limited_effectiveness: (
        0.75,
        "Reported observation from multiple samples showing voltage deficit with thin LiF alone."
    ),
    edai_chemical_passivation: (
        0.75,
        "Mechanism supported by XPS and UPS data showing chemical interaction with Pb ions."
    ),
    nanoscale_contact_requirement: (
        0.70,
        "Established principle from literature on perovskite vs silicon diffusion lengths."
    ),
    passivation_tradeoff: (
        0.75,
        "Observed in device data showing EDAI alone causes FF reduction while improving Voc."
    ),
    lif_discontinuity_confirmation: (
        0.80,
        "TEM directly confirms discontinuous LiF layer morphology."
    ),
    metallic_pb_suppression: (
        0.80,
        "XPS data directly shows metallic Pb peak reduction after EDAI treatment."
    ),
    xps_pb4f_shift: (
        0.75,
        "XPS measurement shows chemical interaction shift."
    ),
    pa_vs_eda_orientation: (
        0.80,
        "DFT calculation with established methodology."
    ),
    tof_sims_edai_distribution: (
        0.75,
        "TOF-SIMS data shows EDAI localized at surface without bulk penetration."
    ),
    eqe_spectral_response: (
        0.75,
        "EQE measurements comparing texture configurations."
    ),
    minority_carrier_lifetime: (
        0.75,
        "Lifetime measurements on three texture configurations."
    ),
    voc_statistical_improvement: (
        0.80,
        "Statistical data from device batches showing consistent Voc improvement."
    ),
    theoretical_prediction_bilayer: (
        0.65,
        "Theoretical prediction based on understanding of bilayer mechanism."
    ),
    theoretical_prediction_edai_only: (
        0.65,
        "Theoretical prediction explaining observed trade-off behavior."
    ),
    theoretical_prediction_lif_only: (
        0.65,
        "Theoretical prediction explaining LiF-only limitations."
    ),
    edai_ff_tradeoff: (
        0.75,
        "Directly observed in device data showing EDAI alone reduces FF."
    ),
    bilayer_no_tradeoff: (
        0.70,
        "Device data shows bilayer achieves both Voc improvement and FF enhancement."
    ),
})