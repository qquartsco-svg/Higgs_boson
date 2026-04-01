#!/usr/bin/env python3
"""Ensure higgs_phenomenology contracts and public API are present."""
from __future__ import annotations

import inspect
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def main() -> int:
    try:
        from higgs_phenomenology import contracts as c
    except ImportError as e:
        print("verify_package_identity:", e, file=sys.stderr)
        return 2

    for name in (
        "HiggsDomain",
        "HiggsFoundationReport",
        "ConceptLayer",
        "FieldConcept",
        "MassContribution",
        "HiggsProcessFact",
    ):
        if not hasattr(c, name):
            print("verify_package_identity: contracts missing", name, file=sys.stderr)
            return 1

    src = inspect.getsource(c)
    if "class HiggsFoundationReport" not in src:
        print("verify_package_identity: contracts.py wrong shape", file=sys.stderr)
        return 1

    import higgs_phenomenology as hp

    if not hasattr(hp, "assess_higgs_foundation"):
        print("verify_package_identity: missing assess_higgs_foundation", file=sys.stderr)
        return 1

    print("verify_package_identity: OK (higgs_phenomenology)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
