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

