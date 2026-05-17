"""
All-perovskite tandem solar cells with improved grain surface passivation.

Lin et al., Nature 2022 (https://doi.org/10.1038/s41586-021-04372-8)

Motivation module -- introduces the research problem and key background.
"""

from gaia.lang import claim, setting, question

# Background on perovskite tandem solar cells
perovskite_tunable_bandgap = claim(
    "Metal-halide perovskites have bandgaps tunable from approximately 1.2 eV to 3.0 eV "
    "through compositional engineering, making them suitable for tandem solar cell applications.",
    title="Perovskite bandgap tunability",
)

tandem_structure = claim(
    "An all-perovskite tandem solar cell is constructed by stacking a mixed bromide/iodide "
    "wide-bandgap (WBG, approximately 1.8 eV) perovskite front cell and a mixed lead-tin "
    "(Pb-Sn) narrow-bandgap (NBG, approximately 1.2 eV) perovskite back cell.",
    title="All-perovskite tandem structure",
)

low_photocurrent_limitation = claim(
    "The certified power conversion efficiency (PCE) of all-perovskite tandem solar cells had "
    "not surpassed that of single-junction perovskite solar cells (PSCs), with a limitation "
    "dominated by low photocurrent density (below 16 mA cm^-2).",
    title="Low photocurrent density limitation",
)

thick_absorber_needed = claim(
    "High photocurrent densities require a Pb-Sn perovskite active layer more than 1 micrometer "
    "thick in the bottom subcell to satisfy the current-matching condition.",
    title="Thick absorber requirement for tandem cells",
)

short_diffusion_length = claim(
    "Efficient (>20%) Pb-Sn PSCs have so far only been demonstrated using an active-layer "
    "thickness of less than 1 micrometer, attributed to the short carrier diffusion length of "
    "polycrystalline Pb-Sn perovskite thin films.",
    title="Short carrier diffusion length limits absorber thickness",
)

grain_surface_passivation_route = claim(
    "Grain surface passivation is a promising route to increase the carrier diffusion length of "
    "perovskite films, given that grain surfaces exhibit trap density one to several orders of "
    "magnitude higher than within the grain.",
    title="Grain surface passivation increases diffusion length",
)

# Problem identification
thickness_limited_by_passivation = claim(
    "The absorber thickness of grain-surface-passivated Pb-Sn PSCs has been limited to less than "
    "1 micrometer in optimized devices, due to incomplete adsorption of passivating agent into "
    "defective sites during film formation.",
    title="Passivation incomplete at current thicknesses",
)

cf3_pa_hypothesis = claim(
    "Enhancing the adsorption of passivating agents during perovskite film formation could "
    "further improve passivation and thus increase the diffusion length in thick Pb-Sn perovskite "
    "films, enabling thicker absorber layers and higher matched photocurrent densities in "
    "all-perovskite tandem solar cells.",
    title="CF3-PA enhanced adsorption hypothesis",
)

# Key research question
research_question = question(
    "Can CF3-PA passivation enable thick Pb-Sn perovskite absorbers (>1 micrometer) with "
    "sufficient carrier diffusion length to achieve high photocurrent density in all-perovskite "
    "tandem solar cells?"
)

# Key hypothesis
certified_26_4_percent = claim(
    "A certified power conversion efficiency of 26.4% was achieved in all-perovskite tandem solar "
    "cells, exceeding that of the best-performing single-junction perovskite solar cells.",
    title="26.4% certified tandem efficiency",
    metadata={"source": "artifacts/full.md"}
)

stability_600h = claim(
    "Encapsulated tandem devices retain more than 90% of their initial performance after 600 hours "
    "of operation at the maximum power point under 1 Sun illumination in ambient conditions.",
    title="Tandem device operational stability",
    metadata={"source": "artifacts/full.md"}
)

__all__ = [
    "perovskite_tunable_bandgap",
    "tandem_structure",
    "low_photocurrent_limitation",
    "thick_absorber_needed",
    "short_diffusion_length",
    "grain_surface_passivation_route",
    "thickness_limited_by_passivation",
    "cf3_pa_hypothesis",
    "research_question",
    "certified_26_4_percent",
    "stability_600h",
]