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
    """
        Get reddit's temporary access token.

        Returns:
            Str: Access Token
    """

    try:
        if not all(isinstance(arg, str) for arg in [client_id, client_secret, username, password, user_agent]):
            raise TypeError("client_id, client_secret, username, password, user_agent arguments must be strings.")
        
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
        print(f"Function: auth_access. Unexpected Error: {err}")
        print(f"Failed to get reddit access token.")
    return None



def get_response (url, auth_params=auth_params):
    """
        Returns the response of request.

        Return:
            Dict: requests.models.Response
    """

    try:
        if not all(isinstance(arg, str) for arg in [url]):
            raise TypeError("url argument must be a string.")
        
        token = auth_access(**auth_params)
        headers = {"Authorization": f"bearer {token}", "User-Agent": auth_params["user_agent"]}
        res = requests.get(url, headers=headers)
        return res
    except Exception as err:
        print(f"Function: get_response. Unexpected Error: {err}")
        print(f"Failed to fetch or parse response.")
    return None



def get_api_limit (auth_params=auth_params):
    """
        Fetches how much api has been used out of daily limit.

        Returns:
            Dict:{
                Request_Count,
                Count_Reset"
            }
    """

    try:
        url = "https://oauth.reddit.com/api/v1/me"
        res = get_response(url)
        headers = res.headers
        if res is None:
            raise RuntimeError("Failed to get a valid response.")

        status = {}
        if "X-Ratelimit-Remaining" in headers:
            status["Request_Count"] = headers['X-Ratelimit-Remaining']
            status["Count_Reset"] = f"{headers['X-Ratelimit-Reset']} seconds"
        else:
            status = headers
        return status
    except Exception as err:
        print(f"Function: get_api_limit. Unexpected Error: {err}")
    return None