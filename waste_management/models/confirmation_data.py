from django.contrib.auth.models import User
from django.db import models

from waste_management.models.cleaner_data import CleanerData


class ConfirmationData(models.Model):
    cleaner_data = models.OneToOneField(
        CleanerData,
        on_delete=models.DO_NOTHING
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    state = models.CharField(
        max_length=128
    )
