"""
Structural and Optoelectronic Characterization Results.

This module covers the results from structural and optical characterization
(Figures 1-3 in the paper, lines 32-52 and 53-68).
"""

from gaia.lang import claim

# 2D Perovskite Characterization Results
two_d_absorption = claim(
    "The (HOOC(CH2)4NH3)2PbI4 2D perovskite shows absorption band edge at 450 nm "
    "with excitonic peak at 425 nm, and PL emission at 453 nm [@Grancini2017].",
    title="2D perovskite optical properties",
    metadata={"figure": "artifacts/images/*.jpg", "caption": "Fig. 1a | Absorption edge at 450 nm, excitonic peak at 425 nm"},
)

two_d_raman_modes = claim(
    "Raman spectra for 100% AVAI shows peaks at 87, 112, and 169 cm-1 (Pb-I stretching/bending) "
    "and 62, 143 cm-1 (organic cation rotation/libration), similar to PbI2 intercalated with ammonia. "
    "Sharp peaks in 50-200 cm-1 range indicate well-defined crystalline structure [@Grancini2017].",
    title="2D perovskite Raman signature",
    metadata={"figure": "artifacts/images/*.jpg", "caption": "Fig. 1b | Sharp Raman peaks at specific wavenumbers"},
)

two_d_xrd_pattern = claim(
    "X-ray diffraction of 100% AVAI shows rich pattern at low angles with dominant peak at 4.7 degrees "
    "and lateral peaks at 4.2 and 5.2 degrees, evidence of low-dimensional perovskite with complex "
    "crystal structure and multiple reflections at 2θ<10 degrees [@Grancini2017].",
    title="2D perovskite XRD low-angle pattern",
    metadata={"figure": "artifacts/images/*.jpg", "caption": "Fig. 1c | Low-angle diffraction peaks"},
)

# 2D/3D Composite Characterization Results
two_d_three_d_absorption = claim(
    "2D/3D films with 3% AVAI absorb across the whole visible region with edge at 760 nm and "
    "a peak at 430 nm. The peak at 430 nm linearly increases with AVAI percentage, resembling "
    "2D perovskite absorption (partially red-shifted), while the 760 nm edge matches 3D perovskite [@Grancini2017].",
    title="2D/3D composite absorption characteristics",
    metadata={"figure": "artifacts/images/*.jpg", "caption": "Fig. 1a | Visible absorption with dual features"},
)

two_d_three_d_raman = claim(
    "The 3% AVAI 2D/3D composite shows well-defined Raman lines matching 2D peaks, emerging from "
    "a broader band characteristic of 3D CH3NH3PbI3 inorganic lattice modes. The sharp features "
    "with reduced broadening suggest more ordered crystal rearrangement compared to pure 3D phase [@Grancini2017].",
    title="2D/3D Raman shows ordered phase",
    metadata={"figure": "artifacts/images/*.jpg", "caption": "Fig. 1b | Sharp 2D-like Raman features in 3% AVAI"},
)

two_d_three_d_xrd = claim(
    "2D/3D XRD shows prominent (110) peak at 14.13 degrees related to CH3NH3PbI3 tetragonal phase. "
    "With 3% AVAI, (002) and (004) peaks decrease while (110) and (220) reflections increase, "
    "indicating preferred orientation along <hk0> direction. No clear 2D phase peaks appear "
    "at 3% AVAI but appear at >10% AVAI [@Grancini2017].",
    title="2D/3D preferred orientation growth",
    metadata={"figure": "artifacts/images/*.jpg", "caption": "Fig. 1d | Peak intensity changes with 3% AVAI"},
)

phase_structure_conclusion = claim(
    "The 2D/3D perovskite film with 3% AVAI consists of: (1) thin 2D perovskite layer (possibly monolayer) "
    "anchored at the oxide interface via carboxylic acid group, (2) oriented 3D phase with marked "
    "preferential growth direction at the interface, and (3) pure 3D tetragonal perovskite on top [@Grancini2017].",
    title="2D/3D graded multi-phase structure",
)

# Photoluminescence Results
pl_oxide_side = claim(
    "PL measured from oxide side (excited at 400 nm) reveals weak emission around 450 nm matching "
    "(HOOC(CH2)4NH3)2PbI4, suggesting 2D phase mostly retained at oxide interface due to favorable "
    "anchoring of AVAI carboxylic acid group to TiO2 scaffold [@Grancini2017].",
    title="2D phase retained at oxide interface",
    metadata={"figure": "artifacts/images/*.jpg", "caption": "Fig. 2a | 450 nm emission from oxide side"},
)

pl_phase_separation = claim(
    "Extended spectral window shows: excitation from bulk top layer yields single PL peak at 760 nm "
    "(standard 3D), while excitation from oxide side yields peak at 730 nm (larger bandgap 1.69 eV) "
    "with shoulder at 760 nm. The 730 nm emission indicates different perovskite phase formed "
    "within oxide scaffold, only in presence of AVAI precursor [@Grancini2017].",
    title="Blue-shifted PL reveals distinct interface phase",
    metadata={"figure": "artifacts/images/*.jpg", "caption": "Fig. 2b | 730 nm peak from oxide side excitation"},
)

pl_730nm_fast_decay = claim(
    "PL dynamics at 730 nm shows fast decay with time constant τ=2 ns (dominating), while 760 nm "
    "shows long-lived decay extending beyond temporal window (band-edge recombination). This faster "
    "decay resembles low-temperature behavior in oriented 3D CH3NH3PbI3, possibly due to "
    "intrinsic reduced electron-hole lifetime [@Grancini2017].",
    title="Fast PL decay at 730 nm",
    metadata={"figure": "artifacts/images/*.jpg", "caption": "Fig. 2c | 2 ns decay at 730 nm vs long decay at 760 nm"},
)

oxide_templating_role = claim(
    "The 2D perovskite anchored on oxide network templates growth of biphasic CH3NH3PbI3: "
    "oriented wider bandgap phase within oxide scaffold and standard tetragonal phase on top. "
    "This templating only occurs with mesoporous oxide - depositing on compact glass yields "
    "no 730 nm blue-shifted emission, only 760 nm regardless of excitation side [@Grancini2017].",
    title="Mesoporous oxide templating essential for graded interface",
)

# DFT Simulation Results
cb_upshift_2d_3d = claim(
    "DFT calculations show 0.14 eV conduction band (CB) upshift at 2D/3D interface compared to 3D bulk, "
    "inducing 0.09 eV larger interface gap than 3D bulk. This matches experimental PL blue shift "
    "of 0.13 eV when probing from oxide side. Only small ~0.02 eV shift of opposite sign found at "
    "MAPbI3/TiO2 interface [@Grancini2017].",
    title="DFT predicts 0.14 eV CB upshift at interface",
    metadata={"figure": "artifacts/images/*.jpg", "caption": "Fig. 3a | Local DOS showing CB upshift"},
)

cb_alignment_favorable = claim(
    "The 2D/3D interface forms a barrier to electron recombination (2D CB at lower energy than 3D CB) "
    "but does not block electron injection to TiO2. The 2D layer acts as protective window against "
    "moisture while preserving efficient charge transport [@Grancini2017].",
    title="2D CB alignment blocks recombination but not injection",
    metadata={"figure": "artifacts/images/*.jpg", "caption": "Fig. 3c | SOC calculations confirm CB alignment"},
)

graded_structure_dft = claim(
    "DFT results confirm 2D/3D perovskite organizes in gradual multi-dimensional structure retaining "
    "individual 2D and 3D phases, while templating formation of novel oriented CH3NH3PbI3 phase "
    "stabilized at the 2D/3D interface [@Grancini2017].",
    title="DFT confirms gradual multi-dimensional interface structure",
)