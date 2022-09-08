from django.urls import path

from . import views

urlpatterns = [
    path('sport_facilities/<int:facility_id>/address/', views.AddressView.as_view()),
]
