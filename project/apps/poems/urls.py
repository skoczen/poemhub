from django.conf.urls.defaults import patterns, include, url
import dselector
parser = dselector.Parser()
url = parser.url

from poems import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^my-writing/?$', views.my_writing, name='my_writing'),
    url(r'^{poet:slug}$', views.poet, name='poet'),
    url(r'^{poet:slug}/{title:slug}/revisions/?$', views.revisions, name='revisions'),
    # url(r'^{poet:slug}/{title:slug}/revision/{revision_umb?$', views.revisions, name='revisions'),

    url(r'^{poet:slug}/{title:slug}/?$', views.poem, name='poem'),
)
