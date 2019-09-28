from django.contrib.auth.models import User
from rest_framework import serializers

from waste_management.models import ReportData


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id',)


class ReportDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReportData
        fields = ('user_id', 'longitude', 'latitude')
