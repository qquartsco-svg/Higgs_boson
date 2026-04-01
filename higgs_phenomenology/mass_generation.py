"""Layer 2 — mass generation A/B/C: gauge bosons, Yukawa fermions, composite caveat."""
from __future__ import annotations

from typing import List

from .contracts import MassContribution, SymmetryBreakingContext
from .mass_and_couplings import mass_origin_axes


def mass_generation_axes():
    """Same physics as mass_origin_axes; name aligned with Layer-2 stack docs."""
    return mass_origin_axes()


def mass_contribution_ledger() -> List[MassContribution]:
    """Structured ledger for pedagogy and agent payloads."""
    return [
        MassContribution(
            source="gauge_boson_masses",
            description="W and Z acquire masses through the Higgs mechanism; photon stays massless.",
            sm_relevance="primary",
        ),
        MassContribution(
            source="fermion_yukawa",
            description="Elementary fermion masses in the SM from Yukawa couplings to the Higgs doublet.",
            sm_relevance="primary",
        ),
        MassContribution(
            source="qcd_binding_nucleon",
            description="Most of proton/neutron mass is dynamical QCD and binding, not valence-quark Yukawa masses.",
            sm_relevance="dominant_for_nucleon",
        ),
    ]


def default_symmetry_breaking_context() -> SymmetryBreakingContext:
    return SymmetryBreakingContext()
