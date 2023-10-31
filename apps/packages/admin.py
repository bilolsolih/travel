from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline

from .models import *


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


class PictureInPackageInLine(admin.TabularInline):
    model = PackagePicture


class DayInPackageInLine(admin.TabularInline):
    model = Day
    extra = 3


@admin.register(Package)
class PackageAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'picture', 'get_discount', 'get_duration']
    list_display_links = ['id', 'title']
    list_editable = ['picture']
    search_fields = ['title']
    readonly_fields = ['get_discount', 'get_duration']
    inlines = [PictureInPackageInLine, DestinationInPackageInLine, PlanInPackage, TripInPackage, DayInPackageInLine]


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


class AccommodationPictureInAccommodation(admin.TabularInline):
    model = AccommodationPicture


@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'type', 'country', 'city']
    list_display_links = ['id', 'title']
    list_filter = ['type']
    search_fields = ['title', 'country', 'city']
    inlines = [AccommodationPictureInAccommodation]


@admin.register(AccommodationType)
class AccommodationTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'picture']
    list_display_links = ['id', 'title']
    list_editable = ['picture']


@admin.register(AccommodationFeature)
class AccommodationFeatureAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'icon', 'is_paid']
    list_display_links = ['id', 'title']
    list_filter = ['is_paid']
    list_editable = ['icon', 'is_paid']
    search_fields = ['title']


class StayInDayInLine(admin.TabularInline):
    model = Stay


class FlightInDayInLine(admin.TabularInline):
    model = Flight


class ActivityInDayInLine(admin.TabularInline):
    model = ActivityBridge


@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ['id', 'package', 'trip', 'day_number']
    list_display_links = ['id']
    list_filter = ['package']
    list_editable = ['package', 'trip']
    inlines = [StayInDayInLine, FlightInDayInLine, ActivityInDayInLine]

# @admin.register()
# class Admin(admin.ModelAdmin):
#     list_display = ['id', ''],
#     list_display_links = ['id', '']
#     list_filter = ['']
#     list_editable = ['']
#     search_fields = ['']

# @admin.register()
# class Admin(admin.ModelAdmin):
#     list_display = ['id', ''],
#     list_display_links = ['id', '']
#     list_filter = ['']
#     list_editable = ['']
#     search_fields = ['']
