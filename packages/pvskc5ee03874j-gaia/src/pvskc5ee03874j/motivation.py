"""
Motivation section: Introduction and Broader Context of the paper.

This module covers:
- Background on perovskite solar cells and their ABX3 structure
- Historical efficiency progression
- Issues with pure perovskite compounds (MAPbI3, FAPbI3, CsPbI3)
- The triple cation Cs/MA/FA strategy as a solution
"""

from gaia.lang import claim, setting

# Historical efficiency progression of perovskite solar cells
efficiency_progression = claim(
    "Perovskite solar cells have achieved power conversion efficiencies (PCE) leaping from 3.8% in 2009 to the world record of 22.1% [@Saliba2016].",
    title="Perovskite solar cell efficiency progression",
)

# ABX3 structure definition
abx3_structure = setting(
    "An organic-inorganic perovskite material has an ABX3 structure comprising: "
    "A = organic cation (methylammonium MA CH3NH3+ or formamidinium FA CH3(NH2)2+), "
    "B = divalent metal (Pb2+, Sn2+, or Ge2+), and "
    "X = halide anion (Cl-, Br-, I-, BF4-, PF6-, or SCN-) [@Saliba2016]."
)

# Exceptional material properties
exceptional_absorption = claim(
    "Perovskite solar cells exhibit remarkably high absorption over the visible spectrum [@Saliba2016].",
    title="High absorption over visible spectrum",
)

low_exciton_binding = claim(
    "Perovskite solar cells have low exciton binding energy [@Saliba2016].",
    title="Low exciton binding energy",
)

long_diffusion_lengths = claim(
    "Perovskite solar cells have charge carrier diffusion lengths in the micrometer range [@Saliba2016].",
    title="Charge carrier diffusion lengths in micrometer range",
)

tuneable_bandgap = claim(
    "Perovskite solar cells have a tuneable band gap from 1.1 to 2.3 eV by interchanging cations, metals, and halides [@Saliba2016].",
    title="Tuneable band gap 1.1 to 2.3 eV",
)

# Issues with pure perovskite compounds
mapbi3_never_exceeded_20percent = claim(
    "MAPbI3 perovskites have never reached efficiencies larger than 20% despite numerous attempts since the early days of research [@Saliba2016].",
    title="MAPbI3 never exceeded 20% efficiency",
)

mapbi3_phase_transition = claim(
    "MAPbI3 perovskites exhibit structural phase transition at 55 degrees Celsius and degrade upon contact with moisture and under thermal stress [@Saliba2016].",
    title="MAPbI3 phase transition and stability issues",
)

mapbi3_halide_segregation = claim(
    "MAPbI3 mixed halide perovskites exhibit light-induced trap-state formation and halide segregation [@Saliba2016].",
    title="MAPbI3 halide segregation issues",
)

fapi3_instability = claim(
    "Pure FAPbI3 lacks structural stability at room temperature, crystallizing into either a photoinactive hexagonal yellow phase or a photoactive black phase that is sensitive to solvents or humidity [@Saliba2016].",
    title="FAPbI3 structural instability",
)

cspbi3_bandgap = claim(
    "The perovskite phase of CsPbI3 has a band gap of 1.73 eV, suitable for PV applications, but crystallizes in a photoinactive yellow phase at room temperature with the photoactive black phase only stable above 300 degrees Celsius [@Saliba2016].",
    title="CsPbI3 band gap and stability constraints",
)

cspbi3_thermal_stability = claim(
    "Purely inorganic cesium lead trihalide perovskites exhibit excellent thermal stability, but CsPbBr3 does not have an ideal band gap for photovoltaics [@Saliba2016].",
    title="CsPbX3 thermal stability but non-optimal band gap",
)

# Mixed cations as design principle
mixed_cations_design_principle = claim(
    "It has become an important design principle to mix cations and halides to achieve perovskite compounds with improved thermal and structural stability [@Saliba2016].",
    title="Mixed cations as design principle for stability",
)

# MA as crystallizer for FA perovskite
ma_crystallizer = claim(
    "MA acts as a 'crystallizer' or stabilizer of the black phase FA perovskite, where a small amount of MA is sufficient to induce preferable crystallization into the photoactive phase [@Saliba2016].",
    title="MA as crystallizer of FA perovskite",
)

yellow_phase_impurities = claim(
    "Even with MA present, it is challenging to obtain FA perovskite with no traces of the yellow phase; these impurities influence crystal growth and morphology, inhibiting efficient charge collection and limiting device performance [@Saliba2016].",
    title="Yellow phase impurities limit performance",
)

# Cesium properties and prior work
cs_ionic_radius = claim(
    "Cesium (Cs) has an ionic radius of 1.81 Angstrom, considerably smaller than MA (2.70 Angstrom) or FA (2.79 Angstrom) [@Saliba2016].",
    title="Cs ionic radius smaller than MA or FA",
)

cs_effectively_promotes_black_phase = claim(
    "Cs is very effective in 'pushing' FA into the beneficial black perovskite phase due to the large size difference between Cs and FA [@Saliba2016].",
    title="Cs promotes black phase formation in FA perovskite",
)

ma_induces_slowly = claim(
    "MA also induces crystallization of FA perovskite but at a much slower rate because MA is only slightly smaller than FA, which still permits a large fraction of the yellow phase to persist [@Saliba2016].",
    title="MA induces FA crystallization slowly",
)

# Triple cation strategy
triple_cation_strategy = claim(
    "The triple Cs/MA/FA cation mixture uses Cs to improve MA/FA perovskite compounds further, where a small amount of Cs is sufficient to effectively suppress yellow phase impurities, permitting more pure, defect-free perovskite films [@Saliba2016].",
    title="Triple cation Cs/MA/FA strategy",
)

triple_cation_versatility = claim(
    "The use of all three cations Cs, MA, and FA provides additional versatility in fine-tuning high quality perovskite films that can yield stabilized PCEs exceeding 21% and approximately 18% after 250 hours under operational conditions [@Saliba2016].",
    title="Triple cation enables high efficiency and stability",
)

triple_cation_robustness = claim(
    "Triple cation perovskite films are thermally more stable and less affected by fluctuating surrounding variables such as temperature, solvent vapors, or heating protocols, which is important for reproducibility in manufacturing [@Saliba2016].",
    title="Triple cation improves robustness to processing variations",
)

cs_suppresses_yellow_phase = claim(
    "Adding Cs to MA/FA mixtures suppresses yellow phase impurities and induces highly uniform perovskite grains extending from the electron to the hole collecting layer, consistent with seed-assisted crystal growth [@Saliba2016].",
    title="Cs suppresses yellow phase and improves grain uniformity",
)

industrialization_relevance = claim(
    "Triple or multiple cation mixtures are a novel compositional strategy on the road to industrialization of perovskite solar cells with better stabilities and repeatable high efficiencies [@Saliba2016].",
    title="Triple cation strategy for industrialization",
)

__all__ = [
    "efficiency_progression",
    "abx3_structure",
    "exceptional_absorption",
    "low_exciton_binding",
    "long_diffusion_lengths",
    "tuneable_bandgap",
    "mapbi3_never_exceeded_20percent",
    "mapbi3_phase_transition",
    "mapbi3_halide_segregation",
    "fapi3_instability",
    "cspbi3_bandgap",
    "cspbi3_thermal_stability",
    "mixed_cations_design_principle",
    "ma_crystallizer",
    "yellow_phase_impurities",
    "cs_ionic_radius",
    "cs_effectively_promotes_black_phase",
    "ma_induces_slowly",
    "triple_cation_strategy",
    "triple_cation_versatility",
    "triple_cation_robustness",
    "cs_suppresses_yellow_phase",
    "industrialization_relevance",
]