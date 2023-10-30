from django.contrib import admin

from .models import Region, Country, City


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id']
    list_editable = ['title']
    search_fields = ['title']


class CityInCountry(admin.TabularInline):
    model = City


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    inlines = [CityInCountry]
