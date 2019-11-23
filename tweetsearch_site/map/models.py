from django.db import models
from djgeojson.fields import PointField

# Create your models here.



class DayMap(models.Model):
    title = models.CharField(max_length=256, default="Map")
    date = models.DateField()

    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title


class Query(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class TweetSpot(models.Model):
    # daymap = models.ForeignKey(DayMap, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    description = models.TextField()
    geom = PointField()
    # { "type": "Point", "coordinates": [LONGITUDE, LATITUDE] }

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
