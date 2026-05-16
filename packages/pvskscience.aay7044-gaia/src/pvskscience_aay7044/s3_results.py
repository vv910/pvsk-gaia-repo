"""
Results for the Min2019 perovskite solar cell paper.

This module covers experimental results: UV-vis/PL spectra, XRD phase stability,
device performance (J-V curves, EQE), defect characterization (SCLC, TRPL),
elemental analysis (XPS, ToF-SIMS), and stability tests (humidity, thermal, photostability).
"""

from gaia.lang import claim

# -----------------------------------------------------------------------------
# Optical absorption and bandgap results
# -----------------------------------------------------------------------------

uvvis_blue_shift = claim(
    "UV-vis absorption spectra of FAPbI3:xMDACl2 (x = 0, 1.9, 3.8, 5.7 mol%) showed "
    "a progressive slight blue-shift with increasing MDACl2 content. The absorption "
    "edge for x=3.8 mol% was nearly identical to that of FAPbI3 without MACl (control "
    "without the MACl mediator), confirming minimal bandgap widening with MDACl2 "
    "incorporation. In contrast, the MAPbBr3 control showed a larger blue-shift "
    "to 816 nm (816 nm PL peak), consistent with greater bandgap widening from Br "
    "incorporation [@Min2019].",
    title="UV-vis blue shift minimal with MDACl2",
)

pl_peak_shifts = claim(
    "PL emission peaks for FAPbI3:xMDACl2 shifted progressively: 826 nm (x=0), "
    "824 nm (x=1.9 mol%), 822 nm (x=3.8 mol%), and 820 nm (x=5.7 mol%). The control "
    "(0.95 FAPbI3/0.05 MAPbBr3) showed a PL peak at 816 nm, confirming that MDACl2 "
    "causes less bandgap widening than MAPbBr3 for equivalent stabilizing amounts. "
    "This indicates MDACl2 preserves the inherent narrow bandgap of FAPbI3 [@Min2019].",
    title="PL peak shifts confirm minimal bandgap change",
)

bandgap_values = claim(
    "The optical bandgap values derived from UV-vis spectra are: pristine FAPbI3 "
    "(1.45 eV), x=1.9 mol% (1.47 eV), x=3.8 mol% (1.49 eV), x=5.7 mol% (1.51 eV), "
    "and control 0.95 FAPbI3/0.05 MAPbBr3 (1.53 eV). These values confirm that "
    "MDACl2 produces a much smaller bandgap increase compared to MAPbBr3 at similar "
    "compositions [@Min2019].",
    title="Bandgap values for different compositions",
)

dft_bandgap_fa_vacancy = claim(
    "DFT calculations for the FA vacancy composition "
    "(FA1-2xMDAx)Pb(I1-xClx)3 yielded a bandgap of 1.47 eV for x=0.037 (corresponding "
    "to 3.8 mol% MDACl2), slightly above the pristine FAPbI3 value of 1.45 eV. "
    "This is consistent with the experimental observation of a small blue-shift "
    "[@Min2019].",
    title="DFT bandgap for FA vacancy composition",
)

dft_bandgap_cl_interstitial = claim(
    "DFT calculations for the Cl interstitial composition "
    "(FA1-xMDAx)PbI3Clx yielded a bandgap of 1.69 eV for x=0.037, substantially "
    "higher than pristine FAPbI3. This indicates that Cl interstitial incorporation "
    "causes significant bandgap widening, but this mechanism is not dominant in "
    "the actual experimental samples where FA vacancies predominate [@Min2019].",
    title="DFT bandgap for Cl interstitial composition",
)

pl_quality_enhancement = claim(
    "Adding 3.8 mol% MDACl2 to FAPbI3 enhanced the PL quantum yield (measured with "
    "an integrated sphere) compared to pristine FAPbI3. However, further MDACl2 "
    "addition (5.7 mol%) greatly reduced PL quantum yield. This indicates that FA "
    "defects at 3.8 mol% do not act as deep electron traps, while excess MDACl2 "
    "introduces non-radiative recombination pathways [@Min2019].",
    title="PL quantum yield enhancement at optimal MDACl2",
)

# -----------------------------------------------------------------------------
# Phase stability results
# -----------------------------------------------------------------------------

humidity_phase_stability = claim(
    "After exposure to 80% relative humidity for 24 hours: pure FAPbI3 (x=0) "
    "completely converted from alpha-phase to delta-phase (detected by XRD at 11.6); "
    "1.9 mol% MDACl2 showed strong phase transition toward delta-phase; 3.8 and "
    "5.7 mol% MDACl2 samples retained pure alpha-phase. The control (MAPbBr3 "
    "stabilized) also showed some delta-phase formation. This demonstrates that "
    "3.8 mol% MDACl2 is the minimum threshold for effective humidity-induced "
    "phase stabilization [@Min2019].",
    title="Humidity-induced phase transition results",
)

alpha_phase_retention_38 = claim(
    "FAPbI3 with 3.8 mol% MDACl2 retained the pure alpha-phase after 24 hours at "
    "80% humidity, while pure FAPbI3 fully converted to the delta-phase. This "
    "confirms that MDA2+ incorporation at 3.8 mol% is sufficient to kinetically "
    "stabilize the metastable alpha-phase against humidity-induced phase transition "
    "[@Min2019].",
    title="3.8 mol% MDACl2 prevents humidity-induced phase transition",
)

alpha_phase_retention_57 = claim(
    "FAPbI3 with 5.7 mol% MDACl2 also retained the pure alpha-phase after 24 hours "
    "at 80% humidity, comparable to the 3.8 mol% sample. This confirms a broad "
    "composition range (at least 3.8 to 5.7 mol%) provides effective alpha-phase "
    "stabilization [@Min2019].",
    title="5.7 mol% MDACl2 also prevents phase transition",
)

crystallinity_improvement = claim(
    "XRD signal intensity increased for MDACl2 addition up to 3.8 mol% without any "
    "impurity peaks, indicating improved crystallinity. Incorporation of >3.8 mol% "
    "MDACl2 may further increase crystallinity by reducing lattice strain at FA "
    "defect sites. No peaks corresponding to FACl or MDACl2 were detected, "
    "confirming complete incorporation and FACl elimination during annealing "
    "[@Min2019].",
    title="MDACl2 improves crystallinity without secondary phases",
)

giwaxs_no_impurity = claim(
    "GIWAXS analysis of x=3.8 mol% and control samples showed identical ring patterns "
    "assigned to alpha-FAPbI3 (100)c, (200)c, (210)c, delta-FAPbI3 (100)h, and "
    "PbI2 (001)t. No diffraction peaks from FACl, MDACl2, or other secondary phases "
    "were observed in either sample. The fitted azimuthal circular average GIWAXS "
    "1D spectra were nearly identical, confirming that MDA substitution does not "
    "alter the crystal structure or create secondary phases [@Min2019].",
    title="GIWAXS confirms no secondary phases",
)

xrd_peak_lower_angle = claim(
    "The XRD (001) orientation peak shifted to a lower diffraction angle with "
    "increasing MDACl2 content (for x=3.8 and 5.7 mol%), indicating lattice expansion. "
    "This expansion is consistent with interstitial Cl- ions (radius 181 pm) in the "
    "lattice rather than contraction from increased hydrogen bonding. The shift "
    "corroborates the DFT prediction that Cl interstitials rather than simple "
    "substitution dominate the structural effect [@Min2019].",
    title="XRD peak shift to lower angle indicates interstitial Cl",
)

# -----------------------------------------------------------------------------
# Device performance results
# -----------------------------------------------------------------------------

pce_distributions = claim(
    "PCE distributions for FAPbI3:xMDACl2 PSCs (x = 0, 1.9, 3.8, 5.7 mol%) and "
    "control showed: x=0 (average 22.01%), x=1.9 (22.46%), x=3.8 (22.46%), "
    "x=5.7 (22.25%), and control (23.05%). The x=3.8 sample showed improved average "
    "PCE compared to undoped FAPbI3, mainly from increased JSC while maintaining "
    "similar or higher VOC and FF. The x=5.7 sample showed slight PCE decline due "
    "to degraded crystallinity and PL [@Min2019].",
    title="PCE distributions across compositions",
)

target_best_jv = claim(
    "The best-performing target device (3.8 mol% MDACl2) showed: JSC = 26.50 mA/cm2, "
    "VOC = 1.14 V, FF = 81.77%, PCE = 24.66% under standard AM 1.5 conditions "
    "(100 mW/cm2) in reverse bias sweep. The control device showed: "
    "JSC = 25.14 mA/cm2, VOC = 1.14 V, FF = 80.55%, PCE = 23.05%. The target's "
    "improvement is primarily from higher JSC (+1.36 mA/cm2) while VOC remained "
    "identical and FF slightly improved [@Min2019].",
    title="Best target vs control J-V parameters",
)

certified_pce = claim(
    "Two target devices were certified by Newport, USA using the quasi-steady-state "
    "(QSS) method: Device 1 achieved JSC = 26.10 mA/cm2, VOC = 1.15 V, "
    "FF = 79.0%, stabilized PCE = 23.73%; Device 2 achieved JSC = 26.70 mA/cm2 "
    "(highest reported for FAPbI3-based PSCs), VOC = 1.144 V, FF = 77.56%, "
    "stabilized PCE = 23.69%. Both values represent the highest certified "
    "efficiencies for mp-TiO2-based PSCs reported at the time [@Min2019].",
    title="Certified PCE measurements",
)

highest_jsc = claim(
    "The certified JSC of 26.70 mA/cm2 represents the highest short-circuit current "
    "density reported for PSCs fabricated from FA-based lead halide perovskites. "
    "This was achieved by maintaining the inherent narrow bandgap of FAPbI3 while "
    "stabilizing the alpha-phase with MDACl2, enabling enhanced photon absorption "
    "in the near-infrared region compared to wider-bandgap compositions [@Min2019].",
    title="Highest JSC for FA-based PSCs",
)

eqe_expanded_range = claim(
    "External quantum efficiency (EQE) measurements showed that the target device "
    "(3.8 mol% MDACl2) had an expanded absorption wavelength range compared to the "
    "control. This EQE improvement explains the higher JSC of the target, arising "
    "from the narrower bandgap maintained with MDACl2 vs MAPbBr3 in the control "
    "[@Min2019].",
    title="EQE confirms expanded absorption range",
)

morphology_unchanged = claim(
    "Scanning electron microscopy (SEM) comparison of target and control showed no "
    "notable differences in surface roughness, grain size, or cross-sectional "
    "perovskite layer thickness. This confirms that introducing MDACl2 into the "
    "FAPbI3 precursor does not negatively affect perovskite film morphology "
    "[@Min2019].",
    title="Morphology unchanged by MDACl2",
)

# -----------------------------------------------------------------------------
# Defect and carrier dynamics
# -----------------------------------------------------------------------------

electron_trap_density = claim(
    "Electron trap densities (N_defects) from SCLC measurements: x=0 (5.4x10^15 cm-3), "
    "x=1.9 (7.6x10^15 cm-3), x=3.8 (5.7x10^15 cm-3), x=5.7 (8.0x10^15 cm-3), "
    "and control (1.0x10^16 cm-3). The electron trap density remained low and "
    "comparable across all FAPbI3:MDACl2 compositions, all lower than the control. "
    "This indicates that MDACl2 incorporation does not introduce detrimental electron "
    "traps and may even reduce them slightly compared to the control [@Min2019].",
    title="Electron trap density measurements",
)

hole_trap_reduction = claim(
    "Hole-only device measurements (not detailed in this module) showed that the "
    "hole-trap density decreased with MDACl2 addition relative to the control, "
    "suggesting MDA2+ or associated defects passivate hole traps in addition to "
    "providing structural stabilization [@Min2019].",
    title="Hole trap density reduction",
)

carrier_lifetime_target = claim(
    "Time-resolved PL measurements on quartz substrates showed that the target "
    "(3.8 mol% MDACl2) had a non-radiative recombination lifetime of 1562 ns, "
    "more than double the control lifetime of 715 ns. This extended lifetime "
    "indicates reduced trap-assisted non-radiative recombination in the "
    "MDA-stabilized films, consistent with passivation effects from interstitial "
    "Cl- and improved film quality [@Min2019].",
    title="Carrier lifetime doubled in target",
)

cl_enriched_interface = claim(
    "XPS depth profiling and ToF-SIMS showed that the Cl content in the target "
    "(3.8 mol% MDACl2) was higher than in the control throughout the perovskite "
    "film, with Cl enrichment particularly concentrated at the TiO2/perovskite "
    "interface. This interfacial Cl enrichment is expected to increase "
    "photostability by suppressing TiO2 photocatalytic degradation reactions "
    "[@Min2019, refs 41-42].",
    title="Cl enrichment at TiO2 interface",
)

# -----------------------------------------------------------------------------
# Stability results
# -----------------------------------------------------------------------------

humidity_stability = claim(
    "Under 85% RH at 25C (unencapsulated devices), the target device retained more "
    "than 90% of its initial PCE after 70 hours, while the control PCE degraded to "
    "only 40% of its initial value. The target's humidity stability far exceeds the "
    "control, demonstrating effective alpha-phase stabilization by MDACl2 against "
    "moisture-induced phase transition [@Min2019].",
    title="Humidity stability: target retains >90% PCE at 70h",
)

thermal_stability = claim(
    "At 150C and approximately 25% RH (unencapsulated devices), the control device "
    "PCE degraded gradually to less than 20% of its initial value after 17 hours, "
    "primarily due to MA evaporation from the MAPbBr3 component. The target device "
    "retained more than 90% of its initial PCE even after 20 hours at 150C in air. "
    "This superior thermal stability confirms the absence of MA in the target "
    "and the effectiveness of MDACl2 stabilization [@Min2019].",
    title="Thermal stability: target retains >90% PCE after 20h at 150C",
)

photostability = claim(
    "Under maximum power point tracking at full AM 1.5G illumination (100 mW/cm2) "
    "in ambient conditions without a UV filter (encapsulated device with spiro-OMeTAD "
    "HTM), the target device maintained approximately 90% of its initial PCE "
    "(greater than 23.0%) over 600 hours of continuous irradiation. This "
    "photostability is attributed to both the high concentration of Cl ions at the "
    "TiO2 interface and the alpha-phase stabilization by MDACl2, which protects "
    "against UV-induced and heat-induced degradation [@Min2019].",
    title="Photostability: >90% PCE retained after 600 hours MPP tracking",
)

# -----------------------------------------------------------------------------
# Key exported conclusions
# -----------------------------------------------------------------------------

optimal_composition = claim(
    "The optimal MDACl2 composition for FAPbI3 is 3.8 mol%, which provides: "
    "(1) effective alpha-phase stabilization under humidity, (2) minimal bandgap "
    "widening (1.49 eV vs 1.45 eV for pristine), (3) improved PCE of 24.66% "
    "(certified 23.73%), (4) the highest reported JSC for FA-based PSCs "
    "(26.70 mA/cm2 certified), and (5) excellent operational stability exceeding "
    "600 hours under full sunlight with MPP tracking [@Min2019].",
    title="Optimal MDACl2 composition is 3.8 mol%",
)

mda_superior_to_mapbbr3 = claim(
    "Compared to the MAPbBr3-stabilized control (the best prior mp-TiO2-based PSC "
    "at 23.05% PCE), the MDACl2-stabilized target achieves higher PCE (24.66% best, "
    "23.73% certified), higher JSC (26.50 vs 25.14 mA/cm2), superior humidity "
    "stability (>90% vs 40% after 70h at 85% RH), superior thermal stability "
    "(>90% after 20h at 150C vs <20% for control), and maintains the inherent "
    "narrower bandgap of FAPbI3 without Br-induced widening. This demonstrates "
    "that MDACl2 is superior to MAPbBr3 for stabilizing alpha-FAPbI3 in PSCs "
    "[@Min2019].",
    title="MDACl2 stabilization outperforms MAPbBr3 control",
)

__all__ = [
    "uvvis_blue_shift",
    "pl_peak_shifts",
    "bandgap_values",
    "dft_bandgap_fa_vacancy",
    "dft_bandgap_cl_interstitial",
    "pl_quality_enhancement",
    "humidity_phase_stability",
    "alpha_phase_retention_38",
    "alpha_phase_retention_57",
    "crystallinity_improvement",
    "giwaxs_no_impurity",
    "xrd_peak_lower_angle",
    "pce_distributions",
    "target_best_jv",
    "certified_pce",
    "highest_jsc",
    "eqe_expanded_range",
    "morphology_unchanged",
    "electron_trap_density",
    "hole_trap_reduction",
    "carrier_lifetime_target",
    "cl_enriched_interface",
    "humidity_stability",
    "thermal_stability",
    "photostability",
    "optimal_composition",
    "mda_superior_to_mapbbr3",
]