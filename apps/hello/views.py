# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

from .models import Developer, MHttpRequest

from django.http import HttpResponse
from django.template import loader, Context

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


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

from django.shortcuts import get_object_or_404
from django.views.generic import ListView


class ReqList(ListView):
    model = MHttpRequest
    template_name = 'hello/list.html'

    def get_queryset(self):
        return MHttpRequest.objects.all().order_by('-rqdate')[0:10]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ReqList, self).get_context_data(**kwargs)
        # Add in the publisher
        context['publisher'] = 'Serge'
        return context

from .forms import DocumentForm

def fupload(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Developer.objects.get(id=1)
            print newdoc.imgfile
            # Developer(imgfile = request.FILES['imgfile'])
            newdoc.imgfile=request.FILES['imgfile']
            print request.FILES['imgfile']
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('hello.views.fupload'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    developers = Developer.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list2.html',
        {'developers': developers, 'form': form},
        context_instance=RequestContext(request)
    )
