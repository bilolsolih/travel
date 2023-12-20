from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import PopularPlace


@admin.register(PopularPlace)
class PopularPlaceAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'picture']
    list_editable = ['picture']
    search_fields = ['title']

# Register your models here.
