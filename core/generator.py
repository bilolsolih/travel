from os import getenv

from dotenv import load_dotenv
from drf_yasg.generators import OpenAPISchemaGenerator

load_dotenv()

DJANGO_SETTINGS_MODULE = getenv('DJANGO_SETTINGS_MODULE')


class HttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        if DJANGO_SETTINGS_MODULE == 'core.settings.development':
            schema.schemes = ["http", "https"]
        elif DJANGO_SETTINGS_MODULE == 'core.settings.production':
            schema.schemes = ["https", "http"]
        return schema
