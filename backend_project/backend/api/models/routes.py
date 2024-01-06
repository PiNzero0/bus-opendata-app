from django.db import models
from . import Agency, Registrant

class Routes(models.Model):
    #
    # GTFS-JP Routes Fields
    #
    route_id = models.CharField(max_length=255)
    agency_id = models.CharField(max_length=255)
    route_short_name = models.CharField(max_length=255, null=True)
    route_long_name = models.CharField(max_length=255, null=True)
    route_desc = models.CharField(max_length=255, null=True)
    route_type = models.IntegerField(null=True)
    route_url = models.CharField(max_length=255,null=True)
    route_color = models.CharField(max_length=255, null=True)
    route_text_color = models.CharField(max_length=255, null=True)

    #
    # Django Routes Fields
    #
    registrant = models.ForeignKey(Registrant, on_delete=models.CASCADE)
    agency_obj = models.ForeignKey(Agency, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['route_id', 'agency_obj'], name='unique_routes')
        ]