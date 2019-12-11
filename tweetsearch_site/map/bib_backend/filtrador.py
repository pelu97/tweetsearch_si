# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 19:53:43 2019

@author: gabri
"""



import pandas as pd
import json
import unidecode
from textblob import TextBlob as tb
from django.conf import settings
from map.bib_backend import analisadorSentimentos

#importar aqui os arquivos para leitura do banco.

#importa base da dos acerca dos estados e municipios
estados = pd.read_csv(settings.BASE_DIR + '/map/dados/estados.csv')
municipios = pd.read_csv(settings.BASE_DIR + '/map/dados/municipios.csv')

#retira acentos e letras maiusculas dos nomes dos estados e municipios
estados['nome'] = estados['nome'].apply(unidecode.unidecode).str.lower()
municipios['nome'] = municipios['nome'].apply(unidecode.unidecode).str.lower()

class filtrador():
    
    #-Recebe um df com os twts tal como no formato gerado em json pela tweepy; recebe string com UF do estado
    def filtra_por_estado(df, ufEstado):

        if df is None:
            return None

        localizacoes = None

        #extraindo localizacoes dos usuarios
        for user in df.user:

            if user.get('location', {}) is None:
                #se nao hah localizacao a mesma eh preenchida como vazia
                aux = pd.DataFrame(data = [
                                            ''
                                        ],
                                       columns = ['localizacao'])
                localizacoes = pd.DataFrame.append(localizacoes, aux)
                continue
            
            #pega a localizacao
            aux = pd.DataFrame(data = [
                                            user.get('location', {}).split(',')[0]
                                        ],
                                       columns = ['localizacao'])
            localizacoes = pd.DataFrame.append(localizacoes, aux, ignore_index = True)
        
        if localizacoes is None:
            return None
        
        #retira acentos e letras maiusculas
        localizacoes['localizacao'] = localizacoes['localizacao'].apply(unidecode.unidecode).str.lower()

        estado = estados[estados.uf == ufEstado]
        resultado = None

        # print(localizacoes)
        for i, row in localizacoes.iterrows():
            # print(localizacoes.loc[i])
            if localizacoes.at[i, 'localizacao'] == '':
                continue
            
            # cria variavel booleana
            positivo = 0
            
            #se a localizacao eh algum estado, o vetor positivo serah true
            positivo = (estado['nome'] == localizacoes.at[i, 'localizacao'])
            #se a localizacao eh algum dos municipios pertencentes ao estado, positivo serah true
            positivo = positivo.sum() +  municipios[municipios.codigo_uf.values == estado.codigo_uf.values].nome.str.contains(localizacoes.at[i,'localizacao']).sum()


            if positivo > 0:
                print(estado)
                if df['id'].count() == 1:
                    return pd.DataFrame.append(None, df, ignore_index = True) #gambiarra para refazer indexs
                else:
                    aux= pd.DataFrame(data = [
                                                df.loc[i + df.index[0]] #encontra posicao correta com base no index zero
                                            ],
                                           columns = df.columns)
                    resultado = pd.DataFrame.append(resultado, aux, ignore_index = True)

        return resultado

    def filtra_por_municipio(df):
        return

class transformador():
    
    def geraSentimentosEstados(df):

            resultado = None

            for i, row in estados.iterrows():

                aux = filtrador.filtra_por_estado(df = df, ufEstado = estados.at[i, 'uf'])

                if aux is None:
                    continue

                coef = analisadorSentimentos.analisadorSentimentos.analisaSentimentosTwts(df = aux)

                aux2 = pd.DataFrame(data = [[
                            estados.at[i, 'nome'],
                            estados.at[i, 'uf'],
                            estados.at[i, 'lon'],
                            estados.at[i, 'lat'],
                            len(aux.index),
                            coef
                            ]],
                        columns = ['localizacao', 'uf', 'longitude', 'latitude', 'qtd_twts', 'coeficiente_de_sentimento']

                        )

                resultado = pd.DataFrame.append(resultado, aux2, ignore_index = True)


            return resultado
