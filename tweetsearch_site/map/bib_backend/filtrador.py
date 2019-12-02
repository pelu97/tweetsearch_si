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

estados = pd.read_csv(settings.BASE_DIR + '/map/dados/estados.csv')
municipios = pd.read_csv(settings.BASE_DIR + '/map/dados/municipios.csv')

estados['nome'] = estados['nome'].apply(unidecode.unidecode).str.lower()
municipios['nome'] = municipios['nome'].apply(unidecode.unidecode).str.lower()

class filtrador():

    def filtra_por_estado(df, ufEstado):

        localizacoes = None

        for user in df.user:

            if user.get('location', {}) is None:
                aux = pd.DataFrame(data = [
                                            ''
                                        ],
                                       columns = ['localizacao'])
                localizacoes = pd.DataFrame.append(localizacoes, aux)
                continue

            aux = pd.DataFrame(data = [
                                            user.get('location', {}).split(',')[0]
                                        ],
                                       columns = ['localizacao'])
            localizacoes = pd.DataFrame.append(localizacoes, aux, ignore_index = True)

        localizacoes['localizacao'] = localizacoes['localizacao'].apply(unidecode.unidecode).str.lower()

        estado = estados[estados.uf == ufEstado]
        resultado = None

        for i, row in localizacoes.iterrows():

            if localizacoes.at[i, 'localizacao'] == '':
                continue

            positivo = 0
            positivo = (estado['nome'] == localizacoes.at[i, 'localizacao'])
            positivo = positivo +  municipios[municipios.codigo_uf.values == estado.codigo_uf.values].nome.str.contains(localizacoes.at[i,'localizacao']).sum()


            if positivo.values[0] != 0:
                aux= pd.DataFrame(data = [
                                            df.loc[i]
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
