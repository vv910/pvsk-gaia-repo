from gaia.lang import (
    claim, setting, support, infer, compare, contradiction,
    abduction, equivalence, complement, disjunction, composite
)
from .motivation import (
    psc_efficiency_exceeds_25,
    t80_lifetime_thousand_hours,
    commercial_requirement_20_years,
    research_objective,
    inorganic_cs_pbi3_chosen,
    capped_vs_uncapped_device_structure,
    all_inorganic_stack_designed,
    how_does_2d_capping_affect_stability,
    what_is_intrinsic_lifetime,
)
from .s2_methods import (
    device_structure_diagram,
    champion_pce_uncapped,
    champion_pce_capped,
    capped_improved_ff_and_voc,
    giwaxs_new_reflections,
    giwaxs_surface_preferential,
    giwaxs_interfacial_nature_confirmed,
    capping_layer_thickness,
    trpl_lifetime_uncapped,
    trpl_lifetime_capped,
    trpl_implies_suppressed_recombination,
    stability_test_conditions,
    no_degradation_capped_35c,
    fitting_r_squared,
    two_transport_regimes,
    high_temperature_ion_dominated,
    xrd_uncapped_degradation,
    xrd_capped_no_change,
    sem_uncapped_pinholes,
    sem_capped_no_change,
    xps_iodine_increase_uncapped,
    xps_no_iodine_capped,
)
from .s3_results import (
    giwaxs_angle_dependence,
    trpl_observation,
    degradation_rate_follows_arrhenius,
    activation_energy_comparable_fast_slow,
    activation_energy_capped_higher,
    ion_migration_speculated,
    af_110c_value,
    t80_110c_capped,
    t80_extrapolated_35c,
    ea_ion_uncapped,
    ea_ion_capped_twice_uncapped,
    passivation_frustrates_ion_migration,
    key_results_summary,
)
from .s4_discussion import (
    ion_migration_degradation_mechanism,
    capping_stabilizes_interface,
    passivation_effect,
    single_mechanism_arrhenius,
    data_collapse_universal_curve,
    intrinsic_lifetime_extrapolation,
    stability_comparison,
    cation_exchange_challenge,
    thermal_photostability_design,
)

# ============================================================================
# STRATEGY: 2D capping layer improves PV performance
# ============================================================================
strat_capping_improves_efficiency = support(
    [champion_pce_uncapped, champion_pce_capped],
    capped_improved_ff_and_voc,
    reason=(
        "The champion PCE increases from 14.9% (uncapped) to 17.4% (capped), with improved FF and VOC. "
        "@champion_pce_uncapped and @champion_pce_capped directly report these measured values, "
        "and @capped_improved_ff_and_voc summarizes the device performance improvement."
    ),
    prior=0.5,
)

# ============================================================================
# STRATEGY: TRPL analysis supports surface passivation
# ============================================================================
strat_trpl_supports_passivation = support(
    [trpl_lifetime_uncapped, trpl_lifetime_capped, trpl_observation],
    trpl_implies_suppressed_recombination,
    reason=(
        "TRPL lifetime increases from 14 ns (@trpl_lifetime_uncapped) to >62 ns (@trpl_lifetime_capped). "
        "This increase is direct evidence of suppressed nonradiative recombination at the surface, "
        "as stated in @trpl_implies_suppressed_recombination."
    ),
    prior=0.5,
)

strat_passivation_effect = support(
    [trpl_implies_suppressed_recombination, capped_improved_ff_and_voc],
    passivation_effect,
    reason=(
        "The 2D layer suppresses nonradiative recombination (@trpl_implies_suppressed_recombination), "
        "leading to improved FF and VOC (@capped_improved_ff_and_voc) and improved PCE."
    ),
    prior=0.5,
)

# ============================================================================
# STRATEGY: GIWAXS confirms 2D layer formation
# ============================================================================
strat_giwaxs_confirms_2d_layer = support(
    [giwaxs_new_reflections, giwaxs_surface_preferential],
    giwaxs_angle_dependence,
    reason=(
        "New reflections in GIWAXS (@giwaxs_new_reflections) and angle-dependent intensity changes "
        "(@giwaxs_surface_preferential) together confirm the 2D layer forms preferentially at the surface. "
        "This is captured in @giwaxs_angle_dependence."
    ),
    prior=0.5,
)

strat_2d_layer_interfacial = support(
    [giwaxs_angle_dependence, giwaxs_interfacial_nature_confirmed],
    capping_layer_thickness,
    reason=(
        "GIWAXS confirms surface 2D formation (@giwaxs_angle_dependence) and SEM confirms interfacial nature "
        "(@giwaxs_interfacial_nature_confirmed), supporting the 20nm thickness estimate (@capping_layer_thickness)."
    ),
    prior=0.5,
)

# ============================================================================
# STRATEGY: Single Arrhenius mechanism validates accelerated aging
# ============================================================================
strat_single_arrhenius_validates_aat = support(
    [degradation_rate_follows_arrhenius, activation_energy_comparable_fast_slow],
    single_mechanism_arrhenius,
    reason=(
        "A single Arrhenius function describes degradation across all temperatures (@degradation_rate_follows_arrhenius), "
        "and Ea_fast and Ea_slow are comparable (@activation_energy_comparable_fast_slow). "
        "This indicates one dominant physical process across the temperature range, validating accelerated aging."
    ),
    prior=0.5,
)

strat_universal_curve = support(
    [data_collapse_universal_curve, af_110c_value],
    single_mechanism_arrhenius,
    reason=(
        "When aging time is multiplied by AF, data collapse to a universal curve (@data_collapse_universal_curve). "
        "This confirms the same mechanism operates at all temperatures, supporting @single_mechanism_arrhenius."
    ),
    prior=0.5,
)

# ============================================================================
# STRATEGY: 2D capping increases activation energy
# ============================================================================
strat_capping_increases_ea = support(
    [activation_energy_capped_higher],
    capping_stabilizes_interface,
    reason=(
        "Capped PSCs have nearly 2x higher activation energy for degradation (@activation_energy_capped_higher), "
        "indicating the 2D layer stabilizes the interface against thermal degradation."
    ),
    prior=0.5,
)

# ============================================================================
# STRATEGY: Ion migration characterization
# ============================================================================
strat_ion_migration_frustrated = support(
    [ea_ion_capped_twice_uncapped],
    passivation_frustrates_ion_migration,
    reason=(
        "Ea_ion for capped films is nearly 2x that of uncapped films (@ea_ion_capped_twice_uncapped), "
        "indicating the 2D cap frustrates ion migration (@passivation_frustrates_ion_migration)."
    ),
    prior=0.5,
)

strat_ion_migration_mechanism = support(
    [ea_ion_uncapped, two_transport_regimes, high_temperature_ion_dominated],
    ion_migration_speculated,
    reason=(
        "Temperature-dependent conductivity shows two transport regimes (@two_transport_regimes), "
        "with the high-temperature regime being ion-dominated (@high_temperature_ion_dominated). "
        "Ea_ion is lower for uncapped films (@ea_ion_uncapped), suggesting ion migration is the "
        "degradation mechanism (@ion_migration_speculated)."
    ),
    prior=0.5,
)

# ============================================================================
# STRATEGY: Degradation evidence from aged devices
# ============================================================================
strat_uncapped_degradation = support(
    [xrd_uncapped_degradation, sem_uncapped_pinholes, xps_iodine_increase_uncapped],
    ion_migration_degradation_mechanism,
    reason=(
        "Aged uncapped PSCs show CuSCN degradation (@xrd_uncapped_degradation), pinhole formation (@sem_uncapped_pinholes), "
        "and iodine accumulation at the HTL surface (@xps_iodine_increase_uncapped). "
        "These are consistent with iodine migration from CsPbI3 degrading CuSCN (@ion_migration_degradation_mechanism)."
    ),
    prior=0.5,
)

strat_capped_no_degradation = support(
    [xrd_capped_no_change, sem_capped_no_change, xps_no_iodine_capped],
    capping_stabilizes_interface,
    reason=(
        "Aged capped PSCs show no CuSCN degradation (@xrd_capped_no_change), no morphology changes (@sem_capped_no_change), "
        "and no iodine accumulation at HTL surface (@xps_no_iodine_capped). "
        "This confirms the 2D capping layer stabilizes the interface (@capping_stabilizes_interface)."
    ),
    prior=0.5,
)

# ============================================================================
# STRATEGY: T80 lifetime extrapolation
# ============================================================================
strat_t80_extrapolation = support(
    [t80_110c_capped, af_110c_value],
    t80_extrapolated_35c,
    reason=(
        "T80 at 110°C is >2100 hours (@t80_110c_capped) and AF at 110°C is 24.2 ± 3.5 (@af_110c_value). "
        "Multiplying gives T80 at 35°C of 5.1 ± 0.7 × 10^4 hours (@t80_extrapolated_35c)."
    ),
    prior=0.5,
)

strat_intrinsic_lifetime = support(
    [t80_extrapolated_35c],
    intrinsic_lifetime_extrapolation,
    reason=(
        "The T80 at 35°C is extrapolated to 51,000 ± 7000 hours (@t80_extrapolated_35c), "
        "representing >5 years of continuous operation at standard conditions."
    ),
    prior=0.5,
)

# ============================================================================
# STRATEGY: Why inorganic 2D layer was necessary
# ============================================================================
strat_cation_exchange_challenge = support(
    [inorganic_cs_pbi3_chosen],
    cation_exchange_challenge,
    reason=(
        "Inorganic CsPbI3 was chosen (@inorganic_cs_pbi3_chosen) to maximize stability. "
        "Cs+ has stronger binding than MA+ or FA+, preventing cation exchange with organic 2D perovskite "
        "precursors, which is why an inorganic Cs2PbI2Cl2 2D layer was needed (@cation_exchange_challenge)."
    ),
    prior=0.5,
)

# ============================================================================
# STRATEGY: Compare stability to state-of-the-art
# ============================================================================
strat_stability_improvement = support(
    [t80_extrapolated_35c, t80_lifetime_thousand_hours, commercial_requirement_20_years],
    stability_comparison,
    reason=(
        "Capped devices extrapolate to T80 of ~51,000 hours at 35°C (@t80_extrapolated_35c), "
        "far exceeding the typical T80 of hundreds/thousands of hours (@t80_lifetime_thousand_hours) "
        "though still short of the >20-year commercial requirement (@commercial_requirement_20_years). "
        "This represents significant stability improvement over state-of-the-art PSCs."
    ),
    prior=0.5,
)

# ============================================================================
# STRATEGY: All-inorganic design rationale
# ============================================================================
strat_inorganic_design = support(
    [inorganic_cs_pbi3_chosen],
    thermal_photostability_design,
    reason=(
        "Inorganic CsPbI3 was chosen (@inorganic_cs_pbi3_chosen) to maximize thermal and photostability, "
        "justifying the all-inorganic stack design for long-term operational durability."
    ),
    prior=0.5,
)

# ============================================================================
# STRATEGY: Key results summary
# ============================================================================
strat_key_results = support(
    [champion_pce_capped, no_degradation_capped_35c, t80_110c_capped, t80_extrapolated_35c,
     activation_energy_capped_higher, ea_ion_capped_twice_uncapped],
    key_results_summary,
    reason=(
        "Key results include: PCE improves to 17.4% (@champion_pce_capped), no degradation at 35°C for >3500h "
        "(@no_degradation_capped_35c), T80 >2100h at 110°C (@t80_110c_capped), extrapolated T80 ~51,000h at 35°C "
        "(@t80_extrapolated_35c), Ea ~2x higher for capped (@activation_energy_capped_higher), "
        "and Ea_ion ~2x higher for capped (@ea_ion_capped_twice_uncapped)."
    ),
    prior=0.5,
)