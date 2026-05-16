# Module: s6_stability

### initial_pce_retention_6000h

**QID:** `github:pvsks41560_023_01254_3::initial_pce_retention_6000h`
**Type:** claim
**Role:** independent
**Content:** The best bifacial minimodule retained 97% of its initial power conversion efficiency (T97) after light soaking for over 6,000 hours from the front side at open-circuit condition and temperature of 60 plus/minus 5 degrees C under simulated 1-sun illumination in air, representing the most stable reported perovskite minimodule [@Gu2023].
**Prior:** 0.90
**Belief:** 0.96
**prior:** 0.9
**prior_justification:** Directly measured stability data with clear protocol and long duration.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::stability_demonstrated`; support -> `github:pvsks41560_023_01254_3::research_objective`; support -> `github:pvsks41560_023_01254_3::front_efficiency_record`

### damp_heat_retention

**QID:** `github:pvsks41560_023_01254_3::damp_heat_retention`
**Type:** claim
**Role:** derived
**Content:** Another bifacial minimodule maintained approximately 84% of its initial efficiency after damp-heat testing for over 1,000 hours at 85 degrees C and approximately 85% relative humidity, demonstrating good stability under damp-heat conditions [@Gu2023].
**Prior:** 0.80
**Belief:** 0.93
**Derived from:** support
**Premises:** `github:pvsks41560_023_01254_3::ald_sno2_stabilization_benefit`, `github:pvsks41560_023_01254_3::stability_benefits_composition`
**prior:** 0.8
**prior_justification:** Direct measured data from damp-heat test chamber with controlled temperature and humidity.
**gaia:** {'provenance': {'cited_refs': ['Gu2023'], 'referenced_claims': ['ald_sno2_stabilization_benefit', 'damp_heat_retention', 'stability_benefits_composition']}}

### ald_sno2_stabilization_benefit

**QID:** `github:pvsks41560_023_01254_3::ald_sno2_stabilization_benefit`
**Type:** claim
**Role:** independent
**Content:** The very good stability of these bifacial minimodules benefits from the ALD SnO2 buffer layer in addition to the intrinsic stability of FA_0.92Cs_0.08PbI3: first, ALD SnO2 greatly reduced damage to perovskite in the laser scribing process, preventing formation of amorphous perovskites with reduced PL intensity around P2 scribing lines; second, replacing amorphous BCP (which can recrystallize during operation) with ALD SnO2 stabilized the C60/electrode interface [@Gu2023].
**Prior:** 0.80
**Belief:** 0.85
**prior:** 0.8
**prior_justification:** Reasoned explanation based on multiple observations including PL imaging and BCP recrystallization.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::stability_demonstrated`; support -> `github:pvsks41560_023_01254_3::damp_heat_retention`

### stability_benefits_composition

**QID:** `github:pvsks41560_023_01254_3::stability_benefits_composition`
**Type:** claim
**Role:** independent
**Content:** The stability benefits of these bifacial minimodules arise from two factors: the ALD SnO2 layer which protects against laser scribing damage and prevents BCP recrystallization, and the intrinsically stable FA_0.92Cs_0.08PbI3 perovskite composition optimized by previous methods that demonstrates good light stability [@Gu2023].
**Prior:** 0.80
**Belief:** 0.85
**prior:** 0.8
**prior_justification:** Reasoned conclusion based on comparison with previous literature on FA-Cs composition stability.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::stability_demonstrated`; support -> `github:pvsks41560_023_01254_3::damp_heat_retention`
