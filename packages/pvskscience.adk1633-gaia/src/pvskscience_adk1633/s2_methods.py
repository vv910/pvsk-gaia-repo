"""
Section 2: Exploring class 1 and 2 molecule combinations.

This module covers the exploration of diammonium ligands (class 1, field-effect passivation)
and methylthio molecules (class 2, chemical passivation), and their combinations.
"""

from gaia.lang import (
    claim, setting, support, infer, compare, deduction, abduction,
    induction, analogy, extrapolation, elimination, case_analysis,
    mathematical_induction, composite, contradiction, equivalence,
    complement, disjunction, infer
)

# Import from motivation
from .motivation import methylthio_chemical_passivation

# Device architecture for screening
device_architecture = claim(
    "The device architecture used for screening diammonium ligands consists of FTO/NiOx/Me-4PACz/perovskite/passivation layer/C60/BCP/Ag [@Liu2024].",
    title="Device architecture for ligand screening",
)

# Control device PCE
control_device_pce = claim(
    "Control devices (without passivation) achieved PCEs of approximately 22.8% with active areas of 0.05 cm^2 [@Liu2024].",
    title="Control device PCE ~22.8%",
)

# EDAI2 and PDAI2 diammonium ligands improve PCE
dianmmonium_pce_improvement = claim(
    "Ethane-1,2-diammonium (EDAI2) and propane-1,3-diammonium iodide (PDAI2), with high binding energy with the perovskite surface, improved PCEs from approximately 22.8% to approximately 23.9% for devices with active areas of 0.05 cm^2 [@Liu2024].",
    title="Dianmmonium ligands improve PCE to ~23.9%",
)

# Diammonium ligands work via field-effect passivation
dianmmonium_field_effect_mechanism = claim(
    "The PCE improvement from diammonium ligands could be explained by field-effect passivation that repels minority carriers at the interface [@Liu2024].",
    title="Dianmmonium field-effect passivation mechanism",
)

# n-butylammonium iodide (BAI) chemical passivation
bai_chemical_passivation = claim(
    "n-butylammonium iodide (BAI), widely used as a chemical passivating agent, was examined as a second molecule combined with PDAI2; its addition increased PCE to approximately 24.3% compared with PDAI2 alone [@Liu2024].",
    title="BAI chemical passivation improves PCE to ~24.3%",
)

# Amylamine hydroiodide (AAI) further improves
aai_improves_baseline = claim(
    "Extending the chain length to amylamine hydroiodide (AAI) further improved the average efficiency to approximately 24.5%, providing a baseline roughly at parity with efficient previously reported inverted PSCs [@Liu2024].",
    title="AAI improves baseline to ~24.5%",
)

# Methylthio-based ammonium ligands
methylthio_synthesis = claim(
    "Methylthio-based ammonium ligands, namely 2-(methylthio)ethylamine hydroiodide (2MTEAI) and 3-(methylthio)propylamine hydroiodide (3MTPAI), were synthesized by incorporating sulfur as a donor atom in the alkyl chain to tune the electrical dipole moment [@Liu2024].",
    title="Synthesis of methylthio-based ammonium ligands",
)

# Dual passivation combinations tested
dual_combinations_improve = claim(
    "Four combinations of diammonium and methylthio molecules -- EDAI2/2MTEAI, PDAI2/2MTEAI, EDAI2/3MTPAI, and PDAI2/3MTPAI -- all showed improved PCE compared to both control devices and single-molecule passivated devices [@Liu2024].",
    title="Dual passivation combinations outperform controls",
)

# Highest PCE with PDAI2/3MTPAI
pai2_3mtpai_highest_pce = claim(
    "The highest average PCE (>25.5%) was achieved with the PDAI2/3MTPAI combination, which was selected for further investigation [@Liu2024].",
    title="PDAI2/3MTPAI achieves highest PCE >25.5%",
)

# Strategy: diammonium and methylthio combination supports high PCE
strat_dianmmonium_methylthio = support(
    [dianmmonium_pce_improvement, dianmmonium_field_effect_mechanism, methylthio_chemical_passivation],
    pai2_3mtpai_highest_pce,
    reason="Dianmmonium ligands provide field-effect passivation by repelling minority carriers, while methylthio molecules provide chemical passivation by binding to defect sites. Their combined use addresses both surface and interface recombination simultaneously, leading to the highest PCE improvement to >25.5% [@Liu2024].",
    prior=0.5,
)

__all__ = [
    "device_architecture",
    "control_device_pce",
    "dianmmonium_pce_improvement",
    "dianmmonium_field_effect_mechanism",
    "bai_chemical_passivation",
    "aai_improves_baseline",
    "methylthio_synthesis",
    "dual_combinations_improve",
    "pai2_3mtpai_highest_pce",
    "strat_dianmmonium_methylthio",
]