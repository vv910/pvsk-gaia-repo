"""
s5_strategies.py - Reasoning strategies connecting claims.

This module adds strategies connecting claims to form the paper's reasoning chain.
"""

from gaia.lang import (
    support,
    claim,
)

from .motivation import (
    challenge_homogeneity,
    ligand_chain_effect,
    halide_phase_effect,
    problem_phase_separation,
    research_objective,
)

from .s3_results import (
    phase_separation_pl,
    dax_halide_pl,
    double_halide_phase_sep,
    dft_formation_enthalpy_double,
    dft_formation_enthalpy_triple,
    triple_halide_eliminates_phase_sep,
    fabr_enables_uniform_n2,
    n_value_challenge,
    giwaxs_results,
    dabr_giwaxs,
    fabr_dabr_giwaxs,
    formation_mechanism,
)

from .s4_discussion import (
    afm_morphology,
    kpfm_surface_potential,
    sclc_trap_density,
    operational_stability,
    champion_small_device,
    large_device_efficiency,
    mini_module_efficiency,
)

from .s5_results import (
    scalable_manufacturing,
    module_20x20,
    module_30x30,
    efficiency_scaling,
)

from .s6_conclusion import (
    main_conclusion,
    efficiency_summary,
    stability_summary,
    large_module_summary,
    mechanism_summary,
    scalability_contribution,
)

# Strategy: Phase separation observed in long-chain ligands
strat_phase_separation_observed = support(
    [challenge_homogeneity, ligand_chain_effect],
    phase_separation_pl,
    reason="The homogeneity problem for 2D passivation layers is well-established, and ligand chain length is known to affect n-value distribution, explaining why long-chain ligands show phase separation.",
    prior=0.5,
)

# Strategy: Double-halide causes phase separation
strat_double_halide_phase_sep = support(
    [dax_halide_pl, dft_formation_enthalpy_double],
    double_halide_phase_sep,
    reason="PL shows DAI and DACl have phase separation but DABr does not. DFT confirms double-halide alloys have increased formation enthalpy, explaining thermodynamic driving force for phase separation.",
    prior=0.5,
)

# Strategy: Triple-halide eliminates phase separation
strat_triple_halide_eliminates = support(
    [dft_formation_enthalpy_triple, double_halide_phase_sep],
    triple_halide_eliminates_phase_sep,
    reason="DFT shows triple-halide has decreased formation enthalpy compared to double-halide, explaining why adding Br reduces I-Cl phase separation.",
    prior=0.5,
)

# Strategy: FABr enables uniform n=2 formation
strat_fabr_enables_n2 = support(
    [triple_halide_eliminates_phase_sep, n_value_challenge],
    fabr_enables_uniform_n2,
    reason="Triple-halide eliminates phase separation but multiple n-values still form. FABr incorporation lowers n=2 formation enthalpy preferentially, enabling pure phase formation.",
    prior=0.5,
)

# Strategy: GIWAXS confirms phase-pure n=2
strat_giwaxs_confirms_n2 = support(
    [fabr_enables_uniform_n2, giwaxs_results],
    fabr_dabr_giwaxs,
    reason="The mechanism of FABr facilitating n=2 formation is confirmed by GIWAXS showing pure n=2 structure for DABr/FABr vs mixed n=1/n=2 for DABr alone.",
    prior=0.5,
)

# Strategy: Formation mechanism explains uniform coverage
strat_formation_mechanism = support(
    [fabr_enables_uniform_n2, dabr_giwaxs],
    formation_mechanism,
    reason="FABr reacts with PbI2 and passivates FA vacancies, while DABr provides the 2D cation. Together they break up fragments and strengthen reaction, explaining uniform phase-pure n=2 formation.",
    prior=0.5,
)

# Strategy: Uniform morphology from AFM/KPFM
strat_uniform_morphology = support(
    [formation_mechanism],
    afm_morphology,
    reason="Phase-pure uniform n=2 2D structure produces smoother surface morphology as confirmed by AFM.",
    prior=0.5,
)

# Strategy: Reduced trap density
strat_reduced_trap_density = support(
    [afm_morphology, fabr_enables_uniform_n2],
    sclc_trap_density,
    reason="Smoother morphology and phase-pure n=2 2D layer reduce trap density at the interface, confirmed by SCLC measurements.",
    prior=0.5,
)

# Strategy: Champion efficiency small device
strat_champion_small = support(
    [sclc_trap_density, afm_morphology, fabr_enables_uniform_n2],
    champion_small_device,
    reason="Reduced trap density and improved morphology from phase-pure n=2 2D passivation lead to champion 25.61% efficiency for small devices.",
    prior=0.5,
)

# Strategy: Large device maintains high efficiency
strat_large_device = support(
    [champion_small_device, afm_morphology],
    large_device_efficiency,
    reason="The homogeneous passivation scales to 1.04 cm2 large devices with 24.62% efficiency, demonstrating scalability.",
    prior=0.5,
)

# Strategy: Mini-module efficiency
strat_mini_module = support(
    [large_device_efficiency],
    mini_module_efficiency,
    reason="Scaling to 13.44 cm2 mini-module yields 23.60% efficiency with <5% loss per tenfold area increase.",
    prior=0.5,
)

# Strategy: Operational stability
strat_operational_stability = support(
    [triple_halide_eliminates_phase_sep, fabr_enables_uniform_n2],
    operational_stability,
    reason="Phase-pure n=2 2D layer with lower mixing enthalpy provides structural stability, enabling T80 > 2000 h at MPPT.",
    prior=0.5,
)

# Strategy: Efficiency scaling summary
strat_efficiency_scaling = support(
    [champion_small_device, large_device_efficiency, mini_module_efficiency],
    efficiency_scaling,
    reason="The efficiency progression (25.61% -> 24.62% -> 23.60%) demonstrates less than 5% loss per tenfold magnification.",
    prior=0.5,
)

# Strategy: Large module scalability
strat_large_module = support(
    [efficiency_scaling, scalable_manufacturing],
    module_20x20,
    reason="Slot-die printing compatible with the DABr/FABr approach enables 18.90% efficiency for 20x20 cm modules.",
    prior=0.5,
)

# Strategy: 30x30 cm module
strat_30x30_module = support(
    [module_20x20],
    module_30x30,
    reason="Scaling to 30x30 cm (802 cm2 aperture) maintains 17.59% efficiency, confirming commercial viability.",
    prior=0.5,
)

# Strategy: Main conclusion - FABr/DABr enables homogeneous passivation
strat_main_conclusion = support(
    [fabr_enables_uniform_n2, triple_halide_eliminates_phase_sep, formation_mechanism],
    main_conclusion,
    reason="FABr/DABr post-treatment solves phase separation through triple-halide engineering, preferential n=2 formation, and uniform morphology, enabling effective 2D passivation.",
    prior=0.5,
)

# Strategy: Efficiency summary
strat_efficiency_summary = support(
    [champion_small_device, large_device_efficiency, mini_module_efficiency],
    efficiency_summary,
    reason="Champion efficiencies of 25.61%, 24.62%, 23.60% for small, large, and mini-module demonstrate scalability.",
    prior=0.5,
)

# Strategy: Stability summary
strat_stability_summary = support(
    [operational_stability],
    stability_summary,
    reason="T80 > 2000 h at MPPT confirms excellent operational stability for mini-modules.",
    prior=0.5,
)

# Strategy: Large module summary
strat_large_module_summary = support(
    [module_20x20, module_30x30],
    large_module_summary,
    reason="20x20 cm (18.90%, 310 cm2) and 30x30 cm (17.59%, 802 cm2) modules demonstrate commercial scalability.",
    prior=0.5,
)

# Strategy: Mechanism summary
strat_mechanism_summary = support(
    [dft_formation_enthalpy_triple, formation_mechanism, fabr_enables_uniform_n2],
    mechanism_summary,
    reason="Lower formation enthalpy of triple-halide n=2, FABr passivation of vacancies, and strengthened reaction with PbX2 explain homogeneous phase-pure n=2 formation.",
    prior=0.5,
)

# Strategy: Scalability contribution
strat_scalability_contribution = support(
    [scalable_manufacturing, module_20x20, module_30x30],
    scalability_contribution,
    reason="Slot-die printing compatibility demonstrates the strategy is manufacturing-ready.",
    prior=0.5,
)