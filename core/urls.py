from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from .drf_schemas import swagger_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include('apps.accounts.urls', namespace='accounts')),
    path('api/v1/packages/', include('apps.packages.urls', namespace='packages')),
    path('api/v1/orders/', include('apps.orders.urls', namespace='orders')),
]

urlpatterns += swagger_patterns

if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls'))
    ]
