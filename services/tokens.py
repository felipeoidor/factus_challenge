from services.api_client import fetch_auth_token, renew_token


def get_refreshed_token():
    auth_token = fetch_auth_token()
    if auth_token is None:
        raise ValueError("Failed to fetch auth token")
    
    access_token = auth_token.get("access_token")
    refresh_token = auth_token.get("refresh_token")
    
    if not access_token or not refresh_token:
        raise ValueError("Missing access_token or refresh_token in auth response")
    
    renewed_token_response = renew_token(access_token, refresh_token)
    if renewed_token_response is None:
        raise ValueError("Failed to renew token")
    
    refreshed_token = renewed_token_response.get("access_token")
    if not refreshed_token:
        raise ValueError("Missing access_token in renewed token response")

    return refreshed_token