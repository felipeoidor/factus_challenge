import json
import os
from dotenv import load_dotenv


# Load environment variables from a .env file
load_dotenv()


# Load API endpoints from the JSON configuration file
def get_endpoints():
    """
    Load and return a dictionary mapping endpoint types to their URLs
    from the 'endpoints.json' configuration file.
    """
    with open("endpoints.json", "r", encoding="UTF-8") as file:
        endpoints = json.load(file)
        urls = endpoints.get("endpoints")
        return {endpoint["type"]: endpoint["url"] for endpoint in urls}


# Load API endpoints
ENDPOINTS = get_endpoints()

# URL Endpoint for obtaining an access token
URL_AUTHENTICATION = ENDPOINTS.get("authentication")
URL_REFRESH_TOKEN = ENDPOINTS.get("refresh_token")
URL_NUMBERING_RANGE = ENDPOINTS.get("numbering_range")

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


# Generate the HTTP headers required for a refresh token request
def refresh_header(access_token: str) -> dict:
    """
    Return a dictionary containing  the Authorization header
    required to use the provided access token in a request.

    Parameters:
        access_token (str): The current access token.

    Returns:
        dict: HTTP headers including Authorization and Accept.
    """
    return {"Authorization": f"Bearer {access_token}", "Accept": "application/json"}


# Body payload for refresh tokens
def refresh_body(refresh_token: str) -> dict:
    """
    Return a dictionary payload for refreshing an access token
    using the provided refresh token.

    Parameters:
        refresh_token (str): The Refresh token issued previously.

    Returns:
        dict: Payload containing grant_type, client_id, client_secret and refresh token.
    """
    return {
        "grant_type": "refresh_token",
        "client_id": os.getenv("CLIENT_ID"),
        "client_secret": os.getenv("CLIENT_SECRET"),
        "refresh_token": refresh_token,
    }


# Generate the HTTP headers required for obtain numbering range
def numbering_range_header(access_token: str) -> dict:
    """
    Return a dictionary containing the Authorization header
    required to obtain numbering range.

    Parameters:
        access_token (str): The current access token.

    Returns:
        dict: HTTP headers including Content-type, Authorization and Accept.
    """
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json",
    }
