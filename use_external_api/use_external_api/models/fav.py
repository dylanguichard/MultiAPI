from django.db import models
from django.conf import settings


class Fav(models.Model):

    username = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    el_id = models.CharField(max_length=255)
    el_type = models.CharField(max_length=255)
