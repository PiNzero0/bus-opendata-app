from django.db import models
from . import Registrant, Calendar

class Calendar_Dates(models.Model):
    #
    # GTFS-JP Calendar_Dates Fields
    #
    service_id = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    exception_type = models.IntegerField()

    #
    # Django Calendar_Dates Fields
    #
    registrant = models.ForeignKey(Registrant, on_delete=models.CASCADE)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['service_id', 'date', 'registrant'], name='unique_calendar_dates'),
            models.UniqueConstraint(fields=['service', 'date', 'registrant'], name='unique_calendar_dates_django'),
        ]
