"""
Methods section: Film characterisation and Device characterisation.

This module covers:
- Triple cation perovskite composition Csx(MA0.17FA0.83)(1-x)Pb(I0.83Br0.17)3
- XRD, absorption, and photoluminescence characterization
- Thermal stability tests
- Film formation dependence on processing conditions
- Device architecture and fabrication
- Optimization of device parameters
"""

from gaia.lang import claim, setting

# Triple cation perovskite composition
triple_cation_composition = setting(
    "The triple cation perovskites have the generic form Csx(MA0.17FA0.83)(1-x)Pb(I0.83Br0.17)3, abbreviated as CsxM where x is in percentage. Cs0M (no Cs) is the basic composition for the best state-of-the-art devices, with lead excess in the precursor [@Saliba2016]."
)

# Film characterisation methods
xrd_measurement = claim(
    "X-ray diffraction (XRD) data for CsxM with x = 0, 5, 10, 15% shows all compositions exhibit a typical perovskite peak at approximately 14 degrees. Cs0M shows small side peaks at 11.6 degrees and 12.7 degrees corresponding to the photoinactive hexagonal yellow phase of FAPbI3 and cubic PbI2 respectively [@Saliba2016].",
    title="XRD characterisation of CsxM series",
    metadata={"figure": "artifacts/images/fig1a.png", "caption": "Fig. 1a | XRD spectra of CsxM series showing perovskite peak at ~14 degrees and yellow phase peaks at 11.6 and 12.7 degrees for Cs0M."},
)

cs_addition_eliminates_impurities = claim(
    "Upon addition of small amounts of Cs from 0, 5, 10 to 15%, the yellow phase and the PbI2 peak disappear completely [@Saliba2016].",
    title="Cs addition eliminates yellow phase and PbI2 peaks",
    metadata={"figure": "artifacts/images/fig1a.png", "caption": "Fig. 1a | XRD spectra showing elimination of yellow phase and PbI2 peaks with Cs addition."},
)

absorption_pl_spectra = claim(
    "The absorption and photoluminescence (PL) spectra in Fig. 1b are blue-shifted by approximately 10 nm from Cs0M to Cs15M [@Saliba2016].",
    title="Absorption and PL blue-shifted by ~10nm with Cs addition",
    metadata={"figure": "artifacts/images/fig1b.png", "caption": "Fig. 1b | Absorption (dashed) and PL (solid) spectra showing blue-shift with increasing Cs content."},
)

cs_integrated_into_lattice = claim(
    "The data are consistent with the Cs cation being integrated into the perovskite lattice, lowering the effective Cs/MA/FA cation radius and shifting the tolerance factor towards a cubic lattice structure that matches the black perovskite phase [@Saliba2016].",
    title="Cs integrates into perovskite lattice",
)

black_phase_entropically_stabilized = claim(
    "The photoactive black phase is entropically stabilized at room temperature, resulting in suppression of the hexagonal yellow phase of FA perovskite which is not entropically stabilized at room temperature anymore [@Saliba2016].",
    title="Black phase entropically stabilized at room temperature",
)

# Thermal stability tests
thermal_stability_test = claim(
    "Films of Cs0M and Cs10M kept at 130 degrees Celsius for 3 hours in dry air show that Cs0M perovskite films start bleaching after this thermal stress, evidenced by decreased absorption spectrum, while Cs10M retains the dark black color and does not bleach noticeably [@Saliba2016].",
    title="Cs10M shows improved thermal stability at 130C",
    metadata={"figure": "artifacts/images/fig2ab.png", "caption": "Fig. 2a,b | Thermal stability test showing Cs10M retains black color while Cs0M bleaches at 130C for 3 hours."},
)

cs_increases_thermal_stability = claim(
    "Cs increases the thermal stability for a fixed halide ratio, and increased Br content also contributes considerably to thermal stability [@Saliba2016].",
    title="Cs increases thermal stability for fixed halide ratio",
)

# Film formation dependence
film_formation_no_annealing = claim(
    "Cs0M does not form a perovskite phase directly after deposition (without annealing) as evidenced by absorbance data not showing characteristic perovskite absorption onset, the film remains red, and XRD data do not exhibit the characteristic perovskite peak at approximately 14 degrees [@Saliba2016].",
    title="Cs0M does not form perovskite without annealing",
    metadata={"figure": "artifacts/images/fig2c.png", "caption": "Fig. 2c | Cs0M remains red without annealing, no perovskite phase formed."},
)

film_formation_with_cs = claim(
    "Under the same deposition conditions, Cs10M yields a clear black perovskite phase as evidenced by the film's color, absorption spectrum, and perovskite peak in XRD, confirming that Cs induces the black phase at room temperature [@Saliba2016].",
    title="Cs10M forms black perovskite phase at room temperature",
    metadata={"figure": "artifacts/images/fig2c.png", "caption": "Fig. 2c | Cs10M turns black at room temperature with characteristic perovskite XRD peak."},
)

processing_temperature_sensitivity = claim(
    "At 18 degrees Celsius glove box temperature, Cs0M does not form perovskite phase even after annealing at 100 degrees Celsius for 1 hour, but increasing temperature by 7 degrees Celsius to 25 degrees Celsius is sufficient to induce black phase formation in Cs0M. Cs10M forms readily the perovskite phase at 18 degrees Celsius [@Saliba2016].",
    title="Cs10M less sensitive to processing temperature variations",
    metadata={"figure": "artifacts/images/fig2d.png", "caption": "Fig. 2d | Processing temperature sensitivity: Cs0M requires 25C but Cs10M forms perovskite at 18C."},
)

cs_benefits_summary = claim(
    "Adding Cs benefits MA/FA perovskites in terms of suppression of the yellow phase, thermal stability, and robustness to temperature variations during processing [@Saliba2016].",
    title="Cs benefits MA/FA perovskites in multiple ways",
)

# Device architecture
device_architecture = setting(
    "The solar cell architecture consists of glass/fluorine-doped tin oxide/compact TiO2/Li-doped mesoporous TiO2/perovskite/spiro-OMeTAD/gold [@Saliba2016].",
    metadata={"figure": "artifacts/images/fig3.png", "caption": "Fig. 3 | Cross-sectional SEM images showing device architecture."},
)

# Device characterisation - optimization
baseline_efficiency = claim(
    "The baseline efficiency for Cs0M devices was just below 17% with respectable currents of approximately 20 mA/cm2, open circuit voltages reaching 1.1 V, and fill factor at 0.7 [@Saliba2016].",
    title="Cs0M baseline efficiency just below 17%",
)

fill_factor_improvement = claim(
    "As Cs is added, the fill factor improves, reaching 0.77 at optimum x = 10% [@Saliba2016].",
    title="Fill factor improves to 0.77 at 10% Cs",
)

# Cs:MA ratio optimization
cs_ma_ratio_optimization = claim(
    "Varying the ratio of Cs:MA for Cs10M composition while keeping FA fixed shows that the resulting device data have an optimum with both Cs and MA present, indicating that the presence of both Cs and MA is highly relevant for device performance [@Saliba2016].",
    title="Both Cs and MA required for optimal device performance",
)

# SEM analysis
cs5m_monomorphic_grains = claim(
    "Cs5M devices show more monolithic perovskite grains that tend to go from bottom to top of the device, while Cs0M grains tend to stack on top of each other. More uniform grains enable better charge transport, explaining the higher fill factor for Cs5M devices [@Saliba2016].",
    title="Cs5M shows monolithic grain structure",
    metadata={"figure": "artifacts/images/fig3.png", "caption": "Fig. 3 | Cross-sectional SEM showing monolithic grains in Cs5M devices."},
)

seed_assisted_crystal_growth = claim(
    "The film formation is assisted by the addition of Cs inducing perovskite seeds already at room temperature. These seeds become nucleation sites for further growth during crystallization, leading to more uniform grains [@Saliba2016].",
    title="Cs acts as seed for crystal growth",
)

# Large scale test statistics
device_statistics = claim(
    "Statistics from 40 controls (Cs0M) and 98 Cs-based (Cs5M) devices over 18 different batches prepared by three different people show improvements in all device parameters: Voc improved from 1121 plus or minus 25 mV (n=40) to 1132 plus or minus 25 mV (n=98), Jsc improved from 21.06 plus or minus 1.53 to 22.69 plus or minus 0.75 mA/cm2, FF improved from 0.693 plus or minus 0.028 to 0.748 plus or minus 0.018, and PCE improved from 16.37 plus or minus 1.49 to 19.20 plus or minus 0.91%. Twenty independent devices show efficiencies greater than 20% [@Saliba2016].",
    title="Device statistics: Cs5M outperforms Cs0M across all parameters",
    metadata={"figure": "artifacts/images/fig4.png", "caption": "Fig. 4 | Statistics of 40 Cs0M and 98 Cs5M devices showing improvements in all parameters and reduced standard deviation."},
)

cs_benefits_reproducibility = claim(
    "Cs addition improves device reproducibility because the stabilization of the black phase of FA perovskite with MA alone is very sensitive to temperature at the beginning of the crystallization process, causing large deviation even within the same batch [@Saliba2016].",
    title="Cs addition improves reproducibility by reducing temperature sensitivity",
)

# High performance devices
best_stabilized_pce = claim(
    "The highest stabilized PCE exceeds 21%, with maximum power point tracking reaching 21.1% at 960 mV, in good agreement with JV scans. Fill factors reach up to approximately 0.8, values rarely reached for highest performances [@Saliba2016].",
    title="Best device achieves 21.1% stabilized PCE",
    metadata={"figure": "artifacts/images/fig5a.png", "caption": "Fig. 5a | JV scan and maximum power point tracking showing 21.1% stabilized PCE."},
)

# Long-term stability
long_term_stability = claim(
    "Under constant illumination and maximum power point tracking in nitrogen at room temperature, the Cs5M device efficiency drops from 20% to approximately 18% within a few hours where it stays stable for at least 250 hours. The Cs0M device shows much less stable behavior with biexponential decay. Cs5M has a slow half-life component of approximately 5000 hours, one of the highest values reported for high efficiency perovskite solar cells [@Saliba2016].",
    title="Cs5M maintains ~18% efficiency after 250 hours under operational conditions",
    metadata={"figure": "artifacts/images/fig5b.png", "caption": "Fig. 5b | Aging test showing Cs5M stable at ~18% for 250h while Cs0M degrades significantly."},
)

fill_factor_degradation = claim(
    "Most degradation stems from fill factor while current and voltage do not decrease significantly. Fill factor losses may stem from decreased conductivity of a degraded organic HTM [@Saliba2016].",
    title="Fill factor is main source of degradation",
)

high_performer_stability = claim(
    "None of the high performing Cs0M devices (16-18%) were as stable as the best Cs devices, especially with current degrading significantly over time. This is the first test where a state-of-the-art 20% device was aged, demonstrating the great potential of perovskite solar cells for industrial applications [@Saliba2016].",
    title="State-of-the-art 20% Cs devices show superior stability",
)

__all__ = [
    "triple_cation_composition",
    "xrd_measurement",
    "cs_addition_eliminates_impurities",
    "absorption_pl_spectra",
    "cs_integrated_into_lattice",
    "black_phase_entropically_stabilized",
    "thermal_stability_test",
    "cs_increases_thermal_stability",
    "film_formation_no_annealing",
    "film_formation_with_cs",
    "processing_temperature_sensitivity",
    "cs_benefits_summary",
    "device_architecture",
    "baseline_efficiency",
    "fill_factor_improvement",
    "cs_ma_ratio_optimization",
    "cs5m_monomorphic_grains",
    "seed_assisted_crystal_growth",
    "device_statistics",
    "cs_benefits_reproducibility",
    "best_stabilized_pce",
    "long_term_stability",
    "fill_factor_degradation",
    "high_performer_stability",
]