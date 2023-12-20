from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import MainPagePictures


@admin.register(MainPagePictures)
class MainPagePictureAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'picture', 'prompt']
    list_display_links = ['id', 'title']
    list_editable = ['picture', 'prompt']
    search_fields = ['title']
