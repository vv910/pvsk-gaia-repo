"""
Hydrophobic additive in hole transport layer (Section 3 of Gu2023).

Covers: ALD SnO2 damage to perovskite, TPFB as protective additive in PTAA HTL,
mechanism of TPFB spreading and moisture resistance enhancement.
"""

from gaia.lang import claim, setting

# ALD SnO2 damages perovskite
ald_damage_to_perovskite = claim(
    "The atomic layer deposition (ALD) of SnO2 during bifacial perovskite minimodule "
    "fabrication imposes a challenge by damaging the perovskite films, frequently causing "
    "fraction of bifacial PSCs to exhibit much lower fill factor compared with monofacial "
    "counterparts using C60/bathocuproine (BCP) as ETL [@Gu2023].",
    title="ALD SnO2 damages perovskite, causing low FF",
)

# TPFB in HTL provides protection
tpfb_in_htl_protection = claim(
    "Mixing 5 wt% of tris(pentafluorophenyl)borane (TPFB) into the PTAA hole transport "
    "layer (HTL) protected the perovskite films from moisture damage during the ALD "
    "process and resulted in even better device reproducibility than adding TPFB as an "
    "additive in the perovskite film or modifying the perovskite surface [@Gu2023].",
    title="TPFB in HTL protects perovskite from moisture",
)

# TPFB spreads from HTL to perovskite
tpfb_spread_to_perovskite = claim(
    "TPFB added to the HTL spreads into the perovskite film, with approximately 35% of the "
    "TPFB added in the HTL (5 wt% in PTAA) spreading into the perovskite layer, equivalent "
    "to 0.067 mol% TPFB to Pb, as confirmed by X-ray photoelectron spectroscopy (XPS) "
    "measurement showing fluorine presence at the perovskite surface [@Gu2023].",
    title="35% of TPFB spreads from HTL to perovskite surface",
)

# Hydrophobic surface confirmation
hydrophobic_surface_confirmation = claim(
    "Surface contact-angle measurement confirmed that the modified perovskites with TPFB "
    "had a more hydrophobic surface compared with control samples, demonstrating enhanced "
    "moisture resistance [@Gu2023].",
    title="TPFB increases surface hydrophobicity",
)

# TPFB passivation effect (PL intensity and lifetime)
tpfb_passivation_effect = claim(
    "TPFB was found to passivate perovskite films, evidenced by stronger photoluminescence "
    "(PL) intensity and longer recombination lifetime from perovskite films covered by a "
    "layer of TPFB, as well as reduced trap density of states in TPFB-modified devices [@Gu2023].",
    title="TPFB passivates perovskite, increases PL and lifetime",
)

# TPFB reduces trap density
tpfb_reduced_trap_density = claim(
    "Perovskite solar cells with TPFB showed reduced trap density of states, further "
    "confirming the passivation effect of TPFB on reducing point defects in perovskite "
    "films [@Gu2023].",
    title="TPFB reduces trap density of states",
)

# TPFB Fermi level change in PTAA
tpfb_frei_level_ptaa = claim(
    "The addition of TPFB in PTAA pulled down the Fermi level of PTAA from -4.51 eV to "
    "-4.82 eV, enabling better energy alignment and conductivity of the p-doped HTL, which "
    "contributes to fill factor enhancement compared with devices with TPFB as an additive in "
    "perovskites [@Gu2023].",
    title="TPFB p-dopes PTAA, lowers Fermi level to -4.82 eV",
)

# FF improvement with TPFB in HTL
ff_improvement_tpfb = claim(
    "The bifacial module using TPFB:PTAA as the HTL has a larger fill factor of 0.76 and "
    "much higher efficiency, while the fill factor of the control (PTAA without TPFB) is "
    "only 0.68 measured from the front side for bifacial modules with aperture area of "
    "25.03 cm^2 [@Gu2023].",
    title="FF increases from 0.68 to 0.76 with TPFB in HTL",
)

# TPFB enhances stability
tpfb_enhanced_stability = claim(
    "Perovskite films deposited on TPFB:PTAA degraded slower than control samples under "
    "accelerated stability testing conditions, proving that TPFB enhances the light stability "
    "of perovskites, possibly through slightly modified grain-growth process resulting in "
    "smaller point-defect density [@Gu2023].",
    title="TPFB enhances perovskite stability under light",
)