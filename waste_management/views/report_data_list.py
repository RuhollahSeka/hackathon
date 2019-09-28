from rest_framework.generics import ListAPIView

from waste_management.models import ReportData
from waste_management.serializers import ReportDataListSerializer
from waste_management.utils import gps_distance


class ReportDataListView(ListAPIView):
    serializer_class = ReportDataListSerializer

    def get_queryset(self):  # TODO get username and exclude reports from the user himself
        params = self.request.query_params
        longitude = params.get('longitude')
        latitude = params.get('latitude')
        user_coords = (latitude, longitude)
        filter_ids = [report.id for report in ReportData.objects.all() if gps_distance(user_coords, report.coords) < 5]

        return ReportData.objects.filter(id__in=filter_ids)
