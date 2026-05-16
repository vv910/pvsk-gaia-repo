# Module: motivation

### bifacial_gain_background

**QID:** `github:pvsks41560_023_01254_3::bifacial_gain_background`
**Type:** claim
**Role:** independent
**Content:** Bifacial silicon solar modules harvesting reflected and diffused rear-side sunlight produce 5% to over 30% more power output than monofacial modules, depending on albedo and installation conditions such as height and density of solar panels [@Gu2023].
**Prior:** 0.85
**Belief:** 0.87
**prior:** 0.85
**prior_justification:** Well-established knowledge about bifacial silicon solar cell advantage, supported by extensive literature.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::bifacial_gain_percentage`

### average_albedo_recorded

**QID:** `github:pvsks41560_023_01254_3::average_albedo_recorded`
**Type:** claim
**Role:** orphaned
**Content:** An average ground-surface albedo of 0.2 or higher has been recorded in many geographic locations, determining the amount of extra radiation gain for bifacial modules [@Gu2023].
**Prior:** 0.85
**Belief:** 0.85
**prior:** 0.85
**prior_justification:** Literature-supported albedo values from multiple geographic locations.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}

### perovskite_bifacial_challenge

**QID:** `github:pvsks41560_023_01254_3::perovskite_bifacial_challenge`
**Type:** claim
**Role:** orphaned
**Content:** Critical challenges for achieving high-efficiency large-area bifacial perovskite solar modules include increased resistive loss from the rear semitransparent electrode and insufficient absorption of long wavelength light due to the absence of reflective metal electrodes [@Gu2023].
**Prior:** 0.90
**Belief:** 0.90
**prior:** 0.9
**prior_justification:** Literature-supported description of challenges common to bifacial perovskite development.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}

### research_objective

**QID:** `github:pvsks41560_023_01254_3::research_objective`
**Type:** claim
**Role:** derived
**Content:** This work demonstrates perovskite bifacial minimodules with both record high efficiency and stability, achieving front efficiency comparable to the best monofacial minimodules while gaining additional energy from albedo light [@Gu2023].
**Prior:** 0.90
**Belief:** 0.98
**Derived from:** support
**Premises:** `github:pvsks41560_023_01254_3::ff_improvement_with_ag_grid`, `github:pvsks41560_023_01254_3::ff_improvement_tpfb`, `github:pvsks41560_023_01254_3::front_pce_improvement_with_np`, `github:pvsks41560_023_01254_3::bifacial_gain_percentage`, `github:pvsks41560_023_01254_3::pgd_by_albedo`, `github:pvsks41560_023_01254_3::initial_pce_retention_6000h`
**prior:** 0.9
**prior_justification:** Clear statement of research intent with quantitative targets and achieved outcomes.
**gaia:** {'provenance': {'cited_refs': ['Gu2023'], 'referenced_claims': ['bifacial_gain_percentage', 'ff_improvement_tpfb', 'ff_improvement_with_ag_grid', 'front_pce_improvement_with_np', 'initial_pce_retention_6000h', 'pgd_by_albedo', 'research_objective']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::power_generation_density_measurement`

### front_efficiency_record

**QID:** `github:pvsks41560_023_01254_3::front_efficiency_record`
**Type:** claim
**Role:** derived
**Content:** The bifacial minimodules achieved a certified stabilized front efficiency of 19.2% and rear efficiency of 14.1%, with an aperture area of approximately 22.0 cm^2, comparable to the best certified monofacial minimodules [@Gu2023].
**Belief:** 0.97
**Derived from:** support
**Premises:** `github:pvsks41560_023_01254_3::minimodule_front_aperture_efficiency`, `github:pvsks41560_023_01254_3::minimodule_rear_aperture_efficiency`
**Derived from:** support
**Premises:** `github:pvsks41560_023_01254_3::bifaciality_small_cell`, `github:pvsks41560_023_01254_3::minimodule_front_aperture_efficiency`, `github:pvsks41560_023_01254_3::nrel_certified_front_efficiency`, `github:pvsks41560_023_01254_3::pgd_by_albedo`, `github:pvsks41560_023_01254_3::initial_pce_retention_6000h`
**gaia:** {'provenance': {'cited_refs': ['Gu2023'], 'referenced_claims': ['bifaciality_small_cell', 'front_efficiency_record', 'initial_pce_retention_6000h', 'minimodule_front_aperture_efficiency', 'minimodule_rear_aperture_efficiency', 'nrel_certified_front_efficiency', 'pgd_by_albedo']}}

### stability_demonstrated

**QID:** `github:pvsks41560_023_01254_3::stability_demonstrated`
**Type:** claim
**Role:** derived
**Content:** The bifacial minimodule retained 97% of its initial power conversion efficiency after light soaking under 1-sun illumination for over 6,000 hours at 60 plus/minus 5 degrees C, demonstrating the most stable reported perovskite minimodule [@Gu2023].
**Belief:** 0.81
**Derived from:** support
**Premises:** `github:pvsks41560_023_01254_3::initial_pce_retention_6000h`, `github:pvsks41560_023_01254_3::ald_sno2_stabilization_benefit`, `github:pvsks41560_023_01254_3::stability_benefits_composition`
**gaia:** {'provenance': {'cited_refs': ['Gu2023'], 'referenced_claims': ['ald_sno2_stabilization_benefit', 'initial_pce_retention_6000h', 'stability_benefits_composition', 'stability_demonstrated']}}

### power_generation_density_measurement

**QID:** `github:pvsks41560_023_01254_3::power_generation_density_measurement`
**Type:** claim
**Role:** derived
**Content:** The small-area single-junction bifacial perovskite cells have a power-generation density of 26.4 mW/cm^2 under 1-sun illumination and an albedo of 0.2, exceeding any reported single-junction perovskite solar cells [@Gu2023].
**Belief:** 0.96
**Derived from:** support
**Premises:** `github:pvsks41560_023_01254_3::simulated_pgds_by_albedo`, `github:pvsks41560_023_01254_3::research_objective`
**Derived from:** support
**Premises:** `github:pvsks41560_023_01254_3::power_generation_density_albedo_02`, `github:pvsks41560_023_01254_3::pgd_by_albedo`
**gaia:** {'provenance': {'cited_refs': ['Gu2023'], 'referenced_claims': ['pgd_by_albedo', 'power_generation_density_albedo_02', 'power_generation_density_measurement', 'research_objective', 'simulated_pgds_by_albedo']}}

### bifaciality_measurement

**QID:** `github:pvsks41560_023_01254_3::bifaciality_measurement`
**Type:** claim
**Role:** orphaned
**Content:** The bifacial minimodules show a bifaciality of 74.3%, converting to a power-generation density of over 23 mW/cm^2 at an albedo of 0.2 under 1-sun front illumination [@Gu2023].
**Prior:** 0.85
**Belief:** 0.85
**prior:** 0.85
**prior_justification:** Bifaciality calculated from independently measured front and rear efficiencies.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}

### initial_efficiency_retention

**QID:** `github:pvsks41560_023_01254_3::initial_efficiency_retention`
**Type:** claim
**Role:** orphaned
**Content:** The bifacial minimodule retained 97% of its initial efficiency after 6,000 hours of light soaking under simulated 1-sun illumination in air at 60 plus/minus 5 degrees C from the front side [@Gu2023].
**Prior:** 0.90
**Belief:** 0.90
**prior:** 0.9
**prior_justification:** Direct measurement of efficiency retention over extended light soaking duration.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}
