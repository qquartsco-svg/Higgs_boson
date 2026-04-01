"""Package identity guard: assert we are higgs_phenomenology, not a foreign engine."""
import importlib
import inspect


def test_contracts_defines_higgs_types():
    mod = importlib.import_module("higgs_phenomenology.contracts")
    names = dir(mod)
    for expected in ("FieldConcept", "ParticleConcept", "MassContribution", "HiggsFoundationReport"):
        assert expected in names, f"contracts.py missing expected type: {expected}"


def test_contracts_has_no_foreign_engine_symbols():
    mod = importlib.import_module("higgs_phenomenology.contracts")
    source = inspect.getsource(mod)
    forbidden = ("NeuronState", "SNN", "memory_engine", "AntimatterInventory", "ConfinementHealth")
    for term in forbidden:
        assert term not in source, f"contracts.py contains foreign symbol: {term!r}"


def test_init_exports_higgs_api():
    import higgs_phenomenology as hp

    required = [
        "VEV_GEV",
        "HIGGS_BOSON_MASS_GEV",
        "assess_higgs_foundation",
        "screen_higgs_claim",
        "HiggsClaimPayload",
        "fermion_mass_gev_from_yukawa",
        "AthenaVerdict",
    ]
    missing = [name for name in required if not hasattr(hp, name)]
    assert not missing, f"__init__.py missing public exports: {missing}"


def test_init_has_no_foreign_engine_symbols():
    import higgs_phenomenology as hp

    source = inspect.getsource(hp)
    forbidden = ("memory_engine", "SNN", "AntimatterFoundation", "ConfinementHealth")
    for term in forbidden:
        assert term not in source, f"__init__.py contains foreign symbol: {term!r}"


def test_version_string():
    import higgs_phenomenology as hp

    assert hasattr(hp, "__version__"), "__version__ must be defined"
    assert hp.__version__.startswith("0."), f"Unexpected version: {hp.__version__!r}"
