from django.urls import path

from . import api_endpoints as views

app_name = 'places'

urlpatterns = [
    path('popular_place/list/', views.PopularPlaceListAPIView.as_view(), name='popular_place_list'),
]
