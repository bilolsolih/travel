from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import api_endpoints as views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.UserRegisterAPIView.as_view(), name='register'),
    path('login/', views.UserLoginAPIView.as_view(), name='login'),
    path('logout/', views.UserLogoutAPIView.as_view(), name='logout'),
    path('retrieve/', views.UserRetrieveAPIView.as_view(), name='retrieve'),
    path('update/', views.UserUpdateAPIView.as_view(), name='update'),
    path('delete/', views.UserDeleteAPIView.as_view(), name='delete'),
    path('check/', views.UserCheckAPIView.as_view(), name='check'),
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #########################################################################
    path('related_person/create/', views.RelatedPersonCreateAPIView.as_view(), name='related_person_create'),
    path('related_person/list/', views.RelatedPersonListAPIView.as_view(), name='related_person_list'),
    path('related_person/retrieve/<int:pk>/', views.RelatedPersonRetrieveAPIView.as_view(), name='related_person_retrieve'),
    path('related_person/delete/<int:pk>/', views.RelatedPersonDeleteAPIView.as_view(), name='related_person_delete'),
    ##################################################################################################################
]
