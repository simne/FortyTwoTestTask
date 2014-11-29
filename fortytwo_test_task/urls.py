from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from apps.hello import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    url(r'^$', views.index, name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', views.index, name='home'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

