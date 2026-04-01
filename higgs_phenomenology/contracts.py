"""Layer-0 contracts — field vs boson, mass bookkeeping, symmetry context, screening."""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class HiggsDomain(str, Enum):
    """Which slice of the foundation story a report emphasizes."""

    FIELD_AND_BOSON = "field_and_boson"
    EWSB = "electroweak_symmetry_breaking"
    MASS_ORIGINS = "mass_origins"
    DISCOVERY = "discovery_context"
    OPEN_THEORY = "open_theory"
    CLAIM_SCREENING = "claim_screening"
    BOSON_PHENOMENOLOGY = "boson_phenomenology"


@dataclass(frozen=True)
class FieldConcept:
    """Pedagogical tag: Higgs field as vacuum property, not a ball of stuff."""

    name: str = "higgs_field"
    summary: str = "A scalar field with a vacuum expectation value after EWSB."
    gauge_note: str = "Described in a gauge-invariant SM framework; not a mechanical aether."


@dataclass(frozen=True)
class ParticleConcept:
    """Pedagogical tag: quantum excitation of the field."""

    name: str = "higgs_boson"
    summary: str = "Spin-0 excitation of the Higgs field; observed as a resonance near ~125 GeV."
    relation_to_field: str = "The boson is a ripple of the field, analogous to other field quanta."


@dataclass(frozen=True)
class MassContribution:
    """Bookkeeping for “where mass comes from” in pedagogy (not a precision fit)."""

    source: str  # e.g. "yukawa_fermion", "gauge_higgs_mechanism", "qcd_binding_composite"
    description: str
    sm_relevance: str  # "primary", "dominant_for_nucleon", etc.


@dataclass(frozen=True)
class SymmetryBreakingContext:
    """Minimal SM cartoon: μ² < 0 drives SSB in the doublet potential story."""

    mu_squared_negative_for_ssb: bool = True
    vev_gev_reference: float = 246.22
    broken_gauge_group_note: str = "SU(2)×U(1)_Y → U(1)_em; W/Z massive, photon massless."


@dataclass(frozen=True)
class HiggsProcessFact:
    """One production or decay pathway tag (phenomenology, not MC)."""

    category: str  # "production" | "decay"
    channel: str
    statement: str


@dataclass(frozen=True)
class HiggsFoundationReport:
    domain: HiggsDomain
    omega_foundation_0_1: float
    summary: str
    key_risk: str
    recommendation: str
    evidence_tags: List[str] = field(default_factory=list)


@dataclass(frozen=True)
class HiggsClaimScreeningResult:
    tier: str
    omega_structure_0_1: float
    notes: List[str]
    flags: List[str] = field(default_factory=list)
    athena_verdict: Optional[str] = None


# Alias for stack docs that name ClaimScreeningReport
ClaimScreeningReport = HiggsClaimScreeningResult


@dataclass(frozen=True)
class ConceptLayer:
    """One pedagogical layer in the stack."""

    name: str
    summary: str
    detail: str
