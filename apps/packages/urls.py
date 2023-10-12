from django.urls import path

from . import api_endpoints as views

app_name = 'packages'

urlpatterns = [
    path('package/list/', views.PackageListAPIView.as_view(), name='package_list'),
    path('package/retrieve/<int:pk>/', views.PackageRetrieveAPIView.as_view(), name='package_retrieve')
]
