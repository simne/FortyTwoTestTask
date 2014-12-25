from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from apps.hello import views

from django.conf import settings
from django.conf.urls.static import static

# from django.views.generic import ListView
from apps.hello import models as hmodels
from hello.models import MHttpRequest
from hello.views import ReqList

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    url(r'^$', views.index, name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', views.index, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^list/', ListView.as_view(
    #  queryset = hmodels.MHttpRequest.objects.all(),
    #  context_object_name='latest_poll_list', template_name='base.html',
    #  paginate_by=25 ), name='blog'),
    # url(r'^list2/', ListView.as_view(
    #  queryset = hmodels.Developer.objects.all(),
    #  context_object_name='latest_poll_list', template_name='base.html' ,
    #  paginate_by=25 ), name='blog2'),
    url(r'^list2/', ReqList.as_view(), name='list2'),
    # url(r'^contact/', include('contact.urls')),
    url(r'^fuploads/', include('hello.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
