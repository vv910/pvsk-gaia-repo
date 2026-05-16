# Narrative Outline

Auto-generated from the coarse reasoning graph. Sections are grouped by connectivity (high cohesion, low coupling) and ordered by topological layer. Use this as the backbone for writing narrative summaries.

## Modified conditions for best-performing devices

1. **Higher photocurrent from increased loading and light scattering ★** (prior: 0.78 → belief: 0.78)
   - → supports: best_device_performance

2. **Modified conditions for best-performing devices ★** (prior: 0.88 → belief: 0.88)
   - → supports: best_device_performance

## Layered PbI2 structure enables cation insertion

3. **Lattice energy difference drives conversion ★** (prior: 0.82 → belief: 0.82)
   - → supports: conversion_facilitation

4. **Nanoscopic morphology combined with high formation energy enhances kinetics ★** (prior: 0.85 → belief: 0.85)
   - → supports: conversion_facilitation

5. **Layered PbI2 structure enables cation insertion ★** (prior: 0.90 → belief: 0.90)
   - → supports: conversion_facilitation

## Tetragonal perovskite XRD peaks observed after conversion

6. **Flat substrate shows incomplete perovskite conversion ★** (prior: 0.85 → belief: 0.85)
   - → supports: conversion_rate_enhancement

7. **PbI2 crystal size limited to ~22 nm in nanopores ★** (prior: 0.88 → belief: 0.88)
   - → supports: conversion_rate_enhancement

8. **Tetragonal perovskite XRD peaks observed after conversion ★** (prior: 0.90 → belief: 0.90)
   - → supports: conversion_rate_enhancement

## Device retains >80% PCE after 500 hours

9. **No photodegradation observed ★** (prior: 0.85 → belief: 0.85)
   - → supports: pce_decrease_mechanism

10. **Device retains >80% PCE after 500 hours ★** (prior: 0.88 → belief: 0.88)
   - → supports: pce_decrease_mechanism

## Batch average PCE: 12.0% +/- 0.5%

11. **Batch average PCE: 12.0% +/- 0.5% ★** (prior: 0.90 → belief: 0.90)
   - → supports: reproducibility_improvement

## Sequential deposition method introduced

12. **PbI2 completely contained within TiO2 nanopores ★** (prior: 0.90 → belief: 0.90)
   - → supports: control_improvement

13. **Sequential deposition method introduced ★** (prior: 0.92 → belief: 0.92)
   - → supports: control_improvement

## IPCE peak exceeds 90% in short wavelengths

14. **APCE exceeds 90% indicating near-unity quantum yield ★** (prior: 0.90 → belief: 0.90)
   - → supports: integrated_current_match

15. **IPCE peak exceeds 90% in short wavelengths ★** (prior: 0.90 → belief: 0.90)
   - → supports: integrated_current_match

## Nanoporous confinement facilitates perovskite conversion

16. **Nanoporous confinement facilitates perovskite conversion ★** (prior: 0.50 → belief: 0.77)
   - ← infer(layered_pbi2_structure, reaction_kinetics_enhancement, thermodynamic_driving_force) [0.31 bits]

## Best device: 15.0% PCE

17. **Best device: 15.0% PCE ★** (prior: 0.50 → belief: 0.77)
   - ← infer(best_device_improvement_attributed, best_device_modification) [0.30 bits]

## Sequential method improves morphology control

18. **Nanoscopic confinement dramatically accelerates conversion ★** (prior: 0.50 → belief: 0.80)
   - ← infer(flat_substrate_incomplete_conversion, pbi2_crystal_size, perovskite_xrd_confirmed) [0.30 bits]
   - → supports: efficiency_achieved

19. **Sequential method improves morphology control ★** (prior: 0.50 → belief: 0.85)
   - ← infer(pbi2_complete_infiltration, sequential_deposition_introduced) [0.24 bits]
   - → supports: efficiency_achieved, reproducibility_improvement

## PCE decrease due to Voc and FF reduction from shunt resistance loss

20. **PCE decrease due to Voc and FF reduction from shunt resistance loss ★** (prior: 0.50 → belief: 0.82)
   - ← infer(no_photodegradation, stability_result) [0.28 bits]

## Integrated IPCE current matches measured Jsc

21. **Integrated IPCE current matches measured Jsc ★** (prior: 0.50 → belief: 0.86)
   - ← infer(apce_exceeds_90_percent, ipce_peak_value) [0.25 bits]

## Sequential method improves reproducibility

22. **15% efficiency achieved with sequential deposition ★** (prior: 0.50 → belief: 0.79)
   - ← infer(control_improvement, conversion_rate_enhancement) [0.20 bits]

23. **Sequential method improves reproducibility ★** (prior: 0.50 → belief: 0.84)
   - ← infer(control_improvement, device_batch_statistics) [0.29 bits]
