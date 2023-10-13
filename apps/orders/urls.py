from django.urls import path

from . import api_endpoints as views

app_name = 'orders'

urlpatterns = [
    path('order/create/', views.OrderCreateAPIView.as_view(), name='order_create'),
    path('order/list/', views.OrderListAPIView.as_view(), name='order_list'),
]
