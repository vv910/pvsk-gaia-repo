"""
Methods for the Min2019 perovskite solar cell paper.

This module covers film preparation, device fabrication, and characterization
methods including UV-vis, PL, XRD, GIWAXS, XPS, ToF-SIMS, SCLC, and photostability
testing.
"""

from gaia.lang import claim, setting

# -----------------------------------------------------------------------------
# Deposition and fabrication methods
# -----------------------------------------------------------------------------

deposition_method = claim(
    "A thin film of FAPbI3 incorporating MDACl2 was deposited using a process "
    "similar to that reported for state-of-the-art mixed perovskites, but adding "
    "MDACl2 instead of MAPbBr3. The precursor solution was coated and annealed at "
    "150C for 10 min to produce the perovskite film [@Min2019].",
    title="FAPbI3:MDACl2 thin film deposition method",
)

surface_passivation = claim(
    "The surface of the target and control perovskite layers was passivated using "
    "previously reported methods including phenethylammonium iodide (PEAI) "
    "and YCl3 treatments to reduce non-radiative recombination and improve "
    "open-circuit voltage and fill factor [@Min2019].",
    title="Surface passivation treatment",
)

device_structure = claim(
    "PSC devices were fabricated with the structure: FTO/SnO2/mp-TiO2/perovskite/"
    "PTAA/Au for regular architecture, or with CuPC as hole-transporting material (HTM) "
    "for thermal stability tests at 150C to avoid degradation by hygroscopic dopants "
    "in spiro-OMeTAD [@Min2019].",
    title="Device structure configuration",
)

# -----------------------------------------------------------------------------
# Characterization methods
# -----------------------------------------------------------------------------

uvvis_absorption = claim(
    "UV-vis absorption spectra were measured for FAPbI3:xMDACl2 (x = 0, 1.9, 3.8, "
    "and 5.7 mol%) films. The absorption spectra showed a slight blue-shift with "
    "increasing MDACl2 content, from 826 nm (x=0) to 824, 822, 820 nm, and 816 nm "
    "for the control (0.95 FAPbI3/0.05 MAPbBr3) [@Min2019].",
    title="UV-vis absorption spectra method and results",
)

pl_spectra = claim(
    "Photoluminescence (PL) emission peaks for FAPbI3:xMDACl2 films shifted from "
    "826 nm (x=0) to 824, 822, and 820 nm for x = 1.9, 3.8, and 5.7 mol% MDACl2, "
    "respectively, consistent with the UV-vis blue-shift. The control (0.95 FAPbI3/"
    "0.05 MAPbBr3) showed a PL peak at 816 nm, indicating a larger bandgap widening "
    "from MAPbBr3 incorporation compared to MDACl2 incorporation [@Min2019].",
    title="PL emission peak shifts with MDACl2 content",
)

ftir_confirms_mda = claim(
    "Fourier-transform infrared spectroscopy (FT-IR) and nuclear magnetic resonance "
    "imaging (NMR) confirmed the presence of MDA in the perovskite films, indicating "
    "successful incorporation of MDA2+ into the FAPbI3 lattice [@Min2019].",
    title="FT-IR confirmation of MDA incorporation",
)

xrd_phase_analysis = claim(
    "X-ray diffraction (XRD) patterns of FAPbI3:xMDACl2 (x = 0, 1.9, 3.8, 5.7 mol%) "
    "and the control exposed to 80% humidity for 24 hours after annealing showed "
    "characteristic alpha-phase peaks at 14.3 and 28.6 degrees (001 and 002 crystal "
    "planes) and a delta-phase peak at 11.6 degrees. Pure FAPbI3 (x=0) completely "
    "converted to delta-phase after 24 hours at 80% humidity, while 3.8 and 5.7 mol% "
    "MDACl2 samples retained the alpha-phase [@Min2019].",
    title="XRD phase stability under humidity",
)

giwaxs_analysis = claim(
    "Grazing-incidence wide-angle X-ray scattering (GIWAXS) analysis of x=3.8 mol% "
    "MDACl2 and control showed diffraction rings assigned to alpha-FAPbI3-(100)c, "
    "alpha-FAPbI3-(200)c, alpha-FAPbI3-(210)c, delta-FAPbI3-(100)h, and PbI2-(001)t. "
    "No appreciable differences were observed between samples, and no peaks related "
    "to FACl or MDACl2 were detected, confirming MDA substitution into the FAPbI3 "
    "lattice without forming secondary phases [@Min2019].",
    title="GIWAXS analysis of crystal phases",
)

xps_cl_content = claim(
    "X-ray photoelectron spectroscopy (XPS) showed that the residual Cl content in "
    "FAPbI3 with 3.8 mol% MDACl2 was higher than in the control. The Cl was "
    "concentrated at the interface with the TiO2 electrode, which is expected to "
    "increase light stability of PSCs. The small Cl content in the control is "
    "consistent with previously reported results from the MACl mediator process "
    "[@Min2019, refs 43-44].",
    title="XPS Cl depth profile",
)

tofsims_cl_mapping = claim(
    "Time-of-flight secondary-ion mass spectrometry (ToF-SIMS) of the "
    "FTO/Bi-TiO2/mp-TiO2/perovskite structure showed higher Cl anion concentration "
    "in the target (3.8 mol% MDACl2) compared to the control. The Cl was enriched "
    "at the perovskite/TiO2 interface, consistent with the XPS results [@Min2019].",
    title="ToF-SIMS Cl mapping",
)

defect_density_sclc = claim(
    "Electron-only devices with structure FTO/SnO2/perovskite/PCBM/Au were fabricated "
    "to measure trap density via space-charge-limited current (SCLC) analysis. "
    "The trap-filled limit voltage in the J-V curve was used with the equation "
    "N_defects = 2*epsilon*epsilon0*V_TFL / (e*L^2) to calculate defect densities. "
    "Defect densities were: x=0 (5.4e15 cm-3), x=1.9 (7.6e15 cm-3), x=3.8 "
    "(5.7e15 cm-3), x=5.7 (8.0e15 cm-3), and control (1.0e16 cm-3) [@Min2019].",
    title="SCLC defect density measurements",
)

pl_lifetime = claim(
    "Time-resolved photoluminescence (TRPL) was measured on perovskite films "
    "deposited on quartz substrates using a time-correlated single-photon counting "
    "instrument. The non-radiative recombination lifetime was obtained using a "
    "biexponential equation: Y = A1*exp(-t/tau1) + A2*exp(-t/tau2), where tau1 and "
    "tau2 are fast and slow decay constants related to radiative and trap-assisted "
    "nonradiative recombination, respectively. The target (3.8 mol% MDACl2) showed "
    "a longer lifetime of 1562 ns compared to the control (715 ns) [@Min2019].",
    title="TRPL charge carrier lifetime",
)

j_v_measurement = claim(
    "Current density-voltage (J-V) characteristics were measured under standard AM 1.5 "
    "conditions (100 mW/cm2) in reverse and forward bias sweep modes. Certified "
    "measurements used the quasi-steady-state (QSS) method at an accredited laboratory "
    "(Newport, USA) [@Min2019].",
    title="J-V measurement conditions",
)

eqe_spectral_response = claim(
    "External quantum efficiency (EQE) was measured to characterize the wavelength-"
    "dependent photocurrent generation. The target device showed expanded absorption "
    "wavelength range compared to the control, consistent with the narrower bandgap "
    "maintained by MDACl2 stabilization [@Min2019].",
    title="EQE spectral response measurement",
)

stability_test_protocols = claim(
    "Stability tests were conducted under three conditions: (1) humidity stability "
    "at 85% RH and 25C for unencapsulated devices, (2) thermal stability at 150C "
    "and approximately 25% RH for unencapsulated devices, and (3) photostability "
    "with maximum power point (MPP) tracking under full AM 1.5G illumination "
    "(100 mW/cm2) in ambient conditions without UV filter, using encapsulated devices "
    "[@Min2019].",
    title="Stability test protocols",
)

# -----------------------------------------------------------------------------
# Theoretical calculations
# -----------------------------------------------------------------------------

dft_bandgap_calculation = claim(
    "Density functional theory (DFT) calculations were performed to compute "
    "bandgap changes from MDACl2 incorporation using two composition models: "
    "FA vacancy (Eq. 1) and Cl interstitial (Eq. 2). The FA vacancy composition "
    "yielded a bandgap of 1.47 eV (slightly above pristine FAPbI3 at 1.45 eV), "
    "while the Cl interstitial composition gave 1.69 eV (significantly increased) "
    "[@Min2019].",
    title="DFT bandgap calculation methodology",
)

xrd_peak_shift = claim(
    "XRD patterns of FAPbI3:xMDACl2 films showed that the (001) orientation peak "
    "shifted to a lower angle with increasing MDACl2 content (x=3.8 and 5.7 mol%), "
    "indicating an expanded unit cell. This expansion is consistent with interstitial "
    "Cl- ions rather than lattice contraction from increased hydrogen bonding "
    "[@Min2019].",
    title="XRD peak shift indicating lattice expansion",
)

__all__ = [
    "deposition_method",
    "surface_passivation",
    "device_structure",
    "uvvis_absorption",
    "pl_spectra",
    "ftir_confirms_mda",
    "xrd_phase_analysis",
    "giwaxs_analysis",
    "xps_cl_content",
    "tofsims_cl_mapping",
    "defect_density_sclc",
    "pl_lifetime",
    "j_v_measurement",
    "eqe_spectral_response",
    "stability_test_protocols",
    "dft_bandgap_calculation",
    "xrd_peak_shift",
]