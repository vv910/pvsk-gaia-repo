"""
Photovoltaic performance of perovskite/silicon TSCs with different SAMs.

This module covers device performance, J-V curves, EQE, and certification results.
"""

from gaia.lang import (
    claim,
    setting,
)

# Device configuration
device_configuration = claim(
    "The top perovskite solar cells were fabricated based on different SAMs with the stack "
    "of IZO/SAM/perovskite/LiF/ethylenediammonium diiodide (EDAI)/C60/SnO2/IZO/Ag/MgF2, "
    "using silicon heterojunction solar cells as the bottom cells for monolithic perovskite/silicon TSCs.",
    title="Device configuration for TSCs",
)

# Statistical performance - box plots data
htl201_average_pce = claim(
    "For devices utilizing HTL201, an average PCE of 34.22% was achieved across 20 independent devices.",
    title="HTL201 average PCE 34.22%",
)

htl201_champion_pce = claim(
    "The champion TSC using HTL201 achieved an efficiency of 34.60%, with a Voc of up to 2.001 V, "
    "a short-circuit current density (Jsc) of 20.64 mA cm^-2 and a fill factor (FF) of 83.79%.",
    title="HTL201 champion device: 34.60% PCE, 2.001V Voc",
)

me4pacz_average_pce = claim(
    "The average PCEs for Me-4PACz and MeO-4PACz were 32.18% and 33.34%, respectively.",
    title="Me-4PACz and MeO-4PACz average PCEs",
)

htl201_enhanced_voc_ff = claim(
    "The HTL201-bearing devices showed significantly enhanced Voc and FF compared with the "
    "other two SAMs.",
    title="HTL201 shows enhanced Voc and FF",
)

# EQE data
eqe_integrated_current = claim(
    "The integrated photogenerated current densities from external quantum efficiency (EQE) "
    "curves are calculated to be 21.50 mA cm^-2 and 20.70 mA cm^-2 for the perovskite top "
    "subcell and silicon bottom subcell, respectively.",
    title="EQE integrated currents: 21.50 and 20.70 mA/cm2",
)

# Certified result
certified_pce_34_58 = claim(
    "One optimized HTL201-based TSC was sent to the European Solar Test Installation for "
    "certification, demonstrating a certified PCE of 34.58%.",
    title="Certified PCE 34.58% by ESTI",
)

htl201_derivatives_also_good = claim(
    "HTL201-like derivatives named HTL207 and HTL203 with different aliphatic chain lengths "
    "(n=2 and n=4) also delivered higher efficiency compared with the Me-4PACz- and MeO-4PACz-based "
    "devices, although HTL201 shows the best performance among the HTL201-like derivatives.",
    title="HTL201 derivatives also perform well",
)

__all__ = [
    "device_configuration",
    "htl201_average_pce",
    "htl201_champion_pce",
    "me4pacz_average_pce",
    "htl201_enhanced_voc_ff",
    "eqe_integrated_current",
    "certified_pce_34_58",
    "htl201_derivatives_also_good",
]