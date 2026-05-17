"""
Discussion and Device Performance Results.

This module covers the solar cell fabrication, efficiency measurements,
and stability test results (Figures 4-5, lines 56-90).
"""

from gaia.lang import claim, setting

# Device Architectures
spiro_omeTAD_architecture = setting(
    "Standard mesoporous configuration with TiO2 blocking layer (30 nm spray pyrolysis), "
    "mesoporous TiO2 layer (400 mg/ml Dyesol 30NRD paste), perovskite layer (1.25 M PbI2:MAI 1:1 in DMSO), "
    "Spiro-OMeTAD hole transporting layer (28.9 mg in 400 μl chlorobenzene with Li-TFSI, TBP, Co(II)TFSI dopants), "
    "and 100 nm Au electrode [@Grancini2017].",
    title="Spiro-OMeTAD/Au device structure",
)

htm_free_architecture = setting(
    "HTM-free carbon-based mesoscopic architecture: FTO/compact TiO2 (aerosol spray pyrolysis)/"
    "nanoporous TiO2 (1 μm screen-printed)/ZrO2 spacer (2 μm)/carbon black/graphite counter electrode (10 μm). "
    "Perovskite infiltrated via drop casting from γ-butyrolactone solution. Fully printable process in air [@Grancini2017].",
    title="HTM-free carbon-based architecture",
)

# Device Performance Results
spiro_cell_efficiency = claim(
    "The 2D/3D perovskite cell with optimal 3% AVAI in Spiro-OMeTAD/Au configuration delivers "
    "champion efficiency of 14.6% (compared to average >13% for pure 3D CH3NH3PbI3 cells in same architecture) [@Grancini2017].",
    title="Spiro-OMeTAD cell achieves 14.6% PCE",
    metadata={"figure": "artifacts/images/*.jpg", "caption": "Fig. 4b | J-V curve for champion 14.6% device"},
)

spiro_cell_stability = claim(
    "Under continuous AM 1.5G illumination (argon, 45°C), the 2D/3D cell with Spiro-OMeTAD maintains "
    "up to 60% of initial PCE after 300h, showing much better stability than standard 3D cells under same conditions [@Grancini2017].",
    title="Spiro cell stability improved with 2D/3D",
    metadata={"figure": "artifacts/images/*.jpg", "caption": "Fig. 4c | 60% retained after 300h"},
)

htm_free_cell_performance = claim(
    "Small area HTM-free cells (0.64 cm2) achieve champion efficiency of 12.71%. "
    "This ranges among the highest reported for HTM-free devices (7-14% range) [@Grancini2017].",
    title="HTM-free cell achieves 12.71% PCE",
    metadata={"figure": "artifacts/images/*.jpg", "caption": "Fig. 5a | Champion cell J-V curve"},
)

module_performance = claim(
    "10x10 cm2 module with geometric fill factor (GFF) of 46.7% and active area of 47.6 cm2 "
    "(8 cells of 85x7 mm2 each) achieves champion efficiency of 11.2%. "
    "Interconnect distance ~3 mm and large margins contribute to area loss [@Grancini2017].",
    title="10x10 cm2 module delivers 11.2% PCE",
    metadata={"figure": "artifacts/images/*.jpg", "caption": "Fig. 5b | Module J-V curve"},
)

module_stability_test = claim(
    "Module stability test under AM 1.5G (1000 W/m2), cycling temperature up to 90°C in ambient air "
    "(ISOS standard conditions) shows extraordinary stability >10,000h with zero loss in performance "
    "over >400 days. Initial increase detected in first 500h, possibly due to light/field-induced "
    "ion movement, structural rearrangement, or interfacial charge accumulation [@Grancini2017].",
    title="Module stable >10,000h with zero efficiency loss",
    metadata={"figure": "artifacts/images/*.jpg", "caption": "Fig. 5c | 10,000h stability test"},
)

hysteresis_observation = claim(
    "The HTM-free devices show not negligible hysteresis, with differences in J-V characteristics "
    "between forward and back scan directions (Supplementary Table 4). This is subject to ongoing "
    "investigation [@Grancini2017].",
    title="Hysteresis observed in HTM-free devices",
)

# Scaling and Reproducibility
module_gff = claim(
    "The module geometric fill factor (ratio of active area to total area) is 46.7%, "
    "within range observed for fully printed organic photovoltaic modules. "
    "Further optimization could reduce interconnect distance and improve efficiency [@Grancini2017].",
    title="Module GFF of 46.7%",
)

reproducibility = claim(
    "Solar cell reproducibility: Spiro-OMeTAD cells - 2 batches of 16 devices produced twice. "
    "HTM-free - 1 batch of 10x10 glass with 18 cells, 9 batches total. Modules - >10 at submission, "
    "20 total. Data reproducible comparing batch to batch [@Grancini2017].",
    title="Device reproducibility across batches",
)

# Key Achievement Summary
one_year_stability_record = claim(
    "The >10,000h stability at controlled standard conditions (55°C, 1 sun, ambient atmosphere) "
    "represents the highest record value for perovskite photovoltaics, surpassing previous results "
    "with a significant step improvement. This enables timely commercialization pathway [@Grancini2017].",
    title="Record stability enables commercialization pathway",
)

upscale_potential = claim(
    "The fully printable industrial-scale process at 10x10 cm2 demonstrates up-scale potential, "
    "with optimization possible by reducing interconnect distance and margins, which would increase "
    "efficiency per total area and reduce ohmic losses in active area [@Grancini2017].",
    title="Fully printable process enables industrial scale-up",
)