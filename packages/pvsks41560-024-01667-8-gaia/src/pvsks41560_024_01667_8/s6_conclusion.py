"""
s6_conclusion.py - Conclusions and summary.

This module covers the main conclusions from the paper.
"""

from gaia.lang import claim

# Main conclusion
main_conclusion = claim(
    "This work reports an effective, scalable passivation strategy enabling homogeneous "
    "formation of phase-pure 2D perovskite capping layer on 3D perovskite surface by "
    "suppressing unfavorable phase segregations in composition and dimensionality. The "
    "selective incorporation of FABr into DABr for 3D perovskite post-treatment facilitates "
    "2D perovskite transition from mixed n=1 and n=2 to pure n=2 with lower formation "
    "enthalpy, reduced mixing enthalpy, and faster formation kinetics, thereby contributing "
    "to uniform morphology, fewer defects, faster interface charge transfer, and "
    "structurally robust 3D/2D heterojunction [@Li2024].",
    title="FABr/DABr enables homogeneous phase-pure 2D passivation",
)

# Efficiency achievements
efficiency_summary = claim(
    "Champion efficiencies of 25.61% (certified 24.95%), 24.62% (certified 24.04%), "
    "and 23.60% are achieved for small-size device (0.14 cm2), large-size device "
    "(1.04 cm2), and mini-module (13.44 cm2), respectively, demonstrating relatively "
    "small efficiency loss with increasing active area (<5% per tenfold magnification) [@Li2024].",
    title="Efficiency achievements across device sizes",
)

# Stability achievements
stability_summary = claim(
    "Solar mini-modules exhibit T80 lifetime exceeding 2000 h at MPPT under continuous "
    "light illumination, indicating excellent operational stability. The phase-pure n=2 "
    "2D layer provides both structural and operational stability to the 3D/2D "
    "heterojunction device [@Li2024].",
    title="Excellent operational stability (T80 > 2000 h)",
)

# Large module achievements
large_module_summary = claim(
    "20 cm x 20 cm and 30 cm x 30 cm large-size PSMs demonstrate champion efficiencies "
    "of 18.90% (aperture area 310 cm2) and 17.59% (aperture area 802 cm2), respectively, "
    "confirming the scalability and effectiveness of the homogenized low-dimensional "
    "structure passivation strategy for commercial manufacturing [@Li2024].",
    title="Large module efficiencies (18.90% and 17.59%)",
)

# Mechanism summary
mechanism_summary = claim(
    "The homogeneous phase-pure n=2 2D perovskite forms because triple-halide composition "
    "(DA2FAPb2(I4-0.5xClx)Br3) has lower formation enthalpy than n=1 or n=3 phases, "
    "enabling preferential formation. FABr passivates FA vacancies and reacts with "
    "residual PbI2 to form uniform crystalline layer. Combined with DABr, this strengthens "
    "reaction between PbX2 and 2D ligands, preventing phase separation and achieving "
    "uniform morphology over large areas [@Li2024].",
    title="Mechanism of homogeneous phase-pure n=2 formation",
)

# Scalability contribution
scalability_contribution = claim(
    "The DABr/FABr passivation strategy is compatible with printing technology, enabling "
    "fully slot-die printed large solar modules. This demonstrates the feasibility of "
    "upscaling manufacturing while maintaining high efficiency and stability, addressing "
    "a key challenge in perovskite solar cell commercialization [@Li2024].",
    title="Strategy compatible with scalable manufacturing",
)

# Impact statement
impact_statement = claim(
    "This homogenized low-dimensional structure passivation strategy holds considerable "
    "potential for accelerating the commercialization of PSMs by providing an effective "
    "route to stable, efficient, and scalable 3D/2D heterojunction devices that maintain "
    "performance from lab-scale cells to manufacturing-scale modules [@Li2024].",
    title="Potential impact on PSM commercialization",
)