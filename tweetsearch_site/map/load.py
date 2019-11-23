from .models import TweetSpot
from django.conf import settings





def delete():
    TweetSpot.objects.all().delete()


def update(new_query):
    new_query + ".txt"
    file = open(settings.BASE_DIR + "/map/search/" + new_query + ".txt", 'r')

    for line in file:
        splitline = line.split(';')
        #substitute arguments with file data
        tweet = TweetSpot(title=splitline[0], description=splitline[1], geom={ "type": "Point", "coordinates": [float(splitline[2]), float(splitline[3])]})
        tweet.save()
    file.close()
