from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from waste_management.models import ReportData
from waste_management.serializers.report_data import ReportDataSerializer


class ReportDataCreateView(CreateAPIView):
    serializer_class = ReportDataSerializer

    def create(self, request: Request, *args, **kwargs):
        data = request.data
        user_id = data.get('user_id')
        user = User.objects.get(id=user_id)
        longitude = data.get('longitude')
        latitude = data.get('latitude')

        ReportData.objects.create(
            user=user,
            longitude=longitude,
            latitude=latitude
        )

        return Response(
            'success',
            status=status.HTTP_200_OK
        )
