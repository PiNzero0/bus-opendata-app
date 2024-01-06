from django.db import models
from . import Registrant

class Shapes(models.Model):
    #
    # GTFS-JP Shapes Fields
    #
    shape_id = models.CharField(max_length=255)
    shape_pt_lat = models.FloatField()
    shape_pt_lon = models.FloatField()
    shape_pt_sequence = models.IntegerField()

    #
    # Django Shapes Fields
    #
    registrant = models.ForeignKey(Registrant, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id', 'source'], name='unique_shapes'),
        ]