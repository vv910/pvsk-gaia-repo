# Module: motivation

### perovskite_definition

**QID:** `github:pvsk2013::perovskite_definition`
**Type:** setting
**Role:** setting
**Content:** Solution-processable organic-inorganic hybrid perovskites have the general formula CH3NH3PbX3 where X = Cl, Br, or I, and have attracted attention as light-harvesting materials for mesoscopic solar cells [@Burschka2013].
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}

### prior_work_limitation

**QID:** `github:pvsk2013::prior_work_limitation`
**Type:** claim
**Role:** orphaned
**Content:** The single-step deposition of perovskite pigment onto mesoporous metal oxide films using a mixture of PbX2 and CH3NH3X in a common solvent produces large morphological variations, resulting in a wide spread of photovoltaic performance in the resulting devices [@Burschka2013].
**Belief:** 0.50
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}

### sequential_deposition_introduced

**QID:** `github:pvsk2013::sequential_deposition_introduced`
**Type:** claim
**Role:** independent
**Content:** A sequential deposition method is introduced for the formation of the perovskite pigment within the porous metal oxide film: PbI2 is first introduced from solution into a nanoporous titanium dioxide film and subsequently transformed into the perovskite by exposing it to a solution of CH3NH3I [@Burschka2013].
**Prior:** 0.92
**Belief:** 0.92
**prior:** 0.92
**prior_justification:** Core method clearly described in paper.
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}
**Referenced by:** support -> `github:pvsk2013::control_improvement`

### control_improvement

**QID:** `github:pvsk2013::control_improvement`
**Type:** claim
**Role:** derived
**Content:** The sequential deposition method permits much better control over perovskite morphology than the previously employed single-step route [@Burschka2013].
**Belief:** 0.85
**Derived from:** support
**Premises:** `github:pvsk2013::sequential_deposition_introduced`, `github:pvsk2013::pbi2_complete_infiltration`
**gaia:** {'provenance': {'cited_refs': ['Burschka2013'], 'referenced_claims': ['prior_work_limitation']}}
**Referenced by:** support -> `github:pvsk2013::efficiency_achieved`; support -> `github:pvsk2013::reproducibility_improvement`

### efficiency_achieved

**QID:** `github:pvsk2013::efficiency_achieved`
**Type:** claim
**Role:** derived
**Content:** Using the sequential deposition technique for solid-state mesoscopic solar cells, a power conversion efficiency of approximately 15% is achieved under standard AM1.5G test conditions [@Burschka2013].
**Belief:** 0.79
**Derived from:** support
**Premises:** `github:pvsk2013::control_improvement`, `github:pvsk2013::conversion_rate_enhancement`
**gaia:** {'provenance': {'cited_refs': ['Burschka2013'], 'referenced_claims': ['certified_efficiency', 'control_improvement', 'conversion_rate_enhancement']}}

### reproducibility_improvement

**QID:** `github:pvsk2013::reproducibility_improvement`
**Type:** claim
**Role:** derived
**Content:** The sequential deposition method greatly increases the reproducibility of photovoltaic performance compared to single-step deposition [@Burschka2013].
**Belief:** 0.84
**Derived from:** support
**Premises:** `github:pvsk2013::device_batch_statistics`, `github:pvsk2013::control_improvement`
**gaia:** {'provenance': {'cited_refs': ['Burschka2013'], 'referenced_claims': ['control_improvement', 'device_batch_statistics']}}
