from src.extract.db import extract_youtube as d_extract_youtube
from src.extract.db import extract_youtube_oauth as d_extract_youtube_oauth
from src.extract.db import extract_reddit as d_extract_reddit
from src.extract.db import extract_reddit_oauth as d_extract_reddit_oauth
from src.extract.db import extract_news_marketaux_stocks as d_extract_news_marketaux_stocks
from src.extract.db import extract_news_marketaux_search as d_extract_news_marketaux_search
from src.extract.db import extract_news_dataio as d_extract_news_dataio
from src.extract.db import extract_news_apiorg as d_extract_news_apiorg
from src.extract.db import extract_googlesearch as d_extract_googlesearch



d_extract_youtube_oauth ()
d_extract_reddit_oauth ()
d_extract_news_marketaux_stocks ()
d_extract_news_marketaux_search ()
d_extract_news_dataio ()
d_extract_news_apiorg ()
d_extract_googlesearch ()