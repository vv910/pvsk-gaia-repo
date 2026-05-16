"""
motivation.py - Introduction and motivation for perovskite solar cell research

This module covers the background problem (fundamental losses in low-cost photovoltaics)
and the research question addressed by the paper.
"""
from gaia.lang import claim, setting

# Fundamental loss mechanisms in low-cost photovoltaic technologies
energy_loss_excitons = claim(
    "Separating tightly bound excitons and extracting free charges from highly "
    "disordered low-mobility networks represents fundamental energy losses for "
    "many low-cost photovoltaic technologies [@Lee2012].",
    title="Energy losses from exciton separation and charge extraction"
)

# Dye-sensitized solar cell losses
dssc_losses = claim(
    "For dye-sensitized solar cells, losses arise both from electron transfer from "
    "the absorber into the TiO2 requiring 'driving force' and from dye regeneration "
    "from the electrolyte requiring overpotential [@Lee2012].",
    title="DSSC loss mechanisms"
)

# Organic solar cell losses
organic_losses = claim(
    "For organic solar cells, losses are predominantly caused by low dielectric constants "
    "leading to tightly bound excitons that require a heterojunction with an electron "
    "acceptor with large energy offset for ionization and charge separation [@Lee2012].",
    title="Organic solar cell losses from low dielectric constant"
)

# sensitized solar cell Voc limitation
sensitized_voc_limitation = claim(
    "Inorganic semiconductor-sensitized solar cells (ETA approach) suffer from rather "
    "low open-circuit voltage (Voc), possibly due to electronically disordered, "
    "low-mobility n-type TiO2 [@Lee2012].",
    title="Sensitized solar cell Voc limitation"
)

# Perovskite as absorber
perovskite_properties = claim(
    "Organometal halide perovskites provide a framework for binding organic and "
    "inorganic components into a molecular composite with tunable crystal cell size, "
    "high crystallinity, and intense visible to near-infrared absorptivity [@Lee2012].",
    title="Perovskite material properties"
)

# Prior perovskite work
prior_perovskite_work = claim(
    "Organometal halide perovskites have been used as sensitizers in liquid electrolyte "
    "photoelectrochemical cells with conversion efficiencies from 3.5 to 6.5%, and CsSnI3 "
    "perovskite functioned as hole conductor in solid-state DSSCs delivering up to 8.5% "
    "power conversion efficiency [@Lee2012].",
    title="Prior perovskite solar cell performance"
)

# Research question / gap
research_gap = claim(
    "A solution-processable solar cell that overcomes the fundamental losses of organic "
    "absorbers and disordered metal oxides was needed, combining the benefits of "
    "perovskite absorbers with a mesostructured scaffold approach [@Lee2012].",
    title="Research gap: overcoming fundamental losses"
)

# Key insight - Al2O3 scaffold
key_insight = claim(
    "Replacement of mesoporous n-type TiO2 with insulating Al2O3 (wide band gap 7-9 eV) "
    "as an inert scaffold improved power conversion efficiency, indicating electron "
    "transport through the perovskite layer was faster than through TiO2 [@Lee2012].",
    title="Key insight: Al2O3 scaffold improves efficiency"
)

__all__ = [
    "energy_loss_excitons",
    "dssc_losses",
    "organic_losses",
    "sensitized_voc_limitation",
    "perovskite_properties",
    "prior_perovskite_work",
    "research_gap",
    "key_insight",
]