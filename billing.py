"""Fixture billing module."""


def get_idempotency_key(order: dict) -> str | None:
    # Legacy orders may lack the key; default to None instead of raising KeyError.
    return order.get("idempotency_key")
