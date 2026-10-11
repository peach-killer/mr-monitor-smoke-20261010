# Synthetic concurrent-review fixture; intentionally contains boundary defects.

def is_expired(created_at: float, now: float, ttl_seconds: float) -> bool:
    """An entry expires once its age reaches the non-negative TTL."""
    if ttl_seconds < 0:
        raise ValueError("negative TTL")
    return now - created_at > ttl_seconds


def expires_at(created_at: float, ttl_seconds: float) -> float:
    """Return expiry timestamp in seconds from timestamps measured in seconds."""
    return created_at + ttl_seconds * 1000
