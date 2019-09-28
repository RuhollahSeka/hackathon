from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from waste_management.models.cleaner_data import CleanerData


class ReportSelectingView(APIView):
    http_method_names = ('post',)

    def post(self, request: Request):
        data = request.data
        report_id = data.get('report_id')
        username = data.get('username')
        user = User.objects.get(username=username)

        cleaner_data = CleanerData.objects.create(
            report_data_id=report_id,
            user=user,
        )

        return Response({'id': cleaner_data.id}, status=status.HTTP_200_OK)
