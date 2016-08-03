# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'', include('web.urls', namespace='web', app_name='web')),
]
