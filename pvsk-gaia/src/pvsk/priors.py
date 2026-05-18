"""
Priors for independent synthesis laws.

Foreign claims imported from paper packages cannot be assigned priors from this
package; Gaia requires package priors to target Knowledge objects declared by
the current package.  Their beliefs are supplied by dependency packages during
`gaia infer . --depth 1`.
"""

from .s4_induction import (
    law_band_alignment_controls_charge_selectivity,
    law_interface_passivation_reduces_nonradiative_loss,
    law_perovskite_absorbers_scale_across_architectures,
    law_scalable_deposition_can_preserve_device_quality,
    law_stability_needs_phase_and_interface_control,
    law_tandems_raise_perovskite_efficiency_ceiling,
)


PRIORS: dict = {
    law_perovskite_absorbers_scale_across_architectures: (
        0.62,
        "A moderate prior is appropriate because the law is generalized across architectures and should be confirmed by independent paper observations.",
    ),
    law_interface_passivation_reduces_nonradiative_loss: (
        0.64,
        "A moderate prior reflects broad physical plausibility while leaving the conclusion to be strengthened by independent passivation packages.",
    ),
    law_stability_needs_phase_and_interface_control: (
        0.58,
        "The law is a synthesis-level generalization across stress modes, so it starts below high confidence until induction over stability packages is applied.",
    ),
    law_band_alignment_controls_charge_selectivity: (
        0.63,
        "Band alignment is a standard device principle, but the PVSK-specific version is tested across imported packages.",
    ),
    law_tandems_raise_perovskite_efficiency_ceiling: (
        0.61,
        "The tandem law is plausible from detailed-balance reasoning, but this package lets certified tandem results provide the main confirmation.",
    ),
    law_scalable_deposition_can_preserve_device_quality: (
        0.55,
        "Scale-up is the most conditional generalization, so its prior is deliberately cautious before manufacturing evidence is applied.",
    ),
}
