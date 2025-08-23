import praw
import pandas as pd

def fetch_reddit(subreddit, limit=50):
    reddit = praw.Reddit(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
        user_agent="sociaLens_app"
    )
    posts = []
    for submission in reddit.subreddit(subreddit).hot(limit=limit):
        posts.append({"date": submission.created_utc, "text": submission.title + " " + submission.selftext})
    return pd.DataFrame(posts)
