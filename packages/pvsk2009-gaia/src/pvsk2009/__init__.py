"""
PVSK 2009 - Kojima et al. (2009)
Organometal Halide Perovskites as Visible-Light Sensitizers for Photovoltaic Cells

This package formalizes the first report of organometal halide perovskite
sensitizers for photovoltaic cells, demonstrating 3.81% efficiency with
CH3NH3PbI3 and 0.96 V open-circuit voltage with CH3NH3PbBr3.
"""

from .motivation import (
    dye_sensitized_tiO2_established,
    organic_sensitizer_limitations,
    quantum_dot_approach,
    perovskite_optical_properties,
    perovskite_sensitization_demonstrated,
    iodide_cell_efficiency,
    bromide_cell_high_voltage,
    research_question,
)

from .s2_methods import (
    fto_substrate_preparation,
    tiO2_mesoporous_film,
    tiO2_thickness_optimization,
    bromide_precursor_synthesis,
    iodide_precursor_synthesis,
    perovskite_self_organization,
    bromide_cubic_structure,
    iodide_tetragonal_structure,
    bromide_particle_size,
    cell_construction,
    bromide_electrolyte,
    iodide_electrolyte,
    measurement_setup,
)

from .s3_results import (
    bromide_ipce_spectrum,
    iodide_ipce_spectrum,
    photocurrent_generation,
    bromide_iv_characteristics,
    iodide_iv_characteristics,
    jsc_comparison,
    voc_comparison,
    ru_complex_voc_comparison,
    efficiency_comparison,
    pv_performance_table,
    efficient_sensitization_confirmation,
    durability_observation,
)

from .s4_discussion import (
    valence_band_levels,
    halide_oxidation_potentials,
    conduction_band_levels,
    bromide_conduction_band_higher,
    bromide_redox_coupling,
    quantum_confinement_assessment,
    bathochromic_shift_explanation,
    charge_separation_mechanism,
    conclusion_perovskite_sensitization,
    conclusion_high_voltage,
    future_directions,
    efficiency_milestone,
)

from . import s5_strategies

__all__ = [
    # From motivation
    "dye_sensitized_tiO2_established",
    "organic_sensitizer_limitations",
    "quantum_dot_approach",
    "perovskite_optical_properties",
    "perovskite_sensitization_demonstrated",
    "iodide_cell_efficiency",
    "bromide_cell_high_voltage",
    "research_question",
    # From s2_methods
    "fto_substrate_preparation",
    "tiO2_mesoporous_film",
    "tiO2_thickness_optimization",
    "bromide_precursor_synthesis",
    "iodide_precursor_synthesis",
    "perovskite_self_organization",
    "bromide_cubic_structure",
    "iodide_tetragonal_structure",
    "bromide_particle_size",
    "cell_construction",
    "bromide_electrolyte",
    "iodide_electrolyte",
    "measurement_setup",
    # From s3_results
    "bromide_ipce_spectrum",
    "iodide_ipce_spectrum",
    "photocurrent_generation",
    "bromide_iv_characteristics",
    "iodide_iv_characteristics",
    "jsc_comparison",
    "voc_comparison",
    "ru_complex_voc_comparison",
    "efficiency_comparison",
    "pv_performance_table",
    "efficient_sensitization_confirmation",
    "durability_observation",
    # From s4_discussion
    "valence_band_levels",
    "halide_oxidation_potentials",
    "conduction_band_levels",
    "bromide_conduction_band_higher",
    "bromide_redox_coupling",
    "quantum_confinement_assessment",
    "bathochromic_shift_explanation",
    "charge_separation_mechanism",
    "conclusion_perovskite_sensitization",
    "conclusion_high_voltage",
    "future_directions",
    "efficiency_milestone",
]