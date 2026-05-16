"""
Motivation module for pvsks41586-024-07997-7-gaia.

This module covers the introduction and motivation for the bilayer interface passivation
strategy in perovskite/silicon tandem solar cells.

Paper: Perovskite/silicon tandem solar cells with bilayer interface passivation
DOI: 10.1038/s41586-024-07997-7
"""

from gaia.lang import (
    claim,
    setting,
    question,
    support,
    infer,
)

# =============================================================================
# Background Settings
# =============================================================================

csi_solar_cell_dominance = setting(
    "Crystalline silicon (c-Si) solar cells dominate the photovoltaic market due to exceptional "
    "efficiency, abundant material supply, and long-term reliability. Commercial CZ silicon wafer "
    "cells have achieved certified PCE exceeding 27% (LONGi Green Energy Technology).",
    title="c-Si solar cell market dominance",
)

auger_recombination_limit = setting(
    "Further enhancements in silicon cell performance are mainly limited by Auger recombination "
    "and parasitic absorption.",
    title="Silicon cell efficiency limits",
)

tandem_strategy = setting(
    "Integrating a wide-bandgap metal halide perovskite atop silicon heterojunction (SHJ) bottom "
    "cells in a tandem configuration minimizes carrier thermalization losses and has demonstrated "
    "independently certified PCEs exceeding 31%.",
    title="Perovskite/silicon tandem strategy",
)

pin_interface_recombination = setting(
    "State-of-the-art high-efficiency tandem solar cells predominantly adopt an inverted p-i-n "
    "configuration. However, p-i-n-type perovskite devices suffer from strong interface "
    "recombination at the perovskite/C60 interface for electron extraction, leading to an "
    "undesirably large open-circuit voltage (Voc) deficit.",
    title="p-i-n interface recombination challenge",
)

passivation_tradeoff = claim(
    "A fundamental challenge in implementing passivation layers in p-i-n devices is achieving "
    "the best balance between minimizing recombination loss and restricting contact resistance, "
    "thereby ensuring efficient electron transport and hole blocking simultaneously.",
    title="Passivation-transport tradeoff",
)

# =============================================================================
# Research Question
# =============================================================================

research_question = question(
    "How can interfacial recombination at the wide-bandgap perovskite/electron transport layer "
    "interface be suppressed without compromising superior charge transport performance in "
    "perovskite/silicon tandem cells?",
    title="Research question",
)

# =============================================================================
# Key Claims - Bilayer Passivation Strategy
# =============================================================================

bilateral_passivation_strategy = claim(
    "A bilayer interface passivation strategy was developed that involves the incorporation of "
    "a thin lithium fluoride (LiF) layer followed by the deposition of a short-chain "
    "ethylenediammonium diiodide (EDAI) molecule. LiF acts as a contact displacer and induces "
    "field passivation, while EDAI chemically passivates unpassivated areas that are not contacted "
    "by the LiF layer, forming nanoscale localized contacts at the perovskite/C60 interface.",
    title="Bilayer interface passivation strategy",
    metadata={"figure": "artifacts/images/.../fig1.png"},
)

lif_limited_effectiveness = claim(
    "A thin LiF interlayer with typical thickness of approximately 1 nm cannot provide sufficient "
    "passivation efficacy due to its discrete nature, still showing a large voltage deficit. "
    "A thicker LiF layer may improve passivation but introduces considerable undesirable resistive loss.",
    title="LiF limited effectiveness alone",
)

edai_chemical_passivation = claim(
    "The EDAI molecule can chemically passivate unpassivated areas not contacted by the LiF layer, "
    "forming nanoscale localized contacts at the perovskite/C60 interface. This provides an optimal "
    "trade-off between passivation and charge extraction.",
    title="EDAI chemical passivation mechanism",
)

nanoscale_contact_requirement = claim(
    "Local contact and selective emitter doping are widely used in mainstream silicon cell "
    "technologies. Implementing them in perovskite cells poses a substantial challenge due to the "
    "considerably shorter charge diffusion lengths of perovskite absorbers compared with silicon, "
    "necessitating local contact spacing at the submicrometre or nanoscale level.",
    title="Nanoscale contact requirement",
)

double_textured_silicon = claim(
    "The tandem devices were constructed on a double-textured Czochralski-based silicon "
    "heterojunction cell featuring a mildly textured front surface (for solution-processed perovskite) "
    "and a heavily textured rear surface (for uncompromised rear passivation and improved spectral response).",
    title="Double-textured silicon substrate design",
)

champion_device_performance = claim(
    "The resulting perovskite/silicon tandem achieved an independently certified stabilized power "
    "conversion efficiency of 33.89%, accompanied by a fill factor of 83.0% and an open-circuit "
    "voltage of nearly 1.97 V. This represents the first reported certified efficiency of a "
    "two-junction tandem solar cell exceeding the single-junction Shockley-Queisser limit of 33.7%.",
    title="Champion device certified performance",
)

# =============================================================================
# Strategy Reasoning
# =============================================================================

strat_bilayer_strategy = support(
    [lif_limited_effectiveness, edai_chemical_passivation, passivation_tradeoff],
    bilateral_passivation_strategy,
    reason=(
        "LiF alone is insufficient due to discrete nature (@lif_limited_effectiveness). "
        "EDAI provides chemical passivation for areas not covered by LiF (@edai_chemical_passivation). "
        "Together they achieve optimal passivation-transport tradeoff (@passivation_tradeoff)."
    ),
    prior=0.5,
)

strat_nanoscale_requirement = support(
    [nanoscale_contact_requirement],
    bilateral_passivation_strategy,
    reason=(
        "The nanoscale contact spacing requirement (@nanoscale_contact_requirement) explains why the "
        "bilayer strategy uses discretely distributed LiF (~1nm) that allows EDAI to form local contacts, "
        "achieving the submicrometre-level contact spacing needed for perovskite cells."
    ),
    prior=0.5,
)

strat_double_texture = support(
    [double_textured_silicon],
    bilateral_passivation_strategy,
    reason=(
        "The double-textured silicon substrate (@double_textured_silicon) enables the bilayer passivation "
        "strategy to be implemented effectively by providing a mildly textured front for perovskite "
        "deposition and a heavily textured rear for optical performance."
    ),
    prior=0.5,
)