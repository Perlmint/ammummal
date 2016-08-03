# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from bs4 import BeautifulSoup
from rest_framework.test import APITestCase
from django.core.urlresolvers import reverse
from web.views import pull


class HomeTest(APITestCase):

    def test_home(self):
        response = self.client.get(reverse('web:home'))
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(soup.is_empty_element, False)

    def test_pull(self):
        self.assertEqual("암움알", pull("아무말"))
        self.assertEqual("닭을악", pull("달그락"))
