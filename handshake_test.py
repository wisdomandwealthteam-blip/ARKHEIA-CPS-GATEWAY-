from api_keys import add_api_key
from router import forward_request

# 1. Create an in‑memory key store
key_store = {}

# 2. Generate a test API key
test_key = add_api_key(key_store, plan="free")
print("Generated test key:", test_key)

# 3. Build a simple payload
payload = {"ping": "gateway-test"}

# 4. Run the handshake through the gateway
result = forward_request(
    api_key=test_key,
    key_store=key_store,
    payload=payload
)

print("Gateway → Backend handshake result:")
print(result)
