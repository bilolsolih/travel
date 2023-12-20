from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from .models import FrequentlyAskedQuestion, TermsAndConditions

@register(FrequentlyAskedQuestion)
class FrequentlyAskedQuestionTranslationOptions(TranslationOptions):
    fields = ['question', 'answer']

@register(TermsAndConditions)
class TermsAndConditionsTranslationOptions(TranslationOptions):
    fields = ['terms']