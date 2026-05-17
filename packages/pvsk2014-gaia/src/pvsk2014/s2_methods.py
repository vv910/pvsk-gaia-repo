"""
Section 2 (Methods) formalization covering:
- Device architecture and fabrication
- Solvent engineering procedure
- Intermediate phase formation mechanism
- Characterization methods
"""

from gaia.lang import (
    claim,
    setting,
)

# --- Device architecture ---

device_architecture = setting(
    "The bilayered perovskite solar cell architecture is glass/FTO/bl-TiO2/mp-TiO2-perovskite nanocomposite layer/perovskite upper layer/PTAA/Au [@Jeon2014]."
)

blocking_layer_spec = setting(
    "A dense blocking layer of TiO2 (bl-TiO2, approximately 70 nm thickness) was deposited onto F-doped SnO2 (FTO) substrate by spray pyrolysis using 20 mM titanium diisopropoxide bis(acetylacetonate) solution at 450 degrees C to prevent direct contact between FTO and hole-conducting layer [@Jeon2014]."
)

mesoporous_layer_spec = setting(
    "A 200-300 nm thick mesoporous TiO2 film (particle size approximately 50 nm, anatase crystalline phase) was spin-coated onto bl-TiO2/FTO substrate using home-made pastes and calcined at 500 degrees C for 1 hour in air [@Jeon2014]."
)

perovskite_upper_layer_thickness = setting(
    "The highly uniform perovskite active layer atop the mp-TiO2 is 100-300 nm thick [@Jeon2014]."
)

hole_transporting_layer = setting(
    "Poly(triarylamine) (PTAA) was used as the hole-transporting material, deposited by spin-coating from a solution in toluene with lithium bistrifluoromethanesulphonimidate and 4-tert-butylpyridine additives [@Jeon2014]."
)

gold_counterelectrode = setting(
    "Au metal was deposited by thermal evaporation as the counterelectrode [@Jeon2014]."
)

active_area = setting(
    "The active area of the electrode was fixed at 0.16 cm^2 [@Jeon2014]."
)

# --- Solvent engineering process ---

solvent_engineering_process = claim(
    "The solvent-engineering process involves five stages: (1) spreading a mixture of MAI, MABr, PbI2, PbBr2, GBL and DMSO in appropriate ratio over the substrate; (2) spin-coating at 1,000 and 5,000 rpm for 10 and 20 seconds to evaporate solvent; (3) dripping toluene (non-dissolving solvent miscible with DMSO and GBL) onto the substrate during spinning; (4) freezing all constituents into a uniform layer on removal of residual DMSO and forming a new intermediate phase; (5) converting the complex into highly uniform and crystalline perovskite on annealing at 100 degrees C for 10 minutes [@Jeon2014].",
    title="Solvent engineering process stages"
)

pure_gbl_outcome = claim(
    "In pure GBL solvent, perovskite crystals form immediately during rotation at 5,000 rpm regardless of toluene drip application, resulting in inhomogeneous islands with low substrate coverage [@Jeon2014].",
    title="Pure GBL produces inhomogeneous perovskite morphology"
)

mixed_solvent_outcome = claim(
    "In DMSO and GBL mixed solvent with toluene drip, the spin-coated layer is extremely uniform and transparent, covers the full surface with low surface roughness, and perovskite crystals do not form during spinning even after 5 minutes [@Jeon2014].",
    title="Mixed solvent with toluene drip yields uniform perovskite morphology"
)

without_toluene_outcome = claim(
    "Without toluene drip treatment, the resulting material adopts a textile-like inhomogeneous layer that does not fully cover the substrate, and perovskite crystals form from the coating only after annealing at 100 degrees C [@Jeon2014].",
    title="Without toluene drip: inhomogeneous textile-like morphology"
)

crystallinity_preserved = claim(
    "The crystallinity of the perovskite films is almost the same regardless of the toluene drop-casting, as indicated by full-width at half-maximum values of (110) XRD peaks [@Jeon2014].",
    title="Crystallinity preserved with or without toluene drip"
)

# --- Intermediate phase ---

intermediate_phase_formation = claim(
    "The intermediate phase MAI-PbI2-DMSO is formed when toluene is introduced onto the wet film comprising PbI2, MAI and DMSO, creating a flat intermediate phase film via intercalation of MAI and DMSO guest molecules between PbI2 layers [@Jeon2014].",
    title="Intermediate phase formation mechanism"
)

dmso_retards_reaction = claim(
    "DMSO in the MAI-PbI2-DMSO phase retards the rapid reaction between PbI2 and MAI during solvent evaporation in the spin-coating process, enabling the formation of a highly uniform and dense surface [@Jeon2014].",
    title="DMSO retards rapid reaction between PbI2 and MAI"
)

intermediate_phase_identity = claim(
    "The intermediate phase isolated by pouring MAI and PbI2 dissolved in GBL and DMSO into toluene is a new and unreported crystalline compound, different from PbI2, MAI, and PbI2(DMSO)2, with composition consistent with MAI-PbI2-DMSO by elemental analysis [@Jeon2014].",
    title="Intermediate phase is new MAI-PbI2-DMSO compound"
)

elemental_analysis_confirms = claim(
    "Elemental analysis of the intermediate phase yielded weight percentages of H=1.6%, C=4.6%, N=2.0%, O=2.2%, S=3.7%, with remainder 85.9% assumed to be Pb and I (30% and 55.9%), in agreement with the MAI-PbI2-DMSO formula (C3H12NSOPbI3) [@Jeon2014].",
    title="Elemental analysis confirms intermediate phase composition"
)

low_angle_xrd_peaks = claim(
    "XRD peaks at low angles (6.55 degrees, 7.21 degrees, 9.17 degrees) indicate that the MAI-PbI2-DMSO intermediate phase has longer interplanar distances than the DMSO-PbI2-DMSO complex due to substitution of MAI for DMSO [@Jeon2014].",
    title="Low-angle XRD peaks confirm intercalation structure"
)

ftir_confirmation = claim(
    "FTIR spectrum of the intermediate phase shows S-O and C-S stretching vibrations from DMSO coordinated to Pb2+ at 1,012 cm^-1, N-H stretching in the range 3,200-3,450 cm^-1, and C-H stretching in the range 2,800-2,950 cm^-1, confirming successful inclusion of DMSO and MAI into PbI2 [@Jeon2014].",
    title="FTIR confirms DMSO and MAI inclusion in intermediate phase"
)

perovskite_conversion_temperature = claim(
    "In situ high-temperature XRD shows that the MAI-PbI2-DMSO intermediate phase completely transforms to MAPbI3 perovskite at 130 degrees C, while both phases coexist at 100 degrees C [@Jeon2014].",
    title="Perovskite conversion complete at 130 degrees C"
)

# --- Morphology characterization ---

intermediate_phase_rms_roughness = claim(
    "Atomic force microscopy measurements show root mean square roughness of 6.0 nm for the intermediate phase film on fused silica substrate [@Jeon2014].",
    title="Intermediate phase RMS roughness is 6.0 nm"
)

perovskite_film_rms_roughness = claim(
    "Atomic force microscopy measurements show root mean square roughness of 8.3 nm for the resulting crystalline perovskite layer on fused silica substrate [@Jeon2014].",
    title="Perovskite film RMS roughness is 8.3 nm"
)

dense_grained_morphology = claim(
    "The perovskite surface exhibits a dense-grained uniform morphology with grain sizes in the range 100-500 nm, and the entire film is composed of a homogeneous, well-crystallized perovskite layer [@Jeon2014].",
    title="Dense-grained uniform morphology with 100-500 nm grains"
)

full_surface_coverage = claim(
    "The perovskite materials fully infiltrate the pores of the mp-TiO2 film and are deposited in a very uniform thick film with 100% surface coverage atop the mp-TiO2, compared with the conventional method [@Jeon2014].",
    title="Full surface coverage achieved with solvent engineering"
)

# --- Characterization methods ---

xrd_method = setting(
    "XRD spectra were measured using a Rigaku SmartLab X-ray diffractometer; in situ XRD experiments used a Rigaku Ultima IV with Cu Kalpha radiation (lambda = 1.5406 angstrom) [@Jeon2014]."
)

ftir_method = setting(
    "FTIR spectra (4,000-500 cm^-1) were recorded on a Bruker EQUINOX 55 spectrophotometer using KBr pellet sample preparation [@Jeon2014]."
)

uv_vis_method = setting(
    "Ultraviolet-visible absorption spectra were recorded on a Shimadzu UV 2550 spectrophotometer in the 200-800 nm wavelength range at room temperature [@Jeon2014]."
)

afm_method = setting(
    "AFM was performed using Bruker Multimode 8 in tapping mode [@Jeon2014]."
)

ipce_method = setting(
    "IPCE was measured using a Newport 300 W xenon lamp (66920) with a monochromator (Newport Cornerstone 260) and a multimeter (Keithley 2001) [@Jeon2014]."
)

jv_measurement_method = setting(
    "J-V curves were measured using a Newport solar simulator (Oriel Class A, 91195A) with a Keithley 2420 source meter at 100 mW cm^-2, AM 1.5 G illumination, and a calibrated Si-reference cell certified by NREL; reverse scan was from forward bias (1.2 V) to short circuit (0 V); forward scan was from short circuit (0 V) to forward bias (1.2 V); step voltage was 10 mV with modulated delay time [@Jeon2014]."
)

elemental_analysis_method = setting(
    "Elemental analysis (C, H, N and S) was performed using a FISONS EA-1108 CHN analyser [@Jeon2014]."
)