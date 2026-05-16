"""
Introduction and Motivation.

This module covers the background on inverted perovskite solar cells (PSCs),
the interface recombination problem at the perovskite/C60 interface, and the
motivation for bimolecular passivation approach.
"""

from gaia.lang import claim, setting, support

# Background context - regular n-i-p PSCs achieve PCEs > 25%
regular_pscs_pce = claim(
    "Regular (n-i-p) perovskite solar cells (PSCs) have achieved certified power conversion efficiencies (PCEs) greater than 25% [@Liu2024].",
    title="Regular n-i-p PSCs achieve PCE > 25%",
)

# Inverted p-i-n PSCs have potential advantages but lower PCEs
inverted_psc_advantages = claim(
    "Inverted (p-i-n) PSCs offer potential advantages including increased operating stability, low-temperature processing, and compatibility with integration into tandem solar cells [@Liu2024].",
    title="Inverted p-i-n PSC advantages",
)

# Inverted PCE rarely surpass 24% under QSS protocol
inverted_psc_pce_gap = claim(
    "Reported PCEs for inverted (p-i-n) PSCs rarely surpass 24% under the stringent quasi-steady-state (QSS) protocol, whereas regular n-i-p PSCs exceed 25% [@Liu2024].",
    title="Inverted PSC PCE gap below 24% QSS",
)

# The efficiency gap is primarily attributed to interface recombination
interface_recombination = claim(
    "The efficiency gap in inverted PSCs is primarily attributed to higher recombination rates at the interface between the perovskite and the electron transport layer (ETL), typically made from C60 and its derivatives [@Liu2024].",
    title="Interface recombination at perovskite/C60",
)

# Two types of recombination losses exist
near_interface_minority_carriers = claim(
    "Near-interface minority carriers (holes in the perovskite layer) lead to direct interface recombination with majority carriers (electrons in the ETL), even at nondefect sites [@Liu2024].",
    title="Near-interface minority carrier recombination",
)

# Defects at perovskite surface cause trapping and recombination
surface_defect_recombination = claim(
    "Defects at the perovskite surface, particularly halide vacancies which have low formation energy, induce surface recombination through trapping of carriers [@Liu2024].",
    title="Surface defect-induced recombination",
)

# Prior work on surface passivation
surface_passivation_suppresses = claim(
    "Surface passivation using organohalides, Lewis bases, and dipolar compounds can suppress interface charge recombination [@Liu2024].",
    title="Surface passivation suppresses recombination",
)

# Single molecule approach is insufficient
single_molecule_insufficient = claim(
    "Reliance on a single species of molecule may fail to address simultaneously both surface and interface recombination processes [@Liu2024].",
    title="Single molecule passivation insufficient",
)

# The dual-passivation strategy concept
dual_passivation_concept = claim(
    "A combination of different molecules with distinct functionalities can address complex interface carrier recombination: one class repels hole carriers through field-effect passivation, while the second class interacts with defect sites to form chemical bonds through chemical passivation [@Liu2024].",
    title="Bimolecular dual-passivation strategy concept",
)

# Diammonium ligands provide field-effect passivation
diammonium_field_effect = claim(
    "Diammonium ligands, in which one -NH3+ group anchors to the perovskite surface and the other extends away, induce a surface dipole and n-type doping that provides effective field-effect passivation by repelling minority carriers at the interface [@Liu2024].",
    title="Diammonium ligands provide field-effect passivation",
)

# Methylthio molecules provide chemical passivation
methylthio_chemical_passivation = claim(
    "Sulfur-modified methylthio molecules (2MTEAI, 3MTPAI) passivate surface defects and suppress recombination through strong coordination and hydrogen bonding [@Liu2024].",
    title="Methylthio molecules provide chemical passivation",
)

__all__ = [
    "regular_pscs_pce",
    "inverted_psc_advantages",
    "inverted_psc_pce_gap",
    "interface_recombination",
    "near_interface_minority_carriers",
    "surface_defect_recombination",
    "surface_passivation_suppresses",
    "single_molecule_insufficient",
    "dual_passivation_concept",
    "diammonium_field_effect",
    "methylthio_chemical_passivation",
]