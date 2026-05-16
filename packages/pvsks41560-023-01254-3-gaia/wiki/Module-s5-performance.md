# Module: s5_performance

### small_cell_front_pce

**QID:** `github:pvsks41560_023_01254_3::small_cell_front_pce`
**Type:** claim
**Role:** independent
**Content:** The front power conversion efficiency of the champion small-size (8 mm^2) MA_0.7FA_0.3PbI_3 bifacial perovskite solar cell is comparable to optimized opaque PSCs with copper electrode, reaching approximately 20.2% [@Gu2023].
**Prior:** 0.90
**Belief:** 0.94
**prior:** 0.9
**prior_justification:** Directly measured experimental result from champion small cell with clear protocol.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::bifaciality_small_cell`

### small_cell_rear_pce

**QID:** `github:pvsks41560_023_01254_3::small_cell_rear_pce`
**Type:** claim
**Role:** independent
**Content:** The rear power conversion efficiency of the champion small-size bifacial perovskite solar cell reached 18.5%, giving a high bifaciality of approximately 80% [@Gu2023].
**Prior:** 0.90
**Belief:** 0.94
**prior:** 0.9
**prior_justification:** Directly measured experimental result from champion small cell with clear protocol.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::bifaciality_small_cell`

### bifaciality_small_cell

**QID:** `github:pvsks41560_023_01254_3::bifaciality_small_cell`
**Type:** claim
**Role:** derived
**Content:** The small-size bifacial perovskite solar cell achieved a bifaciality of approximately 80%, benefiting from both high front efficiency and rear efficiency of 18.5% [@Gu2023].
**Prior:** 0.90
**Belief:** 0.99
**Derived from:** support
**Premises:** `github:pvsks41560_023_01254_3::small_cell_front_pce`, `github:pvsks41560_023_01254_3::small_cell_rear_pce`
**prior:** 0.9
**prior_justification:** Calculated from directly measured front and rear efficiencies with clear method.
**gaia:** {'provenance': {'cited_refs': ['Gu2023'], 'referenced_claims': ['bifaciality_small_cell', 'small_cell_front_pce', 'small_cell_rear_pce']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::front_efficiency_record`

### power_generation_density_albedo_02

**QID:** `github:pvsks41560_023_01254_3::power_generation_density_albedo_02`
**Type:** claim
**Role:** independent
**Content:** The bifacial cell with aperture area of 8 mm^2 delivered an estimated power-generation density of 26.4 mW/cm^2 (PGD_front + albedo times PGD_rear) at an albedo of 0.2, better than any reported single-junction perovskite solar cells [@Gu2023].
**Prior:** 0.85
**Belief:** 0.90
**prior:** 0.85
**prior_justification:** Calculated from direct Jsc and efficiency measurements with known albedo.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::power_generation_density_measurement`

### minimodule_front_aperture_efficiency

**QID:** `github:pvsks41560_023_01254_3::minimodule_front_aperture_efficiency`
**Type:** claim
**Role:** independent
**Content:** The champion MA_0.7FA_0.3PbI_3 bifacial minimodule with an aperture area over 20 cm^2 showed a front aperture efficiency of 20.2%, and the rear aperture efficiency was 15.0%, converting to power-generation densities of 23.2 and 24.7 mW/cm^2 at albedos of 0.2 and 0.3, respectively [@Gu2023].
**Prior:** 0.90
**Belief:** 0.96
**prior:** 0.9
**prior_justification:** Directly measured aperture efficiency with clear area definition and I-V characterization.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::front_efficiency_record`; support -> `github:pvsks41560_023_01254_3::nrel_certified_front_efficiency`; support -> `github:pvsks41560_023_01254_3::front_efficiency_record`

### minimodule_rear_aperture_efficiency

**QID:** `github:pvsks41560_023_01254_3::minimodule_rear_aperture_efficiency`
**Type:** claim
**Role:** independent
**Content:** The rear aperture efficiency of the champion bifacial minimodule was 15.0%, with a bifaciality of 74.3%, and the power-generation density exceeded 23 mW/cm^2 at an albedo of 0.2 under 1-sun front illumination [@Gu2023].
**Prior:** 0.90
**Belief:** 0.96
**prior:** 0.9
**prior_justification:** Directly measured aperture efficiency with clear area definition and I-V characterization.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::front_efficiency_record`; support -> `github:pvsks41560_023_01254_3::nrel_certified_front_efficiency`

### nrel_certified_front_efficiency

**QID:** `github:pvsks41560_023_01254_3::nrel_certified_front_efficiency`
**Type:** claim
**Role:** derived
**Content:** The certified front efficiency of the bifacial minimodule by the National Renewable Energy Laboratory (NREL) was 19.2% (stabilized), comparable to the best certified monofacial minimodules, for a minimodule with aperture area of approximately 22.0 cm^2 [@Gu2023].
**Prior:** 0.95
**Belief:** 0.99
**Derived from:** support
**Premises:** `github:pvsks41560_023_01254_3::minimodule_front_aperture_efficiency`, `github:pvsks41560_023_01254_3::minimodule_rear_aperture_efficiency`
**prior:** 0.95
**prior_justification:** NREL-certified measurement - highest confidence due to independent third-party verification.
**gaia:** {'provenance': {'cited_refs': ['Gu2023'], 'referenced_claims': ['minimodule_front_aperture_efficiency', 'minimodule_rear_aperture_efficiency', 'nrel_certified_front_efficiency', 'nrel_certified_rear_efficiency']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::front_efficiency_record`

### nrel_certified_rear_efficiency

**QID:** `github:pvsks41560_023_01254_3::nrel_certified_rear_efficiency`
**Type:** claim
**Role:** orphaned
**Content:** The NREL-certified stabilized rear efficiency of the bifacial minimodule was 14.1% for a minimodule with aperture area of approximately 22.0 cm^2, confirming the rear-side power generation capability [@Gu2023].
**Prior:** 0.95
**Belief:** 0.95
**prior:** 0.95
**prior_justification:** NREL-certified measurement - highest confidence due to independent third-party verification.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}

### average_front_efficiency_8_modules

**QID:** `github:pvsks41560_023_01254_3::average_front_efficiency_8_modules`
**Type:** claim
**Role:** independent
**Content:** Among eight bifacial minimodules with Ag grids, the average front aperture efficiency reached 19.5%, demonstrating good reproducibility across multiple devices [@Gu2023].
**Prior:** 0.85
**Belief:** 0.90
**prior:** 0.85
**prior_justification:** Statistical data from 8 independently fabricated modules showing good reproducibility.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::pgd_by_albedo`

### average_rear_efficiency_8_modules

**QID:** `github:pvsks41560_023_01254_3::average_rear_efficiency_8_modules`
**Type:** claim
**Role:** independent
**Content:** Among eight bifacial minimodules with Ag grids, the average rear aperture efficiency reached 14.5%, giving average power-generation densities of 22.4, 23.9, and 25.3 mW/cm^2 with albedos of 0.2, 0.3, and 0.4, respectively [@Gu2023].
**Prior:** 0.85
**Belief:** 0.90
**prior:** 0.85
**prior_justification:** Statistical data from 8 independently fabricated modules showing good reproducibility.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::pgd_by_albedo`

### pgd_by_albedo

**QID:** `github:pvsks41560_023_01254_3::pgd_by_albedo`
**Type:** claim
**Role:** derived
**Content:** The average power-generation densities of eight bifacial minimodules are 22.4, 23.9, and 25.3 mW/cm^2 at albedos of 0.2, 0.3, and 0.4, respectively, under 1-sun front illumination [@Gu2023].
**Prior:** 0.85
**Belief:** 0.99
**Derived from:** support
**Premises:** `github:pvsks41560_023_01254_3::average_front_efficiency_8_modules`, `github:pvsks41560_023_01254_3::average_rear_efficiency_8_modules`
**prior:** 0.85
**prior_justification:** Calculated from direct efficiency measurements at multiple albedos with controlled LED calibration.
**gaia:** {'provenance': {'cited_refs': ['Gu2023'], 'referenced_claims': ['average_front_efficiency_8_modules', 'average_rear_efficiency_8_modules', 'pgd_by_albedo']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::power_generation_density_measurement`; support -> `github:pvsks41560_023_01254_3::research_objective`; support -> `github:pvsks41560_023_01254_3::front_efficiency_record`
