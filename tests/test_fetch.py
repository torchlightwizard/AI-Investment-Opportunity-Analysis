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

from src.fetch.newsapiorg import get_headlines as a_get_headlines
from src.fetch.newsapiorg import get_headlines_next_page as a_get_headlines_next_page

from src.fetch.googlesearch import get_company_results

from src.test.test import match_keys

from src.data.schema.fetch import youtube
from src.data.schema.fetch import reddit
from src.data.schema.fetch import reddit_http
from src.data.schema.fetch import news_marketaux
from src.data.schema.fetch import news_dataio
from src.data.schema.fetch import news_apiorg
from src.data.schema.fetch import googlesearch



# def test_youtube():
#     """Youtube"""
    
#     video_id = "ekr2nIex040"
#     search_query = "new ai -tutorial -how -free -cheap -best -rich -trading -crypto -forex -shorts -beginners -beginner -game -gaming -walkthrough -playthrough -twitch -esports -song -songs -music -song -album -lyrics -concert -live -remix -beats -instrumental"
    
#     result = get_video_statistics (video_id)
#     assert isinstance(result, dict),  "Wrong return type."
#     assert match_keys(youtube["get_video_statistics"], result),  "Wrong return value."

#     result = get_video_details (video_id)
#     assert isinstance(result, dict), "Wrong return type."
#     assert match_keys(youtube["get_video_details"], result),  "Wrong return value."

#     result = get_videos (search_query)
#     assert isinstance(result, list), "Wrong return type."
#     assert match_keys(youtube["get_videos"], result),  "Wrong return value."

#     result = y_get_comments (video_id)
#     assert isinstance(result, list), "Wrong return type."
#     assert match_keys(youtube["get_comments"], result),  "Wrong return value."

#     result = get_categories ()
#     assert isinstance(result, list), "Wrong return type."
#     assert match_keys(youtube["get_categories"], result),  "Wrong return value."



# def test_youtube_oauth():
#     """Youtube Oauth"""

#     video_id = "ekr2nIex040"
#     search_query = "new ai -tutorial -how -free -cheap -best -rich -trading -crypto -forex -shorts -beginners -beginner -game -gaming -walkthrough -playthrough -twitch -esports -song -songs -music -song -album -lyrics -concert -live -remix -beats -instrumental"
    
#     result = o_get_video_statistics (video_id)
#     assert isinstance(result, dict),  "Wrong return type."
#     assert match_keys(youtube["get_video_statistics"], result),  "Wrong return value."

#     result = o_get_video_details (video_id)
#     assert isinstance(result, dict), "Wrong return type."
#     assert match_keys(youtube["get_video_details"], result),  "Wrong return value."

#     result = o_get_videos (search_query)
#     assert isinstance(result, list), "Wrong return type."
#     assert match_keys(youtube["get_videos"], result),  "Wrong return value."

#     result = o_y_get_comments (video_id)
#     assert isinstance(result, list), "Wrong return type."
#     assert match_keys(youtube["get_comments"], result),  "Wrong return value."

#     result = o_get_categories ()
#     assert isinstance(result, list), "Wrong return type."
#     assert match_keys(youtube["get_categories"], result),  "Wrong return value."



# def test_reddit():
#     """Reddit"""

#     subreddits = ["MachineLearning"]
#     search_query = "ai fund"
#     post_ids = ["gh1dj9", "1itzfy5"]

#     result = get_posts_subreddit (subreddits)
#     assert isinstance(result, list), "Wrong return type."
#     assert match_keys(reddit["get_posts_subreddit"], result),  "Wrong return value."

#     result = get_posts_searched (search_query)
#     assert isinstance(result, list), "Wrong return type."
#     assert match_keys(reddit["get_posts_searched"], result),  "Wrong return value."

#     result = r_get_comments (post_ids)
#     assert isinstance(result, list), "Wrong return type."
#     assert match_keys(reddit["get_comments"], result),  "Wrong return value."

#     result = get_posts_subreddit_and_comments (subreddits)
#     assert isinstance(result, dict),  "Wrong return type."
#     assert match_keys(reddit["get_posts_subreddit_and_comments"], result),  "Wrong return value."

#     result = get_posts_searched_and_comments (search_query)
#     assert isinstance(result, dict),  "Wrong return type."
#     assert match_keys(reddit["get_posts_searched_and_comments"], result),  "Wrong return value."



# def test_reddit_oauth():
#     """Reddit Oauth"""

#     subreddits = ["MachineLearning"]
#     search_query = "ai fund"
#     post_ids = ["gh1dj9", "1itzfy5"]

#     result = o_get_posts_subreddit (subreddits)
#     assert isinstance(result, list), "Wrong return type."
#     assert match_keys(reddit["get_posts_subreddit"], result),  "Wrong return value."

#     result = o_get_posts_searched (search_query)
#     assert isinstance(result, list), "Wrong return type."
#     assert match_keys(reddit["get_posts_searched"], result),  "Wrong return value."

#     result = o_r_get_comments (post_ids)
#     assert isinstance(result, list), "Wrong return type."
#     assert match_keys(reddit["get_comments"], result),  "Wrong return value."

#     result = o_get_posts_subreddit_and_comments (subreddits)
#     assert isinstance(result, dict),  "Wrong return type."
#     assert match_keys(reddit["get_posts_subreddit_and_comments"], result),  "Wrong return value."

#     result = o_get_posts_searched_and_comments (search_query)
#     assert isinstance(result, dict),  "Wrong return type."
#     assert match_keys(reddit["get_posts_searched_and_comments"], result),  "Wrong return value."



# def test_reddit_http():
#     """Reddit Http"""

#     result = get_api_limit ()
#     assert isinstance(result, dict),  "Wrong return type."
#     assert match_keys(reddit_http["get_api_limit"], result),  "Wrong return value."



# def test_newsmarketaux():
#     """News Market Aux"""

#     company = "TSLA"
#     search_query = "ai"

#     result = get_headlines_by_company (company)
#     assert isinstance(result, dict),  "Wrong return type."
#     assert match_keys(news_marketaux["get_headlines_by_company"], result),  "Wrong return value."

#     result = get_headlines_by_company_next_page (company)
#     assert isinstance(result, list), "Wrong return type."
#     assert match_keys(news_marketaux["get_headlines_by_company_next_page"], result),  "Wrong return value."

#     result = get_headlines_by_search (search_query)
#     assert isinstance(result, dict),  "Wrong return type."
#     assert match_keys(news_marketaux["get_headlines_by_search"], result),  "Wrong return value."

#     result = get_headlines_by_search_next_page (search_query)
#     assert isinstance(result, list), "Wrong return type."
#     assert match_keys(news_marketaux["get_headlines_by_search_next_page"], result),  "Wrong return value."



# def test_newsdataio():
#     """News Data IO"""

#     search_query = "ai artificial intelligence"

#     result = d_get_headlines (search_query)
#     assert isinstance(result, dict),  "Wrong return type."
#     assert match_keys(news_dataio["get_headlines"], result),  "Wrong return value."

#     result = d_get_headlines_next_page (search_query)
#     assert isinstance(result, list), "Wrong return type."
#     assert match_keys(news_dataio["get_headlines_next_page"], result),  "Wrong return value."



# def test_newsapiorg():
#     """News API Org"""

#     search_query = "ai artificial intelligence"

#     result = a_get_headlines (search_query)
#     assert isinstance(result, dict),  "Wrong return type."
#     assert match_keys(news_apiorg["get_headlines"], result),  "Wrong return value."

#     result = a_get_headlines_next_page (search_query)
#     assert isinstance(result, list), "Wrong return type."
#     assert match_keys(news_apiorg["get_headlines_next_page"], result),  "Wrong return value."



# def test_googlesearch():
#     """Google Search"""
    
#     search_query = "codeium"

#     result = get_company_results (search_query)
#     assert isinstance(result, list), "Wrong return type."
#     assert match_keys(googlesearch["get_company_results"], result),  "Wrong return value."