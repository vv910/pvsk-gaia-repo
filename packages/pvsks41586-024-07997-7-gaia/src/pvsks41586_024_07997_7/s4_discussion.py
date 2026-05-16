"""
Discussion module for pvsks41586-024-07997-7-gaia.

This module covers the discussion of results and synthesis of conclusions.

Paper: Perovskite/silicon tandem solar cells with bilayer interface passivation
DOI: 10.1038/s41586-024-07997-7
"""

from gaia.lang import (
    claim,
    setting,
    support,
    infer,
)

from .s3_results import (
    lif_discontinuity_confirmation,
    xps_pb4f_shift,
    metallic_pb_suppression,
    pa_vs_eda_orientation,
    tof_sims_edai_distribution,
    eqe_spectral_response,
    minority_carrier_lifetime,
    voc_statistical_improvement,
    champion_device_jv,
    nrel_certified_pce,
    storage_stability,
    operational_stability,
)

from .motivation import nanoscale_contact_requirement

# =============================================================================
# Key Synthesis Claims
# =============================================================================

bilayer_mechanism_synthesis = claim(
    "The LiF/EDAI bilayer interface passivation strategy works through two complementary mechanisms: "
    "(1) discontinuous LiF layer (~1nm) provides field passivation and contact displacement while "
    "enabling electron tunneling through nanoscale openings, and (2) EDAI molecule provides chemical "
    "passivation at perovskite surface through coordinate binding to Pb defects, forming bridge-like "
    "structure with two amine groups that maximize out-of-plane charge transport. The LiF openings "
    "with spacing of only a few nanometers allow EDAI to form local contacts, which is smaller than "
    "the charge diffusion length of perovskite absorber.",
    title="Bilayer passivation dual mechanism synthesis",
)

nanoscale_contact_design = claim(
    "The design successfully achieves submicrometre/nanoscale local contacts required for perovskite "
    "cells without cumbersome laser- or chemical-etching steps. This is essential because perovskite "
    "charge diffusion lengths are considerably shorter than silicon, necessitating nanoscale contact "
    "spacing for effective charge extraction.",
    title="Nanoscale contact design enables effective perovskite integration",
)

asymmetric_texture_benefits = claim(
    "The asymmetric texture design (mildly textured front for perovskite solution deposition, heavily "
    "textured rear for optical response) simultaneously enhanced photocurrent through improved "
    "infrared photon collection and maintained rear passivation. This解决了 the conflict between "
    "perovskite deposition requirements and silicon bottom cell optical performance.",
    title="Asymmetric texture resolves perovskite-silicon integration challenge",
)

first_to_exceed_sq_limit = claim(
    "The certified stabilized PCE of 33.89% represents the first reported certified efficiency of "
    "a two-junction tandem solar cell exceeding the single-junction Shockley-Queisser limit of 33.7%, "
    "marking a significant milestone in photovoltaic efficiency.",
    title="First certified tandem exceeding Shockley-Queisser limit",
)

stability_implications = claim(
    "The improved operational stability (80% retention after 1,200 hours) with bilayer passivation "
    "compared to LiF-only control (less than 60% retention) demonstrates that the interface "
    "modification strategy not only improves efficiency but also enhances long-term device durability. "
    "This highlights the importance of interface structure in perovskite/silicon tandem stability.",
    title="Bilayer passivation enhances operational stability",
)

# =============================================================================
# Strategy Reasoning for Conclusions
# =============================================================================

strat_bilayer_mechanism = support(
    [lif_discontinuity_confirmation, xps_pb4f_shift, metallic_pb_suppression, pa_vs_eda_orientation],
    bilayer_mechanism_synthesis,
    reason=(
        "TEM confirms LiF discontinuity (@lif_discontinuity_confirmation). "
        "XPS shows EDAI chemical interaction with Pb (@xps_pb4f_shift, @metallic_pb_suppression). "
        "DFT shows EDA2+ horizontal bridge-like binding (@pa_vs_eda_orientation). "
        "Together these evidence points explain the dual passivation-transport mechanism."
    ),
    prior=0.5,
)

strat_nanoscale = support(
    [nanoscale_contact_requirement, tof_sims_edai_distribution],
    nanoscale_contact_design,
    reason=(
        "The nanoscale contact requirement (@nanoscale_contact_requirement) explains why discrete LiF "
        "spacing must be smaller than perovskite diffusion length. TOF-SIMS confirms EDAI localizes "
        "at perovskite surface (@tof_sims_edai_distribution) forming nanoscale contacts without "
        "penetrating bulk."
    ),
    prior=0.5,
)

strat_texture = support(
    [eqe_spectral_response, minority_carrier_lifetime, voc_statistical_improvement],
    asymmetric_texture_benefits,
    reason=(
        "EQE shows improved infrared response from large pyramid rear texture (@eqe_spectral_response). "
        "Minority carrier lifetime confirms rear passivation maintained with texture D (@minority_carrier_lifetime). "
        "Voc statistics show improvement with asymmetric texture (@voc_statistical_improvement)."
    ),
    prior=0.5,
)

strat_certified = support(
    [champion_device_jv, nrel_certified_pce, storage_stability, operational_stability],
    first_to_exceed_sq_limit,
    reason=(
        "Champion device shows 33.96%/34.08% forward/reverse PCE (@champion_device_jv). "
        "NREL certified 33.89% stabilized PCE (@nrel_certified_pce), first to exceed 33.7% SQ limit. "
        "Storage and operational stability demonstrate practical viability (@storage_stability, @operational_stability)."
    ),
    prior=0.5,
)

strat_stability = support(
    [operational_stability, storage_stability],
    stability_implications,
    reason=(
        "Operational stability shows 80% retention after 1200h vs <60% for control (@operational_stability). "
        "Air storage stability shows 90% retention after 53 days vs 82% for control (@storage_stability). "
        "These demonstrate interface structure critically affects device durability."
    ),
    prior=0.5,
)

# =============================================================================
# Export Conclusions
# =============================================================================

__all__ = [
    "csi_solar_cell_dominance",
    "auger_recombination_limit",
    "tandem_strategy",
    "pin_interface_recombination",
    "passivation_tradeoff",
    "research_question",
    "bilateral_passivation_strategy",
    "lif_limited_effectiveness",
    "edai_chemical_passivation",
    "nanoscale_contact_requirement",
    "double_textured_silicon",
    "champion_device_performance",
    "strat_bilayer_strategy",
    "strat_nanoscale_requirement",
    "strat_double_texture",
]