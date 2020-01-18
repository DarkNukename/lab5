from django.db import models
from uuid import uuid4
# Create your models here.
from django.contrib.auth.models import User
class NukeList(models.Model):

    uuid = models.UUIDField(primary_key = True, default = uuid4)
    nps_name = models.CharField(max_length = 30)
    country = models.CharField(max_length = 30)
    factor = models.IntegerField()

    def __str__(self):
        return self.title
