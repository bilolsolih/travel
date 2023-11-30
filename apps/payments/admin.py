from django.contrib import admin

from apps.base.second_admin import second_admin
from .models import Category, Payment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id']
    list_editable = ['title']
    search_fields = ['title']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'payer', 'payee', 'responsible', 'amount']
    list_display_links = ['id', 'payer', 'payee']
    search_fields = ['payee', 'payer', 'responsible']

    def save_model(self, request, obj, form, change):
        obj.responsible = request.user
        obj.save()
        super().save_model(request, obj, form, change)


second_admin.register(Payment, PaymentAdmin)
