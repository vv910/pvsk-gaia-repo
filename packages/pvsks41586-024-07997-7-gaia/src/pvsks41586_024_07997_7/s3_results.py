"""
Results module for pvsks41586-024-07997-7-gaia.

This module covers the experimental results including recombination loss analysis,
interfacial properties, theoretical calculations, and photovoltaic performance.

Paper: Perovskite/silicon tandem solar cells with bilayer interface passivation
DOI: 10.1038/s41586-024-07997-7
"""

from gaia.lang import (
    claim,
    setting,
    support,
    infer,
    compare,
    abduction,
    contradiction,
)

from .motivation import (
    lif_limited_effectiveness,
    edai_chemical_passivation,
    bilateral_passivation_strategy,
    double_textured_silicon,
)

# =============================================================================
# Recombination Loss Analysis Results
# =============================================================================

pl_intensity_ranking = claim(
    "PL imaging showed the bare perovskite sample without any capping layer exhibited the highest "
    "PL intensity. The PL intensity of the LiF/EDAI bilayer lay between those of samples with LiF "
    "and EDAI alone. Direct deposition of C60 on perovskite surface resulted in substantial reduction "
    "in PL emission intensity and TRPL lifetime, indicating high defect density at this interface.",
    title="PL intensity ranking of passivation layers",
    metadata={"figure": "artifacts/images/.../fig1a.png"},
)

plqy_increase_with_c60 = claim(
    "PLQY data showed that in the absence of C60 layer, slight increase in PLQY was observed after "
    "LiF deposition on bare perovskite surface, whereas EDAI deposition alone showed slight decrease. "
    "On a logarithmic scale, no significant change in PLQY was observed for cases without C60. "
    "Difference in PLQY values became clear in presence of C60, indicating passivation effect manifests "
    "only when perovskite is paired with C60.",
    title="PLQY behavior with and without C60",
    metadata={"figure": "artifacts/images/.../fig1b.png"},
)

plqy_with_complete_top_contact = claim(
    "After complete C60/SnO2/IZO top contact depositions, further increase in PLQY was observed, "
    "but the trend that EDAI/LiF bilayer passivation leads to highest PLQY among all C60-coated samples "
    "remained consistent.",
    title="PLQY with complete top contacts",
    metadata={"figure": "artifacts/images/.../fig1b.png"},
)

trpl_lifetime_results = claim(
    "TRPL results and PL images showed that with complete top contact of SnO2/IZO/IZO stack, "
    "EDAI and LiF/EDAI samples exhibited impressively high differential lifetime of >10 microseconds "
    "at rather high PL flux, suggesting minimized non-radiative recombination. This enhancement "
    "benefits Voc and FF values of the perovskite device.",
    title="TRPL lifetime results",
    metadata={"figure": "artifacts/images/.../fig1c.png"},
)

passivation_targets_perovskite_c60 = claim(
    "Effective passivation should target the perovskite/C60 interface rather than bare perovskite "
    "surface. Only after deposition of C60 layer or complete top contacts, passivation efficacy "
    "of interlayers can be revealed.",
    title="Passivation must target perovskite/C60 interface",
)

single_junction_device_results = claim(
    "Semitransparent single-junction p-i-n devices with aperture area approximately 1.0 cm^2 were "
    "fabricated on textured silicon substrates. The unpassivated device yielded Voc and FF of "
    "approximately 1.17 V and 76.2%, respectively, with pseudo-FF of 82.0%. With LiF, EDAI, and "
    "LiF/EDAI bilayer, Voc improved to approximately 1.20, 1.25, and 1.27 V, respectively, while "
    "FF increased to 77.7%, 79.1%, and 80.8%, respectively.",
    title="Single-junction device performance with passivation layers",
    metadata={"figure": "artifacts/images/.../fig1d.png"},
)

pseudo_ff_values = claim(
    "Pseudo-FF values increased to 83.6%, 86.5%, and 86.1% for LiF, EDAI, and LiF/EDAI samples, "
    "respectively, compared with 82.0% for unpassivated device.",
    title="Pseudo-FF improvement with passivation",
    metadata={"figure": "artifacts/images/.../fig1d.png"},
)

power_loss_analysis = claim(
    "Theoretical limit of a 1.69-eV-bandgap cell with 29.1% efficiency and 90.9% FF was used for "
    "comparison. Using LiF/EDAI bilayer passivation resulted in increase in device efficiency to 22.2%, "
    "compared with 20.2% and 21.2% for LiF and EDAI cases, respectively. Compared with EDAI alone, "
    "LiF/EDAI bilayer exhibited reduced current transport loss narrowing from 2.1 to 1.5 mW/cm^2, "
    "indicating lower contact resistance.",
    title="Power loss analysis comparison",
    metadata={"figure": "artifacts/images/.../fig1e.png"},
)

# =============================================================================
# Interfacial Properties Results
# =============================================================================

tof_sims_lif_distribution = claim(
    "TOF-SIMS measurements showed LiF-related fragment distribution confirming discontinuous "
    "nature of the LiF layer. The Cs2CN+ signal attributed to EDA+ from EDAI showed obvious peak "
    "at front interface followed by flat region (150-500 s sputter time), indicating EDAI did not "
    "penetrate into bulk perovskite.",
    title="TOF-SIMS LiF fragment distribution",
    metadata={"figure": "artifacts/images/.../fig2a.png"},
)

tof_sims_edai_distribution = claim(
    "TOF-SIMS showed EDAI-related charged fragments mainly localized on surface of perovskite. "
    "No clear interface between LiF and EDAI layers was observed, indicating the two layers are "
    "intertwined with each other.",
    title="TOF-SIMS EDAI distribution confirms intertwining",
    metadata={"figure": "artifacts/images/.../fig2b.png"},
)

lif_discontinuity_confirmation = claim(
    "TEM results confirmed that the ultrathin LiF layer is discontinuous, allowing EDAI molecule "
    "to locally contact perovskite across the LiF layer. The charge carrier transport at LiF/EDAI "
    "bilayer interface is not affected as LiF opening spacing is only a few nanometers, which is "
    "evidently smaller than charge diffusion length of perovskite absorber.",
    title="LiF discontinuity enables EDAI contact",
    metadata={"figure": "artifacts/images/.../fig2c.png"},
)

kpfm_surface_potential = claim(
    "KPFM imaging showed that for samples without LiF layer, surface potential mapping is relatively "
    "smooth with no evident point-like features. For samples with LiF layer, point-like regions with "
    "low potentials could frequently be observed, attributed to discrete LiF fragments.",
    title="KPFM confirms discrete LiF regions",
    metadata={"figure": "artifacts/images/.../fig7.png"},
)

electric_field_enhancement = claim(
    "Cross-sectional KPFM measurements showed that for unpassivated and LiF-treated devices, "
    "amplitude of electric-field variation at perovskite/ETL interface is relatively small. "
    "Implementing extra EDAI treatment on LiF-coated device made changes in interfacial electric "
    "field become significant. LiF/EDAI bilayer passivation enables improved charge separation "
    "at perovskite/C60 interface regardless of perovskite contacting valley or spire region of "
    "silicon wafer pyramid.",
    title="EDAI enhances interfacial electric field",
    metadata={"figure": "artifacts/images/.../fig2d-f.png"},
)

xps_pb4f_shift = claim(
    "XPS measurements showed small shift in two characteristic main peaks of Pb4f after EDAI "
    "deposition, signifying chemical interaction of EDAI with Pb ions.",
    title="EDAI chemical interaction with Pb ions",
    metadata={"figure": "artifacts/images/.../fig2g.png"},
)

metallic_pb_suppression = claim(
    "Samples without EDAI treatments showed peaks at approximately 141.5 eV and 136.5 eV attributed "
    "to presence of metallic Pb(0), which might be transformed from uncoordinated surface Pb2+ ions "
    "or photodegraded PbI2 phase. After EDAI deposition, magnitude of Pb(0) peak was reduced to "
    "almost invisible, providing strong evidence that EDAI treatment chemically modifies perovskite "
    "surface. LiF/EDAI bilayer treatment showed identical effect as EDAI treatment in suppressing "
    "metallic Pb(0), confirming ultrathin LiF layer did not hinder chemical interaction.",
    title="EDAI suppresses metallic Pb formation",
    metadata={"figure": "artifacts/images/.../fig2g.png"},
)

xps_n1s_results = claim(
    "N1s signals displayed two separated peaks corresponding to C=N bond of formamidinium (FA) at "
    "around 400.5 eV and C-N bond of methylammonium (MA) or EDAI molecules at approximately 402.5 eV. "
    "After subtracting MA component from perovskite film, C-N/C=N ratio was significantly weakened "
    "as EDAI was deposited on LiF-coated perovskite, indicating LiF interlayer could reduce reactivity "
    "of EDAI with perovskite surface or limit penetration into perovskite film.",
    title="N1s XPS confirms EDAI surface modification",
    metadata={"figure": "artifacts/images/.../fig2h.png"},
)

work_function_reduction = claim(
    "UPS measurements showed bilayer-treated sample exhibited smaller work function (WF) of 4.06 eV "
    "compared with bare perovskite (4.47 eV).",
    title="Work function reduction with bilayer treatment",
    metadata={"figure": "artifacts/images/.../fig2i.png"},
)

fermi_level_to_valence_band = claim(
    "The difference between Fermi level and valence band (VB) edge in EDAI-treated sample "
    "(EF-EV = 1.41 eV) was larger than that on bare perovskite surface (0.90 eV), implying surface "
    "energy level bent downwards after EDAI treatments enhancing electron transport.",
    title="Fermi level to VB edge increase",
    metadata={"figure": "artifacts/images/.../fig2i.png"},
)

ionization_potential_slight_increase = claim(
    "Ionization potential (IE) values were 5.37 eV for bare perovskite and 5.47 eV for bilayer-treated "
    "sample. Surface treatments caused slight increase in IE indicating presence of interfacial dipole.",
    title="Ionization potential increase with treatment",
    metadata={"figure": "artifacts/images/.../fig2i.png"},
)

c60_interface_ie_variation = claim(
    "With 3-nm-thin C60 layer, IE variation became significant with values of 6.36 eV (untreated) "
    "and 6.04 eV (bilayer-treated). Surface treatment affected properties of subsequently deposited "
    "C60 layer close to the interface, affecting conduction band offset between perovskite and C60.",
    title="C60 causes significant IE change",
    metadata={"figure": "artifacts/images/.../fig2i.png"},
)

# =============================================================================
# Theoretical Calculation Results
# =============================================================================

dft_slab_structures = claim(
    "DFT calculations on representative FAPbI3(100) surfaces before and after molecular passivation "
    "considered two key terminations: FAI-rich and PbI2-rich, each bearing surface defects in form of "
    "lead vacancy (VPb) and FA vacancy (VFA). Calculations examined diammonium cations with different "
    "carbon chains and monovalent n-propylammonium cations (PA+) featuring alkyl end instead of "
    "two amine ends.",
    title="DFT calculation setup and surface defects",
    metadata={"figure": "artifacts/images/.../fig3a-b.png"},
)

pa_vs_eda_orientation = claim(
    "DFT calculations revealed distinct contrast in orientations of PA+ and EDA2+ with respect to "
    "binding to perovskite surface. PA+ exhibited nearly vertical binding to perovskite surface. "
    "By contrast, EDA2+ adopted horizontal configuration forming bridge-like structure with its two "
    "amine groups, maximizing out-of-plane charge transport across organic layer.",
    title="PA+ vertical vs EDA2+ horizontal binding",
    metadata={"figure": "artifacts/images/.../fig3a-b.png"},
)

binding_energy_comparison = claim(
    "Calculated binding energies (Eb) for diammonium EDA2+ on FAI-rich and PbI2-rich surfaces were "
    "-6.6 and -8.4 eV, respectively, substantially larger in absolute value than those of monoammonium "
    "PA+. This suggests EDAI molecules bind more firmly to perovskite surface providing enhanced "
    "chemical passivation capabilities.",
    title="EDA2+ binding energy substantially larger than PA+",
    metadata={"figure": "artifacts/images/.../fig3c.png"},
)

trap_state_elimination = claim(
    "Calculated projected density of states (PDOS) demonstrated existence of shallow trap states "
    "near VB edge for defective PbI2-rich case in absence of PA+ and EDA2+ adsorption. However, "
    "these shallow states were effectively eliminated after EDAI passivation, displaying substantial "
    "passivation effect.",
    title="EDAI effectively eliminates shallow trap states",
    metadata={"figure": "artifacts/images/.../fig3d-e.png"},
)

# =============================================================================
# Photovoltaic Performance Results
# =============================================================================

textured_substrate_optimization = claim(
    "To adapt silicon bottom cell for perovskite solution deposition, pyramid size of silicon front "
    "surface was optimized with optimal range of 0.5-1 micrometer. Double-sided mild texture caused "
    "Voc and FF losses compared with standard SHJ production line using pyramid size of 3-5 micrometer "
    "on both sides. Asymmetrically sized texture (texture D) with small-sized pyramid on front and "
    "standard-sized pyramid on rear improved both Voc and FF compared with double-sided mild texture.",
    title="Asymmetric texture optimization improves performance",
    metadata={"figure": "artifacts/images/.../fig4a.png"},
)

minority_carrier_lifetime = claim(
    "Effective minority carrier lifetime measurements showed texture A and texture D could hold "
    "tau_eff values of 3.2 and 3.4 ms, respectively, at excess carrier density of 5x10^15 cm^-3. "
    "Double-sided mild texture (texture C) reduced lifetime to only 1.6 ms.",
    title="Minority carrier lifetime by texture type",
    metadata={"figure": "artifacts/images/.../fig4d.png"},
)

eqe_spectral_response = claim(
    "EQE comparison showed multiple reflections at back induced by large-sized pyramids results in "
    "improved collection of infrared photons. EQE difference between textures mainly lies in "
    "long-wavelength range. Mild texture suffers loss of 2.1 mA/cm^2 in 900-1200 nm wavelength range "
    "compared with only 1.9 mA/cm^2 for standard texture.",
    title="Large pyramid texture improves infrared response",
    metadata={"figure": "artifacts/images/.../fig4e.png"},
)

voc_statistical_improvement = claim(
    "For unpassivated tandems, Voc value was mostly below 1.90 V. With LiF, EDAI, and LiF/EDAI "
    "bilayer passivation, average Voc improved to around 1.92, 1.94, and 1.96 V, respectively. "
    "Bilayer passivation achieved average PCE exceeding 33% with some devices reaching above 33.8%.",
    title="Voc and PCE statistical improvement with bilayer",
    metadata={"figure": "artifacts/images/.../fig4f.png"},
)

fill_factor_improvement = claim(
    "EDAI capping layer improved Voc obviously but led to reduced FF and increased data dispersion "
    "due to trade-off between passivation and contact resistance. By contrast, LiF/EDAI bilayer "
    "passivation not only improved Voc but also increased FF due to suppressed interfacial recombination "
    "coupled with more efficient charge extraction at ETL interface.",
    title="Bilayer achieves both Voc improvement and FF enhancement",
    metadata={"figure": "artifacts/images/.../fig4f.png"},
)

champion_device_jv = claim(
    "Champion tandem device showed forward scan PCE of 33.96% and reverse scan PCE of 34.08%, "
    "with current density (Jsc) of 20.67 mA/cm^2 (forward) and 20.68 mA/cm^2 (reverse), Voc of 1.981 V "
    "(forward) and 1.980 V (reverse), and FF of 82.9% (forward) and 83.2% (reverse).",
    title="Champion tandem J-V performance",
    metadata={"figure": "artifacts/images/.../fig4g.png"},
)

stabilized_power_output = claim(
    "Maximum power output of 34.0 mW/cm^2 at fixed voltage of 1.71 V was achieved under standard "
    "AM 1.5G spectra.",
    title="Stabilized power output",
    metadata={"figure": "artifacts/images/.../fig4g.png"},
)

nrel_certified_pce = claim(
    "NREL certified the device delivering stabilized PCE of 33.89% verified against in-house "
    "measurements, representing the first double-junction tandem surpassing single-junction "
    "Shockley-Queisser limit of 33.7%.",
    title="NREL certified 33.89% PCE",
    metadata={"figure": "artifacts/images/.../fig4h.png"},
)

storage_stability = claim(
    "Devices with LiF/EDAI bilayer passivation exhibited improved long-term storage stability in "
    "air for over 50 days compared with LiF-treated control device. After 53 days of air storage, "
    "LiF/EDAI devices retained approximately 90% of original PCEs, whereas control devices decreased "
    "to 82%.",
    title="Bilayer passivation improves air storage stability",
    metadata={"figure": "artifacts/images/.../fig4i.png"},
)

operational_stability = claim(
    "Under simulated 1-sun illumination and maximum power point tracking at room temperature in "
    "nitrogen environment, bilayer-treated tandem retained approximately 80% of initial PCE after "
    "1,200 hours of operation, whereas LiF-treated device retained less than 60% of initial PCE. "
    "Bilayer passivation initial PCE was 33.2% versus 30.7% for LiF-treated control.",
    title="Bilayer passivation enables 80% retention after 1200h operation",
    metadata={"figure": "artifacts/images/.../fig4j.png"},
)

# =============================================================================
# Abduction: Why bilayer outperforms single layers
# =============================================================================

# Theoretical predictions (hypotheses)
theoretical_prediction_lif_only = claim(
    "LiF alone (discontinuous ~1nm) provides field passivation through contact displacement but "
    "cannot sufficiently passivate the perovskite/C60 interface due to its discrete nature, leading "
    "to large voltage deficit and high contact resistance.",
    title="LiF-only theoretical limitation",
)

theoretical_prediction_edai_only = claim(
    "EDAI alone provides chemical passivation through coordinate binding to Pb defects but faces "
    "trade-off between passivation and charge extraction, resulting in reduced fill factor and "
    "increased contact resistance.",
    title="EDAI-only theoretical limitation",
)

theoretical_prediction_bilayer = claim(
    "LiF/EDAI bilayer combines field passivation from discontinuous LiF with chemical passivation "
    "from EDAI at nanoscale localized contacts, achieving optimal balance between recombination "
    "suppression and efficient charge extraction.",
    title="Bilayer theoretical prediction",
)

# Abduction pattern: two support strategies (one per hypothesis/alternative) + one compare
# Each support strategy: [hypothesis claim] → observation claim (prior=0.5)
# Compare: compares two predictions against the observation

s_bilayer = support(
    [theoretical_prediction_bilayer],
    plqy_with_complete_top_contact,
    reason="The bilayer prediction (@theoretical_prediction_bilayer) explains the observed high PLQY "
           "with complete top contacts on bilayer-treated samples.",
    prior=0.5,
)

s_lif = support(
    [theoretical_prediction_lif_only],
    plqy_with_complete_top_contact,
    reason="The LiF-only prediction (@theoretical_prediction_lif_only) explains the intermediate PLQY "
           "observed for LiF-only samples.",
    prior=0.5,
)

comp_passivation = compare(
    theoretical_prediction_bilayer,
    theoretical_prediction_lif_only,
    plqy_with_complete_top_contact,
    reason="PLQY with complete top contacts shows bilayer sample has highest PLQY among C60-coated "
           "samples, consistent with bilayer achieving best passivation. LiF alone shows intermediate "
           "PLQY. (@plqy_with_complete_top_contact)",
    prior=0.5,
)

abduction_bilayer = abduction(
    s_bilayer, s_lif, comp_passivation,
    reason="The abduction compares bilayer prediction against LiF-only prediction using PLQY data",
)

# Second abduction for Voc/FF comparison
s_bilayer_voc = support(
    [theoretical_prediction_bilayer],
    single_junction_device_results,
    reason="The bilayer prediction (@theoretical_prediction_bilayer) explains the observed high Voc "
           "and FF in single-junction devices with bilayer passivation.",
    prior=0.5,
)

s_edai = support(
    [theoretical_prediction_edai_only],
    single_junction_device_results,
    reason="The EDAI-only prediction (@theoretical_prediction_edai_only) explains the observed Voc "
           "improvement but FF reduction in EDAI-only devices.",
    prior=0.5,
)

comp_voc = compare(
    theoretical_prediction_bilayer,
    theoretical_prediction_edai_only,
    single_junction_device_results,
    reason="Single-junction Voc shows bilayer (1.27V) > EDAI (1.25V) > LiF (1.20V), while FF shows "
           "bilayer (80.8%) > EDAI (79.1%) > LiF (77.7%). This confirms bilayer outperforms both "
           "single layers in both Voc and FF. (@single_junction_device_results)",
    prior=0.5,
)

abduction_voc = abduction(
    s_bilayer_voc, s_edai, comp_voc,
    reason="The abduction compares bilayer prediction against EDAI-only prediction using Voc and FF data",
)

# =============================================================================
# Contradiction: EDAI trade-off vs bilayer simultaneous improvement
# =============================================================================

edai_ff_tradeoff = claim(
    "EDAI capping layer improves Voc but reduces FF and increases data dispersion due to "
    "passivation-transport trade-off.",
    title="EDAI passivation-transport trade-off",
)

bilayer_no_tradeoff = claim(
    "LiF/EDAI bilayer passivation improves both Voc and FF simultaneously, overcoming the "
    "passivation-transport trade-off seen with EDAI alone.",
    title="Bilayer overcomes trade-off",
)

contradiction_passivation_transport = contradiction(
    edai_ff_tradeoff,
    bilayer_no_tradeoff,
    reason="The two claims describe incompatible device behaviors: EDAI alone causes trade-off "
           "between Voc improvement and FF reduction, while bilayer achieves both improvements together.",
    prior=0.5,
)