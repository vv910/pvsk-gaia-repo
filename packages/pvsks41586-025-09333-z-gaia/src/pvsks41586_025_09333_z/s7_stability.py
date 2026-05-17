"""
Long-term stability of perovskite/silicon TSCs.

This module covers shelf-life stability and operational stability measurements.
"""

from gaia.lang import (
    claim,
    setting,
)

# Shelf-life stability
htl201_shelf_life_98_9_percent = claim(
    "The HTL201-based TSCs retained approximately 98.9% of the initial efficiency after "
    "1,080 h of storage. In comparison, the MeO-4PACz- and Me-4PACz-bearing TSCs retained "
    "only 94.6% and 84.8% of their initial PCEs, respectively.",
    title="HTL201 retains 98.9% PCE after 1080h storage",
)

# Operational stability - 25°C
htl201_operational_25c_98_percent = claim(
    "After operating for 1,020 h, the devices based on HTL201 retained about 98.0% of their "
    "initial PCE at a controlled temperature of 25 degrees C under 1-sun continuous illumination.",
    title="HTL201 retains 98.0% PCE after 1020h at 25C",
)

# Operational stability - 45°C
htl201_operational_45c_91_3_percent = claim(
    "After operating for 1,020 h, the devices based on HTL201 retained about 91.3% of their "
    "initial PCE at an elevated temperature of 45 degrees C under 1-sun continuous illumination.",
    title="HTL201 retains 91.3% PCE after 1020h at 45C",
)

meo4pacz_operational_stability = claim(
    "The MeO-4PACz-based devices retained 89.6% and 84.4% of their initial PCEs at 25 degrees C "
    "and 45 degrees C, respectively, after 1,020 h of operation.",
    title="MeO-4PACz retains 89.6% at 25C and 84.4% at 45C",
)

me4pacz_significant_decline = claim(
    "The Me-4PACz-based device experienced a significant decline after 500 h of operation.",
    title="Me-4PACz shows significant decline after 500h",
)

# Electrochemical stability
htl201_better_electrochemical_stability = claim(
    "During the continuous anodic scan, after 30 cycles, the redox peak current densities of "
    "Me-4PACz and MeO-4PACz decreased significantly, and the initial chemical species gradually "
    "converted into oxidation products. This observation suggests that both Me-4PACz and MeO-4PACz "
    "exhibit lower electrochemical stability compared with HTL201.",
    title="HTL201 has better electrochemical stability",
)

# Photostability
all_sams_good_photostability = claim(
    "The 1H NMR spectra of all three SAMs showed almost no changes following 24 h of continuous "
    "illumination ageing test, demonstrating the considerable photostability of the Me-4PACz, "
    "MeO-4PACz and HTL201 molecules.",
    title="All SAMs show good photostability",
)

# Mechanism explanation
htl201_impeded_leakage_reduced_recombination = claim(
    "The impeded leakage current and reduced non-radiative recombination of HTL201 at the "
    "buried interface can ensure that the complete device has good operational stability "
    "under illumination.",
    title="HTL201 stability mechanism: impeded leakage and reduced recombination",
)

__all__ = [
    "htl201_shelf_life_98_9_percent",
    "htl201_operational_25c_98_percent",
    "htl201_operational_45c_91_3_percent",
    "meo4pacz_operational_stability",
    "me4pacz_significant_decline",
    "htl201_better_electrochemical_stability",
    "all_sams_good_photostability",
    "htl201_impeded_leakage_reduced_recombination",
]