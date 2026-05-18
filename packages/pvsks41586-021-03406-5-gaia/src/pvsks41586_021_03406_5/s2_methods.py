"""
s2_methods.py - Experimental methods for characterizing perovskite films.

This module covers the characterization techniques used to study
FAPbI3 and Fo-FAPbI3 films: UV-vis absorption, photoluminescence,
SEM, XRD, solid-state NMR, and time-of-flight secondary-ion mass spectrometry.
"""

from gaia.lang import (
    claim, setting, question, support, infer,
    contradiction, complement, equivalence, disjunction,
)

# =============================================================================
# Film Preparation Methods
# =============================================================================

reference_film_preparation = claim(
    "The reference FAPbI3 film was prepared using a precursor solution containing a mixture "
    "of FAPbI3 powder with 35 mol% additional MACl, following previously reported methods "
    "that produce the black α-phase [@Jeong2021].",
    title="Reference FAPbI3 film preparation",
)

fo_fapbi3_film_preparation = claim(
    "For the formate-doped FAPbI3 (Fo-FAPbI3) film, x mol% (x ≤ 4) FAHCOO was added to the "
    "reference precursor solution. The target film used 2% FAHCOO, resulting in approximately "
    "5% MA+ in the final perovskite material [@Jeong2021].",
    title="Fo-FAPbI3 film preparation with FAHCOO",
)

film_preparation_reproducibility = claim(
    "The film preparation process was carried out at controlled room temperature (25°C) and "
    "20% relative humidity. Diethyl ether was dripped during spin-coating to induce controlled "
    "crystallization, followed by annealing at 150°C for 10 minutes [@Jeong2021].",
    title="Film preparation conditions",
)

# =============================================================================
# Characterization Techniques
# =============================================================================

uv_vis_absorption_method = claim(
    "UV-vis absorption spectra were recorded using a Shimadzu UV-1800 spectrophotometer "
    "to measure the optical absorption properties and derive the bandgap of the perovskite "
    "films using the Tauc plot method [@Jeong2021].",
    title="UV-vis absorption spectroscopy method",
)

photoluminescence_method = claim(
    "Steady-state and time-resolved photoluminescence measurements were conducted using a "
    "PicoQuant FluoTime 300 with a pulsed laser diode (λ = 375 nm, pulse FWHM < 70 ps) "
    "to assess non-radiative recombination rates and trap densities [@Jeong2021].",
    title="Photoluminescence measurement method",
)

sem_morphology_method = claim(
    "SEM images of perovskite films were taken with a field-emission scanning electron "
    "microscope (FE-SEM, S-4800, Hitachi) to investigate film morphology and grain size [@Jeong2021].",
    title="SEM morphology characterization method",
)

xrd_crystallinity_method = claim(
    "XRD patterns were performed using a Bruker D8 Advance diffractometer with Cu Kα radiation "
    "(λ = 0.1542 nm) to assess crystallinity and phase composition of the films. "
    "Synchrotron-based 2D grazing-incidence XRD was performed at the SSRF BL14B1 beamline "
    "with X-ray wavelength of 0.6887 Å [@Jeong2021].",
    title="XRD crystallinity characterization method",
)

solid_state_nmr_method = claim(
    "Solid-state NMR measurements were conducted at 100 K (for 1H-13C cross-polarization) "
    "and room temperature (for 207Pb) on a Bruker Avance III 11.7 T spectrometer equipped "
    "with a 3.2 mm low-temperature CPMAS probe. 207Pb and 13C spectra were referenced to "
    "Pb(NO3)2 at -3492 ppm and CH2 resonance of solid adamantane at 38.48 ppm, respectively "
    "[@Jeong2021].",
    title="Solid-state NMR characterization method",
)

tofsims_composition_method = claim(
    "Time-of-flight secondary-ion mass spectrometry (TOF-SIMS) was used to confirm the "
    "presence of FAHCOO in the α-FAPbI3 films, with depth profiling accomplished using a "
    "25 keV BiMn primary ion gun and caesium-ion beam for sputtering [@Jeong2021].",
    title="TOF-SIMS composition characterization method",
)

afm_roughness_method = claim(
    "Surface roughness was assessed using an Asylum Research Cypher S atomic force microscope "
    "under ambient conditions (24°C, 50% relative humidity) with an Olympus AC240-TS tip "
    "operated in tapping mode [@Jeong2021].",
    title="AFM surface roughness method",
)

# =============================================================================
# Device Configuration
# =============================================================================

device_configuration = setting(
    "PSC devices were fabricated with the configuration: FTO/c-TiO2/m-TiO2/perovskite/"
    "octylammonium iodide/Spiro-OMeTAD/Au. The compact TiO2 layer was deposited by spray "
    "pyrolysis, and the mesoporous TiO2 layer by spin-coating using TiO2 nanoparticles "
    "(~50 nm diameter) dispersed in ethanol/terpineol [@Jeong2021].",
    title="PSC device configuration",
)

spiro_ometad_composition = setting(
    "Spiro-OMeTAD (2,2',7,7'-tetrakis(N,N-di-p-methoxyphenylamine)9,9'-spirobifluorene) "
    "was used as the hole-transport layer, deposited by spin-coating at 4,000 rpm for 30 s "
    "[@Jeong2021].",
    title="Spiro-OMeTAD hole-transport layer",
)

# =============================================================================
# Photovoltaic Testing Methods
# =============================================================================

j_v_measurement_method = claim(
    "J-V curves were measured using a McScience K3000 Lab solar cell I-V measurement system "
    "(Class AAA) with light intensity calibrated to AM 1.5G (100 mW cm-2) using a Si-reference "
    "cell certified by NREL. Both reverse scan (1.25 V to 0 V) and forward scan (0 V to 1.25 V) "
    "were performed at a scan speed of 100 mV s-1 [@Jeong2021].",
    title="J-V measurement method",
)

eqe_measurement_method = claim(
    "EQE measurements were performed using a QEX7 system (PV Measurements) to verify the "
    "measured Jsc by integrating the EQE over the AM 1.5G standard spectrum [@Jeong2021].",
    title="EQE measurement method",
)

eqe_el_measurement_method = claim(
    "EQE_EL measurements were performed using a BioLogic SP300 potentiostat with different "
    "bias voltages or currents applied to the PSCs. The emitted photon flux was recorded "
    "using a calibrated 1 cm2 Si photodiode (Hamamatsu S1227-1010BQ) under ambient conditions "
    "(40% relative humidity, 24°C) [@Jeong2021].",
    title="EQE_EL measurement method",
)

stability_test_methods = claim(
    "Stability tests included: (1) shelf-life stability stored in dark at 25°C and 20% RH; "
    "(2) heat stability at 60°C and 20% RH; (3) operational stability under MPP tracking "
    "with AM 1.5G illumination using a BioLogic potentiostat in nitrogen atmosphere [@Jeong2021].",
    title="Stability test methods",
)

# =============================================================================
# Simulation Methods
# =============================================================================

md_simulation_method = claim(
    "Ab initio molecular dynamics simulations were performed to explore the role of HCOO- "
    "anions in the precursor solution and at the perovskite surface. Simulations modeled a "
    "homogeneous mixture of Pb2+, I-, HCOO-, and FA+ ions in the precursor solution and "
    "surface passivation effects at the FAPbI3 slab surface [@Jeong2021].",
    title="Molecular dynamics simulation method",
)

dft_binding_energy_method = claim(
    "Density functional theory (DFT) calculations were used to calculate the formation "
    "energy and relative binding affinities of different anions to iodide vacancies at the "
    "FAPbI3 surface, enabling comparison of HCOO- with Cl-, Br-, I-, and BF4- [@Jeong2021].",
    title="DFT binding energy calculation method",
)

# =============================================================================
# Strategy: Methods Enable Results
# =============================================================================

strat_methods_characterize_films = support(
    [uv_vis_absorption_method, photoluminescence_method, sem_morphology_method,
     xrd_crystallinity_method, solid_state_nmr_method, tofsims_composition_method],
    fo_fapbi3_film_preparation,
    reason="The combination of UV-vis, PL, SEM, XRD, NMR, and TOF-SIMS characterization "
    "techniques comprehensively validates that 2% FAHCOO produces films with: (1) identical "
    "bandgap to reference (1.53 eV), (2) reduced non-radiative recombination, (3) larger grain "
    "size, (4) improved crystallinity, (5) formate at surfaces/grain boundaries but not in bulk, "
    "and (6) confirmed composition with ~5% MA+ [@Jeong2021].",
    prior=0.5,
)

strat_methods_validate_device = support(
    [j_v_measurement_method, eqe_measurement_method, eqe_el_measurement_method,
     stability_test_methods],
    fo_fapbi3_film_preparation,
    reason="The photovoltaic testing methods (J-V, EQE, EQE_EL, stability tests) and device "
    "configuration methods enable rigorous comparison between reference and target (2% Fo-FAPbI3) "
    "devices, allowing the key result of 25.59% PCE (vs 23.92% reference) to be reliably measured "
    "and certified [@Jeong2021].",
    prior=0.5,
)

strat_simulation_explains_mechanism = support(
    [md_simulation_method, dft_binding_energy_method],
    fo_fapbi3_film_preparation,
    reason="The MD and DFT simulation methods provide the fundamental understanding of how "
    "HCOO- anions coordinate strongly with Pb2+ in solution (slowing crystal growth), and "
    "form hydrogen-bonded networks with FA+ at the surface to passivate iodide vacancies "
    "[@Jeong2021].",
    prior=0.5,
)

__all__ = [
    "reference_film_preparation",
    "fo_fapbi3_film_preparation",
    "film_preparation_reproducibility",
    "uv_vis_absorption_method",
    "photoluminescence_method",
    "sem_morphology_method",
    "xrd_crystallinity_method",
    "solid_state_nmr_method",
    "tofsims_composition_method",
    "afm_roughness_method",
    "device_configuration",
    "spiro_ometad_composition",
    "j_v_measurement_method",
    "eqe_measurement_method",
    "eqe_el_measurement_method",
    "stability_test_methods",
    "md_simulation_method",
    "dft_binding_energy_method",
    "strat_methods_characterize_films",
    "strat_methods_validate_device",
    "strat_simulation_explains_mechanism",
]
