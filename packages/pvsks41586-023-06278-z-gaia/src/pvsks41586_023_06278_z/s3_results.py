"""
Pb-Sn PSC and Tandem Solar Cell Results.

This module contains the experimental results for Pb-Sn PSCs with 3D/3D bilayer PHJ
and all-perovskite tandem solar cells.
"""

from gaia.lang import (
    claim,
    setting,
)

#------------------------------------------------------------------------------
# Pb-Sn PSC Performance Results (Figure 1)
#------------------------------------------------------------------------------

control_vs_phj_comparison = claim(
    "The average Voc and FF values of PHJ devices (0.869 V, 80.8%) were substantially "
    "higher than control devices (0.824 V, 78.5%), while Jsc remained similar, "
    "resulting in average PCE of 22.8% for PHJ versus 21.0% for control.",
    title="PHJ improves Voc and FF over control devices",
)

device_statistics = claim(
    "148 PHJ devices were fabricated with a histogram showing PCE distribution centered "
    "around 22-23%, indicating good reproducibility.",
    title="PHJ device statistics (148 devices)",
)

champion_device = claim(
    "The best PHJ device showed PCE of 23.8% (stabilized 23.5%) with Voc of 0.873 V, "
    "Jsc of 33.0 mA cm^-2, and FF of 82.6% under reverse scan, with very minor hysteresis "
    "between forward and reverse scans.",
    title="Champion PHJ device performance",
)

eqe_validation = claim(
    "EQE spectra of the champion PHJ device gave integrated photocurrent of 32.5 mA cm^-2, "
    "in good agreement with the J-V characterization value of 33.0 mA cm^-2.",
    title="EQE validates J-V measurements",
)

#------------------------------------------------------------------------------
# Charge Carrier Dynamics Results (Figure 3)
#------------------------------------------------------------------------------

pl_intensity_increase = claim(
    "The steady-state photoluminescence (PL) intensity was noticeably increased in PHJ films "
    "compared to control films, implying suppressed non-radiative recombination.",
    title="PHJ increases PL intensity",
)

trapped_reduction = claim(
    "Space-charge-limited current measurements showed reduced trap density in PHJ films "
    "compared to control, and PHJ devices showed lower dark-saturation-current density "
    "and smaller ideality factor than controls.",
    title="PHJ reduces traps and dark current",
)

built_in_potential = claim(
    "Mott-Schottky plot measurements revealed an improvement of about 50 mV in built-in "
    "potential (Vbi) in PHJ devices (0.775 V) compared to control devices (0.724 V).",
    title="PHJ increases built-in potential by 50 mV",
)

el_qy_comparison = claim(
    "At current densities equivalent to Jsc at one sun, the electroluminescence quantum yields "
    "were 0.47% for control and 3.09% for PHJ devices, corresponding to Voc losses of "
    "147 mV and 97 mV respectively.",
    title="PHJ device has higher EL quantum yield",
)

voc_loss_reduction = claim(
    "The reduced Voc loss (by approximately 50 mV) with PHJ structures is mainly ascribed "
    "to suppressed non-radiative charge-carrier recombination.",
    title="50 mV Voc loss reduction with PHJ",
)

trpl_phj_film = claim(
    "PHJ films exhibited an initial fast decay (tau_1 = 7 ns) attributed to charge-carrier "
    "separation, followed by a slow decay component (tau_2 = 3,614 ns) mainly caused by "
    "bimolecular carrier recombination.",
    title="PHJ film TRPL: fast charge separation",
)

trpl_control_film = claim(
    "Control films showed no rapid decay component, with bimolecular recombination rates "
    "(tau_1 = 283 ns, tau_2 = 1,073 ns) shorter than PHJ films, indicating more severe "
    "non-radiative recombination.",
    title="Control film TRPL: slower recombination",
)

electron_transfer_rate = claim(
    "Differential lifetime analysis showed faster electron transfer to ETL for PHJ "
    "(70 ns) compared to control (110 ns), indicating the 3D/3D heterostructure "
    "promotes electron transfer to the ETL.",
    title="PHJ enables faster electron transfer to ETL",
)

#------------------------------------------------------------------------------
# Transient Absorption Results
#------------------------------------------------------------------------------

control_ta_spectrum = claim(
    "The control film showed a single photobleaching peak at 934 nm without noticeable shift "
    "at different time delays, indicating homogeneous composition and phase.",
    title="Control film shows single TA peak",
)

phj_ta_nbg_pumped = claim(
    "When pumping the PHJ sample (300 nm Pb-Sn NBG / 100 nm FL-WBG) with 405 nm light "
    "from the NBG side, a second bleaching peak at 780 nm appeared in TA spectra "
    "(attributed to FL-WBG perovskite), increasing over time after 300 ps, indicating "
    "electron injection from Pb-Sn into FL-WBG perovskite.",
    title="PHJ shows charge transfer when pumped from NBG side",
)

phj_ta_fl_wbg_pumped = claim(
    "When pumping the FL-WBG side with 405 nm light, only the 780 nm bleach peak appeared "
    "without notable charge-transfer process, suggesting photocarriers are unlikely to be "
    "back-transferred from FL-WBG to Pb-Sn perovskite - consistent with type II band alignment.",
    title="No back-transfer from FL-WBG to NBG",
)

#------------------------------------------------------------------------------
# Tandem Solar Cell Results (Figure 4)
#------------------------------------------------------------------------------

wbg_subcell_performance = claim(
    "WBG subcells (FA0.8Cs0.2Pb(I0.62Br0.38)3, bandgap 1.78 eV) with NiO/SAM hole transport "
    "layer exhibited PCE of 18.6% with Voc of 1.274 V, Jsc of 17.7 mA cm^-2, and FF of 82.6%.",
    title="WBG subcell performance",
)

nbg_subcell_in_tandem = claim(
    "The NBG subcell with PHJ in tandem configuration showed improved performance, "
    "with the tandem achieving average PCE of 27.9 +/- 0.3% versus 26.5 +/- 0.3% for control.",
    title="PHJ improves tandem performance",
)

tandem_ff_improvement = claim(
    "Under current-matching conditions, the tandem with PHJ NBG subcell shows FF of 81.4% "
    "versus 78.0% for control tandem, and PCE of 27.7% versus 26.0%.",
    title="Tandem FF and PCE improvement with PHJ",
)

tandem_champion = claim(
    "The champion tandem device achieved PCE of 28.5% (reverse scan) with Voc of 2.112 V, "
    "Jsc of 16.5 mA cm^-2, and FF of 81.9%, with stabilized PCE of 28.4%.",
    title="Champion tandem device achieves 28.5% PCE",
)

eqe_tandem = claim(
    "Integrated Jsc values from EQE spectra for both WBG and NBG subcells are both "
    "16.5 mA cm^-2, in good agreement with J-V measurements.",
    title="EQE confirms current matching in tandem",
)

certified_efficiency = claim(
    "The tandem device delivered a certified stabilized PCE of 28.0% by Japan Electrical "
    "Safety and Environment Technology Laboratories (JET), an accredited independent "
    "PV calibration laboratory.",
    title="Tandem certified at 28.0% by JET",
)

large_area_tandem = claim(
    "A large-area tandem device (aperture area 1.05 cm^2) exhibited PCE of 26.9% with "
    "Voc of 2.149 V, Jsc of 15.7 mA cm^-2, and FF of 79.8%.",
    title="Large-area tandem achieves 26.9% PCE",
)

#------------------------------------------------------------------------------
# Operational Stability
#------------------------------------------------------------------------------

operational_stability = claim(
    "The encapsulated tandem device with PHJ maintained 93% of its initial PCE after "
    "600 hours of maximum power point (MPP) tracking under simulated AM 1.5G illumination "
    "(100 mW cm^-2) in ambient air (humidity 30-50%).",
    title="Tandem retains 93% efficiency after 600h",
)

degradation_mechanism = claim(
    "Performance degradation after 688 hours of operation was mainly due to FF drop, "
    "which could partially result from migration of Au from the tunnel recombination "
    "junction into the perovskite absorber.",
    title="FF drop causes long-term degradation",
)

reverse_bias_stability = claim(
    "The reverse-bias stability of all-perovskite tandem solar cells was superior to "
    "that of single-junction PSCs, which is beneficial under partial shading conditions.",
    title="Tandem has good reverse-bias stability",
)

#------------------------------------------------------------------------------
# Device Simulation Results (Figure 2)
#------------------------------------------------------------------------------

simulation_model = claim(
    "SCAPS-1D simulation was used to investigate the effect of PHJs on PV performance, "
    "varying trap density and layer thickness of the defective interface layer (DIL).",
    title="SCAPS-1D simulation of PHJ effect",
)

dil_trap_density_effect = claim(
    "At low DIL trap densities (similar to bulk), PV performances of control and PHJ devices "
    "are comparable; however, at high DIL trap densities, control devices suffer marked "
    "performance reduction while PHJ devices do not.",
    title="PHJ mitigates high DIL trap density effects",
)

dil_thickness_effect = claim(
    "Unlike control devices, PHJ device performance is much less sensitive to DIL thickness, "
    "showing robust performance regardless of interfacial layer thickness.",
    title="PHJ performance insensitive to DIL thickness",
)

simulated_improvement = claim(
    "Simulation predicted more than 40 mV increase in Voc and absolute 5% increase in FF "
    "when PHJ was incorporated with DIL thickness and trap density reasonable for "
    "experimental conditions.",
    title="Simulation predicts >40mV Voc and 5% FF improvement",
)

__all__ = [
    "control_vs_phj_comparison",
    "device_statistics",
    "champion_device",
    "eqe_validation",
    "pl_intensity_increase",
    "trapped_reduction",
    "built_in_potential",
    "el_qy_comparison",
    "voc_loss_reduction",
    "trpl_phj_film",
    "trpl_control_film",
    "electron_transfer_rate",
    "control_ta_spectrum",
    "phj_ta_nbg_pumped",
    "phj_ta_fl_wbg_pumped",
    "wbg_subcell_performance",
    "nbg_subcell_in_tandem",
    "tandem_ff_improvement",
    "tandem_champion",
    "eqe_tandem",
    "certified_efficiency",
    "large_area_tandem",
    "operational_stability",
    "degradation_mechanism",
    "reverse_bias_stability",
    "simulation_model",
    "dil_trap_density_effect",
    "dil_thickness_effect",
    "simulated_improvement",
]