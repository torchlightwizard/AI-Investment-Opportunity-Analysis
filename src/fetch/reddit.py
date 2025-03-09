from dotenv import load_dotenv as env
import os
import praw

path_to_keys = "./keys/.env"
env(path_to_keys)

auth_params = {
    "client_id": f"{os.getenv('REDDIT_CLIENT_ID')}",
    "client_secret": f"{os.getenv('REDDIT_CLIENT_SECRET')}",
    "user_agent": f"{os.getenv('REDDIT_USER_AGENT')}",
    "username": f"{os.getenv('REDDIT_USERNAME')}",
    "password": f"{os.getenv('REDDIT_PASSWORD')}"
    }
limit=5



def auth (client_id, client_secret, user_agent, username, password):
    """
        Gets a reddit object to interact with the api.
        
        Return:
            Reddit Object: praw.reddit.Reddit
    """

    try:
        if not all(isinstance(arg, str) for arg in [client_id, client_secret, user_agent, username, password]):
            raise TypeError("client_id, client_secret, user_agent, username, password arguments must be strings.")
        
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent,
            username=username,
            password=password
        )
        return reddit
    except ValueError as err:
        print(f"Function: auth. Value Error: {err}")
    except KeyError as err:
        print(f"Function: auth. Key Error: {err}")
    except Exception as err:
        print(f"Function: auth. Unexpected Error: {err}")
    print(f"Failed to intialize reddit.")
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

        posts = reddit.subreddit("all").search(search_query, sort="hot", time_filter=days_offset, limit=limit)

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
        if posts is None:
            posts = []

        post_ids = []
        for post in posts:
            if post.get("id", None) is not None:
                post_ids.append(post.get("id"))
        comments = get_comments(post_ids)

        if comments is None:
            comments = []
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
        if posts is None:
            posts = []

        post_ids = []
        for post in posts:
            if post.get("id", None) is not None:
                post_ids.append(post.get("id"))
        comments = get_comments(post_ids)
        
        if comments is None:
            comments = []
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