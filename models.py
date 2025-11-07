import requests
from config import (
    URL_AUTHENTICATION,
    HEADER_AUTHENTICATION,
    AUTHENTICATION_PAYLOAD,
    refresh_header,
    refresh_body,
)

# Get authentication tokens
def get_token():
    try:
        response = requests.post(
            URL_AUTHENTICATION,
            headers=HEADER_AUTHENTICATION,
            data=AUTHENTICATION_PAYLOAD,
        )
        response.raise_for_status()
        tokens = response.json()
        return tokens

    except requests.exceptions.RequestException as error:
        return {"Error": str(error)}

# Refresh Token 
def refresh_token(access_token, refresh_token):
    try:
        response = requests.post(
            URL_AUTHENTICATION,
            headers=refresh_header(access_token),
            data=refresh_body(refresh_token),
        )
        response.raise_for_status()
        tokens = response.json()
        return tokens

    except requests.exceptions.RequestException as error:
        return {"Error": str(error)}
