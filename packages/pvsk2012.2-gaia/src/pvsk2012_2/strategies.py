"""
strategies.py - Reasoning strategies connecting knowledge nodes

This module contains the inferential reasoning that connects claims to conclusions.
"""
from gaia.lang import (
    claim, setting, support, deduction, compare, abduction,
    infer, contradiction, equivalence, complement
)

# Import knowledge nodes
from .motivation import (
    energy_loss_excitons, dssc_losses, organic_losses,
    sensitized_voc_limitation, perovskite_properties,
    prior_perovskite_work, research_gap, key_insight,
)
from .s2_methods import (
    crystal_structure,
    film_crystallinity,
    film_stability,
    n_type_scaffold,
    insulator_scaffold,
    hole_conductor,
    fabrication_process,
    pore_filling,
    perovskite_conductivity,
    spiro_conductivity,
    pia_method,
    transient_photocurrent_method,
    sem_edx_method,
)
from .s3_results import (
    al2o3_best_device, tio2_device, al2o3_high_voc_device, planar_junction,
    voc_improvement, ipce_spectral_range, optical_bandgap, voltage_deficit,
    absorbance_capability, photostability, tio2_sensitization, al2o3_insulating,
    hole_transfer_effective, hole_conductor_required, charge_collection_speed,
    perovskite_semicondo, chemical_capacitance, tio2_chemical_capacitance,
    compact_tio2, mssc_definition,
)
from .s4_discussion import (
    electron_transport_mssc, hole_transfer_mssc, al2o3_not_ntype,
    perovskite_transport_speed, junction_type, planar_junction_interp,
    series_resistance_tradeoff, main_achievement, fundamental_loss_reduction,
    future_absorption, future_photon_management, future_fill_factor,
    future_multijunction, remote_sensing_principle, classical_analog,
)

# ============ Supporting Evidence for Key Insight ============

# Strategy: Fundamental losses motivate need for new approach
strat_loss_motivation = support(
    [energy_loss_excitons, dssc_losses, organic_losses, sensitized_voc_limitation],
    research_gap,
    reason="The fundamental losses in low-cost photovoltaics (exciton separation, charge extraction, Voc limitations) establish the need for a new approach that overcomes these problems [@Lee2012].",
    prior=0.5,
)

# Strategy: Perovskite properties enable solution
strat_perovskite_solution = support(
    [perovskite_properties, prior_perovskite_work],
    key_insight,
    reason="Organometal halide perovskites have demonstrated good performance (up to 8.5%) and the properties (tunable crystal size, high crystallinity, good absorptivity) suggest they could address the fundamental losses when combined with the right architecture [@Lee2012].",
    prior=0.5,
)

# ============ Device Performance Strategies ============

# Strategy: Al2O3 outperforms TiO2
strat_al2o3_outperforms = support(
    [al2o3_best_device, tio2_device, voc_improvement],
    key_insight,
    reason="The experimental data shows Al2O3-based devices achieve 10.9% efficiency compared to 7.6% for TiO2-sensitized devices, with >200 mV higher Voc, demonstrating that electron transport through perovskite is faster than through TiO2 [@Lee2012].",
    prior=0.5,
)

# Strategy: Chemical capacitance explains Voc improvement
strat_capacitance_explanation = support(
    [chemical_capacitance, tio2_chemical_capacitance],
    voc_improvement,
    reason="The increase in Voc when switching from TiO2 to Al2O3 is explained by the reduction in chemical capacitance: TiO2 has sub-band gap states that lower the quasi-Fermi level (@tio2_chemical_capacitance), while the compact TiO2 layer (50-100 nm, spray pyrolysis, ~10^18 cm^-3 donor density) has essentially no chemical capacitance, so all charge resides in the perovskite moving EFn* closer to conduction band [@Lee2012].",
    prior=0.5,
)

# Strategy: Small voltage deficit demonstrates low losses
strat_low_losses = support(
    [optical_bandgap, voltage_deficit],
    fundamental_loss_reduction,
    reason="The voltage deficit of only 0.45 eV (band gap 1.55 eV minus Voc 1.1 V) is competitive with the best thin-film technologies, demonstrating that the MSSC approach successfully reduces fundamental energy losses [@Lee2012].",
    prior=0.5,
)

# Strategy: Efficient hole transfer enables MSSC operation
strat_hole_transfer_enables = support(
    [hole_transfer_effective, hole_conductor_required],
    mssc_definition,
    reason="The PIA spectroscopy shows hole transfer from perovskite to spiro-OMeTAD is highly effective in both TiO2 and Al2O3 systems, and the hole conductor is required to enable long-lived charge species. This confirms the MSSC operates as a two-component hybrid where Al2O3 is truly inert [@Lee2012].",
    prior=0.5,
)

# Strategy: Charge collection speed confirms fast perovskite transport
strat_fast_transport = support(
    [charge_collection_speed, perovskite_transport_speed],
    perovskite_semicondo,
    reason="Transient photocurrent measurements showing >10x faster charge collection in Al2O3 devices compared to TiO2 demonstrate that electron transport through the perovskite phase is much faster than through n-type TiO2, confirming the semiconducting nature of perovskite [@Lee2012].",
    prior=0.5,
)

# Strategy: Spectroscopic evidence for electron location
strat_electron_location = support(
    [tio2_sensitization, al2o3_insulating],
    electron_transport_mssc,
    reason="PIA spectroscopy shows free electrons in TiO2 (effective sensitization) but no signal from Al2O3 (electrons remain in perovskite), confirming that in MSSC electrons must travel through the perovskite layer to be collected [@Lee2012].",
    prior=0.5,
)

# ============ Material Stability Strategies ============

# Strategy: Mixed-halide perovskite stability enables air processing
strat_stability_enables = support(
    [film_stability, film_crystallinity, pore_filling],
    key_insight,
    reason="The remarkable air stability of the iodide-chloride mixed-halide perovskite (contrary to pure iodide versions) combined with high crystallinity (>200 nm domains) and uniform pore filling enables the mesoscopic scaffold approach to work reliably [@Lee2012].",
    prior=0.5,
)

# Strategy: Long-term photostability
strat_photostability = support(
    [photostability, absorbance_capability],
    main_achievement,
    reason="The perovskite absorber maintains 98.4% absorption at 500 nm over 1000 hours of continuous illumination under full sunlight, demonstrating the stability necessary for practical solar cell applications [@Lee2012].",
    prior=0.5,
)

# ============ Performance Achievement Strategy ============

# Strategy: Main achievement synthesis
strat_main_achievement = support(
    [key_insight, al2o3_best_device, fundamental_loss_reduction, perovskite_properties],
    main_achievement,
    reason="The combination of key insight (insulating scaffold enables perovskite transport), 10.9% efficiency achievement, reduced fundamental losses (0.45 eV voltage deficit), and perovskite's favorable properties demonstrates that the MSSC approach is extraordinarily effective for photovoltaics [@Lee2012].",
    prior=0.5,
)

# ============ Performance Limitations ============

# Strategy: Resistance tradeoff limits performance
strat_resistance_tradeoff = support(
    [perovskite_conductivity, spiro_conductivity, series_resistance_tradeoff],
    main_achievement,
    reason="The performance limitation from series-shunt resistance tradeoff (perovskite 10^-3 S/cm vs spiro-OMeTAD 10^-5 S/cm) is the key challenge remaining, but does not prevent achieving >10% efficiency in the current MSSC design [@Lee2012].",
    prior=0.5,
)

# ============ Future Directions ============

# Strategy: Future improvements possible
strat_future_improvements = support(
    [main_achievement, series_resistance_tradeoff],
    future_fill_factor,
    reason="Since fill factor is currently limited by spiro-OMeTAD conductivity and capping layer thickness, improvements in hole transporter mobility or better control of capping layer could enhance performance beyond 10.9% [@Lee2012].",
    prior=0.5,
)

# ============ Supporting Evidence for Material Properties ============

# Strategy: Perovskite structure confirms composition
strat_structure_confirms = support(
    [crystal_structure],
    perovskite_properties,
    reason="X-ray diffraction confirming tetragonal perovskite structure with lattice parameters a=8.825 A, b=8.835 A, c=11.24 A (@crystal_structure) demonstrates successful formation of CH3NH3PbI2Cl perovskite with good crystallinity and the expected perovskite structure properties [@Lee2012].",
    prior=0.5,
)

# Strategy: IPCE demonstrates broad spectral response
strat_ipce_broad = support(
    [ipce_spectral_range],
    absorbance_capability,
    reason="IPCE action spectrum showing >80% peak efficiency across 400-800 nm (@ipce_spectral_range) confirms the good light-harvesting capabilities demonstrated in UV-Vis absorbance measurements, with absorbance ~1.8 at 500 nm corresponding to 98.4% absorption [@Lee2012].",
    prior=0.5,
)

__all__ = [
    "strat_loss_motivation",
    "strat_perovskite_solution",
    "strat_al2o3_outperforms",
    "strat_capacitance_explanation",
    "strat_low_losses",
    "strat_hole_transfer_enables",
    "strat_fast_transport",
    "strat_electron_location",
    "strat_stability_enables",
    "strat_photostability",
    "strat_main_achievement",
    "strat_resistance_tradeoff",
    "strat_future_improvements",
    "strat_structure_confirms",
    "strat_ipce_broad",
]