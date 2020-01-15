
list_stopwords=['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a','an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't", 'infj', 'entp', 'intp', 'intj', 'entj', 'enfj', 'infp', 'enfp', 'isfp', 'istp', 'isfj', 'istj', 'estp', 'esfp', 'estj', 'esfj']
from nltk.stem.porter import PorterStemmer
import string
import re
import pickle

import tweepy
import pandas as pd
import numpy as np

def twitter_setup():

    consumer_key = 'z3HxRl6tXKUUNAStEUcIcLOnn'
    consumer_secret = 'l9Eq3Xo83hsPDA5XfokuglYFnm5z1RrUmifmwg3vcSxKOZIaFK'
    api_token = '1084376557123100674-Uc0V1pC8Ux1ZtqFlMVuSow6OeYgTf3'
    api_secret = 'D8fRb29HaR1NOeq3aImX4DUaer8QoSHgHFPkq7LpuCyhh'

    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(api_token,api_secret)

    api = tweepy.API(auth)
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

def prediction_string(pred_string ,model = pickle.load(open("newpickle_all.sav",'rb'))):
    res = ""
    if "http" in pred_string:
        l = re.findall(r"\b(?:https?://)?(?:(?i:[1-9a-z]+\.))[^\s,]+\b", pred_string)
        for link in l:
            message = pred_string.replace(link, "")
        res = res + " " + pred_string.strip()
    else:
        res = res + pred_string.strip()
    res = re.sub('[^a-zA-Z\s]', " ", res)
    res = res.lower()
    res = res.split()
    res = [word for word in res if not word in list_stopwords]
    wl = PorterStemmer()
    res = [wl.stem(word) for word in res]
    res = " ".join(res)
    nopunc = [char for char in res if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    print(nopunc)

    ie=model[1].predict(model[0].transform([nopunc]).toarray())
    ns=model[2].predict(model[0].transform([nopunc]).toarray())
    tf=model[3].predict(model[0].transform([nopunc]).toarray())
    jp=model[4].predict(model[0].transform([nopunc]).toarray())
    print([ie,ns,tf,jp])
    return [ie,ns,tf,jp]

def final_output(a):
    predicted_velue=prediction_string(a)
    string1=""
    if predicted_velue[0][0]==0:
        string1=string1+"I"
    else:
        string1=string1+"E"

    if predicted_velue[1][0]==0:
        string1=string1+"N"
    else:
        string1=string1+"S"

    if predicted_velue[2][0]==0:
        string1=string1+"T"
    else:
        string1=string1+"F"

    if predicted_velue[3][0]==0:
        string1=string1+"J"
    else:
        string1=string1+"P"

    return string1


        
        
        
