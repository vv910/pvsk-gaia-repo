"""
Light scattering by dielectric nanoparticles (Section 4 of Gu2023).

Covers: SiO2 nanoparticle integration to recover absorption loss from absence
of reflective metal electrodes, Mie scattering optimization, and performance gains.
"""

from gaia.lang import claim, setting

# Jsc reduction without reflective electrode
jsc_reduction_without_reflective_electrode = claim(
    "The absence of a reflecting or opaque metal electrode in bifacial device structure "
    "reduces short-circuit current density (Jsc) by approximately 1.3 mA/cm^2 due to "
    "insufficient absorption in the red and near-infrared wavelength range compared with "
    "opaque monofacial cells with metal back reflector [@Gu2023].",
    title="Jsc reduced by 1.3 mA/cm2 without reflective electrode",
)

# SiO2 NP Mie scattering principle
sio2_np_light_scattering = claim(
    "Silicon oxide (SiO2) nanoparticles (NPs) are introduced in perovskite films to scatter "
    "incident sunlight and increase the optical path, based on resonant Mie scattering, "
    "avoiding metal NPs which raise concerns of chemical reaction with perovskites and "
    "strong non-radiative charge recombination at NP surfaces [@Gu2023].",
    title="SiO2 NPs scatter light via Mie resonance",
)

# Optimal NP size range (400-600nm)
optimal_np_size_range = claim(
    "Light-scattering properties of spherical SiO2 NPs studied by 3D finite-difference "
    "time-domain (FDTD) method show that SiO2 NPs should be larger than 400 nm to efficiently "
    "scatter red and near-infrared light and smaller than 600 nm to minimize losing absorption "
    "of UV-visible light in perovskite films [@Gu2023].",
    title="Optimal NP size 400-600nm for red/NIR scattering",
)

# Optimal NP spacing range (1-1.5 µm)
optimal_np_spacing_range = claim(
    "The simulated absorption of incident light by perovskite with different spacings of NPs "
    "shows that perovskite film with NP spacing from 1 to 1.5 micrometers can absorb 5.4 to "
    "19.8% more 800 nm light than pure film from the front side; larger spacing also increases "
    "light absorption but less significantly [@Gu2023].",
    title="Optimal NP spacing 1-1.5 um gives 5.4-19.8% more 800nm absorption",
)

# Absorption enhancement simulation
absorption_enhancement_simulation = claim(
    "FDTD simulation shows that perovskite film embedded with SiO2 NPs with optimal spacing "
    "of 1-1.5 micrometers shows obviously enhanced absorption of red and near-infrared light "
    "by transverse scattering that increases the optical path, with 5.4-19.8% more 800 nm light "
    "absorption compared with film without NPs [@Gu2023].",
    title="FDTD shows 5.4-19.8% enhanced 800nm absorption with optimal NP spacing",
)

# NP synthesis and embedding
np_synthesis_and_embedding = claim(
    "SiO2 NPs with a diameter of 500 nm were synthesized and dispersed in ethanol, then "
    "pre-deposited on ITO substrate using blade coating with N2 flow assistance, forming a "
    "monolayer of NPs nicely embedded in the perovskite layer without causing cracks or voids; "
    "an optimized NP concentration of 30 mg/ml gives NP spacing of 1-2 micrometers and NPs "
    "occupying 1.9-7.6% of the total film volume [@Gu2023].",
    title="500nm SiO2 NPs embedded by blade coating at 30 mg/ml",
)

# No extra recombination from NPs
no_extra_recombination_from_np = claim(
    "Perovskite film with embedded SiO2 NPs exhibited comparable PL intensity and carrier "
    "lifetime with optimized perovskite films without NPs, showing that these NPs do not "
    "introduce an additional non-radiative charge recombination pathway to the perovskite "
    "films [@Gu2023].",
    title="SiO2 NPs do not introduce extra recombination",
)

# Jsc increase with optimal NP
jsc_increase_with_optimal_np = claim(
    "The average front short-circuit current density (Jsc) of bifacial PSCs with optimal SiO2 "
    "NP spacing increased from 23.1 to 23.9 mA/cm^2 without notably changing open-circuit "
    "voltage (Voc) and fill factor, confirming that the SiO2 NPs with optimal spacing did not "
    "introduce extra defects in the perovskite film and did not change the charge collection "
    "or recombination process [@Gu2023].",
    title="Jsc increases from 23.1 to 23.9 mA/cm2 with optimal NPs",
)

# Front PCE improvement with NPs
front_pce_improvement_with_np = claim(
    "The embedding of SiO2 NPs significantly recovered the light absorption loss after "
    "optimizing the concentration, and the front power conversion efficiency of champion "
    "bifacial PSCs increased from 22.1% to 23.2% with optimal NP spacing; the integrated "
    "front Jsc from EQE increased from 22.5 to 23.3 mA/cm^2, matching well with "
    "statistical Jsc measured from I-V scan [@Gu2023].",
    title="PCE increases from 22.1% to 23.2% with optimal SiO2 NPs",
)