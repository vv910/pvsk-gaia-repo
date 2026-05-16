"""Introduction and motivation for R2R perovskite solar cell research."""

from gaia.lang import (
    claim,
    setting,
    question,
    support,
    infer,
)

# Context settings
perovskite_solar_cell_pce_record = claim(
    "Perovskite solar cells (PeSCs) have demonstrated a record power conversion efficiency (PCE) of 26.1%, competitive with crystalline Si PV at 26.8% [@Weerasinghe2024].",
    title="Perovskite solar cell efficiency record",
)

lab_scale_limitation = claim(
    "Lab-scale PeSCs are often fabricated using materials or methods that are not economically viable or scalable, creating a gap between record efficiencies and commercial deployment [@Weerasinghe2024].",
    title="Lab-scale fabrication limitations",
)

vacuum_electrode_cost = claim(
    "Vacuum-processed Au electrodes are the highest-cost component in perovskite solar cells, and vacuum deposition is costly and incompatible with conventional R2R manufacturing lines [@Weerasinghe2024].",
    title="Vacuum electrode cost barrier",
)

commercial_tce_cost = claim(
    "Commercially produced transparent conductive electrodes (TCEs) are the second-highest cost component in PeSC architecture [@Weerasinghe2024].",
    title="Transparent conductive electrode cost",
)

r2r_promise = claim(
    "Flexible PeSCs enable high-volume and high-throughput manufacturing using continuous roll-to-roll (R2R) manufacturing techniques, offering prospects for high specific power (power-to-weight ratio) suitable for space, vehicle-integrated PV, and building-integrated PV applications [@Weerasinghe2024].",
    title="R2R manufacturing advantages",
)

manufacturing_challenge = claim(
    "The process of manufacturing PeSCs on a continuously-moving flexible plastic substrate imposes technical challenges, particularly time and temperature processing limitations [@Weerasinghe2024].",
    title="R2R manufacturing challenges",
)

pfsd_demonstration = claim(
    "The printing-friendly sequential deposition (PFSD) technique enabled the first PeSCs comprising R2R-deposited electron transport layer (ETL), light-absorbing layer, and hole-transport layer (HTL), with up to 11% PCE achieved for a small-area device [@Weerasinghe2024].",
    title="PFSD technique enables R2R PeSCs",
)

# Research question
main_question = question(
    "Can entirely R2R-printed perovskite solar cell modules be fabricated under ambient room conditions with competitive efficiency and cost?",
    title="Main research question",
)

# Core claims for this work
first_fully_r2r_cells = claim(
    "This work reports the first fully R2R-printed individual PeSCs with a record-high 15.5% PCE, fabricated under ambient room conditions using perovskite-friendly carbon inks to replace vacuum-based electrodes [@Weerasinghe2024].",
    title="First fully R2R-fabricated PeSCs with 15.5% PCE",
)

first_fully_r2r_modules = claim(
    "This work demonstrates the first PeSC modules produced using only industry-relevant R2R fabrication techniques under ambient room conditions, exhibiting up to 11.0% PCE for ~50 cm² active area modules [@Weerasinghe2024].",
    title="First fully R2R-fabricated PeSC modules with 11% PCE",
)

high_throughput_platform = claim(
    "A high-throughput R2R experimental platform was developed that mimics manufacturing processes to produce and test thousands of research cells per day, enabling rapid optimization over large parameter spaces [@Weerasinghe2024].",
    title="High-throughput R2R experimental platform",
)

cost_prediction = claim(
    "Based on the devices produced in this work, a manufacturing cost of approximately 0.7 USD/W_p is predicted for a production rate of 1,000,000 m² per year in Australia, with potential for further significant cost reductions [@Weerasinghe2024].",
    title="R2R PeSC manufacturing cost prediction",
)

__all__ = [
    "perovskite_solar_cell_pce_record",
    "lab_scale_limitation",
    "vacuum_electrode_cost",
    "commercial_tce_cost",
    "r2r_promise",
    "manufacturing_challenge",
    "pfsd_demonstration",
    "main_question",
    "first_fully_r2r_cells",
    "first_fully_r2r_modules",
    "high_throughput_platform",
    "cost_prediction",
]