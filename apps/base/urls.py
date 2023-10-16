from django.urls import path

from . import api_endpoints as views

app_name = 'base'

urlpatterns = [
    path('region/list/', views.RegionListAPIView.as_view(), name='region_list'),
]
