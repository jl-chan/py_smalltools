from google.oauth2 import service_account
from google.auth.transport.requests import Request
import argparse

# Parse input argument for service account file
parser = argparse.ArgumentParser(description="Google Auth Token Generator")
parser.add_argument(
    "--auth-file",
    required=True,
    help="Path to service account JSON file"
)
args = parser.parse_args()

try:
    credentials = service_account.Credentials.from_service_account_file(
        args.auth_file,
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    
    # This forces the library to sign a JWT and exchange it for an access token
    credentials.refresh(Request())
    print("✅ Success! The key and signature are valid.")
    print("Access Token:")
    print(credentials.token)
    
    print(f"Token expires at: {credentials.expiry}")
except Exception as e:
    print(f"❌ Authentication failed: {e}")

