from django.urls import path

from . import api_endpoints as views

app_name = 'payments'

urlpatterns = [
    path('payment/list/', views.PaymentRetrieveAPIView.as_view(), name='payment_list'),
    path('payment/retrieve/<int:pk>/', views.PaymentRetrieveAPIView.as_view(), name='payment_retrieve'),
]
