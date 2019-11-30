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
twitter_stream.filter(track=['#dengue', 'dengue'], languages =['pt'])
                             
import pandas as pd
from nltk.tokenize import word_tokenize
 

df = pd.read_json("python.json", orient = 'records', lines = True) #Otima opcao de leitura

word_tokenize(" ".join(df['text']), language = 'portuguese')



import json
 
with open('python.json', 'r') as f:
    line = f.readline() # read only the first tweet/line
    tweet = json.loads(line) # load it as Python dict
    print(json.dumps(tweet, indent=4)) # pretty-print



tweet['text']

from textblob import TextBlob as tb

count = 0
soma = 0

for teste in df.text:
    
    teste = tb(teste)
    
    teste.tags
    
    teste = teste.translate(to="en")
    
    soma = soma + teste.sentiment.polarity
    
    count = count + 1
    
print(soma/count)

#pegar a localizacao
 df.user.loc[1].get('location', {})






