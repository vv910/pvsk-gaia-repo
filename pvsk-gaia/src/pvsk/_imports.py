"""
Cross-package public-API imports for the PVSK synthesis package.

This module imports only top-level symbols exported by each paper package.  The
EXPORTS dictionaries make the package boundary explicit, while the aliases below
give synthesis modules stable, readable names for selected evidence claims.
"""

import pvsk2009 as pkg_2009
import pvsk2012_1 as pkg_2012_1
import pvsk2012_2 as pkg_2012_2
import pvsk2013 as pkg_2013
import pvsk2014 as pkg_2014
import pvsk2015 as pkg_2015
import pvsk2017 as pkg_2017
import pvskc5ee03874j as pkg_triple_cation
import pvsknature12509 as pkg_vapour
import pvsks41467_024_46016_1 as pkg_r2r
import pvsks41560_023_01254_3 as pkg_bifacial
import pvsks41560_024_01667_8 as pkg_homogeneous_2d
import pvsks41586_021_03406_5 as pkg_formate
import pvsks41586_021_04372_8 as pkg_all_perovskite_tandem
import pvsks41586_023_06278_z as pkg_3d3d
import pvsks41586_024_07997_7 as pkg_persik_2024
import pvsks41586_025_09333_z as pkg_htl201
import pvsks41586_025_09773_7 as pkg_dipolar
import pvskscience_aay7044 as pkg_mda
import pvskscience_abm5784 as pkg_damp_heat
import pvskscience_abn5679 as pkg_all_inorganic
import pvskscience_adk1633 as pkg_dmdp


def _exports(module):
    return {name: getattr(module, name) for name in module.__all__}


PVSK2009_EXPORTS = _exports(pkg_2009)
PVSK2012_1_EXPORTS = _exports(pkg_2012_1)
PVSK2012_2_EXPORTS = _exports(pkg_2012_2)
PVSK2013_EXPORTS = _exports(pkg_2013)
PVSK2014_EXPORTS = _exports(pkg_2014)
PVSK2015_EXPORTS = _exports(pkg_2015)
PVSK2017_EXPORTS = _exports(pkg_2017)
PVSK_TRIPLE_CATION_EXPORTS = _exports(pkg_triple_cation)
PVSK_VAPOUR_EXPORTS = _exports(pkg_vapour)
PVSK_R2R_EXPORTS = _exports(pkg_r2r)
PVSK_BIFACIAL_EXPORTS = _exports(pkg_bifacial)
PVSK_HOMOGENEOUS_2D_EXPORTS = _exports(pkg_homogeneous_2d)
PVSK_FORMATE_EXPORTS = _exports(pkg_formate)
PVSK_ALL_PEROVSKITE_TANDEM_EXPORTS = _exports(pkg_all_perovskite_tandem)
PVSK_3D3D_EXPORTS = _exports(pkg_3d3d)
PVSK_PERSIK_2024_EXPORTS = _exports(pkg_persik_2024)
PVSK_HTL201_EXPORTS = _exports(pkg_htl201)
PVSK_DIPOLAR_EXPORTS = _exports(pkg_dipolar)
PVSK_MDA_EXPORTS = _exports(pkg_mda)
PVSK_DAMP_HEAT_EXPORTS = _exports(pkg_damp_heat)
PVSK_ALL_INORGANIC_EXPORTS = _exports(pkg_all_inorganic)
PVSK_DMDP_EXPORTS = _exports(pkg_dmdp)


# 2009 first perovskite sensitization.
from pvsk2009 import (
    bromide_cell_high_voltage as pvsk2009_bromide_voc,
    bromide_ipce_spectrum as pvsk2009_bromide_ipce,
    conclusion_perovskite_sensitization as pvsk2009_sensitization,
    conduction_band_levels as pvsk2009_conduction_band,
    durability_observation as pvsk2009_durability,
    efficiency_milestone as pvsk2009_efficiency_milestone,
    iodide_cell_efficiency as pvsk2009_efficiency,
    iodide_ipce_spectrum as pvsk2009_iodide_ipce,
    valence_band_levels as pvsk2009_valence_band,
)

# 2012 solid-state and meso-superstructured milestones.
from pvsk2012_1 import (
    bandgap_1_5_ev as pvsk2012_1_bandgap,
    charge_separation_well_aligned as pvsk2012_1_band_alignment,
    ipce_over_50_percent as pvsk2012_1_ipce,
    panchromatic_absorption_leads_to_high_jsc as pvsk2012_1_panchromatic,
    pce_9_7_percent as pvsk2012_1_pce,
    solid_state_dramatically_improved_stability as pvsk2012_1_solid_stability,
    stability_improvement as pvsk2012_1_stability,
)

from pvsk2012_2 import (
    al2o3_best_device as pvsk2012_2_al2o3_best,
    hole_transfer_effective as pvsk2012_2_hole_transfer,
    main_achievement as pvsk2012_2_main_achievement,
    perovskite_semicondo as pvsk2012_2_semiconductor,
    photostability as pvsk2012_2_photostability,
    planar_junction as pvsk2012_2_planar,
    voc_improvement as pvsk2012_2_voc_improvement,
)

# 2013-2015 deposition, solvent, and composition engineering.
from pvsk2013 import (
    best_device_performance as pvsk2013_best_device,
    certified_efficiency as pvsk2013_certified,
    no_photodegradation as pvsk2013_no_photodegradation,
    reproducibility_improvement as pvsk2013_reproducibility,
    sequential_deposition_introduced as pvsk2013_sequential_deposition,
    two_step_method_applicability as pvsk2013_two_step_applicability,
)

from pvsknature12509 import (
    high_efficiency_planar_demonstrated as pvsknature12509_planar_efficiency,
    planar_architecture_sufficiency as pvsknature12509_planar_sufficient,
    tandem_top_cell_potential as pvsknature12509_tandem_potential,
    uniformity_advantage as pvsknature12509_uniformity,
    vapour_deposition_enables_uniform_films as pvsknature12509_vapour_deposition,
    vapour_deposition_maturity as pvsknature12509_vapour_maturity,
)

from pvsk2014 import (
    bilayer_advantages as pvsk2014_bilayer_advantages,
    bilayer_architecture as pvsk2014_bilayer_architecture,
    certified_efficiency_162 as pvsk2014_certified_efficiency,
    formation_mechanism as pvsk2014_formation_mechanism,
    full_surface_coverage as pvsk2014_full_coverage,
    hysteresis_origin as pvsk2014_hysteresis_origin,
    negligible_hysteresis_bilayer as pvsk2014_negligible_hysteresis,
)

from pvsk2015 import (
    bandgap_tuning_tradeoff as pvsk2015_bandgap_tradeoff,
    certified_pce as pvsk2015_certified_pce,
    hysteresis_benefit as pvsk2015_hysteresis_benefit,
    main_conclusion as pvsk2015_main_conclusion,
    phase_stabilization_evidence as pvsk2015_phase_stabilization,
    synergetic_effect as pvsk2015_synergetic_effect,
)

from pvskc5ee03874j import (
    best_stabilized_pce as pvsk_triple_cation_best_pce,
    cs_suppresses_yellow_phase as pvsk_triple_cation_cs_suppression,
    industrialization_relevance as pvsk_triple_cation_industrial_relevance,
    long_term_stability as pvsk_triple_cation_long_term_stability,
    triple_cation_strategy as pvsk_triple_cation_strategy,
    tuneable_bandgap as pvsk_triple_cation_tunable_bandgap,
)

# Interface, passivation, stability, and tandem packages.
from pvsk2017 import (
    cb_upshift_2d_3d as pvsk2017_cb_upshift,
    graded_structure_dft as pvsk2017_graded_structure,
    hysteresis_observation as pvsk2017_hysteresis,
    key_innovation as pvsk2017_key_innovation,
    module_performance as pvsk2017_module_performance,
    one_year_stability_record as pvsk2017_one_year_stability,
    two_d_three_d_composite_preparation as pvsk2017_2d3d_composite,
)

from pvskscience_aay7044 import (
    alpha_phase_retention_38 as pvsk_mda_alpha_38,
    alpha_phase_retention_57 as pvsk_mda_alpha_57,
    certified_pce as pvsk_mda_certified_pce,
    conclusion_alpha_stabilization as pvsk_mda_alpha_stabilization,
    conclusion_no_tradeoff as pvsk_mda_no_tradeoff,
    highest_jsc as pvsk_mda_highest_jsc,
    stabilization_mechanism_h_bonding as pvsk_mda_h_bonding,
)

from pvskscience_abm5784 import (
    champion_pce_24_3_percent as pvsk_damp_heat_pce,
    commercial_relevance as pvsk_damp_heat_commercial_relevance,
    dual_function_passivation as pvsk_damp_heat_dual_passivation,
    energy_level_match_critical as pvsk_damp_heat_energy_match,
    iecs_standard_met as pvsk_damp_heat_iec,
    moisture_oxygen_barrier as pvsk_damp_heat_barrier,
    t95_after_1200_hours as pvsk_damp_heat_t95,
)

from pvskscience_abn5679 import (
    activation_energy_capped_higher as pvsk_all_inorganic_activation_energy,
    arrhenius_temperature_dependence as pvsk_all_inorganic_arrhenius,
    capped_improved_ff_and_voc as pvsk_all_inorganic_capped_improvement,
    champion_pce_capped as pvsk_all_inorganic_pce,
    passivation_frustrates_ion_migration as pvsk_all_inorganic_ion_migration,
    t80_extrapolated_35c as pvsk_all_inorganic_t80,
    thermal_photostability_design as pvsk_all_inorganic_design,
)

from pvskscience_adk1633 import (
    diammonium_field_effect as pvsk_dmdp_field_effect,
    dianmmonium_pce_improvement as pvsk_dmdp_pce_improvement,
    dual_passivation_concept as pvsk_dmdp_dual_concept,
    methylthio_chemical_passivation as pvsk_dmdp_chemical_passivation,
    operating_stability as pvsk_dmdp_operating_stability,
    pai2_3mtpai_highest_pce as pvsk_dmdp_highest_pce,
    qss_pce_certification as pvsk_dmdp_qss_certification,
    single_molecule_insufficient as pvsk_dmdp_single_molecule_limit,
    stable_operation as pvsk_dmdp_stable_operation,
    surface_passivation_suppresses as pvsk_dmdp_surface_passivation,
    tandem_achievement as pvsk_dmdp_tandem_achievement,
    tandem_pce as pvsk_dmdp_tandem_pce,
)

from pvsks41560_023_01254_3 import (
    bifacial_gain_percentage as pvsk_bifacial_gain,
    damp_heat_retention as pvsk_bifacial_damp_heat,
    initial_pce_retention_6000h as pvsk_bifacial_6000h,
    minimodule_front_aperture_efficiency as pvsk_bifacial_module_record,
    nrel_certified_front_efficiency as pvsk_bifacial_nrel_front,
    power_generation_density_measurement as pvsk_bifacial_power_density,
    stability_benefits_composition as pvsk_bifacial_stability_composition,
)

from pvsks41560_024_01667_8 import (
    champion_small_device as pvsk_homogeneous_2d_champion,
    efficiency_summary as pvsk_homogeneous_2d_efficiency,
    fabr_enables_uniform_n2 as pvsk_homogeneous_2d_fabr,
    large_device_efficiency as pvsk_homogeneous_2d_large_device,
    large_module_summary as pvsk_homogeneous_2d_large_module,
    main_conclusion as pvsk_homogeneous_2d_main,
    operational_stability as pvsk_homogeneous_2d_operational_stability,
    stability_summary as pvsk_homogeneous_2d_stability,
    triple_halide_eliminates_phase_sep as pvsk_homogeneous_2d_triple_halide,
)

from pvsks41586_021_03406_5 import (
    formate_at_interfaces as pvsk_formate_interfaces,
    key_role_of_formate as pvsk_formate_key_role,
    long_term_operational_stability as pvsk_formate_long_term_stability,
    non_radiative_recombination_reduction as pvsk_formate_recombination_reduction,
    pcertified_performance as pvsk_formate_certified_performance,
    reduced_ideality_factor as pvsk_formate_ideality,
    target_device_performance as pvsk_formate_target_performance,
)

from pvsks41586_021_04372_8 import (
    certified_26_4_percent as pvsk_all_tandem_certified_26_4,
    certified_pce_264_percent as pvsk_all_tandem_certified,
    deep_in_gap_states_eliminated as pvsk_all_tandem_deep_states,
    diffusion_length_increased_threefold as pvsk_all_tandem_diffusion_length,
    grain_surface_passivation_route as pvsk_all_tandem_passivation_route,
    large_area_tandem as pvsk_all_tandem_large_area,
    operational_stability_600h as pvsk_all_tandem_operational_600h,
    perovskite_tunable_bandgap as pvsk_all_tandem_tunable_bandgap,
)

from pvsks41586_023_06278_z import (
    bilateral_improvement as pvsk_3d3d_bilateral_improvement,
    certified_efficiency as pvsk_3d3d_certified,
    long_term_stability as pvsk_3d3d_long_term_stability,
    phj_solution as pvsk_3d3d_phj_solution,
    record_efficiency as pvsk_3d3d_record_efficiency,
    surface_passivation_tradeoff as pvsk_3d3d_passivation_tradeoff,
    tandem_champion as pvsk_3d3d_tandem_champion,
    type_ii_mechanism as pvsk_3d3d_type_ii_mechanism,
    type_two_band_alignment as pvsk_3d3d_type2_alignment,
)

from pvsks41586_024_07997_7 import (
    bilayer_no_tradeoff as pvsk_persik_2024_no_tradeoff,
    bilateral_passivation_strategy as pvsk_persik_2024_bilateral_passivation,
    champion_device_performance as pvsk_persik_2024_champion,
    edai_ff_tradeoff as pvsk_persik_2024_edai_tradeoff,
    first_to_exceed_sq_limit as pvsk_persik_2024_sq_limit,
    nrel_certified_pce as pvsk_persik_2024_nrel_certified,
    operational_stability as pvsk_persik_2024_operational_stability,
    passivation_tradeoff as pvsk_persik_2024_passivation_tradeoff,
)

from pvsks41586_025_09333_z import (
    certified_pce_34_58 as pvsk_htl201_certified,
    htl201_champion_pce as pvsk_htl201_champion,
    htl201_enhanced_voc_ff as pvsk_htl201_voc_ff,
    htl201_operational_25c_98_percent as pvsk_htl201_operational_25c,
    htl201_outcome as pvsk_htl201_outcome,
    htl201_passivates_pb_defects as pvsk_htl201_pb_passivation,
    htl201_strong_binding_perovskite as pvsk_htl201_binding,
)

from pvsks41586_025_09773_7 import (
    buried_interface_recombination as pvsk_dipolar_buried_recombination,
    conventional_passivation_limitation as pvsk_dipolar_conventional_limit,
    conv_vs_dipolar_contradiction as pvsk_dipolar_conv_vs_dipolar_tension,
    dipolar_passivation_strategy as pvsk_dipolar_strategy,
    diffusion_length_enhancement as pvsk_dipolar_diffusion_length,
    enhanced_charge_extraction as pvsk_dipolar_charge_extraction,
    jet_certified_pce as pvsk_dipolar_jet_certified,
    operational_stability as pvsk_dipolar_operational_stability,
    tandem_operational_stability as pvsk_dipolar_tandem_stability,
    tandem_performance as pvsk_dipolar_tandem_performance,
    type_ii_energy_alignment as pvsk_dipolar_type_ii_alignment,
)

from pvsks41467_024_46016_1 import (
    best_cell_performance as pvsk_r2r_best_cell,
    carbon_electrode_replacement as pvsk_r2r_carbon_electrode,
    cost_prediction as pvsk_r2r_cost_prediction,
    first_fully_r2r_cells as pvsk_r2r_cells,
    first_fully_r2r_modules as pvsk_r2r_modules,
    high_throughput_capability as pvsk_r2r_throughput,
    module_record as pvsk_r2r_module_record,
    pfsd_technique_description as pvsk_r2r_pfsd,
    production_cost_power as pvsk_r2r_production_cost_power,
)
