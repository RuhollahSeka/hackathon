from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response

from waste_management.models import ReportData
from waste_management.serializers import ReportDatPictureSerializer
from waste_management.utils import analyze_image


class ReportPictureView(UpdateAPIView):
    serializer_class = ReportDatPictureSerializer
    queryset = ReportData.objects.all()

    def put(self, request, *args, **kwargs):
        super().put(request, *args, **kwargs)
        report_object = ReportData.objects.get(id=kwargs['pk'])
        score = analyze_image(report_object.reported_picture.path)
        report_object.score = score
        return Response({'score': score}, status=status.HTTP_200_OK)
