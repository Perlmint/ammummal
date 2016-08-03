# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import os

from fabric.api import *
from fabric.colors import *
from ammummal import settings

MANAGE_FILE_PATH = os.path.join(settings.BASE_DIR, 'manage.py')
REQUIREMENTS_FILE_PATH = os.path.join(settings.BASE_DIR, 'requirements.txt')


def status():
    local('git status')


def freeze():
    print(blue("freezing python packages"))
    local('pip freeze > {}'.format(REQUIREMENTS_FILE_PATH))


def update():
    print(blue("updating python packages"))
    local('pip freeze --local | grep -v "^\-e" | cut -d = -f 1 | xargs pip install -U')


def start():
    print(blue("starting server"))
    local('heroku local')


def reload():
    print(blue("reloading server"))
    local('heroku local')


def test():
    print(blue("testing"))
    print(red("stay determined".upper()))
    local('python {} test'.format(MANAGE_FILE_PATH))


def ready():
    print(green("Are you ready? It's okay if you're not. I'm not ready either."))
    local('python {} migrate'.format(MANAGE_FILE_PATH))
    local('pip install -r {}'.format(REQUIREMENTS_FILE_PATH))


def collect():
    print(blue("collecting static"))
    local('python {} collectstatic --noinput'.format(MANAGE_FILE_PATH))


def deploy(target='local'):
    print(yellow("starting deployment"))
    ready()
    collect()
    test()
    if target == 'local':
        local('heroku local')
    elif target == 'heroku':
        local('git push heroku master')
        local('heroku run python manage.py migrate')
