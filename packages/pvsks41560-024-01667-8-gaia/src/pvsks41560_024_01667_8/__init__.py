"""
pvsks41560_024_01667_8 - Gaia knowledge package for homogeneous 2D perovskite passivation.

This package formalizes the paper:
Li et al. "Homogeneous coverage of the low-dimensional perovskite passivation layer
for formamidinium-caesium perovskite solar modules" Nature Energy 2024.

The package covers:
- Motivation: 3D/2D heterostructure for PSC passivation and homogeneity challenges
- Methods: Perovskite preparation, post-treatment, and characterization techniques
- Results: Phase separation identification, triple-halide solution, n=2 formation
- Discussion: Defect passivation, photovoltaic performance, stability
- Scalability: Slot-die printed large-area modules
- Conclusion: FABr/DABr enables homogeneous phase-pure 2D passivation
"""

from gaia.lang import claim, setting, support, contradiction

# Exported conclusions (core scientific contributions)
from .s6_conclusion import (
    main_conclusion,
    efficiency_summary,
    stability_summary,
    large_module_summary,
    mechanism_summary,
    scalability_contribution,
    impact_statement,
)

from .s4_discussion import (
    champion_small_device,
    large_device_efficiency,
    mini_module_efficiency,
    operational_stability,
)

from .s3_results import (
    fabr_enables_uniform_n2,
    triple_halide_eliminates_phase_sep,
)

from .s5_results import (
    module_20x20,
    module_30x30,
)

from . import s5_strategies

__all__ = [
    # Main conclusion
    "main_conclusion",
    "efficiency_summary",
    "stability_summary",
    "large_module_summary",
    "mechanism_summary",
    "scalability_contribution",
    "impact_statement",
    # Key performance results
    "champion_small_device",
    "large_device_efficiency",
    "mini_module_efficiency",
    "operational_stability",
    # Key mechanism findings
    "fabr_enables_uniform_n2",
    "triple_halide_eliminates_phase_sep",
    # Large area modules
    "module_20x20",
    "module_30x30",
]