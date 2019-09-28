from rest_framework import serializers

from waste_management.models import ReportData


class ReportDataListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReportData
        fields = ('score', 'longitude', 'latitude')
