from django.urls import path

from waste_management.views import ReportDataCreateView, ReportPictureView

urlpatterns = [
    path('reports/', ReportDataCreateView.as_view()),
    path('reports/<int:pk>/pictures/', ReportPictureView.as_view()),
]
