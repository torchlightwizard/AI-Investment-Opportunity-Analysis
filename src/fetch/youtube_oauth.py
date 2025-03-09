from dotenv import load_dotenv
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.auth.exceptions import GoogleAuthError
from datetime import datetime, timedelta
import os

path_to_keys = "./keys/.env"
load_dotenv(path_to_keys)

auth_params= {
    "path_to_secret": f"{os.getenv('PATH_TO_SECRET')}",
    "path_to_token": f"{os.getenv('YPATH_TO_TOKEN')}",
    "scopes": ["https://www.googleapis.com/auth/youtube.force-ssl"],
    "port": f"{os.getenv('PORT')}"
}
limit=10



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



def get_video_statistics (video_id, auth_params=auth_params):
    """
        Fetches video statistics.

        Returns:
            Dict: {
                viewCount,
                likeCount,
                commentCount,
                id
            }
    """
    
    try:
        if not all(isinstance(arg, str) for arg in [video_id]):
            raise TypeError("path_to_secret, path_to_token, video_id arguments must be strings.")
        
        youtube = auth(**auth_params)
        if youtube is None:
            raise RuntimeError("Failed to authenticate. Check Credentials")
        
        req = youtube.videos().list(part="statistics", id=video_id)
        res = req.execute()
        if "items" not in res:
            raise ValueError("Invalid response. No items found.")
        items = res.get("items", None)
        first_item = items[0] if isinstance(items, list) else None
        statistics = first_item.get("statistics", None) if isinstance(first_item, dict) else None
        data = {key:value for key, value in statistics.items() if key in ["viewCount", "likeCount", "commentCount"]}
        data["id"] = first_item.get("id", None)
        return data
    except ValueError as err:
        print(f"Function: get_video_statistics. Value Error: {err}")
    except KeyError as err:
        print(f"Function: get_video_statistics. Key Error: {err}")
    except Exception as err:
        print(f"Function: get_video_statistics. Unexpected Error: {err}")
    return None



def get_video_details (video_id, auth_params=auth_params):
    """
        Fetches video details.

        Returns:
            Dict: {
                publishedAt,
                channelId,
                title,
                description,
                channelTitle,
                categoryId,
                id
            }
    """

    try:
        if not all(isinstance(arg, str) for arg in [video_id]):
            raise TypeError("path_to_secret, path_to_token, video_id arguments must be strings.")

        youtube = auth(**auth_params)
        if youtube is None:
            raise RuntimeError("Failed to authenticate. Check Credentials")
        
        req = youtube.videos().list(part="snippet", id=video_id)
        res = req.execute()
        if "items" not in res:
            raise ValueError("Invalid response. No items found.")
        items = res.get("items", None)
        first_item = items[0] if isinstance(items, list) else None
        snippet = first_item.get("snippet", None) if isinstance(first_item, dict) else None
        data = {key:value for key, value in snippet.items() if key in ["title", "description", "publishedAt", "channelId", "channelTitle", "categoryId"]}
        data["id"] = first_item.get("id", None)
        return data
    except ValueError as err:
        print(f"Function: get_video_details. Value Error: {err}")
    except KeyError as err:
        print(f"Function: get_video_details. Key Error: {err}")
    except Exception as err:
        print(f"Function: get_video_details. Unexpected Error: {err}")
    return None



def get_videos (search_query, days_offset=1, auth_params=auth_params, limit=limit):
    """
        Fetches top videos after searching.

        Returns:
            List: [
                    {
                        id,
                        title,
                        description,
                        publishedAt,
                        channelId
                    },
                ]
    """

    try:
        if not all(isinstance(arg, str) for arg in [search_query]):
            raise TypeError("path_to_secret, path_to_token, search_query arguments must be strings.")

        youtube = auth(**auth_params)
        if youtube is None:
            raise RuntimeError("Failed to authenticate. Check Credentials")
        
        yesterday = (datetime.now() - timedelta(days=days_offset)).strftime('%Y-%m-%dT%H:%M:%SZ')
        req = youtube.search().list(
            part="snippet",
            q=search_query,
            type="video",
            videoDuration="medium",
            maxResults=limit,
            order="relevance",
            relevanceLanguage="en",
            publishedAfter=yesterday
        )
        res = req.execute()
        if "items" not in res:
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
        return data
    except ValueError as err:
        print(f"Function: get_videos. Value Error: {err}")
    except KeyError as err:
        print(f"Function: get_videos. Key Error: {err}")
    except Exception as err:
        print(f"Function: get_videos. Unexpected Error: {err}")
    return None



def get_comments (video_id, auth_params=auth_params, limit=limit):
    """
        Fetches top comments of a video.

        Returns:
            List: [
                    {
                        id,
                        video_id,
                        textOriginal,
                        likeCount,
                        publishedAt,
                        totalReplyCount
                    },
                ]
    """

    try:
        if not all(isinstance(arg, str) for arg in [video_id]):
            raise TypeError("path_to_secret, path_to_token, video_id arguments must be strings.")
        
        youtube = auth(**auth_params)
        if youtube is None:
            raise RuntimeError("Failed to authenticate. Check Credentials")
        
        req = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=limit,
            order="relevance"
        )
        res = req.execute()
        if "items" not in res:
            raise ValueError("Invalid response. No items found.")
        items = res.get("items", [])
        data = []
        for item in items:
            item_snippet = item["snippet"]["topLevelComment"]["snippet"]
            id = item["snippet"]["topLevelComment"]["id"]
            data.append({
                "id": id,
                "video_id": video_id,
                "textOriginal": item_snippet["textOriginal"],
                "likeCount": item_snippet["likeCount"],
                "publishedAt": item_snippet["publishedAt"],
                "totalReplyCount": item["snippet"]["totalReplyCount"]
            })
        return data
    except ValueError as err:
        print(f"Function: get_comments. Value Error: {err}")
    except KeyError as err:
        print(f"Function: get_comments. Key Error: {err}")
    except Exception as err:
        print(f"Function: get_comments. Unexpected Error: {err}")
    return None



def get_categories (auth_params=auth_params):
    """
        Fetches all categories.

        Returns:
            List: [
                    {
                        id,
                        title
                    },
                ]
    """
        
    try:
        youtube = auth(**auth_params)
        if youtube is None:
            raise RuntimeError("Failed to authenticate. Check Credentials")

        req = youtube.videoCategories().list(part="snippet", regionCode="US")
        res = req.execute()
        if "items" not in res:
            raise ValueError("Invalid response. No items found.")
        items = res.get("items", [])
        data = []
        for item in items:
            data.append({
                "id": item["id"],
                "title": item["snippet"]["title"]
            })
        return data
    except ValueError as err:
        print(f"Function: get_categories. Value Error: {err}")
    except KeyError as err:
        print(f"Function: get_categories. Key Error: {err}")
    except Exception as err:
        print(f"Function: get_categories. Unexpected Error: {err}")
    return None



def get_videos_and_related (search_query, days_offset=30, limit=10):
    try:
        videos = get_videos(search_query, days_offset=days_offset)
        videos = [{"metadata": video} for video in videos]
        if not videos:
            raise ConnectionError("Function: get_videos. Failed to get data.")

        for video in videos:
            metadata = video.get("metadata", None)
            id = metadata.get("id", None) if isinstance(metadata, dict) else None
            if id is None:
                raise ValueError("Returned faulty data with no id.")
            
            video["statistics"] = get_video_statistics(id)
            video["details"] = get_video_details(id)
            video["comments"] = get_comments(id, limit=limit)
            if video.get("statistics", None) is None:
                video["statistics"] = {}
            if video.get("details", None) is None:
                video["details"] = {}
            if video.get("comments", None) is None:
                video["comments"] = []
        return videos
    
    except ValueError as err:
        print(f"Function: get_videos_and_related. Data error: {err}")
    except Exception as err:
        print(f"Function: get_videos_and_related. Unexpected error: {err}")
    return None