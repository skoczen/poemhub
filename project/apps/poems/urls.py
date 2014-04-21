from django.conf.urls.defaults import patterns, include, url
import dselector
parser = dselector.Parser()
url = parser.url

from poems import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^explore/?$', views.explore, name='explore'),
    url(r'^my-writing/?$', views.my_writing, name='my_writing'),
    url(r'^new-poem$', views.new, name='new'),
    url(r'^save/{poet:slug}/{title:slug}/?$', views.save_revision, name='save_revision'),

    url(r'^{poet:slug}/{title:slug}/revisions/?$', views.revisions, name='revisions'),
    url(r'^{poet:slug}/revision/{pk:digits}/?$', views.revision, name='revision'),
    url(r'^{poet:slug}/?$', views.poet, name='poet'),

    # url(r'^{poet:slug}/{title:slug}/revision/{revision_umb?$', views.revisions, name='revisions'),

    url(r'^{poet:slug}/{title:slug}/?$', views.poem, name='poem'),
    
)
