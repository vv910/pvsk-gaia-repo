"""
s5_results.py - Scalable printed large-area modules results.

This module covers:
- Slot-die printing for large-area modules
- Large module efficiencies
- Scalability demonstration
"""

from gaia.lang import claim, setting

# Scalable manufacturing strategy
scalable_manufacturing = claim(
    "Scalable manufacturing strategy for large-size PSMs uses slot-die printing to "
    "deposit both large-scale perovskite and 2D passivation layers. This demonstrates "
    "the compatibility of the DABr/FABr passivation approach with printing technology "
    "for commercial fabrication [@Li2024].",
    title="Slot-die printing for scalable PSM fabrication",
    figure="artifacts/images/fig5.png",
)

# Printed 30x30 cm module photograph
module_photograph = claim(
    "Photograph shows printed 30 cm x 30 cm small module demonstrating the "
    "scalability of the manufacturing process. Detailed designs for 20cmx20cm and "
    "30cmx30cm PSMs are shown in Supplementary Figures 33 and 34 [@Li2024].",
    title="30x30 cm module photograph",
)

# Laser scribing for GFF
laser_scribing_gff = claim(
    "Careful modulation of laser scribing process for P1, P2, and P3 patterns enables "
    "high geometric filling factor (GFF) of ~96% for large PSMs. This maximizes the "
    "active area utilization in the module design [@Li2024].",
    title="Laser scribing achieves 96% GFF",
)

# 20x20 cm sub-module performance
module_20x20 = claim(
    "20 cm x 20 cm sub-module with series connection of 26 subcells achieves champion "
    "aperture-area efficiency of 18.90% (aperture area 310 cm2). This demonstrates "
    "successful upscaling of the DABr/FABr passivation strategy to large-area modules [@Li2024].",
    title="18.90% efficiency for 20x20 cm sub-module (310 cm2)",
)

# 30x30 cm small module performance
module_30x30 = claim(
    "30 cm x 30 cm small module with series connection of 42 subcells achieves champion "
    "aperture-area efficiency of 17.59% (aperture area 802 cm2). This confirms the "
    "feasibility of the uniform high n-value 2D phase capping layer for commercial "
    "manufacturing of large PSMs [@Li2024].",
    title="17.59% efficiency for 30x30 cm module (802 cm2)",
)

# Efficiency loss per tenfold magnification
efficiency_scaling = claim(
    "The small-size device (0.14 cm2) achieves 25.61% PCE, large-size device (1.04 cm2) "
    "achieves 24.62%, and mini-module (13.44 cm2) achieves 23.60%. This demonstrates "
    "efficiency loss of <5% per ten times magnification in active area, showing good "
    "scalability of the passivation strategy [@Li2024].",
    title="Less than 5% efficiency loss per tenfold area increase",
)

# Active area vs aperture area distinction
active_vs_aperture = claim(
    "Active-area efficiency (PCE_ac) refers to the area of the actual perovskite solar "
    "cell active layer, while aperture-area efficiency (PCE_ap) refers to the total "
    "area including non-active areas like dead zones between cells in a module. "
    "For mini-modules with GFF ~96%, the difference between PCE_ac and PCE_ap is small [@Li2024].",
    title="Active-area vs aperture-area efficiency distinction",
)

# Slot-die printing parameters for perovskite
slot_die_perovskite_params = claim(
    "For perovskite slot-die printing: 1 M concentration in 2-Me, syringe pump 0.2 ml/s, "
    "slot-die head with 10 micrometer internal shim, gap height 110 micrometer, "
    "coating speed 2 mm/s, air knife with N2 pressure 0.35 MPa. Annealing at 100 C "
    "for 1 h then 120 C for 1.5 h in ambient air [@Li2024].",
    title="Slot-die printing parameters for perovskite",
)

# Slot-die printing parameters for 2D layer
slot_die_2d_params = claim(
    "For 2D layer slot-die printing: 5 mM DABr/FABr solution, syringe pump 0.2 ml/s, "
    "gap height 130 micrometer, coating speed 4 mm/s. Annealing at 100 C for 5 min "
    "to form 2D perovskite passivation layer. Spiro-OMeTAD also slot-die printed "
    "until fully covered [@Li2024].",
    title="Slot-die printing parameters for 2D passivation layer",
)

# Commercial manufacturing potential
commercial_potential = claim(
    "The homogenized interface low-dimensional structure engineering using DABr/FABr "
    "passivation offers significant potential for accelerating commercialization of "
    "efficient and stable PSMs. The compatibility with slot-die printing demonstrates "
    "scalability to manufacturing-relevant processes [@Li2024].",
    title="Strategy holds potential for PSM commercialization",
)

# Module stability
module_stability = claim(
    "Encapsulated solar mini-modules with DABr/FABr passivation show remarkable "
    "operational stability under continuous light illumination. T80 lifetime exceeds "
    "2000 h at MPPT, indicating excellent stability suitable for commercial applications [@Li2024].",
    title="Modules maintain stability under operational conditions",
)

# Summary of scaling achievements
scaling_summary = claim(
    "Using uniform phase-pure n=2 2D perovskite passivation with DABr/FABr treatment, "
    "champion efficiencies achieved: 25.61% (small device), 24.62% (large device), "
    "23.60% (mini-module), 18.90% (20x20 cm sub-module), 17.59% (30x30 cm small module). "
    "All show <5% efficiency loss per tenfold area increase, demonstrating excellent "
    "scalability from lab cells to module-scale manufacturing [@Li2024].",
    title="Summary of efficiency across all device sizes",
)