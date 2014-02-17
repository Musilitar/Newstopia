from django.conf.urls import patterns, include, url
from django.contrib import admin
from polls import views

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
                       url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
                       url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
                       )


