from src.file_handling.read import read_from_db_df
from src.load.misc import fill_blanks
import pandas as pd

path_to_db = "./data/datawarehouse/tests/datawarehouse.duckdb"



def fact_options ():
    df = read_from_db_df (path_to_db, "fact")
    df = df["name"]
    return df



def engagement_youtube_avg_views (company=""):
    """List Searched Videos: Avg Views"""

    df = read_from_db_df (path_to_db, "youtube")
    df = df[["company", "views"]]
    df["views"] = df["views"].astype(int)
    df = df.groupby("company").mean().round(2)
    df = df.reset_index()
    df = df[df["company"] == company]
    return df



def engagement_youtube_avg_likes (company=""):
    """List Searched Videos: Avg Likes"""

    df = read_from_db_df (path_to_db, "youtube")
    df = df[["company", "likes"]]
    df["likes"] = df["likes"].astype(int)
    df = df.groupby("company").mean().round(2)
    df = df.reset_index()
    df = df[df["company"] == company]
    return df



def engagement_youtube_avg_comments (company=""):
    """List Searched Videos: Avg Comments"""

    df = read_from_db_df (path_to_db, "youtube")
    df = df[["company", "comments"]]
    df["comments"] = df["comments"].astype(int)
    df = df.groupby("company").mean().round(2)
    df = df.reset_index()
    df = df[df["company"] == company]
    return df



def engagement_youtube_avg_comment_likes (company=""):
    """List Searched Videos: Avg Comment Likes"""

    df = read_from_db_df (path_to_db, "youtube_comments")
    df = df[["company", "likes"]]
    df["likes"] = df["likes"].astype(int)
    df = df.groupby("company").mean().round(2)
    df = df.reset_index()
    df = df[df["company"] == company]
    return df



def engagement_reddit_avg_score (company=""):
    """List Searched Post: Avg Score"""

    df = read_from_db_df (path_to_db, "reddit")
    df = df[df["company"].str.len() > 0]
    df = df[["company", "score"]]
    df["score"] = df["score"].astype(int)
    df = df.groupby("company").mean().round(2)
    df = df.reset_index()
    df = df[df["company"] == company]
    return df



def engagement_reddit_avg_upvote_ratio (company=""):
    """List Searched Post: Avg Upvote Ratio"""

    df = read_from_db_df (path_to_db, "reddit")
    df = df[df["company"].str.len() > 0]
    df = df[["company", "upvote_ratio"]]
    df["upvote_ratio"] = df["upvote_ratio"].astype(float)
    df = df.groupby("company").mean().round(2)
    df = df.reset_index()
    df = df[df["company"] == company]
    return df



def engagement_reddit_avg_comments (company=""):
    """List Searched Post: Avg Comments"""

    df = read_from_db_df (path_to_db, "reddit")
    df = df[df["company"].str.len() > 0]
    df = df[["company", "comments"]]
    df["comments"] = df["comments"].astype(int)
    df = df.groupby("company").mean().round(2)
    df = df.reset_index()
    df = df[df["company"] == company]
    return df



def engagement_reddit_avg_comment_score (company=""):
    """List Searched Post: Avg Comment Score"""

    df = read_from_db_df (path_to_db, "reddit_comments")
    df = df[df["company"].str.len() > 0]
    df = df[["company", "score"]]
    df["score"] = df["score"].astype(int)
    df = df.groupby("company").mean().round(2)
    df = df.reset_index()
    df = df[df["company"] == company]
    return df



def engagement_googlesearch_search_results (company=""):
    """Search Result: Count"""

    df = read_from_db_df (path_to_db, "googlesearch")
    df = df[["company", "search_results"]]
    df["search_results"] = df["search_results"].astype(int)
    df = df.groupby("company").mean().round(2)
    df = df.reset_index()
    df = df[df["company"] == company]
    return df



def engagement_googlesearch_format_time (company=""):
    """Format Time"""

    df = read_from_db_df (path_to_db, "googlesearch")
    df = df[["company", "format_time"]]
    df["format_time"] = df["format_time"].astype(float)
    df = df.groupby("company").mean().round(2)
    df = df.reset_index()
    df = df[df["company"] == company]
    return df



def sentiment_youtube_videos (company=""):
    """Titles + Descriptions"""

    df = read_from_db_df (path_to_db, "sent_youtube")
    df = df[["company", "sentiment"]]
    df = df.value_counts().reset_index().sort_values(by=["company", "sentiment"])
    df["sentiment"] = df["sentiment"].replace({1: "Positive", 0: "Neutral", -1: "Negative"})
    df = df[df["company"] == company]
    df = fill_blanks (df, company)
    return df



def sentiment_youtube_comments (company=""):
    """Comments"""

    df = read_from_db_df (path_to_db, "sent_youtube_comments")
    df = df[["company", "sentiment"]]
    df = df.value_counts().reset_index().sort_values(by=["company", "sentiment"])
    df["sentiment"] = df["sentiment"].replace({1: "Positive", 0: "Neutral", -1: "Negative"})
    df = df[df["company"] == company]
    df = fill_blanks (df, company)
    return df



def sentiment_reddit_posts (company=""):
    """Titles + Descriptions"""

    df = read_from_db_df (path_to_db, "sent_reddit")
    df = df[["company", "sentiment"]]
    df = df[df["company"].str.len() > 0]
    df = df.value_counts().reset_index().sort_values(by=["company", "sentiment"])
    df["sentiment"] = df["sentiment"].replace({1: "Positive", 0: "Neutral", -1: "Negative"})
    df = df[df["company"] == company]
    df = fill_blanks (df, company)
    return df



def sentiment_reddit_comments (company=""):
    """Comments"""

    df = read_from_db_df (path_to_db, "sent_reddit_comments")
    df = df[["company", "sentiment"]]
    df = df[df["company"].str.len() > 0]
    df = df.value_counts().reset_index().sort_values(by=["company", "sentiment"])
    df["sentiment"] = df["sentiment"].replace({1: "Positive", 0: "Neutral", -1: "Negative"})
    df = df[df["company"] == company]
    df = fill_blanks (df, company)
    return df



def sentiment_news_marketaux (company=""):
    """Titles + Descriptions + API's Sentiment Score"""

    df = read_from_db_df (path_to_db, "sent_news_marketaux")
    df["sentiment_api"] = df["sentiment_api"].astype(float)
    df["binned_sentiment_api"] = pd.cut(df["sentiment_api"], 3, labels=["Negative", "Neutral", "Positive"])
    df = df[["company", "binned_sentiment_api"]]
    df = df.rename(columns={"binned_sentiment_api": "sentiment"})
    df = df.value_counts().reset_index().sort_values(by=["company", "sentiment"])
    df = df[df["company"] == company]
    df = fill_blanks (df, company)
    return df



def sentiment_news_apiorg (company=""):
    """Titles + Descriptions"""

    df = read_from_db_df (path_to_db, "sent_news_apiorg")
    df = df[["company", "sentiment"]]
    df = df.value_counts().reset_index().sort_values(by=["company", "sentiment"])
    df["sentiment"] = df["sentiment"].replace({1: "Positive", 0: "Neutral", -1: "Negative"})
    df = df[df["company"] == company]
    df = fill_blanks (df, company)
    return df



def sentiment_news_dataio (company=""):
    """Titles + Descriptions"""

    df = read_from_db_df (path_to_db, "sent_news_dataio")
    df = df[["company", "sentiment"]]
    df = df.value_counts().reset_index().sort_values(by=["company", "sentiment"])
    df["sentiment"] = df["sentiment"].replace({1: "Positive", 0: "Neutral", -1: "Negative"})
    df = df[df["company"] == company]
    df = fill_blanks (df, company)
    return df



def sentiment_googlesearch (company=""):
    """Titles"""

    df = read_from_db_df (path_to_db, "sent_googlesearch")
    df = df[["company", "sentiment"]]
    df = df.value_counts().reset_index().sort_values(by=["company", "sentiment"])
    df["sentiment"] = df["sentiment"].replace({1: "Positive", 0: "Neutral", -1: "Negative"})
    df = df[df["company"] == company]
    df = fill_blanks (df, company)
    return df