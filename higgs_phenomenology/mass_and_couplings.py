"""
Where mass 'comes from' in the SM — with the crucial proton-mass caveat.

This module exists to stop the common myth: **most of visible mass is NOT Higgs Yukawa**.
"""
from __future__ import annotations

from typing import List

from .constants import VEV_GEV
from .contracts import ConceptLayer


def mass_origin_axes() -> List[ConceptLayer]:
    return [
        ConceptLayer(
            name="fermion_yukawa",
            summary="Elementary fermion masses (in the SM) come from Yukawa couplings to the Higgs field.",
            detail=(
                "After EWSB, Yukawa terms become mass terms for quarks and leptons (with generation mixing "
                "for quarks). This addresses **elementary** fermion masses in the SM Lagrangian sense."
            ),
        ),
        ConceptLayer(
            name="gauge_boson_higgs_mechanism",
            summary="W and Z masses arise from the Higgs mechanism (gauge boson mass terms).",
            detail="The photon stays massless; W/Z masses are tied to the electroweak scale and VEV structure.",
        ),
        ConceptLayer(
            name="hadronic_mass_mostly_not_higgs",
            summary="Most of the mass of nucleons (proton/neutron) is **not** bare Yukawa of valence quarks.",
            detail=(
                "Proton mass ~938 MeV is dominated by QCD binding energy and non-perturbative dynamics; "
                "valence quark **rest masses** from the Higgs/Yukawa are a small fraction. "
                "Saying 'the Higgs gives all mass' without this caveat is misleading for everyday matter."
            ),
        ),
        ConceptLayer(
            name="hierarchy_problem_framing",
            summary="Why the Higgs mass is ~100 GeV (not Planck) is an open theoretical tension (naturalness).",
            detail=(
                "Radiative corrections tend to drag scalar masses; explaining the weak scale is **unsolved** "
                "beyond the SM. This engine does not pick a BSM solution — it only names the tension."
            ),
        ),
    ]


def yukawa_coupling_order_of_magnitude(*, fermion_mass_gev: float, vev_gev: float = VEV_GEV) -> float:
    """SM order-of-magnitude Yukawa y ~ sqrt(2) m / v (single Higgs doublet, tree-level intuition)."""
    if vev_gev <= 0.0 or fermion_mass_gev < 0.0:
        return 0.0
    from math import sqrt

    return sqrt(2.0) * fermion_mass_gev / vev_gev
