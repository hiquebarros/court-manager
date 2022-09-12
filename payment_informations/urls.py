from django.urls import path

from . import views

urlpatterns = [
    path('users/<pk>/payment/', views.PaymentInformationView.as_view()),
    path('users/<user_id>/payment/<pk>', views.PaymentInformationIDView.as_view()),
]
