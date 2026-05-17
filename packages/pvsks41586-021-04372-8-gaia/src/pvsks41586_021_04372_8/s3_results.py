"""
PV performance of Pb-Sn perovskite solar cells.

Results module covering device performance with different passivators
from Lin et al., Nature 2022.
"""

from gaia.lang import claim, setting, support, compare

# Passivator concentrations
optimal_concentrations = claim(
    "The optimal concentrations of PEA, PA, and CF3-PA were 0.2, 0.3, and 0.3 mol%, respectively.",
    title="Optimal passivator concentrations",
)

# Device performance comparison
cf3_pa_best_pv_parameters = claim(
    "Among the three passivators (PEA, PA, CF3-PA), CF3-PA resulted in the best performance "
    "values of open-circuit voltage (Voc), short-circuit current density (Jsc), fill factor (FF), "
    "and thus power conversion efficiency (PCE) for 1.2-micrometer-thick devices.",
    title="CF3-PA yields best PV parameters",
    metadata={"figure": "artifacts/images/17c068b8eff8c00671ade58847c7375183210e9bbea69335ef805fe7ef95c03e.jpg",
              "caption": "Fig. 2a | PV parameters of devices with different passivating agents."},
)

jsc_increases_with_thickness_cf3 = claim(
    "The Jsc values of CF3-PA devices increased with thickness, reaching approximately "
    "33 mA cm^-2 at a thickness of 1.2 micrometers, due to higher light absorption at the "
    "near-infrared range as indicated by external quantum efficiency (EQE) spectra.",
    title="CF3-PA Jsc increases with absorber thickness",
    metadata={"figure": "artifacts/images/04be71e816eb2730e6d351911c6249890cb533b6a8a3c248e46b430fdb01cade.jpg",
              "caption": "Fig. 2b,c | J-V and EQE curves of CF3-PA devices with varying thicknesses."},
)

control_jsc_saturates = claim(
    "The Jsc values of control devices did not exhibit an increase when thickness increased "
    "from 900 to 1,200 nm, and Voc and FF values dropped considerably with thickness beyond "
    "900 nm, indicating photogenerated carrier transport limits performance in thick devices.",
    title="Control device Jsc saturates and performance drops",
)

# Best CF3-PA device performance
best_cf3_pa_device = claim(
    "The best CF3-PA device showed a PCE of 22.2% (stabilized 22.0%) with Voc of 0.841 V, "
    "Jsc of 33.0 mA cm^-2, and FF of 80% under reverse scan for a 1.2-micrometer-thick absorber.",
    title="Best CF3-PA device performance",
    metadata={"figure": "artifacts/images/04be71e816eb2730e6d351911c6249890cb533b6a8a3c248e46b430fdb01cade.jpg",
              "caption": "Fig. 2d,e | J-V and EQE curves of the best CF3-PA device."},
)

average_pc3_pa_200_devices = claim(
    "Over 200 CF3-PA mixed Pb-Sn PSCs with 1.2-micrometer-thick absorber were fabricated, "
    "exhibiting an average PCE of 20.8 +/- 0.5%, which is a narrow distribution compared with "
    "typical Pb-Sn perovskite statistics.",
    title="Average PCE of 20.8% across 200+ devices",
)

eqe_integrated_jsc = claim(
    "The integrated Jsc value from EQE spectra of the best CF3-PA device was 32.5 mA cm^-2, "
    "in good agreement with the J-V characterization.",
    title="EQE integrated Jsc matches J-V measurement",
)

# Strategies
# Strategy: CF3-PA enables carrier transport in thick absorbers while control cannot
strat_cf3_vs_control = compare(
    jsc_increases_with_thickness_cf3,  # prediction: CF3-PA devices increase Jsc with thickness
    control_jsc_saturates,             # prediction: Control devices saturate Jsc at thickness > 900nm
    cf3_pa_best_pv_parameters,          # observation: CF3-PA devices achieve higher Voc, Jsc, FF than control
    reason="CF3-PA devices show increasing Jsc with thickness (33 mA cm^-2 at 1.2 micrometers), "
           "while control devices saturate Jsc and show degraded Voc/FF at thickness > 900 nm. "
           "The observation that CF3-PA yields the best PV parameters across all metrics confirms "
           "that the CF3-PA prediction better explains the experimental outcome.",
    prior=0.85,
)

__all__ = [
    "optimal_concentrations",
    "cf3_pa_best_pv_parameters",
    "jsc_increases_with_thickness_cf3",
    "control_jsc_saturates",
    "best_cf3_pa_device",
    "average_pc3_pa_200_devices",
    "eqe_integrated_jsc",
]