import os
from dotenv import load_dotenv

# load environment variables from a .env file
load_dotenv()


# URL Endpoint for obtaining an access token
URL_AUTHENTICATION = "https://api-sandbox.factus.com.co/oauth/token"

# Header for authentication requests
HEADER_AUTHENTICATION = {"Accept": "application/json"}

# Body payload for authentication requests
AUTHENTICATION_PAYLOAD = {
    "grant_type": "password",
    "client_id": os.getenv("CLIENT_ID"),
    "client_secret": os.getenv("CLIENT_SECRET"),
    "username": os.getenv("USERNAME"),
    "password": os.getenv("PASSWORD"),
}


# Header for refresh tokens
def refresh_header(access_token: str):
    return {"Authorization": f"Bearer {access_token}", "Accept": "application/json"}

# Body payload for refresh tokens 
def refresh_body(refresh_token: str):
    return {
        "grant_type": "refresh_token",
        "client_id": os.getenv("CLIENT_ID"),
        "client_secret": os.getenv("CLIENT_SECRET"),
        "refresh_token": refresh_token,
    }
