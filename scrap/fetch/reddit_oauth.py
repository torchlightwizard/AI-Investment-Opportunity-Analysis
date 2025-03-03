from dotenv import load_dotenv as env
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
    "redirect_uri": f"{os.getenv('URL')}:{os.getenv('PORT')}",
    "path_to_token": f"{os.getenv('RPATH_TO_TOKEN')}"
    }
state = str(uuid.uuid4())
limit=5



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



def get_posts_subreddit (subreddits, days_offset="day", auth_params=auth_params, limit=limit):
    """
        Fetches top posts from a subreddit.

        Returns:
            List: [
                {
                    id,
                    subreddit_id,
                    title,
                    description,
                    num_comments,
                    score,
                    upvote_ratio,
                    url
                },
            ]
    """
        
    subreddit_posts = []
    try:
        reddit = auth (**auth_params)
        if reddit is None:
            raise RuntimeError(f"Failed to create reddit instance.")
        
        for subreddit in subreddits:
            try:
                posts = reddit.subreddit(subreddit).top(time_filter=days_offset, limit=limit)

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
                return None
        return subreddit_posts
    except ValueError as err:
        print(f"Function: get_posts_subreddit. Value Error: {err}")
    except KeyError as err:
        print(f"Function: get_posts_subreddit. Key Error: {err}")
    except Exception as err:
        print(f"Function: get_posts_subreddit. Unexpected Error: {err}")
    return None



def get_posts_searched (search_query, days_offset="day", auth_params=auth_params, limit=limit):
    """
        Fetches top posts from the whole of reddit after searching.

        Returns:
            List: [
                {
                    id,
                    subreddit_id,
                    title,
                    description,
                    num_comments,
                    score,
                    upvote_ratio,
                    url
                },
            ]
    """
        
    reddit_posts = []
    try:
        reddit = auth (**auth_params)
        if reddit is None:
            raise RuntimeError(f"Failed to create reddit instance.")

        if not all(isinstance(arg, str) for arg in [search_query]):
            raise TypeError("search_query argument must be a string.")

        posts = reddit.subreddit("all").search(search_query, sort="new", time_filter=days_offset, limit=limit)

        for post in posts:
            reddit_post = {
                "id": post.id,
                "subreddit_id": post.subreddit_id,
                "title": post.title,
                "description":post.selftext if post.selftext else "No Description",
                "num_comments": post.num_comments,
                "score": post.score,
                "upvote_ratio": post.upvote_ratio,
                "url": post.url
            }
            reddit_posts.append(reddit_post)
        return reddit_posts
    except ValueError as err:
        print(f"Function: get_posts_searched. Value Error: {err}")
    except KeyError as err:
        print(f"Function: get_posts_searched. Key Error: {err}")
    except Exception as err:
        print(f"Function: get_posts_searched. Unexpected Error: {err}")
    return None



def get_comments (post_ids, auth_params=auth_params):
    """
        Fetches top all comments from a reddit/subreddit post.

        Returns:
            List: [
                {
                    id,
                    body,
                    score,
                    post_id
                },
            ]
    """
        
    post_ids = [f"t3_{id}" for id in post_ids]
    reddit_comments = []
    try:
        reddit = auth (**auth_params)
        if reddit is None:
            raise RuntimeError(f"Failed to create reddit instance.")
        
        posts = reddit.info(fullnames=post_ids)
        for post in posts:
            try:
                post.comments.replace_more(limit=0)
                comments = post.comments.list()
                post_id = post.id

                for comment in comments:
                    reddit_comment = {
                        "id": comment.id,
                        "body": comment.body, 
                        "score": comment.score,
                        "post_id": post_id,
                        }
                    reddit_comments.append(reddit_comment)
            
            except Exception as err:
                print(f"Error fetching or handling response.")
                return None
        return reddit_comments
    except ValueError as err:
        print(f"Function: get_comments. Value Error: {err}")
    except KeyError as err:
        print(f"Function: get_comments. Key Error: {err}")
    except Exception as err:
        print(f"Function: get_comments. Unexpected Error: {err}")
    return None



def get_posts_subreddit_and_comments(subreddits, days_offset="day", auth_params=auth_params, limit=2):
    """
        Fetches top posts from a subreddit and all comments of that post.

        Returns:
            Dict: {
                posts: 
                    List: [
                        {
                            id,
                            subreddit_id,
                            title,
                            description,
                            num_comments,
                            score,
                            upvote_ratio,
                            url
                        },
                    ],
                comments: 
                    List: [
                        {
                            id,
                            body,
                            score,
                            post_id
                        },
                    ]
            }
    """

    try:
        posts = get_posts_subreddit(subreddits, days_offset, limit=limit)
        post_ids = []
        for post in posts:
            post_ids.append(post["id"])
        comments = get_comments(post_ids)
        return {
            "posts": posts,
            "comments": comments
        }
    except Exception as err:
        print(f"Function: get_posts_subreddit_and_comments. Unexpected Error: {err}")
    return None



def get_posts_searched_and_comments(search_query, days_offset="day", auth_params=auth_params, limit=2):
    """
        Fetches top posts from the whole of reddit after searching  and all comments of that post.

        Returns:
            Dict: {
                posts: 
                    List: [
                        {
                            id,
                            subreddit_id,
                            title,
                            description,
                            num_comments,
                            score,
                            upvote_ratio,
                            url
                        },
                    ],
                comments: 
                    List: [
                        {
                            id,
                            body,
                            score,
                            post_id
                        },
                    ]
            }
    """

    try:
        if not all(isinstance(arg, str) for arg in [search_query]):
            raise TypeError("search_query argument must be a string.")
        posts = get_posts_searched(search_query, days_offset, limit=limit)
        post_ids = []
        for post in posts:
            post_ids.append(post["id"])
        comments = get_comments(post_ids)
        return {
            "posts": posts,
            "comments": comments
        }
    except ValueError as err:
        print(f"Function: get_posts_searched_and_comments. Value Error: {err}")
    except KeyError as err:
        print(f"Function: get_posts_searched_and_comments. Key Error: {err}")
    except Exception as err:
        print(f"Function: get_posts_searched_and_comments. Unexpected Error: {err}")
    return None