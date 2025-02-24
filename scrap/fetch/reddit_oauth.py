from dotenv import load_dotenv as env
from datetime import datetime
import os
import praw
import json
import uuid

path_to_keys = "./keys/.env"
env(path_to_keys)

auth_params = {
    "client_id": f"{os.getenv('REDDIT_CLIENT_ID')}",
    "client_secret": f"{os.getenv('REDDIT_CLIENT_SECRET')}",
    "user_agent": f"{os.getenv('REDDIT_USER_AGENT')}",
    "redirect_uri": f"{os.getenv('URL')}:{os.getenv('Port')}",
    "path_to_token": f"{os.getenv('RPATH_TO_TOKEN')}"
    }
state = str(uuid.uuid4())
subreddits = ["MachineLearning"]
search_query = "ai fund"
output_folder_path = "./scrap/data/reddit/"
post_ids = ["", "", "", "", "", ""]



def write_response (output_folder_path, file_name, data):
    os.makedirs(output_folder_path, exist_ok=True)
    time_stamp = datetime.now().strftime(('%Y_%m_%dT%H_%M_%S'))
    output_file_path = os.path.join(output_folder_path, f"{file_name}_{time_stamp}.json")
    with open(output_file_path, "w") as file:
        json.dump(data, file, indent=4)
    return data



def auth (client_id, client_secret, user_agent, redirect_uri, path_to_token):
    """
        Gets an old TOKEN from file or a new TOKEN from a code and saves it to a JSON file.
        
        Returns:
            Reddit Object: praw.reddit.Reddit
    """

    reddit = None

    try:

        if os.path.exists(path_to_token):
            with open(path_to_token, "r") as token_json:
                token = json.load(token_json)["refresh_token"]
                if token:
                    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent, token=token)
                    return reddit

        reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent, redirect_uri=redirect_uri)
        auth_url = reddit.auth.url(scopes=["identity", "read"], state=state, duration="permanent")
        code = input(f"Please visit {auth_url}\n{redirect_uri}?code==COPY_THIS_PART#_\nEnter the OAuth code: ")
        token = reddit.auth.authorize(code) # refresh token returned
        if token is None:
            raise RuntimeError(f"Failed to get new token.")

        with open(path_to_token, "w") as token_file:
            token_json = {"refresh_token": token}
            json.dump(token_json, token_file, indent=4)
        return reddit
    except (json.JSONDecodeError, KeyError, IOError) as err:
        print(f"Failed to read or write token file.")
        print(f"File Error: {err}")
    except Exception as err:
        print(f"Failed to create and authenticate reddit instance.")
        print(f"Unexpected Error: {err}")
    return None