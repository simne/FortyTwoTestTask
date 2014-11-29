# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HttpRequest'
        db.create_table(u'hello_httprequest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('get', self.gf('django.db.models.fields.TextField')()),
            ('post', self.gf('django.db.models.fields.TextField')()),
            ('cookies', self.gf('django.db.models.fields.TextField')()),
            ('files', self.gf('django.db.models.fields.TextField')()),
            ('meta_CONTENT_LENGTH', self.gf('django.db.models.fields.IntegerField')()),
            ('meta_CONTENT_TYPE', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('meta_HTTP_ACCEPT_ENCODING', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('meta_HTTP_ACCEPT_LANGUAGE', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('meta_HTTP_HOST', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('meta_HTTP_REFERER', self.gf('django.db.models.fields.TextField')()),
            ('meta_HTTP_USER_AGENT', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('meta_QUERY_STRING', self.gf('django.db.models.fields.TextField')()),
            ('meta_REMOTE_ADDR', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('meta_REMOTE_HOST', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('meta_REMOTE_USER', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('meta_REQUEST_METHOD', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('meta_SERVER_NAME', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('meta_SERVER_PORT', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'hello', ['HttpRequest'])


    def backwards(self, orm):
        # Deleting model 'HttpRequest'
        db.delete_table(u'hello_httprequest')


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
        u'hello.httprequest': {
            'Meta': {'object_name': 'HttpRequest'},
            'cookies': ('django.db.models.fields.TextField', [], {}),
            'files': ('django.db.models.fields.TextField', [], {}),
            'get': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_CONTENT_LENGTH': ('django.db.models.fields.IntegerField', [], {}),
            'meta_CONTENT_TYPE': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'meta_HTTP_ACCEPT_ENCODING': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'meta_HTTP_ACCEPT_LANGUAGE': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'meta_HTTP_HOST': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'meta_HTTP_REFERER': ('django.db.models.fields.TextField', [], {}),
            'meta_HTTP_USER_AGENT': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'meta_QUERY_STRING': ('django.db.models.fields.TextField', [], {}),
            'meta_REMOTE_ADDR': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'meta_REMOTE_HOST': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'meta_REMOTE_USER': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'meta_REQUEST_METHOD': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'meta_SERVER_NAME': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'meta_SERVER_PORT': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'post': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['hello']