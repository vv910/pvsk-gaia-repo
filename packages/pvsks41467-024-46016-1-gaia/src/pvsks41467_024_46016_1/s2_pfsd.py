"""Control of perovskite crystallisation for upscaling via PFSD technique."""

from gaia.lang import (
    claim,
    setting,
    support,
)

# PFSD technique claims
pfsd_technique_description = claim(
    "The printing-friendly sequential deposition (PFSD) technique adds organic cations at a loading of less than 50 mol% of PbI₂, far below the stoichiometric amount required to form perovskite crystals. This strategy retards crystallization and the precursor thin-film behaves like an amorphous material with much better film-forming properties than crystalline analogues [@Weerasinghe2024].",
    title="PFSD technique uses sub-stoichiometric organic cations",
)

pfsd_advantage = claim(
    "When additional organic cation is subsequently deposited, the reactive amorphous-phase film quickly converts to a perovskite without needing to remove the additive as it becomes part of the perovskite, allowing conversion on a time scale suitable for R2R processing [@Weerasinghe2024].",
    title="PFSD enables rapid perovskite conversion",
)

shallow_angle_blowing = claim(
    "The shallow-angle blowing technique blows gas at a shallow angle on the edge of a roller, as opposed to the conventional blowing technique applied at a right angle. This approach allows the SD-coated wet films to not be deformed by an aggressive air flow before entering the well-defined solidification zone, significantly reducing crystalline defects [@Weerasinghe2024].",
    title="Shallow-angle blowing technique for R2R",
)

edge_blowing_result = claim(
    "The shallow-angle blowing technique produces perovskite films with an intermediate layer that appears amorphous or comprises small enough grains that allow for rapid and complete conversion to perovskite upon MAI deposition, resulting in mirror-like films under ambient conditions (40-50% relative humidity) [@Weerasinghe2024].",
    title="Edge-blowing produces uniform perovskite films",
)

xrd_analysis = claim(
    "X-ray diffraction (XRD) analysis of edge-blown perovskite films does not indicate the presence of PbI₂ crystals, which would be evidence of ion migration followed by inhomogeneous local concentration in the solidification process [@Weerasinghe2024].",
    title="XRD shows no PbI₂ residual in edge-blown films",
)

sem_improvement = claim(
    "Scanning electron microscope (SEM) images show more homogenous films with compact grains of the shallow-angle-blown sample compared to the right-angle-blown sample [@Weerasinghe2024].",
    title="SEM confirms improved film morphology",
)

humidity_tolerance = claim(
    "The introduction of shallow-angle blowing not only improved the quality of the perovskite and the reliability of device performance but also enhanced humidity tolerance, making the PFSD approach suitable for low-cost manufacturing [@Weerasinghe2024].",
    title="Shallow-angle blowing enhances humidity tolerance",
)

pfsd_record_pce = claim(
    "Further development of the PFSD method resulted in up to 17.9% PCE from R2R-fabricated PeSCs with vacuum-deposited Au electrodes, as discussed in Supplementary Note 2 [@Weerasinghe2024].",
    title="PFSD enables up to 17.9% PCE with Au electrodes",
)

__all__ = [
    "pfsd_technique_description",
    "pfsd_advantage",
    "shallow_angle_blowing",
    "edge_blowing_result",
    "xrd_analysis",
    "sem_improvement",
    "humidity_tolerance",
    "pfsd_record_pce",
]