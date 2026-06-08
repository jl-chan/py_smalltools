import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

workspace_name = os.getenv("workspaceName")
organization_id = os.getenv("organizationId")

if not workspace_name or not organization_id:
    raise ValueError(
        "workspaceName and organizationId must be defined in .env"
    )

# Read access token
with open("access_token.txt", "r") as token_file:
    access_token = token_file.read().strip()

# TODO: Change the WORKER_GROUP_ID and __INPUTID
WORKER_GROUP_ID="aws_prod"
__INPUTID="PROD_Unix"

url = f"https://{workspace_name}-{organization_id}.cribl.cloud/api/v1/m/{WORKER_GROUP_ID}/system/inputs/{__INPUTID}"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

print(f"Status Code: {response.status_code}")

if response.ok:
    print("Response JSON:")
    print(response.json())
else:
    print("Error Response:")
    print(response.text)
