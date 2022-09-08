from django.urls import path

from court_types import views as court_types_views

urlpatterns = [
    path('courts/court_types/<court_type_id>/', court_types_views.Court_typeViewDetail.as_view(), name="court_types-detail-view"),
    path('courts/court_types/', court_types_views.Court_typeView.as_view(), name="court_types-view"),
]
