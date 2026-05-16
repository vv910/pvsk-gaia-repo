"""
priors.py - Prior probability assignments for independent claims

Prior ranges:
- 0.85 to 0.95: well-established fact or strong experimental observation
- 0.65 to 0.85: supported by evidence but imperfect
- 0.40 to 0.65: tentative, single-source, method-dependent, or uncertain
- 0.20 to 0.40: speculative or weak assumption
"""
from .s2_methods import crystal_structure, perovskite_conductivity, spiro_conductivity, pore_filling, film_crystallinity, film_stability
from .s3_results import (
    al2o3_best_device,
    al2o3_insulating,
    charge_collection_speed,
    chemical_capacitance,
    hole_conductor_required,
    hole_transfer_effective,
    ipce_spectral_range,
    optical_bandgap,
    photostability,
    tio2_chemical_capacitance,
    tio2_device,
    tio2_sensitization,
    voltage_deficit,
)
from .s4_discussion import perovskite_transport_speed, series_resistance_tradeoff
from .motivation import (
    dssc_losses,
    energy_loss_excitons,
    organic_losses,
    prior_perovskite_work,
    sensitized_voc_limitation,
)

PRIOR_MOTIVATION = {
    energy_loss_excitons: (
        0.85,
        "Fundamental loss mechanism widely reported in low-cost photovoltaic literature. "
        "Tightly bound excitons and charge extraction losses are well-documented problems."
    ),
    dssc_losses: (
        0.85,
        "DSSC losses from driving force and overpotential are well-established in the literature "
        "and widely discussed in review articles."
    ),
    organic_losses: (
        0.85,
        "Low dielectric constant in organic solar cells leading to bound excitons is a "
        "fundamental material property, well-established in the literature."
    ),
    sensitized_voc_limitation: (
        0.75,
        "Low Voc in sensitized solar cells has been observed and discussed in the literature, "
        "though the exact mechanism attribution to TiO2 disorder is specific to this paper."
    ),
    prior_perovskite_work: (
        0.90,
        "Cited prior work on perovskite solar cells with specific efficiency values from "
        "published papers (3.5-6.5% and up to 8.5%)."
    ),
    series_resistance_tradeoff: (
        0.80,
        "Tradeoff between series and shunt resistance is a standard photovoltaic design "
        "consideration, well-understood in the field."
    ),
    spiro_conductivity: (
        0.85,
        "Spiro-OMeTAD conductivity is a material property that has been characterized "
        "in multiple prior studies."
    ),
}

PRIOR_METHODS = {
    film_crystallinity: (
        0.90,
        "X-ray diffraction measurements provide direct experimental evidence of film "
        "crystallinity with long-range order (>200 nm domains)."
    ),
    film_stability: (
        0.90,
        "Air stability of the mixed-halide perovskite is directly observed experimentally "
        "and contrasts with instability of pure iodide versions."
    ),
    pore_filling: (
        0.80,
        "Pore filling is verified by cross-sectional SEM/EDX analysis, a direct "
        "experimental observation."
    ),
}

PRIOR_RESULTS = {
    al2o3_best_device: (
        0.92,
        "Direct experimental measurement with specific device parameters under standard "
        "AM1.5 illumination conditions."
    ),
    tio2_device: (
        0.92,
        "Direct experimental measurement with specific device parameters under standard "
        "AM1.5 illumination conditions."
    ),
    al2o3_insulating: (
        0.90,
        "Direct PIA spectroscopic measurement showing no free electron signal in Al2O3, "
        "confirming insulating behavior."
    ),
    charge_collection_speed: (
        0.88,
        "Transient photocurrent decay measurements provide quantitative comparison with "
        ">10x difference clearly resolving the faster collection in Al2O3 devices."
    ),
    chemical_capacitance: (
        0.80,
        "Chemical capacitance is a well-established concept in semiconductor electrochemistry, "
        "applied to explain the observed Voc differences in this system."
    ),
    crystal_structure: (
        0.92,
        "X-ray diffraction is a direct structural measurement providing lattice parameters "
        "with high confidence."
    ),
    hole_conductor_required: (
        0.85,
        "PIA spectroscopy directly shows that hole conductor is needed for long-lived "
        "charge species, based on comparison with and without spiro-OMeTAD."
    ),
    hole_transfer_effective: (
        0.88,
        "PIA spectroscopy shows clear absorption features of oxidized spiro-OMeTAD "
        "indicating effective hole transfer in both TiO2 and Al2O3 systems."
    ),
    ipce_spectral_range: (
        0.90,
        "IPCE is a direct spectrally-resolved measurement of device external quantum efficiency."
    ),
    optical_bandgap: (
        0.90,
        "Optical band gap derived from IPCE onset at 800 nm is a direct measurement with "
        "clear experimental signature."
    ),
    perovskite_conductivity: (
        0.82,
        "Electrical conductivity measurement of perovskite material, though the value is "
        "order-of-magnitude (10^-3 S/cm)."
    ),
    perovskite_transport_speed: (
        0.80,
        "Transport speed claim is derived from charge collection measurements; the >10x "
        "factor is clearly established though the exact mechanism attribution is inferred."
    ),
    photostability: (
        0.90,
        "1000-hour stability test with direct absorbance measurements provides strong "
        "experimental evidence."
    ),
    tio2_chemical_capacitance: (
        0.78,
        "Explanation of Voc loss through sub-band gap states in TiO2 is a theoretical "
        "interpretation based on chemical capacitance theory, well-supported by literature "
        "but applied specifically here."
    ),
    tio2_sensitization: (
        0.88,
        "PIA spectroscopy directly shows near-IR features assigned to free electrons in "
        "titania, confirming effective sensitization."
    ),
    voltage_deficit: (
        0.92,
        "Voltage deficit calculation uses directly measured Voc (1.1V) and band gap (1.55 eV) "
        "from IPCE onset - straightforward arithmetic."
    ),
}

PRIOR_META = {
    "prior_motivation": PRIOR_MOTIVATION,
    "prior_methods": PRIOR_METHODS,
    "prior_results": PRIOR_RESULTS,
}

# Flatten all priors into single dict for gaia
PRIORS = {}
PRIORS.update(PRIOR_MOTIVATION)
PRIORS.update(PRIOR_METHODS)
PRIORS.update(PRIOR_RESULTS)