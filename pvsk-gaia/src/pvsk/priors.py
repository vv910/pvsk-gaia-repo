"""
Priors for independent synthesis claims.

Foreign claims imported from paper packages cannot be assigned priors from this
package; Gaia requires package priors to target Knowledge objects declared by
the current package. Their beliefs are supplied by dependency packages during
`gaia infer . --depth 1`.

The current synthesis-layer claims, including induction laws, mechanism nodes,
tension nodes, normalized evidence nodes, and final conclusions, are all derived
by explicit strategies. Their beliefs should therefore come from BP propagation
and strategy warrant priors, not from additional local claim priors.
"""


PRIORS: dict = {}
