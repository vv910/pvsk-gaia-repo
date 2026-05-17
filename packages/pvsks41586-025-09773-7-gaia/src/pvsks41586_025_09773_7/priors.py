"""
priors.py for pvsks41586-025-09773-7-gaia

Prior probability assignments for independent (leaf) knowledge claims.
Derived conclusions do NOT get priors - their belief is determined by BP propagation.
"""

from .motivation import (
    buried_interface_recombination,
    conventional_passivation_limitation,
    diffusion_length_enhancement,
    pb_sn_psc_performance,
)
from .s2_methods import (
    dipolar_passivation_design,
    energy_level_alignment,
    kpfm_potential_change,
)
from .s3_results import (
    limiting_carrier_mobility,
)
from .s4_discussion import (
    contact_loss_mitigation,
    tandem_buried_interface_challenge,
    tandem_device_configuration,
)

# Prior ranges:
# 0.85-0.95: well-established fact or strong experimental observation
# 0.65-0.85: supported by evidence but imperfect
# 0.40-0.65: tentative, single-source, method-dependent, or uncertain
# 0.20-0.40: speculative or weak assumption

PRIORS = {
    # Motivation - core problem statements
    buried_interface_recombination: (
        0.85,
        "Well-established problem statement in perovskite tandem literature: buried interface recombination "
        "is a known limiting factor for all-perovskite tandem solar cells [@Lin2025]."
    ),
    conventional_passivation_limitation: (
        0.85,
        "Widely reported limitation of long-chain amine passivation in mixed Pb-Sn PSCs - this trade-off "
        "between passivation and carrier transport is documented in multiple prior works cited by [@Lin2025]."
    ),
    diffusion_length_enhancement: (
        0.85,
        "Directly measured diffusion length (6.2 um vs 4.8 um control) using terahertz spectroscopy - "
        "clear experimental measurement with established methodology [@Lin2025]."
    ),
    pb_sn_psc_performance: (
        0.9,
        "Best-performing device metrics directly measured with certified J-V characterization - this is "
        "a key reported result of the paper with statistical validation [@Lin2025]."
    ),

    # Methods - experimental observations
    dipolar_passivation_design: (
        0.9,
        "Core experimental design described in the paper - the dipolar passivation strategy with SA is "
        "the central contribution being formally reported [@Lin2025]."
    ),
    energy_level_alignment: (
        0.85,
        "Direct UPS (ultraviolet photoemission spectroscopy) measurements of work function and valence band "
        "maximum - standard characterization technique with clear protocols [@Lin2025]."
    ),
    kpfm_potential_change: (
        0.85,
        "Direct KPFM (Kelvin probe force microscopy) measurements showing surface potential changes - "
        "standard interfacial characterization method with ~10 mV resolution [@Lin2025]."
    ),
    limiting_carrier_mobility: (
        0.8,
        "Derived from terahertz spectroscopy diffusion coefficient measurements - reliable but involves "
        "assumption about carrier type limiting mobility [@Lin2025]."
    ),

    # Discussion - tandem cell observations
    contact_loss_mitigation: (
        0.8,
        "Claim about mechanism - that dipolar passivation mitigates contact losses from the interconnection "
        "layer in tandem configuration, supported by the observed performance improvements [@Lin2025]."
    ),
    tandem_buried_interface_challenge: (
        0.85,
        "Well-documented challenge in all-perovskite tandem cells: the buried NBG interface and the "
        "low-temperature PEDOT:PSS processing issue are known limitations in the field [@Lin2025]."
    ),
    tandem_device_configuration: (
        0.9,
        "Device configuration is a factual description of the fabricated tandem structure - directly reported "
        "from the Methods section with detailed layer specifications [@Lin2025]."
    ),
}