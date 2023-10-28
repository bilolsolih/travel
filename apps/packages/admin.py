from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline

from .models import *  # noqa


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ['id', 'package', 'start_date', 'get_end_date', 'get_is_active']
    list_display_links = ['id']
    list_editable = ['package', 'start_date']
    readonly_fields = ['get_end_date', 'get_is_active']


class PlanInPackage(TranslationStackedInline):
    model = Plan


class TripInPackage(admin.TabularInline):
    model = Trip


class DestinationInPackageInLine(admin.TabularInline):
    model = Destination


@admin.register(Package)
class PackageAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'picture', 'get_discount', 'get_duration']
    list_display_links = ['id', 'title']
    list_editable = ['picture']
    search_fields = ['title']
    readonly_fields = ['get_discount', 'get_duration']
    inlines = [DestinationInPackageInLine, PlanInPackage, TripInPackage]


@admin.register(PlanType)
class PlanTypeAdmin(TranslationAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']


@admin.register(PackageFeature)
class PackageFeatureAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'icon']
    list_display_links = ['id', 'title']
    list_editable = ['icon']
    search_fields = ['title']


@admin.register(Activity)
class ActivityAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'latitude', 'longitude']
    list_display_links = ['id', 'title']
    list_editable = ['latitude', 'longitude']
    search_fields = ['title']

# @admin.register()
# class Admin(admin.ModelAdmin):
#     list_display = ['id', ''],
#     list_display_links = ['id', '']
#     list_filter = ['']
#     list_editable = ['']
#     search_fields = ['']
