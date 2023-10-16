from django.contrib import admin

from .models import Region


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id']
    list_editable = ['title']
    search_fields = ['title']
# Register your models here.
