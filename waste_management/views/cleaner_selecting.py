from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from waste_management.models import ConfirmationData


class CleanerSelectingView(APIView):
    http_method_names = ('post',)

    def post(self, request: Request):
        data = request.data
        cleaner_id = data.get('cleaner_id')
        username = data.get('username')
        user = User.objects.get(username=username)

        confirmation_data = ConfirmationData.objects.create(
            cleaner_data_id=cleaner_id,
            user=user,
        )

        return Response({'id': confirmation_data.id}, status=status.HTTP_200_OK)
