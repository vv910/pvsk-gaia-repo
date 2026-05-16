# Module: s4_discussion

### conversion_facilitation

**QID:** `github:pvsk2013::conversion_facilitation`
**Type:** claim
**Role:** derived
**Content:** The confinement of PbI2 within the nanoporous TiO2 network greatly facilitates its conversion to the perovskite pigment, compared to flat substrate deposition [@Burschka2013].
**Belief:** 0.77
**Derived from:** support
**Premises:** `github:pvsk2013::layered_pbi2_structure`, `github:pvsk2013::thermodynamic_driving_force`, `github:pvsk2013::reaction_kinetics_enhancement`
**gaia:** {'provenance': {'cited_refs': ['Burschka2013'], 'referenced_claims': ['layered_pbi2_structure', 'reaction_kinetics_enhancement', 'thermodynamic_driving_force']}}

### nanomorphology_enforcement

**QID:** `github:pvsk2013::nanomorphology_enforcement`
**Type:** claim
**Role:** orphaned
**Content:** The mesoporous scaffold forces the perovskite to adopt a confined nanomorphology [@Burschka2013].
**Belief:** 0.50
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}

### layered_pbi2_structure

**QID:** `github:pvsk2013::layered_pbi2_structure`
**Type:** claim
**Role:** independent
**Content:** The insertion of the organic cation is facilitated through the layered PbI2 structure, which consists of three spatially repeating planes: I-Pb-I. Strong intralayer chemical bonding combined with weak interlayer van der Waals interactions allows easy insertion of guest molecules between the layers [@Burschka2013].
**Prior:** 0.90
**Belief:** 0.90
**prior:** 0.9
**prior_justification:** Well-established in literature on polytypism and intercalation.
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}
**Referenced by:** support -> `github:pvsk2013::conversion_facilitation`

### thermodynamic_driving_force

**QID:** `github:pvsk2013::thermodynamic_driving_force`
**Type:** claim
**Role:** independent
**Content:** The thermodynamic driving force for the two-step conversion is the difference in bulk lattice energy between PbI2 and CH3NH3PbI3, with the initial crystal lattice serving as a template for the formation of the desired compound. This is analogous to ion exchange reactions used to convert II-V semiconductor nanocrystals to III-V analogues while preserving particle size and distribution [@Burschka2013].
**Prior:** 0.82
**Belief:** 0.82
**prior:** 0.82
**prior_justification:** Established principle from semiconductor nanocrystal ion exchange literature.
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}
**Referenced by:** support -> `github:pvsk2013::conversion_facilitation`

### reaction_kinetics_enhancement

**QID:** `github:pvsk2013::reaction_kinetics_enhancement`
**Type:** claim
**Role:** independent
**Content:** The large energy of formation of the hybrid perovskite combined with the nanoscopic morphology of the PbI2 precursor (approximately 22 nm crystals) greatly enhances reaction kinetics, enabling complete transformation within seconds of contact with methylammonium iodide solution [@Burschka2013].
**Prior:** 0.85
**Belief:** 0.85
**prior:** 0.85
**prior_justification:** Reasonable mechanistic interpretation combining formation energy and nanoscale morphology.
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}
**Referenced by:** support -> `github:pvsk2013::conversion_facilitation`

### two_step_method_applicability

**QID:** `github:pvsk2013::two_step_method_applicability`
**Type:** claim
**Role:** orphaned
**Content:** The two-step sequential deposition method is applicable to other preformed metal halide mesostructures that can be converted into the desired perovskite by insertion reactions [@Burschka2013].
**Belief:** 0.50
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}

### record_efficiency

**QID:** `github:pvsk2013::record_efficiency`
**Type:** claim
**Role:** orphaned
**Content:** The power conversion efficiency of 15% achieved with the best device is amongst the highest for solution-processed photovoltaics and sets a new record for organic or hybrid inorganic-organic solar cells at the time of publication [@Burschka2013].
**Belief:** 0.50
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}

### reproducibility_demonstrated

**QID:** `github:pvsk2013::reproducibility_demonstrated`
**Type:** claim
**Role:** orphaned
**Content:** The sequential deposition method provides a means to achieve excellent photovoltaic performance with high reproducibility, addressing the wide spread of performance characteristic of single-step deposition methods [@Burschka2013].
**Belief:** 0.50
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}

### future_potential

**QID:** `github:pvsk2013::future_potential`
**Type:** claim
**Role:** orphaned
**Content:** Perovskite-based photovoltaic devices fabricated using this method have potential for widespread application and may eventually rival conventional silicon-based photovoltaics [@Burschka2013].
**Belief:** 0.50
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}
