import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
from src.load.db import (
    fact_options,
    engagement_youtube_avg_views, engagement_youtube_avg_likes, engagement_youtube_avg_comments, 
    engagement_youtube_avg_comment_likes, engagement_reddit_avg_score, engagement_reddit_avg_upvote_ratio, 
    engagement_reddit_avg_comments, engagement_reddit_avg_comment_score, engagement_googlesearch_search_results, 
    engagement_googlesearch_format_time, sentiment_youtube_comments, sentiment_reddit_posts, sentiment_reddit_comments, 
    sentiment_news_marketaux, sentiment_news_apiorg, sentiment_news_dataio
)

def get_data(company):
    return {
        "kpis": {
            "Youtube Views": engagement_youtube_avg_views(company).iloc[0]["views"],
            "Reddit Score": engagement_reddit_avg_score(company).iloc[0]["score"],
            "Youtube Likes": engagement_youtube_avg_likes(company).iloc[0]["likes"],
            "Reddit Upvote Ratio": engagement_reddit_avg_upvote_ratio(company).iloc[0]["upvote_ratio"],
            "Youtube Comments": engagement_youtube_avg_comments(company).iloc[0]["comments"],
            "Reddit Comments": engagement_reddit_avg_comments(company).iloc[0]["comments"],
            "Youtube Comment Likes": engagement_youtube_avg_comment_likes(company).iloc[0]["likes"],
            "Reddit Comment Score": engagement_reddit_avg_comment_score(company).iloc[0]["score"],
            "Google Search Results": engagement_googlesearch_search_results(company).iloc[0]["search_results"],
            "Google Search Time": engagement_googlesearch_format_time(company).iloc[0]["format_time"]
        },
        "pie_data": [
            {"title": "Youtube", "data": sentiment_youtube_comments(company)},
            {"title": "Reddit Posts", "data": sentiment_reddit_posts(company)},
            {"title": "Reddit Comments", "data": sentiment_reddit_comments(company)},
            {"title": "News Market AUX", "data": sentiment_news_marketaux(company)},
            {"title": "News API Org", "data": sentiment_news_apiorg(company)},
            {"title": "News Data IO", "data": sentiment_news_dataio(company)}
        ]
    }

app = dash.Dash(__name__)

dark_theme = {"background": "#121212", "card": "#1E1E1E", "text": "#E0E0E0", "accent": "#A970FF"}

app.layout = html.Div([
    html.H3("Dashboard - Realtime Engagement and Sentiment Scores", style={
        "width": "100%", 
        "textAlign": "center",
        "margin": "0", 
        "padding": "10px"
    }),

    html.Div([
        # Pie Charts Section
        html.Div([
            html.H4("Sentiment Distribution", style={"textAlign": "center", "color": dark_theme["text"]}),
            html.Div([
                dcc.Graph(id=f"pie-chart-{i+1}", 
                        style={"width": "30%", "padding": "5px"})
                for i in range(6)
            ], style={"display": "flex", "flexWrap": "wrap", "gap": "10px", "justifyContent": "center"})
        ], style={"width": "65%", "padding": "20px", "background": dark_theme["background"], "borderRadius": "10px"}),

        # KPI Section
        html.Div([
            html.H4("Engagement Scores", style={"textAlign": "center", "color": dark_theme["text"]}),
            dcc.Dropdown(
                id="company-dropdown",
                options=[{"label": c, "value": c} for c in fact_options()],
                value=fact_options().iloc[0],
                clearable=False,
                style={"marginBottom": "10px", "backgroundColor": dark_theme["card"], "color": dark_theme["text"]}
            ),
            html.Div(id="kpi-grid", style={
                "display": "flex",
                "flexWrap": "wrap",
                "justifyContent": "center",
                "gap": "10px",
                "padding": "10px",
                "background": dark_theme["background"],
                "borderRadius": "10px"
            })
        ], style={"width": "30%", "padding": "20px", "verticalAlign": "top"})
    ], style={"display": "flex", "justifyContent": "space-between", "padding": "20px"})
], style={"background": dark_theme["background"], "color": dark_theme["text"], "font-family": "Verdana, sans-serif"})



@app.callback(
    [Output("kpi-grid", "children")] + [Output(f"pie-chart-{i+1}", "figure") for i in range(6)],
    [Input("company-dropdown", "value")]
)
def update_dashboard(company):
    data = get_data(company)
    kpi_boxes = [
        html.Div([
            html.Div(key, style={"fontSize": "14px", "fontWeight": "bold", "margin-bottom": "10px"}),
            html.Div(val, style={"fontSize": "18px"})
        ], style={
            "background": dark_theme["card"],
            "padding": "10px",
            "textAlign": "center",
            "borderRadius": "8px",
            "display": "flex",
            "flexDirection": "column",
            "alignItems": "center",
            "justifyContent": "center",
            "width": "120px",
            "height": "120px",
            "color": dark_theme["text"]
        }) for key, val in data["kpis"].items()
    ]
    
    color_map = {"Positive": "#116D6E", "Neutral": "#D49B54", "Negative": "#CD1818"}
    pie_charts = [
        px.pie(entry["data"], names="sentiment", values="count", title=entry["title"],
               color=entry["data"]["sentiment"], color_discrete_map=color_map)
        .update_layout(paper_bgcolor=dark_theme["background"], font_color=dark_theme["text"])
        for entry in data["pie_data"]
    ]
    
    return [kpi_boxes] + pie_charts

if __name__ == "__main__":
    app.run_server(debug=True)
