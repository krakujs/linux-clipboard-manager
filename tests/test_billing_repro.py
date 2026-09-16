from billing import get_idempotency_key


def test_legacy_order_without_idempotency_key_returns_none():
    """Legacy orders may lack 'idempotency_key'; lookup should default to None, not raise KeyError."""
    assert get_idempotency_key({}) is None
