from src.transform.file import transform_fact_table
from src.transform.db import transform_youtube_oauth
from src.transform.db import transform_reddit_oauth
from src.transform.db import transform_news_marketaux
from src.transform.db import transform_news_dataio
from src.transform.db import transform_news_apiorg
from src.transform.db import transform_googlesearch

from src.sentiment.db import sentiment_youtube
from src.sentiment.db import sentiment_youtube_comment
from src.sentiment.db import sentiment_reddit
from src.sentiment.db import sentiment_reddit_comments
from src.sentiment.db import sentiment_news_marketaux
from src.sentiment.db import sentiment_news_dataio
from src.sentiment.db import sentiment_news_apiorg
from src.sentiment.db import sentiment_googlesearch



transform_fact_table ()
transform_youtube_oauth ()
transform_reddit_oauth ()
transform_news_marketaux ()
transform_news_dataio ()
transform_news_apiorg ()
transform_googlesearch ()

sentiment_youtube ()
sentiment_youtube_comment ()
sentiment_reddit ()
sentiment_reddit_comments ()
sentiment_news_marketaux ()
sentiment_news_dataio ()
sentiment_news_apiorg ()
sentiment_googlesearch ()