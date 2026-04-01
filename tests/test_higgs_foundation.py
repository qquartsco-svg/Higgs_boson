from higgs_phenomenology import (
    AthenaVerdict,
    assess_higgs_foundation,
    bridge_notes_for_sibling_engines,
    default_symmetry_breaking_context,
    extension_roadmap_tags,
    fermion_mass_gev_from_yukawa,
    higgs_decay_channels,
    higgs_production_channels,
    lambda_from_higgs_mass_tree,
    layer1_field_and_symmetry_axes,
    mass_contribution_ledger,
    screen_higgs_claim,
    yukawa_from_fermion_mass_gev,
)
from higgs_phenomenology.contracts import FieldConcept, ParticleConcept
from higgs_phenomenology.potential_energy import higgs_mass_gev_tree_from_lambda, higgs_potential_cartoon
from higgs_phenomenology.screening import HiggsClaimPayload, HiggsClaimTier


def test_layer1_non_empty():
    assert len(layer1_field_and_symmetry_axes()) >= 5


def test_contracts_field_particle():
    assert FieldConcept().name == "higgs_field"
    assert ParticleConcept().name == "higgs_boson"


def test_mass_ledger():
    src = {m.source for m in mass_contribution_ledger()}
    assert "qcd_binding_nucleon" in src


def test_symmetry_context():
    ctx = default_symmetry_breaking_context()
    assert ctx.vev_gev_reference > 200.0


def test_potential_cartoon():
    v0 = higgs_potential_cartoon(phi=0.0, mu_squared=-1.0, lambda_=1.0)
    assert v0 == 0.0


def test_yukawa_roundtrip_electron():
    m = 0.000511
    y = yukawa_from_fermion_mass_gev(m_f_gev=m)
    m2 = fermion_mass_gev_from_yukawa(y_f=y)
    assert abs(m2 - m) < 1e-12


def test_lambda_mass_tree_roundtrip():
    lam = lambda_from_higgs_mass_tree()
    mh = higgs_mass_gev_tree_from_lambda(lambda_=lam)
    assert abs(mh - 125.1) < 0.05


def test_boson_channels():
    assert any(p.channel == "ggF" for p in higgs_production_channels())
    assert any(d.channel == "h_to_gammagamma" for d in higgs_decay_channels())


def test_extension_hooks():
    assert "vacuum" in " ".join(extension_roadmap_tags()).lower() or len(extension_roadmap_tags()) >= 5
    assert len(bridge_notes_for_sibling_engines()) >= 2


def test_screen_ftl_athena_negative():
    r = screen_higgs_claim(HiggsClaimPayload(claims_faster_than_light_or_perpetual_motion_via_higgs=True))
    assert r.tier == HiggsClaimTier.MISLEADING_OR_FALSE.value
    assert r.athena_verdict == AthenaVerdict.NEGATIVE.value


def test_screen_gravity_athena_negative():
    r = screen_higgs_claim(HiggsClaimPayload(claims_higgs_generates_gravity=True))
    assert r.athena_verdict == AthenaVerdict.NEGATIVE.value


def test_screen_bsm_cautious():
    r = screen_higgs_claim(HiggsClaimPayload(suggests_second_higgs_or_composite_sector=True))
    assert r.athena_verdict == AthenaVerdict.CAUTIOUS.value


def test_screen_neutral_uncertainty():
    r = screen_higgs_claim(
        HiggsClaimPayload(collider_signal_ambiguous_within_experimental_uncertainty=True)
    )
    assert r.athena_verdict == AthenaVerdict.NEUTRAL.value


def test_foundation_assess_with_layers():
    rep = assess_higgs_foundation(include_extension_roadmap_tags=True)
    assert 0.0 <= rep.omega_foundation_0_1 <= 1.0
    assert any("production" in t or "decay" in t for t in rep.evidence_tags)
