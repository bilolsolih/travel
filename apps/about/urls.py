from django.urls import path

from . import api_endpoints as views

app_name = 'about'

urlpatterns = [
    path('location/list/', views.LocationListAPIView.as_view(), name='location_list'),
    path('location/retrieve/<int:pk>/', views.LocationRetrieveAPIView.as_view(), name='location_retrieve'),
    path('social_media/list/', views.SocialMediaListAPIView.as_view(), name='social_media_list'),
    path('phone_number/retrieve/', views.PhoneNumberRetrieveAPIView.as_view(), name='phone_number_retrieve'),
    path('terms_and_conditions/retrieve/', views.TermsAndConditionsRetrieveAPIView.as_view(), name='terms_and_conditions_retrieve'),
    path('frequently_asked_questions/list/', views.FrequentlyAskedQuestionListAPIView.as_view(), name='frequently_asked_questions')
]
