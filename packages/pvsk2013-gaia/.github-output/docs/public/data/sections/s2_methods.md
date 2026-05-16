# Module: s2_methods

### device_structure

**QID:** `github:pvsk2013::device_structure`
**Type:** setting
**Role:** setting
**Content:** The photovoltaic device structure consists of: FTO-coated glass substrate (front contact), 30-40 nm TiO2 compact layer (aerosol spray pyrolysis), 350 nm mesoporous TiO2 layer (20-nm-sized anatase particles), perovskite infiltrant, spiro-MeOTAD hole-transporting material (HTM), and 80 nm Au back contact [@Burschka2013].
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}

### mesoporous_tio2_deposition

**QID:** `github:pvsk2013::mesoporous_tio2_deposition`
**Type:** setting
**Role:** setting
**Content:** Mesoporous TiO2 films composed of 20-nm-sized particles are deposited by spin coating at 5,000 rpm for 30 s using TiO2 paste (Dyesol 18NRT) diluted in ethanol (2:7 weight ratio), followed by drying at 125 C and annealing at 500 C for 15 min [@Burschka2013].
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}

### pbi2_infiltration

**QID:** `github:pvsk2013::pbi2_infiltration`
**Type:** setting
**Role:** setting
**Content:** PbI2 is dissolved in N,N-dimethylformamide (DMF) at a concentration of 462 mg/ml (~1 M) under stirring at 70 C. The mesoporous TiO2 films are infiltrated by spin coating at 6,500 rpm for 90 s, then dried at 70 C for 30 min [@Burschka2013].
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}

### mai_conversion

**QID:** `github:pvsk2013::mai_conversion`
**Type:** setting
**Role:** setting
**Content:** After PbI2 infiltration, films are dipped in a solution of CH3NH3I in 2-propanol (10 mg/ml) for 20 s, rinsed with 2-propanol, and dried at 70 C for 30 min to convert PbI2 to CH3NH3PbI3 perovskite [@Burschka2013].
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}

### htm_deposition

**QID:** `github:pvsk2013::htm_deposition`
**Type:** setting
**Role:** setting
**Content:** The HTM is deposited by spin coating at 4,000 rpm for 30 s using a solution of spiro-MeOTAD (72.3 mg), 4-tert-butylpyridine (28.8 ul), lithium bis(trifluoromethylsulphonyl)imide (17.5 ul of 520 mg/ml in acetonitrile), and Co(III) dopant (29 ul of 300 mg/ml in acetonitrile) in 1 ml chlorobenzene [@Burschka2013].
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}

### best_device_modification

**QID:** `github:pvsk2013::best_device_modification`
**Type:** claim
**Role:** independent
**Content:** For the best-performing devices (15% PCE), the PbI2 is spin-cast at 6,500 rpm for 5 s (instead of 90 s), and samples are pre-wetted by dipping in 2-propanol for 1-2 s before the CH3NH3I conversion step [@Burschka2013].
**Prior:** 0.88
**Belief:** 0.88
**prior:** 0.88
**prior_justification:** Direct description of modified conditions: shorter spin-cast and pre-wetting.
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}
**Referenced by:** support -> `github:pvsk2013::best_device_performance`

### j_v_measurement

**QID:** `github:pvsk2013::j_v_measurement`
**Type:** setting
**Role:** setting
**Content:** Current-voltage characteristics are measured under simulated AM1.5G solar irradiation using a 450 W xenon lamp with Schott K113 Tempax sunlight filter. Light intensity is calibrated using a calibrated Si reference diode with KG-3 infrared cut-off filter. Devices are measured using a 0.285 cm^2 metal aperture [@Burschka2013].
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}

### ipce_measurement

**QID:** `github:pvsk2013::ipce_measurement`
**Type:** setting
**Role:** setting
**Content:** IPCE spectra are recorded as functions of wavelength under constant white light bias (approximately 5 mW/cm^2) from an array of white LEDs. The excitation beam from a 300 W xenon lamp is focused through a Gemini-180 double monochromator and chopped at approximately 2 Hz, detected with an SR830 DSP Lock-In Amplifier [@Burschka2013].
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}

### stability_testing

**QID:** `github:pvsk2013::stability_testing`
**Type:** setting
**Role:** setting
**Content:** For long-term stability tests, devices are sealed in argon using a 50-mm-thick hot-melting polymer and microscope coverslip. Devices are subjected to constant light soaking at approximately 100 mW/cm^2 using white LED array (Philips LXM3-PW51 4000K), maintained at maximum power point, at approximately 45 C. J-V measurements at different light intensities are recorded automatically every 2 h [@Burschka2013].
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}

### optical_spectroscopy

**QID:** `github:pvsk2013::optical_spectroscopy`
**Type:** setting
**Role:** setting
**Content:** Optical absorption measurements are carried out using a Varian Cary 5 spectrophotometer. Photoluminescence is measured on a Horiba Jobin Yvon Fluorolog spectrofluorometer. Samples are placed vertically in a 10 mm path length cuvette [@Burschka2013].
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}

### xrd_measurement

**QID:** `github:pvsk2013::xrd_measurement`
**Type:** setting
**Role:** setting
**Content:** X-ray powder diagrams are recorded on an X'Pert MPD PRO (PANalytical) with Cu anode (lambda = 1.54060 A), graphite (002) monochromator, and RTMS X'Celerator detector in BRAGG-BRENTANO geometry. Step size is 0.008 deg with acquisition time up to 7.5 min/deg [@Burschka2013].
**gaia:** {'provenance': {'cited_refs': ['Burschka2013']}}
