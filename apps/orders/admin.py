from django.contrib import admin

from apps.base.second_admin import second_admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'package', 'plan', 'price_total', 'price_paid', 'status']
    list_display_links = ['id', 'user', 'package']
    search_fields = ['user', 'package']
    list_filter = ['status']


second_admin.register(Order, OrderAdmin)
