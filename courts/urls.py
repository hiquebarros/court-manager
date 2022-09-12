from django.urls import path

from . import views

urlpatterns = [
    path('sport_facilities/courts/', views.CourtView.as_view(), name="court-view"),
    path('sport_facilities/courts/<court_id>/', views.CourtDetailView.as_view(), name="court_detail-view"),
    path('sport_facilities/courts/<court_id>/schedules/<date>/', views.CourtAvailableSchedulesView.as_view(), name="list_schedule-view"),
    path('sport_facilities/courts/<court_id>/non_operating_day/', views.RegisterNonOperantingDay.as_view(), name="register_non_operating_day"),
    path('sport_facilities/courts/non_operating_day/<non_operanting_day_id>/', views.DeleteNonOperantingDay.as_view()),
    path('sport_facilities/courts/<court_id>/holidays/', views.RegisterHolidayView.as_view()),
    path('sport_facilities/courts/holidays/<holiday_id>/', views.DeleteHolidayView.as_view()),
]
