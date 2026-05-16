"""
Results: Photovoltaic Performance, Stability Data, and Lifetime Analysis

This module contains experimental results including PV characterization, stability curves,
acceleration factors, and lifetime predictions.
"""
from gaia.lang import claim

# PV characterization results
table_s1_pv_characteristics = claim(
    "Photovoltaic characteristics of capped and uncapped PSCs are summarized, showing improved "
    "fill factor and open-circuit voltage in capped devices.",
    title="Table S1: PV characteristics summary"
)

# GIWAXS angle-dependent intensity
giwaxs_angle_dependence = claim(
    "At incident angle θ = 0.15° (more surface-sensitive), the 2D Cs2PbI2Cl2 reflections are "
    "stronger relative to the CsPbI3 (110) reflection compared to θ = 0.30° (less surface-sensitive), "
    "confirming surface preferential formation of the 2D layer.",
    title="GIWAXS angle dependence confirms surface 2D formation"
)

# TRPL observations
trpl_observation = claim(
    "The TRPL lifetime increased from 14 ns (uncapped) to >62 ns (capped) when the capping "
    "layer was present, consistent with the observed VOC increase in capped PSCs.",
    title="TRPL lifetime increases from 14 ns to >62 ns with capping"
)

# Degradation rate analysis
degradation_rate_follows_arrhenius = claim(
    "Degradation rates could be adequately described by a single Arrhenius function across "
    "the entire temperature range, suggesting that the same degradation mechanism dominated "
    "at all temperatures studied.",
    title="Single Arrhenius function describes degradation across temperature range"
)

activation_energy_comparable_fast_slow = claim(
    "The activation energies associated with the fast and slow degradation (Ea_fast and "
    "Ea_slow) of each type of PSC were comparable, suggesting that the two degradation "
    "rates probed a single physical process.",
    title="Ea_fast and Ea_slow are comparable, indicating single mechanism"
)

activation_energy_capped_higher = claim(
    "The activation energies (Ea) that describe the degradation for capped PSCs are nearly "
    "twice those for uncapped PSCs, suggesting that the 2D Cs2PbI2Cl2 layer stabilizes "
    "devices against thermal degradation.",
    title="Capped PSCs have nearly 2x higher activation energy for degradation"
)

ion_migration_speculated = claim(
    "Ion migration is speculated to be the dominant degradation mechanism based on the "
    "Arrhenius analysis and structural characterization of aged devices.",
    title="Ion migration is the speculated dominant degradation mechanism"
)

# Acceleration factors
af_values_extracted = claim(
    "Acceleration factors were extracted for each accelerated temperature (59°C, 85°C, and "
    "110°C) using the activation energy from k_slow and the AF equation.",
    title="AF values extracted for 59°C, 85°C, and 110°C"
)

af_110c_value = claim(
    "The acceleration factor for capped solar cells at 110°C is 24.2 ± 3.5, allowing "
    "conversion of aging time at 110°C to equivalent time at 35°C.",
    title="AF at 110°C is 24.2 ± 3.5 for capped devices"
)

# Universal curve confirmation
universal_curve_both_types = claim(
    "When aging time is multiplied by the acceleration factor, all data for both capped "
    "and uncapped solar cells collapse onto a universal curve, confirming that the same "
    "mechanism (hastened at elevated temperatures) causes degradation across the temperature range.",
    title="Data collapse to universal curve confirms single mechanism"
)

# T80 lifetime results
t80_110c_capped = claim(
    "The average experimentally measured T80 for capped solar cells operating continuously "
    "at 110°C is >2100 hours.",
    title="T80 at 110°C exceeds 2100 hours for capped devices"
)

t80_extrapolated_35c = claim(
    "Based on the T80 at 110°C (>2100 hours) and AF at 110°C (24.2 ± 3.5), the extrapolated "
    "T80 at 35°C is 5.1 ± 0.7 × 10^4 hours (approximately 5 years of continuous operation).",
    title="T80 at 35°C extrapolated to 51,000 ± 7000 hours"
)

# Ion migration characterization results
ea_ion_uncapped = claim(
    "The activation energy of ion migration (Ea_ion) for uncapped films is lower than "
    "for capped films, indicating easier ion migration in uncapped devices.",
    title="Uncapped films have lower Ea_ion"
)

ea_ion_capped_twice_uncapped = claim(
    "The Ea_ion of the capped film is nearly twice that of the uncapped film, indicating "
    "that the 2D cap frustrates ion migration.",
    title="Capped films have nearly 2x higher Ea_ion"
)

# Mechanism of stabilization
passivation_frustrates_ion_migration = claim(
    "Suppressed ion migration in capped devices likely stems from passivation of iodine "
    "vacancies at the surface of the perovskite active layer by the 2D capping layer.",
    title="2D capping layer passivates iodine vacancies, frustrates ion migration"
)

# Key numerical results summary
key_results_summary = claim(
    "Key results: (1) PCE improves from 14.9% (uncapped) to 17.4% (capped); "
    "(2) Capped devices show no degradation at 35°C for >3500 hours; "
    "(3) Capped devices have T80 >2100 hours at 110°C; "
    "(4) Extrapolated T80 at 35°C is 51,000 ± 7000 hours; "
    "(5) Ea for degradation is ~2x higher for capped than uncapped; "
    "(6) Ea_ion is ~2x higher for capped than uncapped.",
    title="Summary of key quantitative results"
)