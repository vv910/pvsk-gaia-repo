"""
Morphology and crystallinity of perovskite films on different SAMs.

This module covers contact angle measurements, AFM, SEM, XRD, and in-situ characterization.
"""

from gaia.lang import (
    claim,
    setting,
)

# Contact angle measurements
water_contact_angles = claim(
    "The water contact angles of the Me-4PACz-, MeO-4PACz- and HTL201-coated IZO substrates "
    "are 104.6 degrees, 79.6 degrees and 105.6 degrees, respectively.",
    title="Water contact angles on SAM-coated IZO",
)

perovskite_precursor_contact = claim(
    "When the perovskite precursor solution was used, the contact angles on the MeO-4PACz and "
    "HTL201 SAMs are nearly 0 degrees, whereas the contact angle on Me-4PACz increases to 11.6 degrees. "
    "The low contact angle of the perovskite precursor on the substrates is crucial for achieving "
    "full coverage of perovskite films.",
    title="Perovskite precursor contact angles near 0 for HTL201",
)

# AFM morphology
htl201_smooth_uniform = claim(
    "The HTL201-modified IZO substrate shows good smoothness and uniformity without obvious "
    "aggregates, which will facilitate interfacial charge transfer and suppress non-radiative "
    "recombination. By contrast, after coating Me-4PACz and MeO-4PACz SAMs, some irregular "
    "particles can be observed on the sample surface, which may be caused by molecular aggregation.",
    title="HTL201 gives smooth uniform surface",
)

# Perovskite film morphology
htl201_perovskite_dense_uniform = claim(
    "The perovskite film based on a HTL201 layer shows dense and uniform morphology with "
    "larger grain size compared to other SAMs.",
    title="HTL201 perovskite film dense with large grain size",
)

perovskite_thickness = claim(
    "The thickness of the perovskite film is about 900 nm.",
    title="Perovskite film thickness 900 nm",
)

# XRD and crystallinity
htl201_enhanced_crystallinity = claim(
    "The increased diffraction intensity in X-ray diffraction measurements reveals enhanced "
    "crystallinity of perovskite film based on HTL201. A larger (100)/(210) peak intensity "
    "ratio suggests a highly ordered crystal growth along the (100) plane.",
    title="HTL201 perovskite shows enhanced crystallinity",
)

# In-situ crystallization
htl201_delayed_nucleation = claim(
    "The HTL201-based sample shows a large number of nuclei after 540 s, which is slightly "
    "longer than that of the Me-4PACz-coated (180 s) and MeO-4PACz-coated (300 s) substrates. "
    "The nucleation and crystallization processes were notably delayed when using the "
    "HTL201-coated substrate, which can effectively improve the quality of perovskite films.",
    title="HTL201 delays nucleation and crystallization",
)

__all__ = [
    "water_contact_angles",
    "perovskite_precursor_contact",
    "htl201_smooth_uniform",
    "htl201_perovskite_dense_uniform",
    "perovskite_thickness",
    "htl201_enhanced_crystallinity",
    "htl201_delayed_nucleation",
]