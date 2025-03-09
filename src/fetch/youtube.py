from dotenv import load_dotenv
from datetime import datetime, timedelta
import os
import requests

path_to_keys = "./keys/.env"
load_dotenv(path_to_keys)

api_key = f"{os.getenv('YOUTUBE_API_KEY')}"
limit = 10



def get_response (url):
    """
        Returns the response of request in json format.

        Return:
            Dict: requests.models.Response.text (str) or requests.models.Response.text (bytes)
    """

    res = requests.get(url)
    res.raise_for_status()
    res = res.json()
    return res



def get_video_statistics (video_id, api_key=api_key):
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
        if not all(isinstance(arg, str) for arg in [api_key, video_id]):
            raise TypeError("api_key, video_id arguments must be strings.")

        url = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={video_id}&key={api_key}"
        res = get_response(url)
        if "items" not in res:
            raise ValueError("Invalid response. No items found.")
        items = res.get("items", None)
        first_item = items[0] if isinstance(items, list) else None
        statistics = first_item.get("statistics", None) if isinstance(first_item, dict) else None
        data = {key:value for key, value in statistics.items() if key in ["viewCount", "likeCount", "commentCount"]}
        data["id"] = first_item.get("id", None)
        return data
    
    except requests.exceptions.RequestException as err:
        print(f"Function: get_video_statistics. Request error: {err}") # possible cause: wrong api key
    except ValueError as err:
        print(f"Function: get_video_statistics. Data error: {err}")
    except Exception as err:
        print(f"Function: get_video_statistics. Unexpected error: {err}")
    return None



def get_video_details (video_id, api_key=api_key):
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
        if not all(isinstance(arg, str) for arg in [api_key, video_id]):
            raise TypeError("api_key, video_id arguments must be strings.")

        url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"
        res = get_response(url)
        if "items" not in res:
            raise ValueError("Invalid response. No items found.")
        items = res.get("items", None)
        first_item = items[0] if isinstance(items, list) else None
        snippet = first_item.get("snippet", None) if isinstance(first_item, dict) else None
        data = {key:value for key, value in snippet.items() if key in ["title", "description", "publishedAt", "channelId", "channelTitle", "categoryId"]}
        data["id"] = first_item.get("id", None)
        return data
    
    except requests.exceptions.RequestException as err:
        print(f"Function: get_video_details. Request error: {err}") # possible cause: wrong api key
    except ValueError as err:
        print(f"Function: get_video_details. Data error: {err}")
    except Exception as err:
        print(f"Function: get_video_details. Unexpected error: {err}")
    return None



def get_videos (search_query, days_offset=1, api_key=api_key, limit=limit):
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
        limit = str(limit)
        search_query = search_query.replace(" ", "%20")
        if not all(isinstance(arg, str) for arg in [api_key, search_query]):
            raise TypeError("api_key, search_query arguments must be strings.")

        yesterday = (datetime.now() - timedelta(days=days_offset)).strftime('%Y-%m-%dT%H:%M:%SZ')
        url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={search_query}&type=video&videoDuration=medium&maxResults={limit}&order=relevance&relevanceLanguage=en&publishedAfter={yesterday}&key={api_key}"
        res = get_response(url)
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
    
    except requests.exceptions.RequestException as err:
        print(f"Function: get_videos. Request error: {err}") # possible cause: wrong api key
    except ValueError as err:
        print(f"Function: get_videos. Data error: {err}")
    except Exception as err:
        print(f"Function: get_videos. Unexpected error: {err}")
    return None



def get_comments (video_id, api_key=api_key, limit=limit):
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
        limit = str(limit)
        if not all(isinstance(arg, str) for arg in [api_key, video_id]):
            raise TypeError("api_key, video_id arguments must be strings.")
        
        yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
        url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&maxResults={limit}&order=relevance&key={api_key}"
        res = get_response(url)
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
    
    except requests.exceptions.RequestException as err:
        print(f"Function: get_comments. Request error: {err}") # possible cause: wrong api key
    except ValueError as err:
        print(f"Function: get_comments. Data error: {err}")
    except Exception as err:
        print(f"Function: get_comments. Unexpected error: {err}")
    return None



def get_categories (api_key=api_key):
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
        if not all(isinstance(arg, str) for arg in [api_key]):
            raise TypeError("api_key arguments must be strings.")

        url = f"https://www.googleapis.com/youtube/v3/videoCategories?part=snippet&regionCode=US&key={api_key}"
        res = get_response(url)
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
    
    except requests.exceptions.RequestException as err:
        print(f"Function: get_categories. Request error: {err}") # possible cause: wrong api key
    except ValueError as err:
        print(f"Function: get_categories. Data error: {err}")
    except Exception as err:
        print(f"Function: get_categories. Unexpected error: {err}")
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