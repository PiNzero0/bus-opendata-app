from django.db import models
from . import Registrant

class Feed_Info(models.Model):
    #
    # GTFS-JP Feed Info Fields
    #
    feed_publisher_name = models.CharField(max_length=255)
    feed_publisher_url = models.CharField(max_length=255)
    feed_lang = models.CharField(max_length=255)
    feed_start_date = models.CharField(max_length=255, null=True)
    feed_end_date = models.CharField(max_length=255, null=True)
    feed_version = models.CharField(max_length=255, null=True)
 
    #
    # Django Feed Info Fields
    #
    registrant = models.ForeignKey(Registrant, on_delete=models.CASCADE)