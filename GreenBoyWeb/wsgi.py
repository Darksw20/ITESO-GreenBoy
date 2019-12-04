"""
WSGI config for GreenBoyWeb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


os.environ["PROXIES"] = "192.168.43.140:8000"

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GreenBoyWeb.settings')

application = get_wsgi_application()
