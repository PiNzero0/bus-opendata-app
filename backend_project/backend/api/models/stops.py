from django.db import models
from . import Registrant, Stop_Times

class Stops(models.Model):
    #
    # GTFS-JP Stops Fields
    #
    stop_id = models.CharField(max_length=255)
    stop_code = models.CharField(max_length=255, null=True)
    stop_name = models.CharField(max_length=255, null=True)
    stop_desc = models.CharField(max_length=255, null=True)
    stop_lat = models.FloatField()
    stop_lon = models.FloatField()
    zone_id = models.CharField(max_length=255, null=True)
    stop_url = models.CharField(max_length=255, null=True)
    location_type = models.IntegerField(default=0, null=True)
    parent_station = models.CharField(max_length=255, null=True)
    wheelchair_boarding = models.IntegerField(null=True)
    platform_code = models.CharField(max_length=255, null=True)

    #
    # Django Stops Fields
    #
    registrant = models.ForeignKey(Registrant, on_delete=models.CASCADE)
    stop = models.ForeignKey(Stop_Times, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['stop_id', 'registrant'], name='unique_stops'),
        ]
