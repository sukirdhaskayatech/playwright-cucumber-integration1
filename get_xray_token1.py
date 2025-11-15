import os
import requests

AUTH_URL = "https://xray.cloud.getxray.app/api/v1/authenticate"

client_id = os.environ.get("XRAY_CLIENT_ID")
client_secret = os.environ.get("XRAY_CLIENT_SECRET")

if not client_id or not client_secret:
    print("ERROR: XRAY_CLIENT_ID or XRAY_CLIENT_SECRET is not set.")
    exit(1)

payload = {
    "client_id": client_id,
    "client_secret": client_secret
}

headers = {
    "Content-Type": "application/json"
}

resp = requests.post(AUTH_URL, json=payload, headers=headers)

if resp.status_code != 200:
    print("Failed! Status:", resp.status_code)
    print("Response:", resp.text)
else:
    token = resp.text.strip().strip('"')  # Remove quotes
    print("SUCCESS — Token length:", len(token))
    print("\nYour Bearer Token:\n")
    print(token)
