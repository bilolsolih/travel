from django.contrib import admin
from .models import *


class AccommodationPictureInAccommodation(admin.TabularInline):
    model = AccommodationPicture


@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'type', 'country', 'city']
    list_display_links = ['id', 'title']
    list_filter = ['type']
    search_fields = ['title', 'country', 'city']
    inlines = [AccommodationPictureInAccommodation]


@admin.register(AccommodationType)
class AccommodationTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'picture']
    list_display_links = ['id', 'title']
    list_editable = ['picture']


@admin.register(AccommodationFeature)
class AccommodationFeatureAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'icon', 'is_paid']
    list_display_links = ['id', 'title']
    list_filter = ['is_paid']
    list_editable = ['icon', 'is_paid']
    search_fields = ['title']

