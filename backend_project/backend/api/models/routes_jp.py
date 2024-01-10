from django.db import models
from . import Registrant, Routes

class Routes_jp(models.Model):
    #
    # GTFS-JP Routes-JP Fields
    #
    route_id = models.CharField(max_length=255)
    route_update_date = models.CharField(max_length=255, null=True)
    origin_stop = models.CharField(max_length=255, null=True)
    via_stop = models.CharField(max_length=255, null=True)
    destination_stop = models.CharField(max_length=255, null=True)

    #
    # Django Routes-JP Fields
    #
    registrant = models.ForeignKey(Registrant, on_delete=models.CASCADE)
    route_obj = models.ForeignKey(Routes, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id', 'registrant'], name='unique_route_jp'),
        ]