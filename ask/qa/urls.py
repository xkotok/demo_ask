from django.conf.urls import patterns, url
#,include

from django.contrib import admin
admin.autodiscover()
from qa.views import index, question,  ask
urlpatterns = patterns('qa.views',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/', 'test', name='login'),
    url(r'^signup/', 'test', name='signup'),
    url(r'^ask/', ask, name='ask'),
    url(r'^question/(?P<id_s>\d+)/$', question, name='question'),
    url(r'^popular/', index, name='popular'),
    url(r'^new/', 'test', name='new'),
    url(r'^answer/', 'answer'), 
    url(r'^$', index, name='index'),

)
