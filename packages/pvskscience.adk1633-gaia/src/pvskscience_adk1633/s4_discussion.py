"""
Section 4: Discussion.

This module covers the interpretation and implications of the DMDP findings,
the mechanism of bimolecular passivation, and future directions.
"""

from gaia.lang import claim, setting, support, induction

# DMDP mitigates complex carrier recombination
dmdp_mitigation = claim(
    "Realizing both chemical and field-effect passivation by the combined use of methylthio and diammonium molecules has mitigated complex carrier recombination issues at the perovskite/ETL interface [@Liu2024].",
    title="DMDP mitigates interface carrier recombination",
)

# Fivefold longer carrier lifetime
carrier_lifetime_improvement = claim(
    "The DMDP approach led to a fivefold longer carrier lifetime compared with control devices, indicating effective suppression of nonradiative recombination pathways [@Liu2024].",
    title="Fivefold longer carrier lifetime",
)

# One-third PLQY loss
plqy_loss_reduction = claim(
    "The DMDP approach resulted in one-third the photoluminescence quantum yield (PLQY) loss compared with control devices after C60 deposition, demonstrating reduced interface recombination [@Liu2024].",
    title="One-third PLQY loss",
)

# Certification achievement
certified_quasi_steady_state = claim(
    "The DMDP strategy enabled a certified quasi-steady-state PCE of 25.1% for inverted PSCs, exceeding the previous benchmark of 25% for such devices [@Liu2024].",
    title="Certified QSS PCE of 25.1%",
)

# Stable operation at 65C for >2000 hours
stable_operation = claim(
    "DMDP-based devices maintained stable operation at 65 degrees C for more than 2000 hours in ambient air under 1 sun illumination, retaining 96% of initial PCE [@Liu2024].",
    title="Stable operation >2000h at 65C in air",
)

# Monolithic all-perovskite tandem cells at 28.1% PCE
tandem_achievement = claim(
    "Monolithic all-perovskite tandem solar cells with the DMDP strategy achieved 28.1% PCE, demonstrating the applicability of bimolecular passivation to tandem architecture [@Liu2024].",
    title="Tandem cells achieve 28.1% PCE",
)

# Multimolecule passivation as promising direction
future_direction = claim(
    "The multimolecule passivation approach, along with diverse functionalities, represents a promising direction for exploring next-generation passivation strategies to achieve improved performance and stability in perovskite optoelectronics [@Liu2024].",
    title="Multimolecule passivation as promising direction",
)

# DMDP strategy explained by combined mechanisms
strat_dmdp_strategy = support(
    [carrier_lifetime_improvement, plqy_loss_reduction],
    dmdp_mitigation,
    reason="The fivefold longer carrier lifetime and one-third PLQY loss directly demonstrate that the combined chemical passivation (from methylthio molecules) and field-effect passivation (from diammonium molecules) effectively mitigates carrier recombination at the perovskite/ETL interface [@Liu2024].",
    prior=0.5,
)

# Tandem success supports bimolecular approach
dmdp_law = claim(
    "The DMDP strategy (combined chemical and field-effect passivation) effectively mitigates interface recombination in perovskite solar cells, enabling both high single-junction PCE and tandem performance [@Liu2024].",
    title="DMDP strategy mitigates interface recombination",
)

s_lifetime = support(
    [dmdp_law],
    carrier_lifetime_improvement,
    reason="The DMDP law predicts that mitigation of interface recombination would lead to extended carrier lifetimes, confirmed by the fivefold improvement observed",
    prior=0.85,
)

s_qss = support(
    [dmdp_law],
    certified_quasi_steady_state,
    reason="The DMDP law predicts that mitigation of interface recombination would enable high certified QSS PCE, confirmed by 25.1% certification",
    prior=0.85,
)

ind_tandem = induction(
    s_lifetime,
    s_qss,
    law=dmdp_law,
    reason="Independent observations of carrier lifetime and certified QSS PCE both confirm that DMDP mitigates interface recombination; this law then explains tandem cell performance of 28.1%",
)

__all__ = [
    "dmdp_mitigation",
    "dmdp_law",
    "carrier_lifetime_improvement",
    "plqy_loss_reduction",
    "certified_quasi_steady_state",
    "stable_operation",
    "tandem_achievement",
    "future_direction",
    "strat_dmdp_strategy",
    "ind_tandem",
    "s_lifetime",
    "s_qss",
]