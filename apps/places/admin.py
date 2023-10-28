from django.contrib import admin

from .models import PopularPlace, Picture


class PictureInPopularPlaceInLine(admin.TabularInline):
    model = Picture


@admin.register(PopularPlace)
class PopularPlaceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    inlines = [PictureInPopularPlaceInLine]

# Register your models here.
