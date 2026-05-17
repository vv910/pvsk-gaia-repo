"""Priors for pvsks41560-024-01667-8-gaia package."""

from .motivation import (
    challenge_homogeneity,
    ligand_chain_effect,
)

from .s3_results import (
    dax_halide_pl,
    dft_formation_enthalpy_double,
    dft_formation_enthalpy_triple,
    n_value_challenge,
    giwaxs_results,
    dabr_giwaxs,
)

from .s5_results import (
    scalable_manufacturing,
)

PRIORS = {
    challenge_homogeneity: (0.85, "Direct observation of homogeneity problem."),
    ligand_chain_effect: (0.80, "Established relationship between chain length and n-value."),
    dax_halide_pl: (0.90, "Direct PL measurement showing halide behavior."),
    dft_formation_enthalpy_double: (0.80, "DFT calculation showing increased formation enthalpy."),
    dft_formation_enthalpy_triple: (0.80, "DFT calculation showing decreased with Br."),
    n_value_challenge: (0.85, "Direct observation of multiple n-values."),
    giwaxs_results: (0.90, "Direct GIWAXS with specified q-values."),
    dabr_giwaxs: (0.90, "Direct showing n=1 and n=2 coexistence."),
    scalable_manufacturing: (0.85, "Demonstrated with slot-die."),
}