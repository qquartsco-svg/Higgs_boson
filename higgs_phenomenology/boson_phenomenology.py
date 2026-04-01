"""Layer 3 — Higgs boson collider phenomenology tags (no parton-level MC)."""
from __future__ import annotations

from typing import List

from .contracts import HiggsProcessFact


def higgs_production_channels() -> List[HiggsProcessFact]:
    return [
        HiggsProcessFact(
            category="production",
            channel="ggF",
            statement="Gluon fusion (gg → H) is often dominant at the LHC via heavy-quark loops.",
        ),
        HiggsProcessFact(
            category="production",
            channel="VBF",
            statement="Vector boson fusion: two forward jets + Higgs-like central system.",
        ),
        HiggsProcessFact(
            category="production",
            channel="VH",
            statement="Associated production with weak bosons (WH, ZH).",
        ),
        HiggsProcessFact(
            category="production",
            channel="ttH",
            statement="Associated production with a top-quark pair; probes top-Yukawa coupling directly.",
        ),
    ]


def higgs_decay_channels() -> List[HiggsProcessFact]:
    return [
        HiggsProcessFact(
            category="decay",
            channel="h_to_bb",
            statement=r"Large branching to b\bar{b} at ~125 GeV; challenging QCD backgrounds.",
        ),
        HiggsProcessFact(
            category="decay",
            channel="h_to_gammagamma",
            statement="Rare but clean electromagnetic channel; important for early discovery-era sensitivity.",
        ),
        HiggsProcessFact(
            category="decay",
            channel="h_to_WW",
            statement="WW* channel probes weak-boson couplings; kinematics often off-shell.",
        ),
        HiggsProcessFact(
            category="decay",
            channel="h_to_ZZ",
            statement="ZZ* → 4l golden channel historically important for spin-0 discrimination.",
        ),
        HiggsProcessFact(
            category="decay",
            channel="h_to_tautau",
            statement="τ+τ− channel ties Higgs to third-generation fermion Yukawas.",
        ),
    ]
