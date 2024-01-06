from django.db import models
from . import Registrant, Trips, Stops

class Stop_Times(models.Model):
    #
    # GTFS-JP Stop_Times Fields
    #
    trip_id = models.CharField(max_length=255)
    arrival_time = models.CharField(max_length=255)
    departure_time = models.CharField(max_length=255)
    stop_id = models.CharField(max_length=255)
    stop_sequence = models.IntegerField()
    stop_headsign = models.CharField(max_length=255, null=True)
    pickup_type = models.IntegerField(null=True)
    drop_off_type = models.IntegerField(null=True)
    timepoint = models.IntegerField(null=True)

    #
    # Django Stop_Times Fields
    #
    registrant = models.ForeignKey(Registrant, on_delete=models.CASCADE)
    trip_obj = models.ForeignKey(Trips, on_delete=models.CASCADE)
    stop_obj = models.ForeignKey(Stops, on_delete=models.CASCADE)