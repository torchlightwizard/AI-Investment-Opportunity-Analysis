import os
from dotenv import load_dotenv
import requests
import json
from datetime import datetime, timedelta

path_to_keys = "./keys/.env"
load_dotenv(path_to_keys)

api_key = f"{os.getenv('YOUTUBE_API_KEY')}"
output_folder_path = "./scrap/data/youtube/"

video_id = ""
search_query = "new ai -tutorial -how -free -cheap -best -rich -trading -crypto -forex -shorts -beginners -beginner -game -gaming -walkthrough -playthrough -twitch -esports -song -songs -music -song -album -lyrics -concert -live -remix -beats -instrumental"
limit = 10



def get_response (url):
    res = requests.get(url)
    res.raise_for_status()
    res = res.json()
    return res



def write_response (output_folder_path, file_name, data):
    os.makedirs(output_folder_path, exist_ok=True)
    time_stamp = datetime.now().strftime(('%Y_%m_%dT%H_%M_%S'))
    output_file_path = os.path.join(output_folder_path, f"{file_name}_{time_stamp}.json")
    with open(output_file_path, "w") as file:
        json.dump(data, file, indent=4)
    return data



def get_video_statistics (api_key, output_folder_path, video_id):
    """
        Fetches video statistics from response["items"][0]["statistics"] and saves to a JSON file.

        Returns:
            Response Object: Video Statistics | {viewCount, likeCount, commentCount}
    """

    if not all(isinstance(arg, str) for arg in [api_key, output_folder_path, video_id]):
        raise TypeError("All Arguments must be strings.")

    try:
        url = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={video_id}&key={api_key}"
        res = get_response(url)
        if "items" not in res or not res["items"]:
            raise ValueError("Invalid response. No items found.")
        data = res["items"][0]["statistics"]
        data = {key:value for key, value in data.items() if key in ["viewCount", "likeCount", "commentCount"]}

        file_name = f"video_statistics_{video_id}"
        return write_response(output_folder_path, file_name, data)
    
    except requests.exceptions.RequestException as err:
        print(f"Request error: {err}") # possible cause: wrong api key
    except ValueError as err:
        print(f"Data error: {err}") # possible cause: wrong video id
    except Exception as err:
        print(f"Unexpected error: {err}")
    return None



def get_video_details (api_key, output_folder_path, video_id):
    """
        Fetches video details from response["items"][0]["snippet"] and saves to a JSON file.

        Returns:
            Response Object: Video Details | {title, description, publishedAt, channelId, channelTitle, categoryId}
    """

    if not all(isinstance(arg, str) for arg in [api_key, output_folder_path, video_id]):
        raise TypeError("All Arguments must be strings.")

    try:
        url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"
        res = get_response(url)
        if "items" not in res or not res["items"]:
            raise ValueError("Invalid response. No items found.")
        data = res["items"][0]["snippet"]
        data = {key:value for key, value in data.items() if key in ["title", "description", "publishedAt", "channelId", "channelTitle", "categoryId"]}

        file_name = f"video_details_{video_id}"
        return write_response(output_folder_path, file_name, data)
    
    except requests.exceptions.RequestException as err:
        print(f"Request error: {err}") # possible cause: wrong api key
    except ValueError as err:
        print(f"Data error: {err}") # possible cause: wrong video id
    except Exception as err:
        print(f"Unexpected error: {err}")
    return None



def get_top_videos (api_key, output_folder_path, search_query, limit):
    """
        Fetches top videos after search from response["items"][i] and saves to a JSON file.

        Returns:
            Response Object: Video Ids | {id[videoId]}
    """

    limit = str(limit)
    if not all(isinstance(arg, str) for arg in [api_key, output_folder_path, search_query, limit]):
        raise TypeError("All Arguments must be strings.")

    try:
        yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
        url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={search_query}&type=video&videoDuration=medium&maxResults={limit}&order=date&relevanceLanguage=en&publishedAfter={yesterday}&key={api_key}"
        res = get_response(url)
        if "items" not in res or not res["items"]:
            raise ValueError("Invalid response. No items found.")
        items = res["items"]
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
    
    except requests.exceptions.RequestException as err:
        print(f"Request error: {err}") # possible cause: wrong api key
    except ValueError as err:
        print(f"Data error: {err}") # possible cause: wrong search query
    except Exception as err:
        print(f"Unexpected error: {err}")
    return None



def get_top_comments (api_key, output_folder_path, video_id, limit):
    """
        Fetches top comments of a video from response["items"][i]["snippet"] and saves to a JSON file.

        Returns:
            Response Object: Video Top Comments and Statistics | {topLevelComment[snippet[textOriginal, likeCount, publishedAt]], totalReplyCount}
    """

    limit = str(limit)
    if not all(isinstance(arg, str) for arg in [api_key, output_folder_path, video_id, limit]):
        raise TypeError("All Arguments must be strings.")

    try:
        yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
        url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&maxResults={limit}&order=relevance&key={api_key}"
        res = get_response(url)
        if "items" not in res or not res["items"]:
            raise ValueError("Invalid response. No items found.")
        items = res["items"]
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
    
    except requests.exceptions.RequestException as err:
        print(f"Request error: {err}") # possible cause: wrong api key
    except ValueError as err:
        print(f"Data error: {err}") # possible cause: wrong video id
    except Exception as err:
        print(f"Unexpected error: {err}")
    return None