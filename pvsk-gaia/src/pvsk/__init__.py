"""
PVSK Synthesis Package - Cross-paper reasoning across Kojima 2009 and Kim 2012.1

This package synthesizes findings from:
- pvsk2009: Kojima et al. (2009) - first perovskite sensitization (3.81% PCE)
- pvsk2012.1: Kim et al. (2012) - solid-state optimization (9.7% PCE)
"""

from .s1_agreement import (
    agreement_perovskite_sensitization_valid,
    agreement_charge_separation_mechanism,
    agreement_bromide_enables_high_voc,
    agreement_iodide_extends_spectral_range,
    agreement_absorption_strength,
    agreement_tio2_conduction_band_injection,
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

__all__ = [
    # Agreement claims
    "agreement_perovskite_sensitization_valid",
    "agreement_charge_separation_mechanism",
    "agreement_bromide_enables_high_voc",
    "agreement_iodide_extends_spectral_range",
    "agreement_absorption_strength",
    "agreement_tio2_conduction_band_injection",
    # Contradiction resolutions
    "contradiction_durability_stability",
    "resolution_durability_stability",
    # Induction laws
    "law_perovskite_sensitization_effective",
    "law_solid_state_stability",
    "law_panchromatic_absorption",
    # Synthesis conclusions
    "synthesis_perovskite_sensitization_valid",
    "synthesis_efficiency_progress_3p81_to_9p7",
    "synthesis_solid_state_eliminates_electrolyte_degradation",
    "synthesis_band_alignment_critical_for_charge_separation",
    "synthesis_iodide_bromide_tradeoff",
    "synthesis_voc_determined_by_conduction_band_offset",
    "synthesis_high_ipce_confirmed_independent",
    "synthesis_promising_future_directions",
]