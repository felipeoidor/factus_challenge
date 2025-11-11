from models import get_token, renew_token



tokens = get_token()
access_token = tokens.get("access_token")
refresh_token = tokens.get("refresh_token")

new_tokens = renew_token(access_token, refresh_token)
refreshed_access_token = new_tokens.get("access_token")
refreshed_token = new_tokens.get("refresh_token")