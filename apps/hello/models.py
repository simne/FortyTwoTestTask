from django.db import models

# Create your models here.


class Developer(models.Model):
    name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    date_of_birth = models.DateField()
    bio = models.TextField()
    email = models.EmailField()
    jabber = models.EmailField()
    skype = models.CharField(max_length=128)
    other_contacts = models.TextField()


class MHttpRequest (models.Model):
    get = models.TextField()
    post = models.TextField()
    cookies = models.TextField()
    files = models.TextField()
    meta_CONTENT_LENGTH = models.CharField(max_length=128)
    meta_CONTENT_TYPE = models.CharField(max_length=128)
    meta_HTTP_ACCEPT_ENCODING = models.CharField(max_length=128)
    meta_HTTP_ACCEPT_LANGUAGE = models.CharField(max_length=128)
    meta_HTTP_HOST = models.CharField(max_length=128)
    meta_HTTP_REFERER = models.TextField()
    meta_HTTP_USER_AGENT = models.CharField(max_length=128)
    meta_QUERY_STRING = models.TextField()
    meta_PATH_INFO = models.TextField()
    meta_REMOTE_ADDR = models.CharField(max_length=128)
    meta_REMOTE_HOST = models.CharField(max_length=128)
    meta_REMOTE_USER = models.CharField(max_length=128)
    meta_REQUEST_METHOD = models.CharField(max_length=128)
    meta_SERVER_NAME = models.CharField(max_length=128)
    meta_SERVER_PORT = models.CharField(max_length=128)
    rqdate = models.DateTimeField(auto_now_add=True, blank=True)
    rqdump = models.TextField()
