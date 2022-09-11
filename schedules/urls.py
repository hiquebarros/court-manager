from django.urls import path

from .views import ScheduleCreateView, CancelScheduleView


urlpatterns = [
    path('sport_facilities/court/<court_id>/schedule/', ScheduleCreateView.as_view() , name="create_schedule-view"),
    path('sport_facilities/court/schedule/<schedule_id>/', CancelScheduleView.as_view() , name="cancel_schedule-view"),

]

