> **English.** Korean (정본): [README.md](README.md)

# Higgs_Phenomenology_Foundation v0.3.0

**`Higgs_Phenomenology_Foundation` is a conservative foundation layer for answering “what is the Higgs?” through field theory, electroweak symmetry breaking, mass structure, boson phenomenology, and claim screening.**

This package does not treat the Higgs as a lone marble-like particle. Its core object is the combined structure of

- the Higgs **field**
- the electroweak vacuum expectation value (**VEV**)
- electroweak symmetry breaking (**EWSB**)
- gauge and Yukawa mass generation
- the Higgs boson as a quantum **excitation** of the field

So this repository is better read as a **phenomenology foundation** than as a “Higgs particle explainer”.

## What the Higgs is

In short:

- the Higgs **field** is a property of the electroweak vacuum
- the Higgs **boson** is an excitation of that field
- after EWSB, the vacuum value `v ≈ 246 GeV` is tied to
  - `W` and `Z` boson masses
  - elementary fermion masses through Yukawa couplings

The most important conservative clarification is this:

**the Higgs does not account for all mass in the same way.**

For example, most proton and neutron mass is dominated by **QCD binding energy**, not directly by the Higgs field. This engine is designed to preserve exactly that distinction.

## Why it matters

The Higgs sector touches several central questions in modern physics:

- why `W` and `Z` are massive while the photon is massless
- why elementary fermions have such different mass scales
- how the Standard Model organizes electroweak symmetry breaking
- where the open problems begin: hierarchy, naturalness, vacuum stability, and possible extensions

So the Higgs is not just “one more particle”. It is a key access point into the **mass and vacuum structure of the Standard Model**.

## Why this engine exists

In practice, the word “Higgs” is often used too loosely:

- “the Higgs creates gravity”
- “the Higgs gives all mass”
- “the Higgs discovery closed the Standard Model completely”
- “one headline proves beyond-Standard-Model physics”

This engine exists to slow that down and separate:

1. field-level structure
2. boson-level structure
3. mass-generation structure
4. discovery context
5. open-question context

Its purpose is not hype. Its purpose is **concept alignment, pedagogy, and conservative screening**.

## What it does

This package:

- distinguishes the Higgs field from the Higgs boson
- explains EWSB in a layered way
- separates fermion masses, `W/Z` masses, and QCD-dominated nucleon mass
- lists production and decay channels as phenomenology tags
- screens common Higgs claims with a conservative ATHENA verdict language
- leaves open-theory questions as roadmap tags rather than pretending to solve them

## What it does not do

This package does not:

- replace collider Monte Carlo tools
- perform precision branching-ratio fits
- perform detector simulation
- serve as an official experiment authority
- compute SUSY, 2HDM, or composite-Higgs numeric models
- support exaggerated claims such as “the Higgs explains all mass”

It is a **foundation/screening layer**, not a precision collider stack.

## For standalone clone users

This repository works on its own. Some documentation may mention sibling-engine intent from the larger `00_BRAIN` workspace; standalone public clones may not contain those local sibling paths.

## Layer structure

| Layer | Role | Modules |
|------|------|------|
| `L0` | contracts / types | `contracts.py` |
| `L1` | field, VEV, EWSB, symmetry breaking | `field_symmetry.py`, `mechanism.py` |
| `L2` | mass-generation structure | `mass_generation.py`, `mass_and_couplings.py` |
| `L3` | Higgs boson phenomenology | `boson_phenomenology.py`, `discovery_context.py` |
| `L4` | claim screening / ATHENA verdicts | `screening.py` |
| `L5` | open questions / sibling-engine notes | `open_questions.py`, `extension_hooks.py` |

See [docs/LAYER_STACK_EN.md](docs/LAYER_STACK_EN.md) for the compact layer map.

## Core modules

### `field_symmetry.py`

- Higgs field as a vacuum property
- VEV
- spontaneous symmetry breaking
- electroweak story framing

### `mechanism.py`

- `SU(2) × U(1)_Y -> U(1)_em`
- massive `W/Z`
- massless photon
- field-vs-boson separation

### `mass_generation.py`

- pedagogical mass ledger
- `gauge_higgs_mechanism`
- `yukawa_fermion`
- `qcd_binding_nucleon`

### `mass_and_couplings.py`

- Yukawa scale intuition
- order-of-magnitude coupling helpers

### `boson_phenomenology.py`

- production tags
  - `ggF`
  - `VBF`
  - `VH`
  - `ttH`
- decay tags
  - `gamma gamma`
  - `ZZ*`
  - `WW*`
  - `bb`
  - `tau tau`

### `discovery_context.py`

- how the Higgs is spoken about in collider discovery language
- in particular, that “discovery” means channel-specific excess plus collider statistical confirmation context, not a vague pop-science proclamation

### `open_questions.py`

- hierarchy / naturalness
- vacuum stability
- extension prompts

### `screening.py`

- conservative screening for misleading or overstated Higgs claims

### `foundation.py`

- rolls the stack into a single `HiggsFoundationReport`

## Core formulas and intuition

This engine uses formulas as **structural scaffolding**, not as a full precision-physics stack.

- cartoon potential:
  - `V(phi) = mu^2 |phi|^2 + lambda |phi|^4`
  - `mu^2 < 0` connects to spontaneous symmetry breaking
- vacuum expectation value:
  - `v ≈ 246 GeV`
- tree-level Yukawa mass:
  - `m_f = y_f v / sqrt(2)`
  - here `y_f` is a **dimensionless Yukawa coupling** and the returned mass is in **GeV**
- tree-level Higgs mass relation:
  - `m_H^2 = 2 lambda v^2`

The point here is conceptual structure, not precision fitting.

## ATHENA verdicts

`screening.py` uses a conservative four-stage language:

- `positive`
  - pedagogically aligned with Standard Model structure
- `neutral`
  - underspecified or uncertainty-framed without strong claims
- `cautious`
  - BSM, second-Higgs, composite-Higgs, or overstated closure narratives
- `negative`
  - physically misleading claims such as Higgs-as-gravity or all-mass absolutism

This is not a truth oracle. It is a **screening language for explanation quality and structural coherence**.

## Foundation output

`assess_higgs_foundation(...)` returns:

- `omega_foundation_0_1`
- `summary`
- `key_risk`
- `recommendation`
- `evidence_tags`

So the engine does not merely define the Higgs. It reports **which conceptual layers are present or missing** in a given explanation.

At the moment, the foundation output is centered on a **single `omega_foundation_0_1` plus explanation fields**. It does not yet expose separate scores such as `field_score`, `mass_structure_score`, `phenomenology_score`, or `claim_consistency_score`. For now, the repository explains the verdict through `evidence_tags`, `key_risk`, and `recommendation`.

A natural next extension would keep the single top-level `omega` while adding optional subscores such as:

- `field_symmetry_score`
- `mass_structure_score`
- `boson_phenomenology_score`
- `claim_consistency_score`

## Quickstart

```bash
cd Higgs_Phenomenology_Foundation   # or path to your cloned directory
python3 -m pip install -e ".[dev]"
python3 -m pytest tests/ -q
python3 scripts/verify_package_identity.py
```

```python
from higgs_phenomenology import (
    HiggsClaimPayload,
    assess_higgs_foundation,
    fermion_mass_gev_from_yukawa,
    screen_higgs_claim,
)

electron_mass = fermion_mass_gev_from_yukawa(y_f=2.94e-6)
print(electron_mass)

claim = HiggsClaimPayload(says_higgs_gives_all_mass=True)
screened = screen_higgs_claim(claim)
print(screened.tier, screened.athena_verdict)

report = assess_higgs_foundation(claim_payload=claim)
print(report.omega_foundation_0_1, report.key_risk)
```

## Tests and integrity

This repository includes:

- unit tests
- package identity verification
- SHA-256 signature verification
- release checks

Run:

```bash
python3 -m pytest tests/ -q
python3 scripts/verify_package_identity.py
python3 scripts/verify_signature.py
python3 scripts/release_check.py
```

Current baseline: `23 passed`.

## Blockchain signature

In this repository, “blockchain signature” does **not** mean an on-chain consensus system. It means a **SHA-256 integrity manifest** stored in `SIGNATURE.sha256`.

- [BLOCKCHAIN_INFO_EN.md](BLOCKCHAIN_INFO_EN.md)

Verify:

```bash
python3 scripts/verify_signature.py
```

Regenerate:

```bash
python3 scripts/generate_signature.py
```

## Practical uses

This package is well-suited for:

- Higgs pedagogy tools
- physics claim screening in agent systems
- conservative API backends for “what is the Higgs?”
- structured separation between Standard Model pedagogy and BSM roadmap notes
- cross-engine reuse as a safe conceptual layer

## Extensibility

Natural future directions include:

- `Higgs_Precision_Fit_Foundation`
- `Electroweak_Symmetry_Foundation`
- `BSM_Higgs_Extension_Kernel`
- collider report parser layers
- EFT / coupling-deviation tag layers
- vacuum stability / RG-running support notes

## Current limits

This engine is intentionally conservative.

- no collider event generation
- no detector simulation
- no precision fit
- no global branching-ratio analysis
- no full BSM numerical solving
- no authority claims beyond educational screening

It is an engine for **structuring Higgs understanding**, not for computing all Higgs physics.

## Repository files

- [docs/LAYER_STACK_EN.md](docs/LAYER_STACK_EN.md)
- [README.md](README.md)
- [CHANGELOG.md](CHANGELOG.md)
- [BLOCKCHAIN_INFO_EN.md](BLOCKCHAIN_INFO_EN.md)

## License

MIT
