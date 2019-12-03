# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 19:51:17 2019

@author: gabri
"""

import pandas as pd
import json


#nao serah definido neste projeto
class importador():
    
    def importaBanco():
        return pd.read_json("python.json", orient = 'records', lines = True) #Otima opcao de leitura

