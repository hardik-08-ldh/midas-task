# default django settings
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'midas.settings')

application = get_wsgi_application()
