from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

from apps.base.second_admin import second_admin
from .drf_schemas import swagger_patterns

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('second_admin/', second_admin.urls),
    path('api/v1/base/', include('apps.base.urls', namespace='base')),
    path('api/v1/accounts/', include('apps.accounts.urls', namespace='accounts')),
    path('api/v1/packages/', include('apps.packages.urls', namespace='packages')),
    path('api/v1/orders/', include('apps.orders.urls', namespace='orders')),
    path('api/v1/gallery/', include('apps.gallery.urls', namespace='gallery')),
    path('api/v1/payments/', include('apps.payments.urls', namespace='payments')),
    path('api/v1/places/', include('apps.places.urls', namespace='places')),
    path('api/v1/discounts/', include('apps.discounts.urls', namespace='discounts')),
    path('api/v1/about/', include('apps.about.urls', namespace='about')),
    path('api/v1/firebase/', include('apps.firebase.urls', namespace='firebase')),
    path('api/v1/notifications/', include('apps.notifications.urls', namespace='notifications')),
)

urlpatterns += swagger_patterns

# if settings.DEBUG:
#     urlpatterns += [
#         path('__debug__/', include('debug_toolbar.urls')),
#     ]
