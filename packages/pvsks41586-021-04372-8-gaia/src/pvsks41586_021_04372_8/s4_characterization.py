"""
Characterization of Pb-Sn perovskite films.

Results module covering structural and optoelectronic characterization
from Lin et al., Nature 2022.
"""

from gaia.lang import claim, setting, support

# Morphology and structure
passivator_no_morphology_change = claim(
    "Introducing the passivator additives (PEA, PA, CF3-PA) did not notably affect the surface "
    "morphology of Pb-Sn perovskite films.",
    title="Passivators do not change surface morphology",
    metadata={"figure": "artifacts/images/7a532a366e9ff41f6b2c1ee6cbd23d6db079ac5f3d8336c5a2f0e295c26a26e7.jpg",
              "caption": "Fig. 3a,b | SEM images of control and CF3-PA perovskite films."},
)

cf3_pa_at_surfaces_and_boundaries = claim(
    "Time-of-flight secondary ion mass spectrometry (ToF-SIMS) revealed that passivators were "
    "anchored on the top and bottom film surfaces as well as at the grain boundaries within the film.",
    title="Passivators anchored at surfaces and grain boundaries",
)

single_3d_perovskite_phase = claim(
    "X-ray diffraction (XRD) patterns of control and passivated films exhibited a single "
    "three-dimensional (3D) perovskite phase without a 2D (reduced-dimensional) phase and without "
    "non-perovskite phases.",
    title="Single 3D perovskite phase maintained",
    metadata={"figure": "artifacts/images/efc1a193ed31a49d7046e9af83227e1e6eb376480f8bb08043d127952c22e7e4.jpg",
              "caption": "Fig. 3c | XRD patterns showing single 3D perovskite phase."},
)

no_2d_peaks_high_concentration = claim(
    "No diffraction peaks relating to 2D layered perovskites were found even when a large amount "
    "of CF3-PA (20 mol%) was added to the precursor solution, which is beneficial for charge "
    "transport and extraction throughout the thick Pb-Sn perovskite absorber.",
    title="No 2D perovskite formation even at high CF3-PA concentration",
)

# Sn oxidation suppression
sn4_plus_at_surface_control = claim(
    "Angle-dependent XPS measurements at electron take-off angles of 0, 45, and 75 degrees show "
    "that Sn4+ primarily forms on the surface of control films (probing depth 1.5-2 nm at 75 degrees), "
    "indicating surface Sn2+ oxidation.",
    title="Sn4+ forms at surface of control films",
)

sn2_plus_oxidation_suppressed = claim(
    "Surface Sn2+ oxidation was successfully suppressed after anchoring of CF3-PA on the grain "
    "surfaces, indicating that passivation of surface defects (undercoordinated Sn atoms and Sn "
    "vacancies) could retard Sn2+ oxidation.",
    title="CF3-PA suppresses Sn2+ oxidation",
)

# Photoluminescence characterization
pl_intensity_enhanced_cf3 = claim(
    "Steady-state photoluminescence (PL) intensity was noticeably increased with the CF3-PA "
    "passivating agent, implying suppressed non-radiative charge recombination through defects.",
    title="CF3-PA enhances PL intensity",
    metadata={"figure": "artifacts/images/f32a7a3e7454ddf6e1595e9f8d7b42bdf5c2fd4e6ce74f481a5002fb90e6a52f.jpg",
              "caption": "Fig. 3d | Steady-state PL spectra showing enhanced intensity with CF3-PA."},
)

carrier_lifetimes = claim(
    "Time-resolved PL measurements show effective carrier lifetimes: CF3-PA, tau = 966 ns; PA, "
    "tau = 437 ns; PEA, tau = 365 ns; control (non-passivated), tau = 159 ns. The longer "
    "charge-carrier recombination lifetime with CF3-PA was also confirmed by transient photovoltage "
    "decay measurements.",
    title="Carrier lifetimes increase with CF3-PA",
    metadata={"figure": "artifacts/images/aaddfab60fe40f2a4f94b5c160d573e2ac60f62ba9321dfed4993804ca3a6c2.jpg",
              "caption": "Fig. 3e | Time-resolved PL spectra showing longer lifetimes with passivators."},
)

# Mobility and diffusion length
similar_dc_mobility = claim(
    "The control and CF3-PA films exhibited similar effective d.c. charge-carrier mobilities "
    "(mu_dc) of approximately 80 cm^2 V^-1 s^-1, where mu_dc is the sum of electron and hole "
    "mobilities (mu_dc = mu_e + mu_h).",
    title="Similar DC mobility in control and CF3-PA films",
)

diffusion_length_increased_threefold = claim(
    "The diffusion length (Ld) of CF3-PA passivated films was increased threefold compared to "
    "control films (5.4 micrometers versus 1.8 micrometers), due to longer carrier lifetimes despite "
    "similar mobilities.",
    title="Diffusion length increased threefold with CF3-PA",
    metadata={"figure": "artifacts/images/f1f497ebda150e0b7ca552d49aa4d1ad916cf41770350b75ca34a9422c4f9e2d.jpg",
              "caption": "Fig. 3f | Mobilities and diffusion lengths of CF3-PA and control films."},
)

limiting_carrier_mobility = claim(
    "The mobility of the limiting carrier (mu_e,h) was 11.7 +/- 1.5 and 8.2 +/- 1.2 cm^2 V^-1 s^-1 "
    "for CF3-PA and control Pb-Sn perovskite films, respectively.",
    title="Limiting carrier mobility values",
)

# Strategies
strat_lifetime_enables_diffusion = support(
    [carrier_lifetimes, similar_dc_mobility],
    diffusion_length_increased_threefold,
    reason="Diffusion length depends on both mobility and lifetime (Ld = sqrt(mu*tau)). Although "
           "mobilities are similar, the 6-fold increase in carrier lifetime (966 ns vs 159 ns) "
           "produces the 3-fold increase in diffusion length (5.4 um vs 1.8 um).",
    prior=0.85,
)

__all__ = [
    "passivator_no_morphology_change",
    "cf3_pa_at_surfaces_and_boundaries",
    "single_3d_perovskite_phase",
    "no_2d_peaks_high_concentration",
    "sn4_plus_at_surface_control",
    "sn2_plus_oxidation_suppressed",
    "pl_intensity_enhanced_cf3",
    "carrier_lifetimes",
    "similar_dc_mobility",
    "diffusion_length_increased_threefold",
    "limiting_carrier_mobility",
]