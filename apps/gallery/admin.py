from django.contrib import admin

from .models import MainPagePictures


@admin.register(MainPagePictures)
class MainPagePictureAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'picture', 'prompt']
    list_display_links = ['id', 'title']
    list_editable = ['picture', 'prompt']
    search_fields = ['title']
