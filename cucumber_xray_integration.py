import os
import requests

# 1) Xray Endpoint for importing .feature files
IMPORT_URL = "https://xray.cloud.getxray.app/api/v1/import/feature?projectKey=SCRUM"

# 2) Read token from environment variable (set after running get_xray_token.py)
token = os.environ.get("XRAY_BEARER_TOKEN")

if not token:
    print("ERROR: XRAY_BEARER_TOKEN is not set.")
    print("Set it using: $env:XRAY_BEARER_TOKEN=\"<your token>\"")
    exit(1)

# 3) Path to your feature file
feature_file_path = "tests/features/login.feature"   # Change this to the actual file

if not os.path.exists(feature_file_path):
    print(f"ERROR: File not found: {feature_file_path}")
    exit(1)

headers = {
    "Authorization": f"Bearer {token}"
}

files = {
    "file": open(feature_file_path, "rb")
}

# 4) Upload file to Xray
response = requests.post(IMPORT_URL, headers=headers, files=files)

print("Status:", response.status_code)
print("Response:", response.text)
