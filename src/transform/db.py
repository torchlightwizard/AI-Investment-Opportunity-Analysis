from src.file_handling.read import read_from_db_json
from src.file_handling.read import read_from_file
from src.file_handling.write import write_to_db_schema
import json

path_to_db_lake = "./data/datalake/tests/datalake.duckdb"
path_to_db_warehouse = "./data/datawarehouse/tests/datawarehouse.duckdb"
path_to_youtube_categories = "./data/input/youtube_o_get_categories.json"



def transform_youtube_oauth (path_to_db_lake=path_to_db_lake, path_to_db_warehouse=path_to_db_warehouse, table="youtube", comments_table="youtube_comments"):
    """Youtube Oauth"""

    data_table = read_from_db_json (path_to_db_lake, table)
    data_misc_categories = read_from_file(path_to_youtube_categories)

    for row in data_table:
        data_row = json.loads(row[0]) if isinstance(row, tuple) else []
        for item in data_row:
            if isinstance(item, dict):
                video_transformed = {}
                video_transformed["company"] = item.get("company", "")
                video_transformed["search_query"] = item.get("search_query", "")
                video_transformed["video_id"] = item.get("metadata", {}).get("id", "")
                video_transformed["video_title"] = item.get("metadata", {}).get("title", "")
                video_transformed["video_description"] = item.get("metadata", {}).get("description", "")
                video_transformed["channel_id"] = item.get("metadata", {}).get("channelId", "")
                video_transformed["channel_title"] = item.get("details", {}).get("channelTitle", "")
                video_transformed["category"] = item.get("details", {}).get("categoryId", "")
                video_transformed["category"] = [i["title"] for i in data_misc_categories if i["id"] == video_transformed["category"]][0]
                video_transformed["views"] = item.get("statistics", {}).get("viewCount", "0")
                video_transformed["likes"] = item.get("statistics", {}).get("likeCount", "0")
                video_transformed["comments"] = item.get("statistics", {}).get("commentCount", "0")
                write_to_db_schema (path_to_db_warehouse, table, video_transformed)
                
                comments = item.get("comments", [])
                for comment in comments:
                    comment_transformed = {}
                    comment_transformed["company"] = item.get("company", "")
                    comment_transformed["search_query"] = item.get("search_query", "")
                    comment_transformed["id"] = comment.get("id", "")
                    comment_transformed["video_id"] = comment.get("video_id", "")
                    comment_transformed["text"] = comment.get("textOriginal", "")
                    comment_transformed["likes"] = comment.get("likeCount", "0")
                    comment_transformed["replies"] = comment.get("totalReplyCount", "0")
                    write_to_db_schema (path_to_db_warehouse, comments_table, comment_transformed)



def transform_reddit_oauth (path_to_db_lake=path_to_db_lake, path_to_db_warehouse=path_to_db_warehouse, table="reddit", comments_table="reddit_comments"):
    """Reddit Oauth"""

    data_table = read_from_db_json (path_to_db_lake, table)

    for row in data_table:
        data_row = json.loads(row[0]) if isinstance(row, tuple) else []
        posts = data_row.get("posts", [])
        comments = data_row.get("comments", [])

        for post in posts:
            post_transformed = {}
            post_transformed["company"] = data_row.get("company", "")
            post_transformed["search_query"] = data_row.get("search_query", "")
            post_transformed["id"] = post.get("id", "")
            post_transformed["subreddit_id"] = post.get("subreddit_id", "")
            post_transformed["title"] = post.get("title", "")
            post_transformed["description"] = post.get("description", "")
            post_transformed["comments"] = post.get("num_comments", "")
            post_transformed["score"] = post.get("score", "")
            post_transformed["upvote_ratio"] = post.get("upvote_ratio", "")
            write_to_db_schema (path_to_db_warehouse, table, post_transformed)

        for comment in comments:
            comment_transformed = {}
            comment_transformed["company"] = data_row.get("company", "")
            comment_transformed["search_query"] = data_row.get("search_query", "")
            comment_transformed["id"] = comment.get("id", "")
            comment_transformed["post_id"] = comment.get("post_id", "")
            comment_transformed["text"] = comment.get("body", "")
            comment_transformed["score"] = comment.get("score", "")
            write_to_db_schema (path_to_db_warehouse, comments_table, comment_transformed)



def transform_news_marketaux (path_to_db_lake=path_to_db_lake, path_to_db_warehouse=path_to_db_warehouse, input_tables=["news_marketaux_stocks", "news_marketaux_search"], output_table="news_marketaux"):
    """News Market Aux"""

    for table in input_tables:
        data_table = read_from_db_json (path_to_db_lake, table)

        for row in data_table:
            data_row = json.loads(row[0]) if isinstance(row, tuple) else []
            data_row = data_row[0] if isinstance(data_row, list) else {}
            articles = data_row.get("data", [])

            for article in articles:
                article_transformed = {}
                article_transformed["company"] = data_row.get("company_name", "")
                article_transformed["search_query"] = data_row.get("search_query", "")
                article_transformed["source"] = article.get("source", "")
                article_transformed["title"] = article.get("title", "")
                article_transformed["description"] = article.get("description", "")
                article_transformed["sentiment"] = article.get("sentiment_score", "0")
                write_to_db_schema (path_to_db_warehouse, output_table, article_transformed)



def transform_news_dataio (path_to_db_lake=path_to_db_lake, path_to_db_warehouse=path_to_db_warehouse, table="news_dataio"):
    """News Data IO"""

    data_table = read_from_db_json (path_to_db_lake, table)

    for row in data_table:
        data_row = json.loads(row[0]) if isinstance(row, tuple) else []
        data_row = data_row[0] if isinstance(data_row, list) else {}
        articles = data_row.get("data", [])

        for article in articles:
            article_transformed = {}
            article_transformed["company"] = data_row.get("company_name", "")
            article_transformed["search_query"] = data_row.get("search_query", "")
            article_transformed["source"] = article.get("source", "")
            article_transformed["title"] = article.get("title", "")
            article_transformed["description"] = article.get("description", "")
            write_to_db_schema (path_to_db_warehouse, table, article_transformed)



def transform_news_apiorg (path_to_db_lake=path_to_db_lake, path_to_db_warehouse=path_to_db_warehouse, table="news_apiorg"):
    """News Data IO"""

    data_table = read_from_db_json (path_to_db_lake, table)

    for row in data_table:
        data_row = json.loads(row[0]) if isinstance(row, tuple) else []
        data_row = data_row[0] if isinstance(data_row, list) else {}
        articles = data_row.get("data", [])

        for article in articles:
            article_transformed = {}
            article_transformed["company"] = data_row.get("company_name", "")
            article_transformed["search_query"] = data_row.get("search_query", "")
            article_transformed["source"] = article.get("source", "")
            article_transformed["title"] = article.get("title", "")
            article_transformed["description"] = article.get("description", "")
            write_to_db_schema (path_to_db_warehouse, table, article_transformed)



def transform_googlesearch (path_to_db_lake=path_to_db_lake, path_to_db_warehouse=path_to_db_warehouse, table="googlesearch"):
    """News Data IO"""

    data_table = read_from_db_json (path_to_db_lake, table)

    for row in data_table:
        data_row = json.loads(row[0]) if isinstance(row, tuple) else []
        
        for item in data_row:
            link_transformed = {}
            link_transformed["company"] = item.get("company_name", "")
            link_transformed["search_query"] =  item.get("search_query", "")
            link_transformed["title"] = item.get("title", "0")
            link_transformed["search_results"] = item.get("search_results", "0")
            link_transformed["format_time"] = item.get("format_time", "0")
            write_to_db_schema (path_to_db_warehouse, table, link_transformed)