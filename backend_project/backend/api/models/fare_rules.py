from django.db import models
from . import Registrant, Fare_Attributes, Routes, Stops

class Fare_Rules(models.Model):
    #
    # GTFS-JP Fare_Rules Fields
    #
    fare_id = models.CharField(max_length=255)
    route_id = models.CharField(max_length=255, null=True)
    origin_id = models.CharField(max_length=255, null=True)
    destination_id = models.CharField(max_length=255, null=True)

    #
    # Django Fare_Rules Fields
    #
    registrant = models.ForeignKey(Registrant, on_delete=models.CASCADE)
    fare_obj = models.ForeignKey(Fare_Attributes, on_delete=models.CASCADE)
    route_obj = models.ForeignKey(Routes, on_delete=models.CASCADE, null=True, blank=True)
    origin_obj = models.ForeignKey(Stops, on_delete=models.CASCADE, related_name='origin', null=True, blank=True)
    destination_obj = models.ForeignKey(Stops, on_delete=models.CASCADE, related_name='destination', null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['fare_id', 'route_id', 'origin_id', 'destination_id', 'registrant'], name='unique_fare_rules')
        ]