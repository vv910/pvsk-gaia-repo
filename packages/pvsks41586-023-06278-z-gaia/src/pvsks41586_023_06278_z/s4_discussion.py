"""
Discussion and Conclusions.

This module contains the discussion and interpretation of results,
including the mechanism of PHJ function, limitations, and future directions.
"""

from gaia.lang import (
    claim,
    setting,
)

#------------------------------------------------------------------------------
# Mechanism of PHJ Function
#------------------------------------------------------------------------------

type_ii_mechanism = claim(
    "The type II band alignment at the 3D/3D PHJ substantially reduces hole concentration "
    "in the defective interface layer (DIL, which has much higher trap density than bulk) "
    "and facilitates electron extraction into the C60 layer owing to favorable band bending, "
    "thereby suppressing non-radiative recombination at the DIL without affecting carrier transport.",
    title="Type II band alignment reduces recombination in DIL",
)

depletion_region = claim(
    "The heterojunction induces a wider depletion region, which improves charge-collection "
    "efficiency and suppresses surface recombination by reducing hole concentration "
    "near the film surface.",
    title="PHJ widens depletion region",
)

charge_separation = claim(
    "The initial fast decay (7 ns) in PHJ films observed in TRPL measurements is attributed "
    "to charge-carrier separation at the type II heterojunction interface, enabling efficient "
    "charge extraction.",
    title="Fast TRPL decay indicates charge separation",
)

electron_extraction_acceleration = claim(
    "The type II band alignment drives electrons toward the ETL while repelling holes, "
    "accelerating electron drift into the C60 transport layer and reducing non-radiative "
    "recombination at the DIL.",
    title="Type II alignment accelerates electron extraction",
)

#------------------------------------------------------------------------------
# 2D/3D vs 3D/3D Comparison
#------------------------------------------------------------------------------

two_d_layer_limitation = claim(
    "The 2D layer in conventional 2D/3D heterojunctions may hinder charge transport and "
    "increase series resistance owing to asymmetric conductivity and potentially non-uniform distributions, "
    "limiting device FF despite good passivation.",
    title="2D layers limit charge transport",
)

three_d_advantage = claim(
    "The 3D/3D bilayer PHJ achieves both surface passivation (like 2D/3D) and high "
    "conductivity (unlike 2D), avoiding the trade-off between passivation and transport.",
    title="3D/3D PHJ achieves both passivation and transport",
)

#------------------------------------------------------------------------------
# Remaining Losses and Future Directions
#------------------------------------------------------------------------------

remaining_voc_ff_loss = claim(
    "Comparing tandem cell performance with the Shockley-Queisser limit shows notable "
    "electrical loss for Voc and FF, mainly due to non-radiative recombination and "
    "inefficient charge collection in perovskite bulk and perovskite-transport layer interface, "
    "plus additional Voc loss from the tunnel recombination junction.",
    title="Voc and FF losses remain below SQ limit",
)

optical_losses = claim(
    "Jsc in tandems can be further improved by reducing optical losses from reflection, "
    "parasitic absorption, and insufficient light absorption by the NBG perovskite absorber.",
    title="Optical losses limit Jsc",
)

future_improvement_path = claim(
    "A PCE higher than 30% is likely achievable with Voc of 2.2 V, Jsc of 17 mA cm^-2, "
    "and FF of 82%, through reducing bulk defect density, passivating contact interfaces, "
    "light management, and using more transparent front electrodes.",
    title="30% PCE is achievable with further improvements",
)

#------------------------------------------------------------------------------
# Stability Considerations
#------------------------------------------------------------------------------

long_term_stability = claim(
    "PHJ devices showed no obvious PCE degradation after 3,000 hours of aging in the dark "
    "in N2-filled glovebox, and no Sn2+ diffusion into the FL-WBG layer was observed after 60 days.",
    title="PHJ structure is stable over long periods",
)

thermal_stability_note = claim(
    "The thermal stability of all-perovskite tandem solar cells can be further improved by "
    "replacing back-metal electrodes with more robust materials, developing MA-free and "
    "PEDOT:PSS-free Pb-Sn perovskite subcells, and using thermally stable tunnel recombination junctions.",
    title="Thermal stability can be improved further",
)

bromide_migration = claim(
    "Br- easily diffuses into Pb-Sn perovskites even in fresh PHJ samples, but bromide "
    "migration has no notable effect on the absorption (bandgap) compared with control film.",
    title="Br- diffusion does not affect bandgap",
)

#------------------------------------------------------------------------------
# Key Conclusions
#------------------------------------------------------------------------------

record_efficiency = claim(
    "This work demonstrates a record-high certified PCE of 28.0% for all-perovskite "
    "tandem solar cells through the 3D/3D bilayer PHJ approach.",
    title="Record 28.0% certified PCE achieved",
)

bilateral_voc_ff = claim(
    "The 3D/3D bilayer PHJ simultaneously improves Voc and FF by suppressing interfacial "
    "non-radiative recombination while maintaining good charge transport.",
    title="PHJ simultaneously improves Voc and FF",
)

solution_processadvantage = claim(
    "The non-destructive hybrid evaporation-solution method enables construction of "
    "3D/3D bilayer PHJ without damaging the underlying Pb-Sn perovskite absorber, "
    "which was previously challenging with conventional solution-based deposition.",
    title="Hybrid method enables 3D/3D PHJ fabrication",
)

__all__ = [
    "type_ii_mechanism",
    "depletion_region",
    "charge_separation",
    "electron_extraction_acceleration",
    "two_d_layer_limitation",
    "three_d_advantage",
    "remaining_voc_ff_loss",
    "optical_losses",
    "future_improvement_path",
    "long_term_stability",
    "thermal_stability_note",
    "bromide_migration",
    "record_efficiency",
    "bilateral_voc_ff",
    "solution_processadvantage",
]