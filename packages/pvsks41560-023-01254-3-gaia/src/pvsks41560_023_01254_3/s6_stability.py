"""
Stability of bifacial minimodules (Section 5 of Gu2023).

Covers: operational stability under light soaking, damp-heat stability,
and the role of ALD SnO2 and perovskite composition in stability enhancement.
"""

from gaia.lang import claim, setting

# Initial PCE retention after 6000h light soaking
initial_pce_retention_6000h = claim(
    "The best bifacial minimodule retained 97% of its initial power conversion efficiency "
    "(T97) after light soaking for over 6,000 hours from the front side at open-circuit "
    "condition and temperature of 60 plus/minus 5 degrees C under simulated 1-sun illumination "
    "in air, representing the most stable reported perovskite minimodule [@Gu2023].",
    title="97% retention after 6000h light soaking at 60C",
)

# Damp-heat retention
damp_heat_retention = claim(
    "Another bifacial minimodule maintained approximately 84% of its initial efficiency "
    "after damp-heat testing for over 1,000 hours at 85 degrees C and approximately 85% "
    "relative humidity, demonstrating good stability under damp-heat conditions [@Gu2023].",
    title="84% retention after 1000h damp-heat at 85C/85% RH",
)

# ALD SnO2 stabilization benefit
ald_sno2_stabilization_benefit = claim(
    "The very good stability of these bifacial minimodules benefits from the ALD SnO2 "
    "buffer layer in addition to the intrinsic stability of FA_0.92Cs_0.08PbI3: first, ALD SnO2 "
    "greatly reduced damage to perovskite in the laser scribing process, preventing formation "
    "of amorphous perovskites with reduced PL intensity around P2 scribing lines; second, "
    "replacing amorphous BCP (which can recrystallize during operation) with ALD SnO2 "
    "stabilized the C60/electrode interface [@Gu2023].",
    title="ALD SnO2 stabilizes interface and prevents recrystallization",
)

# Stability benefits from composition
stability_benefits_composition = claim(
    "The stability benefits of these bifacial minimodules arise from two factors: the ALD SnO2 "
    "layer which protects against laser scribing damage and prevents BCP recrystallization, "
    "and the intrinsically stable FA_0.92Cs_0.08PbI3 perovskite composition optimized by "
    "previous methods that demonstrates good light stability [@Gu2023].",
    title="Stability from ALD SnO2 and FA-Cs perovskite composition",
)