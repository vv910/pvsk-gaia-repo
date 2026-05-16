# Module: s4_light_scattering

### jsc_reduction_without_reflective_electrode

**QID:** `github:pvsks41560_023_01254_3::jsc_reduction_without_reflective_electrode`
**Type:** claim
**Role:** orphaned
**Content:** The absence of a reflecting or opaque metal electrode in bifacial device structure reduces short-circuit current density (Jsc) by approximately 1.3 mA/cm^2 due to insufficient absorption in the red and near-infrared wavelength range compared with opaque monofacial cells with metal back reflector [@Gu2023].
**Prior:** 0.85
**Belief:** 0.85
**prior:** 0.85
**prior_justification:** Calculated estimate based on optical absorption differences, consistent with observed Jsc values.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}

### sio2_np_light_scattering

**QID:** `github:pvsks41560_023_01254_3::sio2_np_light_scattering`
**Type:** claim
**Role:** independent
**Content:** Silicon oxide (SiO2) nanoparticles (NPs) are introduced in perovskite films to scatter incident sunlight and increase the optical path, based on resonant Mie scattering, avoiding metal NPs which raise concerns of chemical reaction with perovskites and strong non-radiative charge recombination at NP surfaces [@Gu2023].
**Prior:** 0.85
**Belief:** 0.89
**prior:** 0.85
**prior_justification:** Mie scattering is well-established physics, application to this system is novel.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::absorption_enhancement_simulation`

### optimal_np_size_range

**QID:** `github:pvsks41560_023_01254_3::optimal_np_size_range`
**Type:** claim
**Role:** independent
**Content:** Light-scattering properties of spherical SiO2 NPs studied by 3D finite-difference time-domain (FDTD) method show that SiO2 NPs should be larger than 400 nm to efficiently scatter red and near-infrared light and smaller than 600 nm to minimize losing absorption of UV-visible light in perovskite films [@Gu2023].
**Prior:** 0.80
**Belief:** 0.86
**prior:** 0.8
**prior_justification:** FDTD simulation result requiring correct material optical constants.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::absorption_enhancement_simulation`

### optimal_np_spacing_range

**QID:** `github:pvsks41560_023_01254_3::optimal_np_spacing_range`
**Type:** claim
**Role:** independent
**Content:** The simulated absorption of incident light by perovskite with different spacings of NPs shows that perovskite film with NP spacing from 1 to 1.5 micrometers can absorb 5.4 to 19.8% more 800 nm light than pure film from the front side; larger spacing also increases light absorption but less significantly [@Gu2023].
**Prior:** 0.80
**Belief:** 0.86
**prior:** 0.8
**prior_justification:** Simulation result with experimental validation but narrow parameter space studied.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::jsc_increase_with_optimal_np`

### absorption_enhancement_simulation

**QID:** `github:pvsks41560_023_01254_3::absorption_enhancement_simulation`
**Type:** claim
**Role:** derived
**Content:** FDTD simulation shows that perovskite film embedded with SiO2 NPs with optimal spacing of 1-1.5 micrometers shows obviously enhanced absorption of red and near-infrared light by transverse scattering that increases the optical path, with 5.4-19.8% more 800 nm light absorption compared with film without NPs [@Gu2023].
**Prior:** 0.80
**Belief:** 0.96
**Derived from:** support
**Premises:** `github:pvsks41560_023_01254_3::sio2_np_light_scattering`, `github:pvsks41560_023_01254_3::optimal_np_size_range`
**prior:** 0.8
**prior_justification:** FDTD simulation validated by experimental absorption measurements.
**gaia:** {'provenance': {'cited_refs': ['Gu2023'], 'referenced_claims': ['absorption_enhancement_simulation', 'optimal_np_size_range', 'sio2_np_light_scattering']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::front_pce_improvement_with_np`

### np_synthesis_and_embedding

**QID:** `github:pvsks41560_023_01254_3::np_synthesis_and_embedding`
**Type:** claim
**Role:** independent
**Content:** SiO2 NPs with a diameter of 500 nm were synthesized and dispersed in ethanol, then pre-deposited on ITO substrate using blade coating with N2 flow assistance, forming a monolayer of NPs nicely embedded in the perovskite layer without causing cracks or voids; an optimized NP concentration of 30 mg/ml gives NP spacing of 1-2 micrometers and NPs occupying 1.9-7.6% of the total film volume [@Gu2023].
**Prior:** 0.85
**Belief:** 0.90
**prior:** 0.85
**prior_justification:** Direct SEM imaging confirms embedding and spacing, but concentration optimization is empirical.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::jsc_increase_with_optimal_np`

### no_extra_recombination_from_np

**QID:** `github:pvsks41560_023_01254_3::no_extra_recombination_from_np`
**Type:** claim
**Role:** independent
**Content:** Perovskite film with embedded SiO2 NPs exhibited comparable PL intensity and carrier lifetime with optimized perovskite films without NPs, showing that these NPs do not introduce an additional non-radiative charge recombination pathway to the perovskite films [@Gu2023].
**Prior:** 0.85
**Belief:** 0.93
**prior:** 0.85
**prior_justification:** PL intensity and lifetime measurements support no additional recombination, but indirect evidence.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::jsc_increase_with_optimal_np`; support -> `github:pvsks41560_023_01254_3::front_pce_improvement_with_np`

### jsc_increase_with_optimal_np

**QID:** `github:pvsks41560_023_01254_3::jsc_increase_with_optimal_np`
**Type:** claim
**Role:** derived
**Content:** The average front short-circuit current density (Jsc) of bifacial PSCs with optimal SiO2 NP spacing increased from 23.1 to 23.9 mA/cm^2 without notably changing open-circuit voltage (Voc) and fill factor, confirming that the SiO2 NPs with optimal spacing did not introduce extra defects in the perovskite film and did not change the charge collection or recombination process [@Gu2023].
**Prior:** 0.90
**Belief:** 0.98
**Derived from:** support
**Premises:** `github:pvsks41560_023_01254_3::optimal_np_spacing_range`, `github:pvsks41560_023_01254_3::np_synthesis_and_embedding`, `github:pvsks41560_023_01254_3::no_extra_recombination_from_np`
**prior:** 0.9
**prior_justification:** Direct Jsc measurement across 14 samples with clear statistical improvement.
**gaia:** {'provenance': {'cited_refs': ['Gu2023'], 'referenced_claims': ['jsc_increase_with_optimal_np', 'no_extra_recombination_from_np', 'np_synthesis_and_embedding', 'optimal_np_spacing_range']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::front_pce_improvement_with_np`

### front_pce_improvement_with_np

**QID:** `github:pvsks41560_023_01254_3::front_pce_improvement_with_np`
**Type:** claim
**Role:** derived
**Content:** The embedding of SiO2 NPs significantly recovered the light absorption loss after optimizing the concentration, and the front power conversion efficiency of champion bifacial PSCs increased from 22.1% to 23.2% with optimal NP spacing; the integrated front Jsc from EQE increased from 22.5 to 23.3 mA/cm^2, matching well with statistical Jsc measured from I-V scan [@Gu2023].
**Prior:** 0.90
**Belief:** 0.99
**Derived from:** support
**Premises:** `github:pvsks41560_023_01254_3::jsc_increase_with_optimal_np`, `github:pvsks41560_023_01254_3::absorption_enhancement_simulation`, `github:pvsks41560_023_01254_3::no_extra_recombination_from_np`
**prior:** 0.9
**prior_justification:** Direct efficiency measurement from I-V curves with champion cell reporting.
**gaia:** {'provenance': {'cited_refs': ['Gu2023'], 'referenced_claims': ['absorption_enhancement_simulation', 'front_pce_improvement_with_np', 'jsc_increase_with_optimal_np', 'no_extra_recombination_from_np']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::research_objective`
