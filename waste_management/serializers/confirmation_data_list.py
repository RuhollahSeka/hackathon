from rest_framework import serializers

from waste_management.models import CleanerData


class CleanerDataSerializer(serializers.ModelSerializer):
    longitude = serializers.SerializerMethodField()
    latitude = serializers.SerializerMethodField()

    @staticmethod
    def get_longitude(instance: CleanerData):
        return instance.report_data.longitude

    @staticmethod
    def get_latitude(instance: CleanerData):
        return instance.report_data.latitude

    class Meta:
        model = CleanerData
        fields = ('id', 'longitude', 'latitude')
