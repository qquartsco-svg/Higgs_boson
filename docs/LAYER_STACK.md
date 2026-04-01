> **한국어 (정본).** English: [LAYER_STACK_EN.md](LAYER_STACK_EN.md)

# 힉스 기초 레이어 (v0.3.0)

## L0 — Contracts

`FieldConcept`, `ParticleConcept`, `MassContribution`, `SymmetryBreakingContext`, `HiggsProcessFact`, `HiggsFoundationReport`, `HiggsClaimScreeningResult` (`ClaimScreeningReport` 별칭)

## L1 — Field / symmetry

`layer1_field_and_symmetry_axes()`, `core_potential_equation_text()`, 저수준은 `mechanism.py`와 합성.

## L2 — Mass generation

`mass_generation_axes()` (= `mass_origin_axes` 정렬), `mass_contribution_ledger()`, `default_symmetry_breaking_context()`

## L3 — Higgs boson phenomenology

`higgs_production_channels()`, `higgs_decay_channels()` — 태그·문장 수준.

## L4 — Screening / ATHENA

`screen_higgs_claim()`, `AthenaVerdict`, 수식 뼈대는 `potential_energy.py`.

## L5 — Extension hooks

`extension_roadmap_tags()`, `bridge_notes_for_sibling_engines()`

## 통합

`assess_higgs_foundation(...)` — Ω 롤업; `claim_payload` 시 L4 반영.
