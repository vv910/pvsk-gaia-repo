"""
Gaia knowledge package for Lin2025: All-perovskite tandem solar cells with dipolar passivation.
Discussion/Conclusions - Tandem device performance and stability.
"""

from gaia.lang import claim, setting
from .motivation import tandem_performance
from .s3_results import single_junction_metrics

# Tandem device configuration
tandem_device_configuration = claim(
    "All-perovskite tandem solar cells have a device configuration of glass/ITO/NiO/SAM/WBG perovskite/C60/ALD-SnO2/Au/"
    "PEDOT:PSS/NBG perovskite/C60/BCP or ALD/Cu, where SAM is (2-(9H-carbazol-9-yl)ethyl)phosphonic acid (2PACz) and "
    "MeO-2PACz mixture (75:25 vol%), WBG composition is FA0.8Cs0.2Pb(I0.62Br0.38)3 (~1.78 eV bandgap), and NBG is "
    "FA0.7MA0.3Pb0.5Sn0.5I3 (~1.25 eV bandgap) [@Lin2025]."
)

# Buried interface challenges in tandem cells
tandem_buried_interface_challenge = claim(
    "The buried interfaces within the NBG subcells are associated with severe non-radiative carrier recombination and hindered "
    "carrier extraction. Additionally, the low-temperature annealing required for PEDOT:PSS in the interconnection layer "
    "deteriorates its electrical properties, causing further losses in Voc and FF compared with the superposition of each "
    "single-junction subcell [@Lin2025]."
)

# Dipolar passivation reduces tandem sensitivity
tandem_sensitivity_reduction = claim(
    "Dipolar-passivation-treated NBG devices show minimal degradation in tandem photovoltaic performance compared with single-junction "
    "NBG PSCs, indicating that dipolar passivation makes the NBG subcell less sensitive to the crystal quality of PEDOT:PSS [@Lin2025]."
)

# Tandem performance metrics
tandem_pv_parameters = claim(
    "Dipolar-passivation tandem devices show significantly improved FF and Voc compared with control tandem devices. The average PCE "
    "increases to 30.3 ± 0.3% (versus 29.1 ± 0.2% for control devices). The average Voc of dipolar-passivation tandem devices is "
    "approximately 50 mV higher than control devices, exceeding the ~30 mV Voc difference observed between control and "
    "dipolar-passivation single-junction devices, consistent with Voc loss caused by the changed PEDOT:PSS preparation process [@Lin2025]."
)

# Champion tandem device
champion_tandem_device = claim(
    "The champion tandem cell with dipolar passivation shows minimal hysteresis and achieves a reverse-scan PCE of 30.6% with "
    "Voc = 2.211 V, Jsc = 16.6 mA cm^-2, and FF = 83.4%. The stabilized PCE is measured at 30.2%. The integrated Jsc values "
    "from EQE spectra are 16.6 mA cm^-2 for both WBG and NBG subcells, matching J-V measurements [@Lin2025]."
)

# JET certification
jet_certified_pce = claim(
    "Third-party certification by JET confirms a stabilized PCE of 30.1% for a tandem device with active area of 0.049 cm^2, "
    "included in the Solar Cell Efficiency Tables (version 64). A large-area device (1.07 cm^2) achieves a certified stabilized "
    "PCE of 29.6% [@Lin2025]."
)

# Large-area tandem performance
large_area_tandem = claim(
    "Tandem cells with an area of 1.05 cm^2 achieve up to 29.6% PCE in the lab with good homogeneity and current matching. "
    "Performance is confirmed by independent certification (JET) at 29.6% with aperture area of 1.07 cm^2 [@Lin2025]."
)

# WBG subcell performance
wbg_subcell_performance = claim(
    "The WBG subcells (FA0.8Cs0.2Pb(I0.62Br0.38)3, ~1.78 eV) with SAM-modified NiO HTL achieve a PCE of 20.5% with "
    "Voc = 1.329 V, Jsc = 18.4 mA cm^-2, and FF = 83.8% [@Lin2025]."
)

# Thickness optimization
thickness_optimization = claim(
    "For optimal current density matching between subcells, the thicknesses of WBG and NBG absorber layers are optimized "
    "to approximately 380 nm and 1,200 nm, respectively, for the front and back subcells in tandem configuration [@Lin2025]."
)

# Contact loss mitigation
contact_loss_mitigation = claim(
    "Dipolar passivation effectively mitigates contact losses in the NBG subcell induced by the interconnecting layer of "
    "tandem devices, contributing to the outstanding PCE of 30.6% in all-perovskite tandem solar cells [@Lin2025]."
)

# Operational stability of tandem devices
tandem_operational_stability = claim(
    "Encapsulated dipolar-passivation-treated tandem devices retain 87% of initial PCE after 1,025 hours of continuous "
    "maximum power point operation under simulated 1-sun illumination in ambient air, outperforming unpassivated devices [@Lin2025]."
)

# Thermal stability
tandem_thermal_stability = claim(
    "After 216 hours of thermal stress at elevated temperature, degradation proceeds more slowly in dipolar-passivation-based "
    "devices than in control devices. Within the first 50 hours, the dipolar-passivation device shows a much smaller drop in PCE, "
    "likely due to the amphoteric nature of dipolar-passivation molecules mitigating the detrimental impact of PEDOT:PSS "
    "acidity on device stability [@Lin2025]."
)

# Future direction
future_direction = claim(
    "Further mitigation of Jsc losses induced by HTL parasitic absorption (particularly in Pb-Sn PSCs with PEDOT:PSS HTLs) "
    "represents a key direction for advancing the PCE of all-perovskite tandem solar cells. Integration of dipolar passivation "
    "with advanced stabilization strategies will be critical for improving long-term stability [@Lin2025]."
)

__all__ = [
    "tandem_device_configuration",
    "tandem_buried_interface_challenge",
    "tandem_sensitivity_reduction",
    "tandem_pv_parameters",
    "champion_tandem_device",
    "jet_certified_pce",
    "large_area_tandem",
    "wbg_subcell_performance",
    "thickness_optimization",
    "contact_loss_mitigation",
    "tandem_operational_stability",
    "tandem_thermal_stability",
    "future_direction",
]