"""
s3_results.py - Experimental results on phase separation and suppression.

This module covers results from Section "Phase separation and suppression in 2D perovskites":
- PL characterization showing phase separation in long-chain ligands
- DFT calculations on formation enthalpies
- Triple-halide approach to eliminate phase separation
"""

from gaia.lang import claim, setting

# Phase separation observation in long-chain ligands
phase_separation_pl = claim(
    "In PL spectra, splitting of emission peak around 500 nm (n=1 phase) occurs only "
    "in long-chain n-dodecylammonium iodide (DAI), n-dodecylammonium chloride (DACl) "
    "and hexadecylammonium iodide (HDAI) samples. This demonstrates that carbon-chain "
    "length determines phase separation in 2D perovskites [@Li2024].",
    title="PL shows phase separation in long-chain ligand samples",
    figure="artifacts/images/fig1.png",
)

# DAX halide series PL results
dax_halide_pl = claim(
    "For DAX (X = I, Br, Cl) post-treated films: PL splitting of n=1 perovskite only "
    "appears in DAI and DACl samples, while DABr sample shows stable single n=1 peak. "
    "This indicates that halide composition significantly affects phase stability [@Li2024].",
    title="DAI and DACl show phase separation, DABr does not",
)

# MACl residues persist on perovskite surface
macl_residues = claim(
    "X-ray photoelectron spectroscopy reveals surface Cl residues persist even after "
    "prolonged annealing at 100 C for 3 hours. MACl at 30-40% molar ratio to FAPbI is "
    "typically introduced to improve FA-dominated perovskite film quality [@Li2024].",
    title="MACl residues persist on perovskite surface after annealing",
)

# MACl-free perovskite tests
macl_free_tests = claim(
    "Post-treatment of MACl-free pure I-based perovskites shows distinct I- or Br-rich "
    "phase separation in DABr post-treated samples, and I- or Cl-rich phase separation "
    "in DACl post-treated samples. Only DAI post-treatment yields single n=120 phase "
    "on MACl-free pure I-based perovskite surface. Mixed DABr/DACl also yields single "
    "n=120 phase [@Li2024].",
    title="MACl-free perovskite shows halide-dependent phase separation",
)

# Double-halide alloy phase separation
double_halide_phase_sep = claim(
    "Phase separation easily forms in double-halide-alloyed n=120 perovskites but can "
    "be mitigated in triple-halide alloys. This is confirmed by post-treatment of typical "
    "I-Br alloyed perovskites with different halide 2D salts [@Li2024].",
    title="Double-halide alloys show phase separation",
)

# DFT formation enthalpy results - single halide
dft_formation_enthalpy_single = claim(
    "DFT calculations show that formation enthalpy (Ef) of single halide 2D perovskites "
    "varies with halide composition. For DA2PbI4 (n=1), Ef is positive indicating "
    "thermodynamic favorability of phase formation [@Li2024].",
    title="DFT formation enthalpy for single halide 2D perovskites",
)

# DFT formation enthalpy - double halide
dft_formation_enthalpy_double = claim(
    "DFT calculations reveal pronounced increase in formation enthalpy (Ef) and mixing "
    "enthalpy of double-halide alloys (e.g., DA2PbI4-xClx). This explains why double-halide "
    "2D perovskites exhibit phase separation [@Li2024].",
    title="Double-halide alloys have increased formation enthalpy",
)

# DFT formation enthalpy - triple halide
dft_formation_enthalpy_triple = claim(
    "DFT calculations show obvious decrease in formation enthalpy of triple-halide alloys "
    "(e.g., DA2FA2Pb3(I4-0.5xClx)Br4). Introduction of Br significantly reduces formation "
    "enthalpy of self-assembled n=1 Cl-alloyed 2D perovskites, effectively inhibiting "
    "I-Cl phase separation [@Li2024].",
    title="Triple-halide alloys have decreased formation enthalpy",
)

# Triple-halide eliminates phase separation
triple_halide_eliminates_phase_sep = claim(
    "Triple-halide composition successfully eliminates problematic phase separation "
    "observed in double-halide alloys, enabling formation of stable single-phase "
    "2D perovskite structures [@Li2024].",
    title="Triple-halide composition eliminates phase separation",
)

# n-value challenge remains
n_value_challenge = claim(
    "Although halide phase separation in double-halide compositions can be avoided by "
    "triple-halide construction, multiple different n-value structures still form. "
    "High n-value 2D perovskites with higher charge carrier mobility are more favorable "
    "for 3D/2D stacking because insulating n=1 2D perovskite may hinder interfacial "
    "charge transport [@Li2024].",
    title="Multiple n-value structures form despite halide engineering",
)

# FABr enables uniform n=2 formation
fabr_enables_uniform_n2 = claim(
    "Combined use of DAX and FABr leads to growth of uniform n=2 2D structures without "
    "phase separation on 3D perovskite. The lower formation enthalpy of triple-halide "
    "n=2 DA2FAPb2(I4-0.5xClx)Br3 perovskites compared to n=1 and n=3 enables preferential "
    "formation of phase-pure n=2 perovskite [@Li2024].",
    title="FABr enables uniform phase-pure n=2 2D formation",
)

# Universality of FABr approach
universality_fabr = claim(
    "Post-treatment strategy with FABr successfully extends to most conventional 2D ligands "
    "for suppressing unfavorable phase separation and stabilizing pure 2D phases. "
    "This confirms the universality of the FABr approach for homogeneous 2D formation [@Li2024].",
    title="FABr approach is universal across 2D ligands",
)

# In situ PL kinetics - DABr formation
insitu_pl_dabr = claim(
    "In situ PL during spin coating shows n=2 20 phase appears at ~550 nm at ~40 s, "
    "earlier than n=1 2D phase (~54 s), suggesting formation of n=2 phase is preferred "
    "to n=1 phase. Pure IPA solvent control shows variation in emission peak intensity "
    "around 800 nm due to solvent-induced dissolution and recrystallization within "
    "3D perovskite [@Li2024].",
    title="In situ PL shows n=2 forms before n=1",
)

# In situ PL kinetics - FABr/DABr
insitu_pl_fabr_dabr = claim(
    "Mixed FABr/DABr post-treatment enables fast appearance of strong, broad emission "
    "from single n=2 20 perovskite at ~33 s, markedly faster than DABr-treated (~40 s "
    "for n=2), indicating FABr facilitates homogeneous n=2 2D perovskite formation "
    "even at room temperature. This is consistent with DFT calculations showing "
    "lower formation enthalpy for triple-halide n=2 phases [@Li2024].",
    title="FABr accelerates homogeneous n=2 formation",
)

# PL intensity regimes
pl_intensity_regimes = claim(
    "According to intensity evolution of 3D phase, two main regimes can be distinguished "
    "before and after IPA solvent volatilization: Stage I (20 to ~31 s) shows negligible "
    "PL variation after FABr post-treatment compared to control, indicating FABr fills "
    "ion vacancy from IPA dissolution. Stage II (~31 to ~120 s) shows sharp intensity drop "
    "due to reaction between FABr and residual PbI2, forming uniform crystalline "
    "FAPbI3-xBrx layer covering 3D perovskite [@Li2024].",
    title="Two-stage PL intensity evolution during spin coating",
)

# DABr signal breakage observation
dabr_signal_breakage = claim(
    "During Stage I, obvious signal breakage occurs in both DABr and DABr/FABr cases. "
    "This missing emission before 2D phase formation may be caused by introduced DABr "
    "organic salts obstruction. In contrast, no substantial intensity drop during Stage II "
    "for single DABr post-treatment indicates uneven coverage of formed inhomogeneous "
    "2D perovskites [@Li2024].",
    title="Signal breakage indicates inhomogeneous 2D formation",
)

# GIWAXS results after annealing
giwaxs_results = claim(
    "After annealing (100 C for 5 min, cooled to room temperature), GIWAXS confirms "
    "remained 2D structures on 3D perovskite surface. Pristine sample shows isotropic "
    "diffraction ring at q ~ 1.0 A^-1 of 3D perovskite phase and faint residual PbI2 "
    "diffraction arc at q ~ 0.9 A^-1. PbI2 signal vanishes after FABr treatment, "
    "implying FABr preferentially reacts with PbI2 [@Li2024].",
    title="GIWAXS confirms 2D structure and PbI2 reaction",
)

# DABr post-treated GIWAXS
dabr_giwaxs = claim(
    "In DABr post-treated sample, multiple out-of-plane scattering peaks visible: "
    "n=1 at q=0.25, 0.51, 0.77 A^-1 and n=2 at q=0.21, 0.41, 0.62, 0.83 A^-1. "
    "These structures coexist, confirming mixed n=1 and n=2 phases [@Li2024].",
    title="DABr forms mixed n=1 and n=2 phases",
)

# DABr/FABr post-treated GIWAXS
fabr_dabr_giwaxs = claim(
    "In DABr/FABr post-treated sample, only uniform n=2 20 structure exists (q values: "
    "0.21, 0.41, 0.62, 0.83 A^-1). Confocal PL mappings verify more uniform PL emissions "
    "of 2D signals in DABr/FABr post-treated perovskite compared to DABr post-treated, "
    "indicating homogeneous formation of 2D capping layers over large areas [@Li2024].",
    title="DABr/FABr forms pure phase-pure n=2",
)

# Formation mechanism schematic
formation_mechanism = claim(
    "Beginning with defect-rich 3D perovskite surface, DABr post-treatment leads to "
    "corner-sharing 2D octahedral layers with mixed phases (n=1 and n=2), predominantly "
    "due to incomplete reaction between PbI2 and 2D cation ligands hindering further "
    "diffusion of DA cations. FABr incorporation into DABr breaks up big PbX2 fragments "
    "and strengthens reaction between PbX2 and 2D ligands, while also passivating FA "
    "vacancy generated by IPA dissolution, generating high-quality uniformly distributed "
    "phase-pure n=2 20 structure on top of 3D perovskites [@Li2024].",
    title="Formation mechanism of homogeneous n=2 2D perovskite",
)

# Defect elimination by phase-pure 2D
defect_elimination = claim(
    "With phase-pure n=2 20 structure, intrinsic defects on 3D perovskite surface are "
    "substantially eliminated. The homogeneous morphology and phase-pure composition "
    "contribute to reduced interface charge recombination and improved carrier transport [@Li2024].",
    title="Phase-pure 2D eliminates surface defects",
)