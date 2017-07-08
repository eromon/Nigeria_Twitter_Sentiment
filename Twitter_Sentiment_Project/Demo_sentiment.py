# -*- coding: utf-8 -*-
"""
Created on Sat Jul  8 15:15:27 2017

@author: Eromon
"""
#Project To Analyse Sentiment of Current Nigerian Issues on Twitter

#Import dependencies
import numpy as np
import pandas as pd
import tweepy
import matplotlib.pyplot as plt
from textblob import TextBlob

pd.options.display.max_columns = 50
pd.options.display.max_rows= 50
pd.options.display.width= 120

#Authenticate API
consumer_key = "S9kGUNRWSqqcVklAdBECbo4Eg" # Use your own key. To get a key https://apps.twitter.com/
consumer_secret = "eu1Tu6HE13vsjgjvdt6PxjDuqi0YdCmGB9IvrUaAlTS9gCuKaa"
auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
api = tweepy.API(auth)

#Prepare Queries For Sentiment Analysis
Nigerian_Topics = ["Biafra", "Nigeria", "EFCC", "Buhari", "APC", "PDP"]

#Label Tweets with their sentiments
def tweet_label(analysis, threshold = 0):
    if analysis.sentiment.polarity > threshol
    d:
        return "Positive"
    else:
        return "Negative"
    
#Collect Tweets from Twitter API, Save Tweets to CSV, Collate Sentiment
Tweet_Polarities = dict()
for topic in Nigerian_Topics:
    topic_polarities = []
    topic_tweets = api.search(q= topic, count = 100)
    id_list = [tweet.id for tweet in topic_tweets]
    data_set = pd.DataFrame(id_list, columns=["id"])
    data_set["Tweets"] = [tweet.text for tweet in topic_tweets]
    data_set["Sentiment"] = [TextBlob(tweet.text).sentiment.polarity for tweet in topic_tweets]
    data_set["Label"] = [tweet_label(TextBlob(tweet.text)) for tweet in topic_tweets]
    data_set.to_csv("%s_Tweets.csv" %topic)
    Tweet_Polarities[topic] = data_set["Sentiment"].mean()

import operator    
sorted_analysis = sorted(Tweet_Polarities.items(), key=operator.itemgetter(1), reverse=True)
print('Mean Sentiment Polarity in descending order :')
for candidate, polarity in sorted_analysis:
	print('%s : %0.3f' % (candidate, polarity))    
    