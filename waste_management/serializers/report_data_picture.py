from rest_framework import serializers

from waste_management.models import ReportData


class ReportDatPictureSerializer(serializers.ModelSerializer):
    reported_picture = serializers.ImageField()

    class Meta:
        model = ReportData
        fields = ('reported_picture',)
