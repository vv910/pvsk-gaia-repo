"""Transitioning from cells to modules with R2R processes."""

from gaia.lang import (
    claim,
    setting,
    support,
)

# Module fabrication process
module_scalability = claim(
    "The optimised device fabrication parameters were used to produce large-area modules using the same scalable deposition methods with larger SD heads. A 10 cm wide substrate with pre-patterned TCE was used, with SD heads having five channels to produce five-cell modules [@Weerasinghe2024].",
    title="Module fabrication uses scaled-up SD coating",
)

five_channel_deposition = claim(
    "The optimised flow rate for single-stripe coating was simply multiplied by five to produce five-cell modules. Flow rates for the coating of 5 stripes using PbI₂:FAI, MAI, HTAB, P3HT and carbon inks were 100, 300, 140, 92, and 600 μL min⁻¹, respectively [@Weerasinghe2024].",
    title="Five-channel SD coating for module production",
)

carbon_ink_deposition = claim(
    "For the R2R-deposited electrode, the carbon ink was deposited using the reverse gravure (RG) technique. The modules were completed by R2R screen printing a silver paste on the carbon film using an industrial R2R screen printer [@Weerasinghe2024].",
    title="RG carbon coating and screen printing for module electrodes",
)

silver_grid_design = claim(
    "The silver grid design achieved minimal coverage while maintaining adequate conductivity, at least surpassing that of the front electrode, for efficient charge collection. A 0.2 mm line with a 180 mesh screen provided the finest pattern that could be consistently printed onto the carbon surface [@Weerasinghe2024].",
    title="Silver grid design for optimal charge collection",
)

carbon_sheet_resistance = claim(
    "The carbon layer had a sheet resistance of approximately 800 Ω sq⁻¹, making it necessary to incorporate additional conductive elements (silver grids) alongside the carbon layer. Cells without a grid design exhibited significantly poorer performance compared to those with grids [@Weerasinghe2024].",
    title="High carbon sheet resistance requires grid design",
)

# Module specifications
module_active_area = claim(
    "The active area of each strip cell was typically approximately 10 cm² (width: ~1.1 cm and length: 9.0 cm) resulting in an active module area of approximately 50 cm² (1.1 cm × 9 cm × 5 cells) [@Weerasinghe2024].",
    title="Module active area ~50 cm²",
)

module_gff = claim(
    "The geometric fill factor (GFF), defined as the cell area over total area (cell area + gap area), of the modules is 75%. This is lower than laser-scribed modules with demonstrated GFF of up to 99% due to the inherent limitation of the stripe-pattern approach, though laser scribing may not be suitable for high-throughput, cost-effective manufacturing [@Weerasinghe2024].",
    title="Module GFF is 75% due to stripe pattern limitation",
)

module_performance = claim(
    "The entirely R2R-fabricated modules demonstrated up to 11.0% active-area-based PCE with 192 mA current output, 62.3% FF, and 4.59 V V_oc in a reverse scan, and 9.96% PCE in a forward scan. The lower efficiency compared to small cells is likely due to loss of FF caused by the high resistance of the TCE and partial solvent damage incurred during the screen-printing process [@Weerasinghe2024].",
    title="Module achieves up to 11.0% PCE",
)

__all__ = [
    "module_scalability",
    "five_channel_deposition",
    "carbon_ink_deposition",
    "silver_grid_design",
    "carbon_sheet_resistance",
    "module_active_area",
    "module_gff",
    "module_performance",
]