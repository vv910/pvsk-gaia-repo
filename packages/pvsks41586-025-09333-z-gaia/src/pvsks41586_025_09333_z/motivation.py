"""
Perovskite/silicon tandem solar cell with asymmetric self-assembled monolayer HTL201.

This module covers the introduction and motivation of the paper.
"""

from gaia.lang import (
    claim,
    setting,
    question,
)

# Background on perovskite/silicon TSCs
perovskite_silicon_tscs_introduced = claim(
    "Perovskite/silicon tandem solar cells (TSCs) have become a research focus owing to "
    "their superior optoelectronic properties, which have enabled them to go beyond the "
    "efficiency limit of single-junction cells.",
    title="Perovskite/silicon TSCs intro",
)

single_junction_plateau = claim(
    "The efficiency of single-junction solar cells has plateaued, whereas TSCs continue "
    "to show significant growth.",
    title="Single-junction efficiency plateau",
)

voc_loss_problem = claim(
    "The open-circuit voltage (Voc) loss in wide-bandgap perovskite solar cells tends to "
    "increase sharply with increasing bandgap, mainly owing to trap-assisted non-radiative recombination.",
    title="Voc loss problem in wide-bandgap perovskite",
)

sam_advantages = claim(
    "Self-assembled monolayers (SAMs) are highly transparent, dopant-free, easy to process, "
    "low-cost and scalable, making them attractive as hole-selective layers for high-efficiency "
    "single-junction cells and TSCs.",
    title="SAM advantages",
)

existing_sams_limitation = claim(
    "The adsorption behaviour of SAMs on transparent conductive oxide (TCO) varies depending "
    "on their chemical structures, which influences the deposition of the perovskite layer.",
    title="Existing SAMs have variable adsorption behavior",
)

research_objective = claim(
    "Developing SAMs that can form full coverage on TCO, as well as achieving a favourable "
    "energy level, is essential for achieving high-efficiency perovskite/silicon TSCs.",
    title="Research objective for new SAMs",
)

htl201_introduced = claim(
    "An asymmetric SAM named HTL201 was developed through rational molecular design. "
    "HTL201 features spacers and anchoring phosphonic acid groups flanking the phenyl ring "
    "of the carbazole core, serving as a hole-selective layer in perovskite/silicon TSCs.",
    title="HTL201 asymmetric SAM introduced",
)

htl201_design_features = claim(
    "HTL201 features an anchoring group and a spacer flanking a carbazole core, with the "
    "vertical configuration minimizing steric hindrance and enhancing interaction with the "
    "TCO recombination layer.",
    title="HTL201 molecular design features",
)

htl201_outcome = claim(
    "The favourable energy-level alignment between the perovskite and HTL201 facilitates "
    "efficient hole extraction and reduces interfacial non-radiative recombination. "
    "Effective defect passivation at the buried interface enhances the quasi-fermi-level "
    "splitting (QFLS) of the perovskite layer, leading to a Voc of nearly 2V for TSCs.",
    title="HTL201 enables near 2V Voc",
)

certified_pce_result = claim(
    "The perovskite/silicon TSCs achieved a certified power conversion efficiency (PCE) of "
    "34.58% with an area of 1.004 cm^2.",
    title="Certified PCE of 34.58%",
    metadata={"source_figure": "artifacts/full.md", "caption": "Fig. 2i | Certified I-V curve from European Solar Test Installation"},
)

__all__ = [
    "perovskite_silicon_tscs_introduced",
    "single_junction_plateau",
    "voc_loss_problem",
    "sam_advantages",
    "existing_sams_limitation",
    "research_objective",
    "htl201_introduced",
    "htl201_design_features",
    "htl201_outcome",
    "certified_pce_result",
]