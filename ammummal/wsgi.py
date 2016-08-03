# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

PROJECT_NAME = os.path.dirname(os.path.abspath(__file__)).split('/')[-1]
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{}.settings'.format(PROJECT_NAME))

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
