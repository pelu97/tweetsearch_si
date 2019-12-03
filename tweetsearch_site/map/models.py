from django.db import models
from djgeojson.fields import PointField

# Create your models here.




class Query(models.Model):
    title = models.CharField(max_length=20)
    est_mun = models.CharField(max_length=1)

    def __str__(self):
        return self.title


class TweetSpot(models.Model):
    title = models.CharField(max_length=256)
    coe_sent = models.FloatField()
    qt_tweets = models.IntegerField()
    geom = PointField()
    # { "type": "Point", "coordinates": [LONGITUDE, LATITUDE] }

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    
