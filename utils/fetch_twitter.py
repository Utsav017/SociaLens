import snscrape.modules.twitter as sntwitter
import pandas as pd

def fetch_twitter(query, limit=50):
    tweets = []
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        tweets.append({"date": tweet.date, "text": tweet.content})
        if len(tweets) >= limit:
            break
    return pd.DataFrame(tweets)
