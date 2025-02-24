from dotenv import load_dotenv as env
from requests.auth import HTTPBasicAuth
import os
import requests

path_to_keys = "./keys/.env"
env(path_to_keys)

auth_params = {
    "client_id": f"{os.getenv('REDDIT_CLIENT_ID')}",
    "client_secret": f"{os.getenv('REDDIT_CLIENT_SECRET')}",
    "user_agent": f"{os.getenv('REDDIT_USER_AGENT')}",
    "username": f"{os.getenv('REDDIT_USERNAME')}",
    "password": f"{os.getenv('REDDIT_PASSWORD')}"
    }



def auth_access (client_id, client_secret, username, password, user_agent):
    try:
        auth = HTTPBasicAuth(client_id, client_secret)
        data = {
            "grant_type": "password",
            "username": username,
            "password": password,
        }
        headers = {"User-Agent": user_agent}

        res = requests.post("https://www.reddit.com/api/v1/access_token", auth=auth, data=data, headers=headers).json()
        if "access_token" not in res:
            raise ValueError("Invalid response. No items found.")
        token = res.get("access_token")
        return token
    except Exception as err:
        print(f"Failed to get reddit access token.")
        print(f"Unexpected Error: {err}")
    return None