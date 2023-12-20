from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Discount


@admin.register(Discount)
class DiscountAdmin(TranslationAdmin):
    list_display = ['id', 'title']
# Register your models here.
