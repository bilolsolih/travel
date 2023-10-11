from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TravelsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.travels'
    verbose_name = _('Travels')
