"""Conclusion and summary of R2R perovskite solar cell research."""

from gaia.lang import (
    claim,
    setting,
    support,
)

# Main conclusions
first_demo_conclusion = claim(
    "This work successfully addressed the key challenges for low-cost roll-to-roll production of large-area perovskite solar modules and demonstrated the world-first fully roll-to-roll-fabricated perovskite solar modules (including back electrodes) on a commercial substrate [@Weerasinghe2024].",
    title="World-first fully R2R-fabricated PeSC modules",
)

carbon_ink_achievement = claim(
    "A perovskite-friendly carbon ink was developed to replace vacuum-processed metal electrodes, the highest-cost component in perovskite solar cells, enabling the high-throughput, vacuum-free fabrication of perovskite solar cells using only roll-to-roll processes [@Weerasinghe2024].",
    title="Carbon ink replaces vacuum electrodes",
)

throughput_system = claim(
    "Automated roll-to-roll fabrication and testing systems were developed to take full advantage of high-throughput fabrication, allowing thousands of research cells to be fabricated and tested in a single day to rapidly improve roll-to-roll experimentation [@Weerasinghe2024].",
    title="Automated R2R systems enable high-throughput",
)

cell_record = claim(
    "Further optimisation of the process and device configuration enabled fully roll-to-roll fabricated perovskite solar cells with up to 15.5% PCE, which represents the record efficiency for fully roll-to-roll fabricated perovskite solar cells to date [@Weerasinghe2024].",
    title="15.5% PCE record for fully R2R-fabricated cells",
)

module_record = claim(
    "The first demonstration of fully roll-to-roll printed perovskite solar modules with up to 11% PCE based on the active area of the module (~50 cm²) was achieved, with all developments performed with due consideration to upscaling [@Weerasinghe2024].",
    title="11% PCE for fully R2R-printed modules",
)

cost_conclusion = claim(
    "The cost model developed in this work predicts the projected manufacturing cost of modules likely to be approximately 0.7 USD/W_p with the potential for substantial further reduction via replacing remaining high-cost components with low-cost alternatives. This work demonstrates significant progress of the perovskite solar technology towards low-cost at-scale commercial manufacturing [@Weerasinghe2024].",
    title="0.7 USD/W_p manufacturing cost predicted",
)

future_direction = claim(
    "The next step for the technology would be exploring high-value PV markets at the predicted manufacturing costs while addressing the remaining high-cost components to sustainably advance the technology towards commercialisation, including developing a perovskite-friendly conductive carbon ink at least as conductive as TCEs to produce efficient silver-free PeSC modules [@Weerasinghe2024].",
    title="Silver-free modules as next development target",
)

__all__ = [
    "first_demo_conclusion",
    "carbon_ink_achievement",
    "throughput_system",
    "cell_record",
    "module_record",
    "cost_conclusion",
    "future_direction",
]