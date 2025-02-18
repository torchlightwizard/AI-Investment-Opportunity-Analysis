import os
from dotenv import load_dotenv as env
import requests as req
import json
from datetime import datetime, timedelta

path_to_keys = "./keys/.env"
env(path_to_keys)

yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
api_key = f"{os.getenv('YOUTUBE_API_KEY')}"
video_id = ""
channel_id = ""
comment_id = ""
caption_id = ""
search_query = "new ai startup investment funding deal acquisition company tech news -tutorial -how -free -cheap -best -rich -trading -crypto -forex -shorts"
result_len = 10

# 1. Video Statistics | {viewCount, likeCount, commentCount} | response["items"][0]["statistics"]
uvideo_statistics = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={video_id}&key={api_key}"
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

res = req.get(usearch_top_videos).json()
with open("temp.json", "w") as file:
    file.write(json.dumps(res))
