from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from apps.hello import views


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    url(r'^$', views.index, name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', views.index, name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
