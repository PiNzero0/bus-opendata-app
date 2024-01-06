from django.db import models
from . import Registrant

class Office_jp(models.Model):
    #
    # GTFS-JP Office-JP Fields
    #
    office_id = models.CharField(max_length=255)
    office_name = models.CharField(max_length=255)
    office_url = models.CharField(max_length=255, null=True)
    office_phone = models.CharField(max_length=255, null=True)

    #
    # Django Office-JP Fields
    #
    registrant = models.ForeignKey(Registrant, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['office_id', 'registrant'], name='unique_office_jp')
        ]