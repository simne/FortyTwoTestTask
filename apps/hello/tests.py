from django.test import TestCase

# Create your tests here.

import datetime

from random import randint
from hello.models import MHttpRequest

class SomeTests(TestCase):
    fixtures = ['test001.json']

    def test_t1_show_contacts_on_main_page(self):
        response = self.client.get('/')
        self.assertEqual(response.context['name'], 'Serge')
        self.assertEqual(response.context['last_name'], 'Sergeev')
        self.assertEqual(response.context['date_of_birth'],
                         datetime.date(1976, 1, 31))
        self.assertEqual(response.context['bio'], 'Test bio')
        self.assertEqual(response.context['email'], 'simne@github.com')
        self.assertEqual(response.context['jabber'], 'simne@jabber.ru')
        self.assertEqual(response.context['skype'], 'simne100')
        self.assertEqual(response.context['other_contacts'],
                         'Other contacts test')

    def test_t2_store_http_reqs(self):
        murl = "/%d" % randint(1000000,9000000)
        response = self.client.get(murl)
        # mm = MHttpRequest.objects.create(meta_QUERY_STRING=murl, meta_CONTENT_LENGTH = 10)
        # mm.save
        objs = MHttpRequest.objects.order_by('-rqdate')[0]
        # print objs.meta_QUERY_STRING
        self.assertEqual(objs.meta_QUERY_STRING, murl)
