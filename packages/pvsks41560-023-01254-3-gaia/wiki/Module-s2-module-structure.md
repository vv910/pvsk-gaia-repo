# Module: s2_module_structure

### module_structure_p_i_n

**QID:** `github:pvsks41560_023_01254_3::module_structure_p_i_n`
**Type:** claim
**Role:** orphaned
**Content:** The bifacial perovskite module adopts a p-i-n perovskite solar cell structure with poly[bis(4-phenyl)(2,4,6-trimethylphenyl)amine] (PTAA) as the hole transport layer and fullerene (C60) as the electron transport layer, with perovskite composition of MA_0.7FA_0.3PbI_3 or FA_0.92Cs_0.08PbI_3 with slightly excess CsI [@Gu2023].
**Prior:** 0.90
**Belief:** 0.90
**prior:** 0.9
**prior_justification:** Device structure clearly described with layer-by-layer composition and thickness.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}

### ito_sheet_resistance

**QID:** `github:pvsks41560_023_01254_3::ito_sheet_resistance`
**Type:** claim
**Role:** orphaned
**Content:** A low sheet resistance of approximately 30 ohms per square with high transparency was achieved for indium tin oxide (ITO) of 150 nm sputtered at room temperature, but bifacial minimodules showed poor fill factor (FF) of 0.39 when ITO directly replaced the copper electrode [@Gu2023].
**Prior:** 0.85
**Belief:** 0.85
**prior:** 0.85
**prior_justification:** Direct four-point probe measurement providing sheet resistance and transmittance.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}

### ag_grid_design

**QID:** `github:pvsks41560_023_01254_3::ag_grid_design`
**Type:** claim
**Role:** independent
**Content:** Applying silver grids on a rear ITO electrode is an effective way to reduce resistance loss, but requires rational design to balance resistance loss and the shadowing effect of silver grids, which reduces bifacial gain [@Gu2023].
**Prior:** 0.85
**Belief:** 0.90
**prior:** 0.85
**prior_justification:** Well-established engineering principle validated by extensive modeling and experimental FF data.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::ff_improvement_with_ag_grid`

### optimal_ag_grid_spacing

**QID:** `github:pvsks41560_023_01254_3::optimal_ag_grid_spacing`
**Type:** claim
**Role:** independent
**Content:** With Ag grid width of 0.2 mm and height of 500 nm (narrowest achievable by thermal evaporation using a shadow mask) and linear resistance of 8 ohm/cm, the optimal Ag grid spacing is approximately 2 mm at an albedo of 0.2, reducing relative PCE loss induced by rear electrode resistance from 8.6% to less than 0.9% [@Gu2023].
**Prior:** 0.85
**Belief:** 0.91
**prior:** 0.85
**prior_justification:** Simulation result validated by experimental measurement of resistance and FF.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::ff_improvement_with_ag_grid`; support -> `github:pvsks41560_023_01254_3::bifacial_gain_percentage`

### relative_pce_loss_reduction

**QID:** `github:pvsks41560_023_01254_3::relative_pce_loss_reduction`
**Type:** claim
**Role:** independent
**Content:** The modeling shows that the relative PCE loss induced by the rear electrode resistance is reduced from 8.6% to less than 0.9% after adding the Ag grid with spacing of approximately 2 mm, accompanied by an increase of fill factor from 0.70 to 0.77 [@Gu2023].
**Prior:** 0.85
**Belief:** 0.90
**prior:** 0.85
**prior_justification:** Modeling result with experimental validation through FF improvement.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::ff_improvement_with_ag_grid`

### ff_improvement_with_ag_grid

**QID:** `github:pvsks41560_023_01254_3::ff_improvement_with_ag_grid`
**Type:** claim
**Role:** derived
**Content:** The fill factor increases from 0.70 to 0.77 with optimal Ag grid spacing of approximately 2 mm, while the bifacial perovskite modules gain 15% more power output with an albedo of 0.2 compared with monofacial modules [@Gu2023].
**Prior:** 0.90
**Belief:** 0.98
**Derived from:** support
**Premises:** `github:pvsks41560_023_01254_3::ag_grid_design`, `github:pvsks41560_023_01254_3::optimal_ag_grid_spacing`, `github:pvsks41560_023_01254_3::relative_pce_loss_reduction`
**prior:** 0.9
**prior_justification:** Directly measured fill factor values with clear before-after comparison.
**gaia:** {'provenance': {'cited_refs': ['Gu2023'], 'referenced_claims': ['ag_grid_design', 'optimal_ag_grid_spacing', 'relative_pce_loss_reduction']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::bifacial_gain_percentage`; support -> `github:pvsks41560_023_01254_3::research_objective`

### bifacial_gain_percentage

**QID:** `github:pvsks41560_023_01254_3::bifacial_gain_percentage`
**Type:** claim
**Role:** derived
**Content:** The bifacial perovskite modules gain 15% more power output with an albedo of 0.2 compared with monofacial modules, thanks to the rear-side albedo light harvesting [@Gu2023].
**Belief:** 0.88
**Derived from:** support
**Premises:** `github:pvsks41560_023_01254_3::bifacial_gain_background`, `github:pvsks41560_023_01254_3::ff_improvement_with_ag_grid`, `github:pvsks41560_023_01254_3::optimal_ag_grid_spacing`
**gaia:** {'provenance': {'cited_refs': ['Gu2023'], 'referenced_claims': ['bifacial_gain_background', 'bifacial_gain_percentage', 'ff_improvement_with_ag_grid', 'optimal_ag_grid_spacing']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::research_objective`

### simulated_pgds_by_albedo

**QID:** `github:pvsks41560_023_01254_3::simulated_pgds_by_albedo`
**Type:** claim
**Role:** independent
**Content:** The simulated power-generation densities of bifacial modules under 1-sun illumination are 21.5, 23.1, 24.7, and 26.4 mW/cm^2 with albedos of 0.1, 0.2, 0.3, and 0.4, respectively, based on a monofacial module with 20% aperture efficiency [@Gu2023].
**Prior:** 0.80
**Belief:** 0.86
**prior:** 0.8
**prior_justification:** Simulation based on validated device model but depends on albedo assumptions.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::power_generation_density_measurement`
