"""
Methods module for Jeon2015 (Nature 2015).

This module covers the experimental methods and characterization techniques
used in the paper, as well as the compositional system studied.

Key content:
- Composition system: (FAPbI3)1-x(MAPbBr3)x
- Device architecture
- Synthesis procedures
- Characterization methods
"""

from gaia.lang import (
    claim,
    setting,
)

# =============================================================================
# COMPOSITION SYSTEM (SETTING)
# =============================================================================

composition_system = setting(
    "The composition system studied is (FAPbI3)1-x(MAPbBr3)x, where the mole ratio "
    "x ranges between 0 and 0.3. This mixed system combines formamidinium lead iodide "
    "with methylammonium lead bromide at the A-site (FA/MA) and X-site (I/Br) "
    "simultaneously [@Jeon2015].",
    title="Composition system (FAPbI3)1-x(MAPbBr3)x",
)

# =============================================================================
# DEVICE ARCHITECTURE (SETTING)
# =============================================================================

device_architecture = setting(
    "The standard device architecture used is: FTO/blocking-TiO2 (60-70 nm)/"
    "mesoporous-TiO2:perovskite composite layer (200 nm)/perovskite upper layer "
    "(300 nm)/PTAA (50 nm)/Au (100 nm). FTO is fluorine-doped tin oxide, and PTAA "
    "is poly(triarylamine) hole conductor. The active area of the Au electrode is "
    "fixed at 0.16 cm^2 [@Jeon2015].",
    title="Device architecture description",
)

solvent_engineering = setting(
    "The solvent engineering process uses a gamma-butyrolactone:DMSO mixed solvent "
    "with a 7:3 volume ratio. The perovskite solution is coated via two consecutive "
    "spin-coating steps at 1000 rpm and 5000 rpm for 40 s and 20 s, respectively. "
    "During the second step, 1 ml toluene is poured onto the rapidly rotating substrate "
    "to wash out surplus DMSO molecules that do not participate in the formation of "
    "the PbI2-NH2CH=NH2I-DMSO complex. This produces a uniform and flat intermediate-phase "
    "film [@Jeon2015].",
    title="Solvent engineering process",
)

annealing_conditions = setting(
    "For pure FAPbI3 (x=0), annealing is performed at 150 degrees Celsius for 10 min "
    "to form the black perovskite phase. For compositions with x greater than 0, "
    "annealing is performed at 100 degrees Celsius for 10 min to form the perovskite "
    "phase [@Jeon2015].",
    title="Annealing conditions by composition",
)

# =============================================================================
# MATERIAL SYNTHESIS (METHOD DESCRIPTION)
# =============================================================================

mai_synthesis = claim(
    "Methylammonium iodide (MAI, CH3NH3I) was synthesized by reacting 30 ml of 57% "
    "hydroiodic acid in water with 27.86 ml of 40% methylamine in methanol at 0 "
    "degrees Celsius for 2 h with stirring. The precipitate was recovered by "
    "evaporating at 50 degrees Celsius for 1 h, then dissolved in ethanol, "
    "recrystallized using diethyl ether, and finally dried at 60 degrees Celsius "
    "in a vacuum oven for 24 h [@Jeon2015].",
    title="MAI synthesis procedure",
)

fai_synthesis = claim(
    "Formamidinium iodide (FAI, NH2CH=NH2I) was synthesized similarly using formamidine "
    "acetate as the starting material. The product was recrystallized and dried under "
    "the same conditions as MAI [@Jeon2015].",
    title="FAI synthesis procedure",
)

mabr_synthesis = claim(
    "Methylammonium bromide (MABr, CH3NH3Br) was prepared using 48 wt% hydrobromic "
    "acid in water according to a reported procedure [@Jeon2015].",
    title="MABr synthesis procedure",
)

fabr_synthesis = claim(
    "Formamidinium bromide (FABr, NH2CH=NH2Br) was prepared using the same approach "
    "as MABr [@Jeon2015].",
    title="FABr synthesis procedure",
)

perovskite_solution = claim(
    "Desired solutions of FAPbI3, (FAPbI3)1-x(MAPbI3)x, (FAPbI3)1-x(FAPbBr3)x, and "
    "(FAPbI3)1-x(MAPbBr3)x (with x = 0-0.30) were prepared by dissolving the "
    "respective halide salts (MAI, FAI, MABr, FABr) with PbI2 and PbBr2 in the "
    "gamma-butyrolactone:DMSO mixed solvent (7:3 volume ratio) at 60 degrees Celsius "
    "for 10 min [@Jeon2015].",
    title="Perovskite solution preparation",
)

# =============================================================================
# TIO2 PREPARATION (METHOD)
# =============================================================================

tio2_nanoparticles = claim(
    "TiO2 nanoparticles with average diameter of 50 nm (anatase) were prepared by "
    "hydrothermal treatment at 250 degrees Celsius for 12 h from aqueous solutions of "
    "the peroxotitanium complex. The peroxotitanium complex was synthesized via "
    "reaction between hydrogen peroxide and TiO(OH)2 wet cake obtained from hydrolysis "
    "of TiCl4 [@Jeon2015].",
    title="TiO2 nanoparticle synthesis",
)

tio2_paste = claim(
    "The TiO2 paste was prepared by dispersing TiO2 nanoparticles in absolute ethanol "
    "with 10 wt% ethanolic solution of ethyl cellulose (4.5 g per 1 g TiO2) and "
    "terpineol (4.4 g per 1 g TiO2). The mixture was homogenized by ultrasonic "
    "irradiation, then concentrated in a rotary evaporator and processed through a "
    "three-roller mill grinder [@Jeon2015].",
    title="TiO2 paste preparation",
)

blocking_layer = claim(
    "A dense blocking layer of TiO2 (60 nm) was deposited onto the FTO substrate "
    "by spray pyrolysis using a 20 mM titanium diisopropoxide bis(acetylacetonate) "
    "solution at 450 degrees Celsius. This prevents direct contact between FTO and "
    "the hole-conducting layer [@Jeon2015].",
    title="TiO2 blocking layer deposition",
)

mesoporous_layer = claim(
    "A 200-nm-thick mesoporous-TiO2 layer was spin-coated onto the blocking-TiO2/FTO "
    "substrate using TiO2 paste diluted in 2-methoxyethanol (1 g in 5 ml), then "
    "calcined at 500 degrees Celsius for 1 h in air to remove organic components "
    "[@Jeon2015].",
    title="Mesoporous TiO2 layer preparation",
)

# =============================================================================
# HTL DEPOSITION (METHOD)
# =============================================================================

ptaa_deposition = claim(
    "A solution of PTAA (number-average molecular weight Mn = 17,500 g/mol) in "
    "toluene (10 mg/ml) with additives of 7.5 microliters Li-bis(trifluoromethanesulphonyl) "
    "imide/acetonitrile (170 mg/ml) and 4 microliters 4-tert-butylpyridine was "
    "spin-coated on the perovskite layer at 3000 rpm for 30 s [@Jeon2015].",
    title="PTAA hole transport layer deposition",
)

au_electrode = claim(
    "An Au counter electrode was deposited by thermal evaporation. The active area "
    "of this electrode was fixed at 0.16 cm^2 [@Jeon2015].",
    title="Au electrode evaporation",
)

# =============================================================================
# CHARACTERIZATION METHODS (SETTING)
# =============================================================================

xrd_method = setting(
    "XRD spectra of prepared films were measured using a Rigaku SmartLab X-ray "
    "diffractometer with Cu K-alpha radiation (wavelength lambda = 1.5406 Angstrom). "
    "In situ XRD experiments on FAPbI3 yellow powder were performed using a Rigaku "
    "Ultima IV with the same X-ray source [@Jeon2015].",
    title="X-ray diffraction characterization method",
)

uvvis_method = setting(
    "Ultraviolet-visible absorption spectra were recorded on a Shimadzu UV 2550 "
    "spectrophotometer in the 300-800 nm wavelength range at room temperature "
    "[@Jeon2015].",
    title="UV-vis absorption characterization method",
)

sem_method = setting(
    "The morphology of the films was observed using a field-emission SEM "
    "(MIRA3 LMU, Tescan) [@Jeon2015].",
    title="Scanning electron microscopy method",
)

dsc_tga_method = setting(
    "Thermogravimetric and DSC analyses of as-prepared powders were performed with "
    "a heating rate of 2 degrees Celsius per minute from room temperature up to "
    "300 degrees Celsius under nitrogen atmosphere using TA Instruments SDT 2960 "
    "and DSC 2910, respectively [@Jeon2015].",
    title="DSC and TGA characterization method",
)

eqe_method = setting(
    "EQE was measured using a power source (Newport 300W Xenon lamp, 66920) with a "
    "monochromator (Newport Cornerstone 260) and a multimeter (Keithley 2001) "
    "[@Jeon2015].",
    title="External quantum efficiency measurement method",
)

jv_measurement = setting(
    "J-V curves were measured using a solar simulator (Newport, Oriel Class A, 91195A) "
    "with a source meter (Keithley 2420) at 100 mA/cm^2 AM1.5G illumination and a "
    "calibrated Si-reference cell certified by the National Renewable Energy Laboratory, "
    "USA. J-V curves were measured by reverse scan (forward bias 1.2 V to short "
    "circuit 0 V) or forward scan (short circuit 0 V to forward bias 1.2 V). The step "
    "voltage was fixed at 10 mV and the delay time was modulated. J-V curves for all "
    "devices were measured by masking the active area with a metal mask (area 0.096 cm^2) "
    "[@Jeon2015].",
    title="J-V measurement conditions",
)

__all__ = [
    "composition_system",
    "device_architecture",
    "solvent_engineering",
    "annealing_conditions",
    "mai_synthesis",
    "fai_synthesis",
    "mabr_synthesis",
    "fabr_synthesis",
    "perovskite_solution",
    "tio2_nanoparticles",
    "tio2_paste",
    "blocking_layer",
    "mesoporous_layer",
    "ptaa_deposition",
    "au_electrode",
    "xrd_method",
    "uvvis_method",
    "sem_method",
    "dsc_tga_method",
    "eqe_method",
    "jv_measurement",
]