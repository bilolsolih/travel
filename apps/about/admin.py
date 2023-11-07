from django.contrib import admin

from .models import PhoneNumber, Location, SocialMedia


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
