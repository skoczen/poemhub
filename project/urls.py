from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('main_site.urls', namespace="main_site", app_name="main_site")),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'administration/', include(admin.site.urls), name="admin"),


    url(r'^fonts/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': "%s/main_site/fonts" % settings.STATIC_ROOT,
    }),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
    }),
)
