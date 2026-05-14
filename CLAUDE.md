# PVSK Gaia Repository Instructions

This repository is a Gaia monorepo for formalizing many PVSK-related papers into Gaia knowledge packages.

The repository root is:

/personal/pvsk-gaia-repo

The repository root is a workspace root, not a Gaia knowledge package.

Do not treat /personal/pvsk-gaia-repo itself as a Gaia package.

## Repository Layout

Expected layout:

    /personal/pvsk-gaia-repo/
    ├── CLAUDE.md
    ├── pyproject.toml
    ├── uv.lock
    ├── sources/
    │   ├── paper01/
    │   │   ├── paper.md
    │   │   └── images/
    │   ├── paper02/
    │   │   ├── paper.md
    │   │   └── images/
    │   └── ...
    ├── packages/
    │   ├── pvsk-paper01-gaia/
    │   ├── pvsk-paper02-gaia/
    │   └── ...
    └── pvsk-gaia/

Meaning:

- sources/ contains raw source materials. Do not edit sources/ unless explicitly asked.
- packages/ contains one Gaia knowledge package per paper.
- pvsk-gaia/ is reserved for the final synthesis package across all paper-level packages.
- The repository root is only a workspace root.

## Most Important Rule

Never run Gaia commands against the repository root.

Do not run these from /personal/pvsk-gaia-repo:

    gaia compile .
    gaia check .
    gaia infer .
    gaia render .

Always run Gaia commands against a specific target package.

Use this pattern:

    /home/hwz/miniconda3/bin/gaia compile TARGET_PACKAGE
    /home/hwz/miniconda3/bin/gaia check TARGET_PACKAGE
    /home/hwz/miniconda3/bin/gaia check --brief TARGET_PACKAGE
    /home/hwz/miniconda3/bin/gaia check --hole TARGET_PACKAGE
    /home/hwz/miniconda3/bin/gaia infer TARGET_PACKAGE
    /home/hwz/miniconda3/bin/gaia render TARGET_PACKAGE --target github
    /home/hwz/miniconda3/bin/gaia render TARGET_PACKAGE --target docs

**Important:** The `.venv` in this repository has an incomplete Gaia installation
(missing `gaia.inquiry` module). Always use the full Gaia installation at
`/home/hwz/miniconda3/bin/gaia` instead of `uv run gaia`.

Example target package:

    packages/pvsk-paper01-gaia

Example Gaia commands:

    /home/hwz/miniconda3/bin/gaia compile packages/pvsk-paper01-gaia
    /home/hwz/miniconda3/bin/gaia check packages/pvsk-paper01-gaia
    /home/hwz/miniconda3/bin/gaia check --brief packages/pvsk-paper01-gaia
    /home/hwz/miniconda3/bin/gaia check --hole packages/pvsk-paper01-gaia
    /home/hwz/miniconda3/bin/gaia infer packages/pvsk-paper01-gaia
    /home/hwz/miniconda3/bin/gaia render packages/pvsk-paper01-gaia --target github
    /home/hwz/miniconda3/bin/gaia render packages/pvsk-paper01-gaia --target docs

## Required Variables for Every Paper Task

Before formalizing any paper, identify:

    TARGET_PACKAGE = packages/<paper-package-name>
    SOURCE_DIR = sources/<paper-source-directory>
    CITATION_KEY = <citation-key>

If the user provides these, use them exactly.

If the user gives only SOURCE_DIR, infer TARGET_PACKAGE if possible.

If the target paper is ambiguous, ask the user which source directory to use.

Only work on one TARGET_PACKAGE at a time unless the user explicitly asks for batch processing.

## Creating a New Paper Package

Each paper should have its own Gaia package under packages/.

Naming convention:

    packages/pvsk-paper01-gaia
    packages/pvsk-paper02-gaia
    packages/pvsk-paper03-gaia

Each package should contain:

    packages/pvsk-paper01-gaia/
    ├── artifacts/
    │   ├── paper.md
    │   └── images/
    ├── references.json
    ├── pyproject.toml
    ├── src/
    │   └── pvsk_paper01/
    │       ├── __init__.py
    │       └── priors.py
    └── uv.lock

When preparing a package, copy source materials into the package:

- SOURCE_DIR/paper.md should become TARGET_PACKAGE/artifacts/paper.md
- SOURCE_DIR/images/ should become TARGET_PACKAGE/artifacts/images/

Do not formalize directly from sources/. Always formalize from artifacts/ inside the target package.

## references.json

Every paper package should have a references.json file at the package root.

Minimal structure:

    {
      "Paper01": {
        "type": "article-journal",
        "title": "Replace with the real paper title"
      }
    }

Use citation syntax in claims and strategy reasons:

    [@Paper01]

The citation key must match CITATION_KEY.

If the paper metadata is available in the markdown file, fill in the real title, authors, DOI, arXiv ID, journal, and year.

## Formalization Workflow

Formalization must be incremental.

Do not write all DSL files first and only compile at the end.

Use the Gaia six-pass workflow:

1. Pass 1: Extract knowledge nodes.
2. Pass 2: Connect reasoning with draft strategies and operators.
3. Pass 3: Check completeness.
4. Pass 4: Refine strategy types.
5. Pass 5: Verify structural integrity.
6. Pass 6: Polish for standalone readability.

After each pass, run:

    /home/hwz/miniconda3/bin/gaia compile TARGET_PACKAGE
    /home/hwz/miniconda3/bin/gaia check TARGET_PACKAGE

Replace TARGET_PACKAGE with the actual package path.

Example:

    /home/hwz/miniconda3/bin/gaia compile packages/pvsk-paper01-gaia
    /home/hwz/miniconda3/bin/gaia check packages/pvsk-paper01-gaia

If compile or check fails, fix the package before moving to the next pass.

## Source Reading Rules

Read TARGET_PACKAGE/artifacts/paper.md section by section.

Use TARGET_PACKAGE/artifacts/images/ for figures.

For each paper section:

- Create or update one Python module under src/<import_name>/.
- Put Introduction or Motivation content in motivation.py.
- Put methods content in a methods module.
- Put results content in results modules.
- Put discussion or conclusion content in discussion/conclusion modules.

The module docstring should describe the paper section.

Each knowledge node should be placed in the module corresponding to where it first appears in the paper.

## Package Source Organization

Preferred structure:

    src/<import_name>/
    ├── __init__.py
    ├── motivation.py
    ├── s2_methods.py
    ├── s3_results.py
    ├── s4_discussion.py
    └── priors.py

Rules:

- __init__.py should re-export public symbols from modules.
- Only define __all__ in __init__.py.
- Do not define __all__ in submodules.
- __all__ should list the paper's core exported conclusions.
- Public claims and strategies should use descriptive variable names.
- Avoid private underscore-prefixed claims unless they are intentionally internal.
- Never manually assign .label. Labels come from Python variable names.

## Gaia DSL Imports

Use Gaia DSL objects from gaia.lang.

Typical imports:

    from gaia.lang import (
        claim,
        setting,
        question,
        support,
        compare,
        deduction,
        abduction,
        induction,
        analogy,
        extrapolation,
        elimination,
        case_analysis,
        mathematical_induction,
        composite,
        infer,
        contradiction,
        equivalence,
        complement,
        disjunction,
    )

Do not use noisy_and(). Use support() instead.

Do not use old Gaia APIs or Package context managers.

## Claim vs Setting

Use setting() for:

- mathematical definitions;
- notation;
- formal setup;
- device configuration definitions;
- experimental setup;
- fixed modeling assumptions;
- standard physical constants;
- established background principles.

Use claim() for:

- falsifiable scientific assertions;
- theoretical predictions;
- numerical results;
- experimental observations;
- method applicability assertions;
- mechanism claims;
- conclusions;
- assumptions that could be wrong.

When in doubt, use claim().

## Claim Quality Rules

Every claim must be:

- atomic: one claim expresses one proposition;
- self-contained: understandable without opening the original paper;
- judgeable: a reviewer can assess whether it is plausible;
- traceable: cite the paper with [@CITATION_KEY] when appropriate.

Avoid vague claims.

Bad claim:

    result = claim(
        "The method works well.",
        title="Method works well",
    )

Good claim:

    efficiency_improvement = claim(
        "Under the reported PVSK device configuration, the proposed interface treatment increases the measured power conversion efficiency from X% to Y% compared with the untreated control [@Paper01].",
        title="Interface treatment improves PVSK device efficiency",
    )

Do not combine unrelated facts in one claim.

Separate:

- theoretical predictions;
- experimental measurements;
- method descriptions;
- method application results;
- numerical comparisons;
- conclusions.

## Figures and Tables

Important figure and table information must be transcribed into claim content.

Do not create claims that only say “see Figure 3”.

The claim content should include the relevant quantitative values, trends, comparisons, and conditions.

Figure paths should be used as metadata for traceability.

Example:

    hysteresis_data = claim(
        "The J-V scan shows reduced hysteresis after treatment: forward scan PCE is X%, reverse scan PCE is Y%, and the hysteresis index decreases from A to B [@Paper01].",
        title="Treatment reduces J-V hysteresis",
        figure="artifacts/images/fig3.png",
    )

The figure path alone is not enough. The scientific content must be in the claim text.

## Strategy Rules

Use named public variables for all strategies.

Good:

    strat_treatment_supports_efficiency = support(
        [interface_passivation, improved_voc],
        efficiency_improvement,
        reason="The interface passivation evidence and improved open-circuit voltage jointly support the reported efficiency improvement.",
        prior=0.5,
    )

Bad:

    support([a], b)

Avoid anonymous strategies because they are hard to inspect in gaia check --brief.

**During formalization (Pass 1-6): always use `prior=0.5` for all strategies.**
Do not manually tune `prior=` to boost belief values. Let BP automatically
determine posterior beliefs. If a conclusion ends up with low belief, that
reflects a weak reasoning chain — fix the chain structure, not the prior.

**After formalization, during /gaia:review:** strategy warrant priors may be
adjusted based on reasoning quality, per the review skill guide:

| Reasoning quality             | Prior value   |
|------------------------------|--------------|
| Near-certain (rigid deduction)| 0.95-0.99   |
| Strong support               | 0.80-0.95    |
| Reliable but approximate     | 0.60-0.80    |
| Moderate confidence          | 0.40-0.60    |

## Strategy Selection

Use deduction() for strict mathematical or logical derivation.

Use support() for:

- empirical support;
- approximate reasoning;
- numerical calculations;
- method-dependent claims;
- soft implication;
- claims that are likely but not strictly entailed.

Use compare() when comparing two predictions against one observation.

Use abduction() for inference to the best explanation.

Use induction() when multiple independent observations support the same general law.

Use contradiction() when two claims cannot both be true, but both could be false.

Use complement() only when exactly one of two exhaustive alternatives must be true.

Use equivalence() when two claims have the same truth value.

Use disjunction() when at least one of several claims must be true.

Use composite() for multi-step reasoning with meaningful intermediate claims.

Use infer() only as a draft strategy or a last resort.

## Abduction Rules

For abduction, do not use the old observation-hypothesis signature.

Use the newer structure:

- support strategy for hypothesis explaining observation;
- support strategy for alternative explaining observation;
- compare strategy comparing predictions against observation;
- abduction over those strategies.

The alternative must be a real competing explanation, not a placeholder.

Alternative claims should be public and named with an alt_ prefix.

Do not use private names like _alt_xxx for abduction alternatives.

## Contradiction and Complement Rules

contradiction(a, b) means A and B cannot both be true. Both may still be false.

complement(a, b) means exactly one of A or B must be true.

Use contradiction for incompatible mechanisms or mutually inconsistent claims.

Use complement only for exhaustive binary choices.

Do not model mere tension as contradiction.

If two claims can both be true under different conditions, do not use contradiction.

## Priors

Independent claims need priors in priors.py.

Derived conclusions should not get priors.

Use gaia check --hole to identify independent claims that need priors.

priors.py should be located at:

    TARGET_PACKAGE/src/<import_name>/priors.py

Example structure:

    from .motivation import background_claim
    from .s3_results import experimental_observation

    PRIORS = {
        background_claim: (
            0.9,
            "Well-established background claim in the PVSK literature."
        ),
        experimental_observation: (
            0.85,
            "Directly reported experimental measurement with clear protocol."
        ),
    }

Prior ranges (for priors.py only, not for strategies):

- 0.85 to 0.95: well-established fact or strong experimental observation.
- 0.65 to 0.85: supported by evidence but imperfect.
- 0.40 to 0.65: tentative, single-source, method-dependent, or uncertain.
- 0.20 to 0.40: speculative or weak assumption.

**For strategies, use `prior=0.5` during formalization. After /gaia:review,
adjust inline warrant priors based on reasoning quality.**

Do not provide reason without prior, and do not provide prior without reason.

## Review Workflow

After formalization, run:

    /home/hwz/miniconda3/bin/gaia check --brief TARGET_PACKAGE
    /home/hwz/miniconda3/bin/gaia check --hole TARGET_PACKAGE

Fix:

- anonymous _anon_* claims or strategies;
- orphaned claims;
- missing reasoning links;
- missing priors;
- bad prior justifications;
- wrong contradiction/complement usage;
- strategy reasons that mention facts not listed as premises or background;
- missing @label references in strategy reasons;
- important figure or table data missing from claim content.

After priors are complete, run:

    /home/hwz/miniconda3/bin/gaia compile TARGET_PACKAGE
    /home/hwz/miniconda3/bin/gaia infer TARGET_PACKAGE

Then inspect:

    TARGET_PACKAGE/.gaia/beliefs.json

Look for:

- independent claims whose posterior is far from prior;
- derived conclusions below 0.5;
- contradictions that do not resolve;
- both sides of a contradiction remaining high;
- both sides of a contradiction becoming low;
- long reasoning chains causing belief collapse;
- strategies missing prior=.

If the problem is structural, revise the DSL.

If the problem is prior-related, revise priors.py or inline strategy priors.

## Rendering Workflow

After successful inference, run:

    /home/hwz/miniconda3/bin/gaia render TARGET_PACKAGE --target github
    /home/hwz/miniconda3/bin/gaia render TARGET_PACKAGE --target docs

Expected outputs:

    TARGET_PACKAGE/.gaia/ir.json
    TARGET_PACKAGE/.gaia/ir_hash
    TARGET_PACKAGE/.gaia/beliefs.json
    TARGET_PACKAGE/.github-output/
    TARGET_PACKAGE/docs/detailed-reasoning.md

After github rendering, use /gaia:publish to create or update README.md.

The README should be a scientific evidence assessment, not a generic paper summary.

## README Writing Rules

The README should explain:

- what the paper investigates;
- why the problem matters;
- the main claims;
- how the evidence supports each exported conclusion;
- which claims have high belief;
- which claims are weak;
- what assumptions drive uncertainty;
- what experiments or calculations would reduce uncertainty.

The README should not merely summarize the paper.

It should interpret the Gaia reasoning graph in scientific language.

Avoid Gaia jargon in README prose.

Do not lead every paragraph with belief values.

Use belief values as supporting annotations, not as the main subject.

## Synthesis Package

The package pvsk-gaia/ is reserved for final synthesis across all paper-level packages.

Do not put a single paper's artifacts/paper.md into pvsk-gaia/ unless explicitly requested.

The synthesis package should:

- use exported conclusions from paper-level packages;
- model cross-paper agreement;
- model contradictions;
- model competing mechanisms;
- use induction for repeated independent evidence;
- export final PVSK-level conclusions in __all__.

The synthesis package should be created only after several paper-level packages have been formalized and reviewed.

## Git Rules

Do not commit automatically unless asked.

Do not edit files under sources/ unless asked.

Prefer package-level commits.

For a paper package, commit only that package:

    git add packages/<package-name>
    git commit -m "formalize <paper-name> into Gaia package"

For synthesis:

    git add pvsk-gaia
    git commit -m "formalize PVSK synthesis Gaia package"

## How to Respond to User Requests

If the user asks to formalize a paper, first identify:

    TARGET_PACKAGE
    SOURCE_DIR
    CITATION_KEY

Then prepare artifacts if needed.

Then run /gaia:formalization for that target package only.

Then compile and check the target package.

Then review priors.

Then infer.

Then render.

Never process all papers at once unless explicitly requested.

For batch work, process papers one at a time and keep each package independent.