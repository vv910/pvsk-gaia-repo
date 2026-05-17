"""
Module structure and rear electrode design (Section 2 of Gu2023).

Covers: p-i-n device structure, ITO transparent electrode properties,
Ag grid design for balanced resistance loss and bifacial gain.
"""

from gaia.lang import claim, setting

# Device structure: p-i-n with PTAA and C60
module_structure_p_i_n = claim(
    "The bifacial perovskite module adopts a p-i-n perovskite solar cell structure with "
    "poly[bis(4-phenyl)(2,4,6-trimethylphenyl)amine] (PTAA) as the hole transport layer "
    "and fullerene (C60) as the electron transport layer, with perovskite composition of "
    "MA_0.7FA_0.3PbI_3 or FA_0.92Cs_0.08PbI_3 with slightly excess CsI [@Gu2023].",
    title="p-i-n structure with PTAA/C60",
)

# ITO sheet resistance achieved
ito_sheet_resistance = claim(
    "A low sheet resistance of approximately 30 ohms per square with high transparency was "
    "achieved for indium tin oxide (ITO) of 150 nm sputtered at room temperature, but "
    "bifacial minimodules showed poor fill factor (FF) of 0.39 when ITO directly replaced "
    "the copper electrode [@Gu2023].",
    title="ITO sheet resistance 30 ohm/sq, poor FF without Ag grid",
)

# Ag grid design rationale
ag_grid_design = claim(
    "Applying silver grids on a rear ITO electrode is an effective way to reduce resistance "
    "loss, but requires rational design to balance resistance loss and the shadowing effect "
    "of silver grids, which reduces bifacial gain [@Gu2023].",
    title="Ag grid design balances resistance and shading",
)

# Optimal Ag grid spacing calculated
optimal_ag_grid_spacing = claim(
    "With Ag grid width of 0.2 mm and height of 500 nm (narrowest achievable by thermal "
    "evaporation using a shadow mask) and linear resistance of 8 ohm/cm, the optimal Ag grid "
    "spacing is approximately 2 mm at an albedo of 0.2, reducing relative PCE loss induced by "
    "rear electrode resistance from 8.6% to less than 0.9% [@Gu2023].",
    title="Optimal Ag grid spacing ~2mm reduces PCE loss to <0.9%",
)

# Relative PCE loss reduction
relative_pce_loss_reduction = claim(
    "The modeling shows that the relative PCE loss induced by the rear electrode resistance "
    "is reduced from 8.6% to less than 0.9% after adding the Ag grid with spacing of approximately 2 mm, "
    "accompanied by an increase of fill factor from 0.70 to 0.77 [@Gu2023].",
    title="PCE loss reduced from 8.6% to <0.9% with Ag grid",
)

# FF improvement with Ag grid
ff_improvement_with_ag_grid = claim(
    "The fill factor increases from 0.70 to 0.77 with optimal Ag grid spacing of approximately 2 mm, "
    "while the bifacial perovskite modules gain 15% more power output with an albedo of 0.2 "
    "compared with monofacial modules [@Gu2023].",
    title="FF increases from 0.70 to 0.77, bifacial gain 15%",
)

# Bifacial gain percentage
bifacial_gain_percentage = claim(
    "The bifacial perovskite modules gain 15% more power output with an albedo of 0.2 "
    "compared with monofacial modules, thanks to the rear-side albedo light harvesting [@Gu2023].",
    title="15% bifacial power gain at albedo 0.2",
)

# Simulated PGDs by albedo
simulated_pgds_by_albedo = claim(
    "The simulated power-generation densities of bifacial modules under 1-sun illumination "
    "are 21.5, 23.1, 24.7, and 26.4 mW/cm^2 with albedos of 0.1, 0.2, 0.3, and 0.4, respectively, "
    "based on a monofacial module with 20% aperture efficiency [@Gu2023].",
    title="Simulated PGDs: 21.5-26.4 mW/cm2 for albedos 0.1-0.4",
)