"""
Methods module for Liu et al. 2013 Nature paper.

Paper: Efficient planar heterojunction perovskite solar cells by vapour deposition
Citation: [@Liu2013]

This module covers the experimental methods and fabrication procedures.
"""

from gaia.lang import (
    claim,
    setting,
)

# Device substrate preparation
substrate_preparation_method = claim(
    "FTO-coated glass (TEC7, 7V/% sheet resistivity) was patterned by etching with Zn metal powder and 2M HCl, "
    "cleaned with 2% Hellmanex solution, rinsed with deionized water, acetone and ethanol, dried with clean dry air, "
    "and treated with oxygen plasma for 10 minutes [@Liu2013].",
    title="FTO substrate preparation protocol",
)

# Compact TiO2 layer deposition
compact_tio2_deposition = claim(
    "A compact n-type TiO2 layer was deposited by spin-coating an acidic solution of titanium isopropoxide in ethanol "
    "at 2,000 rpm for 1 min, followed by drying at 150°C for 10 min and sintering at 500°C for 30 min [@Liu2013].",
    title="Compact TiO2 layer deposition method",
)

# Dual-source evaporation system
dual_source_evaporation_system = claim(
    "The dual-source evaporation system (Kurt J. Lesker Mini Spectros) uses ceramic crucibles (OLED sources) in a "
    "nitrogen-filled glovebox, with simultaneous evaporation of CH3NH3I (organic source) and PbCl2 (inorganic source) "
    "at 10^-5 mbar pressure [@Liu2013].",
    title="Dual-source thermal evaporation system",
)

# Precursor materials
precursor_materials = claim(
    "The precursor salts are methylammonium iodide (CH3NH3I) and lead chloride (PbCl2), with approximately 500 mg "
    "of CH3NH3I and 100 mg of PbCl2 placed in separate crucibles for evaporation [@Liu2013].",
    title="Precursor materials for vapour deposition",
)

# Vapour deposition conditions
deposition_pressure = claim(
    "The chamber was pumped down to below 10^-5 mbar before deposition, with sources heated to approximately 120°C "
    "for CH3NH3I and 325°C for PbCl2 to remove volatile impurities before deposition [@Liu2013].",
    title="Vapour deposition pressure and pre-deposition heating",
)

# Optimized deposition parameters
optimized_deposition_rate = claim(
    "The optimal deposition rate was 5.3 Å s^-1 for CH3NH3I (achieved with crucible temperature around 116°C) and "
    "1 Å s^-1 for PbCl2 (achieved with crucible temperature around 320°C), maintained for approximately 128 min [@Liu2013].",
    title="Optimized evaporation rates and temperatures",
)

# As-deposited molar ratio
as_deposited_molar_ratio = claim(
    "The as-deposited molar ratio of CH3NH3I to PbCl2 was 4:1 (based on sensor readings above the crucibles), "
    "with deposition rates varying by approximately ±15% for CH3NH3I and ±10% for PbCl2 during evaporation [@Liu2013].",
    title="As-deposited precursor molar ratio",
)

# Film annealing
film_annealing = claim(
    "As-deposited films were annealed at 100°C for 45 min in N2-filled glovebox before spin-coating the hole transporter "
    "to enable full crystallization of the perovskite, resulting in a dark reddish-brown colour and average thickness "
    "of approximately 330 nm [@Liu2013].",
    title="Post-deposition film annealing protocol",
)

# Hole-transporter deposition
hole_transporter_deposition = claim(
    "The hole-transporter layer was deposited by spin-coating (2,000 rpm for 45 s) 25 µl of chlorobenzene solution "
    "containing 61.4 mM spiro-OMeTAD, 55 mM tert-butylpyridine (tBP), and 26 mM lithium bis(trifluoromethylsulfonyl)imide salt [@Liu2013].",
    title="Hole-transporter layer spin-coating protocol",
)

# Device completion
device_completion = claim(
    "Devices were completed by thermal evaporation of silver cathode at 10^-6 mbar, with devices left in desiccator "
    "overnight and tested in air immediately after cathode fabrication [@Liu2013].",
    title="Device completion by silver cathode evaporation",
)

# Tooling factor estimation
tooling_factor_method = claim(
    "Tooling factors were estimated by comparing quartz crystal monitor readings to actual deposited thickness measured "
    "by surface profilometer, yielding factors of 2.16 for CH3NH3I and 5.41 for PbCl2 to account for source-to-monitor "
    "versus source-to-substrate distance differences [@Liu2013].",
    title="Tooling factor estimation method",
)

# Film thickness optimization
film_thickness_optimization = claim(
    "Film thickness was varied from 125 to 500 nm at optimum CH3NH3I:PbCl2 ratio of 3.5:1, with optimum performance "
    "found at 330 nm thickness for the planar heterojunction configuration [@Liu2013].",
    title="Film thickness optimization procedure",
)

# Composition optimization
composition_optimization = claim(
    "The CH3NH3I to PbCl2 ratio was varied from 1:1 to 7:1 at fixed film thickness of 125 nm initially, then fine-tuned "
    "for films with approximately 330 nm thickness to obtain optimum composition of 4:1 [@Liu2013].",
    title="Precursor composition optimization",
)