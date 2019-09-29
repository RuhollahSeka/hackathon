from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from waste_management.models import ConfirmationData


class ConfirmationPictureView(APIView):
    http_method_names = ('post',)

    def post(self, request: Request):
        data = request.data
        confirmation_id = data.get('confirmation_id')
        username = data.get('username')

        confirmation_data = ConfirmationData.objects.get(id=confirmation_id)
        img = open(confirmation_data.cleaner_data.report_data.reported_picture.path, 'rb')

        return Response(img.read(), content_type='image/png')
