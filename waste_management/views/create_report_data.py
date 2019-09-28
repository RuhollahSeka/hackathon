from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from waste_management.models import ReportData


class ReportDataCreateView(CreateAPIView):

    def create(self, request: Request, *args, **kwargs):
        data = request.data
        user_id = data.get('user_id')
        user = User.objects.get(id=user_id)
        longitude = data.get('longitude')
        latitude = data.get('latitude')

        report = ReportData.objects.create(
            user=user,
            longitude=longitude,
            latitude=latitude
        )

        return Response(
            {
                'id': report.id
            },
            status=status.HTTP_200_OK
        )
