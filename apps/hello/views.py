from django.shortcuts import render

# Create your views here.

from .models import Developer

from django.http import HttpResponse
from django.template import loader, Context


def index(request):
    response = HttpResponse()
    s1 = Developer.objects.get(id=1)
    t = loader.get_template('hello/index.html')
    c = Context({
        'name': s1.name,
        'last_name': s1.last_name,
        'date_of_birth': s1.date_of_birth,
        'bio': s1.bio,
        'email': s1.email,
        'jabber': s1.jabber,
        'skype': s1.skype,
        'other_contacts': s1.other_contacts,
    })

    response.write(t.render(c))
    return response
