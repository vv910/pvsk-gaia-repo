"""
S4: Induction laws across independent paper packages.

Each support edge is generative: the proposed law predicts an imported
paper-level observation.  Independent observations are then combined with
binary, chainable induction().
"""

from gaia.lang import claim, induction, support

from ._imports import (
    pvsk2009_sensitization,
    pvsk2012_1_panchromatic,
    pvsk2012_2_semiconductor,
    pvsk2014_certified_efficiency,
    pvsk2015_phase_stabilization,
    pvsk2015_bandgap_tradeoff,
    pvsk_triple_cation_strategy,
    pvsk_triple_cation_tunable_bandgap,
    pvsk2017_2d3d_composite,
    pvsk2017_one_year_stability,
    pvsk_mda_alpha_stabilization,
    pvsk_damp_heat_barrier,
    pvsk_damp_heat_t95,
    pvsk_all_inorganic_ion_migration,
    pvsk_formate_recombination_reduction,
    pvsk_all_tandem_deep_states,
    pvsk_all_tandem_diffusion_length,
    pvsk_all_tandem_large_area,
    pvsk_all_tandem_passivation_route,
    pvsk_all_tandem_tunable_bandgap,
    pvsk_all_tandem_operational_600h,
    pvsk_dmdp_dual_concept,
    pvsk_dmdp_tandem_pce,
    pvsk_dipolar_strategy,
    pvsk_dipolar_charge_extraction,
    pvsk_dipolar_tandem_performance,
    pvsk2012_1_band_alignment,
    pvsk2012_2_hole_transfer,
    pvsk2017_cb_upshift,
    pvsknature12509_tandem_potential,
    pvsk_3d3d_type2_alignment,
    pvsk_3d3d_type_ii_mechanism,
    pvsk_dipolar_type_ii_alignment,
    pvsk_all_tandem_certified,
    pvsk_3d3d_tandem_champion,
    pvsk_persik_2024_nrel_certified,
    pvsk_persik_2024_sq_limit,
    pvsk_htl201_certified,
    pvsk_htl201_voc_ff,
    pvsk_dipolar_jet_certified,
    pvsk2013_sequential_deposition,
    pvsknature12509_vapour_deposition,
    pvsk_r2r_cells,
    pvsk_bifacial_nrel_front,
    pvsk_homogeneous_2d_large_module,
)

from .s1_agreement import (
    agreement_dimensional_interfaces_improve_stability,
    agreement_passivation_reduces_recombination,
    agreement_phase_and_composition_control_matter,
    area_normalized_performance,
    certification_status_normalized,
    encapsulation_and_lifetime_requirements,
    interface_stability_axis,
    ion_migration_axis,
    module_yield_and_reproducibility,
    operational_stability_axis,
    passivation_reduces_recombination_and_improves_voltage,
)
from .s3_contradictions import (
    effective_passivation_requires_defect_reduction_without_transport_penalty,
    hysteresis_suppression_does_not_identify_single_microscopic_cause,
    ion_migration_contributes_to_hysteresis,
    passivation_may_hurt_ff_if_it_blocks_extraction,
)


law_perovskite_absorbers_scale_across_architectures = claim(
    "Perovskite absorbers preserve photovoltaic effectiveness across liquid, "
    "solid-state, mesoporous, planar, and tandem architectures when interfaces are "
    "properly controlled.",
    title="Perovskite absorbers scale across architectures",
)

s_law_absorber_2009 = support(
    [law_perovskite_absorbers_scale_across_architectures],
    pvsk2009_sensitization,
    reason="The law predicts the initial 2009 perovskite sensitization result.",
    prior=0.82,
)
s_law_absorber_2012_1 = support(
    [law_perovskite_absorbers_scale_across_architectures],
    pvsk2012_1_panchromatic,
    reason="The law predicts panchromatic response in the 2012 solid-state device.",
    prior=0.85,
)
s_law_absorber_2012_2 = support(
    [law_perovskite_absorbers_scale_across_architectures],
    pvsk2012_2_semiconductor,
    reason="The law predicts semiconductor behavior in the meso-superstructured device.",
    prior=0.84,
)
s_law_absorber_2014 = support(
    [law_perovskite_absorbers_scale_across_architectures],
    pvsk2014_certified_efficiency,
    reason="The law predicts high certified efficiency after bilayer interface control.",
    prior=0.88,
)

ind_absorber_2009_2012 = induction(
    s_law_absorber_2009,
    s_law_absorber_2012_1,
    law=law_perovskite_absorbers_scale_across_architectures,
    reason="The 2009 and 2012_1 packages are independent architecture tests.",
)
ind_absorber_2012_2 = induction(
    ind_absorber_2009_2012,
    s_law_absorber_2012_2,
    law=law_perovskite_absorbers_scale_across_architectures,
    reason="The 2012_2 meso-superstructured result adds an independent architecture.",
)
induction_perovskite_absorbers_scale = induction(
    ind_absorber_2012_2,
    s_law_absorber_2014,
    law=law_perovskite_absorbers_scale_across_architectures,
    reason="The 2014 bilayer result adds a later certified device architecture.",
)


law_interface_passivation_reduces_nonradiative_loss = claim(
    "Interface passivation reduces non-radiative loss across grain surfaces, buried "
    "interfaces, and dimensional heterointerfaces.",
    title="Interface passivation reduces non-radiative loss",
)

s_law_pass_formate = support(
    [law_interface_passivation_reduces_nonradiative_loss],
    pvsk_formate_recombination_reduction,
    reason="The law predicts the formate reduction of non-radiative recombination.",
    prior=0.86,
)
s_law_pass_cf3 = support(
    [law_interface_passivation_reduces_nonradiative_loss],
    pvsk_all_tandem_deep_states,
    reason="The law predicts elimination of deep in-gap states by grain-surface passivation.",
    prior=0.87,
)
s_law_pass_diffusion = support(
    [law_interface_passivation_reduces_nonradiative_loss],
    pvsk_all_tandem_diffusion_length,
    reason="The law predicts longer diffusion length after recombination-active defects are suppressed.",
    prior=0.86,
)
s_law_pass_dmdp = support(
    [law_interface_passivation_reduces_nonradiative_loss],
    pvsk_dmdp_dual_concept,
    reason="The law predicts the dual-passivation design in the DMDP package.",
    prior=0.84,
)
s_law_pass_dipolar = support(
    [law_interface_passivation_reduces_nonradiative_loss],
    pvsk_dipolar_strategy,
    reason="The law predicts buried-interface dipolar passivation as a recombination-control strategy.",
    prior=0.85,
)

ind_pass_formate_cf3 = induction(
    s_law_pass_formate,
    s_law_pass_cf3,
    law=law_interface_passivation_reduces_nonradiative_loss,
    reason="Formate and CF3-PA packages use independent passivation chemistries.",
)
ind_pass_diffusion = induction(
    ind_pass_formate_cf3,
    s_law_pass_diffusion,
    law=law_interface_passivation_reduces_nonradiative_loss,
    reason="Diffusion-length improvement supplies an independent device-physics consequence.",
)
ind_pass_dmdp = induction(
    ind_pass_diffusion,
    s_law_pass_dmdp,
    law=law_interface_passivation_reduces_nonradiative_loss,
    reason="DMDP adds independent dual-mechanism passivation evidence.",
)
induction_interface_passivation = induction(
    ind_pass_dmdp,
    s_law_pass_dipolar,
    law=law_interface_passivation_reduces_nonradiative_loss,
    reason="Dipolar buried-interface passivation adds an independent tandem-interface test.",
)


law_stability_needs_phase_and_interface_control = claim(
    "Durable perovskite devices require coupled phase stabilization and interface "
    "protection against moisture, oxygen, heat, and ion migration.",
    title="Stability needs phase and interface control",
)

s_law_stab_phase = support(
    [law_stability_needs_phase_and_interface_control],
    pvsk2015_phase_stabilization,
    reason="The law predicts mixed-cation phase stabilization.",
    prior=0.82,
)
s_law_stab_triple = support(
    [law_stability_needs_phase_and_interface_control],
    pvsk_triple_cation_strategy,
    reason="The law predicts triple-cation stabilization as a bulk-composition route.",
    prior=0.84,
)
s_law_stab_2d3d = support(
    [law_stability_needs_phase_and_interface_control],
    pvsk2017_one_year_stability,
    reason="The law predicts one-year stability when 2D/3D interfaces protect the device.",
    prior=0.86,
)
s_law_stab_mda = support(
    [law_stability_needs_phase_and_interface_control],
    pvsk_mda_alpha_stabilization,
    reason="The law predicts alpha-phase stabilization by local chemical stabilization.",
    prior=0.82,
)
s_law_stab_damp_heat = support(
    [law_stability_needs_phase_and_interface_control],
    pvsk_damp_heat_t95,
    reason="The law predicts high damp-heat retention when dimensional passivation blocks degradation.",
    prior=0.88,
)
s_law_stab_ion = support(
    [law_stability_needs_phase_and_interface_control],
    pvsk_all_inorganic_ion_migration,
    reason="The law predicts improved stability when capping suppresses ion migration.",
    prior=0.85,
)

ind_stab_phase_triple = induction(
    s_law_stab_phase,
    s_law_stab_triple,
    law=law_stability_needs_phase_and_interface_control,
    reason="Mixed-cation and triple-cation evidence are independent composition tests.",
)
ind_stab_2d3d = induction(
    ind_stab_phase_triple,
    s_law_stab_2d3d,
    law=law_stability_needs_phase_and_interface_control,
    reason="2D/3D stability adds an independent interface-protection route.",
)
ind_stab_mda = induction(
    ind_stab_2d3d,
    s_law_stab_mda,
    law=law_stability_needs_phase_and_interface_control,
    reason="MDA alpha-phase stabilization adds another independent chemical route.",
)
ind_stab_damp_heat = induction(
    ind_stab_mda,
    s_law_stab_damp_heat,
    law=law_stability_needs_phase_and_interface_control,
    reason="Damp-heat retention adds an independent environmental-stress test.",
)
induction_stability_control = induction(
    ind_stab_damp_heat,
    s_law_stab_ion,
    law=law_stability_needs_phase_and_interface_control,
    reason="Ion-migration suppression adds an independent thermal-degradation mechanism.",
)


law_band_alignment_controls_charge_selectivity = claim(
    "Band alignment and interfacial electrostatics control charge selectivity, "
    "voltage loss, and tandem current extraction.",
    title="Band alignment controls charge selectivity",
)

s_law_band_2012 = support(
    [law_band_alignment_controls_charge_selectivity],
    pvsk2012_1_band_alignment,
    reason="The law predicts efficient charge separation in the 2012 solid-state device.",
    prior=0.84,
)
s_law_band_hole = support(
    [law_band_alignment_controls_charge_selectivity],
    pvsk2012_2_hole_transfer,
    reason="The law predicts effective hole transfer in the meso-superstructured device.",
    prior=0.82,
)
s_law_band_2d3d = support(
    [law_band_alignment_controls_charge_selectivity],
    pvsk2017_cb_upshift,
    reason="The law predicts band-edge shifts induced by 2D/3D grading.",
    prior=0.80,
)
s_law_band_3d3d = support(
    [law_band_alignment_controls_charge_selectivity],
    pvsk_3d3d_type2_alignment,
    reason="The law predicts type-II alignment in 3D/3D bilayer heterojunctions.",
    prior=0.86,
)
s_law_band_dipolar = support(
    [law_band_alignment_controls_charge_selectivity],
    pvsk_dipolar_type_ii_alignment,
    reason="The law predicts dipole-induced type-II energy alignment at buried interfaces.",
    prior=0.85,
)

ind_band_2012 = induction(
    s_law_band_2012,
    s_law_band_hole,
    law=law_band_alignment_controls_charge_selectivity,
    reason="The two 2012 packages test charge selectivity in different architectures.",
)
ind_band_2d3d = induction(
    ind_band_2012,
    s_law_band_2d3d,
    law=law_band_alignment_controls_charge_selectivity,
    reason="The 2017 2D/3D package adds an independent electrostatic alignment mechanism.",
)
ind_band_3d3d = induction(
    ind_band_2d3d,
    s_law_band_3d3d,
    law=law_band_alignment_controls_charge_selectivity,
    reason="The 3D/3D tandem package adds an independent type-II alignment test.",
)
induction_band_alignment = induction(
    ind_band_3d3d,
    s_law_band_dipolar,
    law=law_band_alignment_controls_charge_selectivity,
    reason="The dipolar package adds an independent buried-interface alignment test.",
)


law_tandems_raise_perovskite_efficiency_ceiling = claim(
    "Perovskite tandem architectures raise the practical efficiency ceiling by "
    "combining bandgap tunability with interface-selective charge extraction.",
    title="Tandems raise the perovskite efficiency ceiling",
)

s_law_tandem_all = support(
    [law_tandems_raise_perovskite_efficiency_ceiling],
    pvsk_all_tandem_certified,
    reason="The law predicts the certified all-perovskite tandem result.",
    prior=0.88,
)
s_law_tandem_3d3d = support(
    [law_tandems_raise_perovskite_efficiency_ceiling],
    pvsk_3d3d_tandem_champion,
    reason="The law predicts the 3D/3D tandem champion result.",
    prior=0.86,
)
s_law_tandem_persik = support(
    [law_tandems_raise_perovskite_efficiency_ceiling],
    pvsk_persik_2024_nrel_certified,
    reason="The law predicts the 2024 certified perovskite/silicon tandem record.",
    prior=0.90,
)
s_law_tandem_htl201 = support(
    [law_tandems_raise_perovskite_efficiency_ceiling],
    pvsk_htl201_certified,
    reason="The law predicts the 2025 HTL201 certified tandem record.",
    prior=0.91,
)
s_law_tandem_dipolar = support(
    [law_tandems_raise_perovskite_efficiency_ceiling],
    pvsk_dipolar_jet_certified,
    reason="The law predicts the certified dipolar-passivated tandem result.",
    prior=0.88,
)

ind_tandem_all_3d3d = induction(
    s_law_tandem_all,
    s_law_tandem_3d3d,
    law=law_tandems_raise_perovskite_efficiency_ceiling,
    reason="All-perovskite and 3D/3D tandem packages are independent tandem demonstrations.",
)
ind_tandem_persik = induction(
    ind_tandem_all_3d3d,
    s_law_tandem_persik,
    law=law_tandems_raise_perovskite_efficiency_ceiling,
    reason="Perovskite/silicon certification adds an independent tandem configuration.",
)
ind_tandem_htl201 = induction(
    ind_tandem_persik,
    s_law_tandem_htl201,
    law=law_tandems_raise_perovskite_efficiency_ceiling,
    reason="HTL201 adds an independent contact-engineering advance.",
)
induction_tandem_efficiency_ceiling = induction(
    ind_tandem_htl201,
    s_law_tandem_dipolar,
    law=law_tandems_raise_perovskite_efficiency_ceiling,
    reason="Dipolar passivation adds an independent buried-interface tandem advance.",
)


law_scalable_deposition_can_preserve_device_quality = claim(
    "Scalable deposition and module fabrication can preserve perovskite device "
    "quality when film formation and interface passivation are co-optimized.",
    title="Scalable deposition can preserve device quality",
)

s_law_scale_seq = support(
    [law_scalable_deposition_can_preserve_device_quality],
    pvsk2013_sequential_deposition,
    reason="The law predicts sequential deposition as a scalable film-control route.",
    prior=0.80,
)
s_law_scale_vapour = support(
    [law_scalable_deposition_can_preserve_device_quality],
    pvsknature12509_vapour_deposition,
    reason="The law predicts vapour deposition as a uniform-film route.",
    prior=0.80,
)
s_law_scale_r2r = support(
    [law_scalable_deposition_can_preserve_device_quality],
    pvsk_r2r_cells,
    reason="The law predicts fully roll-to-roll cells when scalable coating preserves film quality.",
    prior=0.84,
)
s_law_scale_bifacial = support(
    [law_scalable_deposition_can_preserve_device_quality],
    pvsk_bifacial_nrel_front,
    reason="The law predicts certified bifacial minimodule performance after module-scale integration.",
    prior=0.82,
)
s_law_scale_homogeneous = support(
    [law_scalable_deposition_can_preserve_device_quality],
    pvsk_homogeneous_2d_large_module,
    reason="The law predicts large-module performance when homogeneous 2D passivation is maintained.",
    prior=0.82,
)

ind_scale_seq_vapour = induction(
    s_law_scale_seq,
    s_law_scale_vapour,
    law=law_scalable_deposition_can_preserve_device_quality,
    reason="Sequential and vapour deposition are independent film-formation routes.",
)
ind_scale_r2r = induction(
    ind_scale_seq_vapour,
    s_law_scale_r2r,
    law=law_scalable_deposition_can_preserve_device_quality,
    reason="Roll-to-roll processing adds an independent manufacturing route.",
)
ind_scale_bifacial = induction(
    ind_scale_r2r,
    s_law_scale_bifacial,
    law=law_scalable_deposition_can_preserve_device_quality,
    reason="Bifacial minimodules add an independent module-integration route.",
)
induction_scalable_deposition = induction(
    ind_scale_bifacial,
    s_law_scale_homogeneous,
    law=law_scalable_deposition_can_preserve_device_quality,
    reason="Homogeneous 2D large modules add an independent large-area passivation route.",
)


interface_control_reduces_recombination = claim(
    "Interface control reduces recombination when chemical, electrostatic, or "
    "dimensional interventions suppress defect-mediated non-radiative pathways.",
    title="Interface control reduces recombination",
)

strat_interface_control_reduces_recombination = support(
    [
        agreement_passivation_reduces_recombination,
        law_interface_passivation_reduces_nonradiative_loss,
        passivation_reduces_recombination_and_improves_voltage,
    ],
    interface_control_reduces_recombination,
    reason=(
        "Agreement, induction, and voltage/recombination-normalized evidence all "
        "converge on interface control as the recombination lever."
    ),
    prior=0.86,
)


interface_control_improves_charge_selectivity = claim(
    "Interface control improves charge selectivity when energy alignment, dipoles, "
    "and contact chemistry favor extraction of one carrier while suppressing "
    "recombination of the other.",
    title="Interface control improves charge selectivity",
)

strat_interface_control_improves_charge_selectivity = support(
    [
        law_band_alignment_controls_charge_selectivity,
        pvsk_dipolar_charge_extraction,
        pvsk_htl201_voc_ff,
    ],
    interface_control_improves_charge_selectivity,
    reason=(
        "Band-alignment induction, dipolar extraction, and HTL201 Voc/FF gains "
        "connect interface chemistry to selective transport."
    ),
    prior=0.80,
)


passivation_reduces_nonradiative_loss = claim(
    "Passivation reduces nonradiative loss across PVSK packages, but the useful "
    "mechanism is loss reduction at electrically active defects rather than an "
    "unqualified improvement from any surface layer.",
    title="Passivation reduces nonradiative loss",
)

strat_passivation_reduces_nonradiative_loss = support(
    [
        law_interface_passivation_reduces_nonradiative_loss,
        interface_control_reduces_recombination,
        agreement_passivation_reduces_recombination,
    ],
    passivation_reduces_nonradiative_loss,
    reason=(
        "The shared mechanism is supported by both the induction law and the "
        "cross-paper agreement cluster."
    ),
    prior=0.86,
)


passivation_can_introduce_transport_barriers = claim(
    "Passivation can introduce transport barriers when the passivating species "
    "decouples the absorber from the contact or creates an overly resistive "
    "interlayer.",
    title="Passivation can introduce transport barriers",
)

strat_passivation_can_introduce_transport_barriers = support(
    [
        passivation_may_hurt_ff_if_it_blocks_extraction,
        pvsk_dmdp_dual_concept,
    ],
    passivation_can_introduce_transport_barriers,
    reason=(
        "The transport penalty is modeled explicitly, while dual-passivation "
        "evidence shows why a single barrier-like layer can be insufficient."
    ),
    prior=0.77,
)


passivation_benefit_is_conditioned_on_preserved_charge_extraction = claim(
    "Passivation benefit is conditioned on preserved charge extraction: a useful "
    "passivation layer must reduce defects while maintaining selective transport.",
    title="Passivation benefit is conditioned on charge extraction",
)

strat_passivation_benefit_is_conditioned_on_preserved_charge_extraction = support(
    [
        passivation_reduces_nonradiative_loss,
        passivation_can_introduce_transport_barriers,
        effective_passivation_requires_defect_reduction_without_transport_penalty,
        interface_control_improves_charge_selectivity,
    ],
    passivation_benefit_is_conditioned_on_preserved_charge_extraction,
    reason=(
        "The node combines the positive recombination mechanism with the transport "
        "limitation, preventing the graph from treating passivation as one-way good."
    ),
    prior=0.78,
)


ion_migration_links_hysteresis_and_stability = claim(
    "Ion migration links hysteresis and stability because mobile ionic defects can "
    "produce scan-history-dependent fields and also accelerate thermal or "
    "operational degradation.",
    title="Ion migration links hysteresis and stability",
)

strat_ion_migration_links_hysteresis_and_stability = support(
    [
        ion_migration_axis,
        ion_migration_contributes_to_hysteresis,
        law_stability_needs_phase_and_interface_control,
        hysteresis_suppression_does_not_identify_single_microscopic_cause,
    ],
    ion_migration_links_hysteresis_and_stability,
    reason=(
        "Ion migration appears in both stability evidence axes and hysteresis "
        "tension nodes, creating a shared bottleneck rather than two isolated topics."
    ),
    prior=0.78,
)


dimensional_interfaces_combine_defect_passivation_and_barrier_protection = claim(
    "Dimensional interfaces combine defect passivation and barrier protection: the "
    "same 2D/3D or capping layer can reduce recombination while slowing moisture, "
    "oxygen, heat, or ion-driven degradation.",
    title="Dimensional interfaces combine passivation and barrier protection",
)

strat_dimensional_interfaces_combine_defect_passivation_and_barrier_protection = support(
    [
        agreement_dimensional_interfaces_improve_stability,
        interface_stability_axis,
        passivation_reduces_nonradiative_loss,
        pvsk_damp_heat_barrier,
    ],
    dimensional_interfaces_combine_defect_passivation_and_barrier_protection,
    reason=(
        "Dimensional-interface packages are not only passivation or only stability "
        "packages; their information gain comes from combining both mechanisms."
    ),
    prior=0.82,
)


bandgap_tunability_enables_current_matching = claim(
    "Bandgap tunability enables tandem current matching by adjusting perovskite "
    "subcell absorption to complement the partner cell rather than maximizing one "
    "single-junction metric.",
    title="Bandgap tunability enables current matching",
)

strat_bandgap_tunability_enables_current_matching = support(
    [
        pvsk_all_tandem_tunable_bandgap,
        pvsk_triple_cation_tunable_bandgap,
        pvsknature12509_tandem_potential,
    ],
    bandgap_tunability_enables_current_matching,
    reason=(
        "The tunable-bandgap and tandem-potential claims make current matching a "
        "reusable design axis."
    ),
    prior=0.82,
)


bandgap_contact_coupling_controls_voc_jsc_ff_tradeoff = claim(
    "Bandgap-contact coupling controls the Voc-Jsc-FF trade-off because absorber "
    "composition sets absorption and voltage potential while contacts determine "
    "selective extraction and fill-factor losses.",
    title="Bandgap-contact coupling controls Voc-Jsc-FF trade-off",
)

strat_bandgap_contact_coupling_controls_voc_jsc_ff_tradeoff = support(
    [
        law_band_alignment_controls_charge_selectivity,
        pvsk2015_bandgap_tradeoff,
        bandgap_tunability_enables_current_matching,
        pvsk_htl201_voc_ff,
        passivation_benefit_is_conditioned_on_preserved_charge_extraction,
    ],
    bandgap_contact_coupling_controls_voc_jsc_ff_tradeoff,
    reason=(
        "The trade-off space is jointly controlled by composition, band alignment, "
        "charge extraction, and contact/passivation losses."
    ),
    prior=0.78,
)


low_loss_recombination_or_contact_layers_are_required = claim(
    "Low-loss recombination or contact layers are required for tandem performance "
    "because stacked subcells only help when interconnects and contacts preserve "
    "voltage and fill factor.",
    title="Low-loss recombination or contact layers are required",
)

strat_low_loss_recombination_or_contact_layers_are_required = support(
    [
        pvsk_all_tandem_passivation_route,
        pvsk_all_tandem_deep_states,
        pvsk_htl201_voc_ff,
        pvsk_dipolar_charge_extraction,
    ],
    low_loss_recombination_or_contact_layers_are_required,
    reason=(
        "Grain-surface passivation, deep-state removal, HTL201 contacts, and "
        "dipolar extraction all identify low-loss interfaces as tandem bottlenecks."
    ),
    prior=0.84,
)


passivation_improves_tandem_voltage_retention = claim(
    "Passivation improves tandem voltage retention when it removes deep states and "
    "buried-interface recombination without sacrificing charge extraction.",
    title="Passivation improves tandem voltage retention",
)

strat_passivation_improves_tandem_voltage_retention = support(
    [
        passivation_reduces_nonradiative_loss,
        pvsk_dipolar_tandem_performance,
        pvsk_dmdp_tandem_pce,
        pvsk_htl201_voc_ff,
    ],
    passivation_improves_tandem_voltage_retention,
    reason=(
        "The tandem packages connect passivation to voltage and certified tandem "
        "output through the same recombination-control mechanism."
    ),
    prior=0.80,
)


tandem_performance_requires_bandgap_matching_and_low_loss_contacts = claim(
    "Tandem performance requires both bandgap matching and low-loss contacts; "
    "stacking alone is not sufficient to raise certified output.",
    title="Tandem performance requires bandgap matching and low-loss contacts",
)

strat_tandem_performance_requires_bandgap_matching_and_low_loss_contacts = support(
    [
        law_tandems_raise_perovskite_efficiency_ceiling,
        bandgap_tunability_enables_current_matching,
        low_loss_recombination_or_contact_layers_are_required,
        bandgap_contact_coupling_controls_voc_jsc_ff_tradeoff,
    ],
    tandem_performance_requires_bandgap_matching_and_low_loss_contacts,
    reason=(
        "The tandem law is refined by its necessary conditions: matched absorption "
        "and low-loss charge extraction."
    ),
    prior=0.82,
)


tandem_record_efficiency_depends_on_interface_contact_engineering = claim(
    "Tandem record efficiency depends on interface and contact engineering, "
    "including type-II alignment, passivation, and selective low-loss transport "
    "layers.",
    title="Tandem records depend on interface-contact engineering",
)

strat_tandem_record_efficiency_depends_on_interface_contact_engineering = support(
    [
        tandem_performance_requires_bandgap_matching_and_low_loss_contacts,
        passivation_improves_tandem_voltage_retention,
        pvsk_3d3d_type_ii_mechanism,
        pvsk_persik_2024_sq_limit,
        pvsk_htl201_certified,
        pvsk_dipolar_jet_certified,
    ],
    tandem_record_efficiency_depends_on_interface_contact_engineering,
    reason=(
        "The record sequence is interpreted through the shared interface-contact "
        "mechanism instead of as independent champion-cell facts."
    ),
    prior=0.83,
)


scalable_manufacturing_requires_uniformity_yield_and_encapsulation = claim(
    "Scalable manufacturing requires uniformity, yield, and encapsulation: "
    "coating a working device is not equivalent to demonstrating deployment-ready "
    "production.",
    title="Scalable manufacturing requires uniformity, yield, and encapsulation",
)

strat_scalable_manufacturing_requires_uniformity_yield_and_encapsulation = support(
    [
        law_scalable_deposition_can_preserve_device_quality,
        module_yield_and_reproducibility,
        area_normalized_performance,
        encapsulation_and_lifetime_requirements,
    ],
    scalable_manufacturing_requires_uniformity_yield_and_encapsulation,
    reason=(
        "The manufacturing mechanism is deliberately routed through normalized "
        "area, yield, and lifetime evidence instead of direct paper-to-conclusion "
        "support."
    ),
    prior=0.74,
)


tandem_deployment_still_depends_on_scalable_stability = claim(
    "Tandem deployment still depends on scalable stability: certified high "
    "efficiency is only an industrial pathway if large-area fabrication and "
    "retained operation survive the tandem stack.",
    title="Tandem deployment still depends on scalable stability",
)

strat_tandem_deployment_still_depends_on_scalable_stability = support(
    [
        tandem_record_efficiency_depends_on_interface_contact_engineering,
        operational_stability_axis,
        scalable_manufacturing_requires_uniformity_yield_and_encapsulation,
        pvsk_all_tandem_large_area,
        pvsk_all_tandem_operational_600h,
    ],
    tandem_deployment_still_depends_on_scalable_stability,
    reason=(
        "The condition keeps high-efficiency tandem records connected to module "
        "area and stability constraints."
    ),
    prior=0.70,
)


deployment_value_requires_efficiency_stability_and_area_scaling = claim(
    "Deployment value requires efficiency, stability, and area scaling to hold "
    "together; module value is not established by any one of these axes alone.",
    title="Deployment value requires efficiency, stability, and area scaling",
)

strat_deployment_value_requires_efficiency_stability_and_area_scaling = support(
    [
        certification_status_normalized,
        operational_stability_axis,
        area_normalized_performance,
        scalable_manufacturing_requires_uniformity_yield_and_encapsulation,
    ],
    deployment_value_requires_efficiency_stability_and_area_scaling,
    reason=(
        "The deployment node is a shared bottleneck connecting efficiency records, "
        "module area, and lifetime conditions before final industrial conclusions."
    ),
    prior=0.74,
)


sustained_improvement_comes_from_reusable_design_axes = claim(
    "Sustained technical improvement comes from reusable design axes: composition "
    "control, interface passivation, bandgap-contact engineering, dimensional "
    "interfaces, and scalable processing can be iterated across packages.",
    title="Sustained improvement comes from reusable design axes",
)

strat_sustained_improvement_comes_from_reusable_design_axes = support(
    [
        agreement_phase_and_composition_control_matter,
        passivation_benefit_is_conditioned_on_preserved_charge_extraction,
        bandgap_contact_coupling_controls_voc_jsc_ff_tradeoff,
        dimensional_interfaces_combine_defect_passivation_and_barrier_protection,
        scalable_manufacturing_requires_uniformity_yield_and_encapsulation,
    ],
    sustained_improvement_comes_from_reusable_design_axes,
    reason=(
        "The node captures reusable technical axes rather than environmental "
        "lifecycle sustainability, and it links performance, stability, hysteresis, "
        "and manufacturability mechanisms."
    ),
    prior=0.74,
)
