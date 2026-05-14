"""
Pass 2: Connect - Reasoning strategies for pvsk2009.

This module adds inference strategies connecting knowledge nodes
to build the reasoning graph for the Kojima et al. (2009) paper.
"""

from gaia.lang import (
    claim,
    setting,
    support,
    deduction,
    compare,
)

# Import all claims and settings from the package
from . import (
    # From motivation
    dye_sensitized_tiO2_established,
    organic_sensitizer_limitations,
    quantum_dot_approach,
    perovskite_optical_properties,
    perovskite_sensitization_demonstrated,
    iodide_cell_efficiency,
    bromide_cell_high_voltage,
    research_question,
    # From s2_methods
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
    # From s3_results
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
    # From s4_discussion
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

# ===== Supporting evidence for perovskite sensitization =====

# Perovskite sensitization demonstrated -> iodide cell efficiency
strat_efficiency_from_sensitization = support(
    [perovskite_sensitization_demonstrated],
    iodide_cell_efficiency,
    reason="The demonstrated perovskite sensitization of TiO2 directly produces the "
           "photovoltaic effect; the 3.81% efficiency is the measured outcome of this "
           "sensitization under AM 1.5 illumination [@pvsk2009].",
    prior=0.5,
)

# Perovskite sensitization demonstrated -> bromide cell high voltage
strat_voltage_from_sensitization = support(
    [perovskite_sensitization_demonstrated],
    bromide_cell_high_voltage,
    reason="The efficient sensitization enables high photovoltage; the bromide perovskite's "
           "higher conduction band (3.36 eV vs 4.0 eV for iodide) combined with the bromide "
           "redox couple produces the notably high Voc of 0.96 V [@pvsk2009].",
    prior=0.5,
)

# ===== Energy band alignment supports charge separation =====

strat_charge_sep_from_bands = support(
    [valence_band_levels, conduction_band_levels],
    charge_separation_mechanism,
    reason="The valence band (5.38-5.44 eV) being more positive than halide oxidation "
           "potentials (4.5-5.6 eV), and conduction bands (3.36-4.0 eV) allowing electron "
           "injection to TiO2 (4.0 eV), establishes the energy alignment for efficient "
           "charge separation [@pvsk2009].",
    prior=0.5,
)

# ===== Results supporting performance comparisons =====

strat_jsc_from_ipce = support(
    [bromide_ipce_spectrum, iodide_ipce_spectrum],
    jsc_comparison,
    reason="The IPCE spectra show that iodide has extended spectral response to 800 nm "
           "with 45% max, while bromide has 65% max but limited to 600 nm. The integrated "
           "IPCE area for iodide yields Jsc twice that of bromide (11.0 vs 5.57 mA/cm2) "
           "[@pvsk2009].",
    prior=0.5,
)

strat_voc_comparison_from_data = support(
    [bromide_iv_characteristics, iodide_iv_characteristics],
    voc_comparison,
    reason="The measured Voc values (0.96 V for bromide, 0.61 V for iodide) reflect the "
           "different conduction band positions: bromide's higher conduction band (3.36 eV) "
           "interacts favorably with TiO2 surface levels to produce higher photovoltage "
           "[@pvsk2009].",
    prior=0.5,
)

strat_ru_comparison = support(
    [voc_comparison],
    ru_complex_voc_comparison,
    reason="The CH3NH3PbBr3 Voc of 0.96 V exceeds the maximal Ru complex Voc range "
           "(0.86-0.93 V) because the bromide redox couple has a more positive potential "
           "than iodide, expanding the photovoltage range beyond what Ru complexes achieve "
           "[@pvsk2009].",
    prior=0.5,
)

strat_table_from_iv = support(
    [bromide_iv_characteristics, iodide_iv_characteristics],
    pv_performance_table,
    reason="The photovoltaic performance table directly summarizes the I-V characteristics "
           "measured for both cells under standard test conditions (100 mW/cm2 AM 1.5) "
           "[@pvsk2009].",
    prior=0.5,
)

strat_efficient_sens_from_ipce = support(
    [bromide_ipce_spectrum, iodide_ipce_spectrum],
    efficient_sensitization_confirmation,
    reason="High IPCE values (65% for bromide, 45% for iodide) directly demonstrate that "
           "TiO2 is efficiently sensitized - incident photons are effectively converted to "
           "photocurrent, confirming the perovskite sensitization function [@pvsk2009].",
    prior=0.5,
)

# ===== Crystal structure supports band levels =====

strat_bands_from_structure = support(
    [bromide_cubic_structure, iodide_tetragonal_structure],
    conduction_band_levels,
    reason="The different crystal structures (cubic for bromide a=5.9A, tetragonal for "
           "iodide a=8.855A, c=12.659A) result in different band gaps, leading to "
           "conduction bands at 3.36 eV (bromide) and 4.0 eV (iodide) calculated from "
           "optical absorption edges [@pvsk2009].",
    prior=0.5,
)

strat_bromide_higher_band = support(
    [bromide_cubic_structure, iodide_tetragonal_structure, conduction_band_levels],
    bromide_conduction_band_higher,
    reason="The cubic bromide perovskite (a=5.9A) has a conduction band at 3.36 eV, "
           "while the tetragonal iodide perovskite (a=8.855A, c=12.659A) has a conduction "
           "band at 4.0 eV. The difference in crystal structure and lattice parameters "
           "directly determines the relative band positions, with bromide being higher "
           "[@pvsk2009].",
    prior=0.5,
)

strat_bromide_redox = support(
    [bromide_conduction_band_higher],
    bromide_redox_coupling,
    reason="The high Voc (0.96 V) with CH3NH3PbBr3 arises because bromide (Br2/Br-) has "
           "a more positive oxidation potential (5.1-5.6 eV) compared to iodide (I2/I-, "
           "4.5-5.0 eV), expanding the achievable photovoltage range when coupled with "
           "the perovskite bromide [@pvsk2009].",
    prior=0.5,
)

strat_bathochromic = support(
    [bromide_ipce_spectrum, iodide_ipce_spectrum],
    bathochromic_shift_explanation,
    reason="The IPCE spectra show a bathochromic (red) shift from bromide (sharp rise at "
           "570 nm, cutoff 600 nm) to iodide (extended to 800 nm), reflecting the narrower "
           "bandgap of the iodide compound. This shift is analogous to silver halide ionic "
           "crystals which also show halogen-dependent bandgap tuning [@pvsk2009].",
    prior=0.5,
)

strat_efficiency_vs_qdots = support(
    [iodide_iv_characteristics, iodide_ipce_spectrum],
    efficiency_comparison,
    reason="The CH3NH3PbI3 cell achieved 3.81% efficiency, significantly exceeding prior "
           "results with nonorganic sensitizers and quantum dots (CdS, CdSe, PbS, InP, "
           "InAs) which suffered from light utilization and charge separation losses at "
           "the semiconductor-sensitizer interface [@pvsk2009].",
    prior=0.5,
)

strat_durability = support(
    [photocurrent_generation],
    durability_observation,
    reason="Photocurrent decay was observed during continuous irradiation of open cells "
           "exposed to air, indicating degradation mechanisms that are not yet characterized "
           "[@pvsk2009].",
    prior=0.5,
)

strat_efficiency_milestone = support(
    [ iodide_cell_efficiency, perovskite_sensitization_demonstrated,
      efficiency_comparison, bromide_cell_high_voltage ],
    efficiency_milestone,
    reason="The 3.81% efficiency with CH3NH3PbI3, together with the 0.96 V Voc from "
           "CH3NH3PbBr3 and the significant improvement over quantum dot sensitizers, "
           "establishes organometal halide perovskites as a new class of visible-light "
           "sensitizers for photovoltaic cells [@pvsk2009].",
    prior=0.5,
)

strat_conclusion_sensitization = support(
    [perovskite_sensitization_demonstrated, efficient_sensitization_confirmation,
     iodide_cell_efficiency],
    conclusion_perovskite_sensitization,
    reason="The evidence that perovskite compounds (CH3NH3PbX3) efficiently sensitize "
           "TiO2 for visible-light conversion, with measured IPCE up to 65% and "
           "photovoltaic efficiency of 3.81%, establishes this as a significant advance "
           "in the field [@pvsk2009].",
    prior=0.5,
)

strat_conclusion_voltage = support(
    [bromide_cell_high_voltage, ru_complex_voc_comparison],
    conclusion_high_voltage,
    reason="The achievement of 0.96 V Voc with CH3NH3PbBr3, exceeding the maximal Voc "
           "of 0.86-0.93 V achieved with Ru complex sensitizers, demonstrates that "
           "perovskite materials are especially promising for high photovoltage applications "
           "[@pvsk2009].",
    prior=0.5,
)

strat_quantum_confinement = support(
    [bromide_ipce_spectrum, iodide_ipce_spectrum],
    quantum_confinement_assessment,
    reason="The IPCE spectra show band-edge characteristic behavior (sharp rise at "
           "absorption edge) rather than strongly shifted excitonic features that would "
           "indicate dominant quantum confinement in the 2-3 nm particles [@pvsk2009].",
    prior=0.5,
)