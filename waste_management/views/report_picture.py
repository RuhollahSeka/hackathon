from rest_framework.generics import UpdateAPIView

from waste_management.models import ReportData
from waste_management.serializers.report_data import ReportDataSerializer


class ReportPictureView(UpdateAPIView):
    serializer_class = ReportDataSerializer
    queryset = ReportData.objects.all()
