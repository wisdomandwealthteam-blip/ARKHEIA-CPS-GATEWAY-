# rate_limit.py
# Enforces per‑minute and per‑day rate limits based on client plan

import time

# Simple in‑memory store for request timestamps
rate_memory = {
    # api_key: [timestamps]
}


PLAN_LIMITS = {
    "free": {
        "per_minute": 5,
        "per_day": 500
    },
    "standard": {
        "per_minute": 30,
        "per_day": 5000
    },
    "enterprise": {
        "per_minute": 120,
        "per_day": 50000
    }
}


def _cleanup_old_requests(timestamps: list) -> list:
    """
    Removes timestamps older than 24 hours.
    """
    now = time.time()
    return [t for t in timestamps if now - t < 86400]


def check_rate_limit(api_key: str, plan: str) -> bool:
    """
    Returns True if the request is allowed under the plan limits.
    """
    now = time.time()

    if api_key not in rate_memory:
        rate_memory[api_key] = []

    # Clean old timestamps
    rate_memory[api_key] = _cleanup_old_requests(rate_memory[api_key])

    timestamps = rate_memory[api_key]

    # Count requests in the last minute
    requests_last_minute = [t for t in timestamps if now - t < 60]

    # Count requests in the last day
    requests_last_day = timestamps

    limits = PLAN_LIMITS.get(plan, PLAN_LIMITS["free"])

    if len(requests_last_minute) >= limits["per_minute"]:
        return False

    if len(requests_last_day) >= limits["per_day"]:
        return False

    # Allowed — record the timestamp
    rate_memory[api_key].append(now)
    return True
