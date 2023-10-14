from django.urls import path

from . import api_endpoints as views

app_name = 'gallery'

urlpatterns = [
    path('main_page_picture/list/', views.MainPagePictureListAPIView.as_view(), name='main_page_picture_list'),
]
