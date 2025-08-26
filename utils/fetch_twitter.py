# utils/fetch_twitter.py
import tweepy
import pandas as pd
import streamlit as st

def fetch_twitter(keyword, limit=50):
    # Authenticate with Twitter API v2
    client = tweepy.Client(bearer_token=st.secrets["X_BEARER_TOKEN"])

    # Build query: no retweets, only English
    query = f"{keyword} -is:retweet lang:en"

    tweets = client.search_recent_tweets(
        query=query,
        max_results=min(limit, 100),   # Twitter API max per call = 100
        tweet_fields=["created_at", "text"]
    )

    posts = []
    if tweets.data:
        for tweet in tweets.data:
            posts.append({
                "date": tweet.created_at,
                "text": tweet.text
            })

    return pd.DataFrame(posts)
