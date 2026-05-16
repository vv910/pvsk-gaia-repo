"""Reasoning strategies connecting claims for R2R perovskite solar cell research."""

from gaia.lang import (
    claim,
    setting,
    support,
    infer,
    contradiction,
    complement,
)

# Import claims and settings from package modules
from .motivation import (
    lab_scale_limitation,
    vacuum_electrode_cost,
    commercial_tce_cost,
    r2r_promise,
    manufacturing_challenge,
    pfsd_demonstration,
    main_question,
    cost_prediction,
)

from .s2_pfsd import (
    pfsd_technique_description,
    pfsd_advantage,
    shallow_angle_blowing,
    edge_blowing_result,
    xrd_analysis,
    sem_improvement,
    humidity_tolerance,
    pfsd_record_pce,
)

from .s3_automated import (
    carbon_electrode_replacement,
    previous_r2r_cell_pce,
    high_throughput_capability,
    throughput_example,
    maistoi_ratio_effect,
    thicker_film_behavior,
    composition_dependence,
    htab_p3ht_introduction,
    htab_passivation,
    p3ht_heating_requirement,
    htab_p3ht_outperforms,
    reliable_production,
    best_cell_performance,
    film_thickness_range,
)

from .s4_modules import (
    module_scalability,
    five_channel_deposition,
    carbon_ink_deposition,
    silver_grid_design,
    carbon_sheet_resistance,
    module_active_area,
    module_gff,
    module_performance,
)

from .s5_cost import (
    cost_model_development,
    sequence_a_description,
    sequence_b_description,
    sequence_c_description,
    cost_fraction_sequence_a,
    cost_fraction_sequence_b,
    production_cost_area,
    production_cost_power,
    cost_reduction_achieved,
    market_position,
    future_improvement_needed,
    future_cost_potential,
)

from .s6_methods import (
    ec_binder,
    carbon_pigment,
    pgmesa_solver,
    two_stage_ink_prep,
    five_stripe_flow_rates,
)

from .conclusions import (
    first_demo_conclusion,
    carbon_ink_achievement,
    throughput_system,
    cell_record,
    module_record,
    cost_conclusion,
    future_direction,
)

# =============================================================================
# STRATEGIES FOR MOTIVATION SECTION
# =============================================================================

strat_r2r_promise = support(
    [lab_scale_limitation, vacuum_electrode_cost],
    r2r_promise,
    reason="The gap between lab-scale efficiency records and commercially scalable production, combined with the high cost of vacuum-processed electrodes, makes R2R manufacturing attractive for flexible PeSCs offering high specific power for emerging applications [@Weerasinghe2024].",
    prior=0.5,
)

strat_manufacturing_challenge = support(
    [r2r_promise],
    manufacturing_challenge,
    reason="While R2R manufacturing offers throughput advantages, the continuous movement of flexible plastic substrates imposes time and temperature constraints that must be addressed for successful perovskite deposition [@Weerasinghe2024].",
    prior=0.5,
)

strat_pfsd_demonstration = support(
    [manufacturing_challenge],
    pfsd_demonstration,
    reason="The PFSD technique was developed to address R2R processing challenges, enabling R2R deposition of ETL, perovskite, and HTL with up to 11% PCE, demonstrating feasibility of R2R PeSC fabrication [@Weerasinghe2024].",
    prior=0.5,
)

# =============================================================================
# STRATEGIES FOR PFSD TECHNIQUE
# =============================================================================

strat_pfsd_advantage = support(
    [pfsd_technique_description],
    pfsd_advantage,
    reason="The amorphous precursor behavior allows rapid conversion to perovskite when additional organic cation is deposited, without requiring additive removal, making the process suitable for R2R time constraints [@Weerasinghe2024].",
    prior=0.5,
)

strat_shallow_angle = support(
    [pfsd_technique_description],
    shallow_angle_blowing,
    reason="The PFSD technique's requirement for controlled film formation motivates the development of shallow-angle blowing as a scalable approach to control gas flow over large areas by adjusting the angle of incidence using the roller geometry [@Weerasinghe2024].",
    prior=0.5,
)

strat_edge_blowing_result = support(
    [shallow_angle_blowing, pfsd_advantage],
    edge_blowing_result,
    reason="The shallow-angle blowing prevents deformation of SD-coated wet films before solidification, producing an amorphous intermediate layer that converts rapidly and completely to perovskite upon MAI deposition, resulting in mirror-like films under 40-50% RH ambient conditions [@Weerasinghe2024].",
    prior=0.5,
)

strat_xrd_analysis = support(
    [edge_blowing_result],
    xrd_analysis,
    reason="XRD analysis of edge-blown films shows no PbI₂ crystals, indicating the intermediate layer converts completely to perovskite without ion migration or inhomogeneous local concentration [@Weerasinghe2024].",
    prior=0.5,
)

strat_sem_improvement = support(
    [edge_blowing_result],
    sem_improvement,
    reason="SEM images confirm more homogenous films with compact grains in shallow-angle-blown samples compared to right-angle-blown samples, validating improved film morphology from the technique [@Weerasinghe2024].",
    prior=0.5,
)

strat_humidity_tolerance = support(
    [edge_blowing_result, sem_improvement],
    humidity_tolerance,
    reason="The improved film quality from shallow-angle blowing enhances both device performance reliability and humidity tolerance during R2R processing under ambient conditions [@Weerasinghe2024].",
    prior=0.5,
)

strat_pfsd_record_pce = support(
    [pfsd_advantage, humidity_tolerance],
    pfsd_record_pce,
    reason="Further PFSD optimization with vacuum-deposited Au electrodes achieved up to 17.9% PCE, demonstrating the technique's capability to produce high-efficiency R2R devices when combined with conventional electrodes [@Weerasinghe2024].",
    prior=0.5,
)

# =============================================================================
# STRATEGIES FOR AUTOMATED FABRICATION
# =============================================================================

strat_carbon_replacement = support(
    [vacuum_electrode_cost],
    carbon_electrode_replacement,
    reason="The high cost of vacuum-processed Au electrodes and incompatibility with R2R lines motivated the development of perovskite-friendly carbon inks as replacement electrodes [@Weerasinghe2024].",
    prior=0.5,
)



strat_throughput_example = support(
    [high_throughput_capability],
    throughput_example,
    reason="The platform successfully produced and tested 1600 PeSCs with 20 different deposition parameter combinations in one day, demonstrating utility for rapid optimization [@Weerasinghe2024].",
    prior=0.5,
)

strat_maistoi_ratio = support(
    [throughput_example],
    maistoi_ratio_effect,
    reason="Analysis of 80 cells per condition shows that stoichiometric MAI content yields optimal performance in the FA₀.₄₅MA₀.₅₅PbI₃ system, with thinnest condition (16 μL min⁻¹) showing best performance and rapid decline with excess MAI or PbI₂ [@Weerasinghe2024].",
    prior=0.5,
)

strat_thicker_film = support(
    [throughput_example],
    thicker_film_behavior,
    reason="Thicker films show composition-dependent behavior: MAI-deficient films exhibit better FF with narrow variation, while excess MAI produces higher J_sc, demonstrating SD coating's quantitative control capability [@Weerasinghe2024].",
    prior=0.5,
)

strat_composition_dependence = support(
    [maistoi_ratio_effect, thicker_film_behavior],
    composition_dependence,
    reason="SD coating's precise material control enables systematic variation of MAI content from cation-deficient through stoichiometric to excessive compositions, revealing performance trends that guide optimization [@Weerasinghe2024].",
    prior=0.5,
)

strat_htab_p3ht_intro = support(
    [htab_p3ht_outperforms],
    htab_p3ht_introduction,
    reason="The HTAB-P3HT HTL system was introduced to improve fully R2R-fabricated cells, combining HTAB surface passivation with P3HT's self-assembly properties for enhanced performance [@Weerasinghe2024].",
    prior=0.5,
)



strat_htab_outperforms = support(
    [htab_passivation, p3ht_heating_requirement],
    htab_p3ht_outperforms,
    reason="The HTAB-P3HT HTL outperforms PPDT2FBT with higher device performance and narrower histogram distribution, demonstrating improved reliability from the combined passivation and molecular self-assembly approach [@Weerasinghe2024].",
    prior=0.5,
)

strat_reliable_production = support(
    [htab_p3ht_outperforms],
    reliable_production,
    reason="Testing in uncontrolled ambient conditions (~60% RH) confirms reliable ~13% average PCE production regardless of humidity, with best results at 30-40% RH, validating manufacturing robustness [@Weerasinghe2024].",
    prior=0.5,
)

strat_film_thickness = support(
    [throughput_example],
    film_thickness_range,
    reason="Three PbI₂ conditions produced perovskite layers 600-1000 nm thick, somewhat thicker than vacuum-deposited devices due to absence of mirror effect from carbon back electrode [@Weerasinghe2024].",
    prior=0.5,
)

strat_best_cell = support(
    [htab_p3ht_outperforms, reliable_production, film_thickness_range],
    best_cell_performance,
    reason="The best-performing HTAB-P3HT device achieved 15.5% PCE (19.9 mA cm⁻² J_sc, 76.1% FF, 1.02 V V_oc), with IPCE-calculated current (19.4 mA cm⁻²) showing good agreement, establishing record for fully R2R-fabricated cells [@Weerasinghe2024].",
    prior=0.5,
)

# =============================================================================
# STRATEGIES FOR MODULES
# =============================================================================

strat_module_scale = support(
    [best_cell_performance],
    module_scalability,
    reason="Optimized cell parameters were directly scaled to module production using multi-channel SD heads and larger substrate widths, demonstrating seamless translation from cell to module fabrication [@Weerasinghe2024].",
    prior=0.5,
)

strat_five_channel = support(
    [module_scalability],
    five_channel_deposition,
    reason="The five-channel SD head simply multiplied single-stripe flow rates by five: 100, 300, 140, 92, and 600 μL min⁻¹ for PbI₂:FAI, MAI, HTAB, P3HT, and carbon inks respectively, maintaining process consistency across module width [@Weerasinghe2024].",
    prior=0.5,
)

strat_carbon_ink_deposition = support(
    [carbon_electrode_replacement],
    carbon_ink_deposition,
    reason="RG coating was used for carbon ink deposition as a scalable R2R technique, with modules completed by R2R screen printing silver paste for charge collection and interconnection [@Weerasinghe2024].",
    prior=0.5,
)

strat_carbon_sheet_resistance = support(
    [carbon_ink_deposition],
    carbon_sheet_resistance,
    reason="The carbon layer's ~800 Ω sq⁻¹ sheet resistance is too high for efficient charge collection, necessitating additional silver grid patterns to achieve adequate conductivity [@Weerasinghe2024].",
    prior=0.5,
)

strat_silver_grid_design = support(
    [carbon_sheet_resistance],
    silver_grid_design,
    reason="A 0.2 mm line with 180 mesh screen provided consistently printable finest pattern, achieving minimal coverage while maintaining conductivity exceeding front electrode for efficient charge collection [@Weerasinghe2024].",
    prior=0.5,
)

strat_module_area = support(
    [five_channel_deposition],
    module_active_area,
    reason="Each strip cell (~1.1 cm × 9.0 cm = ~10 cm²) combined with five series-connected stripes yields ~50 cm² active module area using the scaled-up SD coating process [@Weerasinghe2024].",
    prior=0.5,
)

strat_module_gff = support(
    [module_active_area],
    module_gff,
    reason="The stripe-pattern approach with 2 mm gaps results in 75% GFF, lower than laser-scribed 99% GFF but preferable for high-throughput cost-effective manufacturing where laser scribing is unsuitable [@Weerasinghe2024].",
    prior=0.5,
)

strat_module_performance = support(
    [silver_grid_design, module_gff],
    module_performance,
    reason="Fully R2R-fabricated modules achieved up to 11.0% PCE (192 mA, 62.3% FF, 4.59 V V_oc reverse scan) and 9.96% forward scan PCE. Lower efficiency than cells results from TCE resistance and screen-printing solvent damage [@Weerasinghe2024].",
    prior=0.5,
)

# =============================================================================
# STRATEGIES FOR COST ANALYSIS
# =============================================================================


strat_seq_a = support(
    [vacuum_electrode_cost, commercial_tce_cost],
    sequence_a_description,
    reason="Sequence A (vacuum-deposited Au) represents the high-cost, high-performance baseline where Au electrode equipment and TCE are the dominant cost components [@Weerasinghe2024].",
    prior=0.5,
)

strat_seq_b = support(
    [carbon_electrode_replacement, commercial_tce_cost],
    sequence_b_description,
    reason="Sequence B replaces vacuum electrodes with printed carbon, significantly reducing back electrode cost and leaving only TCE and encapsulation as high-cost components [@Weerasinghe2024].",
    prior=0.5,
)

strat_seq_c = support(
    [sequence_b_description],
    sequence_c_description,
    reason="Sequence C (not demonstrated) proposes eliminating remaining high-cost components (commercial TCEs and silver grids) to achieve further cost reductions toward ultra-low-cost manufacturing [@Weerasinghe2024].",
    prior=0.5,
)

strat_cost_fraction_a = support(
    [sequence_a_description],
    cost_fraction_sequence_a,
    reason="In Sequence A, gold material plus R2R evaporator equipment purchase and running costs are the highest cost component, followed by commercial TCE, with encapsulation and HTL as secondary material costs [@Weerasinghe2024].",
    prior=0.5,
)

strat_cost_fraction_b = support(
    [sequence_b_description],
    cost_fraction_sequence_b,
    reason="In Sequence B, the significant reduction in back electrode cost leaves commercial TCE and encapsulation materials as the only two high-cost components, substantially altering the cost structure [@Weerasinghe2024].",
    prior=0.5,
)

strat_production_cost_area = support(
    [sequence_a_description, sequence_b_description, sequence_c_description],
    production_cost_area,
    reason="Cost modeling shows Seq. B has lower production cost per m² than Seq. A, and Seq. C potentially lower still, demonstrating economic advantage of printed carbon electrodes [@Weerasinghe2024].",
    prior=0.5,
)

strat_production_cost_power = support(
    [production_cost_area, best_cell_performance, module_performance],
    production_cost_power,
    reason="Using best efficiencies (17.9% Seq. A, 15.5% Seq. B, 10% Seq. C), Seq. B projects below 1 USD/W_p and Seq. C below 0.5 USD/W_p, representing major reduction from previous ~1.5 USD/W_p estimates while still above Si at <0.30 USD/W_p [@Weerasinghe2024].",
    prior=0.5,
)

strat_cost_reduction = support(
    [production_cost_power],
    cost_reduction_achieved,
    reason="The achieved cost reduction stems from similar or lower $/m² costs combined with higher recorded efficiencies compared to previous R2R PeSC cost estimates, though still not competitive with mass-produced crystalline Si [@Weerasinghe2024].",
    prior=0.5,
)

strat_market_position = support(
    [module_performance, cost_prediction],
    market_position,
    reason="R2R PeSCs at >10% PCE could compete in portable PV markets where form factor advantages matter. The 11% R2R module demonstration represents significant commercial progress [@Weerasinghe2024].",
    prior=0.5,
)

strat_future_improvement = support(
    [silver_grid_design, market_position],
    future_improvement_needed,
    reason="Printed silver grids face corrosion issues unsuitable for long-term commercial operation. Developing highly conductive perovskite-friendly carbon ink could enable efficient silver-free modules, addressing this critical reliability limitation [@Weerasinghe2024].",
    prior=0.5,
)

strat_future_cost = support(
    [sequence_c_description],
    future_cost_potential,
    reason="Supplementary analysis shows ~5 USD/m² module cost (excluding encapsulation) achievable by eliminating remaining high-cost components, indicating substantial further cost reduction pathway [@Weerasinghe2024].",
    prior=0.5,
)

# =============================================================================
# STRATEGIES FOR CONCLUSIONS
# =============================================================================

strat_first_demo = support(
    [pfsd_demonstration, carbon_electrode_replacement, module_performance],
    first_demo_conclusion,
    reason="This work demonstrates the world-first fully R2R-fabricated PeSC modules including back electrodes on commercial substrates, achieved through PFSD technique, perovskite-friendly carbon inks, and R2R-compatible processes [@Weerasinghe2024].",
    prior=0.5,
)

strat_carbon_ink_achievement = support(
    [carbon_electrode_replacement, carbon_ink_deposition],
    carbon_ink_achievement,
    reason="Development of perovskite-friendly carbon ink successfully replaces vacuum-processed metal electrodes (highest-cost PeSC component), enabling high-throughput vacuum-free R2R fabrication of perovskite cells using only roll-to-roll processes [@Weerasinghe2024].",
    prior=0.5,
)

strat_throughput_system = support(
    [high_throughput_capability, throughput_example],
    throughput_system,
    reason="Automated R2R fabrication and testing systems enable thousands of research cells daily, taking full advantage of high-throughput deposition methods to rapidly iterate and improve R2R experimentation [@Weerasinghe2024].",
    prior=0.5,
)

strat_cell_record = support(
    [best_cell_performance, pfsd_advantage, htab_p3ht_outperforms],
    cell_record,
    reason="Optimization of PFSD process and HTAB-P3HT HTL configuration enabled fully R2R-fabricated cells achieving 15.5% PCE, establishing record efficiency for fully roll-to-roll fabricated perovskite solar cells to date [@Weerasinghe2024].",
    prior=0.5,
)

strat_module_record = support(
    [module_performance, module_scalability],
    module_record,
    reason="First fully R2R-printed perovskite solar modules with 11% PCE (~50 cm² active area) were demonstrated with all developments considering upscaling requirements, marking significant milestone toward commercial manufacturing [@Weerasinghe2024].",
    prior=0.5,
)

strat_cost_conclusion = support(
    [production_cost_power, future_cost_potential],
    cost_conclusion,
    reason="Cost modeling predicts ~0.7 USD/W_p manufacturing cost with pathway to substantial further reduction by replacing remaining high-cost components, demonstrating significant progress toward low-cost at-scale commercial manufacturing [@Weerasinghe2024].",
    prior=0.5,
)

strat_future_direction = support(
    [future_improvement_needed, cost_prediction],
    future_direction,
    reason="Next steps include exploring high-value PV markets at predicted costs while addressing remaining cost barriers, with key development being highly conductive perovskite-friendly carbon ink to enable efficient silver-free modules for commercial longevity [@Weerasinghe2024].",
    prior=0.5,
)

# =============================================================================
# STRATEGIES FOR METHODS (Supporting background for conclusions)
# =============================================================================


strat_stripe_flow = support(
    [five_channel_deposition],
    five_stripe_flow_rates,
    reason="Module fabrication multiplied single-cell flow rates by five for the five-channel SD head: PbI₂:FAI (100), MAI (300), HTAB (140), P3HT (92), carbon (600) μL min⁻¹, maintaining coating consistency across module width [@Weerasinghe2024].",
    prior=0.5,
)

# =============================================================================
# CONTRADICTIONS (None needed - all claims are consistent)
# =============================================================================

__all__ = [
    # Motivation strategies
    "strat_r2r_promise",
    "strat_manufacturing_challenge",
    "strat_pfsd_demonstration",
    # PFSD strategies
    "strat_pfsd_technique",
    "strat_pfsd_advantage",
    "strat_shallow_angle",
    "strat_edge_blowing_result",
    "strat_xrd_analysis",
    "strat_sem_improvement",
    "strat_humidity_tolerance",
    "strat_pfsd_record_pce",
    # Automated fabrication strategies
    "strat_carbon_replacement",
    "strat_previous_r2r",
    "strat_throughput_platform",
    "strat_throughput_example",
    "strat_maistoi_ratio",
    "strat_thicker_film",
    "strat_composition_dependence",
    "strat_htab_p3ht_intro",
    "strat_htab_passivation",
    "strat_p3ht_heating",
    "strat_htab_outperforms",
    "strat_reliable_production",
    "strat_film_thickness",
    "strat_best_cell",
    # Module strategies
    "strat_module_scale",
    "strat_five_channel",
    "strat_carbon_ink_deposition",
    "strat_carbon_sheet_resistance",
    "strat_silver_grid_design",
    "strat_module_area",
    "strat_module_gff",
    "strat_module_performance",
    # Cost strategies
    "strat_cost_model",
    "strat_seq_a",
    "strat_seq_b",
    "strat_seq_c",
    "strat_cost_fraction_a",
    "strat_cost_fraction_b",
    "strat_production_cost_area",
    "strat_production_cost_power",
    "strat_cost_reduction",
    "strat_market_position",
    "strat_future_improvement",
    "strat_future_cost",
    # Conclusion strategies
    "strat_first_demo",
    "strat_carbon_ink_achievement",
    "strat_throughput_system",
    "strat_cell_record",
    "strat_module_record",
    "strat_cost_conclusion",
    "strat_future_direction",
    # Methods strategies
    "strat_ink_prep",
    "strat_stripe_flow",
]