# PVSK Gaia Repository

This repository is a monorepo for PVSK Gaia knowledge packages.

## Layout

- `packages/`: one Gaia package per paper.
- `pvsk-gaia/`: cross-paper PVSK synthesis package.
- `sources/`: local parsed-paper source mirror, ignored by Git.
- `pyproject.toml`: root workspace definition for all packages.
- `uv.lock`: root workspace lock file, when uv is used.

## Dependency Model

The packages are intended to compile against the local Gaia checkout:

```bash
PYTHONPATH=/personal/Gaia gaia compile
```

Do not create per-package virtual environments. Keep package dependencies light;
the root workspace exists to organize packages, not to vendor Gaia runtime code.

## Package Data

Each paper package may include an `artifacts/` directory with parsed markdown,
figures, and a PDF symlink back to `/personal/ppt_data/PVSK发展历史`. The separate
`sources/` directory is a local mirror and is intentionally ignored.
