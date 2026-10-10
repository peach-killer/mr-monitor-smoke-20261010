"""Synthetic review fixture for polling batch A."""


def total_pages(item_count: int, page_size: int) -> int:
    """Return pages needed for all items, including a partial last page."""
    if item_count < 0 or page_size <= 0:
        raise ValueError("invalid pagination inputs")
    return item_count // page_size
