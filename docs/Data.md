# Data
We will be sourcing our data primarily through apis and past data sources.
The apis will help us for new data predictions.
The past data will be used for training.

We will use these sources for our data:<br>
1. Youtube API
    - One Video: Statistics
        - viewCount
        - likeCount
        - commentCount
    - One Video: Details
        - publishedAt
        - channelId
        - title
        - description
        - channelTitle
        - categoryId
    - Top Searched Videos: Metadata
        - id
        - title
        - description
        - publishedAt
        - channelId
    - Top Comments: Metadata and Statistics
        - textOriginal
        - likeCount
        - publishedAt
        - totalReplyCount
2. Reddit API (Prawn)
    - Subreddit Top Posts: Details
        - id
        - subreddit_id
        - title
        - description
        - num_comments
        - score
        - upvote_ratio
        - url
    - Search Top Posts: Details
        - id
        - subreddit_id
        - title
        - description
        - num_comments
        - score
        - upvote_ratio
        - url
    - Top Comments For One Post: Body
        - id (Post Id)
        - num_comments
        - comments
            - body
            - score
    -Top Comments 
3. Google Search
    - Company Name Search: Links
        - company
        - format_time
        - search_results
        - links
            - title
            - link
    - Alternate Company search: Results/Links
        - All response objects
4. News Data IO API - https://newsdata.io/
    - Article Metadata
        - source
        - title
        - description
5. News API Org - https://newsapi.org/
    - Article Metadata
        - source
        - title
        - description
6. Market Aux API - https://www.marketaux.com/
    - Articles By Company
        - source
        - title
        - description
        - snippet
        - entities: Only 1, the Company itself
            - name
            - match_score
            - sentiment_score
    - Articles By Search
        - source
        - title
        - description
        - snippet
        - entities: List, Relevant Companies
            - name
            - match_score
            - sentiment_score
7. News DataHub API - https://newsdatahub.com/
    Their servers are down, will reattempt after they are live.
8. Pyprojects - https://pypi.org/project/pytrends/
    Not an official api and does not work without proper proxy, session and header setup. Hence not used.
9. Newspaper3k - https://newspaper.readthedocs.io/en/latest/
    Not an official api and does not work without proper proxy, session and header setup. Hence not used.