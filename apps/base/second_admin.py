from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class SecondAdmin(admin.AdminSite):
    site_header = _('AirTravels Administration')
    site_title = _('AirTravels Admin site')
    index_title = _('AirTravels Admin home')


second_admin = SecondAdmin(name='second_admin')