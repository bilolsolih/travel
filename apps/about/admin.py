from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import PhoneNumber, Location, SocialMedia, FrequentlyAskedQuestion, TermsAndConditions


@admin.register(FrequentlyAskedQuestion)
class FrequentlyAskedQuestionAdmin(TranslationAdmin):
    list_display = ['id', 'question', 'answer']
    # list_display_links = ['id', 'question', 'answer']
    list_editable = ['question', 'answer']
    search_fields = ['question', 'answer']


@admin.register(TermsAndConditions)
class TermsAndConditionsAdmin(TranslationAdmin):
    list_display = ['id', 'terms']
    list_display_links = ['id', 'terms']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'region', 'city', 'latitude', 'longitude']
    list_display_links = ['id', 'title']
    list_editable = ['region', 'city', 'latitude', 'longitude']
    search_fields = ['title', 'city']


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone_number']
    list_display_links = ['id']
    list_editable = ['phone_number']
    search_fields = ['phone_number']


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'link', 'icon']
    list_display_links = ['id']
    list_editable = ['link', 'icon']
