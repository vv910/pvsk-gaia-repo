"""
Perovskite solar cell stability background and motivation.

This module covers the introduction (lines 1-30 of the paper),
establishing the instability problem that motivates 2D/3D interface engineering.
"""

from gaia.lang import claim, setting

# Perovskite solar cell context
perovskite_pce_record = claim(
    "Perovskite solar cells have achieved power conversion efficiencies (PCE) beyond 22%, "
    "comparable to silicon solar cells at half the cost [@Grancini2017].",
    title="Perovskite PCE exceeds 22%",
)

instability_barrier = claim(
    "Despite impressive photovoltaic performance, perovskite solar cells suffer from "
    "poor device stability under operative conditions, failing to meet market requirements "
    "that demand <10% PCE drop for 20-25 years (equivalent to >1,000h in accelerated aging tests) [@Grancini2017].",
    title="Perovskite stability below market requirements",
)

perovskite_degradation_mechanisms = claim(
    "Perovskite materials degrade through hydrolysis when exposed to moisture, with heat, "
    "electric field, and ultraviolet exposure dramatically accelerating the process. "
    "Degradation produces hygroscopic CH3NH3X and CH(NH2)2X salts and PbX2 (X=halide) [@Grancini2017].",
    title="Moisture-driven perovskite degradation",
)

stability_limiting_factors = claim(
    "Solar cell degradation arises not only from perovskite layer instability but also from "
    "instability of other layers in the stack, particularly the organic hole transporting material (HTM) "
    "which is unstable when in contact with water [@Grancini2017].",
    title="Multi-layer degradation in perovskite cells",
)

two_d_perovskite_stability = claim(
    "Two-dimensional (2D) perovskites exhibit superior stability and water resistance "
    "compared to three-dimensional (3D) counterparts. Quasi-2D (BA)2(MA)2Pb3I10 perovskite "
    "solar cells have achieved 12% efficiency but show 30% drop after 2,250h in ambient conditions [@Grancini2017].",
    title="2D perovskites offer enhanced stability",
)

research_objective = claim(
    "This work develops an innovative concept by engineering a multidimensional junction made "
    "of 2D/3D perovskites, combining enhanced stability of 2D perovskite with panchromatic "
    "absorption and excellent charge transport of 3D ones, enabling efficient and ultra-stable "
    "solar cells [@Grancini2017].",
    title="2D/3D interface engineering approach",
)

key_innovation = claim(
    "The 2D/3D interface engineering enables HTM-free solar cells and modules substituting "
    "HTM with hydrophobic carbon electrodes, demonstrating >10,000h stability (400+ days) "
    "with zero loss in efficiency over a large-area, fully printable, low-cost 10x10 cm2 "
    "solar module with active area of ~50 cm2 [@Grancini2017].",
    title="HTM-free stable perovskite modules demonstrated",
)