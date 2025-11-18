import requests
from myapp.config.loader import load_json
from myapp.config.auth_payloads import (
    auth_payload,
    refresh_payload,
)


def fetch_auth_token(get: str = None) -> dict:
    endpoint = load_json(json_file="json/endpoints.json", get="authentication").get(
        "endpoint"
    )
    header = load_json("json/headers.json").get("auth_header")
    payload = auth_payload()
    response = requests.post(endpoint, headers=header, data=payload)

    if response.status_code == 200:
        data = response.json()
        if get is None:
            return data

        return data.get(get)


def renew_token(access_token: str, refresh_token) -> dict:
    endpoint = load_json(json_file="json/endpoints.json", get="refresh_token").get(
        "endpoint"
    )
    header = load_json("json/headers.json").get("refresh_token")
    header["Authorization"] = f"Bearer {access_token}"
    payload = refresh_payload(refresh_token)
    response = requests.post(endpoint, headers=header, data=payload)

    if response.status_code == 200:
        return response.json()


def base_header(tokens):
    access_token = tokens
    header = load_json("json/headers.json").get("base_header")
    header["Authorization"] = f"Bearer {access_token}"
    return header


def get_requests(url, header):
    endpoint = url
    header_request = header
    response = requests.get(endpoint, headers=header_request)

    return response


def fetch_catalog_data(endpoint, header):
    response = get_requests(endpoint, header)

    if response.status_code == 200:
        return response.json()
