from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from .models import Package, Plan, PlanType, PackageFeature, Activity, AccommodationFeature, Accommodation


@register(Accommodation)
class AccommodationTranslationOptions(TranslationOptions):
    fields = ['title', 'short_description', 'long_description']


@register(AccommodationFeature)
class AccommodationFeatureTranslationOptions(TranslationOptions):
    fields = ['title', 'description']


@register(Package)
class PackageTranslation(TranslationOptions):
    fields = ['title', 'description']


@register(PlanType)
class PlanTypeTranslation(TranslationOptions):
    fields = ['title']


@register(Plan)
class PlanTranslation(TranslationOptions):
    fields = ['description']


@register(PackageFeature)
class PlanFeatureTranslation(TranslationOptions):
    fields = ['title', 'description']


@register(Activity)
class ActivityTranslation(TranslationOptions):
    fields = ['title', 'address', 'landmark', 'description']
