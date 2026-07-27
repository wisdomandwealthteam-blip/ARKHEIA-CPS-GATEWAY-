
# metering.py
# Tracks API usage for billing and plan enforcement

def increment_usage(api_key: str, key_store: dict) -> None:
    """
    Increments the usage counter for the given API key.
    """
    if api_key in key_store:
        current_usage = key_store[api_key].get("usage", 0)
        key_store[api_key]["usage"] = current_usage + 1


def get_usage(api_key: str, key_store: dict) -> int:
    """
    Returns the current usage count for the API key.
    """
    if api_key in key_store:
        return key_store[api_key].get("usage", 0)
    return 0


def reset_usage(api_key: str, key_store: dict) -> None:
    """
    Resets usage for a new billing cycle.
    """
    if api_key in key_store:
        key_store[api_key]["usage"] = 0
