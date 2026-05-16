"""
S3: Cross-paper contradictions and resolutions.

Claims where pvsk2009 and pvsk2012.1 appear to conflict
or represent genuinely different conditions, requiring resolution.
"""

from gaia.lang import contradiction, complement, support

# Import from pvsk2009
from pvsk2009 import (
    durability_observation as pvsk2009_durability,
    iodide_cell_efficiency as pvsk2009_efficiency,
)

# Import from pvsk2012.1
from pvsk2012_1 import (
    stability_improvement as pvsk2012_stability,
    pce_9_7_percent as pvsk2012_pce,
)


# Contradiction: Durability vs Stability
# Kojima 2009: "photocurrent decay observed under continuous irradiation"
# Kim 2012: "PCE remained stable for 500+ hours"
#
# These appear contradictory but are not both true under the same conditions:
# - 2009 used liquid electrolyte (degrades perovskite)
# - 2012 used solid-state hole conductor (stable)
# This is a genuine contradiction only if we fail to specify the different conditions.
# Resolution: complement captures the exhaustive conditions

# The apparent contradiction
contradiction_durability_stability = contradiction(
    pvsk2009_durability,
    pvsk2012_stability,
    reason="Kojima 2009 reports photocurrent decay under continuous irradiation in liquid electrolyte cells, while Kim 2012 reports 500+ hour stability in solid-state cells. Under identical conditions (liquid electrolyte), both would be problematic; under solid-state conditions, stability holds.",
    prior=0.5,
)

# Resolution via complement: different device configurations lead to different outcomes
# The two conditions are exhaustive for perovskite PV devices:
# - liquid electrolyte configuration -> durability problems
# - solid-state configuration -> stable performance
resolution_durability_stability = complement(
    pvsk2009_durability,
    pvsk2012_stability,
    reason="The durability observation in 2009 applies to liquid electrolyte configuration; the stability observation in 2012 applies to solid-state configuration. These are exhaustive alternatives for the two main perovskite device architectures, and exactly one dominates under each condition.",
    prior=0.85,
)