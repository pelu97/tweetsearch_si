from django.db import models
from djgeojson.fields import PointField

# Create your models here.

class TweetSpot(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    geom = PointField()

    def __unicode__(self):
        return self.title
