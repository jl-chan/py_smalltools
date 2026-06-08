import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

client_id = os.getenv("CRIBL_CLIENT_ID")
client_secret = os.getenv("CRIBL_CLIENT_SECRET")

url = "https://login.cribl.cloud/oauth/token"

payload = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret,
    "audience": "https://api.cribl.cloud"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(f"Status Code: {response.status_code}")
print(response.text)

# Optional: extract access token
if response.ok:
    token_data = response.json()
    access_token = token_data.get("access_token")
    # print(f"Access Token: {access_token}")
    with open("access_token.txt", "w") as token_file:
        token_file.write(access_token)
    print("Access token saved to access_token.txt")
else:
    print(f"Failed to obtain token: {response.status_code}")
    print(response.text)
