from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from .models import Discount


@register(Discount)
class DiscountTranslationOptions(TranslationOptions):
    fields = ['title']
