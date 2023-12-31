from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline

from apps.base.second_admin import second_admin
from .models import *



class PlanInPackage(TranslationStackedInline):
    model = Plan



class DestinationInPackageInLine(admin.TabularInline):
    model = Destination


class PictureInPackageInLine(admin.TabularInline):
    model = PackagePicture


class DayInPackageInLine(admin.TabularInline):
    model = Day
    fields = ['change_link', 'day_number']
    readonly_fields = ['change_link']
    extra = 3


@admin.register(Package)
class PackageAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'duration', 'is_active']
    list_display_links = ['id', 'title']
    list_editable = ['is_active']
    search_fields = ['title']
    inlines = [PictureInPackageInLine, DestinationInPackageInLine, PlanInPackage, DayInPackageInLine]


second_admin.register(Package, PackageAdmin)


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


class ActivityPictureInActivityInline(admin.TabularInline):
    model = ActivityPicture


@admin.register(Activity)
class ActivityAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'latitude', 'longitude']
    list_display_links = ['id', 'title']
    list_editable = ['latitude', 'longitude']
    search_fields = ['title']
    inlines = [ActivityPictureInActivityInline]


class AccommodationPictureInAccommodation(admin.TabularInline):
    model = AccommodationPicture


@admin.register(Accommodation)
class AccommodationAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'type', 'city']
    list_display_links = ['id', 'title']
    list_filter = ['type']
    search_fields = ['title', 'city']
    inlines = [AccommodationPictureInAccommodation]


@admin.register(AccommodationType)
class AccommodationTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'picture']
    list_display_links = ['id', 'title']
    list_editable = ['picture']


@admin.register(AccommodationFeature)
class AccommodationFeatureAdmin(TranslationAdmin):
    list_display = ['id', 'title', 'icon', 'is_paid', 'is_popular']
    list_display_links = ['id', 'title']
    list_filter = ['is_paid', 'is_popular']
    list_editable = ['icon', 'is_paid', 'is_popular']
    search_fields = ['title']


class StayInDayInLine(admin.TabularInline):
    model = Stay


class FlightInDayInLine(admin.TabularInline):
    model = Flight


class ActivityInDayInLine(admin.TabularInline):
    model = ActivityBridge


@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ['id', 'package', 'day_number']
    list_display_links = ['id']
    inlines = [StayInDayInLine, FlightInDayInLine, ActivityInDayInLine]


second_admin.register(Day, DayAdmin)

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
