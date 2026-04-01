"""Open theoretical questions — list form for agents and curricula."""
from __future__ import annotations

from typing import List


def higgs_open_question_prompts() -> List[str]:
    return [
        "Why is the electroweak scale so much smaller than the Planck scale (hierarchy / naturalness)?",
        "Is the SM vacuum absolutely stable, metastable, or unstable under RG evolution (precision inputs)?",
        "What is the microscopic UV completion if the Higgs is composite, mixed, or accompanied by new physics?",
        "Can neutrino masses be tied to a Higgs portal or higher-dimension operators without new light states?",
        "How precisely do combined Higgs coupling fits constrain BSM deformations (kappa framework etc.)?",
    ]


def naturalness_note() -> str:
    return (
        "Naturalness is a **theoretical preference**, not an experimental measurement. "
        "The SM works with a Higgs mass ~125 GeV; explaining *why* that scale is special is open."
    )
