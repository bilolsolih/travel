from django.urls import path

from . import api_endpoints as views

app_name = 'base'

urlpatterns = [
    path('region/list/', views.RegionListAPIView.as_view(), name='region_list'),
    path('country/list/', views.CountryListAPIView.as_view(), name='country_list'),
    path('city/list/', views.CityListAPIView.as_view(), name='city_list'),
]
