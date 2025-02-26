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
limit=10

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
        if not all(isinstance(arg, str) for arg in [path_to_secret, path_to_token]):
            raise TypeError("path_to_secret, path_to_token arguments must be strings.")

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
                    print(f"Token refresh failed, re-authenticating:", refresh_err)

        if not creds or not creds.valid:
            flow = InstalledAppFlow.from_client_secrets_file(path_to_secret, scopes)
            creds = flow.run_local_server(port=port)
            with open(path_to_token, "w") as token:
                token.write(creds.to_json())
        return creds
    
    except GoogleAuthError as err:
        print(f"Function: get_creds. Google Authentication Error: {err}")
    except ValueError as err:
        print(f"Function: get_creds. Value Error: {err}")
    except KeyError as err:
        print(f"Function: get_creds. Key Error: {err}")
    except Exception as err:
        print(f"Function: get_creds. Unexpected Error: {err}")
    return None



def get_youtube (credentials):
    """
        Gets a youtube resource to interact with the api.

        Returns:
            Resource Object: googleapiclient.discovery.Resource
    """

    try:
        youtube = build("youtube", "v3", credentials=credentials)
        return youtube
    except ValueError as err:
        print(f"Function: get_youtube. Value Error: {err}")
    except KeyError as err:
        print(f"Function: get_youtube. Key Error: {err}")
    except Exception as err:
        print(f"Function: get_youtube. Unexpected Error: {err}")
    return None



def auth (path_to_secret, path_to_token, scopes, port):
    """
        Combines get_credits and get_youtube and gives a Resource.

        Returns:
            Resource Object: googleapiclient.discovery.Resource
    """
    try:
        creds = get_creds(path_to_secret, path_to_token, scopes, port)
        if creds is None:
            raise RuntimeError("Failed to authenticate. Credentials creation failed.")
            return None
        youtube = get_youtube(creds)
        if youtube is None:
            raise RuntimeError("Failed to authenticate. Resource creation failed.")
        return youtube
    except ValueError as err:
        print(f"Function: auth. Value Error: {err}")
    except KeyError as err:
        print(f"Function: auth. Key Error: {err}")
    except Exception as err:
        print(f"Function: auth. Unexpected Error: {err}")
    return None



def get_video_statistics (path_to_secret, path_to_token, scopes, port, output_folder_path, video_id):
    """
        Fetches video statistics from response["items"][0]["statistics"] and saves to a JSON file.

        Returns:
            Response Object: Video Statistics | {viewCount, likeCount, commentCount}
    """
    
    try:
        if not all(isinstance(arg, str) for arg in [path_to_secret, path_to_token, output_folder_path, video_id]):
            raise TypeError("path_to_secret, path_to_token, output_folder_path, video_id arguments must be strings.")
        
        youtube = auth(path_to_secret, path_to_token, scopes, port)
        if youtube is None:
            raise RuntimeError("Failed to authenticate. Check Credentials")
        
        req = youtube.videos().list(part="statistics", id=video_id)
        res = req.execute()
        if "items" not in res or not res["items"]:
            raise ValueError("Invalid response. No items found.")
        items = res.get("items", None)
        first_item = items[0] if isinstance(items, list) else None
        statistics = first_item.get("statistics", None) if isinstance(first_item, dict) else None
        data = {key:value for key, value in statistics.items() if key in ["viewCount", "likeCount", "commentCount"]}

        file_name = f"video_statistics_{video_id}"
        return write_response(output_folder_path, file_name, data)
    except ValueError as err:
        print(f"Function: get_video_statistics. Value Error: {err}")
    except KeyError as err:
        print(f"Function: get_video_statistics. Key Error: {err}")
    except Exception as err:
        print(f"Function: get_video_statistics. Unexpected Error: {err}")
    return None


def get_video_details (path_to_secret, path_to_token, scopes, port, output_folder_path, video_id):
    """
        Fetches video details from response["items"][0]["snippet"] and saves to a JSON file.

        Returns:
            Response Object: Video Details | {title, description, publishedAt, channelId, channelTitle, categoryId}
    """

    try:
        if not all(isinstance(arg, str) for arg in [path_to_secret, path_to_token, output_folder_path, video_id]):
            raise TypeError("path_to_secret, path_to_token, output_folder_path, video_id arguments must be strings.")

        youtube = auth(path_to_secret, path_to_token, scopes, port)
        if youtube is None:
            raise RuntimeError("Failed to authenticate. Check Credentials")
        
        req = youtube.videos().list(part="snippet", id=video_id)
        res = req.execute()
        if "items" not in res or not res["items"]:
            raise ValueError("Invalid response. No items found.")
        items = res.get("items", None)
        first_item = items[0] if isinstance(items, list) else None
        snippet = first_item.get("snippet", None) if isinstance(first_item, dict) else None
        data = {key:value for key, value in snippet.items() if key in ["title", "description", "publishedAt", "channelId", "channelTitle", "categoryId"]}

        file_name = f"video_details_{video_id}"
        return write_response(output_folder_path, file_name, data)
    except ValueError as err:
        print(f"Function: get_video_details. Value Error: {err}")
    except KeyError as err:
        print(f"Function: get_video_details. Key Error: {err}")
    except Exception as err:
        print(f"Function: get_video_details. Unexpected Error: {err}")
    return None



def get_videos (path_to_secret, path_to_token, scopes, port, output_folder_path, search_query, limit=limit):
    """
        Fetches top videos after search from response["items"][i] and saves to a JSON file.

        Returns:
            Response Object: Video Ids | {id[videoId]}
    """

    try:
        if not all(isinstance(arg, str) for arg in [path_to_secret, path_to_token, output_folder_path, search_query]):
            raise TypeError("path_to_secret, path_to_token, output_folder_path, search_query arguments must be strings.")

        youtube = auth(path_to_secret, path_to_token, scopes, port)
        if youtube is None:
            raise RuntimeError("Failed to authenticate. Check Credentials")
        
        yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
        req = youtube.search().list(
            part="snippet",
            q=search_query,
            type="video",
            videoDuration="medium",
            maxResults=limit,
            order="date",
            relevanceLanguage="en",
            publishedAfter=yesterday
        )
        res = req.execute()
        if "items" not in res or not res["items"]:
                raise ValueError("Invalid response. No items found.")
        items = res.get("items", [])
        data = []
        for item in items:
            data.append({
                "id": item["id"]["videoId"],
                "title": item["snippet"]["title"],
                "description": item["snippet"]["description"],
                "publishedAt": item["snippet"]["publishedAt"],
                "channelId": item["snippet"]["channelId"]
            })

        file_name = f"top_videos"
        return write_response(output_folder_path, file_name, data)
    except ValueError as err:
        print(f"Function: get_videos. Value Error: {err}")
    except KeyError as err:
        print(f"Function: get_videos. Key Error: {err}")
    except Exception as err:
        print(f"Function: get_videos. Unexpected Error: {err}")
    return None



def get_comments (path_to_secret, path_to_token, scopes, port, output_folder_path, video_id, limit=limit):
    """
        Fetches top comments of a video from response["items"][i]["snippet"] and saves to a JSON file.

        Returns:
            Response Object: Video Top Comments and Statistics | {topLevelComment[snippet[textOriginal, likeCount, publishedAt]], totalReplyCount}
    """

    try:
        if not all(isinstance(arg, str) for arg in [path_to_secret, path_to_token, output_folder_path, video_id]):
            raise TypeError("path_to_secret, path_to_token, output_folder_path, video_id arguments must be strings.")
        
        youtube = auth(path_to_secret, path_to_token, scopes, port)
        if youtube is None:
            raise RuntimeError("Failed to authenticate. Check Credentials")
        
        req = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=limit,
            order="relevance"
        )
        res = req.execute()
        if "items" not in res or not res["items"]:
            raise ValueError("Invalid response. No items found.")
        items = res.get("items", [])
        data = []
        for item in items:
            item_snippet = item["snippet"]["topLevelComment"]["snippet"]
            data.append({
                "textOriginal": item_snippet["textOriginal"],
                "likeCount": item_snippet["likeCount"],
                "publishedAt": item_snippet["publishedAt"],
                "totalReplyCount": item["snippet"]["totalReplyCount"]
            })

        file_name = f"top_comments_{video_id}"
        return write_response(output_folder_path, file_name, data)
    except ValueError as err:
        print(f"Function: get_comments. Value Error: {err}")
    except KeyError as err:
        print(f"Function: get_comments. Key Error: {err}")
    except Exception as err:
        print(f"Function: get_comments. Unexpected Error: {err}")
    return None



def get_categories (path_to_secret, path_to_token, scopes, port, output_folder_path):
    """
        Fetches all categories from response["items"][i] and saves to a JSON file.

        Returns:
            Response Object: All Categories | {id, snippet[title]} | 
    """
        
    try:
        if not all(isinstance(arg, str) for arg in [path_to_secret, path_to_token, output_folder_path]):
            raise TypeError("path_to_secret, path_to_token, output_folder_path arguments must be strings.")
        
        youtube = auth(path_to_secret, path_to_token, scopes, port)
        if youtube is None:
            raise RuntimeError("Failed to authenticate. Check Credentials")
        
        req = youtube.videoCategories().list(part="snippet", regionCode="US")
        res = req.execute()
        if "items" not in res or not res["items"]:
            raise ValueError("Invalid response. No items found.")
        items = res.get("items", [])
        data = []
        for item in items:
            data.append({
                "id": item["id"],
                "title": item["snippet"]["title"]
            })

        file_name = f"categories"
        return write_response(output_folder_path, file_name, data)
    except ValueError as err:
        print(f"Function: get_categories. Value Error: {err}")
    except KeyError as err:
        print(f"Function: get_categories. Key Error: {err}")
    except Exception as err:
        print(f"Function: get_categories. Unexpected Error: {err}")
    return None

# get_video_statistics(path_to_secret, path_to_token, scopes, port, output_folder_path, video_id)
# get_video_details(path_to_secret, path_to_token, scopes, port, output_folder_path, video_id)
# get_videos(path_to_secret, path_to_token, scopes, port, output_folder_path, search_query)
# get_comments(path_to_secret, path_to_token, scopes, port, output_folder_path, video_id)
# get_categories(path_to_secret, path_to_token, scopes, port, output_folder_path)