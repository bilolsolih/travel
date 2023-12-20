from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from .models import MainPagePictures


@register(MainPagePictures)
class MainPagePicturesTranslationOptions(TranslationOptions):
    fields = ['prompt']
