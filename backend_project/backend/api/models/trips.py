from django.db import models
from . import Routes, Calendar, Shapes, Office_jp, Registrant

class Trips(models.Model):
    #
    # GTFS-JP Trips Fields
    #
    trip_id = models.CharField(max_length=255)
    route_id = models.CharField(max_length=255)
    service_id = models.CharField(max_length=255)
    trip_headsign = models.CharField(max_length=255, null=True)
    trip_short_name = models.CharField(max_length=255, null=True)
    direction_id = models.IntegerField(null=True)
    block_id = models.CharField(max_length=255, null=True)
    shape_id = models.CharField(max_length=255, null=True)
    wheelchair_accessible = models.IntegerField(null=True)
    bikes_allowed = models.IntegerField(null=True)
    jp_trip_desc = models.CharField(max_length=255, null=True)
    jp_trip_desc_symbol = models.CharField(max_length=255, null=True)
    jp_office_id = models.CharField(max_length=255, null=True)

    #
    # Django Trips Fields
    #
    registrant = models.ForeignKey(Registrant, on_delete=models.CASCADE)
    route_obj = models.ForeignKey(Routes, on_delete=models.CASCADE)
    service_obj = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    jp_office_obj = models.ForeignKey(Office_jp, on_delete=models.CASCADE, blank=True, null=True)
    shapes = models.ManyToManyField('Shapes', blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['trip_id', 'registrant'], name='unique_trips')
        ]
