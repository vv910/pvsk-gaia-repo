"""
Burschka2013: Discussion section.

This module captures the key findings, interpretation, and conclusions from the paper.
"""

from gaia.lang import claim, setting

# === Key Findings ===

conversion_facilitation = claim(
    "The confinement of PbI2 within the nanoporous TiO2 network greatly facilitates its "
    "conversion to the perovskite pigment, compared to flat substrate deposition "
    "[@Burschka2013].",
    title="Nanoporous confinement facilitates perovskite conversion",
)

nanomorphology_enforcement = claim(
    "The mesoporous scaffold forces the perovskite to adopt a confined nanomorphology "
    "[@Burschka2013].",
    title="Mesoporous scaffold enforces perovskite nanomorphology",
)

# === Mechanistic Interpretation ===

layered_pbi2_structure = claim(
    "The insertion of the organic cation is facilitated through the layered PbI2 structure, "
    "which consists of three spatially repeating planes: I-Pb-I. Strong intralayer chemical "
    "bonding combined with weak interlayer van der Waals interactions allows easy insertion "
    "of guest molecules between the layers [@Burschka2013].",
    title="Layered PbI2 structure enables cation insertion",
)

thermodynamic_driving_force = claim(
    "The thermodynamic driving force for the two-step conversion is the difference in bulk "
    "lattice energy between PbI2 and CH3NH3PbI3, with the initial crystal lattice serving as "
    "a template for the formation of the desired compound. This is analogous to ion exchange "
    "reactions used to convert II-V semiconductor nanocrystals to III-V analogues while "
    "preserving particle size and distribution [@Burschka2013].",
    title="Lattice energy difference drives conversion",
)

reaction_kinetics_enhancement = claim(
    "The large energy of formation of the hybrid perovskite combined with the nanoscopic "
    "morphology of the PbI2 precursor (approximately 22 nm crystals) greatly enhances reaction "
    "kinetics, enabling complete transformation within seconds of contact with "
    "methylammonium iodide solution [@Burschka2013].",
    title="Nanoscopic morphology combined with high formation energy enhances kinetics",
)

# === Broader Implications ===

two_step_method_applicability = claim(
    "The two-step sequential deposition method is applicable to other preformed metal halide "
    "mesostructures that can be converted into the desired perovskite by insertion reactions "
    "[@Burschka2013].",
    title="Sequential deposition applicable to other metal halide mesostructures",
)

record_efficiency = claim(
    "The power conversion efficiency of 15% achieved with the best device is amongst the "
    "highest for solution-processed photovoltaics and sets a new record for organic or hybrid "
    "inorganic-organic solar cells at the time of publication [@Burschka2013].",
    title="15% PCE sets record for solution-processed photovoltaics",
)

reproducibility_demonstrated = claim(
    "The sequential deposition method provides a means to achieve excellent photovoltaic "
    "performance with high reproducibility, addressing the wide spread of performance "
    "characteristic of single-step deposition methods [@Burschka2013].",
    title="Method enables reproducible high performance",
)

future_potential = claim(
    "Perovskite-based photovoltaic devices fabricated using this method have potential for "
    "widespread application and may eventually rival conventional silicon-based photovoltaics "
    "[@Burschka2013].",
    title="Perovskite photovoltaics may rival silicon",
)

__all__ = [
    "conversion_facilitation",
    "nanomorphology_enforcement",
    "layered_pbi2_structure",
    "thermodynamic_driving_force",
    "reaction_kinetics_enhancement",
    "two_step_method_applicability",
    "record_efficiency",
    "reproducibility_demonstrated",
    "future_potential",
]