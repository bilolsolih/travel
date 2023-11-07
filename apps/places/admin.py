from django.contrib import admin

from .models import PopularPlace


@admin.register(PopularPlace)
class PopularPlaceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'picture']
    list_editable = ['picture']
    search_fields = ['title']

# Register your models here.
