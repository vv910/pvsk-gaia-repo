"""
Methods module for Azmi et al. 2022 paper on damp heat-stable PSCs.

This module covers the experimental methods, characterization techniques,
device fabrication procedures, and processing conditions.
"""

from gaia.lang import claim, setting

# -----------------------------------------------------------------------------
# Device structure and architecture
# -----------------------------------------------------------------------------

device_structure = claim(
    "Inverted PSCs were fabricated with the structure: glass/ITO/2PACz/3D perovskite/"
    "2D perovskite/C60/bathocuproine (BCP)/Ag, where 2PACz is the hole-selective "
    "contact and C60 is the electron-selective contact [@Azmi2022].",
    title="Inverted PSC device structure",
    figure="artifacts/images/f36edc247e1cf48db214d869b83ce4333d6137e86635fb332b9d0077d2a83579.jpg",
    caption="Fig. 3A: Device architecture of inverted PSCs",
)

# -----------------------------------------------------------------------------
# OLAI post-treatment method
# -----------------------------------------------------------------------------

olai_post_treatment = claim(
    "Oleylammonium iodide (OLAI) molecules were applied to post-treat surface defects "
    "of 3D perovskites, forming Ruddlesden-Popper-phase 2D perovskite layers that "
    "resulted in higher PCEs and prolonged stabilities of inverted PSCs [@Azmi2022].",
    title="OLAI post-treatment method",
)

two_d_rt_processing = claim(
    "The 2D perovskite dimensionality (n) was tailored by tuning annealing conditions. "
    "2D-RT (room temperature) processing with OLAI molecules produced more pronounced "
    "higher-dimensionality layers (n >= 2) compared to 2D-TA (thermal annealing at "
    "100 degrees C) which was dominated by n=1 [@Azmi2022].",
    title="2D-RT vs 2D-TA processing conditions",
)

# -----------------------------------------------------------------------------
# Characterization techniques
# -----------------------------------------------------------------------------

giwaxs_characterization = claim(
    "Grazing-incidence wide-angle X-ray scattering (GIWAXS) was used to investigate "
    "the formation of 2D perovskite passivation films on 3D perovskites. The 2D "
    "perovskite passivation films exhibited diffraction qz peaks at approximately 0.2 "
    "to 0.5 Angstrom^-1, corresponding to the (001) and (002) planes of 2D perovskite "
    "crystals. 2D-TA films were dominated by n=1 layers with peak at qz approximately "
    "0.35 Angstrom^-1. 2D-RT films showed both n=1 and n=2 peaks, with substantial "
    "n=2 peak at lower qz [@Azmi2022].",
    title="GIWAXS characterization of 2D perovskite films",
    figure="artifacts/images/52ed4188068ba9353517ea429228b8c03b7aa55fb420fa76aae23e980f68652b.jpg",
    caption="Fig. 1C: GIWAXS maps of each film",
)

hr_stem_elemental_mapping = claim(
    "Cross-sectional high-resolution scanning transmission electron microscopy "
    "(HR-STEM) and high-angle annular dark-field (HAADF)/energy-dispersive X-ray "
    "spectroscopy (EDS) elemental mapping were used to differentiate between n=1 "
    "and n=2 layers. 2D-RT samples showed both n=1 and n=2 layers, while 2D-TA "
    "samples showed only n=1. The interlayer distances were approximately 1.2 nm "
    "for n=1 and approximately 1.5 nm for n=2 [@Azmi2022].",
    title="HR-STEM elemental mapping",
    figure="artifacts/images/7d3a48ec36304f0832c53a977f79d69198ea5527b649e1189fbd5c61a737904e.jpg",
    caption="Fig. 1E: HAADF/EDS elemental map of 2D-RT samples",
)

pl_characterization = claim(
    "Photoluminescence (PL) imaging and spectroscopy were used to characterize "
    "perovskite films. 2D perovskite passivation films exhibited stronger PL emission "
    "with longer PL decay lifetime than control 3D perovskite films due to suppression "
    "of nonradiative recombination associated with trap states at the surface. PL images "
    "at approximately 570 nm wavelength showed uniform n=2 capping layer formation "
    "on 3D perovskite surfaces for 2D-RT samples [@Azmi2022].",
    title="PL characterization",
    figure="artifacts/images/e54d44a0509ebef94cccb43fda2a9f0099e32f748d9b79c6aa2f37feb86d4ea0.jpg",
    caption="Fig. 2A: PL images of control 3D, 2D-TA, and 2D-RT films",
)

ups_energy_levels = claim(
    "Ultraviolet photoelectron spectroscopy (UPS) was used to determine energy-level "
    "diagrams. With OLAI post-treatment, the secondary electron cutoff shifted to "
    "higher binding energy, indicating that ion exchange-induced 3D-to-2D perovskite "
    "phase transition could lower the Fermi level of post-treated perovskite films. "
    "The energetic gap between Fermi level and VBM of 2D-RT samples was wider, "
    "indicating enhanced n-type character and successful 2D perovskite passivation. "
    "The CBM of 2D-RT films was closer to CBM of C60, enabling more efficient charge "
    "transfer at the 2D/3D perovskite interface [@Azmi2022].",
    title="UPS energy level measurements",
    figure="artifacts/images/3f7b317dea0ff692769d9e6ddad6b25cd6ba1cc9068db6fdd854c4e03e1facfc.jpg",
    caption="Fig. 2C: Energy level scheme for control and OLAI-treated films",
)

contact_angle_moisture_resistance = claim(
    "Contact angle measurements showed that 2D perovskite capping layers enhanced "
    "the resilience against moisture of 3D perovskite films, confirming improved "
    "environmental stability [@Azmi2022].",
    title="Contact angle moisture resistance",
)

sem_morphology = claim(
    "Scanning electron microscopy (SEM) topview images revealed that the surface "
    "morphology of perovskite films after 2D perovskite passivation did not change "
    "substantially [@Azmi2022].",
    title="SEM surface morphology unchanged",
)

# -----------------------------------------------------------------------------
# Device characterization
# -----------------------------------------------------------------------------

j_v_characteristics = claim(
    "Current density-voltage (J-V) characteristics were measured for inverted PSC "
    "devices. The 2D-RT devices demonstrated substantially improved PCEs with maximum "
    "PCE of 24.3%, stabilized PCE of approximately 24%, open-circuit voltage (VOC) "
    "of approximately 1.20 V, and fill factor (FF) of approximately 82% [@Azmi2022].",
    title="J-V device characteristics",
    figure="artifacts/images/0f05678c3c9719f454b06ffe47aa5055c0db665b266646291d62d463780af3ab.jpg",
    caption="Fig. 3C: J-V scan of champion PSCs",
)

pce_gain_absolute = claim(
    "The 2D-RT passivation yielded an absolute approximately 2% PCE gain compared "
    "to control devices, representing a substantial improvement in device performance "
    "[@Azmi2022].",
    title="Absolute PCE gain of 2%",
)

energy_loss_reduction = claim(
    "2D-RT passivation enables minimization of device energy loss (Eloss = Eg - qVOC) "
    "up to 0.34 eV, which represents approximately 96% of the thermodynamic limit "
    "of VOC (1.262 V) for Eg of 1.55 eV. This reduced nonradiative loss is comparable "
    "to state-of-the-art GaAs solar cells with VOC of 1.127 V yielding approximately "
    "98% of thermodynamic limit [@Azmi2022].",
    title="Energy loss minimization to 0.34 eV",
)

trap_assisted_recombination = claim(
    "Transient photovoltage decay and light intensity dependent measurements under "
    "open-circuit conditions showed that 2D-passivated devices exhibited longer "
    "charge recombination lifetime and lower ideality factor than control devices, "
    "confirming reduced trap-assisted recombination at 3D/C60 interfaces by the 2D "
    "perovskite passivation [@Azmi2022].",
    title="Reduced trap-assisted recombination",
)

# -----------------------------------------------------------------------------
# Stability testing
# -----------------------------------------------------------------------------

damp_heat_test_protocol = claim(
    "Encapsulated devices were subjected to damp-heat tests at 85 degrees C and 85% "
    "relative humidity according to IEC 61215:2016 protocols. The 2D perovskite "
    "passivation served simultaneously as ion migration-blocking moisture/oxygen "
    "ingress barriers and as defect passivation layers at elevated operating "
    "temperatures [@Azmi2022].",
    title="Damp-heat test protocol",
    figure="artifacts/images/9bee39095af7b7493d3509b57aa9cd38d84d8d285f861c2ee1d71559f9348204.jpg",
    caption="Fig. 3D: Variation of PCEs during damp-heat test",
)

mppt_measurement = claim(
    "Maximum power point tracking (MPPT) measurements were performed for "
    "encapsulated cells under simulated 1-sun illumination (AM 1.5) in ambient air "
    "for >500 hours [@Azmi2022].",
    title="MPPT measurement protocol",
    figure="artifacts/images/fa88eaf894bc3dbf94386ce2ada6de1693b8901bc428f88f2bbafa311e2dd714.jpg",
    caption="Fig. 3E: Continuous MPPT for encapsulated cells",
)

university_for_various_compositions = claim(
    "The proposed passivation approach was universal for various perovskite "
    "compositions (various bandgaps) and deposition techniques (one-step, two-step, "
    "and blade-coating), as demonstrated by systematic absolute PCE enhancement "
    "of 1.5 to 2.0% across different conditions [@Azmi2022].",
    title="Universal for various compositions and techniques",
)

reproducibility = claim(
    "The narrow statistical distribution of PCE, VOC, FF, and JSC values confirmed "
    "high reproducibility. Less than 0.5% deviation was observed for person-to-person "
    "variations among seven different researchers [@Azmi2022].",
    title="High reproducibility demonstrated",
)