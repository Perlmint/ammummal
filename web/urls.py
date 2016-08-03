# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from django.conf.urls import include, url
from web import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
]
