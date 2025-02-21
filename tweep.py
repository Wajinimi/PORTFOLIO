import tweepy
import pandas as pd
from cleaningtweep import cleaning_tweet

# API keys
api_key = "zRKAKyotjvpBviNFWp33u1ugz"
api_key_secret = "r9Hr9uuPoooaEYUTfMOa7Qyk7sv9VCCvaq08D3a5hXs9yMy9hP"
access_token = "3353942567-LtoUbGX7mCnAyvCFTyuk63TXoaEw1VqtvS3Hsot"
access_token_secret = "sYuJXtC9REIGoaUWwxSciJu3IJbDaDfrCtophOb7ZCHAS"

#I had to include bearers token because the request doesnt support access to the endpoint
bearer_token = "AAAAAAAAAAAAAAAAAAAAACRvzQEAAAAABV3ltQOmUmNNEtNFSC%2BXegfrQ50%3DVPmGaFu5VhwzcPVVu7DsC4ncIYtREVNgKZyQU7ZJ4Nwb9xbzON"
# Authenticate to Twitter API v2
client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)

# Search query and ensure only tweets in English are retrieved.
query = "Bayern -is:retweet lang:en"
tweets = tweepy.Paginator(client.search_recent_tweets, query=query, max_results=10).flatten(limit=10)

# Collect tweet texts
tweet_list = pd.DataFrame([[tweet.text] for tweet in tweets], columns = ["Tweet"])

#Clean the tweets using the function from cleaningtweep file
tweet_list["Cleaned_Tweet"] = tweet_list["Tweet"].apply(cleaning_tweet)

print(tweet_list.head())



