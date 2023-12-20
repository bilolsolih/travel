from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

from .models import Region, Country, City


@admin.register(Region)
class RegionAdmin(TranslationAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id']
    list_editable = ['title']
    search_fields = ['title']


class CityInCountry(TranslationTabularInline):
    model = City


@admin.register(Country)
class CountryAdmin(TranslationAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    inlines = [CityInCountry]
