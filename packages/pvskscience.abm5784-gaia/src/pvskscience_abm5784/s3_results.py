"""
Results module for Azmi et al. 2022 paper on damp heat-stable PSCs.

This module covers the experimental results including structural characterization,
device performance, and stability data.
"""

from gaia.lang import claim

# -----------------------------------------------------------------------------
# Structural characterization results
# -----------------------------------------------------------------------------

giwaxs_n1_n2_peaks = claim(
    "GIWAXS data confirmed that 2D-TA films were dominated by n=1 layers with "
    "prominent peak at qz approximately 0.35 Angstrom^-1, while 2D-RT films "
    "exhibited diffraction peaks of both n=1 and n=2, with a more substantial "
    "n=2 peak at lower qz. The strong intensity in the z-direction indicated "
    "highly oriented lateral direction of the top 3D perovskite layers "
    "[@Azmi2022].",
    title="GIWAXS confirms n=1 and n=2 presence in 2D-RT",
    figure="artifacts/images/203433b22d308414b6c930c7cb2458507a47fddb5cfd04363cfa7d86d02e066e.jpg",
    caption="Fig. 1B: Integrated intensity of GIWAXS data along qz",
)

hr_stem_n1_n2_confirmation = claim(
    "Cross-sectional HR-STEM images showed n=1 and n=2 layers in 2D-RT samples "
    "but only n=1 in 2D-TA samples. Elemental mapping showed reduction in density "
    "of C, Pb, and I elements corresponding to n=1 and n=2 layers. Average "
    "interlayer distances were approximately 1.2 nm for n=1 and approximately "
    "1.5 nm for n=2 [@Azmi2022].",
    title="HR-STEM confirms n=2 existence in 2D-RT",
    figure="artifacts/images/07ab1fdbe0b6c1735ab5d7f26c09e6fb8c8b10fdc2b7c6e82cbbf23960374655.jpg",
    caption="Fig. 1D: Cross-sectional HR-STEM image of 2D-RT samples",
)

pl_n2_uniform_capping = claim(
    "PL imaging at approximately 570 nm wavelength corresponding to n=2 showed "
    "that the 2D perovskite (n=2) capping layer formed uniformly on top of 3D "
    "perovskite surfaces for 2D-RT samples. PL spectra confirmed n=1 dominance "
    "in 2D-TA samples and more pronounced n=2 emission in 2D-RT samples "
    "[@Azmi2022].",
    title="PL confirms uniform n=2 capping in 2D-RT",
)

# -----------------------------------------------------------------------------
# Energy level alignment results
# -----------------------------------------------------------------------------

ef_vbm_wider_gap_2d_rt = claim(
    "The energetic gap between Fermi level (EF) and valence band maximum (VBM) "
    "of the 2D-RT sample was wider than control, indicating enhanced n-type "
    "character of post-treated 3D perovskite films, attributed to successful "
    "2D perovskite passivation strategy [@Azmi2022].",
    title="2D-RT has wider EF-VBM gap (enhanced n-type character)",
)

cbm_closer_to_c60_2d_rt = claim(
    "The conduction band minimum (CBM) of 2D-RT films was closer to the CBM of "
    "C60 at the n-type contact, resulting in more efficient charge transfer at "
    "the 2D/3D perovskite interface and the C60 electron-selective layer. In "
    "contrast, CBM of 2D-TA films was much higher than CBM of C60 with less "
    "n-type character, resulting in less efficient charge transfer [@Azmi2022].",
    title="2D-RT has CBM closer to C60 enabling efficient charge transfer",
)

# -----------------------------------------------------------------------------
# Device performance results
# -----------------------------------------------------------------------------

champion_pce_24_3_percent = claim(
    "The 2D-RT devices achieved a maximum PCE of 24.3% and stabilized PCE of "
    "approximately 24%, with open-circuit voltage (VOC) of approximately 1.20 V "
    "and fill factor (FF) of approximately 82% [@Azmi2022].",
    title="Champion PCE of 24.3% achieved",
)

pce_gain_2_percent_absolute = claim(
    "These results represent an absolute approximately 2% PCE gain upon 2D-RT "
    "passivation compared to control devices, and compare favorably with PCEs "
    "reported for other inverted PSCs [@Azmi2022].",
    title="Absolute 2% PCE gain from 2D-RT passivation",
)

voc_1_20_v = claim(
    "The open-circuit voltage (VOC) of 2D-RT devices was approximately 1.20 V, "
    "which is high for the bandgap of 1.55 eV, representing approximately 96% "
    "of the thermodynamic limit of 1.262 V [@Azmi2022].",
    title="VOC of 1.20 V achieved",
)

ff_82_percent = claim(
    "The fill factor (FF) of 2D-RT devices was approximately 82%, indicating "
    "efficient charge extraction and low resistive losses. In contrast, 2D-TA "
    "passivated devices suffered from lower FF values (<79%), indicative of "
    "energy level mismatch at the electron-selective contact [@Azmi2022].",
    title="FF of 82% for 2D-RT devices",
)

energy_loss_0_34_ev = claim(
    "The device energy loss (Eloss = Eg - qVOC) was minimized to 0.34 eV with "
    "2D-RT passivation, representing approximately 96% of the thermodynamic "
    "limit of VOC (1.262 V) for Eg of 1.55 eV. This is comparable to GaAs "
    "solar cells achieving approximately 98% of thermodynamic limit "
    "[@Azmi2022].",
    title="Energy loss reduced to 0.34 eV",
)

ta_lower_ff = claim(
    "The 2D-TA passivated devices suffered from lower fill factor values less "
    "than 79%, which is indicative of an energy level mismatch at the "
    "electron-selective contact, as derived from UPS results. The CBM of "
    "2D-TA films was much higher than CBM of C60 with less n-type character "
    "[@Azmi2022].",
    title="2D-TA devices have lower FF due to energy level mismatch",
)

# -----------------------------------------------------------------------------
# Reproducibility
# -----------------------------------------------------------------------------

narrow_statistical_distribution = claim(
    "The narrow statistical distribution of PCE, VOC, FF, and JSC values of the "
    "devices confirmed the high reproducibility of the approach. Less than 0.5% "
    "deviation was observed for person-to-person variations among seven different "
    "researchers [@Azmi2022].",
    title="Narrow statistical distribution confirms reproducibility",
)

universality_across_compositions = claim(
    "The 2D-RT passivation approach was universal across various perovskite "
    "compositions (various bandgaps) and deposition techniques (one-step, two-step, "
    "and blade-coating), with systematic absolute PCE enhancement of 1.5 to 2.0% "
    "[@Azmi2022].",
    title="Universality across compositions and techniques demonstrated",
)

# -----------------------------------------------------------------------------
# Recombination characterization
# -----------------------------------------------------------------------------

longer_recombination_lifetime = claim(
    "2D-passivated devices exhibited longer charge recombination lifetime and "
    "lower ideality factor than control devices, confirming reduced trap-assisted "
    "recombination at 3D/C60 interfaces by 2D perovskite passivation "
    "[@Azmi2022].",
    title="Longer recombination lifetime in 2D-passivated devices",
)

# -----------------------------------------------------------------------------
# Stability results
# -----------------------------------------------------------------------------

t95_after_1200_hours = claim(
    "The 2D-RT-based device retained more than 95% of initial PCE (T95) after "
    "more than 1200 hours for champion stability cells under damp-heat test "
    "conditions. After the damp-heat test, three devices showed an average PCE "
    "of 19.3 +/- 0.69% [@Azmi2022].",
    title="T95 retention after >1200 hours damp-heat test",
)

pce_after_damp_heat_19_3_percent = claim(
    "After more than 1000 hours of damp-heat testing, three devices showed an "
    "average PCE of 19.3 +/- 0.69%, representing excellent retention of device "
    "performance meeting IEC 61215:2016 protocols. The final PCE of more than "
    "19% after more than 1000 hours represents a very high retained PCE "
    "[@Azmi2022].",
    title="PCE of 19.3% after damp-heat test",
)

structural_optical_robustness = claim(
    "There was no substantial change in the structural and optical properties "
    "of the 2D perovskite passivation films (both 3D and 2D perovskites) after "
    "more than 500 hours of thermal annealing at 85 degrees C under dark "
    "conditions, confirming the robustness of the 2D perovskite passivation "
    "approach [@Azmi2022].",
    title="Structural and optical properties stable after 500 hours at 85C",
)

mppt_95_percent_retention = claim(
    "During MPPT testing under simulated 1-sun illumination in ambient air for "
    "more than 500 hours, 2D-RT-based devices retained up to approximately 95% "
    "of their initial PCE, whereas control devices retained PCE of less than 90% "
    "for only approximately 100 hours [@Azmi2022].",
    title="MPPT shows 95% retention after >500 hours",
)

enhanced_moisture_resistance = claim(
    "Unencapsulated devices tested in damp-heat chamber under thermal tests in "
    "ambient air with relative humidity more than 50% (extreme outdoor conditions) "
    "showed that the 2D capping layer introduced substantially enhanced resistance "
    "against high moisture and thermal stress [@Azmi2022].",
    title="Enhanced resistance against moisture and thermal stress",
)

industry_standard_achieved = claim(
    "The results represent the successful encapsulation of PSCs passing the "
    "industry-relevant damp-heat test according to IEC 61215:2016 protocols. "
    "This meets one of the critical industrial stability standards for PV "
    "modules [@Azmi2022].",
    title="IEC 61215:2016 damp-heat test passed",
)

# -----------------------------------------------------------------------------
# Comparison with prior approaches
# -----------------------------------------------------------------------------

rt_vs_ta_comparison = claim(
    "2D-RT passivation produced n >= 2 layers leading to better energy level "
    "alignment with C60 and higher device performance (PCE 24.3%, FF 82%), "
    "while 2D-TA produced only n=1 layers with poor energy level alignment "
    "(lower FF <79%) and lower overall device performance [@Azmi2022].",
    title="2D-RT outperforms 2D-TA due to higher n layers",
)

passivation_vs_control = claim(
    "2D-RT passivated devices significantly outperformed control devices "
    "without passivation: PCE increased from approximately 22% (control) to "
    "24.3% (2D-RT), representing approximately 2% absolute gain. The passivated "
    "devices also showed dramatically improved stability under damp-heat testing "
    "[@Azmi2022].",
    title="2D-RT passivation significantly outperforms control devices",
)