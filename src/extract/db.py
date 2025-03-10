from src.fetch.youtube import get_video_statistics
from src.fetch.youtube import get_video_details
from src.fetch.youtube import get_videos
from src.fetch.youtube import get_comments as y_get_comments
from src.fetch.youtube import get_categories
from src.fetch.youtube import get_videos_and_related

from src.fetch.youtube_oauth import get_video_statistics as o_get_video_statistics
from src.fetch.youtube_oauth import get_video_details as o_get_video_details
from src.fetch.youtube_oauth import get_videos as o_get_videos
from src.fetch.youtube_oauth import get_comments as o_y_get_comments
from src.fetch.youtube_oauth import get_categories as o_get_categories
from src.fetch.youtube_oauth import get_videos_and_related as o_get_videos_and_related

from src.fetch.reddit import get_posts_subreddit
from src.fetch.reddit import get_posts_searched
from src.fetch.reddit import get_comments as r_get_comments
from src.fetch.reddit import get_posts_subreddit_and_comments
from src.fetch.reddit import get_posts_searched_and_comments

from src.fetch.reddit_oauth import get_posts_subreddit as o_get_posts_subreddit
from src.fetch.reddit_oauth import get_posts_searched as o_get_posts_searched
from src.fetch.reddit_oauth import get_comments as o_r_get_comments
from src.fetch.reddit_oauth import get_posts_subreddit_and_comments as o_get_posts_subreddit_and_comments
from src.fetch.reddit_oauth import get_posts_searched_and_comments as o_get_posts_searched_and_comments

from src.fetch.reddit_http import get_api_limit

from src.fetch.newsmarketaux import get_headlines_by_company
from src.fetch.newsmarketaux import get_headlines_by_search
from src.fetch.newsmarketaux import get_headlines_by_company_next_page
from src.fetch.newsmarketaux import get_headlines_by_search_next_page

from src.fetch.newsdataio import get_headlines as d_get_headlines
from src.fetch.newsdataio import get_headlines_next_page as d_get_headlines_next_page

from src.fetch.newsapiorg import get_headlines as n_get_headlines
from src.fetch.newsapiorg import get_headlines_next_page as n_get_headlines_next_page

from src.fetch.googlesearch import get_company_results

from src.file_handling.read import read_from_file
from src.file_handling.write import write_to_db_json

path_to_searches = "./data/input/search.json"
path_to_db = "./data/datalake/tests/datalake.duckdb"



def extract_youtube ():
    """Youtube"""

    try:
        searches = read_from_file(path_to_searches)
        keys = searches.get("keys", None)
        youtube = keys.get("youtube", None) if isinstance(keys, dict) else None
       
        for company in searches.get("company", []):
            name = company.get("name", "") if isinstance(company, dict) else ""
            if len(name) < 1:
                raise ValueError("No company to add to search query.")
            
            query = youtube[0] if isinstance(youtube, list) and (len(youtube) > 0) else ""
            search_query = name + " " + query

            videos = get_videos_and_related(search_query=search_query)
            if videos is None:
                raise ConnectionError("Failed to get data.")
            
            if len(videos) > 0:
                for video in videos:
                    video["company"] = name
                    video["search_query"] = search_query
            write_to_db_json (path_to_db, "youtube", videos)

        return True
    except Exception as err:
        print(f"Function: extract_youtube. Unexpected Error: {err}")
    return False



def extract_youtube_oauth ():
    """Youtube Oauth"""

    try:
        searches = read_from_file(path_to_searches)
        keys = searches.get("keys", None)
        youtube = keys.get("youtube", None) if isinstance(keys, dict) else None
        
        for company in searches.get("company", []):
            name = company.get("name", "") if isinstance(company, dict) else ""
            if len(name) < 1:
                raise ValueError("No company to add to search query.")
            
            query = youtube[0] if isinstance(youtube, list) and (len(youtube) > 0) else ""
            search_query = name + " " + query

            videos = o_get_videos_and_related(search_query=search_query)
            if videos is None:
                raise ConnectionError("Failed to get data.")
            
            if len(videos) > 0:
                for video in videos:
                    video["company"] = name
                    video["search_query"] = search_query
            write_to_db_json (path_to_db, "youtube", videos)

        return True
    except Exception as err:
        print(f"Function: extract_youtube_oauth. Unexpected Error: {err}")
    return False



def extract_reddit ():
    """Reddit"""

    try:
        searches = read_from_file(path_to_searches)
        keys = searches.get("keys", None)
        reddit = keys.get("reddit", None) if isinstance(keys, dict) else None
        subreddits = reddit.get("subreddits", []) if isinstance(reddit, dict) else []

        posts_and_comments = get_posts_subreddit_and_comments(subreddits=subreddits)
        if posts_and_comments is None:
            posts_and_comments = {"posts": [], "comments": []}
        write_to_db_json (path_to_db, "reddit", posts_and_comments)
        
        for company in searches.get("company", []):
            name = company.get("name", "") if isinstance(company, dict) else ""
            if len(name) < 1:
                raise ValueError("No company to add to search query.")
            
            query = reddit.get("queries", []) if isinstance(reddit, dict) else []
            query = query[0] if isinstance(query, list) and (len(query) > 0) else ""
            search_query = name + " " + query

            posts_and_comments = get_posts_searched_and_comments(search_query=search_query)
            if posts_and_comments is None:
                posts_and_comments = {"company": name, "search_query": search_query, "posts": [], "comments": []}
            posts_and_comments["company"] = name
            posts_and_comments["search_query"] = search_query
            write_to_db_json (path_to_db, "reddit", posts_and_comments)
        
        return True
    except Exception as err:
        print(f"Function: extract_reddit. Unexpected Error: {err}")
    return False



def extract_reddit_oauth ():
    """Reddit Oauth"""

    try:
        searches = read_from_file(path_to_searches)
        keys = searches.get("keys", None)
        reddit = keys.get("reddit", None) if isinstance(keys, dict) else None
        subreddits = reddit.get("subreddits", []) if isinstance(reddit, dict) else []

        posts_and_comments = o_get_posts_subreddit_and_comments(subreddits=subreddits)
        if posts_and_comments is None:
            posts_and_comments = {"posts": [], "comments": []}
        write_to_db_json (path_to_db, "reddit", posts_and_comments)
        
        for company in searches.get("company", []):
            name = company.get("name", "") if isinstance(company, dict) else ""
            if len(name) < 1:
                raise ValueError("No company to add to search query.")
            
            query = reddit.get("queries", []) if isinstance(reddit, dict) else []
            query = query[0] if isinstance(query, list) and (len(query) > 0) else ""
            search_query = name + " " + query

            posts_and_comments = o_get_posts_searched_and_comments(search_query=search_query)
            if posts_and_comments is None:
                posts_and_comments = {"company": name, "search_query": search_query, "posts": [], "comments": []}
            posts_and_comments["company"] = name
            posts_and_comments["search_query"] = search_query
            write_to_db_json (path_to_db, "reddit", posts_and_comments)
        
        return True
    except Exception as err:
        print(f"Function: extract_reddit_oauth. Unexpected Error: {err}")
    return False



def extract_news_marketaux_stocks ():
    """Market Aux API"""

    try:
        searches = read_from_file(path_to_searches)
        keys = searches.get("keys", None)
        news_marketaux = keys.get("news_marketaux", None) if isinstance(keys, dict) else None
        
        for company in searches.get("company", []):
            name = company.get("name", "") if isinstance(company, dict) else ""
            stock_indicator = company.get("stock_indicator", "") if isinstance(company, dict) else ""
            if len(name) < 1:
                raise ValueError("No company to add to search query.")
            
            query = news_marketaux[0] if isinstance(news_marketaux, list) and (len(news_marketaux) > 0) else ""
            search_query = name + " " + query

            articles = get_headlines_by_company_next_page(stock_indicator)
            if articles is None:
                articles = []
            
            for article in articles:
                if isinstance(article, dict):
                    article["company_name"] = name
                    article["company_stock_indicator"] = stock_indicator
            
            write_to_db_json(path_to_db, "news_marketaux_stocks", articles)

        return True
    except Exception as err:
        print(f"Function: extract_news_marketaux_stocks. Unexpected Error: {err}")
    return False



def extract_news_marketaux_search ():
    """Market Aux API"""

    try:
        searches = read_from_file(path_to_searches)
        keys = searches.get("keys", None)
        news_marketaux = keys.get("news_marketaux", None) if isinstance(keys, dict) else None
        
        for company in searches.get("company", []):
            name = company.get("name", "") if isinstance(company, dict) else ""
            stock_indicator = company.get("stock_indicator", "") if isinstance(company, dict) else ""
            if len(name) < 1:
                raise ValueError("No company to add to search query.")
            
            query = news_marketaux[0] if isinstance(news_marketaux, list) and (len(news_marketaux) > 0) else ""
            search_query = name
            if query:
                search_query = search_query + " " + query

            articles = get_headlines_by_search_next_page(search_query)
            if articles is None:
                articles = []
            
            for article in articles:
                if isinstance(article, dict):
                    article["company_name"] = name
                    article["search_query"] = search_query
            
            write_to_db_json(path_to_db, "news_marketaux_search", articles)

        return True
    except Exception as err:
        print(f"Function: extract_news_marketaux_search. Unexpected Error: {err}")
    return False



def extract_news_dataio ():
    """Data IO"""

    try:
        searches = read_from_file(path_to_searches)
        keys = searches.get("keys", None)
        news_dataio = keys.get("news_dataio", None) if isinstance(keys, dict) else None
        
        for company in searches.get("company", []):
            name = company.get("name", "") if isinstance(company, dict) else ""
            stock_indicator = company.get("stock_indicator", "") if isinstance(company, dict) else ""
            if len(name) < 1:
                raise ValueError("No company to add to search query.")
            
            query = news_dataio[0] if isinstance(news_dataio, list) and (len(news_dataio) > 0) else ""
            search_query = name
            if query:
                search_query = search_query + " " + query

            articles = d_get_headlines_next_page(search_query)
            if articles is None:
                articles = []
            
            for article in articles:
                if isinstance(article, dict):
                    article["company_name"] = name
                    article["search_query"] = search_query
            
            write_to_db_json(path_to_db, "news_dataio", articles)

        return True
    except Exception as err:
        print(f"Function: extract_news_dataio. Unexpected Error: {err}")
    return False



def extract_news_apiorg ():
    """Market Aux API"""

    try:
        searches = read_from_file(path_to_searches)
        keys = searches.get("keys", None)
        news_apiorg = keys.get("news_apiorg", None) if isinstance(keys, dict) else None
        
        for company in searches.get("company", []):
            name = company.get("name", "") if isinstance(company, dict) else ""
            stock_indicator = company.get("stock_indicator", "") if isinstance(company, dict) else ""
            if len(name) < 1:
                raise ValueError("No company to add to search query.")
            
            query = news_apiorg[0] if isinstance(news_apiorg, list) and (len(news_apiorg) > 0) else ""
            search_query = name
            if query:
                search_query = search_query + " " + query

            articles = n_get_headlines_next_page(search_query)
            if articles is None:
                articles = []
            
            for article in articles:
                if isinstance(article, dict):
                    article["company_name"] = name
                    article["search_query"] = search_query
            
            write_to_db_json(path_to_db, "news_apiorg", articles)

        return True
    except Exception as err:
        print(f"Function: extract_news_apiorg. Unexpected Error: {err}")
    return False



def extract_googlesearch ():
    """Market Aux API"""

    try:
        searches = read_from_file(path_to_searches)
        keys = searches.get("keys", None)
        googlesearch = keys.get("googlesearch", None) if isinstance(keys, dict) else None
        
        for company in searches.get("company", []):
            name = company.get("name", "") if isinstance(company, dict) else ""
            stock_indicator = company.get("stock_indicator", "") if isinstance(company, dict) else ""
            if len(name) < 1:
                raise ValueError("No company to add to search query.")
            
            query = googlesearch[0] if isinstance(googlesearch, list) and (len(googlesearch) > 0) else ""
            search_query = name
            if query:
                search_query = search_query + " " + query

            articles = get_company_results(search_query)
            if articles is None:
                articles = []
            
            for article in articles:
                if isinstance(article, dict):
                    article["company_name"] = name
                    article["search_query"] = search_query

            write_to_db_json (path_to_db, "googlesearch", articles)

        return True
    except Exception as err:
        print(f"Function: extract_news_apiorg. Unexpected Error: {err}")
    return False