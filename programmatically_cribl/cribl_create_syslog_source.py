import csv
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

# Cribl API endpoint
# url = (
#     f"https://{workspace_name}-{organization_id}.cribl.cloud"
#     "/api/v1/system/inputs"
# )

# TODO: Change the WORKER_GROUP_ID
WORKER_GROUP_ID="aws_prod"
url = f"https://{workspace_name}-{organization_id}.cribl.cloud/api/v1/m/{WORKER_GROUP_ID}/system/inputs"


headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

csv_file = "sources_to_created.csv"

with open(csv_file, newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    # If the Syslog source is to used UDP, then replace the key field "tcpPort" with "udpPort"
    for row in reader:
        # The column header must be id,description,port
        source_id = row["id"].strip()
        description = row["description"].strip()
        tcp_port = int(row["port"].strip())

        payload = {
            "id": source_id,
            "description": f"{description} Datasources",
            "type": "syslog",
            "host": "0.0.0.0",
            "tcpPort": tcp_port,
            "sendToRoutes": True,
            "pqEnabled": False
        }

        try:
            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=30
            )

            if response.ok:
                print(
                    f"[SUCCESS] Created source "
                    f"{source_id} on port {tcp_port}"
                )
            else:
                print(
                    f"[FAILED] {source_id} "
                    f"({response.status_code})"
                )
                print(response.text)
        except Exception as e:
            print(f"[ERROR] {source_id}: {e}")
