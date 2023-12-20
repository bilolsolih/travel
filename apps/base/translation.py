from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from .models import City, Country, Region


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ['title']


@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ['title']
@register(Region)
class RegionTranslationOptions(TranslationOptions):
    fields = ['title']