"""
Burschka2013: Sequential deposition as a route to high-performance perovskite-sensitized solar cells.

This module captures the introduction and motivation from the paper.
"""

from gaia.lang import claim, setting

# Background context
perovskite_definition = setting(
    "Solution-processable organic-inorganic hybrid perovskites have the general formula "
    "CH3NH3PbX3 where X = Cl, Br, or I, and have attracted attention as light-harvesting "
    "materials for mesoscopic solar cells [@Burschka2013].",
    title="Perovskite material definition",
)

prior_work_limitation = claim(
    "The single-step deposition of perovskite pigment onto mesoporous metal oxide films using "
    "a mixture of PbX2 and CH3NH3X in a common solvent produces large morphological variations, "
    "resulting in a wide spread of photovoltaic performance in the resulting devices [@Burschka2013].",
    title="Single-step deposition produces morphological variability",
)

sequential_deposition_introduced = claim(
    "A sequential deposition method is introduced for the formation of the perovskite pigment "
    "within the porous metal oxide film: PbI2 is first introduced from solution into a nanoporous "
    "titanium dioxide film and subsequently transformed into the perovskite by exposing it to a "
    "solution of CH3NH3I [@Burschka2013].",
    title="Sequential deposition method introduced",
)

control_improvement = claim(
    "The sequential deposition method permits much better control over perovskite morphology "
    "than the previously employed single-step route [@Burschka2013].",
    title="Sequential method improves morphology control",
)

efficiency_achieved = claim(
    "Using the sequential deposition technique for solid-state mesoscopic solar cells, a power "
    "conversion efficiency of approximately 15% is achieved under standard AM1.5G test conditions "
    "[@Burschka2013].",
    title="15% efficiency achieved with sequential deposition",
)

reproducibility_improvement = claim(
    "The sequential deposition method greatly increases the reproducibility of photovoltaic "
    "performance compared to single-step deposition [@Burschka2013].",
    title="Sequential method improves reproducibility",
)

__all__ = [
    "perovskite_definition",
    "prior_work_limitation",
    "sequential_deposition_introduced",
    "control_improvement",
    "efficiency_achieved",
    "reproducibility_improvement",
]