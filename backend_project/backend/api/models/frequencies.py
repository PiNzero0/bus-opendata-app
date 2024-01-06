from django.db import models
from . import Registrant, Trips

class Frequencies(models.Model):
    #
    # GTFS-JP Frequencies Fields
    #
    trip_id = models.CharField(max_length=255)
    start_time = models.CharField(max_length=255)
    end_time = models.CharField(max_length=255)
    headway_secs = models.IntegerField()
    exact_times = models.IntegerField(null=True)

    #
    # Django Frequencies Fields
    #
    registrant = models.ForeignKey(Registrant, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trips, on_delete=models.CASCADE)

    