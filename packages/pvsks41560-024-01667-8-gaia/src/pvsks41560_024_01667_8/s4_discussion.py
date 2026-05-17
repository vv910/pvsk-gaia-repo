"""
s4_discussion.py - Defect passivation effects and photovoltaic performance.

This module covers:
- AFM and KPFM characterization of surface morphology
- Defect density measurements from SCLC
- Photovoltaic performance (J-V curves, EQE)
- Device stability characterization
"""

from gaia.lang import claim, setting

# AFM surface morphology results
afm_morphology = claim(
    "AFM reveals that mixed DABr/FABr post-treated perovskite film has smoother surface "
    "morphology compared to DABr post-treated and pristine perovskite films. The "
    "statistical distribution of height values shows narrower distribution for "
    "DABr/FABr-treated films, indicating improved uniformity [@Li2024].",
    title="DABr/FABr treatment produces smoother surface morphology",
    figure="artifacts/images/fig3.png",
)

# KPFM surface potential results
kpfm_surface_potential = claim(
    "KPFM shows narrower surface potential distribution for DABr/FABr post-treated "
    "perovskite film compared to DABr post-treated and pristine films. Gaussian "
    "distribution fitting of surface potential data confirms more uniform electronic "
    "properties across the surface [@Li2024].",
    title="DABr/FABr treatment produces uniform surface potential",
)

# Confocal PL mapping uniformity
confocal_pl_uniformity = claim(
    "Confocal PL mappings demonstrate uniform and strong PL emission of 3D signal for "
    "DABr/FABr post-treated perovskite, compared to pristine and DABr post-treated films. "
    "This indicates effective suppression of interfacial defect-assisted non-radiative "
    "recombination in DABr/FABr-treated samples [@Li2024].",
    title="DABr/FABr treatment shows uniform PL emission",
)

# Time-resolved confocal PL results
trpl_mapping_results = claim(
    "Time-resolved confocal PL mappings show pristine perovskite film has long lifetime "
    "(green region) in perovskite grains but short lifetime (blue region) at grain "
    "boundaries due to excessive PbI2 fragments. After DABr post-treatment, red regions "
    "(longer PL lifetime) appear and become dominant after DABr/FABr post-treatment, "
    "implying phase-pure n=2 2D structure minimizes defect-assisted charge recombination "
    "more effectively than mixed n=1 and n=2 structures [@Li2024].",
    title="DABr/FABr treatment increases carrier lifetime",
)

# Average carrier lifetime from TRPL
carrier_lifetime_trpl = claim(
    "Average carrier lifetimes (tau_ave) calculated from TRPL spectra of different "
    "perovskite films with and without hole transport layer (HTL) confirm that "
    "introduction of proper amount of DABr/FABr modification markedly passivates "
    "surface defects and accelerates hole extraction simultaneously. This is shown in "
    "Supplementary Tables 2 and 3 of the original paper [@Li2024].",
    title="TRPL confirms improved carrier lifetime with DABr/FABr",
)

# SCLC trap density results
sclc_trap_density = claim(
    "From SCLC measurements on electron-only and hole-only devices: DABr/FABr "
    "post-treatment gives most considerable reduction of Nt (trap density) values "
    "in both device configurations compared to DABr post-treated and pristine "
    "perovskite films. This correlates with improved perovskite film quality and "
    "is beneficial for enhancing device performance [@Li2024].",
    title="DABr/FABr reduces trap density",
)

# Mobility from SCLC
mobility_results = claim(
    "Electron and hole trap density (Nt) and mobility values of perovskite films "
    "quantified through SCLC measurements. DABr/FABr post-treatment shows improved "
    "mobility compared to DABr-only and pristine controls, consistent with reduced "
    "defect density and better interface quality [@Li2024].",
    title="DABr/FABr improves carrier mobility",
)

# Light irradiation stability
light_stability = claim(
    "In situ PL spectra performed with LED light source (405 nm) for 30 minutes show "
    "for DABr post-treated film: emission of n=1 2D phase disappears quickly within 2 min, "
    "while n=2 phase persists up to 20 min. In contrast, n=2 20 phase in DABr/FABr "
    "post-treated film exhibits higher PL intensity initially and can still be distinguished "
    "at 30 min. DABr/FABr post-treated perovskite film shows no notable decay compared "
    "to others, confirming pure n=2 20 perovskite is more structurally robust under "
    "light illumination [@Li2024].",
    title="DABr/FABr-treated film stable under light irradiation",
)

# Thermal stability
thermal_stability = claim(
    "Time-resolved GIWAXS and PL during 100 C thermal annealing shows for DABr post-treated "
    "film: sequential disappearance of n=1 (20 min) and n=2 (40 min) 2D phases, then "
    "generation of extra PbI2 (60 min) attributed to perovskite degradation. For "
    "DABr/FABr post-treated film, no noticeable changes tracked throughout entire heating "
    "process, indicating structural integrity of 3D/2D heterojunction is well maintained. "
    "Lower mixing enthalpy of DA-based quasi-2D (n=2) phases enables stable robust "
    "structure, resisting DA ions migration into 3D perovskite [@Li2024].",
    title="DABr/FABr maintains structural integrity during thermal annealing",
)

# Moisture stability
moisture_stability = claim(
    "DABr/FABr post-treated perovskite film shows larger water contact angle and slower "
    "film fading under highly humid air compared to controls, indicating improved "
    "moisture resistance. DABr/FABr-modified PSCs retain ~88% of initial PCEs in ambient "
    "air for >3000 h (20 C, 20% RH), whereas DABr and pristine devices only retain "
    "78% and 64% respectively [@Li2024].",
    title="DABr/FABr treatment improves moisture stability",
)

# Thermal stability of devices
device_thermal_stability = claim(
    "DABr/FABr post-treated PSCs show great thermal stability, maintaining 89% of initial "
    "PCEs after ~650 h under 55 C in N2, more stable than DABr post-treated (~72% after "
    "~650 h) and pristine (~59% after ~450 h) devices. The structural robustness upon "
    "heating contributes to improved thermal stability of the 3D/2D heterojunction [@Li2024].",
    title="DABr/FABr devices maintain thermal stability",
)

# Light soaking stability
light_soaking_stability = claim(
    "DABr/FABR devices exhibit superior light soaking stability in N2 atmosphere, "
    "maintaining ~93% of original efficiency for 2500 h under white LED light irradiation "
    "(continuous light illumination). This exceeds the stability of DABr-only and "
    "pristine devices under the same conditions [@Li2024].",
    title="DABr/FABr devices show excellent light soaking stability",
)

# Operational stability - MPPT
operational_stability = claim(
    "DABr/FABr post-treated encapsulated solar mini-module demonstrates remarkable "
    "operational stability with T80 lifetime exceeding 2000 h at maximum power point "
    "tracking (MPPT) under continuous light illumination. Performance before and after "
    "MPPT test shows minimal degradation, confirming excellent operational stability "
    "of the DABr/FABr approach [@Li2024].",
    title="Mini-module T80 lifetime exceeds 2000 hours",
)

# J-V curves comparison
jv_comparison = claim(
    "J-V curves of typical small PSCs with different post-treatments show DABr/FABr "
    "post-treatment achieves highest photovoltaic parameters among all samples. "
    "Most significant improvement in open-circuit voltage (Voc) is observed, attributed "
    "to defect minimization and favorable band alignment of uniform phase-pure "
    "quasi-2D perovskite passivation layer [@Li2024].",
    title="DABr/FABr achieves highest photovoltaic parameters",
)

# Champion small device efficiency
champion_small_device = claim(
    "DABr/FABr post-treated PSCs demonstrate champion PCE of 25.61% (certified 24.95%) "
    "for small devices (0.14 cm2). The corresponding integrated current density from EQE "
    "is as high as 24.80 mA/cm2, well matched with J-V characterization results [@Li2024].",
    title="25.61% champion efficiency for small device",
)

# Large-size device efficiency
large_device_efficiency = claim(
    "Large-size PSCs with aperture area of 1.04 cm2 achieve champion PCE of 24.62% "
    "(certified 24.04%) with DABr/FABr post-treatment. This demonstrates good "
    "scalability from small to large device areas with minimal efficiency loss [@Li2024].",
    title="24.62% efficiency for 1.04 cm2 large device",
)

# Mini-module efficiency
mini_module_efficiency = claim(
    "Antisolvent-free spin-coated mini-modules achieve high PCE of 23.60% on total "
    "aperture area of 13.44 cm2 with DABr/FABr treatment. High efficiency of 22.22% "
    "on aperture area of 16 cm2 with geometric filling factor (GFF) ~96% is also "
    "demonstrated, equivalent to active-area PCE of 23.1% [@Li2024].",
    title="23.60% efficiency for 13.44 cm2 mini-module",
)

# HDABr validation
hdabr_validation = claim(
    "HDABr/FABr-treated device shows lower efficiency than DABr/FABr-treated device "
    "due to oversized 2D ligand, but still demonstrates notable improvement over "
    "single HDABr-treated device. This suggests validity of homogeneous passivation "
    "approach even with larger ligands [@Li2024].",
    title="HDABr/FABr also improves over HDABr alone",
)

# Stability comparison summary
stability_comparison = claim(
    "Comprehensive stability comparison of devices with different post-treatment "
    "strategies shows DABr/FABr treatment provides best performance retention under "
    "thermal, moisture, and light soaking conditions. The structural robustness of "
    "phase-pure n=2 2D layer contributes to comprehensive stability improvement [@Li2024].",
    title="DABr/FABr provides best overall stability",
)