"""
Results module for Liu et al. 2013 Nature paper.

Paper: Efficient planar heterojunction perovskite solar cells by vapour deposition
Citation: [@Liu2013]

This module covers the results sections: structural characterization, morphology, and device performance.
"""

from gaia.lang import (
    claim,
    setting,
    support,
    infer,
)

# X-ray diffraction characterization
xrd_peak_positions = claim(
    "X-ray diffraction spectra of both vapour-deposited and solution-processed CH3NH3PbI3-xClx films show identical "
    "main diffraction peaks at 14.12° (110), 28.44° (220), and 43.23° (330), indicating both techniques produce "
    "the same mixed-halide perovskite with orthorhombic crystal structure [@Liu2013].",
    title="XRD peak positions for perovskite films",
)

xrd_phase_purity = claim(
    "The (110) diffraction peak region at 14.12° shows only a small signature of a peak at 12.65° (the (001) diffraction "
    "peak for PbI2) and no measurable peak at 15.68° (the (110) diffraction peak for CH3NH3PbCl3), indicating a high "
    "level of phase purity in the mixed-halide perovskite films [@Liu2013].",
    title="High phase purity from XRD analysis",
)

xrd_c_axis_contraction = claim(
    "The mixed-halide perovskite shows a slight contraction of the c axis compared to CH3NH3PbI3, consistent with Cl "
    "atoms residing in apical positions out of the PbI4 plane rather than in equatorial octahedral sites, as theoretically "
    "predicted [@Liu2013].",
    title="c-axis contraction indicates Cl positioning",
)

# Crystal structure description
crystal_structure_description = claim(
    "The perovskite absorber adopts the ABX3 form where A is methylammonium (CH3NH3+), B is lead (Pb2+), and X is iodine "
    "or chlorine (I- or Cl-), with the crystal structure being orthorhombic as determined by XRD analysis [@Liu2013].",
    title="Perovskite ABX3 crystal structure",
)

# SEM top-view imaging
vapour_deposited_morphology = claim(
    "Vapour-deposited perovskite films are extremely uniform with crystalline features on the length scale of hundreds "
    "of nanometres, as observed in top-view SEM images [@Liu2013].",
    title="Vapour-deposited film morphology - uniform",
)

solution_processed_morphology = claim(
    "Solution-processed perovskite films appear to coat the substrate only partially, with crystalline 'platelets' on "
    "the length scale of tens of micrometres, and voids between crystals extending directly to the compact TiO2-coated "
    "FTO-coated glass substrate [@Liu2013].",
    title="Solution-processed film morphology - incomplete coverage",
)

# Cross-sectional SEM imaging
vapour_deposited_cross_section = claim(
    "The cross-sectional SEM image of vapour-deposited perovskite film shows a uniform layer similar in appearance to "
    "the FTO layer, albeit with slightly larger crystal features, with average film thickness of approximately 330 nm [@Liu2013].",
    title="Vapour-deposited film cross-section - uniform 330 nm",
)

solution_processed_cross_section = claim(
    "The cross-sectional SEM image of solution-processed perovskite film appears extremely smooth in the SEM image, "
    "consistent with much larger crystal grain size than the field of view, with undulating nature and thickness varying "
    "from 50 to 410 nm, and areas where perovskite is completely absent (0 to 465 nm variation observed) [@Liu2013].",
    title="Solution-processed film cross-section - undulating with pinholes",
)

# Crystal size estimation
crystal_size_limited = claim(
    "Crystal sizes for both films are larger than can be determined from the peak width of X-ray diffraction spectra "
    "(about 400 nm) due to machine broadening, indicating grains at least 400 nm in size [@Liu2013].",
    title="Crystal size estimation from XRD peak width",
)

# Best-performing device metrics - vapour deposited
vapour_best_Jsc = claim(
    "The best-performing vapour-deposited perovskite device achieved a short-circuit photocurrent (Jsc) of 21.5 mA cm^-2 [@Liu2013].",
    title="Vapour-deposited best device Jsc",
)

vapour_best_Voc = claim(
    "The best-performing vapour-deposited perovskite device achieved an open-circuit voltage (Voc) of 1.07 V [@Liu2013].",
    title="Vapour-deposited best device Voc",
)

vapour_best_FF = claim(
    "The best-performing vapour-deposited perovskite device achieved a fill factor (FF) of 0.68 [@Liu2013].",
    title="Vapour-deposited best device fill factor",
)

vapour_best_PCE = claim(
    "The best-performing vapour-deposited perovskite device achieved a power conversion efficiency (PCE) of 15.4% under "
    "simulated AM1.5 sunlight at 101 mW cm^-2 irradiance [@Liu2013].",
    title="Vapour-deposited best device efficiency - 15.4%",
)

# Best-performing device metrics - solution processed
solution_best_Jsc = claim(
    "The best-performing solution-processed planar heterojunction perovskite solar cell produced a short-circuit photocurrent "
    "of 17.6 mA cm^-2 [@Liu2013].",
    title="Solution-processed best device Jsc",
)

solution_best_Voc = claim(
    "The best-performing solution-processed planar heterojunction perovskite solar cell produced an open-circuit voltage "
    "of 0.84 V [@Liu2013].",
    title="Solution-processed best device Voc",
)

solution_best_FF = claim(
    "The best-performing solution-processed planar heterojunction perovskite solar cell produced a fill factor of 0.58 [@Liu2013].",
    title="Solution-processed best device fill factor",
)

solution_best_PCE = claim(
    "The best-performing solution-processed planar heterojunction perovskite solar cell produced an overall efficiency of 8.6% [@Liu2013].",
    title="Solution-processed best device efficiency - 8.6%",
)

# Statistical data for vapour-deposited batch
vapour_batch_Jsc_avg = claim(
    "A batch of 12 identically processed vapour-deposited perovskite solar cells showed an average short-circuit photocurrent "
    "of 18.9 ± 1.8 mA cm^-2 [@Liu2013].",
    title="Vapour-deposited batch average Jsc",
)

vapour_batch_Voc_avg = claim(
    "A batch of 12 identically processed vapour-deposited perovskite solar cells showed an average open-circuit voltage "
    "of 1.05 ± 0.03 V [@Liu2013].",
    title="Vapour-deposited batch average Voc",
)

vapour_batch_FF_avg = claim(
    "A batch of 12 identically processed vapour-deposited perovskite solar cells showed an average fill factor "
    "of 0.62 ± 0.05 [@Liu2013].",
    title="Vapour-deposited batch average FF",
)

vapour_batch_PCE_avg = claim(
    "A batch of 12 identically processed vapour-deposited perovskite solar cells showed an average power conversion "
    "efficiency of 12.3 ± 2.0% [@Liu2013].",
    title="Vapour-deposited batch average PCE",
)

# Diffusion length implication
diffusion_length_lower_bound = claim(
    "The vapour-deposited film thickness of 330 nm sets a lower limit on the electron and hole diffusion length in this "
    "perovskite absorber, since charges must be collected at the p-type and n-type heterojunctions [@Liu2013].",
    title="Diffusion length lower bound - 330 nm",
)

# Film uniformity advantage
uniformity_advantage = claim(
    "Dual-source vapour deposition results in superior uniformity of the coated perovskite films over a range of length "
    "scales, which subsequently results in substantially improved solar cell performance compared to solution processing [@Liu2013].",
    title="Vapour deposition uniformity advantage for performance",
)

# Pinhole problem in solution processing
pinhole_shunting = claim(
    "The complete absence of material (pinholes) in some regions of solution-processed films results in direct contact of "
    "p-type spiro-OMeTAD and n-type TiO2 compact layer, creating a shunting path that contributes to lower fill factor "
    "and open-circuit voltage in solution-cast planar heterojunction devices [@Liu2013].",
    title="Solution-processed pinholes cause shunting",
)

# Surprising efficiency despite inhomogeneity
solution_efficiency_surprise = claim(
    "It is remarkable that such inhomogeneous and undulating solution-cast films can deliver devices with over 8% efficiency, "
    "demonstrating the capability of the perovskite absorber material itself [@Liu2013].",
    title="Solution-processed efficiency despite inhomogeneity",
)