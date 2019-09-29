from django.urls import path

from waste_management.views import ReportDataCreateView, ReportPictureView, ReportDataListView, ReportSelectingView, \
    CleanerPictureView, UserCreateView, CleanFinishView, CleanerDataListView, ConfirmCleanView, CleanerSelectingView, \
    ConfirmationPictureView

urlpatterns = [
    path('reports/', ReportDataCreateView.as_view()),
    path('reports/<int:pk>/pictures/', ReportPictureView.as_view()),
    path('reports/list/', ReportDataListView.as_view()),
    path('reports/select/', ReportSelectingView.as_view()),
    path('cleaners/<int:pk>/picture/', CleanerPictureView.as_view()),
    path('users/', UserCreateView.as_view()),
    path('cleaners/finish/', CleanFinishView.as_view()),
    path('cleaners/', CleanerDataListView.as_view()),
    path('confirmations/', ConfirmCleanView.as_view()),
    path('cleaners/select/', CleanerSelectingView.as_view()),
    path('confirmations/picture/', ConfirmationPictureView.as_view())
]
