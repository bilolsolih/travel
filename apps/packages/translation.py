from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from .models import Package, Plan, PlanType, PackageFeature, Activity


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
