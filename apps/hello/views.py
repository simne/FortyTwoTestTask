from django.shortcuts import render

# Create your views here.

from .models import Developer

def index(request):
    response = HttpResponse()
    t = loader.get_template('hello/index.html')
    c = Context({
        'name': 'Serge',
    })

    response.write(t.render(c))
    return response

