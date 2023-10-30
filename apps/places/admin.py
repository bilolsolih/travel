from django.contrib import admin

from .models import PopularPlace, Feature


class FeatureInPopularPlace(admin.TabularInline):
    model = Feature


@admin.register(PopularPlace)
class PopularPlaceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'picture']
    list_editable = ['picture']
    search_fields = ['title']
    inlines = [FeatureInPopularPlace]

# Register your models here.
