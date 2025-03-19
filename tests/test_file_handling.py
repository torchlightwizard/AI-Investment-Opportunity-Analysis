from src.fetch.youtube import get_video_statistics
from src.fetch.youtube import get_video_details
from src.fetch.youtube import get_videos
from src.fetch.youtube import get_comments as y_get_comments
from src.fetch.youtube import get_categories

from src.fetch.youtube_oauth import get_video_statistics as o_get_video_statistics
from src.fetch.youtube_oauth import get_video_details as o_get_video_details
from src.fetch.youtube_oauth import get_videos as o_get_videos
from src.fetch.youtube_oauth import get_comments as o_y_get_comments
from src.fetch.youtube_oauth import get_categories as o_get_categories

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

from src.file_handling.write import write_to_file
from src.file_handling.write import write_to_db_json

path_to_file = "./data/staging/tests/"
path_to_db = "./data/datalake/tests/datalake.duckdb"



# def test_file_youtube():
#     """Youtube"""

#     video_id = "ekr2nIex040"
#     search_query = "new ai -tutorial -how -free -cheap -best -rich -trading -crypto -forex -shorts -beginners -beginner -game -gaming -walkthrough -playthrough -twitch -esports -song -songs -music -song -album -lyrics -concert -live -remix -beats -instrumental"
    
#     result = write_to_file (path_to_file, "youtube_get_video_statistics", get_video_statistics (video_id))
#     assert isinstance(result, bool),  "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_file (path_to_file, "youtube_get_video_details", get_video_details (video_id))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_file (path_to_file, "youtube_get_videos", get_videos (search_query))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_file (path_to_file, "youtube_y_get_comments", y_get_comments (video_id))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_file (path_to_file, "youtube_get_categories", get_categories ())
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."



# def test_file_youtube_oauth():
#     """Youtube Oauth"""

#     video_id = "ekr2nIex040"
#     search_query = "new ai -tutorial -how -free -cheap -best -rich -trading -crypto -forex -shorts -beginners -beginner -game -gaming -walkthrough -playthrough -twitch -esports -song -songs -music -song -album -lyrics -concert -live -remix -beats -instrumental"
    
#     result = write_to_file (path_to_file, "youtube_o_get_video_statistics", o_get_video_statistics (video_id))
#     assert isinstance(result, bool),  "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_file (path_to_file, "youtube_o_get_video_details", o_get_video_details (video_id))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_file (path_to_file, "youtube_o_get_videos", o_get_videos (search_query))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_file (path_to_file, "youtube_o_y_get_comments", o_y_get_comments (video_id))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."

    # result = write_to_file (path_to_file, "youtube_o_get_categories", o_get_categories ())
    # assert isinstance(result, bool), "Wrong return type."
    # assert result == True,  "Wrong return value."



# def test_file_reddit():
#     """Reddit"""

#     subreddits = ["MachineLearning"]
#     search_query = "ai fund"
#     post_ids = ["gh1dj9", "1itzfy5"]

#     result = write_to_file (path_to_file, "reddit_get_posts_subreddit", get_posts_subreddit (subreddits))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_file (path_to_file, "reddit_get_posts_searched", get_posts_searched (search_query))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_file (path_to_file, "reddit_r_get_comments", r_get_comments (post_ids))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_file (path_to_file, "reddit_get_posts_subreddit_and_comments", get_posts_subreddit_and_comments (subreddits))
#     assert isinstance(result, bool),  "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_file (path_to_file, "reddit_get_posts_searched_and_comments", get_posts_searched_and_comments (search_query))
#     assert isinstance(result, bool),  "Wrong return type."
#     assert result == True,  "Wrong return value."



# def test_file_reddit_oauth():
#     """Reddit Oauth"""

#     subreddits = ["MachineLearning"]
#     search_query = "ai fund"
#     post_ids = ["gh1dj9", "1itzfy5"]

#     result = write_to_file (path_to_file, "reddit_o_get_posts_subreddit", o_get_posts_subreddit (subreddits))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_file (path_to_file, "reddit_o_get_posts_searched", o_get_posts_searched (search_query))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_file (path_to_file, "reddit_o_r_get_comments", o_r_get_comments (post_ids))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_file (path_to_file, "reddit_o_get_posts_subreddit_and_comments", o_get_posts_subreddit_and_comments (subreddits))
#     assert isinstance(result, bool),  "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_file (path_to_file, "reddit_o_get_posts_searched_and_comments", o_get_posts_searched_and_comments (search_query))
#     assert isinstance(result, bool),  "Wrong return type."
#     assert result == True,  "Wrong return value."



# def test_file_reddit_http():
#     """Reddit Http"""

#     result = write_to_file (path_to_file, "reddit_get_api_limit", get_api_limit ())
#     assert isinstance(result, bool),  "Wrong return type."
#     assert result == True,  "Wrong return value."



# def test_file_newsmarketaux():
#     """News Market Aux"""

#     company = "TSLA"
#     search_query = "ai"

#     result = write_to_file (path_to_file, "news_marketaux_get_headlines_by_company", get_headlines_by_company (company))
#     assert isinstance(result, bool),  "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_file (path_to_file, "news_marketaux_get_headlines_by_company_next_page", get_headlines_by_company_next_page (company))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_file (path_to_file, "news_marketaux_get_headlines_by_search", get_headlines_by_search (search_query))
#     assert isinstance(result, bool),  "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_file (path_to_file, "news_marketaux_get_headlines_by_search_next_page", get_headlines_by_search_next_page (search_query))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."



# def test_file_newsdataio():
#     """News Data IO"""

#     search_query = "ai artificial intelligence"
#     countries = "cn,fr,de,in,us"
#     categories = "business,science,technology,world"

#     result = write_to_file (path_to_file, "news_dataio_d_get_headlines", d_get_headlines (search_query, countries, categories))
#     assert isinstance(result, bool),  "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_file (path_to_file, "news_dataio_d_get_headlines_next_page", d_get_headlines_next_page (search_query, countries, categories))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."



# def test_file_newsapiorg():
#     """News API Org"""

#     search_query = "ai artificial intelligence"
#     countries = "cn,fr,de,in,us"
#     categories = "business,science,technology,world"

#     result = write_to_file (path_to_file, "news_apiorg_n_get_headlines", n_get_headlines (search_query, countries, categories))
#     assert isinstance(result, bool),  "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_file (path_to_file, "news_apiorg_n_get_headlines_next_page", n_get_headlines_next_page (search_query, countries, categories))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."



# def test_file_googlesearch():
#     """Google Search"""
    
#     search_query = "codeium"

#     result = write_to_file (path_to_file, "googlesearch_get_company_results", get_company_results (search_query))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."



# def test_db_youtube():
#     """Youtube"""

#     video_id = "ekr2nIex040"
#     search_query = "new ai -tutorial -how -free -cheap -best -rich -trading -crypto -forex -shorts -beginners -beginner -game -gaming -walkthrough -playthrough -twitch -esports -song -songs -music -song -album -lyrics -concert -live -remix -beats -instrumental"
    
#     result = write_to_db_json (path_to_db, "youtube", get_video_statistics (video_id))
#     assert isinstance(result, bool),  "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_db_json (path_to_db, "youtube", get_video_details (video_id))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_db_json (path_to_db, "youtube", get_videos (search_query))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_db_json (path_to_db, "youtube", y_get_comments (video_id))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_db_json (path_to_db, "youtube", get_categories ())
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."



# def test_db_youtube_oauth():
#     """Youtube Oauth"""

#     video_id = "ekr2nIex040"
#     search_query = "new ai -tutorial -how -free -cheap -best -rich -trading -crypto -forex -shorts -beginners -beginner -game -gaming -walkthrough -playthrough -twitch -esports -song -songs -music -song -album -lyrics -concert -live -remix -beats -instrumental"
    
#     result = write_to_db_json (path_to_db, "youtube", o_get_video_statistics (video_id))
#     assert isinstance(result, bool),  "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_db_json (path_to_db, "youtube", o_get_video_details (video_id))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_db_json (path_to_db, "youtube", o_get_videos (search_query))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_db_json (path_to_db, "youtube", o_y_get_comments (video_id))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_db_json (path_to_db, "youtube", o_get_categories ())
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."



# def test_db_reddit():
#     """Reddit"""

#     subreddits = ["MachineLearning"]
#     search_query = "ai fund"
#     post_ids = ["gh1dj9", "1itzfy5"]

#     result = write_to_db_json (path_to_db, "reddit", get_posts_subreddit (subreddits))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_db_json (path_to_db, "reddit", get_posts_searched (search_query))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_db_json (path_to_db, "reddit", r_get_comments (post_ids))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_db_json (path_to_db, "reddit", get_posts_subreddit_and_comments (subreddits))
#     assert isinstance(result, bool),  "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_db_json (path_to_db, "reddit", get_posts_searched_and_comments (search_query))
#     assert isinstance(result, bool),  "Wrong return type."
#     assert result == True,  "Wrong return value."



# def test_db_reddit_oauth():
#     """Reddit Oauth"""

#     subreddits = ["MachineLearning"]
#     search_query = "ai fund"
#     post_ids = ["gh1dj9", "1itzfy5"]

#     result = write_to_db_json (path_to_db, "reddit", o_get_posts_subreddit (subreddits))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_db_json (path_to_db, "reddit", o_get_posts_searched (search_query))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_db_json (path_to_db, "reddit", o_r_get_comments (post_ids))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_db_json (path_to_db, "reddit", o_get_posts_subreddit_and_comments (subreddits))
#     assert isinstance(result, bool),  "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_db_json (path_to_db, "reddit", o_get_posts_searched_and_comments (search_query))
#     assert isinstance(result, bool),  "Wrong return type."
#     assert result == True,  "Wrong return value."



# def test_db_reddit_http():
#     """Reddit Http"""

#     result = write_to_db_json (path_to_db, "reddit_http", get_api_limit ())
#     assert isinstance(result, bool),  "Wrong return type."
#     assert result == True,  "Wrong return value."



# def test_db_newsmarketaux():
#     """News Market Aux"""

#     company = "TSLA"
#     search_query = "ai"

#     result = write_to_db_json (path_to_db, "news_marketaux", get_headlines_by_company (company))
#     assert isinstance(result, bool),  "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_db_json (path_to_db, "news_marketaux", get_headlines_by_company_next_page (company))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_db_json (path_to_db, "news_marketaux", get_headlines_by_search (search_query))
#     assert isinstance(result, bool),  "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_db_json (path_to_db, "news_marketaux", get_headlines_by_search_next_page (search_query))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."



# def test_db_newsdataio():
#     """News Data IO"""

#     search_query = "ai artificial intelligence"
#     countries = "cn,fr,de,in,us"
#     categories = "business,science,technology,world"

#     result = write_to_db_json (path_to_db, "news_dataio", d_get_headlines (search_query, countries, categories))
#     assert isinstance(result, bool),  "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_db_json (path_to_db, "news_dataio", d_get_headlines_next_page (search_query, countries, categories))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."



# def test_db_newsapiorg():
#     """News API Org"""

#     search_query = "ai artificial intelligence"
#     countries = "cn,fr,de,in,us"
#     categories = "business,science,technology,world"

#     result = write_to_db_json (path_to_db, "news_apiorg", n_get_headlines (search_query, countries, categories))
#     assert isinstance(result, bool),  "Wrong return type."
#     assert result == True,  "Wrong return value."

#     result = write_to_db_json (path_to_db, "news_apiorg", n_get_headlines_next_page (search_query, countries, categories))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."



# def test_db_googlesearch():
#     """Google Search"""
    
#     search_query = "codeium"

#     result = write_to_db_json (path_to_db, "googlesearch", get_company_results (search_query))
#     assert isinstance(result, bool), "Wrong return type."
#     assert result == True,  "Wrong return value."