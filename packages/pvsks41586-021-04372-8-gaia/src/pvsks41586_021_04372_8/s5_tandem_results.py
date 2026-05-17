"""
Performance and stability of all-perovskite tandem solar cells.

Results module covering tandem device performance and operational stability
from Lin et al., Nature 2022.
"""

from gaia.lang import claim, support

# WBG subcell performance
wbg_cell_pce = claim(
    "Wide-bandgap (WBG) solar cells exhibited a PCE of 17.3% with Voc of 1.22 V, "
    "Jsc of 17.4 mA cm^-2, and FF of 81.6%.",
    title="WBG subcell performance",
)

# Tandem device optimization
thicknesses_optimized = claim(
    "The thicknesses of WBG and NBG absorber layers for front and back subcells were optimized "
    "to approximately 380 nm and 1,200 nm, respectively, to obtain a high matched current density "
    "between subcells.",
    title="Optimal thickness configuration for tandem cells",
    metadata={"figure": "artifacts/images/80c9d3e7d7cd06ae1a65b839f1cf1de319230454421a3a7842dab90012a4914d.jpg",
              "caption": "Fig. 4a | Cross-sectional SEM image of all-perovskite tandem solar cell."},
)

jsc_increases_with_nbg_thickness = claim(
    "The Jsc values (from J-V curves) increased from 15.4 to 16.5 mA cm^-2 when the thickness "
    "of the NBG perovskite absorber increased from 750 to 1,200 nm, with WBG thickness kept at "
    "approximately 380 nm.",
    title="Tandem Jsc increases with NBG thickness",
    metadata={"figure": "artifacts/images/af9b1d8883f16c03046d46bc6ea7b8a17ea7af2b04d05a5093006418c048657.jpg",
              "caption": "Fig. 4b,c | J-V and EQE curves of tandem cells with various NBG thicknesses."},
)

pce_increases_with_thickness = claim(
    "The PCE increased from 25.0% for the 750-nm-thick NBG subcell to 26.4% for the 1.2-micrometer-thick "
    "NBG subcell, mainly due to higher spectral response (light absorption) in the back subcell.",
    title="Tandem PCE increases with NBG thickness",
)

# Best tandem device
best_tandem_reverse = claim(
    "The best tandem cell had a PCE of 26.7% from the reverse scan (with Voc of 2.03 V, "
    "Jsc of 16.5 mA cm^-2, and FF of 79.9%), and exhibited a stabilized PCE of 26.6%.",
    title="Best tandem device reverse scan performance",
    metadata={"figure": "artifacts/images/b69485a62009b0dbfe13d50c195692c533cd00a3add9856ed4e0058336ee106e.jpg",
              "caption": "Fig. 4d,e | J-V and EQE curves of the best tandem device."},
)

eqe_matched_currents = claim(
    "The integrated Jsc values from EQE spectra of front and back subcells were 16.7 and "
    "16.8 mA cm^-2, respectively, agreeing well with the Jsc value from J-V measurements.",
    title="EQE shows well-matched subcell currents",
)

average_tandem_96_devices = claim(
    "Ninety-six all-perovskite tandem solar cells (with aperture area of 0.049 cm^2) with "
    "1.2-micrometer-thick NBG subcells had an average PCE of 25.6 +/- 0.5%.",
    title="Average PCE of 25.6% across 96 tandem devices",
)

# Certified performance
certified_pce_264_percent = claim(
    "Independent certification by Japan Electrical Safety and Environment Technology Laboratories "
    "(JET) delivered certified stabilized PCEs of 26.4% and 26.1%, included in Solar Cell "
    "Efficiency Tables (version 58), exceeding other thin-film solar cells and comparable to "
    "best single-crystalline silicon solar cells.",
    title="Certified PCE of 26.4% by JET",
)

# Large-area devices
large_area_tandem = claim(
    "A large-area tandem device (aperture area 1.05 cm^2) exhibited a PCE of 25.3% with Voc of "
    "2.03 V, Jsc of 16 mA cm^-2, and FF of 78%, with the performance gap attributed to improved "
    "film uniformity from formamidine sulfinic acid (FSA) addition.",
    title="Large-area tandem device performance",
    metadata={"figure": "artifacts/images/257a3424c5998cd1b884730ca241248640a90924fb6783852f4261a4fb1b0878.jpg",
              "caption": "Fig. 4f | J-V curve of large-area tandem device."},
)

# Stability
shelf_stability_2400h = claim(
    "Unencapsulated tandem devices exhibited no obvious PCE degradation after 2,400 hours of "
    "aging under dark conditions in N2 glovebox.",
    title="Shelf stability over 2400 hours",
)

operational_stability_600h = claim(
    "CF3-PA-passivated tandem devices maintained 90% of their initial PCE after 600 hours of "
    "maximum power point (MPP) operation under 1 Sun illumination (AM1.5G, 100 mW cm^-2) in "
    "ambient air (humidity 30-50%), exhibiting improved operating stability compared to "
    "unpassivated control devices.",
    title="CF3-PA tandem retains 90% PCE after 600h operation",
    metadata={"figure": "artifacts/images/5e01e10e5f893331f1cd5ac0875715e5b2a6a0f03561d298d0d09b3bd13f3390.jpg",
              "caption": "Fig. 4g | Continuous MPP tracking showing operational stability."},
)

__all__ = [
    "wbg_cell_pce",
    "thicknesses_optimized",
    "jsc_increases_with_nbg_thickness",
    "pce_increases_with_thickness",
    "best_tandem_reverse",
    "eqe_matched_currents",
    "average_tandem_96_devices",
    "certified_pce_264_percent",
    "large_area_tandem",
    "shelf_stability_2400h",
    "operational_stability_600h",
]