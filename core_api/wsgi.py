import os

from decouple import config as env
from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", f"core_api.settings.{env('ENVIRONMENT')}"
)

application = get_wsgi_application()
