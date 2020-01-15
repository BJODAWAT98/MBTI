# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 21:38:04 2019

@author: Anant Jodawat
"""

import tweepy
import pandas as pd
import numpy as np

consumer_key = 'z3HxRl6tXKUUNAStEUcIcLOnn'
consumer_secret = 'l9Eq3Xo83hsPDA5XfokuglYFnm5z1RrUmifmwg3vcSxKOZIaFK'
api_token = '1084376557123100674-Uc0V1pC8Ux1ZtqFlMVuSow6OeYgTf3'
api_secret = 'D8fRb29HaR1NOeq3aImX4DUaer8QoSHgHFPkq7LpuCyhh'


def twitter_setup():
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(api_token,api_secret)

    api = tweepy.API(auth)
    print("set up success")
    return api
def get_posts(name,count):
    extractor = twitter_setup()
    name = name.lower()
    name = name.replace(" ","")
    tweet_data=""
    try:
        tweets = extractor.user_timeline(screen_name = name,count = count)    
        tweet_data=""
        for tweet in tweets[:count]:
            tweet_data=tweet_data+tweet.text
        return tweet_data
    except:
        return tweet_data