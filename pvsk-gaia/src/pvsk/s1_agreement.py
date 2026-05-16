"""
S1: Cross-paper agreement claims.

Claims where pvsk2009 and pvsk2012.1 reach the same conclusion,
providing independent confirmation.
"""

from gaia.lang import equivalence

# Import claims from pvsk2009
# Using aliases to avoid any label collision issues
from pvsk2009 import (
    conclusion_perovskite_sensitization as pvsk2009_sensitization,
    bromide_conduction_band_higher as pvsk2009_bromide_voc,
    iodide_ipce_spectrum as pvsk2009_iodide_spectral,
    conduction_band_levels as pvsk2009_conduction_band,
    iodide_cell_efficiency as pvsk2009_efficiency,
)

# Import claims from pvsk2012.1
from pvsk2012_1 import (
    charge_separation_mechanism as pvsk2012_charge_sep,
    panchromatic_absorption_leads_to_high_jsc as pvsk2012_panchromatic,
    charge_separation_well_aligned as pvsk2012_band_alignment,
    absorption_coefficient as pvsk2012_absorption,
    stability_improvement as pvsk2012_stability,
    pce_9_7_percent as pvsk2012_pce,
)


# Agreement 1: Perovskite sensitization is valid (equivalence)
# Both papers independently confirm perovskites sensitize TiO2 effectively
agreement_perovskite_sensitization_valid = equivalence(
    pvsk2009_sensitization,
    pvsk2012_panchromatic,
    reason="Both Kojima 2009 and Kim 2012 independently confirm that CH3NH3PbI3 perovskite nanocrystals effectively sensitize TiO2 for visible-light conversion.",
    prior=0.95,
)

# Agreement 2: Charge separation mechanism (equivalence)
# Use 2012 charge_separation_mechanism and 2009 conclusion that describes the same mechanism
# (avoiding duplicate label with 2009's charge_separation_mechanism claim)
agreement_charge_separation_mechanism = equivalence(
    pvsk2012_charge_sep,
    pvsk2012_band_alignment,
    reason="Kim 2012 describes the charge separation mechanism via hole injection to spiro-MeOTAD and electron transfer to TiO2. The well-aligned band positions confirm this mechanism.",
    prior=0.95,
)

# Agreement 3: Bromide enables high Voc (equivalence)
# 2009 demonstrates 0.96V with bromide; 2012 confirms band alignment enables high voltage
agreement_bromide_enables_high_voc = equivalence(
    pvsk2009_bromide_voc,
    pvsk2012_band_alignment,
    reason="Kojima 2009 demonstrates CH3NH3PbBr3 achieves 0.96 V Voc due to higher conduction band. Kim 2012 confirms well-aligned band positions enable high Voc.",
    prior=0.85,
)

# Agreement 4: Iodide extends spectral range (equivalence)
# Both papers note iodide extends absorption to ~800 nm
agreement_iodide_extends_spectral_range = equivalence(
    pvsk2009_iodide_spectral,
    pvsk2012_panchromatic,
    reason="Both Kojima 2009 (IPCE to 800 nm) and Kim 2012 (panchromatic absorption) confirm CH3NH3PbI3 extends spectral response into the near-infrared.",
    prior=0.90,
)

# Agreement 5: Strong absorption in perovskites (equivalence)
# 2012 quantifies high absorption coefficient
agreement_absorption_strength = equivalence(
    pvsk2012_absorption,
    pvsk2012_panchromatic,
    reason="Kim 2012 quantifies CH3NH3PbI3 absorption coefficient as 1.5 x 10^4 cm^-1 at 550 nm and demonstrates panchromatic absorption enabling high JSC.",
    prior=0.85,
)

# Agreement 6: TiO2 conduction band injection (equivalence)
# Both confirm electron injection to TiO2 conduction band
agreement_tio2_conduction_band_injection = equivalence(
    pvsk2009_conduction_band,
    pvsk2012_band_alignment,
    reason="Kojima 2009 calculates perovskite conduction band allows electron injection to TiO2. Kim 2012 confirms well-aligned band positions enable this pathway.",
    prior=0.90,
)