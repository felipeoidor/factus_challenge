import os
from config.loader import load_json
from dotenv import load_dotenv


# Authorization Payload
def auth_payload() -> dict:
    load_dotenv()
    auth = load_json("json/payloads.json").get("auth_payload")
    auth["client_id"] = os.getenv("CLIENT_ID")
    auth["client_secret"] = os.getenv("CLIENT_SECRET")
    auth["username"] = os.getenv("USERNAME")
    auth["password"] = os.getenv("PASSWORD")
    return auth


def refresh_payload(refresh_token: str):
    load_dotenv()
    refresh = load_json("json/payloads.json").get("refresh_payload")
    refresh["client_id"] = os.getenv("CLIENT_ID")
    refresh["client_secret"] = os.getenv("CLIENT_SECRET")
    refresh["refresh_token"] = refresh_token
    return refresh
