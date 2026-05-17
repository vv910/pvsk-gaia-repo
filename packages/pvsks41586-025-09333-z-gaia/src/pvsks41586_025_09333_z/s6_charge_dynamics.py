"""
Effect of SAMs on charge-carrier dynamics.

This module covers PL mapping, steady-state PL, TRPL, PLQY, QFLS, UPS, and C-AFM measurements.
"""

from gaia.lang import (
    claim,
    setting,
)

# PL mapping and steady-state PL
htl201_brighter_pl_mapping = claim(
    "The perovskite film deposited on HTL201 shows brighter PL mapping images than those on "
    "Me-4PACz and MeO-4PACz, suggesting a lower trap density.",
    title="HTL201 perovskite shows brighter PL mapping",
)

pl_peak_at_733nm = claim(
    "The steady-state PL spectra of perovskite films show a characteristic PL peak at 733 nm, "
    "which is consistent with the bandgap of 1.69 eV.",
    title="PL peak at 733nm consistent with 1.69eV bandgap",
)

# TRPL carrier lifetime
htl201_higher_carrier_lifetime = claim(
    "The perovskite film on HTL201 shows a higher carrier lifetime (5,860 ns) than those on "
    "Me-4PACz (5,574 ns) and MeO-4PACz (1,813 ns), indicating a lower trap density and "
    "suppressed non-radiative recombination at the buried interface.",
    title="HTL201 perovskite has highest carrier lifetime 5860ns",
)

# XPS Pb 4f shifts
htl201_most_significant_pb_shift = claim(
    "The Pb 4f signals of the perovskite films after coating the SAMs all shift to lower binding "
    "energies compared with the bare perovskite film, indicating an increased electron cloud "
    "density around the Pb atoms. The most significant shift of the Pb core level was observed "
    "in the HTL201-modified perovskite film, indicating the stronger interaction between the "
    "perovskite film and HTL201.",
    title="HTL201 causes most significant Pb 4f shift",
)

# PLQY measurements
plqry_values = claim(
    "The PLQY values of perovskite films grown on IZO/Me-4PACz, IZO/MeO-4PACz and IZO/HTL201 "
    "substrates are 0.346%, 0.152% and 0.399%, respectively. The HTL201-based perovskite film "
    "shows the highest PLQY value, indicating the superior ability of diminishing the "
    "recombination loss at the perovskite/HTL interface.",
    title="PLQY values: HTL201 highest at 0.399%",
)

# QFLS analysis
qfls_values = claim(
    "The samples based on Me-4PACz, MeO-4PACz and HTL201 show QFLS values of 1.267 V, 1.246 V "
    "and 1.270 V, respectively. The high QFLS values of Me-4PACz- and HTL201-based solar cells "
    "explain the cause of their high Voc.",
    title="QFLS values: HTL201 1.270V, Me-4PACz 1.267V",
)

# UPS measurements
ups_valence_band = claim(
    "The valence band of the perovskite film is measured to be -5.47 eV by UPS.",
    title="Perovskite valence band -5.47 eV",
)

homo_levels_by_ups = claim(
    "The HOMO of Me-4PACz, MeO-4PACz and HTL201 is -5.66 eV, -5.30 eV and -5.38 eV, "
    "respectively, as measured by UPS.",
    title="UPS measured HOMO levels",
)

htl201_minimal_energy_difference = claim(
    "The minimal energy difference between HTL201 and perovskite (0.09 eV) helps to reduce "
    "Voc loss and facilitate hole extraction. Me-4PACz has a deeper HOMO than the perovskite "
    "valence band, which will partially obstruct hole extraction and result in a low FF.",
    title="HTL201 has minimal energy difference with perovskite",
)

# C-AFM measurements
htl201_highest_conducting_current = claim(
    "According to the C-AFM measurements, perovskite film grown on the HTL201 shows the "
    "highest conducting current flow among the three samples, implying the improved "
    "conductivity of the perovskite film. This also indicates that HTL201 material can "
    "significantly facilitate charge transfer.",
    title="HTL201 perovskite has highest conducting current",
)

# Suns-Voc measurements
htl201_smaller_pff_ff_difference = claim(
    "The group of devices based on HTL201 exhibit the smaller value difference between the "
    "pseudo-FF (pFF) and the actual FF, as well as the lower series resistance (Rs). This "
    "indicates that the transport losses and non-radiative recombination at the buried "
    "interface are significantly suppressed.",
    title="HTL201 devices have smaller pFF-FF difference",
)

htl201_lower_reverse_saturation = claim(
    "The HTL201 device showed a much lower reverse saturation current under dark conditions, "
    "suggesting the suppressed carrier recombination.",
    title="HTL201 has lower reverse saturation current",
)

__all__ = [
    "htl201_brighter_pl_mapping",
    "pl_peak_at_733nm",
    "htl201_higher_carrier_lifetime",
    "htl201_most_significant_pb_shift",
    "plqry_values",
    "qfls_values",
    "ups_valence_band",
    "homo_levels_by_ups",
    "htl201_minimal_energy_difference",
    "htl201_highest_conducting_current",
    "htl201_smaller_pff_ff_difference",
    "htl201_lower_reverse_saturation",
]