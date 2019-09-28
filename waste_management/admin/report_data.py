from django.contrib import admin

from waste_management.models import ReportData


@admin.register(ReportData)
class ReportDataAdmin(admin.ModelAdmin):
    pass
