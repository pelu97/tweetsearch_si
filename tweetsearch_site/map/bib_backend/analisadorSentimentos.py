# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 19:56:03 2019

@author: gabri
"""

from textblob import TextBlob as tb
import pandas as pd
from nltk.tokenize import word_tokenize
import nltk
import random
from nltk import classify
from nltk import NaiveBayesClassifier
from django.conf import settings
     
   
dfSentimento =  pd.read_excel(settings.BASE_DIR + '/map/dados/dfSentimentos.xlsx')

class analisadorSentimentos():
    
    
    global mlAnalisador

    mlAnalisador = None
    
    def MLTreinamento(dfSentimento):
        
        global mlAnalisador
        
        palavrasInuteis = ['a', 'o', 'um', 'uma', 'os', 'as', 'e', 'com', 'que',
                   'na', 'em', 'da', 'de', 	'este', 'esta', 'estes', 'estas', 'isto',
                   'esse', 'essa', 'esses', 'essas', 'isso', 'aquele', 'aquela', 'aqueles', 'aquelas', 'aquilo',
                   'tu', 'nos', 'vos', 'eles', 'elas', 'ele', 'ela']
        
        dfPositivo = dfSentimento[dfSentimento.Sentimento == 1]
        
        dfNegativo = dfSentimento[dfSentimento.Sentimento == 0]
        
        nltk.download('wordnet')
        nltk.download('averaged_perceptron_tagger')
        
        posTokenizado = word_tokenize(" ".join(dfPositivo['Frase']), language = 'portuguese')
        negTokenizado = word_tokenize(" ".join(dfNegativo['Frase']), language = 'portuguese')
        
        
        posTokenizado = list(filter(lambda token: token not in palavrasInuteis, posTokenizado))
        negTokenizado = list(filter(lambda token: token not in palavrasInuteis, negTokenizado))
        
        
        def get_tweets_for_model(cleaned_tokens_list):
            for tweet_tokens in cleaned_tokens_list:
                yield dict([token, True] for token in tweet_tokens)
        
        posiModel = get_tweets_for_model(posTokenizado)
        negModel = get_tweets_for_model(negTokenizado)
        
        positive_dataset = [(tweet_dict, 1)
                             for tweet_dict in posiModel]
        
        negative_dataset = [(tweet_dict, 0)
                             for tweet_dict in negModel]
        
        dataset = positive_dataset + negative_dataset
        
        random.shuffle(dataset)
        
        train_data = dataset[:329359]
        test_data = dataset[329359:]
        
        mlAnalisador = NaiveBayesClassifier.train(train_data)
        
        print("Accuracy is:", classify.accuracy(mlAnalisador, test_data))
    
    def analisaSentimentosTwts(df):
        
        count = 0
        positivos = 0
        
        for twt in df.text:
    
            custom_tokens = word_tokenize(twt)
    
            resultado = mlAnalisador.classify(dict([token, True] for token in custom_tokens))
            
            positivos = positivos + resultado
            
            count = count + 1
            
        media = positivos/count
        negativos = len(df.text) - positivos
    
        return('media:' + str(media) + "   " + 
               'qtdPositivos:' + str(positivos)  + "   " +
               'qtdNegativos:' + str(negativos))
        
    
analisadorSentimentos.MLTreinamento(dfSentimento = dfSentimento)
        