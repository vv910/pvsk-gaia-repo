"""
Density functional theory studies -- computational methods and predictions.

Module covers DFT simulation methods, molecular dynamics, and key predictions
about passivator behavior from Lin et al., Nature 2022.
"""

from gaia.lang import claim, setting, question, support, infer

# Passivators studied
three_ammonium_cations = claim(
    "Three aromatic ammonium cations were selected for study: phenethylammonium (PEA), "
    "phenylammonium (PA), and 4-trifluoromethyl-phenylammonium (CF3-PA).",
    title="Three passivators studied",
)

electrostatic_potential_ordering = claim(
    "The electrostatic potentials (phi_max) at the -NH3+ side follow the order: "
    "phi_max,PEA < phi_max,PA < phi_max,CF3-PA, with CF3-PA having the highest electropositivity "
    "at the ammonium group.",
    title="Electrostatic potential ordering",
    metadata={"figure": "artifacts/images/051f8d42fdc4e837bedee8f5088cd1e6e2dbd96c7d94cccd7abee36cbef198d0.jpg",
              "caption": "Fig. 1a | Gaussian calculated electrostatic potentials showing increasing electropositivity from PEA to PA to CF3-PA."},
)

# Molecular dynamics simulations
cf3_pa_complete_adsorption = claim(
    "Ab initio molecular dynamics simulations at 400 K (perovskite crystallization temperature) "
    "show that CF3-PA has the strongest tendency to anchor on the perovskite surface, with all "
    "16 cations adsorbed completely on the surface in simulation.",
    title="CF3-PA complete adsorption at 400K",
    metadata={"figure": "artifacts/images/7f0ef0c477217aed6cee3a7329b71b13396930050c4c6d2fcda9650611ac4dee.jpg",
              "caption": "Fig. 1c,d | Ab initio MD snapshots showing complete CF3-PA adsorption at 400K."},
)

pea_pa_incomplete_adsorption = claim(
    "In comparison, one PA cation and three PEA cations are not adsorbed into the A-site "
    "vacancies at 400 K, and iodide ions are observed to escape from the surface in PA and PEA cases.",
    title="PEA and PA incomplete adsorption",
    metadata={"source": "artifacts/full.md"},
)

cf3_pa_suppresses_iodine_vacancies = claim(
    "CF3-PA not only increases the probability of adsorbed ammonium cations on the perovskite "
    "grain surface but also suppresses the formation of iodine vacancies on the surface at "
    "elevated temperatures, which may also suppress the formation of iodine interstitial defects.",
    title="CF3-PA suppresses iodine vacancy formation",
)

# Binding energies
cf3_pa_strongest_binding = claim(
    "The binding energies (Eb) between CF3-PA and acceptor-type defects on the perovskite grain "
    "surface are highest compared to PA and PEA, due to the highly electronegative fluorine atom "
    "in CF3-PA withdrawing electron density strongly from neighboring atoms, leaving higher "
    "electropositivity at the -NH3+ side for enhanced binding with negatively charged defects.",
    title="CF3-PA has strongest binding with acceptor defects",
    metadata={"figure": "artifacts/images/4e553fdfc36c975aeb4f3022d832d3abf8261c07e8b923c191f4e63550ffd58.jpg",
              "caption": "Fig. 1e | Binding energy between passivators and various acceptor-like defects."},
)

# Electronic structure predictions
deep_in_gap_states_eliminated = claim(
    "The deep in-gap states from I_Sn and I_Pb antisite defects are eliminated upon CF3-PA "
    "passivation.",
    title="Deep in-gap states eliminated by CF3-PA",
)

sn_vacancy_formation_increased = claim(
    "CF3-PA passivation is predicted to increase the defect formation energy of the Sn vacancy "
    "(V_Sn), reducing the numbers of vacancies.",
    title="CF3-PA increases Sn vacancy formation energy",
)

donor_defect_reduction = claim(
    "CF3-PA passivation also reduces the formation of donor-type defects.",
    title="CF3-PA reduces donor-type defects",
)

# Reasoning strategies
strat_electrostatic_rationale = support(
    [electrostatic_potential_ordering],
    cf3_pa_strongest_binding,
    reason="The electrostatic potential ordering (phi_max,PEA < phi_max,PA < phi_max,CF3-PA) indicates "
           "CF3-PA has the highest electropositivity at the -NH3+ side, which enhances binding with "
           "negatively charged acceptor defects on the perovskite surface.",
    prior=0.8,
)

strat_md_adsorption_prediction = support(
    [electrostatic_potential_ordering],
    cf3_pa_complete_adsorption,
    reason="Ab initio molecular dynamics at crystallization temperature (400 K) directly simulates "
           "the dynamic adsorption process and shows CF3-PA achieves complete surface coverage, "
           "consistent with its higher electrostatic potential.",
    prior=0.8,
)

strat_defect_elimination = support(
    [cf3_pa_strongest_binding],
    deep_in_gap_states_eliminated,
    reason="Stronger binding of CF3-PA to surface defects eliminates the deep in-gap states "
           "associated with I_Sn and I_Pb antisite defects.",
    prior=0.8,
)

strat_sn_vacancy = support(
    [cf3_pa_strongest_binding],
    sn_vacancy_formation_increased,
    reason="The strong binding of CF3-PA with Sn vacancies increases the defect formation energy, "
           "making vacancies less likely to form.",
    prior=0.8,
)

__all__ = [
    "three_ammonium_cations",
    "electrostatic_potential_ordering",
    "cf3_pa_complete_adsorption",
    "pea_pa_incomplete_adsorption",
    "cf3_pa_suppresses_iodine_vacancies",
    "cf3_pa_strongest_binding",
    "deep_in_gap_states_eliminated",
    "sn_vacancy_formation_increased",
    "donor_defect_reduction",
]