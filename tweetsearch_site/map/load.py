from .models import TweetSpot
from django.conf import settings
import pandas
import map.buscador.buscador
from map.bib_backend import analisadorSentimentos
from map.bib_backend import filtrador

df = 0

def init():
    global df
    print("reading twts.json")
    df = pandas.read_json(settings.BASE_DIR + "/map/dados/twts.json", orient = 'records', lines = True)

def delete():
    TweetSpot.objects.all().delete()


def update(new_query):
    global df
    df = pandas.read_json(settings.BASE_DIR + "/map/dados/twts.json", orient = 'records', lines = True)

    df_proc = filtrador.transformador.geraSentimentosEstados(df)
    print(df_proc)
    #df.loc[df["created_at"].dt.date.astype(str) == new_query]

    for index, row in df_proc.iterrows():
        # print(row)
        tweet = TweetSpot(title = row["localizacao"],  coe_sent = row["coeficiente_de_sentimento"], qt_tweets = ["qtd_twts"], geom = {"type": "Point", "coordinates": [row["longitude"],row["latitude"]]})
        tweet.save()
