# Module: s3_hydrophobic_additive

### ald_damage_to_perovskite

**QID:** `github:pvsks41560_023_01254_3::ald_damage_to_perovskite`
**Type:** claim
**Role:** orphaned
**Content:** The atomic layer deposition (ALD) of SnO2 during bifacial perovskite minimodule fabrication imposes a challenge by damaging the perovskite films, frequently causing fraction of bifacial PSCs to exhibit much lower fill factor compared with monofacial counterparts using C60/bathocuproine (BCP) as ETL [@Gu2023].
**Prior:** 0.85
**Belief:** 0.85
**prior:** 0.85
**prior_justification:** Direct SEM imaging and XRD evidence of perovskite degradation after ALD process.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}

### tpfb_in_htl_protection

**QID:** `github:pvsks41560_023_01254_3::tpfb_in_htl_protection`
**Type:** claim
**Role:** independent
**Content:** Mixing 5 wt% of tris(pentafluorophenyl)borane (TPFB) into the PTAA hole transport layer (HTL) protected the perovskite films from moisture damage during the ALD process and resulted in even better device reproducibility than adding TPFB as an additive in the perovskite film or modifying the perovskite surface [@Gu2023].
**Prior:** 0.85
**Belief:** 0.94
**prior:** 0.85
**prior_justification:** Accelerated moisture test shows clear protective effect, reproducibility demonstrated.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::hydrophobic_surface_confirmation`; support -> `github:pvsks41560_023_01254_3::ff_improvement_tpfb`

### tpfb_spread_to_perovskite

**QID:** `github:pvsks41560_023_01254_3::tpfb_spread_to_perovskite`
**Type:** claim
**Role:** independent
**Content:** TPFB added to the HTL spreads into the perovskite film, with approximately 35% of the TPFB added in the HTL (5 wt% in PTAA) spreading into the perovskite layer, equivalent to 0.067 mol% TPFB to Pb, as confirmed by X-ray photoelectron spectroscopy (XPS) measurement showing fluorine presence at the perovskite surface [@Gu2023].
**Prior:** 0.85
**Belief:** 0.94
**prior:** 0.85
**prior_justification:** XPS measurement providing direct compositional evidence of TPFB spreading.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::hydrophobic_surface_confirmation`; support -> `github:pvsks41560_023_01254_3::tpfb_passivation_effect`

### hydrophobic_surface_confirmation

**QID:** `github:pvsks41560_023_01254_3::hydrophobic_surface_confirmation`
**Type:** claim
**Role:** derived
**Content:** Surface contact-angle measurement confirmed that the modified perovskites with TPFB had a more hydrophobic surface compared with control samples, demonstrating enhanced moisture resistance [@Gu2023].
**Prior:** 0.85
**Belief:** 0.98
**Derived from:** support
**Premises:** `github:pvsks41560_023_01254_3::tpfb_in_htl_protection`, `github:pvsks41560_023_01254_3::tpfb_spread_to_perovskite`
**prior:** 0.85
**prior_justification:** Direct contact angle measurement providing physical evidence of hydrophobicity change.
**gaia:** {'provenance': {'cited_refs': ['Gu2023'], 'referenced_claims': ['hydrophobic_surface_confirmation', 'tpfb_in_htl_protection', 'tpfb_spread_to_perovskite']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::tpfb_passivation_effect`

### tpfb_passivation_effect

**QID:** `github:pvsks41560_023_01254_3::tpfb_passivation_effect`
**Type:** claim
**Role:** derived
**Content:** TPFB was found to passivate perovskite films, evidenced by stronger photoluminescence (PL) intensity and longer recombination lifetime from perovskite films covered by a layer of TPFB, as well as reduced trap density of states in TPFB-modified devices [@Gu2023].
**Prior:** 0.85
**Belief:** 0.99
**Derived from:** support
**Premises:** `github:pvsks41560_023_01254_3::tpfb_spread_to_perovskite`, `github:pvsks41560_023_01254_3::hydrophobic_surface_confirmation`
**prior:** 0.85
**prior_justification:** Direct PL measurement showing increased intensity and lifetime, supported by trap density data.
**gaia:** {'provenance': {'cited_refs': ['Gu2023'], 'referenced_claims': ['hydrophobic_surface_confirmation', 'tpfb_passivation_effect', 'tpfb_spread_to_perovskite']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::tpfb_enhanced_stability`; support -> `github:pvsks41560_023_01254_3::ff_improvement_tpfb`

### tpfb_reduced_trap_density

**QID:** `github:pvsks41560_023_01254_3::tpfb_reduced_trap_density`
**Type:** claim
**Role:** independent
**Content:** Perovskite solar cells with TPFB showed reduced trap density of states, further confirming the passivation effect of TPFB on reducing point defects in perovskite films [@Gu2023].
**Prior:** 0.85
**Belief:** 0.89
**prior:** 0.85
**prior_justification:** Direct measurement of trap density via dark injection Current-Voltage analysis.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::tpfb_enhanced_stability`

### tpfb_frei_level_ptaa

**QID:** `github:pvsks41560_023_01254_3::tpfb_frei_level_ptaa`
**Type:** claim
**Role:** independent
**Content:** The addition of TPFB in PTAA pulled down the Fermi level of PTAA from -4.51 eV to -4.82 eV, enabling better energy alignment and conductivity of the p-doped HTL, which contributes to fill factor enhancement compared with devices with TPFB as an additive in perovskites [@Gu2023].
**Prior:** 0.85
**Belief:** 0.90
**prior:** 0.85
**prior_justification:** Direct UPS measurement of Fermi level shift with clear methodology.
**gaia:** {'provenance': {'cited_refs': ['Gu2023']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::ff_improvement_tpfb`

### ff_improvement_tpfb

**QID:** `github:pvsks41560_023_01254_3::ff_improvement_tpfb`
**Type:** claim
**Role:** derived
**Content:** The bifacial module using TPFB:PTAA as the HTL has a larger fill factor of 0.76 and much higher efficiency, while the fill factor of the control (PTAA without TPFB) is only 0.68 measured from the front side for bifacial modules with aperture area of 25.03 cm^2 [@Gu2023].
**Prior:** 0.90
**Belief:** 0.98
**Derived from:** support
**Premises:** `github:pvsks41560_023_01254_3::tpfb_in_htl_protection`, `github:pvsks41560_023_01254_3::tpfb_passivation_effect`, `github:pvsks41560_023_01254_3::tpfb_frei_level_ptaa`
**prior:** 0.9
**prior_justification:** Directly measured fill factor improvement with statistical validation across 14 samples.
**gaia:** {'provenance': {'cited_refs': ['Gu2023'], 'referenced_claims': ['ff_improvement_tpfb', 'tpfb_frei_level_ptaa', 'tpfb_in_htl_protection', 'tpfb_passivation_effect']}}
**Referenced by:** support -> `github:pvsks41560_023_01254_3::research_objective`

### tpfb_enhanced_stability

**QID:** `github:pvsks41560_023_01254_3::tpfb_enhanced_stability`
**Type:** claim
**Role:** derived
**Content:** Perovskite films deposited on TPFB:PTAA degraded slower than control samples under accelerated stability testing conditions, proving that TPFB enhances the light stability of perovskites, possibly through slightly modified grain-growth process resulting in smaller point-defect density [@Gu2023].
**Prior:** 0.80
**Belief:** 0.95
**Derived from:** support
**Premises:** `github:pvsks41560_023_01254_3::tpfb_passivation_effect`, `github:pvsks41560_023_01254_3::tpfb_reduced_trap_density`
**prior:** 0.8
**prior_justification:** Accelerated stability test under light soaking with comparison to control samples.
**gaia:** {'provenance': {'cited_refs': ['Gu2023'], 'referenced_claims': ['tpfb_enhanced_stability', 'tpfb_passivation_effect', 'tpfb_reduced_trap_density']}}
