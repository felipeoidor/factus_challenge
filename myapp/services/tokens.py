from myapp.services.api_client import fetch_auth_token, renew_token

auth_token = fetch_auth_token()
access_token = auth_token.get("access_token")
refresh_token = auth_token.get("refresh_token")
refreshed_token = renew_token(access_token, refresh_token).get("access_token")