from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from .models import PopularPlace


@register(PopularPlace)
class PopularPlaceTranslationOptions(TranslationOptions):
    fields = ['title', 'description']
