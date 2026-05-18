"""
Discussion and conclusions for the Min2019 perovskite solar cell paper.

This module covers the mechanistic interpretation of results: phase stabilization
mechanisms, Cl interstitial role, stability mechanisms, and final conclusions.
"""

from gaia.lang import (
    claim,
)

# -----------------------------------------------------------------------------
# Stabilization mechanisms
# -----------------------------------------------------------------------------

stabilization_mechanism_h_bonding = claim(
    "MDA2+ stabilizes the alpha-FAPbI3 phase through hydrogen bonding between the "
    "multiple H-N groups of MDA and I- ions in the lattice, similar to the mechanism "
    "by which MA stabilizes alpha-FAPbI3. However, MDA has more hydrogen atoms than "
    "FA or MA, enabling more H-bonds with I-, providing structural stabilization at "
    "even smaller amounts than MA (3.8 mol% MDACl2 vs 5 mol% MAPbBr3 in control) "
    "[@Min2019, refs 33-35].",
    title="H-bonding stabilization mechanism",
)

stabilization_mechanism_entropic = claim(
    "Cation mixing at FA sites (MDA2+ substituting for FA+) affords entropic "
    "stabilization through the resulting entropy gain and small internal energy "
    "input, forming a solid solution that stabilizes the black alpha-phase against "
    "conversion to the yellow delta-phase. This entropic contribution complements "
    "the enthalpic H-bonding stabilization from MDA [@Min2019, ref 32].",
    title="Entropic stabilization from cation mixing",
)

stabilization_mechanism_tolerance_factor = claim(
    "Goldschmidt tolerance factor t for FAPbI3 is approximately 1.0, above the "
    "optimal t ~ 0.9 for the cubic phase. Substituting MDA2+ (ionic radius 262 pm) "
    "for FA+ (256 pm) at 3.8 mol% brings t slightly closer to 0.9, improving "
    "thermodynamic stability of the cubic alpha-phase. The divalent state of MDA2+ "
    "also introduces beneficial lattice strain relaxation through charge-compensating "
    "defects (FA vacancies or Cl interstitials) [@Min2019].",
    title="Tolerance factor adjustment by MDA substitution",
)

stabilization_mechanism_cl_interstitial = claim(
    "Cl- ions (ionic radius 181 pm, much smaller than I- at 220 pm) introduced "
    "alongside MDA2+ incorporation occupy interstitial sites rather than substituting "
    "for I- sites. These interstitial Cl- ions expand the lattice (observed in XRD "
    "peak shift to lower angles) and reduce lattice strain, contributing to "
    "phase stabilization. The interstitial Cl is distinct from Cl substitution "
    "(which would cause larger bandgap widening) and explains the smaller-than-expected "
    "bandgap increase with MDACl2 addition [@Min2019].",
    title="Interstitial Cl- ions contribute to stabilization",
)

v_fa_defects_shallow = claim(
    "FA vacancy (V_FA) defects formed by MDA2+ substitution are shallow traps "
    "near the conduction band, as confirmed by the fact that 3.8 mol% MDACl2 "
    "incorporation does not reduce JSC (which would be expected if deep traps were "
    "present) and actually enhances PL quantum yield. This is consistent with "
    "prior reports that V_FA defects in FAPbI3 do not act as detrimental "
    "non-radiative recombination centers [@Min2019, ref 37].",
    title="FA vacancy defects are shallow and non-trapping",
)

phase_stability_summary = claim(
    "The alpha-phase stabilization of FAPbI3 by MDACl2 arises from three factors: "
    "(1) H-bonding between MDA's H-N groups and I- in the lattice, (2) entropic "
    "stabilization from cation mixing at FA sites, and (3) lattice strain relief "
    "from interstitial Cl- ions accommodating charge compensation. These mechanisms "
    "kinetically trap the metastable alpha-phase at room temperature, preventing "
    "the thermodynamically favored conversion to the delta-phase "
    "under humidity, thermal, and optical stress conditions [@Min2019].",
    title="Multi-factor alpha-phase stabilization mechanism",
)

# -----------------------------------------------------------------------------
# Cl interface enrichment and photostability
# -----------------------------------------------------------------------------

cl_interface_photostability = claim(
    "The Cl enrichment at the TiO2/perovskite interface (confirmed by XPS and "
    "ToF-SIMS) contributes to the exceptional photostability of the target device. "
    "Prior studies showed that Cl at this interface increases the light stability "
    "of PSCs by suppressing TiO2 photocatalytic activity that would otherwise "
    "degrade the perovskite layer under UV illumination. The MDACl2 doping "
    "strategy naturally concentrates Cl at this critical interface, whereas the "
    "control MAPbBr3 does not [@Min2019, refs 41-42].",
    title="Interface Cl improves photostability",
)

photostability_mechanism = claim(
    "The exceptional photostability (90% PCE retention after 600 hours MPP tracking) "
    "results from two synergistic factors: (1) interfacial Cl enrichment suppressing "
    "TiO2 photocatalysis, and (2) alpha-phase stabilization by MDA preventing "
    "photo-induced phase transition. Both factors are necessary for the observed "
    "long-term performance under full sunlight without UV filtering [@Min2019].",
    title="Dual mechanism for photostability",
)

# -----------------------------------------------------------------------------
# Comparison with existing literature
# -----------------------------------------------------------------------------

literature_comparison = claim(
    "Prior to this work, the highest efficiency for mp-TiO2-based PSCs was achieved "
    "with FAPbI3 stabilized by MAPbBr3 (5 mol%), reaching approximately 23% PCE "
    "with certified JSC around 25 mA/cm2. The target device in this work achieves "
    "24.66% PCE (certified 23.73%) with certified JSC of 26.70 mA/cm2, "
    "representing a 1.6 mA/cm2 improvement in current density. This improvement "
    "directly results from maintaining the inherent narrower bandgap of FAPbI3 "
    "[@Min2019].",
    title="Performance exceeds prior art mp-TiO2 PSCs",
)

aberration_free_stability = claim(
    "Unlike mixed-cation-anion approaches that sacrifice thermal stability (MA), "
    "introduce phase segregation (Br), or require complex synthesis (Cs/Rb), "
    "the MDACl2 approach achieves both high efficiency and robust stability "
    "without any of these trade-offs. The MDACl2-stabilized devices retain more "
    "than 90% of initial PCE after 20 hours at 150C in air (vs <20% for MA "
    "-containing control) and after 70 hours at 85% RH (vs 40% for control). "
    "This demonstrates that alpha-FAPbI3 can be stabilized without the usual "
    "efficiency-stability trade-offs inherent to mixed-cation-anion approaches "
    "[@Min2019].",
    title="No efficiency-stability trade-off with MDACl2",
)

# -----------------------------------------------------------------------------
# Stabilization mechanisms - supported via prior art
# -----------------------------------------------------------------------------

conclusion_alpha_stabilization = claim(
    "MDACl2 doping at 3.8 mol% effectively stabilizes the alpha-phase of FAPbI3 "
    "without MA, Cs, or Br, preserving the inherent narrow bandgap of pristine "
    "FAPbI3 (1.49 eV vs 1.53 eV for MAPbBr3 control). The stabilization mechanisms "
    "include H-bonding, tolerance factor optimization, entropic stabilization, and "
    "interstitial Cl- lattice strain relief. This enables the highest reported "
    "performance for mp-TiO2-based PSCs: certified PCE of 23.73% and record JSC "
    "of 26.70 mA/cm2, along with exceptional operational stability (90% PCE "
    "retention after 600 hours MPP tracking under full sunlight) [@Min2019].",
    title="MDACl2 stabilizes alpha-FAPbI3 with high efficiency and stability",
)

conclusion_no_tradeoff = claim(
    "The MDACl2 approach resolves the long-standing efficiency-stability trade-off "
    "in FAPbI3-based PSCs: prior mixed-cation methods (MA, Cs, Br) improved "
    "stability at the cost of bandgap widening (reducing JSC) or thermal instability "
    "(MA evaporation). MDACl2 achieves both the highest certified efficiency and "
    "the best stability reported for this class of devices, without any of these "
    "adulterants. This work demonstrates that the inherent bandgap of alpha-FAPbI3 "
    "can be fully utilized in stable, high-efficiency PSCs [@Min2019].",
    title="MDACl2 eliminates the efficiency-stability trade-off in FAPbI3 PSCs",
)

__all__ = [
    "stabilization_mechanism_h_bonding",
    "stabilization_mechanism_entropic",
    "stabilization_mechanism_tolerance_factor",
    "stabilization_mechanism_cl_interstitial",
    "v_fa_defects_shallow",
    "phase_stability_summary",
    "cl_interface_photostability",
    "photostability_mechanism",
    "literature_comparison",
    "aberration_free_stability",
    "conclusion_alpha_stabilization",
    "conclusion_no_tradeoff",
]