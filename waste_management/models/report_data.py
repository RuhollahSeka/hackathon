from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class ReportData(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    longitude = models.FloatField(
        default=0,
    )

    latitude = models.FloatField(
        default=0,
    )

    reported_picture = models.ImageField(
        upload_to='images/',
    )

    confirmation_datetime = models.DateTimeField(
        default=datetime.now
    )

    score = models.IntegerField(
        default=0
    )

    @property
    def coords(self):
        return self.latitude, self.longitude
