"""Synthetic arithmetic helpers used only for MR Monitor smoke tests."""


def average(values):
    """Return the arithmetic mean, or 0.0 for an empty list."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def discount_price(price, percent):
    """Return price after a discount; percent is between 0 and 100."""
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return price * (1 - percent / 100)
