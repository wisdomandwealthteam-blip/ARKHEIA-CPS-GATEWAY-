
# router.py
# Forwards validated and rate-limited requests to the backend

import requests
from auth import validate_api_key, get_client_plan
from rate_limit import check_rate_limit
from metering import increment_usage
from config import BACKEND_URL


def forward_request(api_key: str, key_store: dict, payload: dict) -> dict:
    """
    Main gateway entry point.
    Validates key, checks rate limits, meters usage,
    then forwards the request to the backend.
    """

    # 1. Validate API key
    if not validate_api_key(api_key, key_store):
        return {"error": "Invalid or inactive API key"}

    # 2. Determine client plan
    plan = get_client_plan(api_key, key_store)

    # 3. Rate limit check
    if not check_rate_limit(api_key, plan):
        return {"error": "Rate limit exceeded"}

    # 4. Meter usage
    increment_usage(api_key, key_store)

    # 5. Forward request to backend
    try:
        response = requests.post(
            BACKEND_URL,
            json=payload,
            timeout=10
        )
        return response.json()
    except Exception as e:
        return {"error": f"Backend request failed: {str(e)}}
