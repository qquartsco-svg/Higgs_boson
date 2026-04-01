"""
Electroweak symmetry breaking (EWSB) — conceptual structure only.

No lattice QFT, no parton shower: screening-level language aligned with SM textbooks.
"""
from __future__ import annotations

from typing import List

from .constants import HIGGS_BOSON_MASS_GEV
from .contracts import ConceptLayer


def higgs_field_and_boson_layers() -> List[ConceptLayer]:
    """Distinguish the **Higgs field** (vacuum property) from the **Higgs boson** (quantum)."""
    return [
        ConceptLayer(
            name="scalar_field",
            summary="The Higgs field is a scalar field with a non-zero value in the vacuum.",
            detail=(
                "In the SM, a doublet acquires a vacuum expectation value (VEV) after EWSB. "
                "That VEV is ~246 GeV in the usual convention; it is a property of the ground state, "
                "not a proof that 'space is filled with molasses' in a literal mechanical sense."
            ),
        ),
        ConceptLayer(
            name="higgs_boson",
            summary="The Higgs boson is an excitation (quantum) of that field.",
            detail=(
                "Like other fields, the Higgs field can ripple; those ripples appear as a spin-0 particle "
                f"(mass reference order ~{HIGGS_BOSON_MASS_GEV} GeV). Discovering the boson confirms the quantum sector "
                "exists; many precision coupling tests followed at colliders."
            ),
        ),
        ConceptLayer(
            name="gauge_invariance_vs_mass",
            summary="EWSB hides electroweak symmetry while leaving photon massless.",
            detail=(
                "W and Z acquire mass through the Higgs mechanism; the photon remains massless. "
                "This is a gauge redundancy story best read with a textbook Lagrangian, not oversimplified "
                "to 'Higgs drags on everything equally'."
            ),
        ),
    ]


def ew_symmetry_breaking_axes() -> List[ConceptLayer]:
    """Short axes for 'what breaks' and 'what stays massless'."""
    return [
        ConceptLayer(
            name="su2_x_u1_to_em",
            summary="Electroweak SU(2)×U(1) is broken down to electromagnetic U(1)_em.",
            detail="The W± and Z are massive; the photon is the massless gauge boson of unbroken EM.",
        ),
        ConceptLayer(
            name="potential_and_vev",
            summary="The Mexican-hat potential picture: choosing a vacuum breaks symmetry spontaneously.",
            detail=(
                "Pedagogical potential V(φ) with minima away from φ=0; quantum corrections and RG running "
                "make the full story richer than a single cartoon."
            ),
        ),
    ]
