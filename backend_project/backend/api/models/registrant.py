from django.db import models

#
# Open Data Registarant Model
#
# This model is used to store registrant's name
# which is used to identify the source of the data.
class Registrant(models.Model):
  name = models.CharField(unique=True, max_length=255)