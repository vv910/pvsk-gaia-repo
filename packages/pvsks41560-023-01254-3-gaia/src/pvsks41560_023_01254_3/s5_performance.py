"""
Photovoltaic performance of bifacial modules (Section 5 of Gu2023).

Covers: small cell performance, minimodule performance, NREL certification,
and power-generation density measurements.
"""

from gaia.lang import claim, setting

# Small cell front PCE
small_cell_front_pce = claim(
    "The front power conversion efficiency of the champion small-size (8 mm^2) MA_0.7FA_0.3PbI_3 "
    "bifacial perovskite solar cell is comparable to optimized opaque PSCs with copper "
    "electrode, reaching approximately 20.2% [@Gu2023].",
    title="Small cell front PCE ~20.2%",
)

# Small cell rear PCE
small_cell_rear_pce = claim(
    "The rear power conversion efficiency of the champion small-size bifacial perovskite "
    "solar cell reached 18.5%, giving a high bifaciality of approximately 80% [@Gu2023].",
    title="Small cell rear PCE 18.5%, bifaciality ~80%",
)

# Bifaciality of small cell
bifaciality_small_cell = claim(
    "The small-size bifacial perovskite solar cell achieved a bifaciality of approximately 80%, "
    "benefiting from both high front efficiency and rear efficiency of 18.5% [@Gu2023].",
    title="Small cell bifaciality ~80%",
)

# Power generation density at albedo 0.2
power_generation_density_albedo_02 = claim(
    "The bifacial cell with aperture area of 8 mm^2 delivered an estimated power-generation "
    "density of 26.4 mW/cm^2 (PGD_front + albedo times PGD_rear) at an albedo of 0.2, "
    "better than any reported single-junction perovskite solar cells [@Gu2023].",
    title="PGD 26.4 mW/cm2 at albedo 0.2 - best single-junction",
)

# Minimodule front aperture efficiency
minimodule_front_aperture_efficiency = claim(
    "The champion MA_0.7FA_0.3PbI_3 bifacial minimodule with an aperture area over 20 cm^2 "
    "showed a front aperture efficiency of 20.2%, and the rear aperture efficiency was 15.0%, "
    "converting to power-generation densities of 23.2 and 24.7 mW/cm^2 at albedos of 0.2 "
    "and 0.3, respectively [@Gu2023].",
    title="Minimodule front 20.2%, rear 15.0%, area >20 cm2",
)

# Minimodule rear aperture efficiency
minimodule_rear_aperture_efficiency = claim(
    "The rear aperture efficiency of the champion bifacial minimodule was 15.0%, with a "
    "bifaciality of 74.3%, and the power-generation density exceeded 23 mW/cm^2 at an "
    "albedo of 0.2 under 1-sun front illumination [@Gu2023].",
    title="Minimodule rear efficiency 15.0%, bifaciality 74.3%",
)

# NREL certified front efficiency
nrel_certified_front_efficiency = claim(
    "The certified front efficiency of the bifacial minimodule by the National Renewable "
    "Energy Laboratory (NREL) was 19.2% (stabilized), comparable to the best certified "
    "monofacial minimodules, for a minimodule with aperture area of approximately 22.0 cm^2 [@Gu2023].",
    title="NREL certified stabilized front efficiency 19.2%",
)

# NREL certified rear efficiency
nrel_certified_rear_efficiency = claim(
    "The NREL-certified stabilized rear efficiency of the bifacial minimodule was 14.1% "
    "for a minimodule with aperture area of approximately 22.0 cm^2, confirming the "
    "rear-side power generation capability [@Gu2023].",
    title="NREL certified stabilized rear efficiency 14.1%",
)

# Average front efficiency of 8 modules
average_front_efficiency_8_modules = claim(
    "Among eight bifacial minimodules with Ag grids, the average front aperture efficiency "
    "reached 19.5%, demonstrating good reproducibility across multiple devices [@Gu2023].",
    title="Average front efficiency 19.5% across 8 modules",
)

# Average rear efficiency of 8 modules
average_rear_efficiency_8_modules = claim(
    "Among eight bifacial minimodules with Ag grids, the average rear aperture efficiency "
    "reached 14.5%, giving average power-generation densities of 22.4, 23.9, and "
    "25.3 mW/cm^2 with albedos of 0.2, 0.3, and 0.4, respectively [@Gu2023].",
    title="Average rear efficiency 14.5% across 8 modules",
)

# PGD by albedo
pgd_by_albedo = claim(
    "The average power-generation densities of eight bifacial minimodules are 22.4, 23.9, and "
    "25.3 mW/cm^2 at albedos of 0.2, 0.3, and 0.4, respectively, under 1-sun front illumination [@Gu2023].",
    title="Average PGD 22.4-25.3 mW/cm2 for albedos 0.2-0.4",
)