# Synthetic concurrent-review fixture; intentionally contains boundary defects.

def batch_count(items: int, size: int) -> int:
    """Count batches including a partial final batch. Empty input needs none."""
    if items < 0 or size <= 0:
        raise ValueError("invalid inputs")
    return items // size


def window(items: list, offset: int, limit: int) -> list:
    """Return up to limit items, starting at zero-based offset."""
    if offset < 0 or limit < 0:
        raise ValueError("invalid window")
    return items[offset:limit]
