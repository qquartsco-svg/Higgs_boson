"""
Layer 4 — narrative / claim screening + ATHENA-style conservative verdict (pedagogy).

ATHENA verdicts are **interpretation guidance**, not experiment sign-off.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List

from .contracts import HiggsClaimScreeningResult


class HiggsClaimTier(str, Enum):
    CONSISTENT_WITH_SM_PEDAGOGY = "consistent_with_sm_pedagogy"
    NEEDS_NUANCE = "needs_nuance"
    MISLEADING_OR_FALSE = "misleading_or_false"


class AthenaVerdict(str, Enum):
    """Conservative four-way guidance (feedback-aligned)."""

    POSITIVE = "positive"
    NEUTRAL = "neutral"
    CAUTIOUS = "cautious"
    NEGATIVE = "negative"


@dataclass(frozen=True)
class HiggsClaimPayload:
    """Boolean flags for agent payloads."""

    says_higgs_gives_all_mass: bool = False
    ignores_qcd_binding_for_nucleon: bool = False
    equates_higgs_field_with_luminiferous_aether: bool = False
    claims_faster_than_light_or_perpetual_motion_via_higgs: bool = False
    presents_god_particle_as_physical_theory_term: bool = False
    claims_higgs_generates_gravity: bool = False
    claims_energy_non_conservation: bool = False
    suggests_second_higgs_or_composite_sector: bool = False
    frames_standard_model_as_absolutely_final: bool = False
    collider_signal_ambiguous_within_experimental_uncertainty: bool = False


def payload_from_dict(d: Dict[str, Any]) -> HiggsClaimPayload:
    return HiggsClaimPayload(
        says_higgs_gives_all_mass=bool(d.get("says_higgs_gives_all_mass", False)),
        ignores_qcd_binding_for_nucleon=bool(d.get("ignores_qcd_binding_for_nucleon", False)),
        equates_higgs_field_with_luminiferous_aether=bool(
            d.get("equates_higgs_field_with_luminiferous_aether", False)
        ),
        claims_faster_than_light_or_perpetual_motion_via_higgs=bool(
            d.get("claims_faster_than_light_or_perpetual_motion_via_higgs", False)
        ),
        presents_god_particle_as_physical_theory_term=bool(
            d.get("presents_god_particle_as_physical_theory_term", False)
        ),
        claims_higgs_generates_gravity=bool(d.get("claims_higgs_generates_gravity", False)),
        claims_energy_non_conservation=bool(d.get("claims_energy_non_conservation", False)),
        suggests_second_higgs_or_composite_sector=bool(
            d.get("suggests_second_higgs_or_composite_sector", False)
        ),
        frames_standard_model_as_absolutely_final=bool(
            d.get("frames_standard_model_as_absolutely_final", False)
        ),
        collider_signal_ambiguous_within_experimental_uncertainty=bool(
            d.get("collider_signal_ambiguous_within_experimental_uncertainty", False)
        ),
    )


def athena_verdict_from_screening(
    payload: HiggsClaimPayload,
    *,
    tier: str,
    omega_structure_0_1: float,
    flags: List[str],
) -> AthenaVerdict:
    if payload.claims_energy_non_conservation or payload.claims_faster_than_light_or_perpetual_motion_via_higgs:
        return AthenaVerdict.NEGATIVE
    if payload.claims_higgs_generates_gravity:
        return AthenaVerdict.NEGATIVE
    if "violates_basic_physics" in flags:
        return AthenaVerdict.NEGATIVE
    if tier == HiggsClaimTier.MISLEADING_OR_FALSE.value and omega_structure_0_1 < 0.35:
        return AthenaVerdict.NEGATIVE

    if payload.suggests_second_higgs_or_composite_sector:
        return AthenaVerdict.CAUTIOUS
    if payload.frames_standard_model_as_absolutely_final:
        return AthenaVerdict.CAUTIOUS

    if payload.collider_signal_ambiguous_within_experimental_uncertainty:
        return AthenaVerdict.NEUTRAL
    if tier == HiggsClaimTier.NEEDS_NUANCE.value:
        return AthenaVerdict.NEUTRAL
    if tier == HiggsClaimTier.MISLEADING_OR_FALSE.value:
        return AthenaVerdict.CAUTIOUS

    return AthenaVerdict.POSITIVE


def screen_higgs_claim(payload: HiggsClaimPayload) -> HiggsClaimScreeningResult:
    notes: List[str] = []
    flags: List[str] = []
    omega = 1.0

    if payload.claims_energy_non_conservation:
        av = athena_verdict_from_screening(
            payload,
            tier=HiggsClaimTier.MISLEADING_OR_FALSE.value,
            omega_structure_0_1=0.0,
            flags=["violates_basic_physics"],
        )
        return HiggsClaimScreeningResult(
            tier=HiggsClaimTier.MISLEADING_OR_FALSE.value,
            omega_structure_0_1=0.0,
            notes=["Energy conservation is foundational; this claim is outside SM pedagogy."],
            flags=["violates_basic_physics"],
            athena_verdict=av.value,
        )

    if payload.claims_faster_than_light_or_perpetual_motion_via_higgs:
        av = athena_verdict_from_screening(
            payload,
            tier=HiggsClaimTier.MISLEADING_OR_FALSE.value,
            omega_structure_0_1=0.0,
            flags=["violates_basic_physics"],
        )
        return HiggsClaimScreeningResult(
            tier=HiggsClaimTier.MISLEADING_OR_FALSE.value,
            omega_structure_0_1=0.0,
            notes=["Contradicts established relativity / thermodynamics; not a Higgs mechanism claim."],
            flags=["violates_basic_physics"],
            athena_verdict=av.value,
        )

    if payload.claims_higgs_generates_gravity:
        omega = 0.0
        flags.append("gravity_misattributed")
        notes.append("Gravitation is not the SM Higgs mechanism; do not conflate with spacetime metric dynamics.")

    if payload.says_higgs_gives_all_mass or payload.ignores_qcd_binding_for_nucleon:
        omega -= 0.35
        flags.append("mass_origin_oversimplified")
        notes.append(
            "Nucleon mass is mostly QCD binding energy; elementary fermion masses are Yukawa/Higgs-linked in the SM."
        )

    if payload.equates_higgs_field_with_luminiferous_aether:
        omega -= 0.25
        flags.append("bad_analogy")
        notes.append("Higgs field is not a 19th-century mechanical aether; analogy misleads about gauge invariance.")

    if payload.presents_god_particle_as_physical_theory_term:
        omega -= 0.1
        flags.append("media_label")
        notes.append("'God particle' is journalistic branding, not standard theory terminology.")

    omega = max(0.0, min(1.0, omega))

    if omega >= 0.85:
        tier = HiggsClaimTier.CONSISTENT_WITH_SM_PEDAGOGY
    elif omega >= 0.45:
        tier = HiggsClaimTier.NEEDS_NUANCE
    else:
        tier = HiggsClaimTier.MISLEADING_OR_FALSE

    if not notes:
        notes.append("No major red flags in payload flags; still verify sources for any quantitative claim.")

    av = athena_verdict_from_screening(payload, tier=tier.value, omega_structure_0_1=omega, flags=flags)

    return HiggsClaimScreeningResult(
        tier=tier.value,
        omega_structure_0_1=omega,
        notes=notes,
        flags=flags,
        athena_verdict=av.value,
    )
