"""
Priors for PVSK synthesis package.

Independent claims from cross-paper synthesis.
Only claims (not strategies) belong in PRIORS.
"""

from .s1_agreement import (
    agreement_perovskite_sensitization_valid,
    agreement_charge_separation_mechanism,
    agreement_bromide_enables_high_voc,
    agreement_iodide_extends_spectral_range,
)

from .s3_contradictions import (
    contradiction_durability_stability,
    resolution_durability_stability,
)

from .s4_induction import (
    law_perovskite_sensitization_effective,
    law_solid_state_stability,
    law_panchromatic_absorption,
)

from .s5_synthesis import (
    synthesis_perovskite_sensitization_valid,
    synthesis_efficiency_progress_3p81_to_9p7,
    synthesis_solid_state_eliminates_electrolyte_degradation,
    synthesis_band_alignment_critical_for_charge_separation,
    synthesis_iodide_bromide_tradeoff,
    synthesis_voc_determined_by_conduction_band_offset,
    synthesis_high_ipce_confirmed_independent,
    synthesis_promising_future_directions,
)


PRIORS = {
    # Agreement claims - high prior for cross-validated claims
    agreement_perovskite_sensitization_valid: (
        0.92,
        "Cross-validated by two independent papers (2009, 2012) demonstrating effective sensitization."
    ),
    agreement_charge_separation_mechanism: (
        0.92,
        "Cross-validated mechanism description from two independent studies."
    ),
    agreement_bromide_enables_high_voc: (
        0.85,
        "Supported by 2009 bromide data and 2012 band alignment confirmation."
    ),
    agreement_iodide_extends_spectral_range: (
        0.88,
        "Independent observations of extended spectral response in both papers."
    ),

    # Contradiction/resolution - moderate prior for resolved tensions
    contradiction_durability_stability: (
        0.50,
        "Apparent contradiction between durability observations - resolved by complement."
    ),
    resolution_durability_stability: (
        0.82,
        "Resolution via complement is well-grounded in different device configurations."
    ),

    # Induction laws - high prior for multi-study convergence
    law_perovskite_sensitization_effective: (
        0.90,
        "Two independent PCE demonstrations (3.81% and 9.7%) strongly support the conclusion."
    ),
    law_solid_state_stability: (
        0.85,
        "Clear comparison between liquid and solid-state configurations supports this."
    ),
    law_panchromatic_absorption: (
        0.88,
        "Three independent observations (two IPCE spectra + JSC) confirm panchromatic absorption."
    ),

    # Synthesis claims - high prior for well-supported conclusions
    synthesis_perovskite_sensitization_valid: (
        0.90,
        "Well-supported by cross-paper agreement, support chains, and induction."
    ),
    synthesis_efficiency_progress_3p81_to_9p7: (
        0.88,
        "Directly measured efficiency values from both papers."
    ),
    synthesis_solid_state_eliminates_electrolyte_degradation: (
        0.85,
        "Clear mechanism explanation for stability improvement."
    ),
    synthesis_band_alignment_critical_for_charge_separation: (
        0.88,
        "Quantitative band measurements from UPS and optical spectroscopy."
    ),
    synthesis_iodide_bromide_tradeoff: (
        0.85,
        "Direct comparison of device performance from both papers."
    ),
    synthesis_voc_determined_by_conduction_band_offset: (
        0.82,
        "Band calculations and Voc measurements consistent across papers."
    ),
    synthesis_high_ipce_confirmed_independent: (
        0.87,
        "Multiple IPCE measurements from both papers confirm high efficiency."
    ),
    synthesis_promising_future_directions: (
        0.80,
        "Supported by demonstrated efficiency gains and stability improvements."
    ),
}