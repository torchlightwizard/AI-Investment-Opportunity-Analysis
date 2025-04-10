# Suggested Requirements

Before we begin our project. What is our target audience and what are their goals that they can achieve with this dashboard/pipeline?<br>
Our target audience will be us or anyone who wishes to find sentiment surrounding an ai company. We will accomplish this using a variety of platforms. Below are some of the KPIs and charts we might be interested in.<br>



# Metrics

Our goals in this analysis can be:
1. Measure Engagement
2. Measure Sentiment
3. Find new companies: By Similarity
4. Find new companies: Entity Recognition (Blind search)

For following timeframes we can get data:
1. day
2. week
3. month

For the following criteria we can get data:
1. Popularity
2. Latest

Our sources are:
1. Youtube
2. Reddit
3. Google Search
4. News Data IO
5. News API Org
6. Market Aux API

We have some options for searching:
1. Search for company name
2. Search for company name with additional keywords
3. Search relevant keywords without company name
4. Search keywords to find new/relevant companies



# Proposal Version 1: Engagement Metrics Dashboard

With a mindset to create value first instead of diving into deeper uncharted analysis.
1. First we will first focus on basic kpi and metric building.
2. We will collect data to fill these kpis and metrics in a time series fashion.
3. A dashboard will be created to highlight and showcase these kpis and metrics.
4. Then we will apply statististical anlaysis for hypothesis testing and finding actionable insights.

## Data Criteria

The search criteria is selected as:
1. Search for company name
2. Search for company name with additional keywords<br>
    1. Positive<br>
        1. Stock Performance<br>
        2. Market Analysis<br>
        3. Funding Round<br>
        4. Revenue Growth<br>
        5. Valuation<br>
        6. Acquisition Rumors<br>
        7. IPO<br>
        8. Investor Sentiment<br>
        9. Why People Love<br>
    2. Negative<br>
        1. Layoffs<br>
        2. Investor Exit<br>
        3. Scandals<br>
        4. Revenue Decline<br>
        5. Valuation Drop<br>
        6. Why People Hate<br>
        7. Backlash<br>

## KPIs

We can easily scoop up the following kpis and metrics:
1. Youtube<br>
    1. List Searched Videos: Max Views<br>
    2. List Searched Videos: Max Likes<br>
    3. List Searched Videos: Max Comments<br>
    4. List Searched Videos: Max Comment Likes<br>
    5. List Searched Videos: Max Comment Replies<br>

    6. List Searched Videos: Avg Views<br>
    7. List Searched Videos: Avg Likes<br>
    8. List Searched Videos: Avg Comments<br>
    9. List Searched Videos: Avg Comment Likes<br>
    10. List Searched Videos: Avg Comment Replies<br>

    11. List Searched Videos Count<br>
2. Reddit<br>
    1. List Searched Post: Max Score<br>
    2. List Searched Post: Max Upvote Ratio<br>
    3. List Searched Post: Max Comments<br>
    4. List Searched Post: Max Comment Score<br>
    5. List Searched Post: Max Comment Replies<br>

    6. List Searched Post: Avg Score<br>
    7. List Searched Post: Avg Upvote Ratio<br>
    8. List Searched Post: Avg Comments<br>
    9. List Searched Post: Avg Comment Score<br>
    10. List Searched Post: Avg Comment Replies<br>
3. Google Search<br>
    1. Search Result: Count<br>
    2. Format Time<br>
4. News Data IO API<br>
    1. Search Result: Count<br>
    2. Description Length<br>
    3. Source<br>
5. News API Org<br>
    1. Search Result: Count<br>
    2. Description Length<br>
    3. Source<br>
6. Market Aux API<br>
    1. Search Query Result: Count<br>
    2. Search Query Result: Description Length<br>
    3. Search Query Result: Source<br>
    4. Search Query Result Entities and Sentiment: Scores List<br>
    5. Search Query Result Entity With: Max Sentiment Score<br>
    6. Search Query Result: Avg Sentiment Scores<br>

    7. Search Company Result: Count<br>
    8. Search Company Result: Description Length<br>
    9. Search Company Result: Source<br>
    10. Search Company Result: Entities and Sentiment: Scores List<br>
    11. Search Company Result Entity With: Max Sentiment Score<br>
    12. Search Company Result: Avg Sentiment Scores<br>



# Proposal Version 2: Sentiment Analsis, Data Collection and Dashboard

When and if substantial data has been collected.<br>
1. We will use sentiment analysis to find a basic positive or negative score associated with text of each company.<br>
1. day<br>
2. week<br>
3. month (if possible)<br>
2. The "BERT" model/transformer will be used for this. It will be pretrained on another dataset which is yet to be decided.
3. Finally per company, per timeframe sentiment score will be added to our dashboard.

## Data Collection

For proposal version 3, we needed positive and negative texts separate from one another. Though we are limitd by our free plans, we can accomodate maybe something like two per day.

We can collect data from these:
1. Youtube<br>
    1. List Searched Videos: Titles<br>
    2. List Searched Videos: Descriptions<br>
    3. List Searched Videos: Categories<br>
    4. List Searched Videos: Comments<br>
2. Reddit<br>
    1. List Searched Post: Titles<br>
    2. List Searched Post: Descriptions<br>
    3. List Searched Post: Comments<br>

    4. List Subreddit Top Post: Titles<br>
    5. List Subreddit Top Post: Descriptions<br>
    6. List Subreddit Top Post: Comments<br>
3. Google Search<br>
    1. Link Titles<br>
4. News Data IO<br>
    1. List Searched Articles: Titles<br>
    2. List Searched Articles: Descriptions<br>
    3. List Searched Articles: Sources<br>
5. News API Org<br>
    1. List Searched Articles: Titles<br>
    2. List Searched Articles: Descriptions<br>
    3. List Searched Articles: Sources<br>
6. Market Aux API<br>
    1. List Searched Articles: Titles<br>
    2. List Searched Articles: Descriptions<br>
    3. List Searched Articles: Sources<br>
    4. List Searched Articles: Snippets<br>

## KPIs

We should do this by combining data from all above sources and classifying per company that is the subject or object of the texts. 
Another thing that can be done, fine tune some pretrained Sentiment classifier on all our data.

With alot of data we can these scores for each platform:
1. Youtube<br>
    1. Positive or negative sentiment<br>
        1. Titles<br>
        2. Descriptions<br>
        3. Comments<br>
        4. Categories<br>
2. Reddit<br>
    1. Searched<br>
        1. Positive or negative sentiment<br>
            1. Titles<br>
            2. Descriptions<br>
            3. Comments<br>
    2. Subreddit<br>
        1. Positive or negative sentiment<br>
            1. Titles<br>
            2. Descriptions<br>
            3. Comments<br>
3. Google Search<br>
    1. Positive or negative sentiment<br>
        1. Link Titles<br>
4. News Data IO<br>
    1. Positive or negative sentiment<br>
        1. Titles<br>
        2. Descriptions<br>
        3. Sources<br>
5. News API Org<br>
    1. Positive or negative sentiment<br>
        1. Titles<br>
        2. Descriptions<br>
        3. Sources<br>
6. Market Aux API<br>
    1. Positive or negative sentiment<br>
        1. Titles<br>
        2. Descriptions<br>
        3. Sources<br>
        4. Snippets<br>

With alot of data we can these scores for each company:
1. Company XYZ<br>
    1. Positive or negative sentiment<br>
        1. Youtube<br>
            1. Titles<br>
            2. Descriptions<br>
            3. Comments<br>
            4. Categories<br>
        2. Reddit<br>
            1. Searched<br>
                1. Titles<br>
                2. Descriptions<br>
                3. Comments<br>
            2. Subreddit<br>
                1. Titles<br>
                2. Descriptions<br>
                3. Comments<br>
        3. Google Search<br>
            1. Link Titles<br>
        4. News Data IO<br>
            1. Titles<br>
            2. Descriptions<br>
            3. Sources<br>
        5. News API Org<br>
            1. Titles<br>
            2. Descriptions<br>
            3. Sources<br>
        6. Market Aux API<br>
            1. Titles<br>
            2. Descriptions<br>
            3. Sources<br>
            4. Snippets<br>



# Proposal Version 3: Advanced Sentiment Analysis, Different Search Queries

Sentiment is very difficult to do properly. There are many ways to compare texts regarding two different companies.
For example:
1. Company 1 latest texts vs Company 2 latest texts
2. Company 1 popular texts vs Company 2 popular texts
3. Company 1 postive texts vs Company 2 positive texts
4. Company 1 negative texts vs Company 2 negative texts
5. Use engagement metrics with sentiment scores for further classification

The goal of this version 3, is to repeat the Version 1 and Version 2. However, now use keys in a different way. Use search keys that will guarantee us negative or positive results and compare them.



# Proposal Version 4: Expand our search queries from simple company names to something more

There are three main characteristics that determine rise or fall in economy and hence our company's future.
1. The related industries
2. The expertise
3. The opportunities

For other industries and stocks, these things are taught in business schools. Even so, we will not rely on the financial instructions, for they simply do not apply in the world of computing. 
E.g there is no need for us to analyse how many smartphone companies have embedded some new AI algorithm into their new phones. 
This knowledge is simply useless. In light of our above three characteristics we shall use the following metrics:

1. The related industries<br>
    1. Companies using the same AI models<br>
    2. Academic Funding (Increased chance to find something interesting)<br>
    3. Company RnD Funding (Increased chance to find something interesting)<br>
2. The expertise<br>
    1. Research papers published (Per new ai model discovered)<br>
    2. Phds working in said companies<br>
    3. Acadmic achievements of these Phds<br>
3. The opportunities<br>
    1. Research papers that have different keywords than most but suddenly too many reviews<br>
    2. AI models that have been launched and have high benchmarks<br>



# Proposal 5: New Company (Entitiy) Discovery

We repeat version 4, this time, without mentioning company names. And applying entity recognition models we find new companies. Then repeat versions 1-4 for the new companies.



# Proposal 6: Training Efficiency

We need to restart the whole process (versions 1-5). This time, when searching for posts, with our trained transformers, find similarity or relevancy scores of fetched data with our keywords. And discard news/data that does not match our company or industry or agenda.



# Notes

I dont think I will go beyond Proposal 1 in this project. Proposal 4 is so large, each point in itself is a fullscale project.