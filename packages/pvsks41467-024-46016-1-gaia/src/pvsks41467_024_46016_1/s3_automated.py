"""Automated, ambient, and vacuum-free device fabrication using R2R processes."""

from gaia.lang import (
    claim,
    setting,
    support,
)

# Carbon ink development
carbon_electrode_replacement = claim(
    "The discovery of R2R-printable electrodes for PeSCs has long been a critical challenge in the realisation of fully R2R-fabricated vacuum-free cells. This work developed perovskite-friendly carbon inks to replace vacuum-processed Au electrodes [@Weerasinghe2024].",
    title="Carbon ink replaces vacuum electrodes",
)

previous_r2r_cell_pce = claim(
    "The first fully R2R-fabricated PeSC was reported recently using a printed carbon electrode, achieving a PCE of 10.8%. The efficiency was significantly lower than vacuum-based counterparts, suggesting performance degradation caused by the carbon ink [@Weerasinghe2024].",
    title="Previous R2R carbon electrode achieved only 10.8%",
)

# High-throughput platform
high_throughput_capability = claim(
    "A programmable R2R SD coater was developed for unmanned operation, allowing fabrication of thousands of unique PeSCs daily. An automated R2R tester tests over ten thousand solar cells per day, with device parameters automatically calculated and saved online [@Weerasinghe2024].",
    title="High-throughput R2R fabrication and testing",
)

throughput_example = claim(
    "The high-throughput experimental platform was used to explore extensive fabrication parameters of vacuum-free PeSCs, producing and testing 1600 consecutively fabricated PeSCs with 20 deposition parameter combinations in one day [@Weerasinghe2024].",
    title="1600 PeSCs tested with 20 parameter combinations",
)

# Device optimization results
maistoi_ratio_effect = claim(
    "The devices with an MAI content close to the stoichiometric amount show better performance than others in the FA₀.₄₅MA₀.₅₅PbI₃ system. The thinnest condition (16 μL min⁻¹) shows the best performance at the stoichiometric amount and performance decreases rapidly with an excess of MAI or PbI₂ [@Weerasinghe2024].",
    title="Stoichiometric MAI content yields best performance",
)

thicker_film_behavior = claim(
    "Thicker perovskite films show more interesting behavior: MAI-deficient films show better fill factor (FF) with narrow performance variations, while films with excess MAI show higher short-circuit current (J_sc) [@Weerasinghe2024].",
    title="Thickness-dependent performance trends",
)

composition_dependence = claim(
    "The ability of SD coating to give quantitative control over the amount of material deposited allowed for the amount of MAI present in the perovskite layer to be varied from slightly cation deficient (lead-excessive composition) through to stoichiometric and slightly excessive compositions for each PbI₂ condition [@Weerasinghe2024].",
    title="Composition-dependent device performance identified",
)

# HTAB-P3HT HTL system
htab_p3ht_introduction = claim(
    "A significant improvement in fully R2R-fabricated cells was achieved by introducing a new hole-transport layer (HTL) system using poly(3-hexylthiophene) (P3HT) combined with n-hexyl trimethyl ammonium bromide (HTAB), which passivates surface traps of the perovskite layer and provides anchoring points for P3HT self-assembly [@Weerasinghe2024].",
    title="HTAB-P3HT HTL system introduced",
)

htab_passivation = claim(
    "HTAB passivates the surface traps of the perovskite layer and also provides anchoring points for the hexyl side chain of P3HT to self-assemble in the preferred molecular orientation, improving both performance and reliability [@Weerasinghe2024].",
    title="HTAB provides surface passivation and molecular anchoring",
)

p3ht_heating_requirement = claim(
    "A uniform P3HT layer was achieved by heating the substrate to 45°C, which lowers the surface tension of the polymer solution and promotes the self-assembly of P3HT on the HTAB surface. Without substrate heating, P3HT formed poor films on HTAB intermittently [@Weerasinghe2024].",
    title="Substrate heating enables uniform P3HT coating",
)

htab_p3ht_outperforms = claim(
    "The HTAB-P3HT HTL clearly outperformed PPDT2FBT HTL, with devices showing higher performance and improved reliability (narrower distribution in the histogram) [@Weerasinghe2024].",
    title="HTAB-P3HT outperforms PPDT2FBT",
)

reliable_production = claim(
    "Reliable production of PeSCs with an average PCE of approximately 13% was confirmed regardless of humidity in the lab (tested in uncontrolled ambient conditions on a day with ~60% RH). Best devices were obtained on days with low humidity (30-40% RH) [@Weerasinghe2024].",
    title="Reliable 13% average PCE across humidity conditions",
)

# Best cell performance
best_cell_performance = claim(
    "The best-performing device achieved 15.5% PCE, 19.9 mA cm⁻² J_sc, 76.1% FF, and 1.02 V V_oc under standard illumination (AM 1.5 G). The IPCE spectrum shows good agreement with a calculated current density of 19.4 mA cm⁻² [@Weerasinghe2024].",
    title="Best cell achieves 15.5% PCE",
)

film_thickness_range = claim(
    "Three PbI₂ conditions were selected to fabricate perovskite layers of about 600 nm to 1000 nm thickness. This range is somewhat thicker than typical vacuum-deposited electrode devices due to the absence of a mirror effect from the carbon-based back electrode [@Weerasinghe2024].",
    title="Perovskite film thickness 600-1000 nm",
)

__all__ = [
    "carbon_electrode_replacement",
    "previous_r2r_cell_pce",
    "high_throughput_capability",
    "throughput_example",
    "maistoi_ratio_effect",
    "thicker_film_behavior",
    "composition_dependence",
    "htab_p3ht_introduction",
    "htab_passivation",
    "p3ht_heating_requirement",
    "htab_p3ht_outperforms",
    "reliable_production",
    "best_cell_performance",
    "film_thickness_range",
]