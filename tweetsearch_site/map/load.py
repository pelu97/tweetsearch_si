from .models import TweetSpot
from django.conf import settings
import pandas


df = 0

def init():
    global df
    df = pandas.read_json(settings.BASE_DIR + "/map/search/python.json", orient = 'records', lines = True)

def delete():
    TweetSpot.objects.all().delete()


def update(new_query):
    global df
    # new_query + ".txt"
    # file = open(settings.BASE_DIR + "/map/search/" + new_query + ".txt", 'r')


    # for line in file:
    #     splitline = line.split(';')
    #     #substitute arguments with file data
    #     tweet = TweetSpot(title=splitline[0], description=splitline[1], geom={ "type": "Point", "coordinates": [float(splitline[2]), float(splitline[3])]})
    #     tweet.save()
    # file.close()

    for index, row in df[df["created_at"].dt.date.astype(str) == new_query].iterrows():
        # print(row)
        tweet = TweetSpot(title = row["created_at"],  coe_sent = 0, qt_tweets = 0, geom = {"type": "Point", "coordinates": [-47.880322,-15.8079598]})
        tweet.save()
