from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response

from waste_management.models import CleanerData
from waste_management.serializers import CleanerDataPictureSerializer
from waste_management.utils import analyze_image


class CleanerPictureView(UpdateAPIView):
    serializer_class = CleanerDataPictureSerializer
    queryset = CleanerData.objects.all()

    def put(self, request, *args, **kwargs):
        super().put(request, *args, **kwargs)
        cleaner_object = CleanerData.objects.get(id=kwargs['pk'])
        score = analyze_image(cleaner_object.picture_before_cleaning.path)
        if score > 0.1 * cleaner_object.report_data.score:
            return Response({'continue': True}, status=status.HTTP_200_OK)
        cleaner_object.delete()
        return Response({'continue': False}, status=status.HTTP_200_OK)
