"""
Reasoning strategies for the PVSK 2017 paper formalization.

This module contains the reasoning strategies connecting knowledge nodes
to build the reasoning graph for the 2D/3D interface engineering paper.

Pass 2: Initial draft strategies (generic infer)
Pass 4: Refined to specific strategy types
"""

from gaia.lang import (
    claim, setting, support, infer, compare, abduction,
    contradiction, complement, equivalence, composite,
    extrapolation, induction
)

# =============================================================================
# CLAIM REFERENCES - Import all claims to use in strategies
# =============================================================================

from .motivation import (
    perovskite_pce_record, instability_barrier,
    perovskite_degradation_mechanisms, stability_limiting_factors,
    two_d_perovskite_stability, research_objective, key_innovation
)

from .s2_methods import (
    avai_synthesis, two_d_three_d_composite_preparation,
    absorption_spectroscopy, raman_spectroscopy, xrd_method,
    steady_state_pl, pl_excitation_selectivity,
    dft_methodology, interface_model
)

from .s3_results import (
    two_d_absorption, two_d_raman_modes, two_d_xrd_pattern,
    two_d_three_d_absorption, two_d_three_d_raman, two_d_three_d_xrd,
    phase_structure_conclusion,
    pl_oxide_side, pl_phase_separation, pl_730nm_fast_decay,
    oxide_templating_role, cb_upshift_2d_3d, cb_alignment_favorable,
    graded_structure_dft
)

from .s4_discussion import (
    spiro_omeTAD_architecture, htm_free_architecture,
    spiro_cell_efficiency, spiro_cell_stability,
    htm_free_cell_performance, module_performance,
    module_stability_test, hysteresis_observation,
    module_gff, reproducibility, one_year_stability_record,
    upscale_potential
)

# =============================================================================
# PASS 2 & 4: REASONING STRATEGIES - Connect premises to conclusions
# Only claims can be premises; settings are referenced in reason text
# =============================================================================

# --- Core Problem Identification ---
strat_instability_supports_motivation = support(
    [perovskite_pce_record, instability_barrier],
    research_objective,
    reason="The impressive 22%+ efficiency of perovskite solar cells (@perovskite_pce_record) cannot be commercially deployed due to poor stability under operation (@instability_barrier), creating the need for the 2D/3D interface engineering solution (@research_objective).",
    prior=0.9
)

strat_degradation_supports_barrier = support(
    [perovskite_degradation_mechanisms, stability_limiting_factors],
    instability_barrier,
    reason="The moisture-driven hydrolysis degradation (@perovskite_degradation_mechanisms) combined with HTM layer instability (@stability_limiting_factors) together explain why perovskite cells fail market stability requirements.",
    prior=0.9
)

strat_2d_stability_supports_solution = support(
    [two_d_perovskite_stability],
    research_objective,
    reason="The superior water resistance and stability of 2D perovskites (@two_d_perovskite_stability) provides the foundation for the 2D/3D interface engineering concept, combining 2D stability with 3D performance (@research_objective).",
    prior=0.85
)

# --- Material Synthesis Evidence Chain ---
strat_synthesis_enables_characterization = support(
    [avai_synthesis, two_d_three_d_composite_preparation],
    two_d_absorption,
    reason="The AVAI-based 2D perovskite synthesis (@avai_synthesis) and 2D/3D composite preparation (@two_d_three_d_composite_preparation) produce films with characteristic optical properties (absorption edge 450 nm, excitonic peak 425 nm) as shown in Raman (@raman_spectroscopy) and XRD (@xrd_method) characterization.",
    prior=0.9
)

strat_raman_confirms_2d_structure = support(
    [avai_synthesis],
    two_d_raman_modes,
    reason="Raman spectroscopy on the synthesized AVAI perovskite (@avai_synthesis) reveals characteristic peaks at 87, 112, 169 cm-1 (Pb-I modes) and 62, 143 cm-1 (cation rotations), confirming the 2D perovskite structure (@two_d_raman_modes).",
    prior=0.9
)

strat_xrd_confirms_2d_structure = support(
    [avai_synthesis],
    two_d_xrd_pattern,
    reason="X-ray diffraction on the synthesized AVAI perovskite (@avai_synthesis) shows low-angle peaks at 4.7, 4.2, 5.2 degrees characteristic of low-dimensional perovskite structure (@two_d_xrd_pattern).",
    prior=0.9
)

# --- 2D/3D Composite Evidence ---
strat_composite_absorption_proves_mixture = support(
    [two_d_three_d_composite_preparation],
    two_d_three_d_absorption,
    reason="The 2D/3D composite prepared at 3% AVAI (@two_d_three_d_composite_preparation) shows dual absorption features: edge at 760 nm matching 3D perovskite and peak at 430 nm resembling 2D phase (partially red-shifted), confirming formation of mixed 2D/3D composite (@two_d_three_d_absorption).",
    prior=0.9
)

strat_composite_raman_confirms_ordering = support(
    [two_d_three_d_absorption],
    two_d_three_d_raman,
    reason="Raman spectroscopy on the 2D/3D composite (@two_d_three_d_absorption) shows well-defined 2D-like peaks emerging from 3D broad bands, with reduced broadening indicating more ordered crystal rearrangement (@two_d_three_d_raman).",
    prior=0.85
)

strat_composite_xrd_confirms_orientation = support(
    [two_d_three_d_absorption],
    two_d_three_d_xrd,
    reason="XRD on 3% AVAI 2D/3D composite (@two_d_three_d_absorption) shows decreased (002)/(004) peaks and increased (110)/(220) peaks, indicating preferred orientation along <hk0> direction (@two_d_three_d_xrd).",
    prior=0.85
)

# --- Phase Structure Conclusion ---
strat_structural_evidence_supports_phase_model = support(
    [two_d_three_d_absorption, two_d_three_d_raman, two_d_three_d_xrd, pl_oxide_side],
    phase_structure_conclusion,
    reason="Combined evidence from absorption (@two_d_three_d_absorption), Raman (@two_d_three_d_raman), XRD (@two_d_three_d_xrd), and PL from oxide side (@pl_oxide_side) supports the three-component phase model: thin 2D layer at oxide interface, oriented 3D phase, and pure 3D tetragonal phase on top (@phase_structure_conclusion).",
    prior=0.9
)

# --- PL Evidence Chain ---
strat_pl_oxide_side_identifies_2d = support(
    [two_d_three_d_composite_preparation],
    pl_oxide_side,
    reason="Steady-state PL measured from the oxide side of 2D/3D composite (@two_d_three_d_composite_preparation) reveals 450 nm emission matching (HOOC(CH2)4NH3)2PbI4, indicating 2D phase retained at oxide interface (@pl_oxide_side).",
    prior=0.9
)

strat_pl_phase_separation = support(
    [two_d_three_d_composite_preparation, pl_excitation_selectivity],
    pl_phase_separation,
    reason="Selective excitation PL measurements on 2D/3D composite (@two_d_three_d_composite_preparation, @pl_excitation_selectivity) reveal 730 nm emission (1.69 eV) from oxide side versus 760 nm from bulk, indicating distinct wider bandgap phase at interface (@pl_phase_separation).",
    prior=0.9
)

strat_pl_decay_supports_interface_phase = support(
    [pl_phase_separation],
    pl_730nm_fast_decay,
    reason="Time-resolved PL on the 730 nm interface phase (@pl_phase_separation) shows fast τ=2 ns decay (versus long-lived 760 nm decay), resembling low-temperature behavior in oriented 3D perovskite, supporting the conclusion of distinct interface phase (@pl_730nm_fast_decay).",
    prior=0.85
)

strat_oxide_templating_role = support(
    [pl_phase_separation, pl_730nm_fast_decay, two_d_three_d_xrd],
    oxide_templating_role,
    reason="The blue-shifted 730 nm PL (@pl_phase_separation) with fast decay (@pl_730nm_fast_decay) combined with preferred orientation in XRD (@two_d_three_d_xrd) demonstrates that mesoporous oxide scaffolds template the formation of graded 2D/3D interface - depositing on compact glass yields no 730 nm emission (@oxide_templating_role).",
    prior=0.9
)

# --- DFT Simulation Evidence ---
strat_dft_predicts_cb_upshift = support(
    [interface_model],
    cb_upshift_2d_3d,
    reason="DFT calculations on the interface model (@interface_model) predict 0.14 eV CB upshift at 2D/3D interface, inducing 0.09 eV larger interface gap, consistent with experimental PL blue shift of 0.13 eV (@cb_upshift_2d_3d).",
    prior=0.9
)

strat_cb_alignment_supports_device_function = support(
    [cb_upshift_2d_3d],
    cb_alignment_favorable,
    reason="DFT results (@cb_upshift_2d_3d) show 2D CB at lower energy than 3D CB, creating barrier to electron recombination but not blocking injection to TiO2, explaining why 2D layer protects without hindering device performance (@cb_alignment_favorable).",
    prior=0.85
)

strat_dft_confirms_graded_structure = support(
    [cb_upshift_2d_3d, cb_alignment_favorable],
    graded_structure_dft,
    reason="The DFT-predicted CB upshift (@cb_upshift_2d_3d) and favorable alignment (@cb_alignment_favorable) confirm that 2D/3D perovskite organizes in gradual multi-dimensional structure retaining individual phases while forming novel oriented interface phase (@graded_structure_dft).",
    prior=0.85
)

# --- Abduction: 2D/3D Interface Explains PL Blue Shift ---
# Hypothesis: 2D/3D interface causes CB upshift matching observed PL
# Alternative: Standard MAPbI3/TiO2 interface (small ~0.02 eV shift)

dft_2d3d_pred = claim(
    "DFT predicts 0.14 eV CB upshift at 2D/3D interface, yielding 0.13 eV PL blue shift.",
    title="2D/3D DFT prediction"
)

dft_standard_pred = claim(
    "Standard MAPbI3/TiO2 interface produces only ~0.02 eV shift of opposite sign.",
    title="Standard interface DFT prediction"
)

pl_observed = claim(
    "PL measurements show 0.13 eV blue shift (730 nm vs 760 nm) when exciting from oxide side.",
    title="Observed PL blue shift"
)

support_h = support([dft_2d3d_pred], pl_observed,
    reason="DFT-predicted 0.14 eV upshift at 2D/3D interface explains observed 0.13 eV PL shift",
    prior=0.9)

support_alt = support([dft_standard_pred], pl_observed,
    reason="Standard interface 0.02 eV shift cannot explain the 0.13 eV blue shift",
    prior=0.25)

compare_pred = compare(dft_2d3d_pred, dft_standard_pred, pl_observed,
    reason="0.14 eV vs 0.02 eV prediction - clearly 2D/3D matches experiment",
    prior=0.9)

strat_abduction_pl_shift = abduction(support_h, support_alt, compare_pred,
    reason="2D/3D interface better explains PL blue shift than standard interface")

# --- Device Performance Evidence ---
strat_spiro_cell_performance = support(
    [two_d_three_d_absorption, cb_alignment_favorable],
    spiro_cell_efficiency,
    reason="Spiro-OMeTAD/Au device with 3% AVAI 2D/3D perovskite (@two_d_three_d_absorption) achieves 14.6% PCE due to favorable CB alignment that blocks recombination while preserving injection (@cb_alignment_favorable). Device architecture as described in @spiro_omeTAD_architecture.",
    prior=0.9
)

strat_spiro_stability = support(
    [spiro_cell_efficiency, phase_structure_conclusion, oxide_templating_role],
    spiro_cell_stability,
    reason="The 2D/3D cell maintains 60% initial PCE after 300h (@spiro_cell_stability) because the graded multi-dimensional structure (@phase_structure_conclusion) templated by mesoporous oxide (@oxide_templating_role) provides moisture protection while maintaining charge transport.",
    prior=0.85
)

strat_htm_free_cell_performance = support(
    [phase_structure_conclusion, cb_alignment_favorable],
    htm_free_cell_performance,
    reason="HTM-free carbon cell with 2D/3D perovskite achieves 12.71% PCE (@htm_free_cell_performance), enabled by the protective 2D layer that prevents moisture ingress without blocking electron injection (@phase_structure_conclusion, @cb_alignment_favorable). Architecture per @htm_free_architecture.",
    prior=0.85
)

strat_module_performance = support(
    [htm_free_cell_performance],
    module_performance,
    reason="The 10x10 cm2 module achieves 11.2% PCE (@module_performance) using HTM-free architecture (@htm_free_cell_performance) with 46.7% GFF (@module_gff). Area losses from interconnect distance and margins leave room for optimization.",
    prior=0.85
)

strat_module_stability = support(
    [module_performance, phase_structure_conclusion, cb_alignment_favorable],
    module_stability_test,
    reason="The module shows >10,000h stability with zero efficiency loss (@module_stability_test) because the 2D/3D graded interface (@phase_structure_conclusion) with favorable CB alignment (@cb_alignment_favorable) enables moisture-resistant operation in ambient conditions.",
    prior=0.9
)

strat_key_innovation = support(
    [module_stability_test, htm_free_cell_performance, module_performance],
    key_innovation,
    reason="The >10,000h stability (@module_stability_test) with 11.2% module efficiency (@module_performance) and 12.71% cell efficiency (@htm_free_cell_performance) demonstrates the key innovation: HTM-free, fully printable, low-cost architecture with unprecedented stability (@key_innovation).",
    prior=0.9
)

strat_record_stability = support(
    [key_innovation, module_stability_test],
    one_year_stability_record,
    reason="The >10,000h stability (@module_stability_test) represents the highest record for perovskite photovoltaics, enabling commercialization pathway (@one_year_stability_record).",
    prior=0.9
)

strat_upscale_potential = support(
    [module_performance, module_gff],
    upscale_potential,
    reason="The 10x10 cm2 module with 46.7% GFF (@module_performance, @module_gff) demonstrates industrial scalability. Further optimization by reducing interconnect distance can improve efficiency and reduce ohmic losses (@upscale_potential).",
    prior=0.8
)