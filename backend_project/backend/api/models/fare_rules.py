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
    fare = models.ForeignKey(Fare_Attributes, on_delete=models.CASCADE)
    route = models.ForeignKey(Routes, on_delete=models.CASCADE)
    origin = models.ForeignKey(Stops, on_delete=models.CASCADE, related_name='origin')
    destination = models.ForeignKey(Stops, on_delete=models.CASCADE, related_name='destination')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['fare_id', 'route_id', 'origin_id', 'destination_id', 'registrant'], name='unique_fare_rules')
        ]