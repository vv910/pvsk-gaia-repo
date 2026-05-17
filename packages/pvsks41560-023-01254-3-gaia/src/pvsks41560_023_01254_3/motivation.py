"""
Motivation section of Gu2023 bifacial perovskite minimodules paper.

Covers: background on bifacial solar cells, challenges for perovskite bifacial modules,
and the research objective of this work.
"""

from gaia.lang import claim, setting, question

# Background setting: silicon bifacial modules gain 5-30% more power
bifacial_gain_background = claim(
    "Bifacial silicon solar modules harvesting reflected and diffused rear-side sunlight "
    "produce 5% to over 30% more power output than monofacial modules, depending on albedo "
    "and installation conditions such as height and density of solar panels [@Gu2023].",
    title="Bifacial silicon modules show 5-30% power gain",
)

# Background: average albedo of 0.2 recorded in many geographic locations
average_albedo_recorded = claim(
    "An average ground-surface albedo of 0.2 or higher has been recorded in many "
    "geographic locations, determining the amount of extra radiation gain for bifacial modules [@Gu2023].",
    title="Average albedo 0.2 or higher common",
)

# Challenge: perovskite bifacial cells/modules have low efficiency
perovskite_bifacial_challenge = claim(
    "Critical challenges for achieving high-efficiency large-area bifacial perovskite solar modules "
    "include increased resistive loss from the rear semitransparent electrode and insufficient "
    "absorption of long wavelength light due to the absence of reflective metal electrodes [@Gu2023].",
    title="Perovskite bifacial challenges: resistance loss and absorption",
)

# Research objective: achieve record high efficiency AND stability
research_objective = claim(
    "This work demonstrates perovskite bifacial minimodules with both record high efficiency "
    "and stability, achieving front efficiency comparable to the best monofacial minimodules "
    "while gaining additional energy from albedo light [@Gu2023].",
    title="Research objective: record efficiency and stability",
)

# Front efficiency record achieved
front_efficiency_record = claim(
    "The bifacial minimodules achieved a certified stabilized front efficiency of 19.2% "
    "and rear efficiency of 14.1%, with an aperture area of approximately 22.0 cm^2, "
    "comparable to the best certified monofacial minimodules [@Gu2023].",
    title="Front efficiency comparable to monofacial record",
)

# Stability demonstrated: 97% retention after 6000h
stability_demonstrated = claim(
    "The bifacial minimodule retained 97% of its initial power conversion efficiency after "
    "light soaking under 1-sun illumination for over 6,000 hours at 60 plus/minus 5 degrees C, "
    "demonstrating the most stable reported perovskite minimodule [@Gu2023].",
    title="97% retention after 6000h light soaking",
)

# Power generation density measurement under 1 sun + albedo
power_generation_density_measurement = claim(
    "The small-area single-junction bifacial perovskite cells have a power-generation density "
    "of 26.4 mW/cm^2 under 1-sun illumination and an albedo of 0.2, exceeding any reported "
    "single-junction perovskite solar cells [@Gu2023].",
    title="PGD of 26.4 mW/cm2 at albedo 0.2",
)

# Bifaciality measurement
bifaciality_measurement = claim(
    "The bifacial minimodules show a bifaciality of 74.3%, converting to a power-generation "
    "density of over 23 mW/cm^2 at an albedo of 0.2 under 1-sun front illumination [@Gu2023].",
    title="Bifaciality of 74.3% and PGD over 23 mW/cm2",
)

# Initial efficiency retention (97% after 6000h)
initial_efficiency_retention = claim(
    "The bifacial minimodule retained 97% of its initial efficiency after 6,000 hours of "
    "light soaking under simulated 1-sun illumination in air at 60 plus/minus 5 degrees C "
    "from the front side [@Gu2023].",
    title="97% initial efficiency retention after 6000h",
)