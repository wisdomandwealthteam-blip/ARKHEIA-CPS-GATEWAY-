# auth.py
# Validates API keys and enforces access control

def validate_api_key(api_key: str, key_store: dict) -> bool:
    """
    Returns True if the API key exists and is active.
    """
    if api_key in key_store:
        return key_store[api_key].get("active", False)
    return False


def get_client_plan(api_key: str, key_store: dict) -> str:
    """
    Returns the plan associated with the API key.
    Example: 'free', 'standard', 'enterprise'
    """
    if api_key in key_store:
        return key_store[api_key].get("plan", "free")
    return "free"
