"""Towards ultra-low-cost manufacturing with technoeconomic analysis."""

from gaia.lang import (
    claim,
    setting,
    support,
)

# Cost model overview
cost_model_development = claim(
    "A cost model was developed based on previous work implementing the new materials, processes and device configurations used in this work. Three device configurations (sequences A, B, and C) were considered to predict the potential for further cost reduction [@Weerasinghe2024].",
    title="Cost model developed for three device sequences",
)

sequence_a_description = claim(
    "Sequence A (high-cost, high-performance): Uses vacuum-deposited Au electrode. The combination of the gold material and the equipment purchase and running costs of a R2R evaporator is the highest cost component, followed by the commercial TCE. Other significant material costs include the encapsulation materials and the HTL, while the costs of the ETL and perovskite are negligible in comparison [@Weerasinghe2024].",
    title="Sequence A has vacuum-deposited Au electrode",
)

sequence_b_description = claim(
    "Sequence B (fully R2R-fabricated): Uses printed carbon electrode to replace vacuum-processed back electrode. This configuration shows a significant reduction in the back electrode cost, resulting in only two high-cost components: the commercial TCE and the encapsulation material [@Weerasinghe2024].",
    title="Sequence B uses printed carbon electrode",
)

sequence_c_description = claim(
    "Sequence C (ultra-low-cost printing option, not experimentally demonstrated): Eliminates remaining high-cost components, i.e., commercial TCEs and silver grids, to predict potential for further cost reduction [@Weerasinghe2024].",
    title="Sequence C eliminates TCE and silver grids",
)

# Cost results
cost_fraction_sequence_a = claim(
    "For the vacuum-deposited electrode (Seq. A), a combination of the gold material and the equipment purchase and running costs of a R2R evaporator is the highest cost component, followed by the commercial TCE [@Weerasinghe2024].",
    title="Seq A: Au electrode and TCE are highest cost components",
)

cost_fraction_sequence_b = claim(
    "For the fully printed configuration (Seq. B), the significant reduction in back electrode cost leaves only two high-cost components: the commercial TCE and the encapsulation material [@Weerasinghe2024].",
    title="Seq B: TCE and encapsulation are highest cost components",
)

production_cost_area = claim(
    "The projected production costs of the modules per unit area (m²) are: Seq. A at the highest, Seq. B significantly lower, and Seq. C potentially below Seq. B. The cost for Seq. B is likely to be lower than 1 USD/W_p [@Weerasinghe2024].",
    title="Module production cost per area",
)

production_cost_power = claim(
    "The projected production costs per peak watt (W_p) for the three sequences are: Seq. A (17.9% PCE), Seq. B (15.5% PCE), and Seq. C (10% PCE). Seq. B is likely to be lower than 1 USD/W_p, and Seq. C could be lower than 0.5 USD/W_p, representing significant reduction from previous estimates of around 1.5 USD/W_p [@Weerasinghe2024].",
    title="Module production cost per peak watt",
)

cost_reduction_achieved = claim(
    "The cost reduction results from similar or lower cost in $/m² and a higher recorded efficiency compared to previous works. However, the technology is still not able to compete with mass-produced silicon solar cells, for which module spot prices have been lower than 0.30 USD/W_p [@Weerasinghe2024].",
    title="Cost reduction achieved but still above Si",
)

market_position = claim(
    "Through market surveys and considering advantages in the form factor, R2R PeSCs could become competitive in the portable PV market at greater than 10% PCE. Therefore, the demonstration of an 11% R2R-fabricated module is a significant step forward in commercialising this technology [@Weerasinghe2024].",
    title="R2R PeSCs competitive in portable PV market",
)

future_improvement_needed = claim(
    "The printed silver used in this work may not be suitable for long-term operation for commercial applications due to corrosion issues. The next challenge would be developing a perovskite-friendly conductive carbon ink that is at least as conductive as TCEs to produce efficient silver-free PeSC modules [@Weerasinghe2024].",
    title="Silver-free modules needed for long-term stability",
)

future_cost_potential = claim(
    "Supplementary Figure 12 shows the potential for further cost reduction by eliminating the remaining high-cost components, with about 5 USD/m² module cost (excluding encapsulation) achievable [@Weerasinghe2024].",
    title="Further cost reduction potential identified",
)

__all__ = [
    "cost_model_development",
    "sequence_a_description",
    "sequence_b_description",
    "sequence_c_description",
    "cost_fraction_sequence_a",
    "cost_fraction_sequence_b",
    "production_cost_area",
    "production_cost_power",
    "cost_reduction_achieved",
    "market_position",
    "future_improvement_needed",
    "future_cost_potential",
]