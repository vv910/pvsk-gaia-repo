"""
Gaia knowledge package for Lee2012 - Efficient Hybrid Solar Cells Based on
Meso-Superstructured Organometal Halide Perovskites

This package formalizes the knowledge from the 2012 Science paper demonstrating
10.9% power conversion efficiency in perovskite solar cells using a meso-superstructured
design with insulating Al2O3 scaffold.
"""
from gaia.lang import claim, setting, support, infer

# Import all modules
from . import motivation
from . import s2_methods
from . import s3_results
from . import s4_discussion
from . import strategies

# Re-export public symbols from each module
from .motivation import (
    energy_loss_excitons,
    dssc_losses,
    organic_losses,
    sensitized_voc_limitation,
    perovskite_properties,
    prior_perovskite_work,
    research_gap,
    key_insight,
)

from .s2_methods import (
    perovskite_composition,
    crystal_structure,
    film_crystallinity,
    film_stability,
    device_architecture,
    n_type_scaffold,
    insulator_scaffold,
    hole_conductor,
    fabrication_process,
    pore_filling,
    perovskite_conductivity,
    spiro_conductivity,
    ipce_method,
    jv_method,
    pia_method,
    transient_photocurrent_method,
    sem_edx_method,
)

from .s3_results import (
    al2o3_best_device,
    tio2_device,
    al2o3_high_voc_device,
    planar_junction,
    voc_improvement,
    ipce_spectral_range,
    optical_bandgap,
    voltage_deficit,
    absorbance_capability,
    photostability,
    tio2_sensitization,
    al2o3_insulating,
    hole_transfer_effective,
    hole_conductor_required,
    charge_collection_speed,
    perovskite_semicondo,
    chemical_capacitance,
    tio2_chemical_capacitance,
    compact_tio2,
    mssc_definition,
)

from .s4_discussion import (
    electron_transport_mssc,
    hole_transfer_mssc,
    al2o3_not_ntype,
    perovskite_transport_speed,
    junction_type,
    planar_junction_interp,
    series_resistance_tradeoff,
    main_achievement,
    fundamental_loss_reduction,
    future_absorption,
    future_photon_management,
    future_fill_factor,
    future_multijunction,
    remote_sensing_principle,
    classical_analog,
)

# Re-export strategies
from .strategies import (
    strat_loss_motivation,
    strat_perovskite_solution,
    strat_al2o3_outperforms,
    strat_capacitance_explanation,
    strat_low_losses,
    strat_hole_transfer_enables,
    strat_fast_transport,
    strat_electron_location,
    strat_stability_enables,
    strat_photostability,
    strat_main_achievement,
    strat_resistance_tradeoff,
    strat_future_improvements,
    strat_structure_confirms,
    strat_ipce_broad,
)

__all__ = [
    # motivation
    "energy_loss_excitons",
    "dssc_losses",
    "organic_losses",
    "sensitized_voc_limitation",
    "perovskite_properties",
    "prior_perovskite_work",
    "research_gap",
    "key_insight",
    # methods
    "perovskite_composition",
    "crystal_structure",
    "film_crystallinity",
    "film_stability",
    "device_architecture",
    "n_type_scaffold",
    "insulator_scaffold",
    "hole_conductor",
    "fabrication_process",
    "pore_filling",
    "perovskite_conductivity",
    "spiro_conductivity",
    "ipce_method",
    "jv_method",
    "pia_method",
    "transient_photocurrent_method",
    "sem_edx_method",
    # results
    "al2o3_best_device",
    "tio2_device",
    "al2o3_high_voc_device",
    "planar_junction",
    "voc_improvement",
    "ipce_spectral_range",
    "optical_bandgap",
    "voltage_deficit",
    "absorbance_capability",
    "photostability",
    "tio2_sensitization",
    "al2o3_insulating",
    "hole_transfer_effective",
    "hole_conductor_required",
    "charge_collection_speed",
    "perovskite_semicondo",
    "chemical_capacitance",
    "tio2_chemical_capacitance",
    "compact_tio2",
    "mssc_definition",
    # discussion
    "electron_transport_mssc",
    "hole_transfer_mssc",
    "al2o3_not_ntype",
    "perovskite_transport_speed",
    "junction_type",
    "planar_junction_interp",
    "series_resistance_tradeoff",
    "main_achievement",
    "fundamental_loss_reduction",
    "future_absorption",
    "future_photon_management",
    "future_fill_factor",
    "future_multijunction",
    "remote_sensing_principle",
    "classical_analog",
    # strategies
    "strat_loss_motivation",
    "strat_perovskite_solution",
    "strat_al2o3_outperforms",
    "strat_capacitance_explanation",
    "strat_low_losses",
    "strat_hole_transfer_enables",
    "strat_fast_transport",
    "strat_electron_location",
    "strat_stability_enables",
    "strat_photostability",
    "strat_main_achievement",
    "strat_resistance_tradeoff",
    "strat_future_improvements",
    "strat_structure_confirms",
    "strat_ipce_broad",
]