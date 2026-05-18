# Analysis: pvsknature12509-gaia (Liu et al. 2013 Nature)

## Package Statistics

| Metric | Value |
|--------|-------|
| Total knowledge nodes | 103 |
| Strategies | 25 |
| Operators | 0 |
| Independent premises | 20 |
| Derived conclusions | 24 |
| Orphaned claims | 58 (mostly method descriptions) |
| Reasoning graph MI | 6.0 bits |

**Strategy type distribution:** 25 `support` strategies (all with `prior=0.5`), 0 `deduction`, 0 `abduction`, 0 `induction`.

**Claim classification:** 20 independent premises with priors (all from `priors.py`), 24 derived conclusions (belief propagated by BP), 58 orphaned (method descriptions with no downstream reasoning).

## BP Result Summary

All 20 independent premises have high belief (~prior), confirming they are well-grounded. All 24 derived conclusions have belief > 0.5, with the strongest being `planar_architecture_sufficiency` (0.77) and the weakest being `all_perovskite_multijunction` (0.61). No contradictions or abnormal resolution patterns.

**Noteworthy:**
- `threshold_15_percent` (0.64): Best device exceeds 15%, but batch average (12.3 ± 2.0%) pulls the confidence down
- `wider_bandgap_top_cell_target` (0.61) and `all_perovskite_multijunction` (0.61): Long chains with multiple inferences reduce belief
- No derived conclusions with belief < 0.5 — no broken reasoning chains

## Weak Points

| Claim | Belief | Issue |
|-------|--------|-------|
| `threshold_15_percent` | 0.64 | Best device (15.4%) + weak batch (12.3 ± 2.0%) = uncertain reproducibility |
| `wider_bandgap_top_cell_target` | 0.61 | 3-hop chain: tandem potential + infra compat → target; both intermediate steps have moderate belief |
| `all_perovskite_multijunction` | 0.61 | 2-hop chain through perovskite versatility, which itself has moderate belief from XRD structure |
| `vapour_vs_solution_fom_comparison` | 0.63 | 6-premise flat `support` — multiplicative uncertainty from combining many measurements |

**Structural concern:** The `vapour_vs_solution_fom_comparison` strategy has 6 premises in a single `support`. This creates a large multiplicative suppression (0.90^6 ≈ 0.53 effective prior), which is why the conclusion only reaches 0.63 despite strong individual measurements. A `composite` decomposition would give more transparent intermediate claims.

## Evidence Gaps

- **Diffusion length precision**: Only a lower bound (≥330 nm) is established. Time-resolved spectroscopy would give exact values.
- **Device stability**: No lifetime or degradation data reported.
- **Solution-processed baseline**: The 8.6% control may not be fully optimized, so the vapour-vs-solution efficiency gap is partially uncertain.
- **Shunt mechanism detail**: Pinholes are identified as the cause of low FF/Voc in solution devices, but the exact shunting pathway is not fully characterized.

## Contradictions

No formal `contradiction()` or `complement()` operators in this package. There are no explicit contradictions in the Liu et al. 2013 paper — the vapour and solution approaches are compared as complementary processing routes, not competing hypotheses.

## Confidence Assessment

| Tier | Belief range | Claims |
|------|-------------|--------|
| Very high | 0.85–0.95 | `high_efficiency_planar_demonstrated` (0.91), all individual Jsc/Voc/FF metrics (0.90) |
| High | 0.70–0.84 | `planar_architecture_sufficiency` (0.77), `vapour_deposition_enables_uniform_films` (0.86), `diffusion_length_lower_bound` (0.71) |
| Moderate | 0.60–0.69 | Most derived conclusions including `threshold_15_percent` (0.64), `vapour_best_PCE` (0.69) |
| Tentative | < 0.60 | None in this package |