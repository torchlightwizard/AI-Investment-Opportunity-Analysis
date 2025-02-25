from dotenv import load_dotenv as env
from datetime import datetime
import os
import praw
import json

path_to_keys = "./keys/.env"
env(path_to_keys)

auth_params = {
    "client_id": f"{os.getenv('REDDIT_client_id')}",
    "client_secret": f"{os.getenv('REDDIT_client_secret')}",
    "user_agent": f"{os.getenv('REDDIT_USER_AGENT')}",
    "username": f"{os.getenv('REDDIT_USERNAME')}",
    "password": f"{os.getenv('REDDIT_PASSWORD')}"
    }
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



def auth (client_id, client_secret, user_agent, username, password):
    """
        Return:
            Reddit Object: praw.reddit.Reddit
    """
    try:
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent,
            username=username,
            password=password
        )
        return reddit
    except Exception as err:
        print(f"Failed to intialize reddit.")
        print(f"Unexpected Error: {err}")
    return None



def get_posts_subreddit (auth_params, subreddits, limit=20):
    subreddit_posts = []
    try:
        reddit = auth (**auth_params)
        if reddit is None:
            raise RuntimeError(f"Failed to create reddit instance.")
        
        for subreddit in subreddits:
            try:
                posts = reddit.subreddit(subreddit).top(limit=limit)

                for post in posts:
                    subreddit_post = {
                        "id": post.id,
                        "subreddit_id": post.subreddit_id,
                        "title": post.title,
                        "description":post.selftext if post.selftext else "No Description",
                        "num_comments": post.num_comments,
                        "score": post.score,
                        "upvote_ratio": post.upvote_ratio,
                        "url": post.url
                    }
                    subreddit_posts.append(subreddit_post)
            except Exception as err:
                print(f"Error fetching or handling response.")
    except Exception as err:
        print(f"Unexpected Error: {err}")

    file_name = f"subreddit_posts"
    return write_response(output_folder_path, file_name, subreddit_posts)