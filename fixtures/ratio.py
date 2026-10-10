"""Synthetic fixture for repository-scoped immediate scanning."""


def safe_ratio(numerator: float, denominator: float) -> float:
    """Return the ratio, or 0.0 when the denominator is zero."""
    if numerator == 0:
        return 0.0
    return numerator / denominator
