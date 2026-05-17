"""
Gaia knowledge package for Lin2025: All-perovskite tandem solar cells with dipolar passivation.
Reasoning strategies connecting knowledge nodes.
"""

from gaia.lang import (
    claim, setting, support, infer,
    compare, contradiction, equivalence
)
from .motivation import (
    buried_interface_recombination,
    conventional_passivation_limitation,
    optimal_buried_passivation_requirement,
    dipolar_passivation_strategy,
    sa_dipole_moment,
    diffusion_length_enhancement,
    pb_sn_psc_performance,
    tandem_performance,
)
from .s2_methods import (
    device_structure,
    dipolar_passivation_design,
    tof_simms_analysis,
    xps_evidence,
    aimd_molecular_orientation,
    kpfm_potential_change,
    energy_level_alignment,
    type_ii_energy_alignment,
)
from .s3_results import (
    steady_state_pl,
    trpl_decay_components,
    enhanced_charge_extraction,
    terahertz_mobility,
    limiting_carrier_mobility,
    diffusion_length,
    electroluminescence_qy,
    average_voc_improvement,
    qfis_values,
    single_junction_metrics,
    pcce_histogram,
    operational_stability,
)
from .s4_discussion import (
    tandem_device_configuration,
    tandem_buried_interface_challenge,
    tandem_sensitivity_reduction,
    tandem_pv_parameters,
    champion_tandem_device,
    jet_certified_pce,
    large_area_tandem,
    wbg_subcell_performance,
    thickness_optimization,
    contact_loss_mitigation,
    tandem_operational_stability,
    tandem_thermal_stability,
    future_direction,
)

# =============================================================================
# STRATEGIES: Motivation -> Methods
# =============================================================================

strat_problem_supports_solution = support(
    [buried_interface_recombination, conventional_passivation_limitation],
    dipolar_passivation_strategy,
    reason="The problem of non-radiative recombination at HTL/perovskite interface combined with the limitation that "
          "conventional long-chain amine passivation causes carrier transport losses motivates the dipolar passivation "
          "approach as a solution that addresses both issues simultaneously [@Lin2025].",
    prior=0.5,
)

strat_aimd_supports_orientation = support(
    [dipolar_passivation_design],
    aimd_molecular_orientation,
    reason="AIMD simulations at the perovskite/HTL interface provide molecular-level insight into the favoured orientation "
           "of sulfanilic acid molecules, confirming that -NH3+ anchors to the perovskite while -SO3- faces the HTL [@Lin2025].",
    prior=0.5,
)

strat_kpfm_confirms_orientation = support(
    [kpfm_potential_change, energy_level_alignment],
    type_ii_energy_alignment,
    reason="KPFM measurements showing surface potential changes and UPS energy level measurements collectively confirm "
           "the formation of a type-II energy-level alignment with the preferential molecular orientation of SA dipoles "
           "[@Lin2025].",
    prior=0.5,
)

strat_tof_simms_confirms_sa = support(
    [dipolar_passivation_design],
    tof_simms_analysis,
    reason="ToF-SIMS analysis confirms that SA molecules accumulate at the buried interface as designed, with stronger "
           "signal near the bottom surface consistent with the dipolar orientation strategy [@Lin2025].",
    prior=0.5,
)

strat_xps_confirms_sa = support(
    [tof_simms_analysis],
    xps_evidence,
    reason="XPS measurements independently corroborate ToF-SIMS findings by detecting S 2p signals at the buried "
           "perovskite interface, confirming SA presence after perovskite deposition [@Lin2025].",
    prior=0.5,
)

# =============================================================================
# STRATEGIES: Methods -> Results
# =============================================================================

strat_energy_align_supports_pl = support(
    [type_ii_energy_alignment],
    steady_state_pl,
    reason="The type-II energy-level alignment created by dipolar passivation facilitates efficient hole injection "
           "and repels electrons from the interface, which suppresses non-radiative recombination and increases "
           "photoluminescence intensity observed in steady-state PL measurements [@Lin2025].",
    prior=0.5,
)

strat_energy_align_supports_trpl = support(
    [type_ii_energy_alignment],
    trpl_decay_components,
    reason="The type-II alignment enables rapid charge-carrier separation at the HTL interface, explaining the much "
           "shorter initial decay component (43 ns vs 132 ns) in dipolar-passivation-treated films compared with controls "
           "[@Lin2025].",
    prior=0.5,
)

strat_trpl_supports_extraction = support(
    [trpl_decay_components],
    enhanced_charge_extraction,
    reason="The rapid initial decay (τ1 = 43 ns) in dipolar-passivation-treated films directly demonstrates enhanced "
           "charge extraction at the interface, consistent with the type-II energy-level alignment that creates an electric "
           "field driving holes toward PEDOT:PSS [@Lin2025].",
    prior=0.5,
)

strat_terahertz_mobility = support(
    [enhanced_charge_extraction],
    terahertz_mobility,
    reason="Femtosecond-resolved optical-pump terahertz-probe spectroscopy measures the improved charge-transport "
           "properties resulting from enhanced interfacial charge extraction, showing carrier mobility increasing from "
           "67.5 to 113.5 cm^2 V^-1 s^-1 with dipolar passivation [@Lin2025].",
    prior=0.5,
)

strat_mobility_supports_diffusion_length = support(
    [terahertz_mobility, limiting_carrier_mobility],
    diffusion_length,
    reason="The enhanced carrier mobility (μdc = 113.5 cm^2 V^-1 s^-1) and improved limiting carrier mobility "
           "(μe,h = 14.7 cm^2 V^-1 s^-1) directly enable longer carrier diffusion lengths of 6.2 μm compared with "
           "4.8 μm for control films, improving carrier collection across the absorber layer [@Lin2025].",
    prior=0.5,
)

strat_pl_supports_el = support(
    [steady_state_pl],
    electroluminescence_qy,
    reason="The increased photoluminescence intensity from suppressed non-radiative recombination correlates with "
           "higher electroluminescence quantum yield (7.05% vs 2.40%), both indicating reduced defect-mediated "
           "recombination at the HTL interface [@Lin2025].",
    prior=0.5,
)

strat_el_supports_voc = support(
    [electroluminescence_qy],
    average_voc_improvement,
    reason="The improved electroluminescence quantum yield (7.05% vs 2.40%) corresponds to reduced Voc losses "
           "(73 mV vs 103 mV), explaining the 23 mV average Voc improvement in dipolar-passivation devices "
           "[@Lin2025].",
    prior=0.5,
)

strat_diffusion_length_supports_qfils = support(
    [diffusion_length],
    qfis_values,
    reason="The longer carrier diffusion length (6.2 μm vs 4.8 μm) in dipolar-passivation films enables better "
           "carrier collection and reduced non-radiative recombination, contributing to higher QFLS values "
           "(940 meV vs 904 meV at the perovskite/HTL interface) [@Lin2025].",
    prior=0.5,
)

strat_diffusion_supports_metrics = support(
    [diffusion_length, enhanced_charge_extraction, average_voc_improvement],
    single_junction_metrics,
    reason="The combination of enhanced charge extraction (rapid τ1 decay), improved carrier diffusion length "
           "(6.2 μm), and reduced Voc loss (23 mV improvement) collectively enable the champion device performance "
           "of PCE = 24.9% with Voc = 0.911 V, Jsc = 33.1 mA cm^-2, FF = 82.6% [@Lin2025].",
    prior=0.5,
)

strat_statistics = support(
    [single_junction_metrics],
    pcce_histogram,
    reason="Statistical analysis of 208 devices confirms the reproducibility of the dipolar passivation approach, "
           "showing average PCE improvement from 22.6 ± 0.2% (control) to 23.9 ± 0.3% (dipolar passivation) with "
           "reduced ideality factor and dark saturation current indicating suppressed non-radiative recombination "
           "[@Lin2025].",
    prior=0.5,
)

strat_stability = support(
    [dipolar_passivation_design],
    operational_stability,
    reason="The robust molecular anchoring of SA at the buried interface (confirmed by ToF-SIMS and XPS) provides "
           "stable passivation without degrading carrier transport, resulting in no significant PCE degradation "
           "after 1,000+ hours in nitrogen glovebox storage [@Lin2025].",
    prior=0.5,
)

# =============================================================================
# STRATEGIES: Results -> Discussion (Tandem Cells)
# =============================================================================

strat_nbg_tandem_challenge = support(
    [tandem_buried_interface_challenge],
    tandem_sensitivity_reduction,
    reason="The challenge of severe non-radiative recombination and deteriorated PEDOT:PSS properties in tandem "
           "configuration is mitigated by dipolar passivation, which makes NBG subcells less sensitive to HTL quality "
           "by reducing interfacial defects and improving contact properties [@Lin2025].",
    prior=0.5,
)

strat_contact_loss_mitigation = support(
    [tandem_sensitivity_reduction, contact_loss_mitigation],
    tandem_pv_parameters,
    reason="Dipolar passivation mitigates contact losses from the interconnecting layer by improving the NBG subcell's "
           "buried interface, leading to improved FF and Voc in tandem devices. The average PCE increases to 30.3 ± 0.3% "
           "compared with 29.1 ± 0.2% for control tandem devices [@Lin2025].",
    prior=0.5,
)

strat_tandem_champion = support(
    [tandem_pv_parameters],
    champion_tandem_device,
    reason="Building on the average tandem improvements (PCE 30.3 ± 0.3%), the champion device achieves PCE = 30.6% "
           "(reverse scan) with Voc = 2.211 V, Jsc = 16.6 mA cm^-2, and FF = 83.4%, demonstrating minimal hysteresis and "
           "stabilized PCE of 30.2% [@Lin2025].",
    prior=0.5,
)

strat_jet_certification = support(
    [champion_tandem_device],
    jet_certified_pce,
    reason="Third-party JET certification independently confirms the stabilized PCE of 30.1% for a 0.049 cm^2 device "
           "and 29.6% for a 1.07 cm^2 device, validating the lab measurements and inclusion in Solar Cell Efficiency "
           "Tables version 64 [@Lin2025].",
    prior=0.5,
)

strat_large_area = support(
    [jet_certified_pce],
    large_area_tandem,
    reason="Scaling to large-area devices (1.05 cm^2) achieves 29.6% PCE with good homogeneity and current matching, "
           "confirmed by independent JET certification at 29.6% with 1.07 cm^2 aperture area [@Lin2025].",
    prior=0.5,
)

strat_operational_stability = support(
    [dipolar_passivation_design],
    tandem_operational_stability,
    reason="Dipolar passivation provides stable field passivation that maintains interfacial properties under illumination, "
           "with encapsulated tandem devices retaining 87% of initial PCE after 1,025 hours of continuous MPP tracking "
           "under 1-sun illumination in ambient air [@Lin2025].",
    prior=0.5,
)

strat_thermal_stability = support(
    [dipolar_passivation_design],
    tandem_thermal_stability,
    reason="The amphoteric nature of dipolar-passivation molecules (containing both -NH3+ and -SO3- groups) helps "
           "mitigate the detrimental impact of PEDOT:PSS acidity on device stability, resulting in slower degradation "
           "under thermal stress compared with control devices [@Lin2025].",
    prior=0.5,
)

strat_wbg_performance = support(
    [tandem_device_configuration],
    wbg_subcell_performance,
    reason="The WBG subcell with SAM-modified NiO HTL achieves PCE = 20.5% with optimized composition "
           "(FA0.8Cs0.2Pb(I0.62Br0.38)3, ~1.78 eV bandgap) and appropriate thickness for current matching "
           "[@Lin2025].",
    prior=0.5,
)

strat_thickness_balance = support(
    [wbg_subcell_performance],
    thickness_optimization,
    reason="Thickness optimization of WBG (~380 nm) and NBG (~1,200 nm) absorber layers achieves optimal current "
           "density matching between subcells in the tandem configuration, enabling the high tandem PCE of 30.6% "
           "[@Lin2025].",
    prior=0.5,
)

strat_diff_length_enhancement_supports_main_claim = support(
    [diffusion_length_enhancement, pb_sn_psc_performance],
    tandem_performance,
    reason="The extended carrier diffusion length to 6.2 μm in dipolar-passivation-treated Pb-Sn perovskite "
           "films enables improved carrier collection, which translates to high PCE of 24.9% for single-junction "
           "devices and contributes to the 30.6% certified PCE for all-perovskite tandem solar cells [@Lin2025].",
    prior=0.5,
)

# =============================================================================
# OPERATORS: Contradictions and Equivalences
# =============================================================================

# Contrast with conventional passivation limitation
conv_vs_dipolar_contradiction = contradiction(
    conventional_passivation_limitation,
    dipolar_passivation_strategy,
    reason="Conventional long-chain amine passivation induces carrier transport losses (asymmetric conductivity, "
           "insulating barriers), while dipolar passivation with sulfanilic acid simultaneously suppresses recombination "
           "AND establishes ohmic contact for efficient hole transport - they cannot both be optimal strategies.",
    prior=0.5,
)