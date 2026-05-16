"""
s3_results.py - Film characterization results.

This module covers the experimental results from characterizing
FAPbI3 and Fo-FAPbI3 perovskite films: optical properties,
morphology, crystallinity, and NMR spectroscopy.
"""

from gaia.lang import (
    claim, setting, question, support, infer,
    contradiction, complement, equivalence, disjunction,
)

# =============================================================================
# UV-Vis Absorption and Bandgap
# =============================================================================

absorption_spectra_results = claim(
    "UV-vis absorption spectra of FAPbI3 films (x = 0, 2, and 4% Fo-FAPbI3) show that the "
    "absorption threshold and photoluminescence peak position are identical for all films, "
    "with an obvious decrease in absorbance only for the 4% Fo-FAPbI3 film. The derived "
    "bandgap is 1.53 eV for all films using the Tauc plot method [@Jeong2021].",
    title="UV-vis absorption and bandgap results",
    metadata={"figure": "artifacts/images/461969b79fbf6780b00675513b5f1b3a034d61b3249d88d9dd137fea5c229575.jpg",
               "caption": "Fig. 1a | UV-vis absorption and PL spectra of FAPbI3 films"},
)

bandgap_identical = claim(
    "The bandgap of 1.53 eV derived from Tauc plot analysis is identical for reference and "
    "Fo-FAPbI3 films, indicating that formate addition does not modify the electronic bandgap "
    "of the perovskite material [@Jeong2021].",
    title="Bandgap identical across all films",
)

# =============================================================================
# Photoluminescence Results
# =============================================================================

pl_decay_results = claim(
    "Time-resolved photoluminescence measurements show that the 2% Fo-FAPbI3 perovskite film "
    "has slower PL decay than the reference, indicating reduced non-radiative recombination "
    "due to reduced trap-mediated bulk or surface recombination. In contrast, the 4% Fo-FAPbI3 "
    "film shows faster PL decay than the reference, indicating excess formate degrades "
    "photoluminescence properties [@Jeong2021].",
    title="PL decay rate results",
    metadata={"figure": "artifacts/images/7496b1e32f08797d39154225984684ff65e1ebd5754f822f210b1add9da0e274.jpg",
               "caption": "Fig. 1b | Time-resolved photoluminescence of FAPbI3 films"},
)

reduced_trap_density = claim(
    "The slower PL decay in 2% Fo-FAPbI3 compared to reference indicates a reduction in "
    "trap-mediated non-radiative recombination, which is a key mechanism for improved "
    "photovoltaic performance [@Jeong2021].",
    title="2% Fo-FAPbI3 has reduced trap density",
)

# =============================================================================
# SEM Morphology Results
# =============================================================================

sem_morphology_results = claim(
    "SEM images show that the 2% Fo-FAPbI3 film has a slightly larger grain size of up to "
    "2 μm compared to the reference FAPbI3 film. Both reference and 2% Fo-FAPbI3 films show "
    "monolithic grains from top to bottom in cross-sectional SEM images. The 4% Fo-FAPbI3 "
    "films show irregular grain size indicating degraded morphology [@Jeong2021].",
    title="SEM morphology results",
    metadata={"figure": "artifacts/images/2034ea71cc957c5a420d10d662918b1a08e3a8619ad2da93f059b0a58d2e4827.jpg",
               "caption": "Fig. 1c,d | SEM images of reference and 2% Fo-FAPbI3 films; scale bar 2 μm"},
)

larger_grain_size = claim(
    "The 2% Fo-FAPbI3 film exhibits larger grain size (up to 2 μm) compared to the reference, "
    "which is consistent with the proposed mechanism of formate coordinating with Pb2+ to "
    "slow the crystal growth process during film formation [@Jeong2021].",
    title="2% Fo-FAPbI3 has larger grain size",
)

monolithic_grain_structure = claim(
    "Both reference and 2% Fo-FAPbI3 films show monolithic grains extending from top to "
    "bottom, indicating high-quality polycrystalline films with good vertical crystallite "
    "alignment [@Jeong2021].",
    title="Monolithic grain structure in both films",
)

# =============================================================================
# Surface Roughness Results
# =============================================================================

surface_roughness_results = claim(
    "AFM measurements reveal a surface roughness of 41.66 nm and 57.47 nm for the reference "
    "and 2% Fo-FAPbI3 films, respectively. The slightly increased surface roughness of the "
    "2% Fo-FAPbI3 film is attributed to the slightly increased grain size [@Jeong2021].",
    title="Surface roughness results",
)

# =============================================================================
# XRD Crystallinity Results
# =============================================================================

xrd_phase_results = claim(
    "XRD measurements show identical peak positions at around 13.95° and 27.85° for both "
    "reference and Fo-FAPbI3 perovskite films, corresponding to the α-phase of FAPbI3. "
    "The 4% Fo-FAPbI3 film shows additional peaks assigned to FTO substrates and different "
    "orientations of α-FAPbI3, with broader and lower-intensity diffraction peaks indicating "
    "poor crystallinity [@Jeong2021].",
    title="XRD phase composition results",
)

alpha_phase_confirmation = claim(
    "Both reference and 2% Fo-FAPbI3 films show peaks at 13.95° and 27.85° corresponding "
    "to the α-phase of FAPbI3, confirming that formate addition does not induce phase "
    "transitions to the photoinactive δ-phase at this concentration [@Jeong2021].",
    title="α-phase confirmed in both films",
)

improved_crystallinity_2percent = claim(
    "The full-width at half-maximum (FWHM) of the α-phase peak is decreased for the 2% "
    "Fo-FAPbI3 film compared to reference, indicating improved crystallinity with formate "
    "addition at the optimal 2% concentration [@Jeong2021].",
    title="2% Fo-FAPbI3 has improved crystallinity",
)

# =============================================================================
# Grazing-Incidence XRD Results
# =============================================================================

gi_xrd_stabilization_results = claim(
    "Two-dimensional grazing-incidence XRD measurements at ~100% relative humidity and 30°C "
    "in air show the presence of δ-phase in the reference film but absence of δ-phase in "
    "the 2% Fo-FAPbI3 film. This provides strong evidence that FAHCOO stabilizes the α-phase "
    "of FAPbI3 against humidity, a key stability improvement [@Jeong2021].",
    title="GI-XRD shows α-phase stabilization",
    metadata={"figure": "artifacts/images/ca4b633fefcfa15e0960f5c69a970b8d99892699503db8e33d172ef00d75ef39.jpg",
               "caption": "Fig. 1e,f | 2D GI-XRD patterns showing δ-phase in reference but not in 2% Fo-FAPbI3"},
)

alpha_stabilization_humidity = claim(
    "The 2% Fo-FAPbI3 film stabilizes the α-phase against humidity, preventing the transition "
    "to the photoinactive δ-phase that occurs in the reference film under same conditions "
    "[@Jeong2021].",
    title="Formate stabilizes α-phase against humidity",
)

# =============================================================================
# Solid-State NMR Results
# =============================================================================

pb207_nmr_results = claim(
    "The 207Pb solid-state NMR spectrum of α-FAPbI3 shows a resonance at 1,543 ppm. "
    "Addition of 5% FABr results in a notable shoulder on the low-frequency side, "
    "corresponding to 207Pb in a [PbBrI5] site. However, the 207Pb resonance of "
    "α-FAPbI3 + 5% FAHCOO remains the same, providing strong evidence that HCOO- does "
    "NOT substitute for iodide anions in the FAPbI3 lattice [@Jeong2021].",
    title="207Pb NMR shows formate does not substitute in lattice",
    metadata={"figure": "artifacts/images/1e6200febe25eeb77c80cd39ce70dc91f335ef01d62ca5f00bb12f7de6de4bf5.jpg",
               "caption": "Fig. 2a | 207Pb solid-state NMR spectra showing formate does not enter lattice"},
)

formate_not_in_bulk = claim(
    "The 207Pb NMR resonance remaining unchanged with FAHCOO addition confirms that formate "
    "does not incorporate into the FAPbI3 lattice - it must reside at surfaces or grain "
    "boundaries instead. This is supported by DFT calculations of formation energy "
    "[@Jeong2021].",
    title="Formate does not incorporate into bulk lattice",
)

c13_nmr_formate_environment = claim(
    "13C solid-state NMR shows FAHCOO has resonances at 167.8 ppm (HCOO-) and 158.5 ppm (FA+). "
    "δ-FAPbI3 shows 13C at 157.6 ppm and α-FAPbI3 at 153.4 ppm. Upon mixing 5 mol% FAHCOO "
    "with FAPbI3, the α-FAPbI3 13C signal remains at 153.4 ppm (no broadening), but the HCOO- "
    "peak shows considerable broadening - indicative of a distribution of local environments "
    "consistent with formate interacting with undercoordinated Pb2+ at surfaces/grain boundaries "
    "[@Jeong2021].",
    title="13C NMR shows formate at surfaces with distribution of environments",
    metadata={"figure": "artifacts/images/756af9cfd3155cfcca2e6d9c11f6f125153ee0e7a8a9de9fa81c7ab2f1d8b9a0.jpg",
               "caption": "Fig. 2b | 13C solid-state NMR spectra showing formate local environments"},
)

formate_at_interfaces = claim(
    "The broadening of the HCOO- 13C signal in Fo-FAPbI3 (as opposed to the well-defined "
    "environment in crystalline FAHCOO) is consistent with formate interacting with "
    "undercoordinated Pb2+ to passivate iodide vacancies at surfaces or grain boundaries "
    "[@Jeong2021].",
    title="Formate local environment at interfaces",
)

quantitative_c13_nmr = claim(
    "Integration of FA+ and MA+ resonances in quantitative 13C NMR spectra yields a MA+ "
    "concentration of 5.1% in the final 2% Fo-FAPbI3 thin film, confirming the expected "
    "composition from the 35 mol% MACl additive in the precursor solution [@Jeong2021].",
    title="MA+ concentration is 5.1% in target film",
)

# =============================================================================
# TOF-SIMS Confirmation
# =============================================================================

tofsims_confirmation = claim(
    "Time-of-flight secondary-ion mass spectrometry (TOF-SIMS) measurements confirm "
    "the presence of FAHCOO in the 2% Fo-FAPbI3 thin films, supporting the NMR findings "
    "that formate is present in the perovskite film but at surfaces/grain boundaries "
    "rather than in the bulk lattice [@Jeong2021].",
    title="TOF-SIMS confirms formate presence",
)

# =============================================================================
# Strategies
# =============================================================================

strat_optical_supports_passivation = support(
    [absorption_spectra_results, bandgap_identical, pl_decay_results, reduced_trap_density],
    claim("Formate passivation reduces traps in FAPbI3 without modifying bandgap"),
    reason="UV-vis confirms bandgap unchanged (1.53 eV), while PL decay shows reduced "
    "non-radiative recombination - together these indicate formate passivates defects "
    "without changing the fundamental electronic structure of the perovskite [@Jeong2021].",
    prior=0.5,
)

strat_morphology_supports_crystallinity = support(
    [sem_morphology_results, larger_grain_size, monolithic_grain_structure,
     surface_roughness_results, xrd_phase_results, improved_crystallinity_2percent],
    claim("2% FAHCOO improves FAPbI3 crystallinity"),
    reason="SEM shows larger grain size (up to 2 μm), XRD shows reduced FWHM of α-phase "
    "peak indicating improved crystallinity, and AFM confirms the increased grain size "
    "contributes to slightly higher surface roughness. Both films show monolithic grain "
    "structure. These findings support that 2% formate improves crystallinity, while 4% "
    "degrades it (irregular grains, poor crystallinity) [@Jeong2021].",
    prior=0.5,
)

strat_nmr_supports_surface_passivation = support(
    [pb207_nmr_results, formate_not_in_bulk, c13_nmr_formate_environment,
     formate_at_interfaces, quantitative_c13_nmr, tofsims_confirmation],
    claim("HCOO- anions passivate iodide vacancies at surfaces and grain boundaries"),
    reason="207Pb NMR shows formate does NOT substitute in the lattice (resonance unchanged). "
    "13C NMR shows formate HCOO- peak is broadened with distribution of environments, "
    "consistent with formate coordinating to undercoordinated Pb2+ at surfaces/grain boundaries. "
    "TOF-SIMS confirms formate presence. Together these provide strong evidence for surface/grain "
    "boundary passivation rather than bulk incorporation [@Jeong2021].",
    prior=0.5,
)

strat_gi_xrd_supports_stability = support(
    [gi_xrd_stabilization_results, alpha_stabilization_humidity],
    claim("2% formate stabilizes α-FAPbI3 against humidity"),
    reason="2D GI-XRD at 100% RH and 30°C shows δ-phase present in reference but absent in "
    "2% Fo-FAPbI3, providing direct evidence that formate stabilizes the photoactive α-phase "
    "against humidity-induced phase transition [@Jeong2021].",
    prior=0.5,
)

__all__ = [
    "absorption_spectra_results",
    "bandgap_identical",
    "pl_decay_results",
    "reduced_trap_density",
    "sem_morphology_results",
    "larger_grain_size",
    "monolithic_grain_structure",
    "surface_roughness_results",
    "xrd_phase_results",
    "alpha_phase_confirmation",
    "improved_crystallinity_2percent",
    "gi_xrd_stabilization_results",
    "alpha_stabilization_humidity",
    "pb207_nmr_results",
    "formate_not_in_bulk",
    "c13_nmr_formate_environment",
    "formate_at_interfaces",
    "quantitative_c13_nmr",
    "tofsims_confirmation",
    "strat_optical_supports_passivation",
    "strat_morphology_supports_crystallinity",
    "strat_nmr_supports_surface_passivation",
    "strat_gi_xrd_supports_stability",
]