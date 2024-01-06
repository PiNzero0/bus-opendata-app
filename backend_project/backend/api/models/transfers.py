from django.db import models
from . import Registrant, Stops

class Transfers(models.Model):
    #
    # GTFS-JP Transfers Fields
    #
    from_stop_id = models.CharField(max_length=255)
    to_stop_id = models.CharField(max_length=255)
    transfer_type = models.IntegerField()
    min_transfer_time = models.IntegerField(null=True)

    #
    # Django Transfers Fields
    #
    registrant = models.ForeignKey(Registrant, on_delete=models.CASCADE)
    from_stop_obj = models.ForeignKey(Stops, on_delete=models.CASCADE, related_name='from_stop')
    to_stop_obj = models.ForeignKey(Stops, on_delete=models.CASCADE, related_name='to_stop')
