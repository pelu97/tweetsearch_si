# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 19:56:03 2019

@author: gabri
"""

from textblob import TextBlob as tb
import pandas as pd
from nltk.tokenize import word_tokenize

class analisadorSentimentos():
    
    
    def analisaSentimentosTwts(self, df):
        
        count = 0
        soma = 0
        
        for twt in df.text:
    
            twt = tb(twt)
            
            twt = twt.translate(to="en")
            
            soma = soma + twt.sentiment.polarity
            
            count = count + 1
    
        return(soma/count)

        