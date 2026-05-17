"""
Jeon et al. 2014 paper formalization.

This module covers the Introduction (Section 1) of the paper:
- Background on organolead trihalide perovskite materials for photovoltaic cells
- Prior work on mesoscopic and planar heterojunction architectures
- Problem: spin-coating does not yield homogeneous perovskite layers
- Proposed solution: solvent-engineering technology with GBL/DMSO mixed solvent + toluene drip
"""

from gaia.lang import (
    claim,
    setting,
    question,
)

# --- Perovskite material properties (established background) ---

perovskite_optical_properties = setting(
    "Organolead trihalide perovskite materials exhibit excellent optical properties that are tunable by managing chemical compositions [@Jeon2014]."
)

perovskite_ambipolar_transport = setting(
    "Organolead trihalide perovskite materials exhibit ambipolar charge transport [@Jeon2014]."
)

perovskite_long_diffusion_lengths = setting(
    "Organolead trihalide perovskite materials exhibit very long electron-hole diffusion lengths exceeding 1 micrometer [@Jeon2014]."
)

# --- Prior performance benchmarks ---

sequential_deposition_benchmark = claim(
    "When MAPbI3 was loaded on a mesoporous-TiO2 electrode by sequential deposition of PbI2 and methylammonium iodide, a 15.0% power-conversion efficiency was achieved under 1 sun illumination [@Jeon2014; @Burschka2013]."
)

vacuum_deposition_benchmark = claim(
    "A maximum performance of 15.4% efficiency with open-circuit voltage of 1.07 V and short-circuit current density of 21.5 mA cm^-2 was achieved using uniform MAPbI3-xClx planar thin layers deposited by vacuum thermal evaporation without mesoporous TiO2 [@Jeon2014; @Liu2013]."
)

# --- Problem statement ---

spin_coating_problem = claim(
    "Simple spin-coating does not yield a homogeneous perovskite layer having uniform thickness over a large area, despite applying convective spreading flow due to centrifugal force with slowly evaporating solvents [@Jeon2014; @Eperon2014]."
)

uniformity_limitation = claim(
    "The uniformity of perovskite films depends on the thickness of the TiO2 compact layer, and modification of spinning conditions cannot achieve 100% surface coverage [@Jeon2014; @Eperon2014]."
)

# --- Research question ---

research_question = question(
    "How can a fully solution-based process deposit extremely uniform and dense perovskite layers to enable high-efficiency perovskite solar cells?"
)

# --- Proposed solution overview ---

bilayer_architecture = claim(
    "A bilayer architecture comprising key features of both mesoscopic and planar structures was fabricated by a fully solution-based solvent-engineering process [@Jeon2014]."
)

perovskite_composition = claim(
    "The perovskite composition CH3NH3Pb(I1-xBrx)3 (x = 0.1-0.15) was used because substitution of 10-15 mol% Br- for I- in MAPbI3 greatly improved stability in ambient atmosphere while demonstrating similar performance across the compositional range [@Jeon2014; @Noh2013]."
)

mixed_solvent_solution = claim(
    "The use of a mixed solvent of gamma-butyrolactone (GBL) and dimethylsulphoxide (DMSO) followed by toluene drop-casting leads to extremely uniform and dense perovskite layers via a CH3NH3|PbI2-DMSO intermediate phase [@Jeon2014]."
)

certified_efficiency = claim(
    "The solvent-engineering technology enabled a fully solution-processed perovskite solar cell with a certified 16.2% power-conversion efficiency under standard reporting conditions (AM 1.5 G, 100 mW cm^-2) [@Jeon2014]."
)