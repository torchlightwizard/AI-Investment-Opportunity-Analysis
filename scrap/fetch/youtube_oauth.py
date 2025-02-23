from dotenv import load_dotenv
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.auth.exceptions import GoogleAuthError
from datetime import datetime, timedelta
import os
import json

path_to_keys = "./keys/.env"
load_dotenv(path_to_keys)

path_to_secret = f"{os.getenv('PATH_TO_SECRET')}"
path_to_token = f"{os.getenv('YPATH_TO_TOKEN')}"
port = f"{os.getenv('PORT')}"

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
video_id = ""
output_folder_path = "./scrap/data/youtube/"
search_query = "new ai -tutorial -how -free -cheap -best -rich -trading -crypto -forex -shorts -beginners -beginner -game -gaming -walkthrough -playthrough -twitch -esports -song -songs -music -song -album -lyrics -concert -live -remix -beats -instrumental"



def write_response (output_folder_path, file_name, data):
    os.makedirs(output_folder_path, exist_ok=True)
    time_stamp = datetime.now().strftime(('%Y_%m_%dT%H_%M_%S'))
    output_file_path = os.path.join(output_folder_path, f"{file_name}_{time_stamp}.json")
    with open(output_file_path, "w") as file:
        json.dump(data, file, indent=4)
    return data



def get_creds (path_to_secret, path_to_token, scopes, port):
    """
        Gets an old TOKEN from file or a new TOKEN from secret and saves it to a JSON file.
        
        Returns:
            Credentials Objec: google.oauth2.credentials.Credentials
    """

    try:
        port = int(port)
        creds = None
        if os.path.exists(path_to_token):
            creds = Credentials.from_authorized_user_file(path_to_token)
            if creds and creds.expired and creds.refresh_token:
                try:
                    creds.refresh(Request())
                    with open(path_to_token, "w") as token:
                        token.write(creds.to_json())
                except GoogleAuthError as refresh_err:
                    print("Token refresh failed, re-authenticating:", refresh_err)

        if not creds or not creds.valid:
            flow = InstalledAppFlow.from_client_secrets_file(path_to_secret, scopes)
            creds = flow.run_local_server(port=port)
            with open(path_to_token, "w") as token:
                token.write(creds.to_json())
        return creds
    
    except GoogleAuthError as err:
        print(f"Google Authentication Error: {err}")
    except Exception as err:
        print(f"Unexpected Error: {err}")
    return None