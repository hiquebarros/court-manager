from django.urls import path

from . import views

urlpatterns = [
    path('courts/', views.CourtView.as_view(), name="court-view"),
    path('sport_facilities/court/<court_id>/schedule/<date>/', views.CourtAvailableSchedulesView.as_view(), name="list_schedule-view"),
    path('courts/<court_id>/non_operating_day/register/', views.RegisterNonOperantingDay.as_view(), name="register_non_operating_day"),
    path('courts/non_operating_day/<non_operanting_day_id>/', views.DeleteNonOperantingDay.as_view()),
    path('courts/<court_id>/holidays/register/', views.RegisterHolidayView.as_view()),
    path('courts/holidays/<holiday_id>/', views.DeleteHolidayView.as_view()),

]
