# CLAUDE Guide for `packages/`

This directory contains one Gaia package per paper. Always operate inside one concrete subpackage directory, never from `/personal/pvsk-gaia-repo` or `/personal/pvsk-gaia-repo/packages`.

Example:

```bash
cd /personal/pvsk-gaia-repo/packages/pvsk2013-gaia
```

For every paper package, execute the workflow in this exact order:

1. `/gaia:formalization`
2.  
3. `gaia compile`
4. `gaia check`
5. `/gaia:review`
6. `gaia infer --depth 1`
7. `/gaia:review`
8. `gaia render --target github`
9. `gaia render --target docs`
10. `gaia starmap`
11. `/gaia:publish`

Do not skip, reorder, or merge steps. If a step fails, fix the current package and rerun that same step before continuing.

Use the local Gaia checkout when running shell commands:

```bash
PYTHONPATH=/personal/Gaia /home/hwz/miniconda3/bin/gaia <command>
```

Do not create package-local virtual environments, and do not run `uv add gaia-lang`.
