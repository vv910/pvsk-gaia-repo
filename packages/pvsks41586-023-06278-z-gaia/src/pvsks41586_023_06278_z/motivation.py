"""
All-perovskite tandem solar cells with 3D/3D bilayer perovskite heterojunction.

Lin et al., Nature (2023) - https://doi.org/10.1038/s41586-023-06278-z

This module contains the introduction and motivation for developing
3D/3D bilayer perovskite heterojunctions to overcome the performance
limitations of mixed Pb-Sn narrow-bandgap perovskite subcells.
"""

from gaia.lang import (
    claim,
    setting,
    question,
)

#------------------------------------------------------------------------------
# Background on all-perovskite tandem solar cells
#------------------------------------------------------------------------------

tandem_configuration = claim(
    "All-perovskite tandem solar cells comprise a lead-based mixed bromide-iodide "
    "wide-bandgap (WBG, approximately 1.8 eV) perovskite top cell and a mixed "
    "lead-tin (Pb-Sn) narrow-bandgap (NBG, approximately 1.2 eV) perovskite bottom cell.",
    title="All-perovskite tandem configuration",
)

performance_potential = claim(
    "All-perovskite tandem solar cells promise higher power-conversion efficiency (PCE) "
    "than single-junction perovskite solar cells (PSCs) while maintaining low fabrication cost, "
    "owing to increased solar spectrum utilization and reduced thermalization losses.",
    title="Tandem cells offer higher efficiency potential",
)

previous_limitation = claim(
    "Previously reported record-performing all-perovskite tandem solar cells exhibited "
    "undesirable high open-circuit voltage (Voc) deficit and relatively low fill factor (FF) "
    "in the mixed Pb-Sn perovskite bottom cell, primarily caused by non-radiative carrier "
    "recombination at the interface between Pb-Sn perovskites and fullerene (C60)-based "
    "electron transport layer (ETL).",
    title="Previous record tandems had high Voc deficit and low FF",
)

#------------------------------------------------------------------------------
# Problem with 2D/3D heterojunctions
#------------------------------------------------------------------------------

two_d_three_d_problem = claim(
    "Although intermixed 2D/3D perovskite heterojunctions could reduce surface recombination "
    "in PSCs, the 2D layer may hinder charge transport and increase series resistance owing to "
    "asymmetric conductivity and potentially non-uniform distributions.",
    title="2D/3D heterojunctions cause transport losses",
)

surface_passivation_tradeoff = claim(
    "There exists a fundamental trade-off between surface passivation and "
    "passivation-layer conductivity in perovskite heterojunctions.",
    title="Trade-off between passivation and conductivity",
)

#------------------------------------------------------------------------------
# The 3D/3D bilayer PHJ solution
#------------------------------------------------------------------------------

phj_solution = claim(
    "A 3D/3D bilayer perovskite heterojunction (PHJ) with type II band structure "
    "at the Pb-Sn perovskite-ETL interface can suppress interfacial non-radiative "
    "recombination and facilitate charge extraction, while avoiding the transport losses "
    "associated with 2D interlayers.",
    title="3D/3D bilayer PHJ solves the trade-off",
)

type_two_band_alignment = claim(
    "The 3D/3D bilayer PHJ exhibits type II band alignment between Pb-Sn and FL-WBG perovskites, "
    "which reduces hole concentration in the defective interface layer (DIL) and facilitates "
    "electron extraction into the C60 layer.",
    title="Type II band alignment at PHJ",
)

bilateral_improvement = claim(
    "With the 3D/3D bilayer PHJ, both the open-circuit voltage (Voc) and fill factor (FF) "
    "of Pb-Sn PSCs are simultaneously improved, suggesting suppressed non-radiative carrier "
    "recombination along with good electrical contact.",
    title="PHJ simultaneously improves Voc and FF",
)

#------------------------------------------------------------------------------
# Deposition method
#------------------------------------------------------------------------------

hybrid_deposition_method = claim(
    "The bilayer PHJ is formed by depositing a layer of lead-halide wide-bandgap (WBG) "
    "perovskite on top of the mixed Pb-Sn narrow-bandgap (NBG) perovskite through a "
    "non-destructive hybrid evaporation-solution-processing method, which avoids damage "
    "to the underlying Pb-Sn perovskite absorber.",
    title="Hybrid evaporation-solution deposition method",
)

ion_immiscibility = claim(
    "Pb2+ and Sn2+ ion migration is considerably prohibited in the Pb-Sn perovskite system, "
    "enabling the construction of stable 3D/3D bilayer heterostructures with clearly defined "
    "interfaces that persist after fabrication.",
    title="Limited metal-ion intermixing enables stable PHJ",
)

#------------------------------------------------------------------------------
# Key results for NBG PSCs with PHJ
#------------------------------------------------------------------------------

nbg_champion_pce = claim(
    "The best PHJ Pb-Sn PSC showed a PCE of 23.8% (stabilized 23.5%) with Voc of 0.873 V, "
    "short-circuit current density (Jsc) of 33.0 mA cm^-2, and FF of 82.6% under reverse scan.",
    title="NBG PSC with PHJ achieves 23.8% PCE",
)

nbg_average_improvement = claim(
    "PHJ devices had considerably higher average PCE of 22.8% compared to 21.0% for control devices, "
    "with average Voc of 0.869 V versus 0.824 V and average FF of 80.8% versus 78.5%.",
    title="Average performance improvement with PHJ",
)

#------------------------------------------------------------------------------
# Research questions
#------------------------------------------------------------------------------

mechanism_question = question(
    "How does the 3D/3D bilayer PHJ structure suppress non-radiative recombination "
    "while maintaining good charge transport properties?",
    title="Mechanism of PHJ function",
)

tandem_question = question(
    "Can the 3D/3D bilayer PHJ enable record efficiency in all-perovskite tandem solar cells?",
    title="Tandem efficiency potential with PHJ",
)

__all__ = [
    "tandem_configuration",
    "performance_potential",
    "previous_limitation",
    "two_d_three_d_problem",
    "surface_passivation_tradeoff",
    "phj_solution",
    "type_two_band_alignment",
    "bilateral_improvement",
    "hybrid_deposition_method",
    "ion_immiscibility",
    "nbg_champion_pce",
    "nbg_average_improvement",
    "mechanism_question",
    "tandem_question",
]