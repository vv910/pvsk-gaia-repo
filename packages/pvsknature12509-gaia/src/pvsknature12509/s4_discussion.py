"""
Discussion module for Liu et al. 2013 Nature paper.

Paper: Efficient planar heterojunction perovskite solar cells by vapour deposition
Citation: [@Liu2013]

This module covers the discussion and conclusion sections.
"""

from gaia.lang import (
    claim,
    setting,
    support,
    infer,
    contradiction,
)

# Main conclusion - perovskite versatility
perovskite_versatility = claim(
    "The perovskite absorbers are versatile materials for incorporation into highly efficient solar cells, given: "
    "(1) low-temperature processing requirements, (2) option of using solution processing, vapour deposition, or both, "
    "(3) simplified device architecture, and (4) availability of many other metal and organic salts that could form "
    "a perovskite structure [@Liu2013].",
    title="Perovskite absorber versatility",
)

# Vapour deposition advantage for large-area processing
vapour_deposition_maturity = claim(
    "Vapour deposition is a mature technique used in the glazing industry, liquid-crystal display industry, and thin-film "
    "solar cell industry, enabling full optimization of electronic contact at interfaces through multilayers with controlled "
    "levels of doping [@Liu2013].",
    title="Vapour deposition maturity for industrial applications",
)

# OLED compatibility
oled_vapour_deposition_compatibility = claim(
    "Organic light-emitting diodes (OLEDs) have proved commercially sound with extremely thin multilayer stacks fabricated "
    "by vapour deposition, demonstrating the viability of vapour-phase processing for organic-containing devices [@Liu2013].",
    title="OLED vapour deposition commercial success",
)

# Tandem application potential
tandem_top_cell_potential = claim(
    "An interesting possibility for the vapour-deposited perovskite technology is to use it as a 'top cell' in a hybrid "
    "tandem junction with either crystalline silicon or copper indium gallium (di)selenide (CIGS), as the perovskite cells "
    "have achieved performance sufficient to increase absolute efficiency of high-efficiency crystalline silicon and CIGS "
    "solar cells [@Liu2013].",
    title="Perovskite as top cell in tandem configuration",
)

# All-perovskite multi-junction prospect
all_perovskite_multijunction = claim(
    "Ultimately an 'all-perovskite' multi-junction cell should be realizable, leveraging the versatility of the perovskite "
    "material family across different bandgaps [@Liu2013].",
    title="All-perovskite multi-junction prospect",
)

# Compatibility with existing PV infrastructure
infra_compatibility = claim(
    "Vapour deposition of perovskite layers is entirely compatible with conventional processing methods for silicon-wafer-based "
    "and thin-film solar cells, meaning existing manufacturing infrastructure could be used to scale up this technology [@Liu2013].",
    title="Compatibility with existing PV manufacturing infrastructure",
)

# Manufacturing question
manufacturing_route_question = claim(
    "Whether vapour deposition emerges as the preferred route for manufacture or simply represents a benchmark method for "
    "fabricating extremely uniform films (that will ultimately be matched by solution processing) remains to be seen [@Liu2013].",
    title="Manufacturing route question - vapour vs solution",
)

# Diffusion length - work needed
diffusion_length_needs_work = claim(
    "More work is required to determine the electron and hole diffusion lengths precisely and to understand the primary "
    "excitation and the mechanisms for free-charge generation in these materials [@Liu2013].",
    title="Future work needed on diffusion length characterization",
)

# Key target achievement
wider_bandgap_top_cell_target = claim(
    "A key target for the photovoltaics community has been to find a wider-bandgap highly efficient 'top cell' to enable "
    "the next step in improving the performance of crystalline silicon and existing second-generation thin-film solar cells. "
    "This perovskite technology is now compatible with first- and second-generation technologies and may find rapid "
    "adoption by the conventional photovoltaics community and industry [@Liu2013].",
    title="Perovskite as wide-bandgap top cell achieving community target",
)

# Efficiency threshold achievement
threshold_15_percent = claim(
    "The planar heterojunction perovskite solar cell built with vapour-deposited absorber has crossed the 15% efficiency "
    "threshold, demonstrating that mesostructure is not necessary to achieve high efficiencies with organometal halide "
    "perovskite absorbers [@Liu2013].",
    title="15% efficiency threshold crossed - mesostructure not necessary",
)

# Planar architecture sufficiency
planar_architecture_sufficiency = claim(
    "Perovskite absorbers can function at the highest efficiencies in simplified device architectures, without the need "
    "for complex nanostructures, as demonstrated by achieving over 15% PCE in a simple planar heterojunction configuration [@Liu2013].",
    title="Planar architecture sufficient for highest perovskite efficiencies",
)

# Future directions
future_directions = claim(
    "Future work should focus on: (1) precise determination of electron and hole diffusion lengths, "
    "(2) understanding primary excitation and free-charge generation mechanisms, "
    "(3) optimizing interface engineering, and (4) scaling up manufacturing processes [@Liu2013].",
    title="Future research directions",
)

# Key figures of merit improvement
vapour_vs_solution_fom_comparison = claim(
    "Vapour-deposited devices outperform solution-processed planar heterojunction devices across all key figures of merit: "
    "Jsc (21.5 vs 17.6 mA cm^-2), Voc (1.07 vs 0.84 V), FF (0.68 vs 0.58), and PCE (15.4% vs 8.6%) [@Liu2013].",
    title="Vapour vs solution processing key metrics comparison",
)