from django.db import models
from . import Registrant

class Fare_Attributes(models.Model):
    #
    # GTFS-JP Fare_Attributes Fields
    #
    fare_id = models.CharField(max_length=255)
    price = models.IntegerField()
    currency_type = models.CharField(max_length=255)
    payment_method = models.IntegerField()
    transfers = models.IntegerField()
    transfer_duration = models.CharField(max_length=255, null=True,blank=True)

    #
    # Django Fare_Attributes Fields
    #
    registrant = models.ForeignKey(Registrant, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['fare_id', 'currency_type', 'registrant'], name='unique_fare_attributes')
        ]