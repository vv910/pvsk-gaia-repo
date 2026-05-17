"""
Interface interactions between SAMs and IZO/TCO substrates.

This module covers XPS measurements, molecular dynamics simulations,
and binding energy calculations.
"""

from gaia.lang import (
    claim,
    setting,
)

# XPS measurements - coordination interaction
izo_htl201_strong_interaction = claim(
    "When compared with pristine IZO, the characteristic Zn 2p and In 3d signals of the "
    "IZO/HTL201 show significant shifts of about 0.7 eV and 0.5 eV, respectively. These shifts "
    "are more pronounced than those observed in IZO/MeO-4PACz (about 0.5 eV and 0.35 eV) and "
    "IZO/Me-4PACz (about 0.1 eV and 0.15 eV), indicating that HTL201 has a stronger interaction "
    "with the IZO recombination layer.",
    title="HTL201 shows strongest XPS shifts on IZO",
)

htl201_stronger_affinity = claim(
    "HTL201 has a stronger affinity for the IZO surface than Me-4PACz and MeO-4PACz, as "
    "demonstrated by calculated adsorption energies as a function of simulation time.",
    title="HTL201 stronger affinity for IZO surface",
)

htl201_higher_fractional_coverage = claim(
    "HTL201 molecules showed higher fractional coverage on the IZO surface compared to "
    "Me-4PACz and MeO-4PACz, as observed in molecular dynamics simulations.",
    title="HTL201 has highest fractional coverage",
)

# Coverage factor measurements
coverage_factors_before_wash = claim(
    "The calculated coverage factors for as-deposited Me-4PACz-, MeO-4PACz- and HTL201-modified "
    "IZO substrates before washing were 19.38 x 10^-3, 16.40 x 10^-3 and 12.96 x 10^-3, "
    "respectively.",
    title="Coverage factors before washing",
)

coverage_factors_stable = claim(
    "The coverage factors of Me-4PACz, MeO-4PACz and HTL201 showed negligible variation as "
    "the number of washing cycles increased from one to five, indicating stable SAM formation.",
    title="Coverage factors stable across washing cycles",
)

htl201_higher_coverage_factor = claim(
    "In both cases with and without washing, HTL201-coated IZO substrates always showed a "
    "higher coverage factor value compared with the other two SAMs, further indicating that "
    "HTL201 can form a denser thin film.",
    title="HTL201 always shows highest coverage factor",
)

# Thickness measurements
sam_thickness_comparable_to_molecule_length = claim(
    "The specific thickness values obtained were comparable to the molecule length, indicating "
    "that the molecules anchored to the substrate formed a monolayer after solvent washing.",
    title="SAM thickness indicates monolayer formation",
)

# Binding energy calculations
htl201_strong_binding_perovskite = claim(
    "HTL201 shows the highest binding energy with the perovskite film among the three SAMs, "
    "driven by an enhanced dipole moment (mu) induced by the asymmetric molecular structure "
    "design of HTL201 which promotes polar dipole interaction between the perovskite and the SAM.",
    title="HTL201 has strongest binding to perovskite",
)

htl201_passivates_pb_defects = claim(
    "HTL201 shows a higher binding energy and a shorter distance (D[N-Pb]) between the N in "
    "the SAM and the Pb2+ defect in the perovskite film compared with Me-4PACz and MeO-4PACz. "
    "Therefore, the coordination interaction between HTL201 and the Pb2+ defect can passivate "
    "the defects at the SAM/perovskite surface.",
    title="HTL201 coordinates with Pb2+ to passivate defects",
)

__all__ = [
    "izo_htl201_strong_interaction",
    "htl201_stronger_affinity",
    "htl201_higher_fractional_coverage",
    "coverage_factors_before_wash",
    "coverage_factors_stable",
    "htl201_higher_coverage_factor",
    "sam_thickness_comparable_to_molecule_length",
    "htl201_strong_binding_perovskite",
    "htl201_passivates_pb_defects",
]