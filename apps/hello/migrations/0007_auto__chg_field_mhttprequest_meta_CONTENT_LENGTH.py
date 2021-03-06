# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'MHttpRequest.meta_CONTENT_LENGTH'
        db.alter_column(u'hello_mhttprequest', 'meta_CONTENT_LENGTH', self.gf('django.db.models.fields.CharField')(default=0, max_length=128))

    def backwards(self, orm):

        # Changing field 'MHttpRequest.meta_CONTENT_LENGTH'
        db.alter_column(u'hello_mhttprequest', 'meta_CONTENT_LENGTH', self.gf('django.db.models.fields.IntegerField')(null=True))

    models = {
        u'hello.developer': {
            'Meta': {'object_name': 'Developer'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'hello.mhttprequest': {
            'Meta': {'object_name': 'MHttpRequest'},
            'cookies': ('django.db.models.fields.TextField', [], {}),
            'files': ('django.db.models.fields.TextField', [], {}),
            'get': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_CONTENT_LENGTH': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'meta_CONTENT_TYPE': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'meta_HTTP_ACCEPT_ENCODING': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'meta_HTTP_ACCEPT_LANGUAGE': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'meta_HTTP_HOST': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'meta_HTTP_REFERER': ('django.db.models.fields.TextField', [], {}),
            'meta_HTTP_USER_AGENT': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'meta_PATH_INFO': ('django.db.models.fields.TextField', [], {}),
            'meta_QUERY_STRING': ('django.db.models.fields.TextField', [], {}),
            'meta_REMOTE_ADDR': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'meta_REMOTE_HOST': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'meta_REMOTE_USER': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'meta_REQUEST_METHOD': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'meta_SERVER_NAME': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'meta_SERVER_PORT': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'post': ('django.db.models.fields.TextField', [], {}),
            'rqdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['hello']