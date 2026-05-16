"""
s4_discussion.py - Discussion and Conclusions

This module covers the interpretation of results, the MSSC mechanism,
limitations, and future outlook.
"""
from gaia.lang import claim, setting

# ============ MSSC Mechanism ============

# Electron transport in MSSC
electron_transport_mssc = claim(
    "In Al2O3-based cells, electrons must remain in the perovskite phase until "
    "collected at the planar TiO2-coated FTO electrode, and must be transported "
    "throughout the film thickness in the perovskite [@Lee2012].",
    title="Electron transport in MSSC"
)

# Hole transfer in MSSC
hole_transfer_mssc = claim(
    "Hole transfer from photoexcited perovskite to spiro-OMeTAD occurs in both "
    "TiO2- and Al2O3-based cells in much the same way [@Lee2012].",
    title="Hole transfer mechanism in MSSC"
)

# Al2O3 does not act as n-type
al2o3_not_ntype = claim(
    "Al2O3 did not act as an n-type oxide in DSSCs - it is truly inert "
    "[@Lee2012].",
    title="Al2O3 is inert scaffold"
)

# Perovskite faster transport
perovskite_transport_speed = claim(
    "Electron transport through the perovskite layer is much faster than through "
    "n-type TiO2, as evidenced by charge collection being > 10 times faster in "
    "Al2O3 devices [@Lee2012].",
    title="Perovskite electron transport speed"
)

# ============ Junction Type Question ============

# Excitonic vs distributed p-n junction
junction_type = claim(
    "A central question is whether the MSSC is excitonic or a distributed p-n "
    "junction. Perovskites tend to form layered structures with quasi-two-dimensional "
    "confinement that can result in exciton binding energy up to a few hundred "
    "meV [@Lee2012].",
    title="Junction type question"
)

# Planar junction interpretation
planar_junction_interp = claim(
    "Reasonably high photocurrents from planar-junction solar cells could be "
    "explained by either moderately delocalized and highly mobile excitons being "
    "quenched at the perovskite-spiro-OMeTAD interface, or generation of free "
    "charges in the bulk of perovskite films with reasonably good electron and "
    "hole migration [@Lee2012].",
    title="Planar junction photocurrent interpretation"
)

# ============ Performance Limitations ============

# Series-shunt tradeoff
series_resistance_tradeoff = claim(
    "The key limitation in MSSC performance is a balance between series and shunt "
    "resistance. Short-circuiting occurs if contact exists between silver electrode "
    "and perovskite absorber, but thick spiro-OMeTAD capping layer results in high "
    "series resistance due to its lower conductivity (10^-5 S cm^-1 vs perovskite's "
    "10^-3 S cm^-1) [@Lee2012].",
    title="Series-shunt resistance tradeoff"
)

# ============ Key Achievement ============

# Main achievement
main_achievement = claim(
    "The application of a mesostructured insulating scaffold upon which extremely "
    "thin films of n-type and p-type semiconductors are assembled (MSSC) has proven "
    "extraordinarily effective with n-type perovskite, delivering more than 10.9% "
    "power conversion efficiency under full solar illumination [@Lee2012].",
    title="Main achievement: 10.9% efficiency"
)

# Fundamental loss reduction
fundamental_loss_reduction = claim(
    "The meso-superstructured solar cell exhibits exceptionally few fundamental "
    "energy losses, capable of generating open-circuit voltage of more than 1.1 V "
    "despite the relatively narrow absorber band gap of 1.55 eV, resulting in a "
    "voltage deficit of only 0.45 eV competitive with best thin-film technologies "
    "[@Lee2012].",
    title="Reduction of fundamental losses"
)

# ============ Future Directions ============

# Absorption extension
future_absorption = claim(
    "Further advances in power conversion efficiency could come from extending "
    "the absorption onset toward 940 nm through new perovskites or broadening "
    "to other solution-processable semiconductors [@Lee2012].",
    title="Future: extend absorption"
)

# Photocurrent enhancement
future_photon_management = claim(
    "Enhanced light absorption near the band edge through carefully engineered "
    "mesostructures or better photon management would increase photocurrent "
    "[@Lee2012].",
    title="Future: photon management"
)

# Fill factor improvement
future_fill_factor = claim(
    "Reduced series resistance through higher-mobility hole transporters or better "
    "control over capping layer thickness would improve fill factor [@Lee2012].",
    title="Future: fill factor improvement"
)

# Multijunction potential
future_multijunction = claim(
    "Extending the MSSC concept to multijunction devices could further enhance "
    "performance without the requirement for lattice matching as in conventional "
    "multijunction solar cells [@Lee2012].",
    title="Future: multijunction devices"
)

# ============ Broader Impact ============

# Remote sensing application
remote_sensing_principle = claim(
    "Entanglement-enabled angular rotation measurement precision increases by "
    "factor l relative to polarization-entangled pairs, applicable to low-light "
    "scenarios like biological imaging [@pvsk2012_2].",
    title="High-OAM entanglement for remote sensing"
)

# Classical analog
classical_analog = claim(
    "An analogous improvement can be achieved classically if diagonally or circularly "
    "polarized light enters the transfer setup, but entanglement enables remote "
    "measurements with spatially separated photons or photons in unknown locations "
    "[@pvsk2012_2].",
    title="Classical vs quantum remote sensing"
)

__all__ = [
    # Mechanism
    "electron_transport_mssc",
    "hole_transfer_mssc",
    "al2o3_not_ntype",
    "perovskite_transport_speed",
    # Junction
    "junction_type",
    "planar_junction_interp",
    # Limitations
    "series_resistance_tradeoff",
    # Achievements
    "main_achievement",
    "fundamental_loss_reduction",
    # Future
    "future_absorption",
    "future_photon_management",
    "future_fill_factor",
    "future_multijunction",
    # Broader
    "remote_sensing_principle",
    "classical_analog",
]