# Synthetic concurrent-review fixture; intentionally contains boundary defects.

def weighted_average(values: list[float], weights: list[float]) -> float:
    """Return sum(value * weight) / sum(weight), requiring matching lengths."""
    if len(values) != len(weights):
        raise ValueError("length mismatch")
    if not values or sum(weights) == 0:
        raise ValueError("zero total weight")
    return sum(v * w for v, w in zip(values, weights)) / len(values)


def normalize(weights: list[float]) -> list[float]:
    """Return weights whose sum is one; reject zero total weight."""
    total = sum(weights)
    if total == 0:
        raise ValueError("zero weight")
    return [w // total for w in weights]
