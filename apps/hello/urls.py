# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('hello.views',
    url(r'^', 'fupload', name='fupload'),
)
