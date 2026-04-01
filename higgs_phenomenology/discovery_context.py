"""LHC-era discovery framing — tags and text, not event reconstruction."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class DiscoveryFact:
    tag: str
    statement: str


def lhc_higgs_discovery_facts() -> List[DiscoveryFact]:
    return [
        DiscoveryFact(
            tag="collider",
            statement="Evidence came from proton-proton collisions at the LHC (ATLAS and CMS).",
        ),
        DiscoveryFact(
            tag="mass_scale",
            statement="Higgs-like resonance near ~125 GeV (combined channels; reference PDG for precision).",
        ),
        DiscoveryFact(
            tag="channels",
            statement="Key search channels included γγ, ZZ*, WW*, ττ, bb (with channel-dependent sensitivity).",
        ),
        DiscoveryFact(
            tag="spin_parity",
            statement="Data favored spin-0, CP-even quantum numbers consistent with the SM Higgs boson.",
        ),
        DiscoveryFact(
            tag="couplings_program",
            statement="Post-discovery program: measure couplings and tensor structure as precision tests of the SM.",
        ),
    ]
