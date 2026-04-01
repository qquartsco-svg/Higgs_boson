> **English.** Korean (정본): [LAYER_STACK.md](LAYER_STACK.md)

# Higgs foundation layer (v0.3.0)

## L0 — Contracts

`FieldConcept`, `ParticleConcept`, `MassContribution`, `SymmetryBreakingContext`, `HiggsProcessFact`, `HiggsFoundationReport`, `HiggsClaimScreeningResult` (alias `ClaimScreeningReport`)

## L1 — Field / symmetry

`layer1_field_and_symmetry_axes()`, `core_potential_equation_text()`, composed with `mechanism.py`.

## L2 — Mass generation

`mass_generation_axes()`, `mass_contribution_ledger()`, `default_symmetry_breaking_context()`

## L3 — Higgs boson phenomenology

`higgs_production_channels()`, `higgs_decay_channels()` — tag-level only.

## L4 — Screening / ATHENA

`screen_higgs_claim()`, `AthenaVerdict`; formula cartoons in `potential_energy.py`.

## L5 — Extension hooks

`extension_roadmap_tags()`, `bridge_notes_for_sibling_engines()`

## Rollup

`assess_higgs_foundation(...)`; optional `claim_payload` applies L4.
