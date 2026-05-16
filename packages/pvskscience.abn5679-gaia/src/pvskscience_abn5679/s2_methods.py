"""
Methods: Device Fabrication, Characterization, and Stability Testing

This module contains methodological claims about device fabrication, characterization techniques,
and accelerated aging experimental protocols.
"""
from gaia.lang import claim, setting

# Device structure and fabrication
device_structure_diagram = claim(
    "The capped device structure features a 2D Cs2PbI2Cl2 layer atop the 3D CsPbI3 perovskite "
    "active layer, between the perovskite and the CuSCN hole transport layer.",
    title="Capped device structure features 2D layer"
)

# Photovoltaic characterization
champion_pce_uncapped = claim(
    "Uncapped CsPbI3 PSC champion device exhibits a power conversion efficiency (PCE) of 14.9%.",
    title="Uncapped champion PCE is 14.9%"
)

champion_pce_capped = claim(
    "Capped CsPbI3 PSC champion device exhibits a power conversion efficiency (PCE) of 17.4%, "
    "representing an improvement over uncapped devices.",
    title="Capped champion PCE is 17.4%"
)

capped_improved_ff_and_voc = claim(
    "Capped PSCs have improved fill factors (FFs) and open-circuit voltages (VOC) compared "
    "to uncapped devices, leading to higher PCE.",
    title="Capped devices show improved FF and VOC"
)

highest_efficiency_all_inorganic = claim(
    "The 17.4% PCE of capped CsPbI3 PSCs is the highest among fully inorganic PSCs in which "
    "all functional materials in the stack are inorganic.",
    title="17.4% is highest efficiency for all-inorganic PSCs"
)

# GIWAXS characterization of 2D layer
giwaxs_new_reflections = claim(
    "GIWAXS patterns showed two new reflections emerging on CsPbI3 films after CsCl treatment "
    "corresponding to the (002) and (004) reflections of 2D Cs2PbI2Cl2.",
    title="GIWAXS shows new 2D reflections after CsCl treatment"
)

giwaxs_surface_preferential = claim(
    "Increasing the incident angle of the x-ray beam resulted in a decrease in the relative "
    "intensity of the 2D reflections, suggesting that the 2D layer formed preferentially "
    "on the CsPbI3 surface.",
    title="2D layer forms preferentially at the surface"
)

giwaxs_interfacial_nature_confirmed = claim(
    "Cross-sectional scanning electron microscopy (SEM) imaging confirmed the interfacial "
    "nature of the 2D layer.",
    title="SEM confirms interfacial nature of 2D layer"
)

capping_layer_thickness = claim(
    "The thickness of the Cs2PbI2Cl2 capping layer is estimated to be 20 nm, determined by "
    "tracking chlorine content via XPS depth profiling.",
    title="Capping layer thickness is approximately 20 nm"
)

# TRPL characterization
trpl_lifetime_uncapped = claim(
    "The photoluminescence lifetime of uncapped CsPbI3 films on glass is 14 ns.",
    title="Uncapped film TRPL lifetime is 14 ns"
)

trpl_lifetime_capped = claim(
    "The photoluminescence lifetime of capped CsPbI3 films on glass exceeds 62 ns, "
    "increased relative to uncapped films.",
    title="Capped film TRPL lifetime exceeds 62 ns"
)

trpl_implies_suppressed_recombination = claim(
    "The increased TRPL lifetime in capped films suggests that the 2D capping layer "
    "effectively suppressed nonradiative recombination at the CsPbI3 surface and extended "
    "the lifetime and diffusion length of charge carriers.",
    title="Increased lifetime indicates suppressed surface recombination"
)

# Stability testing protocol
stability_test_conditions = claim(
    "N2-encapsulated solar cells were aged at their maximum power point (MPP) under constant "
    "illumination from a metal halide solar simulator at 35°C, 59°C, 85°C, and 110°C in "
    "(65±26)% relative humidity air.",
    title="Stability test conditions: MPP, 35-110°C, 1 sun"
)

no_degradation_capped_35c = claim(
    "Capped solar cells operating at 35°C did not show any PCE degradation, even after "
    "3531 hours of continuous operation.",
    title="Capped devices show no degradation at 35°C for 3531 hours"
)

biexponential_degradation_model = setting(
    "PCE degradation follows a biexponential function: "
    "PCE(t) = A1*exp(-k_fast*t) + A2*exp(-k_slow*t) + B, "
    "where k_fast and k_slow are fast and slow degradation rates, "
    "A1, A2, and B are constants, and t is time."
)

arrhenius_temperature_dependence = setting(
    "The degradation rate follows Arrhenius temperature dependence: "
    "k(T) = A*exp(-Ea/(kB*T)), where k(T) is the degradation rate at temperature T, "
    "A is a constant, Ea is the activation energy, and kB is Boltzmann's constant."
)

activation_energy_equation = setting(
    "Activation energy is equivalent to the slope: "
    "Ea = -∂ln(k(T))/∂(1/(kB*T))"
)

acceleration_factor_equation = setting(
    "Acceleration factor is defined as: "
    "AF = k_acc/k_ref = exp((Ea/kB)*(1/T_ref - 1/T_acc)), "
    "where T_acc and T_ref are the accelerated and reference temperatures."
)

# Fitting quality
fitting_r_squared = claim(
    "Biexponential fits to the degradation data achieved R-squared > 0.95 across the "
    "temperature range, except for capped solar cells at 35°C where no degradation was observed.",
    title="Biexponential fits have R^2 > 0.95"
)

# Ion migration characterization
temperature_dependent_conductivity = setting(
    "Temperature-dependent conductivity was measured in two-terminal lateral devices using "
    "the Nernst-Einstein equation: σ(T) = (σ0/T)*exp(-Ea_ion/(kB*T)), where σ0 is a "
    "temperature-independent prefactor and Ea_ion is the activation energy of ion migration."
)

two_transport_regimes = claim(
    "Plotting 1/T versus ln(σT) revealed two distinct transport regimes in both capped "
    "and uncapped films, corresponding to two distinct transport mechanisms.",
    title="Two distinct transport regimes observed"
)

high_temperature_ion_dominated = claim(
    "The high-temperature linear regime corresponds to ion-dominated transport and was used "
    "to extract the activation energy of ion migration (Ea_ion).",
    title="High-temperature regime is ion-dominated"
)

# XRD characterization of aged devices
xrd_uncapped_degradation = claim(
    "After 2000 hours of aging at 110°C under continuous illumination, the XRD reflection at "
    "2θ = 16.15° corresponding to the (003) reflection of CuSCN in uncapped PSCs became "
    "broader and less intense, suggesting decreased CuSCN crystallite size.",
    title="CuSCN XRD peak broadens in aged uncapped PSCs"
)

xrd_capped_no_change = claim(
    "After 2000 hours of aging at 110°C under continuous illumination, the XRD patterns of "
    "capped PSCs did not show appreciable changes in the CuSCN region.",
    title="CuSCN XRD peak unchanged in aged capped PSCs"
)

# SEM of aged devices
sem_uncapped_pinholes = claim(
    "SEM images of aged uncapped PSCs show the formation of pinholes and decreased film "
    "uniformity on the CuSCN surface.",
    title="SEM shows pinholes in aged uncapped PSCs"
)

sem_capped_no_change = claim(
    "SEM images of aged capped PSCs show no appreciable changes in film structure and morphology.",
    title="SEM shows no degradation in aged capped PSCs"
)

# XPS of aged devices
xps_iodine_increase_uncapped = claim(
    "The I 3d signal increased substantially in the XPS spectrum of the aged HTL surface "
    "for uncapped PSCs, indicating iodine migration from the CsPbI3 active layer.",
    title="I 3d signal increases in aged uncapped PSCs"
)

xps_no_iodine_capped = claim(
    "No appreciable I 3d signal was observed in the XPS spectrum of the HTL surface of "
    "aged capped PSCs.",
    title="No I 3d signal in aged capped PSCs"
)