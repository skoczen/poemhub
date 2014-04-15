from django.conf.urls.defaults import patterns, include, url

from main_site import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^ui-mock$', views.ui_mock, name='ui_mock'),
    url(r'^detail-mock$', views.detail_mock, name='detail_mock'),
)
