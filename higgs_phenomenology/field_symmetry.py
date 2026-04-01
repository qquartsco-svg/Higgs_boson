"""Layer 1 — field, VEV, spontaneous EWSB vocabulary (wraps + extends mechanism layers)."""
from __future__ import annotations

from typing import List

from .constants import VEV_GEV
from .contracts import ConceptLayer
from .mechanism import ew_symmetry_breaking_axes, higgs_field_and_boson_layers


def layer1_field_and_symmetry_axes() -> List[ConceptLayer]:
    """Layer 1: distinguish field / boson / VEV / SSB / electroweak group."""
    extra = [
        ConceptLayer(
            name="vev_scale",
            summary=f"Electroweak VEV is of order v ≈ {VEV_GEV} GeV (convention-dependent normalization).",
            detail="This sets the weak scale together with gauge couplings; it is not 'mass of the Higgs particle'.",
        ),
        ConceptLayer(
            name="spontaneous_breaking",
            summary="Symmetry can be broken by the vacuum choosing a state, not necessarily by explicit breaking terms in the potential.",
            detail="Mexican-hat cartoon: unstable origin if μ²<0 in the renormalized tree story; quantum corrections alter the full picture.",
        ),
    ]
    return higgs_field_and_boson_layers() + ew_symmetry_breaking_axes() + extra


def core_potential_equation_text() -> str:
    return r"Tree cartoon: V(φ) = μ²|φ|² + λ|φ|⁴ ; μ² < 0 → SSB minima (doublet story in textbooks)."
