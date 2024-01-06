from django.db import models
from . import Registrant

class Agency(models.Model):
    #
    # GTFS-JP Agency Fields
    #
    agency_id = models.CharField(max_length=255)
    agency_name = models.CharField(max_length=255)
    agency_url = models.CharField(max_length=255)
    agency_timezone = models.CharField(max_length=255)
    agency_lang = models.CharField(max_length=255)
    agency_phone = models.CharField(max_length=255,null=True)
    agency_fare_url = models.CharField(max_length=255,null=True)
    agency_email = models.CharField(max_length=255,null=True)

    #
    # Django Agency Fields
    #
    registrant = models.ForeignKey(Registrant, on_delete=models.CASCADE)

    class Meta:
      constraints = [
        models.UniqueConstraint(fields=['agency_id', 'registrant'], name='unique_agency')
      ]