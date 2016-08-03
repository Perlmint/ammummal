# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import random
import hashlib

from django.utils import timezone


def get_now():
    return timezone.now()


def sha1(value):
    return hashlib.sha1(unicode(value).encode('utf-8')).hexdigest()


def generate_token():
    return sha1(str(random.random()))
