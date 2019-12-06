from .models import TweetSpot
from django.conf import settings
import pandas
import map.buscador.buscador
from map.bib_backend import analisadorSentimentos
from map.bib_backend import filtrador
import os



df = 0

# def init():
#     global df
#     print("reading twts.json")
#     df = pandas.read_json(settings.BASE_DIR + "/map/dados/twts.json", orient = 'records', lines = True)

def setkey(keyword):
    with open(settings.BASE_DIR + "/map/buscador/key.txt", 'w') as keyfile:
        keyfile.write(keyword)
    command = "python3 " + settings.BASE_DIR + "/map/busca.py"
    os.system("gnome-terminal -e 'bash -c \"" + command + "; sleep 1000000\"'")
    # os.system('python3 ' + settings.BASE_DIR + '/map/busca.py')


def delete():
    TweetSpot.objects.all().delete()


def update(new_query_ini, new_query_fim, keyword):
    global df
    df = pandas.read_json(settings.BASE_DIR + "/map/dados/" + keyword + ".json", orient = 'records', lines = True)

    # print(new_query)
    # print(df)
    # print(df[df["created_at"].dt.date.astype(str) == new_query])
    df_loc = df.loc[(df["created_at"].dt.date.astype(str) >= new_query_ini) & (df["created_at"].dt.date.astype(str) <= new_query_fim)]
    # print(df_loc.loc[19])
    # print(df_loc.index[0])
    df_proc = filtrador.transformador.geraSentimentosEstados(df_loc)
    # print(df_proc)
    #df.loc[df["created_at"].dt.date.astype(str) == new_query]

    for index, row in df_proc.iterrows():
        # print(row)
        tweet = TweetSpot(title = row["localizacao"],  coe_sent = row["coeficiente_de_sentimento"], qt_tweets = row["qtd_twts"], geom = {"type": "Point", "coordinates": [row["longitude"],row["latitude"]]})
        tweet.save()
