"""
Higgs phenomenology foundation — layered pedagogy (L0–L5 hooks), not a collider MC.

L1 field/VEV/EWSB, L2 mass generation, L3 boson channels, L4 screening + ATHENA verdict,
L5 extension roadmap strings.
"""

from .boson_phenomenology import higgs_decay_channels, higgs_production_channels
from .constants import ELECTROWEAK_SCALE_GEV, HIGGS_BOSON_MASS_GEV, VEV_GEV
from .contracts import (
    ClaimScreeningReport,
    ConceptLayer,
    FieldConcept,
    HiggsClaimScreeningResult,
    HiggsDomain,
    HiggsFoundationReport,
    HiggsProcessFact,
    MassContribution,
    ParticleConcept,
    SymmetryBreakingContext,
)
from .discovery_context import DiscoveryFact, lhc_higgs_discovery_facts
from .extension_hooks import bridge_notes_for_sibling_engines, extension_roadmap_tags
from .field_symmetry import core_potential_equation_text, layer1_field_and_symmetry_axes
from .foundation import assess_higgs_foundation
from .mass_and_couplings import mass_origin_axes, yukawa_coupling_order_of_magnitude
from .mass_generation import default_symmetry_breaking_context, mass_contribution_ledger, mass_generation_axes
from .mechanism import ew_symmetry_breaking_axes, higgs_field_and_boson_layers
from .open_questions import higgs_open_question_prompts, naturalness_note
from .potential_energy import (
    fermion_mass_gev_from_yukawa,
    higgs_mass_gev_tree_from_lambda,
    higgs_potential_cartoon,
    lambda_from_higgs_mass_tree,
    yukawa_from_fermion_mass_gev,
)
from .screening import (
    AthenaVerdict,
    HiggsClaimPayload,
    HiggsClaimTier,
    athena_verdict_from_screening,
    payload_from_dict,
    screen_higgs_claim,
)

__all__ = [
    "VEV_GEV",
    "HIGGS_BOSON_MASS_GEV",
    "ELECTROWEAK_SCALE_GEV",
    "HiggsDomain",
    "FieldConcept",
    "ParticleConcept",
    "MassContribution",
    "SymmetryBreakingContext",
    "HiggsProcessFact",
    "ConceptLayer",
    "HiggsFoundationReport",
    "HiggsClaimScreeningResult",
    "ClaimScreeningReport",
    "DiscoveryFact",
    "HiggsClaimPayload",
    "HiggsClaimTier",
    "AthenaVerdict",
    "layer1_field_and_symmetry_axes",
    "core_potential_equation_text",
    "mass_generation_axes",
    "mass_contribution_ledger",
    "default_symmetry_breaking_context",
    "higgs_production_channels",
    "higgs_decay_channels",
    "extension_roadmap_tags",
    "bridge_notes_for_sibling_engines",
    "higgs_potential_cartoon",
    "fermion_mass_gev_from_yukawa",
    "yukawa_from_fermion_mass_gev",
    "higgs_mass_gev_tree_from_lambda",
    "lambda_from_higgs_mass_tree",
    "higgs_field_and_boson_layers",
    "ew_symmetry_breaking_axes",
    "mass_origin_axes",
    "yukawa_coupling_order_of_magnitude",
    "lhc_higgs_discovery_facts",
    "higgs_open_question_prompts",
    "naturalness_note",
    "payload_from_dict",
    "athena_verdict_from_screening",
    "screen_higgs_claim",
    "assess_higgs_foundation",
]

__version__ = "0.3.0"
