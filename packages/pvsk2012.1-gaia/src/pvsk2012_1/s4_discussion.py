from gaia.lang import (
    claim,
    setting,
    support,
    compare,
    deduction,
    abduction,
    induction,
    contradiction,
    complement,
)

from .motivation import (
    jsc_17_6_ma_cm2,
    voc_0_888_v,
    ff_0_62,
    bandgap_1_5_ev,
    tiO2_bandgap_3_1_ev,
    charge_separation_mechanism,
    stability_improvement,
)

from .s3_results import (
    hole_injection_mechanism,
)

__all__ = [
    "panchromatic_absorption_leads_to_high_jsc",
    "charge_separation_well_aligned",
    "solid_state_dramatically_improved_stability",
    "pce_9_7_percent_conclusion",
    # Strategies
    "strat_panchromatic_absorption",
    "strat_charge_separation",
    "strat_stability",
    "strat_pce_conclusion",
    "strat_bandgap_evidence",
]


# ===== DISCUSSION / CONCLUSIONS =====

panchromatic_absorption_leads_to_high_jsc = claim(
    "CH3NH3PbI3 deposited on TiO2 particles exhibits panchromatic absorption of visible light, leading to high photocurrent density in submicron-thick thin films (JSC = 17.6 mA/cm^2 in 0.6 micrometer-thick mesoporous TiO2 film).",
    title="Panchromatic absorption enables high JSC"
)

charge_separation_well_aligned = claim(
    "The band positions of TiO2, CH3NH3PbI3, and spiro-MeOTAD are well aligned for charge separation. The valence band energy (-5.43 eV) and conduction band energy (-3.93 eV) of CH3NH3PbI3, combined with the TiO2 conduction band position, enable efficient charge separation.",
    title="Band alignment favorable for charge separation"
)

solid_state_dramatically_improved_stability = claim(
    "The use of a solid hole conductor (spiro-MeOTAD) dramatically improved device stability compared to CH3NH3PbI3-sensitized liquid junction cells. The PCE remained stable during 500+ hours of testing without encapsulation.",
    title="Solid-state configuration dramatically improves stability"
)

pce_9_7_percent_conclusion = claim(
    "A power conversion efficiency of 9.7% was achieved under AM 1.5G illumination with excellent long-term stability, rendering this system very attractive for further investigations.",
    title="9.7% PCE with excellent stability achieved"
)


# ===== REASONING STRATEGIES =====

# Support for panchromatic absorption claim
strat_panchromatic_absorption = support(
    [panchromatic_absorption_leads_to_high_jsc, charge_separation_well_aligned],
    jsc_17_6_ma_cm2,
    reason=(
        "The panchromatic absorption of CH3NH3PbI3 combined with well-aligned band positions "
        " jointly explain the high JSC of 17.6 mA/cm^2 achieved in submicron-thick films."
    ),
    prior=0.75,
)

# Charge separation reasoning
strat_charge_separation = support(
    [charge_separation_well_aligned, hole_injection_mechanism],
    charge_separation_mechanism,
    reason=(
        "The well-aligned band structure enables efficient charge separation. TAS measurements "
        "confirm hole injection from excited perovskite into spiro-MeOTAD, followed by electron "
        "transfer to TiO2."
    ),
    prior=0.7,
)

# Stability reasoning
strat_stability = support(
    [solid_state_dramatically_improved_stability],
    stability_improvement,
    reason=(
        "The solid-state configuration eliminates the electrolyte dissolution problem that plagued "
        "liquid junction cells, leading to dramatically improved stability over 500+ hours."
    ),
    prior=0.75,
)

# PCE conclusion - abduction pattern
# Theory predicts 9.7% based on JSC, VOC, FF values
pce_prediction_from_individual_params = claim(
    "Based on JSC of 17.6 mA/cm^2, VOC of 0.888 V, and FF of 0.62, the theoretical PCE calculation yields approximately 9.7%.",
    title="PCE calculated from JSC, VOC, FF"
)

strat_bandgap_evidence = support(
    [bandgap_1_5_ev, tiO2_bandgap_3_1_ev],
    charge_separation_well_aligned,
    reason=(
        "The bandgap of 1.5 eV for CH3NH3PbI3 (direct transition) and 3.1 eV for TiO2 (indirect transition) "
        " establish the energy level positions that enable favorable band alignment for charge separation."
    ),
    prior=0.75,
)

strat_pce_conclusion = support(
    [pce_prediction_from_individual_params, jsc_17_6_ma_cm2, voc_0_888_v, ff_0_62],
    pce_9_7_percent_conclusion,
    reason=(
        "The individual photovoltaic parameters (JSC=17.6 mA/cm^2, VOC=0.888 V, FF=0.62) were all measured "
        "independently and together yield PCE = 9.7%, representing the highest efficiency for solid-state "
        "perovskite-sensitized solar cells at that time."
    ),
    prior=0.85,
)

# Long term stability reasoning - induction pattern for multiple observations
stability_observation_1 = claim(
    "JSC showed only slight decrease during the first 200 hours, attaining a plateau thereafter.",
    title="JSC stability observation"
)

stability_observation_2 = claim(
    "VOC remained stable throughout the 500+ hour test period.",
    title="VOC stability observation"
)

stability_observation_3 = claim(
    "FF improved and stabilized with time, contributing to a 14% increase in initial PCE after 200 hours.",
    title="FF improvement observation"
)

# Long term stability reasoning - multiple independent observations support stability claim
strat_stability_obs = support(
    [stability_observation_1, stability_observation_2, stability_observation_3],
    solid_state_dramatically_improved_stability,
    reason="Three independent stability indicators (JSC, VOC, and FF) all demonstrate stability of the solid-state device over 500+ hours",
    prior=0.85,
)