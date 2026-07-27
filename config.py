# config.py
# Central configuration for the API gateway

# URL of your backend service
BACKEND_URL = "https://arkheia-cps-backend.onrender.com/api"

# Plan definitions for billing + rate limits
PLANS = {
    "free": {
        "name": "Free Tier",
        "monthly_quota": 500
    },
    "standard": {
        "name": "Standard Tier",
        "monthly_quota": 5000
    },
    "enterprise": {
        "name": "Enterprise Tier",
        "monthly_quota": 50000
    }
}

# Optional: storage file for API keys (JSON)
KEY_STORE_FILE = "key_store.json"
