from django.db import models
from . import Agency, Registrant

class Agency_jp(models.Model):
    #
    # GTFS-JP Agency-JP Fields
    #
    agency_id = models.CharField(max_length=255)
    agency_official_name = models.CharField(max_length=255, null=True)
    agency_zip_number = models.CharField(max_length=255, null = True)
    agency_address = models.CharField(max_length=255, null=True)
    agency_president_pos = models.CharField(max_length=255,null=True)
    agency_president_name = models.CharField(max_length=255,null=True)

    #
    # Django Agency-JP Fields
    #
    registrant = models.ForeignKey(Registrant, on_delete=models.CASCADE)
    agency_obj = models.OneToOneField(Agency, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['agency_id', 'registrant'], name='unique_agency_jp')
        ]
