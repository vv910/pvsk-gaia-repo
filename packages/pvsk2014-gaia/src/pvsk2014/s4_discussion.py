"""
Section 4 (Discussion) formalization covering:
- Mechanism of uniform perovskite formation
- Role of intermediate phase
- Bilayer architecture advantages
- Summary of key conclusions
"""

from gaia.lang import (
    claim,
    setting,
)

# --- Mechanism of uniform perovskite formation ---

formation_mechanism = claim(
    "The formation mechanism proceeds as follows: (1) initial stage - film composed of MAI and PbI2 dissolved in DMSO/GBL solvent mixture; (2) intermediate stage - film composition concentrated by evaporation of GBL (higher evaporation rate than DMSO); (3) toluene droplet introduction causes immediate freezing of constituents via quick removal of excess DMSO and rapid formation of MAI-PbI2-DMSO phase, leaving a uniform and transparent thin layer; (4) annealing at 100 degrees C converts the flat intermediate phase film into pure crystalline MAPbI3 perovskite layer [@Jeon2014].",
    title="Stepwise formation mechanism of uniform perovskite layer"
)

intermediate_phase_critical = claim(
    "The formation of a stable MAI(Br)-PbI2-DMSO phase via an intercalation process during dropwise application of a non-dissolving solvent (toluene) is a decisive factor in retarding the rapid reaction between MAI(Br) and PbI2(Br)2, which enables the formation of a highly uniform and dense surface [@Jeon2014].",
    title="Intermediate phase formation is decisive for uniform surface"
)

role_of_dmso = claim(
    "DMSO functions as a structure-directing agent that coordinates with Pb2+ to form the MAI-PbI2-DMSO intermediate phase, retarding the rapid reaction between PbI2 and MAI during solvent evaporation; GBL functions purely as a solvent with higher evaporation rate than DMSO during spinning [@Jeon2014].",
    title="DMSO coordinates with Pb2+ to form intermediate phase"
)

role_of_toluene = claim(
    "Toluene, as a non-dissolving solvent miscible with DMSO and GBL, removes excess DMSO and freezes all constituents into a uniform layer during spin-coating, enabling formation of the MAI-PbI2-DMSO intermediate phase [@Jeon2014].",
    title="Toluene removes DMSO and freezes constituents into uniform layer"
)

solid_state_conversion = claim(
    "The perovskite film is extremely uniform and flat because of the solid-state conversion from the uniform and flat intermediate phase film during annealing [@Jeon2014].",
    title="Solid-state conversion preserves uniformity from intermediate phase"
)

# --- Bilayer architecture ---

bilayer_advantages = claim(
    "The bilayer architecture (mesoscopic + planar) is effective for sufficiently absorbing light and collecting charges; the mesoscopic mp-TiO2-perovskite nanocomposite layer provides large interface for charge separation while the pure perovskite upper layer ensures complete light absorption with uniform morphology [@Jeon2014].",
    title="Bilayer architecture combines light absorption and charge collection advantages"
)

mp_tio2_necessity = claim(
    "An optimally thick mp-TiO2 layer (approximately 200 nm) is necessary for efficient charge collection from the perovskite via the large TiO2 interface, eliminating the large discrepancy between forward and reverse scan measurements [@Jeon2014].",
    title="Optimal mp-TiO2 thickness (~200 nm) enables efficient charge collection"
)

# --- Scientific contribution ---

solvent_engineering_contribution = claim(
    "The solvent-engineering technology provides a simple and effective means for realizing high-efficiency and low-cost perovskite-based solar cells via a fully solution-based process [@Jeon2014].",
    title="Solvent engineering enables low-cost high-efficiency perovskite solar cells"
)

intercalation_strategy = claim(
    "These results provide an effective strategy for forming uniform PbI2-based perovskite layers through intercalation, which can lead to more efficient and cost-effective inorganic-organic hybrid heterojunction solar cells [@Jeon2014].",
    title="Intercalation strategy enables uniform PbI2-based perovskite layers"
)

key_achievement = claim(
    "The key achievement is the demonstration that a fully solution-processed perovskite solar cell can achieve certified 16.2% PCE under standard reporting conditions (AM 1.5 G, 100 mW cm^-2) through solvent-engineering technology without vacuum processing or high-temperature annealing [@Jeon2014].",
    title="Certified 16.2% PCE achieved by fully solution-based process"
)