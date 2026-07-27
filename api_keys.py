
# api_keys.py
# Generates, stores, and manages API keys for clients

import secrets

def generate_api_key() -> str:
    """
    Generates a secure 32‑byte hex API key.
    """
    return secrets.token_hex(32)


def create_key_record(plan: str = "free") -> dict:
    """
    Creates a new key record with default fields.
    """
    return {
        "active": True,
        "plan": plan,
        "usage": 0
    }


def add_api_key(key_store: dict, plan: str = "free") -> str:
    """
    Generates a new API key and adds it to the key store.
    Returns the new API key.
    """
    new_key = generate_api_key()
    key_store[new_key] = create_key_record(plan)
    return new_key


def deactivate_api_key(api_key: str, key_store: dict) -> bool:
    """
    Deactivates an API key. Returns True if successful.
    """
    if api_key in key_store:
        key_store[api_key]["active"] = False
        return True
    return False
