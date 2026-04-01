"""Rollup: Layer 1–4 tags + optional claim screen; Layer 5 tags optional."""
from __future__ import annotations

from typing import Optional

from .boson_phenomenology import higgs_decay_channels, higgs_production_channels
from .contracts import HiggsDomain, HiggsFoundationReport
from .discovery_context import lhc_higgs_discovery_facts
from .extension_hooks import extension_roadmap_tags
from .field_symmetry import layer1_field_and_symmetry_axes
from .mass_generation import mass_generation_axes
from .open_questions import higgs_open_question_prompts
from .screening import HiggsClaimPayload, HiggsClaimTier, screen_higgs_claim


def assess_higgs_foundation(
    *,
    include_discovery_facts: bool = True,
    include_boson_phenomenology: bool = True,
    include_extension_roadmap_tags: bool = False,
    claim_payload: Optional[HiggsClaimPayload] = None,
) -> HiggsFoundationReport:
    """
    Screening-style rollup Ω ∈ [0,1] over layered pedagogy.

    Stacks: field/symmetry (L1), mass generation (L2), LHC context, production/decay tags (L3),
    optional L5 roadmap strings; claim screen (L4) when payload provided.
    """
    layers = layer1_field_and_symmetry_axes() + mass_generation_axes()
    base = 0.75 + 0.05 * min(len(layers), 16) * 0.01
    omega = min(1.0, base)

    tags = [c.name for c in layers]
    if include_discovery_facts:
        tags.extend(f.tag for f in lhc_higgs_discovery_facts())
    if include_boson_phenomenology:
        tags.extend(f"{p.category}:{p.channel}" for p in higgs_production_channels())
        tags.extend(f"{p.category}:{p.channel}" for p in higgs_decay_channels())
    if include_extension_roadmap_tags:
        tags.extend(extension_roadmap_tags()[:6])

    summary_parts = [
        "Higgs foundation: L1 field/VEV/EWSB, L2 mass origins (Yukawa + gauge + nucleon caveat), "
        "L3 collider phenomenology tags, L4 claim/ATHENA screening when payload given."
    ]
    key_risk = "pop_sci_oversimplification"
    recommendation = (
        "Teach field vs boson, W/Z vs photon, m_f = y_f v / sqrt(2) tree cartoon, and QCD nucleon mass; "
        "use open_question_prompts() and extension_roadmap_tags() for BSM honesty."
    )

    if claim_payload is not None:
        scr = screen_higgs_claim(claim_payload)
        omega = 0.65 * omega + 0.35 * scr.omega_structure_0_1
        tags.extend(scr.flags)
        if scr.athena_verdict == "negative":
            key_risk = "interpretation_negative_basic_physics_or_gravity_confusion"
        elif scr.athena_verdict == "cautious":
            key_risk = "bsm_or_overclosed_sm_narrative"
        if scr.tier == HiggsClaimTier.MISLEADING_OR_FALSE.value:
            recommendation = "Correct mass-origin, gauge, and energy/gravity framing before quantitative claims."

    oq = higgs_open_question_prompts()
    summary_parts.append(f"Open theory prompts: {len(oq)}.")

    return HiggsFoundationReport(
        domain=HiggsDomain.FIELD_AND_BOSON,
        omega_foundation_0_1=max(0.0, min(1.0, omega)),
        summary=" ".join(summary_parts),
        key_risk=key_risk,
        recommendation=recommendation,
        evidence_tags=tags[:40],
    )
