import requests
from config import (
    URL_AUTHENTICATION,
    URL_REFRESH_TOKEN,
    URL_NUMBERING_RANGE,
    URL_MUNICIPALITY,
    HEADER_AUTHENTICATION,
    AUTHENTICATION_PAYLOAD,
    refresh_header,
    refresh_body,
    numbering_range_header,
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
def renew_token(access_token, refresh_token):
    try:
        response = requests.post(
            URL_REFRESH_TOKEN,
            headers=refresh_header(access_token),
            data=refresh_body(refresh_token),
        )
        response.raise_for_status()
        tokens = response.json()
        return tokens

    except requests.exceptions.RequestException as error:
        return {"Error": str(error)}


# Numbering range
def get_numbering_range(access_token):
    response = requests.get(
        URL_NUMBERING_RANGE, headers=numbering_range_header(access_token)
    )

    return response.json().get("data").get("data")


# Municipality
def get_municipality(access_token):
    response = requests.get(
        URL_MUNICIPALITY,
        # I'll use the numbering range header for now
        headers=numbering_range_header(access_token),
    )

    return response.json().get("data")
