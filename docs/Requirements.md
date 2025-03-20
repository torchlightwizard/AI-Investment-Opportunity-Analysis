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
    a. Positive<br>
        i. Stock Performance<br>
        ii. Market Analysis<br>
        iii. Funding Round<br>
        iv. Revenue Growth<br>
        v. Valuation<br>
        vi. Acquisition Rumors<br>
        vii. IPO<br>
        viii. Investor Sentiment<br>
        ix. Why People Love<br>
    b. Negative<br>
        i. Layoffs<br>
        ii. Investor Exit<br>
        iii. Scandals<br>
        iv. Revenue Decline<br>
        v. Valuation Drop<br>
        vi. Why People Hate<br>
        vii. Backlash<br>

## KPIs

We can easily scoop up the following kpis and metrics:
1. Youtube<br>
    a. List Searched Videos: Max Views<br>
    b. List Searched Videos: Max Likes<br>
    c. List Searched Videos: Max Comments<br>
    d. List Searched Videos: Max Comment Likes<br>
    e. List Searched Videos: Max Comment Replies<br>

    f. List Searched Videos: Avg Views<br>
    g. List Searched Videos: Avg Likes<br>
    h. List Searched Videos: Avg Comments<br>
    i. List Searched Videos: Avg Comment Likes<br>
    j. List Searched Videos: Avg Comment Replies<br>

    k. List Searched Videos Count<br>
2. Reddit<br>
    a. List Searched Post: Max Score<br>
    b. List Searched Post: Max Upvote Ratio<br>
    c. List Searched Post: Max Comments<br>
    d. List Searched Post: Max Comment Score<br>
    e. List Searched Post: Max Comment Replies<br>

    f. List Searched Post: Avg Score<br>
    g. List Searched Post: Avg Upvote Ratio<br>
    h. List Searched Post: Avg Comments<br>
    i. List Searched Post: Avg Comment Score<br>
    j. List Searched Post: Avg Comment Replies<br>
3. Google Search<br>
    a. Search Result: Count<br>
    b. Format Time<br>
4. News Data IO API<br>
    a. Search Result: Count<br>
    b. Description Length<br>
    c. Source<br>
5. News API Org<br>
    a. Search Result: Count<br>
    b. Description Length<br>
    c. Source<br>
6. Market Aux API<br>
    a. Search Query Result: Count<br>
    b. Search Query Result: Description Length<br>
    c. Search Query Result: Source<br>
    d. Search Query Result Entities and Sentiment: Scores List<br>
    e. Search Query Result Entity With: Max Sentiment Score<br>
    f. Search Query Result: Avg Sentiment Scores<br>

    g. Search Company Result: Count<br>
    h. Search Company Result: Description Length<br>
    i. Search Company Result: Source<br>
    j. Search Company Result: Entities and Sentiment: Scores List<br>
    k. Search Company Result Entity With: Max Sentiment Score<br>
    l. Search Company Result: Avg Sentiment Scores<br>



# Proposal Version 2: Sentiment Analsis, Data Collection and Dashboard

When and if substantial data has been collected.<br>
1. We will use sentiment analysis to find a basic positive or negative score associated with text of each company.<br>
a. day<br>
b. week<br>
c. month (if possible)<br>
2. The "BERT" model/transformer will be used for this. It will be pretrained on another dataset which is yet to be decided.
3. Finally per company, per timeframe sentiment score will be added to our dashboard.

## Data Collection

For proposal version 3, we needed positive and negative texts separate from one another. Though we are limitd by our free plans, we can accomodate maybe something like two per day.

We can collect data from these:
1. Youtube<br>
    a. List Searched Videos: Titles<br>
    b. List Searched Videos: Descriptions<br>
    c. List Searched Videos: Categories<br>
    d. List Searched Videos: Comments<br>
2. Reddit<br>
    a. List Searched Post: Titles<br>
    b. List Searched Post: Descriptions<br>
    c. List Searched Post: Comments<br>

    d. List Subreddit Top Post: Titles<br>
    e. List Subreddit Top Post: Descriptions<br>
    f. List Subreddit Top Post: Comments<br>
3. Google Search<br>
    a. Link Titles<br>
4. News Data IO<br>
    a. List Searched Articles: Titles<br>
    b. List Searched Articles: Descriptions<br>
    c. List Searched Articles: Sources<br>
5. News API Org<br>
    a. List Searched Articles: Titles<br>
    b. List Searched Articles: Descriptions<br>
    c. List Searched Articles: Sources<br>
6. Market Aux API<br>
    a. List Searched Articles: Titles<br>
    b. List Searched Articles: Descriptions<br>
    c. List Searched Articles: Sources<br>
    d. List Searched Articles: Snippets<br>

## KPIs

We should do this by combining data from all above sources and classifying per company that is the subject or object of the texts. 
Another thing that can be done, fine tune some pretrained Sentiment classifier on all our data.

With alot of data we can these scores for each platform:
1. Youtube<br>
    a. Positive or negative sentiment<br>
        i. Titles<br>
        ii. Descriptions<br>
        iii. Comments<br>
        iv. Categories<br>
2. Reddit<br>
    a. Searched<br>
        i. Positive or negative sentiment<br>
            (1) Titles<br>
            (2) Descriptions<br>
            (3) Comments<br>
    b. Subreddit<br>
        i. Positive or negative sentiment<br>
            (1) Titles<br>
            (2) Descriptions<br>
            (3) Comments<br>
3. Google Search<br>
    a. Positive or negative sentiment<br>
        i. Link Titles<br>
4. News Data IO<br>
    a. Positive or negative sentiment<br>
        i. Titles<br>
        ii. Descriptions<br>
        iii. Sources<br>
5. News API Org<br>
    a. Positive or negative sentiment<br>
        i. Titles<br>
        ii. Descriptions<br>
        iii. Sources<br>
6. Market Aux API<br>
    a. Positive or negative sentiment<br>
        i. Titles<br>
        ii. Descriptions<br>
        iii. Sources<br>
        iv. Snippets<br>

With alot of data we can these scores for each company:
1. Company XYZ<br>
    a. Positive or negative sentiment<br>
        i. Youtube<br>
            (1) Titles<br>
            (2) Descriptions<br>
            (3) Comments<br>
            iv. Categories<br>
        ii. Reddit<br>
            (1) Searched<br>
                (a) Titles<br>
                (b) Descriptions<br>
                (c) Comments<br>
            (2) Subreddit<br>
                (a) Titles<br>
                (b) Descriptions<br>
                (c) Comments<br>
        iii. Google Search<br>
            (1) Link Titles<br>
        iv. News Data IO<br>
            (1) Titles<br>
            (2) Descriptions<br>
            (3) Sources<br>
        v. News API Org<br>
            (1) Titles<br>
            (2) Descriptions<br>
            (3) Sources<br>
        vi. Market Aux API<br>
            (1) Titles<br>
            (2) Descriptions<br>
            (3) Sources<br>
            (4) Snippets<br>



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
    a. Companies using the same AI models<br>
    b. Academic Funding (Increased chance to find something interesting)<br>
    c. Company RnD Funding (Increased chance to find something interesting)<br>
2. The expertise<br>
    a. Research papers published (Per new ai model discovered)<br>
    b. Phds working in said companies<br>
    c. Acadmic achievements of these Phds<br>
3. The opportunities<br>
    a. Research papers that have different keywords than most but suddenly too many reviews<br>
    b. AI models that have been launched and have high benchmarks<br>



# Proposal 5: New Company (Entitiy) Discovery

We repeat version 4, this time, without mentioning company names. And applying entity recognition models we find new companies. Then repeat versions 1-4 for the new companies.



# Proposal 6: Training Efficiency

We need to restart the whole process (versions 1-5). This time, when searching for posts, with our trained transformers, find similarity or relevancy scores of fetched data with our keywords. And discard news/data that does not match our company or industry or agenda.



# Notes

I dont think I will go beyond Proposal 1 in this project. Proposal 4 is so large, each point in itself is a fullscale project.