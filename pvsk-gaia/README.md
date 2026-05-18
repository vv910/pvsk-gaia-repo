# PVSK Synthesis: Cross-Paper Reasoning Graph

> **Original corpus:** 22 Gaia knowledge packages formalizing perovskite solar-cell papers from the first organometal-halide sensitizer report through recent tandem, stability, passivation, bifacial-module, and roll-to-roll manufacturing results. Representative source works include Kojima et al., "Organometal Halide Perovskites as Visible-Light Sensitizers for Photovoltaic Cells," *Journal of the American Chemical Society* 131, 6050-6051 (2009), DOI: 10.1021/ja809598r; Kim et al., "Lead Iodide Perovskite Sensitized All-Solid-State Submicron Thin Film Mesoscopic Solar Cell with Efficiency Exceeding 9%," *Scientific Reports* 2, 591 (2012), DOI: 10.1038/srep00591; Lin et al., "All-perovskite tandem solar cells with improved grain surface passivation," *Nature* (2022), DOI: 10.1038/s41586-021-04372-8; Azmi et al., "Damp heat-stable perovskite solar cells with tailored-dimensionality 2D/3D heterojunctions," *Science* (2022), DOI: 10.1126/science.abm5784; Jia et al., "Efficient perovskite/silicon tandem with asymmetric self-assembly molecule," *Nature* (2025), DOI: 10.1038/s41586-025-09333-z; and Lin et al., "All-perovskite tandem solar cells with dipolar passivation," *Nature* (2025), DOI: 10.1038/s41586-025-09773-7.

> [!NOTE]
> This README is an AI-generated analysis based on a [Gaia](https://github.com/SiliconEinstein/Gaia) reasoning graph. Belief values reflect the graph's probabilistic assessment of support after importing the paper packages; they are not the original authors' confidence values.

## Summary

This synthesis package does not re-formalize the original PVSK papers. It imports the public claims exported by 22 paper-level Gaia packages and builds a cross-package reasoning graph over agreement, directed support, mechanism tensions, induction laws, and final synthesis conclusions. The resulting graph supports perovskites as a validated photovoltaic platform across liquid, solid-state, planar, mesoporous, tandem, module, and roll-to-roll settings (belief 0.93). The strongest conclusions concern integrated stability control (0.97), interface-driven efficiency growth (0.96), bifacial module value (0.95), and tandem architectures as the main high-efficiency path (0.94); the most cautious conclusions are low-cost printable-contact deployment (0.79) and three-way industrialization alignment (0.80), where manufacturing and cost evidence is still less mature.

> [!TIP]
> **Reasoning graph information gain: `0.8 bits`**
>
> Total mutual information between leaf premises and exported conclusions — measures how much the reasoning structure reduces uncertainty about the results.

```mermaid
---
config:
  flowchart:
    rankSpacing: 80
    nodeSpacing: 30
---
graph TB
    synthesis_perovskites_are_validated_pv_platform["★ Perovskites are a validated photovoltaic platform\n(0.50 → 0.93)"]:::exported
    synthesis_efficiency_progression_is_interface_driven["★ Efficiency progression is interface and architecture driven\n(0.50 → 0.96)"]:::exported
    synthesis_passivation_is_general_design_rule["★ Passivation is a general design rule\n(0.50 → 0.91)"]:::exported
    synthesis_stability_requires_integrated_control["★ Stability requires integrated control\n(0.50 → 0.97)"]:::exported
    synthesis_hysteresis_is_practically_suppressed["★ Hysteresis is practically suppressible\n(0.50 → 0.91)"]:::exported
    synthesis_bandgap_and_contact_engineering_define_tradeoff_space["★ Bandgap and contact engineering define the trade-off space\n(0.50 → 0.93)"]:::exported
    synthesis_tandems_are_primary_high_efficiency_path["★ Tandems are the primary high-efficiency path\n(0.50 → 0.94)"]:::exported
    synthesis_mechanistic_tensions_are_conditionally_resolved["★ Mechanistic tensions are conditionally resolved\n(0.50 → 0.85)"]:::exported
    synthesis_scalable_manufacturing_is_demonstrated["★ Scalable manufacturing is demonstrated across routes\n(0.50 → 0.81)"]:::exported
    synthesis_low_cost_path_depends_on_printable_contacts["★ Low-cost path depends on printable contacts\n(0.50 → 0.79)"]:::exported
    synthesis_bifacial_modules_add_system_value["★ Bifacial modules add system-level value\n(0.50 → 0.95)"]:::exported
    synthesis_industrialization_requires_three_way_alignment["★ Industrialization requires efficiency-stability-scale alignment\n(0.50 → 0.80)"]:::exported
    solid_state_dramatically_improved_stability["Solid-state configuration dramatically improves stability\n(0.50 → 0.86)"]:::premise
    sequential_deposition_introduced["Sequential deposition method introduced\n(0.50 → 0.99)"]:::premise
    bilayer_architecture["bilayer_architecture\n(0.50 → 0.77)"]:::premise
    certified_efficiency_162["Certified PCE of 16.2% under AM 1.5 G full sun\n(0.50 → 1.00)"]:::premise
    phase_stabilization_evidence["Evidence for perovskite phase stabilization\n(0.50 → 0.98)"]:::premise
    synergetic_effect["Synergetic effect of MA+ and Br- co-substitution\n(0.50 → 0.91)"]:::premise
    triple_cation_strategy["Triple cation Cs/MA/FA strategy\n(0.50 → 1.00)"]:::premise
    best_stabilized_pce["Best device achieves 21.1% stabilized PCE\n(0.50 → 0.95)"]:::premise
    one_year_stability_record["Record stability enables commercialization pathway\n(0.50 → 0.99)"]:::premise
    t95_after_1200_hours["T95 retention after >1200 hours damp-heat test\n(0.50 → 1.00)"]:::premise
    conclusion_alpha_stabilization["MDACl2 stabilizes alpha-FAPbI3 with high efficiency and stability\n(0.50 → 1.00)"]:::premise
    passivation_frustrates_ion_migration["2D capping layer passivates iodine vacancies, frustrates ion migration\n(0.50 → 1.00)"]:::premise
    formate_at_interfaces["Formate local environment at interfaces\n(0.50 → 0.91)"]:::premise
    non_radiative_recombination_reduction["Formate treatment reduces non-radiative recombination 5x\n(0.50 → 0.99)"]:::premise
    diffusion_length_increased_threefold["Diffusion length increased threefold with CF3-PA\n(0.50 → 1.00)"]:::premise
    cb_upshift_2d_3d["DFT predicts 0.14 eV CB upshift at interface\n(0.50 → 0.99)"]:::premise
    type_ii_energy_alignment["type_ii_energy_alignment\n(0.50 → 0.99)"]:::premise
    type_two_band_alignment["Type II band alignment at PHJ\n(0.50 → 1.00)"]:::premise
    certified_pce_264_percent["Certified PCE of 26.4% by JET\n(0.50 → 0.99)"]:::premise
    tandem_champion["Champion tandem device achieves 28.5% PCE\n(0.50 → 1.00)"]:::premise
    nrel_certified_pce["NREL certified 33.89% PCE\n(0.50 → 1.00)"]:::premise
    certified_pce_34_58["Certified PCE 34.58% by ESTI\n(0.50 → 1.00)"]:::premise
    htl201_strong_binding_perovskite["HTL201 has strongest binding to perovskite\n(0.50 → 0.86)"]:::premise
    htl201_passivates_pb_defects["HTL201 coordinates with Pb2+ to passivate defects\n(0.50 → 0.83)"]:::premise
    dipolar_passivation_strategy["dipolar_passivation_strategy\n(0.50 → 0.94)"]:::premise
    diffusion_length_enhancement["diffusion_length_enhancement\n(0.50 → 0.91)"]:::premise
    jet_certified_pce["jet_certified_pce\n(0.50 → 0.99)"]:::premise
    iecs_standard_met["IEC 61215:2016 damp-heat standard met\n(0.50 → 0.98)"]:::premise
    fabr_enables_uniform_n2["FABr enables uniform phase-pure n=2 2D formation\n(0.50 → 0.72)"]:::premise
    conclusion_perovskite_sensitization["Perovskite efficiently sensitizes TiO2 for visible-light conversion\n(0.50 → 0.92)"]:::premise
    panchromatic_absorption_leads_to_high_jsc["Panchromatic absorption enables high JSC\n(0.50 → 0.97)"]:::premise
    perovskite_semicondo["Perovskite as semiconductor\n(0.50 → 0.94)"]:::premise
    certified_efficiency["Certified PCE: 14.14%\n(0.50 → 0.53)"]:::premise
    deep_in_gap_states_eliminated["Deep in-gap states eliminated by CF3-PA\n(0.50 → 1.00)"]:::premise
    negligible_hysteresis_bilayer["Bilayer cell exhibits negligible hysteresis\n(0.50 → 0.87)"]:::premise
    first_fully_r2r_cells["First fully R2R-fabricated PeSCs with 15.5% PCE\n(0.50 → 0.89)"]:::premise
    first_fully_r2r_modules["First fully R2R-fabricated PeSC modules with 11% PCE\n(0.50 → 0.58)"]:::premise
    nrel_certified_front_efficiency["NREL certified stabilized front efficiency 19.2%\n(0.50 → 1.00)"]:::premise
    large_module_summary["Large module efficiencies (18.90% and 17.59%)\n(0.50 → 0.92)"]:::premise
    durability_observation["Photocurrent decay observed under continuous irradiation\n(0.50 → 0.73)"]:::premise
    stability_improvement["Excellent long-term stability demonstrated\n(0.50 → 0.94)"]:::premise
    hysteresis_origin["Hysteresis originates from large diffusion capacitance\n(0.50 → 0.77)"]:::premise
    hysteresis_observation["Hysteresis observed in HTM-free devices\n(0.50 → 0.53)"]:::premise
    diammonium_field_effect["Diammonium ligands provide field-effect passivation\n(0.50 → 0.77)"]:::premise
    methylthio_chemical_passivation["Methylthio molecules provide chemical passivation\n(0.50 → 0.77)"]:::premise
    passivation_tradeoff["Passivation-transport tradeoff\n(0.50 → 0.79)"]:::premise
    edai_ff_tradeoff["EDAI passivation-transport trade-off\n(0.50 → 0.47)"]:::premise
    bilayer_no_tradeoff["Bilayer overcomes trade-off\n(0.50 → 0.37)"]:::premise
    single_molecule_insufficient["Single molecule passivation insufficient\n(0.50 → 0.50)"]:::premise
    dual_passivation_concept["Bimolecular dual-passivation strategy concept\n(0.50 → 0.95)"]:::premise
    conventional_passivation_limitation["conventional_passivation_limitation\n(0.50 → 0.07)"]:::premise
    charge_separation_well_aligned["Band alignment favorable for charge separation\n(0.50 → 0.98)"]:::premise
    hole_transfer_effective["Hole transfer to spiro-OMeTAD\n(0.50 → 0.98)"]:::premise
    vapour_deposition_enables_uniform_films["Vapour deposition creates uniform films\n(0.50 → 0.97)"]:::premise
    bromide_cell_high_voltage["CH3NH3PbBr3 cell Voc 0.96 V\n(0.50 → 0.90)"]:::premise
    iodide_ipce_spectrum["CH3NH3PbI3 IPCE 45% with extended spectral range to 800 nm\n(0.50 → 0.91)"]:::premise
    bandgap_tuning_tradeoff["Bandgap tuning creates performance tradeoff\n(0.50 → 0.72)"]:::premise
    carbon_electrode_replacement["Carbon ink replaces vacuum electrodes\n(0.50 → 0.75)"]:::premise
    cost_prediction["R2R PeSC manufacturing cost prediction\n(0.50 → 0.72)"]:::premise
    production_cost_power["Module production cost per peak watt\n(0.50 → 0.61)"]:::premise
    high_throughput_capability["High-throughput R2R fabrication and testing\n(0.50 → 0.86)"]:::premise
    bifacial_gain_percentage["15% bifacial power gain at albedo 0.2\n(0.50 → 0.91)"]:::premise
    power_generation_density_measurement["PGD of 26.4 mW/cm2 at albedo 0.2\n(0.50 → 0.97)"]:::premise
    strat_0(["infer\n0.13 bits"]):::weak
    bromide_cell_high_voltage --> strat_0
    iodide_ipce_spectrum --> strat_0
    charge_separation_well_aligned --> strat_0
    hole_transfer_effective --> strat_0
    bandgap_tuning_tradeoff --> strat_0
    cb_upshift_2d_3d --> strat_0
    type_two_band_alignment --> strat_0
    type_ii_energy_alignment --> strat_0
    strat_0 --> synthesis_bandgap_and_contact_engineering_define_tradeoff_space
    strat_1(["infer\n0.06 bits"]):::weak
    conclusion_perovskite_sensitization --> strat_1
    panchromatic_absorption_leads_to_high_jsc --> strat_1
    solid_state_dramatically_improved_stability --> strat_1
    perovskite_semicondo --> strat_1
    certified_efficiency --> strat_1
    bilayer_architecture --> strat_1
    certified_efficiency_162 --> strat_1
    strat_1 --> synthesis_perovskites_are_validated_pv_platform
    strat_2(["infer"]):::weak
    durability_observation --> strat_2
    stability_improvement --> strat_2
    hysteresis_origin --> strat_2
    negligible_hysteresis_bilayer --> strat_2
    phase_stabilization_evidence --> strat_2
    synergetic_effect --> strat_2
    hysteresis_observation --> strat_2
    one_year_stability_record --> strat_2
    best_stabilized_pce --> strat_2
    triple_cation_strategy --> strat_2
    formate_at_interfaces --> strat_2
    non_radiative_recombination_reduction --> strat_2
    deep_in_gap_states_eliminated --> strat_2
    diffusion_length_increased_threefold --> strat_2
    bilayer_no_tradeoff --> strat_2
    edai_ff_tradeoff --> strat_2
    passivation_tradeoff --> strat_2
    htl201_passivates_pb_defects --> strat_2
    htl201_strong_binding_perovskite --> strat_2
    dipolar_passivation_strategy --> strat_2
    conclusion_alpha_stabilization --> strat_2
    t95_after_1200_hours --> strat_2
    passivation_frustrates_ion_migration --> strat_2
    diammonium_field_effect --> strat_2
    dual_passivation_concept --> strat_2
    methylthio_chemical_passivation --> strat_2
    single_molecule_insufficient --> strat_2
    strat_2 --> synthesis_mechanistic_tensions_are_conditionally_resolved
    strat_3(["infer"]):::weak
    charge_separation_well_aligned --> strat_3
    hole_transfer_effective --> strat_3
    cb_upshift_2d_3d --> strat_3
    formate_at_interfaces --> strat_3
    non_radiative_recombination_reduction --> strat_3
    certified_pce_264_percent --> strat_3
    deep_in_gap_states_eliminated --> strat_3
    diffusion_length_increased_threefold --> strat_3
    tandem_champion --> strat_3
    type_two_band_alignment --> strat_3
    nrel_certified_pce --> strat_3
    certified_pce_34_58 --> strat_3
    htl201_passivates_pb_defects --> strat_3
    htl201_strong_binding_perovskite --> strat_3
    conventional_passivation_limitation --> strat_3
    diffusion_length_enhancement --> strat_3
    dipolar_passivation_strategy --> strat_3
    jet_certified_pce --> strat_3
    type_ii_energy_alignment --> strat_3
    dual_passivation_concept --> strat_3
    strat_3 --> synthesis_tandems_are_primary_high_efficiency_path
    strat_4(["infer\n0.26 bits"]):::weak
    sequential_deposition_introduced --> strat_4
    vapour_deposition_enables_uniform_films --> strat_4
    first_fully_r2r_cells --> strat_4
    bifacial_gain_percentage --> strat_4
    nrel_certified_front_efficiency --> strat_4
    power_generation_density_measurement --> strat_4
    large_module_summary --> strat_4
    iecs_standard_met --> strat_4
    strat_4 --> synthesis_bifacial_modules_add_system_value
    strat_5(["infer"]):::weak
    sequential_deposition_introduced --> strat_5
    phase_stabilization_evidence --> strat_5
    synergetic_effect --> strat_5
    one_year_stability_record --> strat_5
    best_stabilized_pce --> strat_5
    triple_cation_strategy --> strat_5
    vapour_deposition_enables_uniform_films --> strat_5
    first_fully_r2r_cells --> strat_5
    nrel_certified_front_efficiency --> strat_5
    large_module_summary --> strat_5
    formate_at_interfaces --> strat_5
    non_radiative_recombination_reduction --> strat_5
    certified_pce_264_percent --> strat_5
    deep_in_gap_states_eliminated --> strat_5
    diffusion_length_increased_threefold --> strat_5
    tandem_champion --> strat_5
    nrel_certified_pce --> strat_5
    certified_pce_34_58 --> strat_5
    htl201_passivates_pb_defects --> strat_5
    htl201_strong_binding_perovskite --> strat_5
    diffusion_length_enhancement --> strat_5
    dipolar_passivation_strategy --> strat_5
    jet_certified_pce --> strat_5
    conclusion_alpha_stabilization --> strat_5
    iecs_standard_met --> strat_5
    t95_after_1200_hours --> strat_5
    passivation_frustrates_ion_migration --> strat_5
    dual_passivation_concept --> strat_5
    strat_5 --> synthesis_industrialization_requires_three_way_alignment
    strat_6(["infer\n0.11 bits"]):::weak
    sequential_deposition_introduced --> strat_6
    vapour_deposition_enables_uniform_films --> strat_6
    first_fully_r2r_cells --> strat_6
    first_fully_r2r_modules --> strat_6
    nrel_certified_front_efficiency --> strat_6
    large_module_summary --> strat_6
    strat_6 --> synthesis_scalable_manufacturing_is_demonstrated
    strat_7(["infer"]):::weak
    hysteresis_origin --> strat_7
    negligible_hysteresis_bilayer --> strat_7
    phase_stabilization_evidence --> strat_7
    synergetic_effect --> strat_7
    hysteresis_observation --> strat_7
    one_year_stability_record --> strat_7
    best_stabilized_pce --> strat_7
    triple_cation_strategy --> strat_7
    formate_at_interfaces --> strat_7
    non_radiative_recombination_reduction --> strat_7
    deep_in_gap_states_eliminated --> strat_7
    diffusion_length_increased_threefold --> strat_7
    htl201_passivates_pb_defects --> strat_7
    htl201_strong_binding_perovskite --> strat_7
    dipolar_passivation_strategy --> strat_7
    conclusion_alpha_stabilization --> strat_7
    t95_after_1200_hours --> strat_7
    passivation_frustrates_ion_migration --> strat_7
    dual_passivation_concept --> strat_7
    strat_7 --> synthesis_hysteresis_is_practically_suppressed
    strat_8(["infer"]):::weak
    phase_stabilization_evidence --> strat_8
    synergetic_effect --> strat_8
    one_year_stability_record --> strat_8
    best_stabilized_pce --> strat_8
    triple_cation_strategy --> strat_8
    formate_at_interfaces --> strat_8
    non_radiative_recombination_reduction --> strat_8
    certified_pce_264_percent --> strat_8
    deep_in_gap_states_eliminated --> strat_8
    diffusion_length_increased_threefold --> strat_8
    tandem_champion --> strat_8
    nrel_certified_pce --> strat_8
    certified_pce_34_58 --> strat_8
    htl201_passivates_pb_defects --> strat_8
    htl201_strong_binding_perovskite --> strat_8
    diffusion_length_enhancement --> strat_8
    dipolar_passivation_strategy --> strat_8
    jet_certified_pce --> strat_8
    conclusion_alpha_stabilization --> strat_8
    t95_after_1200_hours --> strat_8
    passivation_frustrates_ion_migration --> strat_8
    dual_passivation_concept --> strat_8
    strat_8 --> synthesis_efficiency_progression_is_interface_driven
    strat_9(["infer"]):::weak
    phase_stabilization_evidence --> strat_9
    synergetic_effect --> strat_9
    one_year_stability_record --> strat_9
    best_stabilized_pce --> strat_9
    triple_cation_strategy --> strat_9
    formate_at_interfaces --> strat_9
    non_radiative_recombination_reduction --> strat_9
    deep_in_gap_states_eliminated --> strat_9
    diffusion_length_increased_threefold --> strat_9
    bilayer_no_tradeoff --> strat_9
    edai_ff_tradeoff --> strat_9
    passivation_tradeoff --> strat_9
    htl201_passivates_pb_defects --> strat_9
    htl201_strong_binding_perovskite --> strat_9
    dipolar_passivation_strategy --> strat_9
    conclusion_alpha_stabilization --> strat_9
    t95_after_1200_hours --> strat_9
    passivation_frustrates_ion_migration --> strat_9
    diammonium_field_effect --> strat_9
    dual_passivation_concept --> strat_9
    methylthio_chemical_passivation --> strat_9
    single_molecule_insufficient --> strat_9
    strat_9 --> synthesis_passivation_is_general_design_rule
    strat_10(["infer\n0.02 bits"]):::weak
    phase_stabilization_evidence --> strat_10
    synergetic_effect --> strat_10
    one_year_stability_record --> strat_10
    best_stabilized_pce --> strat_10
    triple_cation_strategy --> strat_10
    conclusion_alpha_stabilization --> strat_10
    t95_after_1200_hours --> strat_10
    passivation_frustrates_ion_migration --> strat_10
    strat_10 --> synthesis_stability_requires_integrated_control
    strat_11(["infer\n0.24 bits"]):::weak
    carbon_electrode_replacement --> strat_11
    cost_prediction --> strat_11
    high_throughput_capability --> strat_11
    production_cost_power --> strat_11
    fabr_enables_uniform_n2 --> strat_11
    strat_11 --> synthesis_low_cost_path_depends_on_printable_contacts

    classDef premise fill:#ddeeff,stroke:#4488bb,color:#333
    classDef exported fill:#d4edda,stroke:#28a745,stroke-width:2px,color:#333
    classDef weak fill:#fff9c4,stroke:#f9a825,stroke-dasharray: 5 5,color:#333
    classDef contra fill:#ffebee,stroke:#c62828,color:#333
```

> [!NOTE]
> **[Per-module reasoning details ->](docs/detailed-reasoning.md)**
>
> The detailed documentation is generated from the same Gaia graph and provides a module-level audit trail for claims, dependencies, and inferred beliefs.

## Source Corpus

The imported package set covers early sensitizer and solid-state demonstrations, solution and vapour deposition, solvent/composition engineering, 2D/3D interface stabilization, pseudo-halide and molecular passivation, all-perovskite and perovskite/silicon tandems, bifacial minimodules, homogeneous large modules, and roll-to-roll manufacturing. The synthesis layer imports each dependency package through its top-level `__all__` boundary and adds only cross-paper reasoning. Intermediate agreement, tension, and induction claims remain public inside the package, while only final synthesis conclusions are exported from `pvsk.__all__`.

## Reasoning Structure

### Perovskites are a validated photovoltaic platform (belief: 0.93)

This conclusion says that perovskite photovoltaics are no longer supported by one narrow cell architecture. The evidence spans the 2009 visible-light sensitizer result, the 2012 solid-state panchromatic device, meso-superstructured and planar devices, certified bilayer cells, later tandem records, and scalable module demonstrations. The key scientific point is that later progress modifies interfaces, contacts, composition, and device stack design while preserving the same absorber-level platform.

**Evidence support:**
- **Cross-architecture absorber agreement** (weakest link, belief 0.91): Early sensitizer, solid-state, meso-superstructured, and certified bilayer packages converge on absorber validity. The residual risk is that the agreement is broad and abstracts away device-specific failure modes.
- **Induced absorber law** (belief 0.91): Independent observations support a law that perovskite absorbers work across liquid, solid-state, mesoporous, planar, and tandem settings when interfaces are controlled.
- **Solid-state architecture evidence** (belief 0.76): This is the weakest supporting route because it compresses several early architecture changes into one claim, so it is less diagnostic about which design element matters most.

**Verdict:** Well supported as a platform-level conclusion. The remaining risk is not absorber validity, but whether each new architecture can satisfy stability and manufacturing constraints at the same time.

### Efficiency progression is driven by interfaces and architecture (belief: 0.96)

The graph reads the historical efficiency increase as a sequence of interface, architecture, composition, and contact-engineering gains rather than a replacement of the basic absorber concept. Key examples include the early move to solid-state hole transport, sequential and vapour deposition for film control, mixed-cation phase stabilization, passivation that reduces non-radiative recombination, and recent selective-contact improvements such as HTL201 certified tandem performance.

**Evidence support:**
- **Composition plus passivation chain** (weakest link, belief 0.93): Composition and phase control repeatedly enable high performance, while passivation reduces recombination. The link is strong, but it combines bulk and interface mechanisms that are experimentally separated only in some packages.
- **HTL201 contact evidence** (belief near 1.00): The certified 34.58% perovskite/silicon tandem result supplies a later contact-engineering check.
- **Architecture agreement** (belief 0.76): Early solid-state and controlled architectures support the trend, but this route is less precise because many design changes happen together.

**Verdict:** Strongly supported. The main scientific risk is over-attributing efficiency progress to a single class of interfaces when high-performing devices often improve film formation, bulk composition, and contacts simultaneously.

### Passivation is a general PVSK design rule (belief: 0.91)

Passivation appears in the graph as a general design rule rather than one specific molecule or surface treatment. Formate, grain-surface CF3-PA, tailored-dimensionality 2D/3D interfaces, bimolecular passivation, and dipolar buried interfaces all support the same practical claim: reducing recombination-active defects improves device performance when charge extraction is not blocked.

**Evidence support:**
- **Passivation-recombination agreement** (belief 0.94): Multiple packages connect passivation to reduced non-radiative recombination or improved device signatures.
- **Interface passivation law** (belief 0.95): Independent observations induce a broader law covering grain surfaces, buried interfaces, and dimensional heterointerfaces.
- **Passivation-transport tension** (weakest link, belief 0.61): This is the vulnerable link because some passivators improve voltage while harming fill factor; the general rule only holds when passivation geometry preserves transport.

**Verdict:** Well supported, but conditional. Passivation is not automatically beneficial; the mechanism must suppress defects without adding an extraction barrier.

### Stability requires integrated phase, interface, and ion-control design (belief: 0.97)

The stability conclusion rejects a single universal stability mechanism. The graph combines mixed-cation and triple-cation phase stabilization, MDA-based alpha-FAPbI3 stabilization, 2D/3D interface protection, damp-heat stable dimensional heterojunctions, and all-inorganic capping that suppresses ion migration. These routes target different stressors: moisture, oxygen, heat, phase segregation, and mobile ions.

**Evidence support:**
- **Stability phase/interface law** (belief 0.98): The strongest route comes from repeated independent observations that durable devices need both phase and interface control.
- **Dimensional interface agreement** (belief 0.95): 2D/3D interfaces and capping layers repeatedly improve moisture, thermal, or operational stability.
- **Condition-specific stability tension** (belief 0.94): Different stability routes do not contradict each other; they are scoped to different degradation drivers.

**Verdict:** One of the strongest synthesis conclusions. The main risk is external validity under long-term outdoor field conditions, where combined stressors may exceed the individual tests captured by the packages.

### Hysteresis is practically suppressible, not fully reduced to one cause (belief: 0.91)

The graph treats current-density hysteresis as practically controllable while leaving its microscopic causes plural. Evidence from bilayer architecture, 2D/3D interface engineering, and buried-interface dipolar passivation supports practical suppression. At the same time, the tension node keeps ion migration, delayed polarization, and interface recombination as coexisting sources.

**Evidence support:**
- **Architecture-level suppression** (belief 0.86): Multiple packages show that design choices can reduce hysteresis to a practical level.
- **Multiple-source tension** (weakest link, belief 0.73): The weaker link is mechanistic specificity: several causal mechanisms can fit the observations, so this supports practical control better than universal explanation.

**Verdict:** Supported for engineering practice. It should not be read as a claim that one microscopic hysteresis mechanism has been settled.

### Bandgap and contact engineering define the PVSK trade-off space (belief: 0.93)

This conclusion links material bandgap tuning to contact selectivity. Iodide extends spectral response and current; bromide can raise voltage; mixed compositions tune the bandgap; and selective contacts control extraction and voltage loss. The graph therefore frames PVSK optimization as a coupled bandgap-contact problem rather than independent maximization of current, voltage, and fill factor.

**Evidence support:**
- **Halide and composition trade-off** (weakest link, belief 0.72): The material-side evidence is convincing but broad, and composition changes can also affect phase stability and transport.
- **Band-alignment law** (belief 0.97): Independent charge-selectivity observations support the contact side of the trade-off space.
- **Early iodide/bromide contrast** (beliefs 0.90 and 0.91): The 2009 halide contrast remains useful because it directly separates spectral range from voltage behavior.

**Verdict:** Strongly supported as a design-space statement. The vulnerable assumption is that bandgap and contact effects can be cleanly decomposed in heavily engineered modern stacks.

### Tandems are the primary high-efficiency path (belief: 0.94)

The graph identifies tandem architectures as the main path to the highest PVSK efficiencies. Evidence includes certified all-perovskite tandem performance, 3D/3D bilayer heterojunctions, perovskite/silicon records, HTL201 contact engineering, and dipolar-passivated tandem devices. The conclusion is not that stacking alone is sufficient; it depends on bandgap tunability and low-loss interfacial charge extraction.

**Evidence support:**
- **Tandem agreement** (belief 0.97): Multiple tandem packages independently raise the efficiency ceiling.
- **Tandem induction law** (belief 0.97): Independent tandem configurations support a general efficiency-ceiling law.
- **Buried-interface passivation tension** (weakest link, belief 0.60): The low belief reflects uncertainty about whether conventional and dipolar passivation evidence fully generalizes across tandem buried-interface conditions.

**Verdict:** Strongly supported for record-efficiency direction. The main risk is deployment relevance: tandem records must still align with stability and manufacturability.

### Mechanistic tensions are conditionally resolved (belief: 0.85)

The synthesis graph deliberately avoids treating most mechanism differences as hard contradictions. Liquid-electrolyte instability and solid-state stability are architecture-dependent; planar and mesoporous results depend on process route; passivation mechanisms can be complementary; and stability routes target different stress conditions. The conclusion is that many apparent conflicts reflect scope conditions rather than mutually exclusive laws.

**Evidence support:**
- **Architecture and stability tensions** (beliefs 0.82 and 0.94): Stability conflicts are resolved by device stack and stress condition.
- **Interface mechanism tensions** (weakest link, belief range 0.61-0.77): These are weaker because multiple mechanisms can reinforce each other, but the exact dominance of each mechanism is context-dependent.
- **No strict contradiction edge**: The graph does not use contradiction or complement for these relationships because the alternatives can coexist under different conditions.

**Verdict:** Moderately strong. The risk is that some local mechanisms may become mutually exclusive under narrower experimental definitions than this synthesis currently encodes.

### Scalable manufacturing is demonstrated across routes (belief: 0.81)

This conclusion aggregates evidence that perovskite device quality can survive several scale-up routes: sequential deposition, vapour deposition, fully roll-to-roll cells, roll-to-roll modules, bifacial minimodules, and homogeneous 2D large modules. The scientific claim is about demonstrated routes, not yet about universal manufacturing maturity.

**Evidence support:**
- **Scalable deposition law** (belief 0.90): Independent film-formation and module-integration observations support quality-preserving scale-up.
- **Multiple-route agreement** (weakest link, belief 0.72): The route diversity is real, but different packages measure different device sizes, certification levels, and stress conditions.
- **Concrete module evidence** (weakest imported link, first fully roll-to-roll modules belief 0.58): Roll-to-roll module evidence is important but still comparatively uncertain inside the imported graph.

**Verdict:** Supported as a demonstration claim, not as a claim of deployment-ready manufacturing.

### Low-cost deployment depends on printable contacts (belief: 0.79)

The low-cost path is tied to printable high-throughput processing and low-cost contacts, especially carbon electrodes that reduce reliance on noble-metal evaporation. Roll-to-roll best-cell performance supports technical feasibility, while cost prediction, production-cost-per-watt, and throughput claims support economic plausibility.

**Evidence support:**
- **Printable contact chain** (weakest link, carbon electrode replacement belief 0.75): Carbon replacement is promising but must maintain performance and stability across larger modules.
- **Cost and throughput chain** (weakest link, production cost per peak watt belief 0.61): Cost models are sensitive to assumptions about yield, encapsulation, lifetime, and throughput.
- **Best roll-to-roll cell performance** (belief 0.91): Device performance supports feasibility but does not by itself prove low cost.

**Verdict:** Plausible but the least certain exported conclusion. The largest risk is economic extrapolation from early manufacturing demonstrations.

### Bifacial modules add system-level value (belief: 0.95)

Bifacial perovskite modules contribute value by collecting rear-side reflected light and improving power generation density, so their value is not captured by front-side efficiency alone. The graph combines bifacial gain, power-density measurements, NREL-certified front efficiency, and long operation with high retained performance.

**Evidence support:**
- **Bifacial gain and power density** (weakest link, bifacial gain belief 0.91): Direct module-level measurements support the value claim.
- **Certification and operation** (beliefs near 1.00): NREL certification and 6000-hour retention support practical relevance.
- **System-value inference**: The inference from measured gain to deployment value depends on albedo and installation context, which are only partly represented in the graph.

**Verdict:** Strongly supported for module-level value under suitable deployment conditions. Site-specific irradiance and albedo remain the main external variables.

### Industrialization requires efficiency, stability, and scale at the same time (belief: 0.80)

This conclusion is intentionally conjunctive: industrialization requires record efficiency, stress-tested stability, and scalable manufacturing to align simultaneously. Evidence comes from tandem efficiency laws and certified records, stability laws and IEC damp-heat evidence, and scalable deposition plus roll-to-roll cell evidence.

**Evidence support:**
- **Efficiency axis** (beliefs 0.97 to near 1.00): Tandem records and certified contact-engineered devices strongly support the performance axis.
- **Stability axis** (beliefs 0.98 and 0.98): Phase/interface stability laws and IEC damp-heat evidence are strong.
- **Scale axis** (weakest link, first fully roll-to-roll cells belief 0.89; scalable manufacturing conclusion 0.81): Scale evidence is meaningful but not yet as mature as efficiency and stability evidence.

**Verdict:** Scientifically conservative and deployment-focused. The belief is lower than the individual efficiency or stability conclusions because all three axes must hold together.

## Conclusions

| Label | Content | Prior | Belief |
|-------|---------|-------|--------|
| synthesis_bandgap_and_contact_engineering_define_tradeoff_space | PVSK optimization is governed by a bandgap-contact trade-off space: iodide, b... | 0.50 | 0.93 |
| synthesis_bifacial_modules_add_system_value | Bifacial perovskite modules add system-level value because rear-side collecti... | 0.50 | 0.95 |
| synthesis_efficiency_progression_is_interface_driven | The long-run efficiency progression is best explained by interface, architect... | 0.50 | 0.96 |
| synthesis_hysteresis_is_practically_suppressed | Current-density hysteresis is not a single solved microscopic mechanism, but ... | 0.50 | 0.91 |
| synthesis_industrialization_requires_three_way_alignment | PVSK industrialization requires simultaneous alignment of record efficiency, ... | 0.50 | 0.80 |
| synthesis_low_cost_path_depends_on_printable_contacts | The low-cost PVSK path depends on printable high-throughput processing and lo... | 0.50 | 0.79 |
| synthesis_mechanistic_tensions_are_conditionally_resolved | The major apparent conflicts across PVSK papers are conditionally resolved: t... | 0.50 | 0.85 |
| synthesis_passivation_is_general_design_rule | Passivation is a general PVSK design rule: chemically bound passivators, fiel... | 0.50 | 0.91 |
| synthesis_perovskites_are_validated_pv_platform | The 22-package evidence base supports perovskite photovoltaics as a validated... | 0.50 | 0.93 |
| synthesis_scalable_manufacturing_is_demonstrated | PVSK scale-up is demonstrated at the synthesis level: roll-to-roll cells and ... | 0.50 | 0.81 |
| synthesis_stability_requires_integrated_control | Durable PVSK devices require integrated control of phase stability, dimension... | 0.50 | 0.97 |
| synthesis_tandems_are_primary_high_efficiency_path | Tandem architectures are the primary high-efficiency path for PVSK: their adv... | 0.50 | 0.94 |

## Weak Points

<details open>
<summary>Weak Points Analysis</summary>

The single weakest internal link is the low-cost manufacturing argument, especially production cost per peak watt (belief 0.61) and first fully roll-to-roll module performance (belief 0.58).

**Roll-to-roll module evidence is still early-stage.** The roll-to-roll cell claim is stronger than the module claim, but industrially relevant deployment depends on modules, yield, encapsulation, and repeatability. This affects scalable manufacturing and the industrialization conclusion. More independently certified large-area roll-to-roll modules with durability testing would most directly strengthen this link.

**Printable-contact cost evidence depends on model assumptions.** Carbon-electrode replacement is promising, but the cost pathway also depends on throughput, yield, lifetime, and avoided evaporation costs. The downstream low-cost conclusion inherits this uncertainty. A side-by-side techno-economic analysis using measured roll-to-roll yield and module lifetime would be more decisive than isolated device cost projections.

**Passivation mechanisms can be complementary but not automatically additive.** The passivation-transport tension remains moderate because voltage gains can come with fill-factor penalties. This affects the general passivation rule and the tandem-interface conclusions. Device studies that vary passivator geometry, dipole strength, and transport resistance independently would clarify when passivation helps rather than blocks extraction.

**Buried-interface passivation in tandems has a narrow evidence base.** The conventional-versus-dipolar buried-interface tension has low belief because it comes from a specialized tandem condition. It supports the claim that tandem records depend on contact design, but the exact boundary between conventional and dipolar approaches needs more independent replication.

**Imported claims without local priors remain a structural limitation.** This synthesis package cannot assign priors to foreign Knowledge objects from dependency packages. Depth-1 inference loads the dependency graphs, but `gaia check --brief` still lists foreign independent claims as holes inside the local package view. This does not invalidate the synthesis, but it makes dependency package prior quality important.

</details>

## Evidence Gaps

<details>
<summary>Evidence Gaps & Future Work</summary>

**Experimental gaps:** The largest missing evidence is field-relevant durability for modules and tandems under combined stress: heat, humidity, UV, bias, thermal cycling, and outdoor irradiance. Filling this gap would strengthen the stability, bifacial-value, scalable-manufacturing, and industrialization conclusions.

**Manufacturing gaps:** Roll-to-roll and large-module packages need more evidence on yield, batch-to-batch reproducibility, encapsulation, and certified module lifetime. This would most improve the scalable-manufacturing, low-cost, and industrialization conclusions.

**Economic gaps:** Cost claims depend on production-cost models that are sensitive to throughput, materials utilization, electrode lifetime, and module warranty assumptions. A shared techno-economic benchmark across carbon-electrode, vapour, sequential, and homogeneous-2D routes would reduce uncertainty in the low-cost path.

**Mechanistic gaps:** Passivation and hysteresis mechanisms are represented as conditionally resolved tensions, not settled universal mechanisms. Independent experiments that isolate ion migration, dipolar alignment, defect chemical bonding, and extraction resistance would sharpen the passivation, hysteresis, and tandem-contact conclusions.

**Cross-package consistency gaps:** The dependency packages use different experimental scales, certification bodies, stress tests, and reporting conventions. A normalized evidence layer for area, scan protocol, stabilized output, encapsulation, and stress condition would make future synthesis graphs more quantitative.

</details>

## Detailed Graph Artifacts

For generated per-module claim details, strategy reasons, and belief values, see [docs/detailed-reasoning.md](docs/detailed-reasoning.md).
