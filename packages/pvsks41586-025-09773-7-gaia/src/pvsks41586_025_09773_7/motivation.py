"""
Gaia knowledge package for Lin2025: All-perovskite tandem solar cells with dipolar passivation.
Nature, 2025. https://doi.org/10.1038/s41586-025-09773-7

This module contains Introduction/Motivation content.
"""

from gaia.lang import claim, setting, question

# Background on all-perovskite tandem solar cells
all_perovskite_tandem_description = setting(
    "All-perovskite tandem solar cells vertically stack a wide-bandgap (WBG; ~1.8 eV) mixed bromide/iodide perovskite front cell "
    "with a complementary narrow-bandgap (NBG; ~1.25 eV) mixed lead-tin (Pb-Sn) perovskite rear cell, offering promise to surpass "
    "single-junction perovskite solar cell efficiency while retaining low-cost solution-processing advantages [@Lin2025]."
)

# Problem statement: non-radiative recombination at buried interface
buried_interface_recombination = claim(
    "Non-radiative recombination loss at the hole transport layer (HTL)/perovskite interface in the narrow-bandgap subcell "
    "constrains the power conversion efficiency (PCE) of all-perovskite tandem solar cells [@Lin2025]."
)

# Challenge with conventional passivation
conventional_passivation_limitation = claim(
    "Conventional long-chain amine-based passivation strategies often induce carrier transport losses, limiting both fill factor "
    "and short-circuit current density (Jsc) in mixed Pb-Sn perovskite solar cells due to asymmetric conductivity and insulating barrier formation [@Lin2025]."
)

# Research question
optimal_buried_passivation_requirement = question(
    "How can carrier recombination be minimized at the HTL/perovskite interface while simultaneously establishing an ohmic contact "
    "for efficient carrier extraction in mixed Pb-Sn perovskite solar cells?"
)

# Dipolar passivation strategy overview
dipolar_passivation_strategy = claim(
    "A dipolar-passivation strategy was developed using sulfanilic acid (SA) as the dipolar-passivation molecule, featuring an "
    "-NH3+ passivating group and a -SO3- dipole group, to minimize carrier recombination and improve hole transport at the "
    "HTL/Pb-Sn perovskite interface [@Lin2025]."
)

# SA molecule properties
sa_dipole_moment = claim(
    "Sulfanilic acid (SA) has a dipole moment of 23.58 D [@Lin2025]."
)

# Key outcomes
diffusion_length_enhancement = claim(
    "Dipolar passivation extends the carrier diffusion length to 6.2 μm, compared with 4.8 μm for the control [@Lin2025]."
)

pb_sn_psc_performance = claim(
    "Mixed Pb-Sn perovskite solar cells with dipolar passivation achieve a PCE of 24.9% with an open-circuit voltage (Voc) of 0.911 V, "
    "short-circuit current density (Jsc) of 33.1 mA cm^-2, and fill factor (FF) of 82.6% [@Lin2025]."
)

tandem_performance = claim(
    "All-perovskite tandem solar cells with dipolar passivation achieve a certified stabilized PCE of 30.1% (active area 0.049 cm^2) "
    "and 29.6% (active area 1.05 cm^2), both certified by JET [@Lin2025]."
)

__all__ = [
    "all_perovskite_tandem_description",
    "buried_interface_recombination",
    "conventional_passivation_limitation",
    "optimal_buried_passivation_requirement",
    "dipolar_passivation_strategy",
    "sa_dipole_moment",
    "diffusion_length_enhancement",
    "pb_sn_psc_performance",
    "tandem_performance",
]