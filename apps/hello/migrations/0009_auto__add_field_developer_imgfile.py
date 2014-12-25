# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Developer.imgfile'
        db.add_column(u'hello_developer', 'imgfile',
                      self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Developer.imgfile'
        db.delete_column(u'hello_developer', 'imgfile')


    models = {
        u'hello.developer': {
            'Meta': {'object_name': 'Developer'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imgfile': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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
            'rqdate': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'rqdump': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['hello']