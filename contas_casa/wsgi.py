"""
WSGI config for contas_casa project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'contas_casa.settings')


if os.environ.get('DJANGO_ENV') == 'production':
    app = get_wsgi_application()
else:
    application = get_wsgi_application()
