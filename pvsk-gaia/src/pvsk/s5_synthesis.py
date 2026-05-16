"""
S5: Final synthesis conclusions.

These are the top-level conclusions exported from the PVSK synthesis package,
representing cross-paper findings that advance the field.
"""

from gaia.lang import claim, support

from pvsk2009 import (
    iodide_cell_efficiency as pvsk2009_efficiency,
    bromide_cell_high_voltage as pvsk2009_bromide_voc,
    perovskite_sensitization_demonstrated as pvsk2009_sensitization,
)

from pvsk2012_1 import (
    pce_9_7_percent as pvsk2012_pce,
    voc_0_888_v as pvsk2012_voc,
    stability_improvement as pvsk2012_stability,
    charge_separation_well_aligned as pvsk2012_band_alignment,
    absorption_coefficient as pvsk2012_absorption,
    bandgap_1_5_ev as pvsk2012_bandgap,
)

from .s1_agreement import (
    agreement_perovskite_sensitization_valid,
    agreement_charge_separation_mechanism,
)
from .s3_contradictions import resolution_durability_stability
from .s4_induction import (
    law_perovskite_sensitization_effective,
    law_solid_state_stability,
)


# Synthesis 1: Perovskite sensitization is validated
synthesis_perovskite_sensitization_valid = claim(
    "Organometal halide perovskites (CH3NH3PbX3, X=I, Br) function as effective "
    "visible-light sensitizers for TiO2-based photovoltaic cells, demonstrated "
    "independently in Kojima 2009 (3.81% PCE) and Kim 2012 (9.7% PCE) [@pvsk2009; @pvsk2012.1].",
    title="Perovskite sensitization validated across independent studies",
)

# Synthesis 2: Efficiency progression
synthesis_efficiency_progress_3p81_to_9p7 = claim(
    "Perovskite-sensitized photovoltaic cells achieved power conversion efficiency "
    "of 3.81% in 2009 (liquid electrolyte) and 9.7% in 2012 (solid-state), "
    "representing a 2.5x improvement through configuration optimization [@pvsk2009; @pvsk2012.1].",
    title="PCE improved from 3.81% to 9.7% across studies",
)

# Synthesis 3: Solid-state eliminates electrolyte degradation
synthesis_solid_state_eliminates_electrolyte_degradation = claim(
    "The replacement of liquid electrolyte with solid-state hole-transporting material "
    "(spiro-MeOTAD) eliminates perovskite dissolution and dramatically improves device "
    "stability from rapid photocurrent decay to 500+ hours of stable operation [@pvsk2009; @pvsk2012.1].",
    title="Solid-state configuration eliminates liquid electrolyte degradation",
)

# Synthesis 4: Band alignment critical for charge separation
synthesis_band_alignment_critical_for_charge_separation = claim(
    "Favorable band alignment between perovskite, TiO2, and hole-transporting material "
    "is critical for efficient charge separation: perovskite ECB (-3.93 eV) above TiO2 "
    "ECB enables electron injection; perovskite EVB (-5.43 eV) allows hole transfer "
    "to spiro-MeOTAD [@pvsk2012.1].",
    title="Band alignment enables efficient charge separation",
)

# Synthesis 5: Iodide vs bromide tradeoff
synthesis_iodide_bromide_tradeoff = claim(
    "CH3NH3PbI3 offers narrower bandgap (1.5 eV) extending spectral response to ~800 nm "
    "and higher photocurrent, while CH3NH3PbBr3 offers higher conduction band position "
    "enabling higher open-circuit voltage (0.96 V vs 0.61 V for iodide) [@pvsk2009].",
    title="Iodide-bromide tradeoff: current vs voltage",
)

# Synthesis 6: Voc determined by conduction band offset
synthesis_voc_determined_by_conduction_band_offset = claim(
    "The open-circuit voltage in perovskite-sensitized cells is determined by the "
    "conduction band offset between the perovskite and TiO2, with higher perovskite "
    "conduction band (as in CH3NH3PbBr3 at ~3.36 eV vs TiO2 at ~4.0 eV) enabling "
    "higher Voc up to 0.96 V [@pvsk2009].",
    title="Voc determined by perovskite-TiO2 conduction band offset",
)

# Synthesis 7: High IPCE confirmed independently
synthesis_high_ipce_confirmed_independent = claim(
    "High incident photon-to-electron conversion efficiency (IPCE) in perovskite "
    "sensitized cells is confirmed independently: 65% max for bromide and 45% for "
    "iodide in 2009, and >50% from 450-750 nm in 2012, demonstrating efficient "
    "light harvesting [@pvsk2009; @pvsk2012.1].",
    title="High IPCE confirmed across independent studies",
)

# Synthesis 8: Promising future directions
synthesis_promising_future_directions = claim(
    "Organometal halide perovskites represent a promising class of materials for "
    "photovoltaic applications, with demonstrated efficiency milestones (3.81% in 2009, "
    "9.7% in 2012), excellent stability potential with solid-state configuration, and "
    "tunable bandgaps through halide composition (Br, I) for optimal light harvesting "
    "[@pvsk2009; @pvsk2012.1].",
    title="Perovskites are promising for photovoltaic applications",
)


# Strategy for the main synthesis conclusion
strat_synthesis_main = support(
    [
        agreement_perovskite_sensitization_valid,
        agreement_charge_separation_mechanism,
        resolution_durability_stability,
        law_perovskite_sensitization_effective,
        law_solid_state_stability,
    ],
    synthesis_perovskite_sensitization_valid,
    reason=(
        "Multiple independent lines of evidence confirm perovskite sensitization: "
        "(1) equivalence between papers on sensitization effectiveness, "
        "(2) equivalence on charge separation mechanism, "
        "(3) resolution of durability/stability contradiction via device configuration, "
        "(4) induction over independent PCE demonstrations."
    ),
    prior=0.90,
)