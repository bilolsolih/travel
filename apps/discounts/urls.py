from django.urls import path

from . import api_endpoints as views

app_name = 'discounts'

urlpatterns = [
    path('discount/list/', views.DiscountListAPIView.as_view(), name='discount_list')
]
