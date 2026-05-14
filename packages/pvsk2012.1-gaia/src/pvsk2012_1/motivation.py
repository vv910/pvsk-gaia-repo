from gaia.lang import (
    claim,
    setting,
    question,
    support,
    compare,
    deduction,
    abduction,
    induction,
    analogy,
    extrapolation,
    elimination,
    case_analysis,
    mathematical_induction,
    composite,
    infer,
    contradiction,
    equivalence,
    complement,
    disjunction,
)

__all__ = [
    # Core device performance
    "pce_9_7_percent",
    "jsc_17_6_ma_cm2",
    "voc_0_888_v",
    "ff_0_62",
    "ipce_over_50_percent",
    # Materials characterization
    "bandgap_1_5_ev",
    "evb_minus_5_43_ev",
    "ecb_minus_3_93_ev",
    "tiO2_bandgap_3_1_ev",
    # Stability
    "stability_improvement",
    # Device structure
    "device_structure",
    "charge_separation_mechanism",
    # Methods/background
    "solid_state_sensitized_solar_cells_background",
    "perovskite_nanocrystals_as_light_harvesters",
]


# ===== INTRODUCTION / MOTIVATION =====

solid_state_sensitized_solar_cells_background = setting(
    "Solid-state sensitized heterojunction photovoltaic cells use molecular dyes, quantum dots (QD), or extremely thin absorber (ETA) layers as light harvesting agents. The sensitizer is deposited at the interface between hole and electron conducting materials, often a large band gap oxide semiconductor of mesoscopic structure. Following light excitation, the light harvester injects negative and positive charge carriers into the respective electronic transport materials, which are subsequently collected as photocurrent at the cell contacts. The photo-voltage is given by the difference in quasi-Fermi level under illumination of the electron- and hole-conducting solids."
)

perovskite_nanocrystals_as_light_harvesters = claim(
    "CH3NH3PbI3 perovskite nanocrystals exhibit one order of magnitude higher absorption coefficient than the conventional N719 dye, offering advantages for solid-state sensitized solar cells where much thinner TiO2 layers can be employed compared to liquid junction devices. Previous liquid junction cells achieved impressive PCE values up to 6.54% but suffered rapid degradation due to perovskite dissolution in the electrolyte."
)

# ===== RESULTS =====

# Device performance - core claims (separate for abduction later)
pce_9_7_percent = claim(
    "The solid-state device based on CH3NH3PbI3 perovskite NPs deposited on a 0.6 micrometer thick mesoporous TiO2 film achieved a power conversion efficiency (PCE) of 9.7% under AM 1.5G solar illumination, representing the highest reported efficiency to date for such cells.",
    title="9.7% PCE achieved"
)

jsc_17_6_ma_cm2 = claim(
    "The short-circuit photocurrent density (JSC) was 17.6 mA/cm squared.",
    title="JSC = 17.6 mA/cm^2"
)

voc_0_888_v = claim(
    "The open-circuit voltage (VOC) was 0.888 V.",
    title="VOC = 0.888 V"
)

ff_0_62 = claim(
    "The fill factor (FF) was 0.62.",
    title="FF = 0.62"
)

ipce_over_50_percent = claim(
    "The incident photon-to-electron conversion efficiency (IPCE) reached a broad maximum at 450 nm and remained at a level over 50% up to 750 nm.",
    title="IPCE >50% from 450-750 nm"
)

# Materials characterization
bandgap_1_5_ev = claim(
    "The optical band gap (Eg) for CH3NH3PbI3 deposited on TiO2 film was determined to be 1.5 eV from the extrapolation of the linear part of the [F(R)hv]^2 plot, indicating that optical absorption in the perovskite sensitizer occurs via a direct transition.",
    title="Perovskite band gap = 1.5 eV (direct)"
)

tiO2_bandgap_3_1_ev = claim(
    "The optical band gap (Eg) of the bare TiO2 film was determined to be 3.1 eV based on the indirect transition.",
    title="TiO2 band gap = 3.1 eV (indirect)"
)

evb_minus_5_43_ev = claim(
    "The valence band energy (EVB) of CH3NH3PbI3 was estimated to be -5.43 eV below vacuum level based on UPS measurements, consistent with previous reports.",
    title="Valence band = -5.43 eV"
)

ecb_minus_3_93_ev = claim(
    "The conduction band energy (ECB) of CH3NH3PbI3 was determined to be -3.93 eV based on the observed optical band gap, which is slightly higher than the ECB for TiO2.",
    title="Conduction band = -3.93 eV"
)

# Stability
stability_improvement = claim(
    "The solid-state device demonstrated remarkably improved stability compared to liquid junction cells over 500 hours of testing. The initial PCE improved by about 14% after 200 hours and remained stable thereafter, with JSC showing only slight decrease and VOC remaining stable.",
    title="Excellent long-term stability demonstrated"
)

# Charge separation mechanism
charge_separation_mechanism = claim(
    "Femtosecond laser studies combined with photo-induced absorption measurements showed charge separation proceeds via hole injection from the excited CH3NH3PbI3 NPs into the spiro-MeOTAD followed by electron transfer to the mesoscopic TiO2 film.",
    title="Charge separation mechanism elucidated"
)

# Device structure
device_structure = claim(
    "The device employs CH3NH3PbI3 perovskite nanocrystals as light absorbers and spiro-MeOTAD as the hole-transporting layer, deposited on a submicron-thick mesoscopic TiO2 film whose pores were infiltrated with the hole-conductor.",
    title="Solid-state mesoscopic heterojunction structure"
)

# Absorption coefficient
absorption_coefficient = claim(
    "The perovskite nanoparticles have an absorption coefficient of 1.5 x 10^4 cm^-1 at 550 nm, enabling high photocurrent in submicron-thick films.",
    title="High absorption coefficient"
)