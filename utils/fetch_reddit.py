import praw
import streamlit as st
import pandas as pd

def fetch_reddit(subreddit, limit=50):
    reddit = praw.Reddit(
        client_id=st.secrets["REDDIT_CLIENT_ID"],
        client_secret=st.secrets["REDDIT_CLIENT_SECRET"],
        user_agent=st.secrets["REDDIT_USER_AGENT"],
    )

    posts = []
    for submission in reddit.subreddit(subreddit).hot(limit=limit):
        posts.append({
            "date": submission.created_utc,
            "text": submission.title + " " + submission.selftext
        })
    return pd.DataFrame(posts)
