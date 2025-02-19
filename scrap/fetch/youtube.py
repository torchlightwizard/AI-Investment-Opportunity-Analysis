import os
from dotenv import load_dotenv as env
import requests
import json
from datetime import datetime, timedelta

path_to_keys = "./keys/.env"
env(path_to_keys)

yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
api_key = f"{os.getenv('YOUTUBE_API_KEY')}"
output_folder_path = "./scrap/data/youtube/"
video_id = ""
channel_id = ""
comment_id = ""
caption_id = ""
search_query = "new ai startup investment funding deal acquisition company tech news -tutorial -how -free -cheap -best -rich -trading -crypto -forex -shorts"
result_len = 10

# 2. Video Details | {title, description, publishedAt, channelId, channelTitle, categoryId, tags} | response["items"][0]["snippet"]
uvideo_details = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"
# 3. Channel Id | {channelId} | response["items"][0]["snippet"]
uchannel_id = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"
# 4. Video Ids | {id[videoId]} | response["items"][i]
usearch_top_videos = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={search_query}&type=video&videoDuration=medium&maxResults={result_len}&order=date&publishedAfter={yesterday}&key={api_key}"
# 5.Video Top Comments and Statistics | {topLevelComment[id, snippet[textOriginal, likeCount, publishedAt]], totalReplyCount} | response["items"][i]["snippet"]
utop_comments = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&maxResults={result_len}&order=relevance&key={api_key}"
# 6. All Categories | {id, snippet[title]} | res["items"][i]
ucategories_list = f"https://www.googleapis.com/youtube/v3/videoCategories?part=snippet&regionCode=US&key={api_key}"

def get_video_statistics (api_key, output_folder_path, video_id):
    """
        Fetches video statistics (views, likes, comments) and saves to a JSON file.

        Returns:
            Response Object: Video Statistics | {viewCount, likeCount, commentCount} | response["items"][0]["statistics"] 
    """

    if not all(isinstance(arg, str) for arg in [api_key, output_folder_path, video_id]):
        raise TypeError("All Arguments must be strings.")

    try:
        url = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={video_id}&key={api_key}"
        res = requests.get(url)
        res.raise_for_status()
        data = res.json()
        if "items" not in data or not data["items"]:
            raise ValueError("Invalid response. No items found.")
        data = data["items"][0]["statistics"]

        time_stamp = datetime.now().strftime(('%Y_%m_%dT%H_%M_%S'))
        os.makedirs(output_folder_path, exist_ok=True)
        output_file_path = os.path.join(output_folder_path, f"video_statistics_{video_id}_{time_stamp}.json")
        with open(output_file_path, "w") as file:
            json.dump(data, file, indent=4)
        return data
    
    except requests.exceptions.RequestException as err:
        print(f"Request error: {err}")
    except ValueError as err:
        print(f"Data error: {err}")
    except Exception as err:
        print(f"Unexpected error: {err}")
    return None

get_video_statistics(api_key, output_folder_path, video_id)