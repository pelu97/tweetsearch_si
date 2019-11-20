# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 09:27:16 2019

@author: gabri
"""

import tweepy as tweepy
from tweepy import OAuthHandler
import pandas as pd

from tweepy import Stream
from tweepy.streaming import StreamListener
                              
auth = tweepy.OAuthHandler(
        
        'hekIG6uXiTvaMQZSNTmBWigMp' , 
        'Si2UhKyt6ZfDaaK4JZ8M1vptT409KvkgLT80RVyrez4qAdyUyc' 
        
        )

auth.set_access_token(
        
        '1142224560974180353-T86fpnAPEuSsJU9jQUkmUJQkaWZZKs', 
        'crQ8l36d7Sxpux8TM7X5ZEfF1lRnJS0mt4zkbfULdXUAt'
        
        )

api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True, 
                 compression=True, 
                 retry_count=9080, 
                 retry_delay= 15)

class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#dengue', 'dengue'])
                             
                             
stream = tweepy.Stream(api, escutadorDeTuites())
stream.filter(track= tags, languages=['pt'])





























