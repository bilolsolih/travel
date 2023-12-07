from django.urls import path

from . import api_endpoints as views

app_name = 'notifications'

urlpatterns = [
    path('notification/send/', views.NotificationSendAPIView.as_view(), name='notification_send'),
]
