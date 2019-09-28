from django.urls import path

from waste_management.views import ReportDataCreateView

urlpatterns = [
    path('reports/', ReportDataCreateView.as_view())
]
