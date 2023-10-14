from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

from .models import *  # noqa


class PlanInPackage(TranslationTabularInline):
    model = Plan


@admin.register(Package)
class PackageAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'picture', 'city']
    list_display_links = ['id', 'title']
    list_editable = ['picture']
    search_fields = ['title']
    inlines = [PlanInPackage]


@admin.register(PlanType)
class PlanTypeAdmin(TranslationAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']


@admin.register(Activity)
class ActivityAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'latitude', 'longitude']
    list_display_links = ['id', 'title']
    list_editable = ['latitude', 'longitude']
    search_fields = ['title']


@admin.register(PlanFeature)
class PlanFeatureAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'icon']
    list_display_links = ['id', 'title']
    list_editable = ['icon']
    search_fields = ['title']

# @admin.register()
# class Admin(admin.ModelAdmin):
#     list_display = ['id', ''],
#     list_display_links = ['id', '']
#     list_filter = ['']
#     list_editable = ['']
#     search_fields = ['']
