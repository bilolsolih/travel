from django.contrib import admin

from .models import *  # noqa


class PlanInPackage(admin.TabularInline):
    model = Plan


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'picture', 'city']
    list_display_links = ['id', 'title']
    list_editable = ['picture']
    search_fields = ['title']
    inlines = [PlanInPackage]


@admin.register(PlanType)
class PlanTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'latitude', 'longitude']
    list_display_links = ['id', 'title']
    list_editable = ['latitude', 'longitude']
    search_fields = ['title']


@admin.register(PlanFeature)
class PlanFeatureAdmin(admin.ModelAdmin):
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
