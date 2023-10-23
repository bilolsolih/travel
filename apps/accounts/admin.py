from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, AdminUser


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['id', 'phone_number']
    list_display_links = ['id', 'phone_number']
    list_filter = ['is_active', 'is_verified']
    fieldsets = (
        (None, {'fields': ('phone_number', 'is_verified', 'is_active')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'gender', 'birthdate')}),
        ('Address', {'fields': ('region', 'district')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('phone_number', 'first_name', 'last_name', 'password1', 'password2')}),
    )
    search_fields = ['first_name', 'last_name', 'phone_number']
    readonly_fields = ['last_login', 'created', 'updated']
    ordering = ('-created',)

    def get_queryset(self, request):
        qs = self.model._default_manager.filter(is_superuser=False, is_staff=False)
        ordering = self.get_ordering(request)
        if ordering:
            qs.order_by(*ordering)
        return qs


@admin.register(AdminUser)
class AdminUserAdmin(CustomUserAdmin):
    def get_queryset(self, request):
        qs = self.model._default_manager.filter(is_superuser=True, is_staff=True)
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs
