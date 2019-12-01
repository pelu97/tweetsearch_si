# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 19:51:17 2019

@author: gabri
"""

import pandas as pd
from nltk.tokenize import word_tokenize
import json
from textblob import TextBlob as tb


class importador():
    
    def importaBanco(self):
        return pd.read_json("python.json", orient = 'records', lines = True) #Otima opcao de leitura

