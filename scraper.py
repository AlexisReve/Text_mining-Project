import os
import pandas as pd
import tweepy
import config



client = tweepy.Client(bearer_token= config.BEARER_TOKEN)

query = '#AsterixEtObelixLEmpireDuMilieu lang:fr -is:retweet'

tweets = tweepy.Paginator(client.search_recent_tweets, query=query, tweet_fields=[
                          'context_annotations', 'created_at'], max_results=100).flatten(limit=10000)


df = pd.DataFrame(tweets)
# Print first five the tweet ids and tweets
print(df.shape)

#Save the data to csv:
df.to_csv("Tweet_Asterix.csv", sep = ";")