from rest_framework import serializers

from waste_management.models import ReportData


class CleanerDataPictureSerializer(serializers.ModelSerializer):
    picture_before_cleaning = serializers.ImageField()

    class Meta:
        model = ReportData
        fields = ('picture_before_cleaning',)
