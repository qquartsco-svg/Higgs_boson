"""
Layer 5 — extension hooks (no BSM fits here).

Reserve tags for future: 2HDM, SUSY Higgs sectors, vacuum stability RG analysis,
electroweak phase transition / baryogenesis links, precision kappa fits.
"""
from __future__ import annotations

from typing import List


def extension_roadmap_tags() -> List[str]:
    return [
        "bsm_multiple_higgs_doublets",
        "supersymmetric_higgs_sectors",
        "rg_vacuum_stability_meta_stability",
        "electroweak_phase_transition",
        "baryogenesis_ew_scale_linkage",
        "higgs_portal_dark_matter",
        "kappa_framework_precision",
    ]


def bridge_notes_for_sibling_engines() -> List[str]:
    """Documentation-only bridge intents (implement in sibling packages, not required here)."""
    return [
        "Antimatter_Phenomenology: η_B and EW baryogenesis are distinct literature threads; link only as open prompts.",
        "FrequencyCore: Higgs resonance linewidth / detector bandwidth are experimental noise topics, not this layer.",
        "Anomalous_Observation_Foundation: BSM excesses belong in collider statistics + AOF-style screening, not here.",
    ]
