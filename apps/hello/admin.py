from django.contrib import admin

# Register your models here.
from hello.models import Developer, MHttpRequest
admin.site.register(Developer)
admin.site.register(MHttpRequest)
