from django.db import models
from . import Registrant

class Calendar(models.Model):
    #
    # GTFS-JP Calendar Fields
    #
    service_id = models.CharField(max_length=255)
    monday = models.IntegerField()
    tuesday = models.IntegerField()
    wednesday = models.IntegerField()
    thursday = models.IntegerField()
    friday = models.IntegerField()
    saturday = models.IntegerField()
    sunday = models.IntegerField()
    start_date = models.CharField(max_length=255)
    end_date = models.CharField(max_length=255)

    #
    # Django Calendar Fields
    #
    registrant = models.ForeignKey(Registrant, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['service_id', 'registrant'], name='unique_calendar'),
        ]