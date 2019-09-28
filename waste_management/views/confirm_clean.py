from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from waste_management.models import CleanerData, ConfirmationData


class ConfirmCleanView(APIView):
    http_method_names = ('post',)

    def post(self, request: Request):
        data = request.data
        cleaner_id = data.get('cleaner_id')
        is_cleaned = data.get('is_cleaned')
        username = data.get('username')
        confirmer = User.objects.get(username=username)
        cleaner = CleanerData.objects.get(cleaner_id)
        cleaner_user = cleaner.user
        user_profile = cleaner_user.userprofile
        if is_cleaned:
            user_profile.score += cleaner.report_data.score
        else:
            user_profile.score -= cleaner.report_data.score
        user_profile.save()
        cleaner_user.save()
        ConfirmationData.objects.create(
            cleaner_data_id=cleaner_id,
            user=confirmer
        )
        return Response({'success': True}, status=status.HTTP_200_OK)
