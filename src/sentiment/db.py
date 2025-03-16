from src.file_handling.read import read_from_db_df
from src.file_handling.write import write_to_db_df
from src.sentiment.calculate import calculate_sentiment
import pandas as pd

path_to_db = "./data/datawarehouse/tests/datawarehouse.duckdb"



def sentiment_youtube ():
    """
    1. Youtube<br>
        a. Positive or negative sentiment<br>
            i. Titles<br>
            ii. Descriptions<br>
    """

    df = read_from_db_df (path_to_db, "youtube")
    df = df[["company","video_title", "video_description"]]
    df["sentence"] = df["video_title"] + ". " + df["video_description"]
    df["sentiment"] = df["sentence"].apply(lambda s: calculate_sentiment(s))
    df = df.drop(["video_title", "video_description"], axis=1)
    write_to_db_df (path_to_db, "sent_youtube", df)



def sentiment_youtube_comment ():
    """
    1. Youtube<br>
        a. Positive or negative sentiment<br>
            i. Comments
    """

    df = read_from_db_df (path_to_db, "youtube_comments")
    df["sentence"] = df["text"]
    df = df[["company", "sentence", "text"]]
    df["sentiment"] = df["sentence"].apply(lambda s: calculate_sentiment(s))
    df = df.drop(["text"], axis=1)
    write_to_db_df (path_to_db, "sent_youtube_comments", df)



def sentiment_reddit ():
    """
    2. Reddit<br>
        a. Searched<br>
            i. Positive or negative sentiment<br>
                (1) Titles
                (2) Descriptions<br>
    """

    df = read_from_db_df (path_to_db, "reddit")
    df = df[["company", "title", "description"]]
    df["sentence"] =  df["title"] + ". " + df["description"]
    df["sentiment"] = df["sentence"].apply(lambda s: calculate_sentiment(s))
    df = df.drop(["title", "description"], axis=1)
    write_to_db_df (path_to_db, "sent_reddit", df)



def sentiment_reddit_comments ():
    """
    2. Reddit<br>
        a. Searched<br>
            i. Positive or negative sentiment<br>
                (1) Comments
    """

    df = read_from_db_df (path_to_db, "reddit_comments")
    df["sentence"] = df["text"]
    df = df[["company", "sentence", "text"]]
    df["sentiment"] = df["sentence"].apply(lambda s: calculate_sentiment(s))
    df = df.drop(["text"], axis=1)
    write_to_db_df (path_to_db, "sent_reddit_comments", df)



def sentiment_news_marketaux ():
    """
    3. Market Aux API<br>
        a. Positive or negative sentiment<br>
            i. Titles
            ii. Descriptions<br>
            ii. API's Sentiment Score<br>
    """

    df = read_from_db_df (path_to_db, "news_marketaux")
    df = df[["company", "title", "description", "sentiment"]]
    df = df.rename(columns={"sentiment": "sentiment_api"})
    df["sentence"] =  df["title"] + ". " + df["description"]
    df["sentiment_local"] = df["sentence"].apply(lambda s: calculate_sentiment(s))
    df = df.drop(["title", "description"], axis=1)
    write_to_db_df (path_to_db, "sent_news_marketaux", df)



def sentiment_news_apiorg ():
    """
    4. News API Org<br>
        a. Positive or negative sentiment<br>
            i. Titles
            ii. Descriptions<br>
    """

    df = read_from_db_df (path_to_db, "news_apiorg")
    df = df[["company", "title", "description"]]
    df["sentence"] =  df["title"] + ". " + df["description"]
    df["sentiment"] = df["sentence"].apply(lambda s: calculate_sentiment(s))
    df = df.drop(["title", "description"], axis=1)
    write_to_db_df (path_to_db, "sent_news_apiorg", df)



def sentiment_news_dataio ():
    """
    5. News Data IO<br>
        a. Positive or negative sentiment<br>
            i. Titles + Descriptions<br>
    """

    df = read_from_db_df (path_to_db, "news_dataio")
    df = df[["company", "title", "description"]]
    df["sentence"] =  df["title"] + ". " + df["description"]
    df["sentiment"] = df["sentence"].apply(lambda s: calculate_sentiment(s))
    df = df.drop(["title", "description"], axis=1)
    write_to_db_df (path_to_db, "sent_news_dataio", df)



def sentiment_googlesearch ():
    """
    6. Google Search<br>
        a. Positive or negative sentiment<br>
            i. Link Titles<br>
    """

    df = read_from_db_df (path_to_db, "googlesearch")
    df["sentence"] = df["title"]
    df = df[["company", "sentence", "title"]]
    df["sentiment"] = df["sentence"].apply(lambda s: calculate_sentiment(s))
    df = df.drop(["title"], axis=1)
    write_to_db_df (path_to_db, "sent_googlesearch", df)