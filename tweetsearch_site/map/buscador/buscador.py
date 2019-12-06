# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 19:46:45 2019

@author: gabri
"""

import tweepy as tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from time import sleep
import sys

# from django.conf import settings

globalkey = None
globalpath = None

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
                 retry_delay= 15,
                 timeout = sys.maxsize
                 )

class MyListener(StreamListener):

    def on_data(self, data):
        try:
            global globalkey
            global globalpath
            with open(globalpath + 'dados/' + globalkey + '.json', 'a') as f:
                f.write(data)
                #O sleep eh uma solucao provisoria para a aplicacao nao cair quando houverem mtos twts
                sleep(0.01) #sugestao: Criar um tratamento para controlar o fluxo de dados
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

class buscaTwts():

    def iniciaBusca(key, time, path):
        global globalkey
        global globalpath
        globalkey = key
        globalpath = path
        twitter_stream = Stream(auth, MyListener())
        twitter_stream.filter(track=['#' + key, key], languages =['pt'])
#
# def main():
#     print("Iniciando busca")
#     with open('key.txt', 'r') as keyfile:
#         key = keyfile.read()
#         if(key[-1] == '\n'):
#             key = key[:-1]
#         print("Buscando pela palavra: %s" % (key))
#         buscaTwts.iniciaBusca(key, 10)
#
# if __name__ == "__main__":
#     main()
