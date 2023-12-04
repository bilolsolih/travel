from django.urls import path

from . import api_endpoints as views

app_name = 'firebase'

urlpatterns = [
    path('fcm_token/create/', views.FCMTokenCreateAPIView.as_view(), name='fcm_token_create'),
]
