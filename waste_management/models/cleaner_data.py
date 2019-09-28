from django.contrib.auth.models import User
from django.db import models

from waste_management.models import ReportData


class CleanerData(models.Model):
    report_data = models.OneToOneField(
        ReportData,
        on_delete=models.DO_NOTHING
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    state = models.CharField(
        max_length=128
    )
