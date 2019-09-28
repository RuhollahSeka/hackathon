from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from waste_management.models import CleanerData


class CleanFinishView(APIView):
    http_method_names = ('post',)

    def post(self, request: Request):
        data = request.data
        cleaner_id = data.get('cleaner_id')
        cleaner = CleanerData.objects.get(id=cleaner_id)
        cleaner.state = 'finished'
        cleaner.save()
        return Response({'success': True}, status=status.HTTP_200_OK)
