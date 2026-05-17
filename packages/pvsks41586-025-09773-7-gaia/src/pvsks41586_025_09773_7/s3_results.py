"""
Gaia knowledge package for Lin2025: Results - Charge-carrier dynamics and photovoltaic performance.
"""

from gaia.lang import claim, setting
from .motivation import diffusion_length_enhancement, pb_sn_psc_performance
from .s2_methods import type_ii_energy_alignment

# Steady-state photoluminescence
steady_state_pl = claim(
    "Steady-state photoluminescence measurements reveal a notable increase in photoluminescence intensity upon dipolar-passivation "
    "treatment, indicating suppressed non-radiative recombination in mixed Pb-Sn perovskite films [@Lin2025]."
)

# Time-resolved photoluminescence decay components
trpl_decay_components = claim(
    "Time-resolved photoluminescence analysis shows dipolar-passivation-treated films have a rapid initial decay component "
    "τ1 = 43 ns (attributed to charge-carrier separation) followed by a slower decay component τ2 = 3,912 ns (associated with "
    "bimolecular carrier recombination). In contrast, control films show τ1 = 132 ns and τ2 = 1,882 ns [@Lin2025]."
)

# Enhanced charge extraction
enhanced_charge_extraction = claim(
    "The rapid initial decay component (τ1 = 43 ns) for dipolar-passivation-treated films reflects enhanced charge extraction "
    "at the interface, consistent with the type-II energy-level alignment that facilitates efficient hole injection into PEDOT:PSS "
    "while repelling electrons from the HTL/Pb-Sn perovskite interface [@Lin2025]."
)

# Terahertz mobility measurements
terahertz_mobility = claim(
    "Femtosecond-resolved optical-pump terahertz-probe spectroscopy yields carrier mobilities of 67.5 cm^2 V^-1 s^-1 "
    "(control) and 113.5 cm^2 V^-1 s^-1 (dipolar-passivation), where μdc is the sum of electron and hole mobilities "
    "(μdc = μe + μh) [@Lin2025]."
)

# Limiting carrier mobility
limiting_carrier_mobility = claim(
    "The limiting carrier mobility (μe,h) is estimated at 14.7 cm^2 V^-1 s^-1 for dipolar-passivation samples and "
    "8.8 cm^2 V^-1 s^-1 for control samples, as determined by relating individual mobilities to their respective diffusion "
    "coefficients [@Lin2025]."
)

# Diffusion length
diffusion_length = claim(
    "The enhanced carrier mobility and relaxation dynamics in dipolar-passivation-treated films lead to longer diffusion "
    "lengths (Ld) of 6.2 μm, compared with 4.8 μm for the control, enabling improved carrier collection across the absorber "
    "layer [@Lin2025]."
)

# Electroluminescence quantum yield
electroluminescence_qy = claim(
    "Electroluminescence quantum yield analysis shows values of 2.40% (control) and 7.05% (dipolar-passivation) at current "
    "densities equivalent to Jsc under 1-sun illumination, corresponding to Voc losses of 103 mV and 73 mV, respectively [@Lin2025]."
)

# Average Voc improvement
average_voc_improvement = claim(
    "The average open-circuit voltage increases from 859 ± 8 mV (control devices) to 883 ± 12 mV (dipolar-passivation-treated "
    "devices), representing a 23 mV improvement attributable to reduced non-radiative recombination at the HTL interface [@Lin2025]."
)

# QFLS measurements
qfis_values = claim(
    "Quasi-Fermi level splitting (QFLS) measurements on perovskite films deposited on glass substrates show values of 958 meV "
    "(control) and 968 meV (dipolar-passivation). When the perovskite/PEDOT:PSS interface is included, QFLS values decrease to "
    "904 meV (control) and 940 meV (dipolar-passivation). The dipolar-passivation device shows an approximately 37-meV lower QFLS "
    "loss across the entire device stack compared with the control device [@Lin2025]."
)

# Photovoltaic performance metrics for single-junction Pb-Sn PSCs
single_junction_metrics = claim(
    "The best-performing dipolar-passivation device achieves a PCE of 24.9% (stabilized 24.7%) with Voc = 0.911 V, "
    "Jsc = 33.1 mA cm^-2, and FF = 82.6% under reverse scan (PCE = 24.7% under forward scan). The integrated photocurrent "
    "from EQE spectra is 32.7 mA cm^-2, in good agreement with J-V characterization [@Lin2025]."
)

# Statistical performance distribution
pcce_histogram = claim(
    "Statistical analysis of 208 dipolar-passivation-treated mixed Pb-Sn PSCs shows a narrow PCE distribution. The average PCE "
    "is 23.9 ± 0.3% compared with 22.6 ± 0.2% for control devices, representing a 1% improvement. The dipolar-passivation devices "
    "also show lower dark saturation-current density and smaller ideality factor, indicating suppressed non-radiative recombination [@Lin2025]."
)

# Operational stability
operational_stability = claim(
    "Dipolar-passivation-treated devices show no significant PCE degradation after over 1,000 hours in a nitrogen glovebox "
    "in the dark without encapsulation, demonstrating good stability under shelf storage conditions [@Lin2025]."
)

__all__ = [
    "steady_state_pl",
    "trpl_decay_components",
    "enhanced_charge_extraction",
    "terahertz_mobility",
    "limiting_carrier_mobility",
    "diffusion_length",
    "electroluminescence_qy",
    "average_voc_improvement",
    "qfis_values",
    "single_junction_metrics",
    "pcce_histogram",
    "operational_stability",
]