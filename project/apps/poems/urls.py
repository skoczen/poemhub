from django.conf.urls.defaults import patterns, include, url
import dselector
parser = dselector.Parser()
url = parser.url

from poems import views

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^explore/?$', views.explore, name='explore'),
    url(r'^my-writing/?$', views.my_writing, name='my_writing'),
    url(r'^my-reading/?$', views.my_reading, name='my_reading'),
    url(r'^my-account/?$', views.my_account, name='my_account'),
    url(r'^my-backups/?$', views.my_backups, name='my_backups'),
    url(r'^premium/?$', views.premium, name='premium'),
    url(r'^generate-backup/?$', views.generate_backup, name='generate_backup'),
    url(r'^new-poem$', views.new, name='new'),
    url(r'^save/{poet:slug}/{title:slug}/?$', views.save_revision, name='save_revision'),
    url(r'^fantastic/{poem_id:digits}/?$', views.this_was_fantastic, name='this_was_fantastic'),
    url(r'^read/{poem_id:digits}/?$', views.mark_read, name='mark_read'),

    url(r'^{poet:slug}/{title:slug}/revisions/?$', views.revisions, name='revisions'),
    url(r'^{poet:slug}/revision/{pk:digits}/?$', views.revision, name='revision'),
    url(r'^{poet:slug}/?$', views.poet, name='poet'),

    # url(r'^{poet:slug}/{title:slug}/revision/{revision_umb?$', views.revisions, name='revisions'),

    url(r'^{poet:slug}/{title:slug}/?$', views.poem, name='poem'),
)
