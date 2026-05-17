"""
motivation.py - Introduction and motivation for 2D perovskite passivation.

This module covers the background and motivation from the paper:
Li et al. "Homogeneous coverage of the low-dimensional perovskite passivation layer
for formamidinium-caesium perovskite solar modules" Nature Energy 2024.
"""

from gaia.lang import claim, setting

# Background on 3D/2D perovskite heterostructures
context_3d2d_heterostructure = setting(
    "Surface passivation of 3D perovskite light-harvesting layers with 2D perovskites "
    "is an effective strategy to boost stability and PCE of PSCs. 2D layers offer "
    "superior hydrophobicity and thermostability, and can passivate defects at the "
    "3D perovskite surface, reducing interface charge recombination and improving "
    "carrier transport [@Li2024].",
    title="3D/2D heterostructure for PSC passivation",
)

# Challenge: homogeneity of 2D formation
challenge_homogeneity = claim(
    "Few reports address the homogeneity of 2D perovskite capping layer formation, "
    "which is more crucial for large-size perovskite solar modules (PSMs). Poor "
    "coverage and random distribution of 2D phases dominate undesirable energy disorder "
    "at the interface, deteriorating device performance [@Li2024].",
    title="Homogeneity challenge for 2D passivation layers",
)

# n-value definition
n_value_explanation = setting(
    "The variable n represents the number of PbX6^4- layers in the 2D structure, "
    "where X is a halide. Lower n values correspond to shorter emission wavelengths "
    "in PL spectra (450-650 nm range) [@Li2024].",
    title="n-value definition in 2D perovskites",
)

# Ligand chain length effects
ligand_chain_effect = claim(
    "Shorter alkylamine spacers prefer to form higher n-value structures due to ease "
    "of diffusion. Large ligand lengths tend to give rise to 2D structures with smaller "
    "n values. Both generally possess a variety of n-value structures on the 3D "
    "perovskite surface, resulting in uneven distribution of 2D phases [@Li2024].",
    title="Ligand chain length determines n-value distribution",
)

# Halide effects on phase composition
halide_phase_effect = claim(
    "Different halides in 2D perovskite ligands form different halide- or n-value-based "
    "2D phases. For example, neoPABr and neoPAI generate pure n=1 iodide-based 2D "
    "perovskite films, whereas neoPACl induces formation of mixed-phase n=1 and n=2 "
    "2D perovskite capping layers due to strong electronegativity of Cl- [@Li2024].",
    title="Halide composition affects 2D phase distribution",
)

# Problem statement: need for homogeneous phase-pure 2D
problem_phase_separation = claim(
    "The introduced interfacial energy disorder from mixed phases serves as a "
    "recombination channel and deteriorates interfacial charge transport of 3D/2D "
    "perovskite bilayers. To minimize efficiency losses during upscaling of PSMs, "
    "gaining in-depth understanding of 2D structure formation kinetics and "
    "homogenizing the 2D passivation layer are of vital importance [@Li2024].",
    title="Phase separation degrades 3D/2D interface quality",
)

# Prior work on phase-pure 2D
prior_phase_pure_work = claim(
    "Jang et al. reported solid-state in-plane growth of phase-pure n=12D perovskite "
    "(BA2PbI4) on 3D perovskite by carefully controlling formation conditions, "
    "demonstrating efficient and stable 3D/2D PSCs with PCE of 24.8%. Sidhik et al. "
    "tailored solvents for deterministic fabrication of 3D/2D bilayer stacks with specific "
    "n-value BA-based 2D perovskites, enabling uniform n=3 2D capping layer with "
    "superior operational stability of T99 > 2000 hours [@Li2024].",
    title="Prior work on phase-pure 2D perovskite formation",
)

# Research gap
research_gap = claim(
    "It is uncertain whether these techniques satisfy upscaling fabrication of "
    "large-size PSMs and whether they can be applied to other 2D materials, especially "
    "for large-space or long-chain alkylamine ligands that are generally considered more "
    "stable due to inherent hydrophobicity and strong steric hindrance for inhibiting "
    "ions migration [@Li2024].",
    title="Scalability and applicability gap for large-chain ligands",
)

# Research objective
research_objective = claim(
    "This work systematically investigates effects of typical 2D ligands with different "
    "halides on homogeneity of formed 2D perovskite passivation layers. The goal is "
    "to identify and solve the phase separation problem in double-halide alloyed 2D "
    "perovskites with long-chain alkylamine ligands, and develop a universal strategy "
    "for phase-pure n-value 2D perovskite capping layers with homogeneous morphology "
    "compatible with scalable manufacturing [@Li2024].",
    title="Research objective: homogenize 2D passivation for scalability",
)