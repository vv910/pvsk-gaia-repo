# Module: s3_results

### pbi2_complete_infiltration

**QID:** `github:pvsk2013::pbi2_complete_infiltration`
**Type:** claim
**Role:** independent
**Content:** PbI2 infiltration into mesoporous TiO2 films is complete: cross-sectional SEM shows no PbI2 crystals protruding from the surface of the mesoporous anatase layer, indicating the PbI2 is entirely contained within the nanopores of the TiO2 film [@Burschka2013].
**Prior:** 0.90
**Belief:** 0.90
**figure:** artifacts/images/69b073fcc4e62cd49d023e1cb9ef2463693d4e96daa89a53adbd820ba36d0736.jpg
**caption:** Figure 1a | Cross-sectional SEM of mesoporous TiO2 film infiltrated with PbI2
**prior:** 0.9
**prior_justification:** Direct SEM observation showing complete PbI2 infiltration into TiO2 nanopores.
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}
**Referenced by:** support -> `github:pvsk2013::control_improvement`

### pbi2_crystal_size

**QID:** `github:pvsk2013::pbi2_crystal_size`
**Type:** claim
**Role:** independent
**Content:** When confined within mesoporous TiO2 scaffold, PbI2 crystal size is limited to approximately 22 nm by the pore size of the host [@Burschka2013].
**Prior:** 0.88
**Belief:** 0.88
**prior:** 0.88
**prior_justification:** Crystal size (~22 nm) measured from pore size constraint.
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}
**Referenced by:** support -> `github:pvsk2013::conversion_rate_enhancement`

### color_change_observed

**QID:** `github:pvsk2013::color_change_observed`
**Type:** claim
**Role:** orphaned
**Content:** Dipping the TiO2/PbI2 composite film into CH3NH3I solution (10 mg/ml in 2-propanol) immediately changes its color from yellow to dark brown, indicating formation of CH3NH3PbI3 perovskite [@Burschka2013].
**Belief:** 0.50
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}

### absorption_increase

**QID:** `github:pvsk2013::absorption_increase`
**Type:** claim
**Role:** orphaned
**Content:** The increase in perovskite absorption at 550 nm during conversion is practically complete within a few seconds of exposing the PbI2-loaded TiO2 film to the CH3NH3I solution. A small additional increase occurring on a timescale of 100 s contributes only a few percent to the total signal and is attributed to morphological changes producing enhanced light scattering [@Burschka2013].
**Belief:** 0.50
**figure:** artifacts/images/812927a881b7f784576ec010bd66cabe025fc61278ac82f69354e608ee33a5d9.jpg
**caption:** Figure 1b | Change in absorbance at 550 nm during transformation
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}

### pl_quenching_pbi2

**QID:** `github:pvsk2013::pl_quenching_pbi2`
**Type:** claim
**Role:** orphaned
**Content:** The conversion is accompanied by quenching of PbI2 emission at 425 nm, confirming PbI2 consumption during the reaction with CH3NH3I [@Burschka2013].
**Belief:** 0.50
**figure:** artifacts/images/4d3ba16bb81cb82a3f6f57fd90fcff571011f8e0ddef30b26c97e0a2a3260375.jpg
**caption:** Figure 1c | Change in PL intensity at 520 nm during transformation (PbI2 quenching)
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}

### perovskite_pl_increase

**QID:** `github:pvsk2013::perovskite_pl_increase`
**Type:** claim
**Role:** orphaned
**Content:** The perovskite luminescence at 775 nm increases concomitantly with conversion, passing through a maximum before decreasing to a stationary value due to self-absorption by the perovskite formed during the reaction [@Burschka2013].
**Belief:** 0.50
**figure:** artifacts/images/6f8732eee03b71858adb70c12950c115a1b1a3be8f2833a752724acc6e98ec34.jpg
**caption:** Figure 1d | Change in PL intensity at 775 nm during transformation
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}

### pbi2_tio2_orientation

**QID:** `github:pvsk2013::pbi2_tio2_orientation`
**Type:** claim
**Role:** orphaned
**Content:** PbI2 loaded on mesoporous TiO2 shows three additional diffraction peaks (not present for flat glass) that suggest the anatase scaffold induces a different orientation for PbI2 crystal growth, with peaks attributed to the (110) and (111) lattice planes of the 2H polytype and a third peak assigned to a different PbI2 variant [@Burschka2013].
**Belief:** 0.50
**figure:** artifacts/images/24e66302fb6f429bfb526cadc0e18b7d9f0e5f77befc950e9aea73d31d5700b7.jpg
**caption:** Figure 1e | XRD spectra showing PbI2 orientation differences
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}

### perovskite_xrd_confirmed

**QID:** `github:pvsk2013::perovskite_xrd_confirmed`
**Type:** claim
**Role:** independent
**Content:** XRD shows new diffraction peaks after CH3NH3I reaction that are in good agreement with literature data on the tetragonal phase of CH3NH3PbI3 perovskite, confirming complete conversion within the mesoporous TiO2 scaffold [@Burschka2013].
**Prior:** 0.90
**Belief:** 0.90
**prior:** 0.9
**prior_justification:** Direct XRD measurement showing tetragonal perovskite peaks after conversion.
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}
**Referenced by:** support -> `github:pvsk2013::conversion_rate_enhancement`

### flat_substrate_incomplete_conversion

**QID:** `github:pvsk2013::flat_substrate_incomplete_conversion`
**Type:** claim
**Role:** independent
**Content:** On flat glass substrate, conversion of PbI2 to perovskite is incomplete; a large amount of unreacted PbI2 remains even after a dipping time of 45 min, with CH3NH3I insertion hardly proceeding beyond the surface of thin PbI2 films [@Burschka2013].
**Prior:** 0.85
**Belief:** 0.85
**prior:** 0.85
**prior_justification:** Direct XRD observation of unreacted PbI2 after 45 min on flat glass.
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}
**Referenced by:** support -> `github:pvsk2013::conversion_rate_enhancement`

### conversion_rate_enhancement

**QID:** `github:pvsk2013::conversion_rate_enhancement`
**Type:** claim
**Role:** derived
**Content:** Confining PbI2 crystals to approximately 22 nm within mesoporous TiO2 drastically enhances their rate of conversion to perovskite, completing within a few seconds of contact with methylammonium iodide solution. In contrast, flat surface deposition produces larger 50-200 nm crystallites resulting in incomplete conversion [@Burschka2013].
**Belief:** 0.80
**Derived from:** support
**Premises:** `github:pvsk2013::pbi2_crystal_size`, `github:pvsk2013::perovskite_xrd_confirmed`, `github:pvsk2013::flat_substrate_incomplete_conversion`
**gaia:** {'provenance': {'cited_refs': ['Burschka2013'], 'referenced_claims': ['flat_substrate_incomplete_conversion', 'perovskite_xrd_confirmed']}}
**Referenced by:** support -> `github:pvsk2013::efficiency_achieved`

### nanomorphology_enforced

**QID:** `github:pvsk2013::nanomorphology_enforced`
**Type:** claim
**Role:** orphaned
**Content:** The mesoporous TiO2 scaffold forces the perovskite to adopt a confined nanomorphology dictated by the pore structure [@Burschka2013].
**Belief:** 0.50
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}

### typical_device_performance

**QID:** `github:pvsk2013::typical_device_performance`
**Type:** claim
**Role:** orphaned
**Content:** A typical photovoltaic device measured at 95.6 mW/cm^2 shows: short-circuit photocurrent Jsc = 17.1 mA/cm^2, open-circuit voltage Voc = 992 mV, fill factor = 0.73, yielding a power conversion efficiency (PCE) of 12.9% [@Burschka2013].
**Belief:** 0.50
**figure:** artifacts/images/304cf01e9bc888f63eb7dbfd5375abdd63bf2a6095ed6db5c2eb0982abea2473.jpg
**caption:** Figure 3a | J-V curves for typical photovoltaic device
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}

### device_batch_statistics

**QID:** `github:pvsk2013::device_batch_statistics`
**Type:** claim
**Role:** independent
**Content:** Statistical data from a batch of ten photovoltaic devices shows an average PCE of 12.0% with a standard deviation of 0.5%, demonstrating high reproducibility [@Burschka2013].
**Prior:** 0.90
**Belief:** 0.90
**prior:** 0.9
**prior_justification:** Direct experimental measurement from 10 devices: average PCE 12.0% +/- 0.5%.
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}
**Referenced by:** support -> `github:pvsk2013::reproducibility_improvement`

### performance_table

**QID:** `github:pvsk2013::performance_table`
**Type:** claim
**Role:** orphaned
**Content:** Photovoltaic performance at different light intensities:

| Intensity (mW/cm^2) | Jsc (mA/cm^2) | Voc (mV) | Fill factor | PCE (%) |
|---------------------|---------------|----------|-------------|----------|
| 9.3 | 1.7 | 901 | 0.77 | 12.6 |
| 49.8 | 8.9 | 973 | 0.75 | 13.0 |
| 95.6 | 17.1 | 992 | 0.73 | 12.9 |
**Belief:** 0.50

### ipce_onset

**QID:** `github:pvsk2013::ipce_onset`
**Type:** claim
**Role:** orphaned
**Content:** IPCE shows photocurrent generation starting at 800 nm, consistent with the bandgap of CH3NH3PbI3 [@Burschka2013].
**Belief:** 0.50
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}

### ipce_peak_value

**QID:** `github:pvsk2013::ipce_peak_value`
**Type:** claim
**Role:** independent
**Content:** IPCE reaches peak values of over 90% in the short-wavelength region of the visible spectrum [@Burschka2013].
**Prior:** 0.90
**Belief:** 0.90
**figure:** artifacts/images/73e7d62dd1f08bd7af0963e8c61d91d3dcfa444e62e272a37a03fcc4c8960783.jpg
**caption:** Figure 3b | IPCE spectrum
**prior:** 0.9
**prior_justification:** Direct IPCE measurement showing peak values exceeding 90%.
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}
**Referenced by:** support -> `github:pvsk2013::integrated_current_match`

### integrated_current_match

**QID:** `github:pvsk2013::integrated_current_match`
**Type:** claim
**Role:** derived
**Content:** Integrating the overlap of the IPCE spectrum with the AM1.5G solar photon flux yields a current density of 18.4 mA/cm^2, in excellent agreement with the measured photocurrent density extrapolated to 17.9 mA/cm^2 at standard AM1.5G intensity of 100 mW/cm^2. This confirms negligible mismatch between simulated sunlight and AM1.5G standard [@Burschka2013].
**Belief:** 0.86
**Derived from:** support
**Premises:** `github:pvsk2013::ipce_peak_value`, `github:pvsk2013::apce_exceeds_90_percent`
**gaia:** {'provenance': {'cited_refs': ['Burschka2013'], 'referenced_claims': ['apce_exceeds_90_percent', 'ipce_peak_value']}}

### lhe_data

**QID:** `github:pvsk2013::lhe_data`
**Type:** claim
**Role:** orphaned
**Content:** The low IPCE values in the 600-800 nm range result from the smaller absorption of the perovskite in this spectral region, as shown by the light-harvesting efficiency (LHE) spectrum [@Burschka2013].
**Belief:** 0.50
**figure:** artifacts/images/1ee928c00973afd1bc0ebf8da9c2181388d15dfd517d9d7ef13717ea14e7a97f.jpg
**caption:** Figure 3c | LHE spectrum
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}

### apce_exceeds_90_percent

**QID:** `github:pvsk2013::apce_exceeds_90_percent`
**Type:** claim
**Role:** independent
**Content:** The absorbed-photon-to-current conversion efficiency (APCE) derived from IPCE and LHE is greater than 90% over the whole visible region (without correction for reflective losses), indicating near-unity quantum yield for charge carrier generation and collection [@Burschka2013].
**Prior:** 0.90
**Belief:** 0.90
**figure:** artifacts/images/d9ddb917d9b8fdbaebbeedf48fcaab5c06d3ca74a788681f8be91d4562b9c26a.jpg
**caption:** Figure 3d | APCE spectrum
**prior:** 0.9
**prior_justification:** Direct measurement showing APCE >90% across visible range without correction for reflective losses.
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}
**Referenced by:** support -> `github:pvsk2013::integrated_current_match`

### best_device_performance

**QID:** `github:pvsk2013::best_device_performance`
**Type:** claim
**Role:** derived
**Content:** The best-performing cell (fabricated with modified conditions) shows: Jsc = 20.0 mA/cm^2, Voc = 993 mV, fill factor = 0.73, yielding a PCE of 15.0% measured at 96.4 mW/cm^2. Several cells achieved PCEs between 14% and 15% [@Burschka2013].
**Belief:** 0.77
**Derived from:** support
**Premises:** `github:pvsk2013::best_device_modification`, `github:pvsk2013::best_device_improvement_attributed`
**figure:** artifacts/images/5e89a0ec78a1236458ca9f46731194a29585111f8b637b16a187c490746b0482.jpg
**caption:** Figure 3e | J-V curves for best-performing cell
**gaia:** {'provenance': {'cited_refs': ['Burschka2013'], 'referenced_claims': ['best_device_improvement_attributed', 'best_device_performance']}}

### certified_efficiency

**QID:** `github:pvsk2013::certified_efficiency`
**Type:** claim
**Role:** orphaned
**Content:** One of the best-performing devices was sent to an accredited photovoltaic calibration laboratory for certification, confirming a power conversion efficiency of 14.14% under standard AM1.5G reporting conditions [@Burschka2013].
**Belief:** 0.50
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}

### best_device_improvement_attributed

**QID:** `github:pvsk2013::best_device_improvement_attributed`
**Type:** claim
**Role:** independent
**Content:** The significantly higher photocurrent in top-performance devices is attributed to increased loading of the porous TiO2 film with perovskite pigment and increased light scattering from the pre-wetting step, improving the long-wavelength response of the cell [@Burschka2013].
**Prior:** 0.78
**Belief:** 0.78
**prior:** 0.78
**prior_justification:** Attribution supported by pre-wetting modification and spectral response changes.
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}
**Referenced by:** support -> `github:pvsk2013::best_device_performance`

### stability_result

**QID:** `github:pvsk2013::stability_result`
**Type:** claim
**Role:** independent
**Content:** A sealed photovoltaic device maintained more than 80% of its initial PCE after 500 hours of continuous light soaking at approximately 100 mW/cm^2 and 45 C under argon atmosphere with maximum power point tracking [@Burschka2013].
**Prior:** 0.88
**Belief:** 0.88
**prior:** 0.88
**prior_justification:** Direct 500-hour stability test: device retains >80% of initial PCE.
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}
**Referenced by:** support -> `github:pvsk2013::pce_decrease_mechanism`

### no_photodegradation

**QID:** `github:pvsk2013::no_photodegradation`
**Type:** claim
**Role:** independent
**Content:** No change in short-circuit photocurrent is observed during the 500-hour stability test, indicating no photodegradation of the perovskite light harvester [@Burschka2013].
**Prior:** 0.85
**Belief:** 0.85
**prior:** 0.85
**prior_justification:** Direct observation of unchanged Jsc during stability test.
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}
**Referenced by:** support -> `github:pvsk2013::pce_decrease_mechanism`

### pce_decrease_mechanism

**QID:** `github:pvsk2013::pce_decrease_mechanism`
**Type:** claim
**Role:** derived
**Content:** The decrease in PCE during stability testing is due only to decreases in open-circuit voltage and fill factor, with similar decay shapes suggesting a linked degradation mechanism attributed mainly to a decrease in shunt resistance [@Burschka2013].
**Belief:** 0.82
**Derived from:** support
**Premises:** `github:pvsk2013::stability_result`, `github:pvsk2013::no_photodegradation`
**gaia:** {'provenance': {'cited_refs': ['Burschka2013'], 'referenced_claims': ['no_photodegradation', 'stability_result']}}
