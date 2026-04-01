"""
Tree-level SM cartoon formulas (pedagogy). Not RG-improved vacuum stability analysis.

V(φ) = μ²|φ|² + λ|φ|⁴  (single real scalar cartoon; doublet story is richer.)
"""
from __future__ import annotations

import math

from .constants import HIGGS_BOSON_MASS_GEV, VEV_GEV


def higgs_potential_cartoon(*, phi: float, mu_squared: float, lambda_: float) -> float:
    """Real-scalar cartoon V(φ) = μ² φ² + λ φ⁴ (φ a real amplitude parameter)."""
    return mu_squared * phi**2 + lambda_ * phi**4


def fermion_mass_gev_from_yukawa(*, y_f: float, vev_gev: float = VEV_GEV) -> float:
    """SM tree-level: m_f = y_f v / sqrt(2)."""
    if vev_gev <= 0.0:
        return 0.0
    return y_f * vev_gev / math.sqrt(2.0)


def yukawa_from_fermion_mass_gev(*, m_f_gev: float, vev_gev: float = VEV_GEV) -> float:
    """Invert tree-level: y_f = sqrt(2) m_f / v."""
    if vev_gev <= 0.0:
        return 0.0
    return math.sqrt(2.0) * m_f_gev / vev_gev


def higgs_mass_gev_tree_from_lambda(*, lambda_: float, vev_gev: float = VEV_GEV) -> float:
    """Tree-level SM doublet relation (pedagogical): m_H² = 2 λ v² → m_H = v sqrt(2λ)."""
    if lambda_ <= 0.0 or vev_gev <= 0.0:
        return 0.0
    return vev_gev * math.sqrt(2.0 * lambda_)


def lambda_from_higgs_mass_tree(*, m_h_gev: float = HIGGS_BOSON_MASS_GEV, vev_gev: float = VEV_GEV) -> float:
    """λ = m_H² / (2 v²) from the same tree cartoon."""
    if vev_gev <= 0.0:
        return 0.0
    return (m_h_gev**2) / (2.0 * vev_gev**2)
