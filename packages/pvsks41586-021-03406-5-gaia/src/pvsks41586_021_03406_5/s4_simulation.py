"""
s4_simulation.py - Molecular dynamics simulation results.

This module covers the computational findings on how HCOO- anions
coordinate in solution and passivate iodide vacancies at FAPbI3 surfaces.
"""

from gaia.lang import (
    claim, setting, question, support, infer,
    contradiction, complement, equivalence, disjunction,
)

# =============================================================================
# MD Simulation Results - Solution Phase
# =============================================================================

md_solution_coordination = claim(
    "Ab initio molecular dynamics simulations of a homogeneous mixture of Pb2+, I-, HCOO-, "
    "and FA+ ions in the precursor solution show that HCOO- anions coordinate strongly with "
    "Pb2+ cations. This strong coordination helps slow the crystal growth process, resulting "
    "in larger stacked grains of the perovskite film [@Jeong2021].",
    title="MD simulations show HCOO- coordinates strongly with Pb2+ in solution",
)

in_situ_crystal_growth = claim(
    "In situ images of perovskite films without annealing confirm slower color change from "
    "brown to black for the target (2% FAHCOO) compared to the reference film, validating "
    "the MD prediction of slower crystal growth with formate addition [@Jeong2021].",
    title="In situ observations confirm slower crystal growth with formate",
)

# =============================================================================
# MD Simulation Results - Surface Passivation
# =============================================================================

md_surface_passivation = claim(
    "MD simulations of the α-FAPbI3 perovskite slab show that surface iodide vacancies can "
    "be replaced by formate anions. HCOO- anions form a hydrogen-bonded network with FA+ "
    "ions at the surface, in agreement with hydrogen bonding observed in FAHCOO crystal "
    "structures. HCOO- also forms a bonding network on the Pb2+ ion-terminated surface "
    "due to their strong affinity towards lead [@Jeong2021].",
    title="MD simulations show HCOO- forms hydrogen-bonded network at surface",
)

md_passivation_structure = claim(
    "Calculated structure illustrates an HCOO- anion passivating an I- vacancy at the "
    "FAPbI3 surface: Pb2+ (yellow), I- (pink), O (red), C (green), N (blue), H (white). "
    "This passivation eliminates the most deleterious defect in halide perovskites "
    "[@Jeong2021].",
    title="Calculated passivation structure at I- vacancy",
    metadata={"figure": "artifacts/images/9573edf2df8c28e32bdbb5c9b6dfdc9e124034773fa8cc2c7487383997feb64e.jpg",
               "caption": "Fig. 2c | Calculated structure showing HCOO- passivating I- vacancy at FAPbI3 surface"},
)

# =============================================================================
# DFT Binding Energy Results
# =============================================================================

binding_affinity_comparison = claim(
    "DFT calculations of relative binding affinities of different anions (HCOO-, Cl-, Br-, "
    "I-, BF4-) to I- vacancies at the FAPbI3 surface show that HCOO- has the highest binding "
    "energy to I- vacant sites. This explains why formate is the most effective at eliminating "
    "this prevalent and deleterious lattice defect [@Jeong2021].",
    title="HCOO- has highest binding affinity to I- vacancy",
    metadata={"figure": "artifacts/images/0e455b55126a92f3fc16fbeaa383e16a68bede5901604730eef40ec72a8f1f06.jpg",
               "caption": "Fig. 2d | Relative interaction strengths of different anions with I- vacancy at surface"},
)

formate_highest_affinity = claim(
    "Among all halide and pseudo-halide anions tested (Cl-, Br-, I-, BF4-), HCOO- shows the "
    "highest binding energy to iodide vacancy sites at the FAPbI3 surface, making it the best "
    "candidate for eliminating the most abundant and deleterious lattice defects in halide "
    "perovskite films [@Jeong2021].",
    title="Formate has highest binding energy among all anions",
)

fa_cation_binding = claim(
    "DFT calculations of bonding energies of FA+ cations at the interface with different "
    "anions show that FA+ forms stronger bonds with HCOO- than with other anions. This "
    "further supports the stability of the passivation structure formed by HCOO- at "
    "iodide vacancy sites [@Jeong2021].",
    title="FA+ forms stronger bonds with HCOO- than other anions",
)

# =============================================================================
# Mechanism Summary
# =============================================================================

defect_elimination_mechanism = claim(
    "The HCOO- anion acts by eliminating anion-vacancy defects through its small size "
    "(fitting into I- vacancy), highest binding affinity among all anions, and ability to "
    "form hydrogen-bonded networks with FA+ at the surface. This results in markedly "
    "reduced trap-mediated non-radiative recombination validated by EQE_EL, time-resolved "
    "PL, ideality factor, and SCLC measurements [@Jeong2021].",
    title="HCOO- eliminates anion-vacancy defects through multiple mechanisms",
)

# =============================================================================
# Strategies
# =============================================================================

strat_md_solution_supports_slower_growth = support(
    [md_solution_coordination, in_situ_crystal_growth],
    claim("Formate coordination slows perovskite crystal growth"),
    reason="MD simulations show HCOO- coordinates strongly with Pb2+ in solution, which "
    "slows crystal growth. In situ observations confirm this: the target film shows slower "
    "color change (brown to black) during processing compared to reference, leading to larger "
    "grain size observed in SEM [@Jeong2021].",
    prior=0.5,
)

strat_md_surface_supports_passivation = support(
    [md_surface_passivation, md_passivation_structure, binding_affinity_comparison,
     formate_highest_affinity, fa_cation_binding],
    claim("HCOO- passivates iodide vacancies at FAPbI3 surfaces"),
    reason="MD simulations show HCOO- forms hydrogen-bonded network with FA+ at the surface "
    "and bonds strongly to Pb2+. DFT shows HCOO- has the highest binding affinity to I- vacancy "
    "among all anions tested (Cl-, Br-, I-, BF4-). The calculated passivation structure shows "
    "HCOO- fills the I- vacancy. FA+ also binds more strongly to HCOO- than to other anions, "
    "stabilizing the passivation interface [@Jeong2021].",
    prior=0.5,
)

strat_binding_affinity_validates_formate = support(
    [formate_highest_affinity, fa_cation_binding],
    defect_elimination_mechanism,
    reason="The highest binding affinity of HCOO- for I- vacancies (vs Cl-, Br-, I-, BF4-) "
    "explains why formate is uniquely effective at eliminating iodide vacancies, the most "
    "deleterious defects in halide perovskites. The additional FA+ binding preference further "
    "stabilizes the passivation structure. This mechanism accounts for the observed improvements "
    "in defect passivation, crystallinity, and stability [@Jeong2021].",
    prior=0.5,
)

__all__ = [
    "md_solution_coordination",
    "in_situ_crystal_growth",
    "md_surface_passivation",
    "md_passivation_structure",
    "binding_affinity_comparison",
    "formate_highest_affinity",
    "fa_cation_binding",
    "defect_elimination_mechanism",
    "strat_md_solution_supports_slower_growth",
    "strat_md_surface_supports_passivation",
    "strat_binding_affinity_validates_formate",
]