from rest_framework.generics import ListAPIView

from waste_management.models import CleanerData
from waste_management.serializers.confirmation_data_list import CleanerDataSerializer
from waste_management.utils import gps_distance


class CleanerDataListView(ListAPIView):
    serializer_class = CleanerDataSerializer

    def get_queryset(self):
        params = self.request.query_params
        longitude = params.get('longitude')
        latitude = params.get('latitude')
        user_coords = (latitude, longitude)
        filter_ids = [cleaner.id for cleaner in CleanerData.objects.all()
                      if gps_distance(user_coords, cleaner.report_data.coords) < 5]

        return CleanerData.objects.filter(id__in=filter_ids)
