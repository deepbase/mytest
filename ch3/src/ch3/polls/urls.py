'''
Created on 2016. 8. 20.

@author: deepbase
'''

from django.conf.urls import url
from polls import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'ch3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
]