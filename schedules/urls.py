from django.urls import path

from .views import ScheduleCreateView, CancelScheduleView


urlpatterns = [
    path('sport_facilities/courts/<court_id>/schedules/', ScheduleCreateView.as_view() , name="create_schedule-view"),
    path('sport_facilities/courts/schedules/<schedule_id>/', CancelScheduleView.as_view() , name="cancel_schedule-view"),

]

