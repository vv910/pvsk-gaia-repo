"""
s5_performance.py - Photovoltaic performance results.

This module covers the device performance data including J-V curves,
PCE, EQE, EQE_EL, and ideality factor measurements for reference
and target (2% Fo-FAPbI3) PSCs.
"""

from gaia.lang import (
    claim, setting, question, support, infer,
    contradiction, complement, equivalence, disjunction,
)

# =============================================================================
# J-V Curve Results
# =============================================================================

reference_device_performance = claim(
    "The reference PSC device (without formate) achieved a maximum PCE of 23.92% with "
    "Jsc = 25.72 mA/cm², Voc = 1.153 V, and fill factor = 80.69% under reverse scan "
    "conditions [@Jeong2021].",
    title="Reference device performance",
    metadata={"figure": "artifacts/images/bdfa0eae6bcd8185b282aa70cc8971fd0f24bb34ed7b2baa7c325e3f5c936c10.jpg",
               "caption": "Fig. 3b | J-V curves of reference and target PSCs"},
)

target_device_performance = claim(
    "The target PSC device (2% Fo-FAPbI3) achieved a maximum PCE of 25.59% with "
    "Jsc = 26.35 mA/cm², Voc = 1.189 V, and fill factor = 81.7% under reverse scan "
    "conditions [@Jeong2021].",
    title="Target device performance",
    metadata={"figure": "artifacts/images/bdfa0eae6bcd8185b282aa70cc8971fd0f24bb34ed7b2baa7c325e3f5c936c10.jpg",
               "caption": "Fig. 3b | J-V curves of reference and target PSCs"},
)

performance_improvement = claim(
    "Compared to the reference device (23.92% PCE), the target device shows a relative "
    "improvement of 1.67% absolute PCE (from 23.92% to 25.59%), with improvements across "
    "all key photovoltaic parameters: higher Jsc (+0.63 mA/cm²), higher Voc (+36 mV), and "
    "higher fill factor (+1.01%) [@Jeong2021].",
    title="Performance improvement from formate addition",
)

pcertified_performance = claim(
    "Certification by Newport (accredited photovoltaic test laboratory) confirmed a "
    "quasi-steady-state PCE of 25.21% for a target PSC device, with Voc = 1.174 V, "
    "Jsc = 26.25 mA/cm², and fill factor = 81.8% [@Jeong2021].",
    title="Certified PCE of 25.21%",
    metadata={"figure": "artifacts/images/54fc16043d8f6d315ac3d8f8d91e594b9ab93b999c3af88f350949e9ecb9a4ae.jpg",
               "caption": "Supplementary Fig. 2 | Certified efficiency measurement"},
)

performance_distribution = claim(
    "Statistical distribution of measured PCE for reference and target PSCs shows "
    "consistent improvement with 2% formate addition across multiple devices, "
    "confirming the reproducibility of the performance enhancement [@Jeong2021].",
    title="Statistical performance distribution",
    metadata={"figure": "artifacts/images/5520f2e6a344601d8089422d32096ca46da274ae7e82452c566d4801136cd992.jpg",
               "caption": "Fig. 3c | Distribution of PCEs for reference and target PSCs"},
)

# =============================================================================
# EQE Results
# =============================================================================

eqe_results = claim(
    "EQE measurements show the target cell has higher external quantum efficiency than "
    "the reference cell over the whole visible-light absorption region. Integrating the "
    "EQE over the AM 1.5G standard spectrum gives projected Jsc of 25.75 mA/cm² for "
    "reference and 26.35 mA/cm² for target, well matching the measured Jsc under "
    "solar simulator [@Jeong2021].",
    title="EQE results",
    metadata={"figure": "artifacts/images/cf0cb5b793ad5e6a81c0a736f723c63f09fb2a445c3f3e21516c6fc5376d23b5.jpg",
               "caption": "Fig. 3d | EQE and integrated Jsc of reference and target PSCs"},
)

jsc_verification = claim(
    "The EQE-integrated Jsc values (25.75 mA/cm² for reference, 26.35 mA/cm² for target) "
    "match well with the Jsc values measured under the solar simulator, confirming the "
    "accuracy of the current density measurements [@Jeong2021].",
    title="Jsc verified by EQE integration",
)

# =============================================================================
# EQE_EL Results (Electroluminescence)
# =============================================================================

eqe_el_results = claim(
    "EQE_EL measurements at injection current densities corresponding to Jsc under 1 sun "
    "illumination (25.5 mA/cm² for reference, 26.5 mA/cm² for target) show that the "
    "reference cell has EQE_EL of 2.2% while the target cell has EQE_EL of 10.1% - "
    "a fivefold reduction in non-radiative recombination rate with formate treatment "
    "[@Jeong2021].",
    title="EQE_EL results show 5x improvement",
    metadata={"figure": "artifacts/images/9235dd842dba135c2ebdea3550ad0d31d59bff5577e24479cd96981db206cca9.jpg",
               "caption": "Fig. 3e | EQE_EL measurements of reference and target PSCs"},
)

non_radiative_recombination_reduction = claim(
    "The fivefold increase in EQE_EL (from 2.2% to 10.1%) with formate treatment indicates "
    "a corresponding fivefold reduction in non-radiative recombination rate, directly "
    "validating the defect passivation mechanism identified by NMR and MD simulations "
    "[@Jeong2021].",
    title="Formate treatment reduces non-radiative recombination 5x",
)

voc_shadowqueisser = claim(
    "The Voc of 1.21 V obtained for the target cell (from EQE_EL measurement) is 96% of "
    "the Shockley-Queisser limit (1.25 V) - the highest value yet reported for FAPbI3 "
    "PSCs, indicating near-optimal Voc with minimal non-radiative recombination losses "
    "[@Jeong2021].",
    title="Target Voc is 96% of Shockley-Queisser limit",
)

# =============================================================================
# Light Intensity Dependence Results
# =============================================================================

jsc_light_intensity_linearity = claim(
    "Linear relationship between Jsc and light intensity (slope ~0.95) for both reference "
    "and target PSCs indicates good charge transport and negligible bimolecular "
    "recombination in both devices [@Jeong2021].",
    title="Jsc vs light intensity is linear",
)

voc_light_intensity_ideality = claim(
    "Voc vs logarithm of light intensity shows linear relationship with slope fitted to "
    "ηid kBT/q, where ηid is the ideality factor, kB is Boltzmann constant, T is "
    "temperature, and q is electron charge. The reference cell has ηid = 1.52 while "
    "the target cell has ηid = 1.18 - lower than the previously reported value of 1.27 "
    "and approaching unity, indicating reduced trap-assisted recombination [@Jeong2021].",
    title="Ideality factor results",
    metadata={"figure": "artifacts/images/36e6796e08d95d399fe3237a6f15673c878d735f89d45760f5fc43a381d8486b.jpg",
               "caption": "Fig. 3f | Voc vs light intensity relationship for reference and target PSCs"},
)

reduced_ideality_factor = claim(
    "The reduction in ideality factor from 1.52 (reference) to 1.18 (target) confirms "
    "reduced trap-assisted recombination with formate passivation, supporting the "
    "mechanism of iodide vacancy elimination identified in the characterization studies "
    "[@Jeong2021].",
    title="Target has lower ideality factor (1.18 vs 1.52)",
)

fill_factor_improvement_mechanism = claim(
    "The fill factor critically depends on the ideality factor; the reduction in ηid "
    "from 1.52 to 1.18 contributes to the increased fill factor measured for the "
    "target PSCs (81.7% vs 80.69%) [@Jeong2021].",
    title="Lower ideality factor improves fill factor",
)

# =============================================================================
# Alternative Additive Results
# =============================================================================

formamidinium_acetate_control = claim(
    "Devices fabricated using formamidinium acetate as an additive (instead of FAHCOO) "
    "showed a negative effect on performance, confirming that the specific formate anion "
    "is responsible for the performance improvement, not the general effect of adding "
    "an acetate-based additive [@Jeong2021].",
    title="Formamidinium acetate control experiment",
)

formate_without_macl = claim(
    "For devices fabricated without MACl additives or passivation layers, those containing "
    "formate still showed performance advantages, demonstrating that formate alone can "
    "provide beneficial effects even without the MACl additive system [@Jeong2021].",
    title="Formate works even without MACl additive",
)

# =============================================================================
# Strategies
# =============================================================================

strat_formate_improves_voc = support(
    [target_device_performance, voc_shadowqueisser, reduced_ideality_factor],
    claim("Formate passivation improves Voc toward radiative limit"),
    reason="Target device Voc = 1.189 V (reverse scan) and 1.21 V (from EQE_EL) reaches "
    "96% of Shockley-Queisser limit, with ideality factor reduced to 1.18 (from 1.52). "
    "This demonstrates that eliminating iodide vacancies through formate passivation "
    "effectively reduces non-radiative recombination, allowing Voc to approach its "
    "theoretical maximum [@Jeong2021].",
    prior=0.5,
)

strat_formate_improves_ff = support(
    [target_device_performance, fill_factor_improvement_mechanism, reduced_ideality_factor],
    claim("Formate passivation improves fill factor"),
    reason="Fill factor increases from 80.69% (reference) to 81.7% (target). This "
    "improvement is linked to the reduced ideality factor (1.52 → 1.18), which "
    "critically depends on the fill factor. Formate passivation reduces trap-assisted "
    "recombination, improving FF [@Jeong2021].",
    prior=0.5,
)

strat_formate_improves_jsc = support(
    [target_device_performance, eqe_results, jsc_verification],
    claim("Formate passivation improves Jsc"),
    reason="Jsc increases from 25.72 mA/cm² (reference) to 26.35 mA/cm² (target), "
    "confirmed by EQE measurements showing higher EQE across the visible spectrum. "
    "This improvement is consistent with better charge transport and reduced "
    "recombination with formate treatment [@Jeong2021].",
    prior=0.5,
)

strat_abduction_performance = support(
    [performance_improvement, non_radiative_recombination_reduction],
    claim("Formate passivation is the mechanism for PCE improvement"),
    reason="Target PCE of 25.59% represents a 1.67% absolute improvement over reference "
    "(23.92%). The fivefold EQE_EL improvement (2.2% → 10.1%) directly measures a "
    "fivefold reduction in non-radiative recombination. This is consistent with the "
    "mechanism established by NMR (formate at surfaces not bulk) and MD simulations "
    "(HCOO- has highest binding to I- vacancy) - formate eliminates iodide vacancies, "
    "reducing trap-assisted recombination, improving all photovoltaic parameters "
    "[@Jeong2021].",
    prior=0.5,
)

strat_control_validates_formate = support(
    [formamidinium_acetate_control, formate_without_macl],
    claim("Formate-specific effect confirmed by control experiments"),
    reason="Formamidinium acetate (different anion) has negative effect, confirming "
    "the specific benefit of HCOO-. Formate also works without MACl additive, showing "
    "the effect is from formate itself, not just a combination with MACl. These controls "
    "validate that formate is the key improvement agent [@Jeong2021].",
    prior=0.5,
)

# Note: performance_improvement was misspelled, using correct one
strat_overall_improvement = support(
    [reference_device_performance, target_device_performance, pcertified_performance],
    claim("2% Fo-FAPbI3 achieves 25.6% PCE (certified 25.2%)"),
    reason="Target device achieves 25.59% PCE with all improved parameters. Newport "
    "certification confirms 25.21% quasi-steady-state efficiency. This represents the "
    "highest reported efficiency for FAPbI3-based PSCs, exceeding the previous record "
    "of 23.73% and breaking the 25% barrier for the first time [@Jeong2021].",
    prior=0.5,
)

__all__ = [
    "reference_device_performance",
    "target_device_performance",
    "performance_improvement",
    "pcertified_performance",
    "performance_distribution",
    "eqe_results",
    "jsc_verification",
    "eqe_el_results",
    "non_radiative_recombination_reduction",
    "voc_shadowqueisser",
    "jsc_light_intensity_linearity",
    "voc_light_intensity_ideality",
    "reduced_ideality_factor",
    "fill_factor_improvement_mechanism",
    "formamidinium_acetate_control",
    "formate_without_macl",
    "strat_formate_improves_voc",
    "strat_formate_improves_ff",
    "strat_formate_improves_jsc",
    "strat_abduction_performance",
    "strat_control_validates_formate",
    "strat_overall_improvement",
]