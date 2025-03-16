youtube = {
    "get_video_statistics":{
        "viewCount": "",
        "likeCount": "",
        "commentCount": "",
        "id": ""
    },

    "get_video_details": {
        "publishedAt": "",
        "channelId": "",
        "title": "",
        "description": "",
        "channelTitle": "",
        "categoryId": "",
        "id": ""
    },

    "get_videos": [
        {
            "id": "",
            "title": "",
            "description": "",
            "publishedAt": "",
            "channelId": ""
        },
    ],
    
    "get_comments": [
        {
            "id": "",
            "video_id": "",
            "textOriginal": "",
            "likeCount": 0,
            "publishedAt": "",
            "totalReplyCount": 0
        },
    ],

    "get_categories": [
        {
            "id": "",
            "title": ""
        },
    ]
}

reddit = {
    "get_posts_subreddit": [
        {
            "id": "",
            "subreddit_id": "",
            "title": "",
            "description": "",
            "num_comments": 0,
            "score": 0,
            "upvote_ratio": 0.1,
            "url": ""
        },
    ],

    "get_posts_searched": [
        {
            "id": "",
            "subreddit_id": "",
            "title": "",
            "description": "",
            "num_comments": 0,
            "score": 0,
            "upvote_ratio": 0.1,
            "url": ""
        },
    ],

    "get_comments":[
        {
            "id": "",
            "body": "",
            "score": 0,
            "post_id": ""
        },
    ],

    "get_posts_subreddit_and_comments": {
        "posts": [
            {
                "id": "",
                "subreddit_id": "",
                "title": "",
                "description": "",
                "num_comments": 0,
                "score": 0,
                "upvote_ratio": 0.1,
                "url": ""
            },
        ],
        "comments": [
            {
                "id": "",
                "body": "",
                "score": 0,
                "post_id": ""
            },
        ],
    },

    "get_posts_searched_and_comments": {
        "posts": [
            {
                "id": "",
                "subreddit_id": "",
                "title": "",
                "description": "",
                "num_comments": 0,
                "score": 0,
                "upvote_ratio": 0.1,
                "url": ""
            },
        ],
        "comments": [
            {
                "id": "",
                "body": "",
                "score": 0,
                "post_id": ""
            },
        ],
    },
}

reddit_http = {
    "get_api_limit": {
        "Request_Count": "",
        "Count_Reset": "",
    }
}

news_marketaux = {
    "get_headlines_by_company": {
        "data": [
            {
                "id": "",
                "entity_name": "",
                "match_score": 0.1,
                "sentiment_score": 0.1,
                "source": "",
                "title": "",
                "description": "",
                "snippet": ""
            },
        ],
        "pages": 0.1,
        "page": 0
    },

    "get_headlines_by_search": {
        "data": [
            {
                "id": "",
                "entity_name": "",
                "match_score": 0.1,
                "sentiment_score": 0.1,
                "source": "",
                "title": "",
                "description": "",
                "snippet": ""
                },
        ],
        "pages": 0.1,
        "page": 0
    },

    "get_headlines_by_company_next_page": [
        {
            "data": [
                {
                    "id": "",
                    "entity_name": "",
                    "match_score": 0.1,
                    "sentiment_score": 0.1,
                    "source": "",
                    "title": "",
                    "description": "",
                    "snippet": ""
                },
            ],
            "pages": 0.1,
            "page": 0
        },
    ],
    
    "get_headlines_by_search_next_page": [
        {
            "data": [
                {
                    "id": "",
                    "entity_name": "",
                    "match_score": 0.1,
                    "sentiment_score": 0.175,
                    "source": "",
                    "title": "",
                    "description": "",
                    "snippet": ""
                },
            ],
            "pages": 0.1,
            "page": 0
        },
    ],
}

news_dataio = {
    "get_headlines": {
        "data": [
            {
                "id": "",
                "source": "",
                "title": "",
                "description": "",
            },
        ],
        "pages": 0.1,
        "next_page": ""
    },

    "get_headlines_next_page": [
        {
            "data": [
                {
                    "id": "",
                    "source": "",
                    "title": "",
                    "description": "",
                },
            ],
            "pages": 0.1,
            "next_page": ""
        },
    ]
}

news_apiorg = {
    "get_headlines": {
        "data": [
            {
                "source": "",
                "title": "",
                "description": "",
            },
        ],
        "pages": 0.1,
    },

    "get_headlines_next_page": [
        {
            "data": [
                {
                    "source": "",
                    "title": "",
                    "description": "",
                },
            ],
            "pages": 0.1,
        },
    ]
}

googlesearch = {
    "get_company_results": [
        {
            "title": "",
            "link": "",
            "format_time": "",
            "search_results": "",
        },
    ],
}