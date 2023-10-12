from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AccommodationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.accommodations'
    verbose_name = _('Accommodations')
